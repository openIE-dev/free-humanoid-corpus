#!/usr/bin/env python3
"""lookup.py — patent-claim prior-art analyzer.

Given a claim phrase (or a free-form description of subject matter),
returns ranked corpus entries that disclose the matching subsystems,
in chronological order. The earliest disclosure with a tag match is
the strongest 102 prior art candidate.

Usage:
    python3 tools/lookup.py "harmonic drive reducer with output torque sensor"
    python3 tools/lookup.py "cycloidal reducer" --before 2015 --limit 5
    python3 tools/lookup.py "ZMP balancing" --commons-only
    python3 tools/lookup.py --tag actuator-electric-harmonic-drive

Ranking: tag matches (high weight) > prior_art_notes / details (medium)
> name / aliases (low). Ties broken by earlier disclosure date wins.

Output: per match, shows id, name, year, ip status, and the matched tags.
Pipe to less, grep, or jq-like filters to subset further.
"""
import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).parent.parent
CORPUS = ROOT / "corpus.jsonl"

# Map common claim-language phrases / tokens onto subsystem tags.
# Each value is a tag from the corpus's disclosed_subsystems taxonomy.
# Keep these phrases conservative — if the claim says "harmonic drive",
# almost certainly hits actuator-electric-harmonic-drive. If it says
# "actuator", that's too generic to map.
TAG_KEYWORDS = {
    # actuators
    "harmonic drive": "actuator-electric-harmonic-drive",
    "harmonic gear": "actuator-electric-harmonic-drive",
    "strain wave": "actuator-electric-harmonic-drive",
    "cycloidal": "actuator-electric-cycloidal",
    "cycloid reducer": "actuator-electric-cycloidal",
    "planetary gear": "actuator-electric-planetary",
    "planetary reducer": "actuator-electric-planetary",
    "quasi-direct-drive": "actuator-electric-quasi-direct-drive",
    "qdd": "actuator-electric-quasi-direct-drive",
    "quasi direct drive": "actuator-electric-quasi-direct-drive",
    "direct-drive": "actuator-electric-direct-drive",
    "direct drive": "actuator-electric-direct-drive",
    "series elastic": "actuator-electric-series-elastic",
    "sea actuator": "actuator-electric-series-elastic",
    "tendon-driven": "actuator-electric-tendon-driven",
    "tendon driven": "actuator-electric-tendon-driven",
    "cable-driven": "actuator-electric-tendon-driven",
    "spherical actuator": "actuator-spherical-multi-dof",
    "multi-dof actuator": "actuator-spherical-multi-dof",
    "hydraulic actuator": "actuator-hydraulic",
    "hydraulic": "actuator-hydraulic",
    "pneumatic muscle": "actuator-pneumatic-muscle",
    "mckibben": "actuator-pneumatic-muscle",
    "bldc controller": "actuator-bldc-controller",
    "brushless motor controller": "actuator-bldc-controller",
    "foc controller": "actuator-foc-controller",
    "field-oriented control": "actuator-foc-controller",
    # mechanism / morphology
    "anthropomorphic hand": "mechanism-anthropomorphic-hand",
    "robot hand": "mechanism-anthropomorphic-hand",
    "five-fingered hand": "mechanism-anthropomorphic-hand",
    "tendon routing": "mechanism-tendon-routing",
    "underactuated grasp": "mechanism-underactuated-grasping",
    "underactuated": "mechanism-underactuated-grasping",
    "passive dynamic": "mechanism-passive-dynamic-walking",
    "passive walker": "mechanism-passive-dynamic-walking",
    "bipedal locomotion": "mechanism-bipedal-locomotion",
    "biped": "mechanism-bipedal-locomotion",
    "bipedal walking": "mechanism-bipedal-locomotion",
    "humanoid walking": "mechanism-bipedal-locomotion",
    "quadrupedal locomotion": "mechanism-quadrupedal-locomotion",
    "quadruped": "mechanism-quadrupedal-locomotion",
    "wheel-leg": "mechanism-wheel-leg-hybrid",
    "wheel leg hybrid": "mechanism-wheel-leg-hybrid",
    "wheeled balancing": "mechanism-wheeled-balancing",
    "self-balancing wheeled": "mechanism-wheeled-balancing",
    # control
    "zmp": "control-zmp-balancing",
    "zero moment point": "control-zmp-balancing",
    "model predictive": "control-mpc",
    "mpc": "control-mpc",
    "reduced-order model": "control-reduced-order-model",
    "spring-loaded inverted pendulum": "control-reduced-order-model",
    "slip model": "control-reduced-order-model",
    "centroidal dynamics": "control-reduced-order-model",
    "rl policy": "control-rl-policy",
    "reinforcement learning": "control-rl-policy",
    "sim-to-real": "control-sim-to-real",
    "domain randomization": "control-sim-to-real",
    "teleoperation": "control-teleoperation",
    "teleop": "control-teleoperation",
    "vision-language-action": "control-vla-vision-language-action",
    "vla model": "control-vla-vision-language-action",
    "behavior tree": "control-behavior-tree",
    # safety
    "safety supervisor": "safety-hard-constraint",
    "hard constraint": "safety-hard-constraint",
    "control barrier": "safety-hard-constraint",
    "safety filter": "safety-hard-constraint",
    "simplex": "safety-simplex-supervisor",
    "simplex architecture": "safety-simplex-supervisor",
    "shielded rl": "safety-hard-constraint",
    # sensing
    "imu": "sensing-imu",
    "inertial measurement": "sensing-imu",
    "lidar": "sensing-lidar",
    "stereo camera": "sensing-stereo-camera",
    "monocular depth": "sensing-monocular-depth",
    "force-torque sensor": "sensing-force-torque",
    "force torque sensor": "sensing-force-torque",
    "force/torque sensor": "sensing-force-torque",
    "tactile fingertip": "sensing-tactile-fingertip",
    "tactile sensor": "sensing-tactile-fingertip",
    "whole-body tactile": "sensing-tactile-whole-body",
    "proprioceptive actuator": "sensing-proprioceptive-actuator",
    "torque sensing actuator": "sensing-proprioceptive-actuator",
    # power
    "fuel cell": "power-fuel-cell",
    "hot-swap battery": "power-hot-swap",
    "hot swap battery": "power-hot-swap",
    "li-ion": "power-li-ion",
    "lithium-ion": "power-li-ion",
    "li-po": "power-li-po",
    "lithium polymer": "power-li-po",
    "tethered power": "power-tethered",
    # software
    "ros 2": "software-ros2",
    "ros2": "software-ros2",
    "ros 1": "software-ros1",
    "ros1": "software-ros1",
    "rosp": "software-ros1",
    "openhrp": "software-openhrp",
    "yarp": "software-yarp",
    "mjbots": "software-mjbots-stack",
    "moteus": "software-mjbots-stack",
}


def load_corpus():
    return [json.loads(l) for l in CORPUS.read_text().splitlines() if l.strip()]


def tags_from_claim(claim: str) -> dict:
    """Map a claim string to {tag: number_of_phrase_hits}.

    Longer phrases match before shorter ones (greedy), so "harmonic drive"
    is preferred over a hypothetical bare "drive" key.
    """
    text = " " + claim.lower() + " "
    text = re.sub(r"[\(\)\.,;:/]", " ", text)
    hits = defaultdict(int)
    matched_spans = []
    # sort phrases by length desc so longer matches come first
    phrases = sorted(TAG_KEYWORDS.keys(), key=len, reverse=True)
    for phrase in phrases:
        idx = 0
        while True:
            i = text.find(" " + phrase + " ", idx) if " " in phrase else text.find(phrase, idx)
            if i == -1:
                break
            # avoid double-matching the same span across overlapping phrases
            if any(s <= i < e or s < i + len(phrase) <= e for s, e in matched_spans):
                idx = i + 1
                continue
            hits[TAG_KEYWORDS[phrase]] += 1
            matched_spans.append((i, i + len(phrase)))
            idx = i + len(phrase)
    return dict(hits)


def score_entry(entry: dict, tag_hits: dict, claim_lower: str) -> tuple:
    """Return a (score, tiebreaker) tuple. Higher score = better match.
    Tiebreaker is negative year so earlier disclosures rank higher on ties.
    """
    score = 0
    matched_tags = set()
    for t in entry.get("disclosed_subsystems") or []:
        if t in tag_hits:
            score += 10 * tag_hits[t]
            matched_tags.add(t)
    fields = [
        entry.get("prior_art_notes"),
        entry.get("actuator_details"),
        entry.get("control_architecture"),
        entry.get("sensing"),
        entry.get("end_effector"),
    ]
    for f in fields:
        if not f:
            continue
        f_lower = f.lower()
        for term in claim_lower.split():
            if len(term) >= 4 and term in f_lower:
                score += 1
    name_lower = (entry.get("canonical_name") or "").lower()
    aliases = " ".join(entry.get("aliases") or []).lower()
    for term in claim_lower.split():
        if len(term) >= 4 and (term in name_lower or term in aliases):
            score += 1
    year_str = (entry.get("first_disclosure_date") or "")[:4]
    try:
        year = int(year_str)
    except ValueError:
        year = 9999
    return score, -year, matched_tags


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("claim", nargs="*", help="claim phrase or free-form description")
    p.add_argument("--tag", action="append", default=[], help="explicit tag(s) to look up; repeatable")
    p.add_argument("--before", type=int, help="only entries disclosed before this year")
    p.add_argument("--after", type=int, help="only entries disclosed after this year")
    p.add_argument("--commons-only", action="store_true", help="exclude draft entries")
    p.add_argument("--limit", type=int, default=15, help="max results to print (default 15)")
    p.add_argument("--json", action="store_true", help="output JSON instead of text")
    args = p.parse_args()

    if not args.claim and not args.tag:
        p.error("provide a claim phrase or --tag <tag>")

    claim = " ".join(args.claim)
    tag_hits = tags_from_claim(claim) if claim else {}
    for t in args.tag:
        tag_hits[t] = tag_hits.get(t, 0) + 1

    if not tag_hits and claim:
        # No tag mapped — fall back to free-text search across notes.
        pass

    entries = load_corpus()
    scored = []
    for e in entries:
        if args.commons_only and e.get("draft"):
            continue
        year_str = (e.get("first_disclosure_date") or "")[:4]
        try:
            year = int(year_str)
        except ValueError:
            year = None
        if args.before is not None and (year is None or year >= args.before):
            continue
        if args.after is not None and (year is None or year <= args.after):
            continue
        s, neg_year, matched_tags = score_entry(e, tag_hits, claim.lower())
        if s > 0:
            scored.append((s, neg_year, matched_tags, e))
    scored.sort(key=lambda x: (-x[0], x[1]))

    if args.json:
        print(json.dumps([
            {
                "id": e["id"],
                "canonical_name": e["canonical_name"],
                "year": (e.get("first_disclosure_date") or "")[:4],
                "corpus": e["corpus"],
                "ip_status": e.get("ip_status"),
                "draft": bool(e.get("draft")),
                "score": s,
                "matched_tags": sorted(mt),
                "disclosure_citation": e.get("disclosure_citation"),
                "prior_art_notes": e.get("prior_art_notes"),
            }
            for s, _, mt, e in scored[:args.limit]
        ], indent=2, ensure_ascii=False))
        return

    if claim:
        print(f"Claim: {claim}")
    if tag_hits:
        print("Mapped tags:")
        for t, n in sorted(tag_hits.items(), key=lambda x: -x[1]):
            print(f"  {t} ×{n}")
    else:
        print("(no tag mapped from claim — see TAG_KEYWORDS in lookup.py to extend)")
    print()
    if not scored:
        print("No matching entries.")
        return
    print(f"Top {min(args.limit, len(scored))} of {len(scored)} matches (chronological tiebreak: earlier wins):")
    print("-" * 72)
    for s, _, mt, e in scored[:args.limit]:
        year = (e.get("first_disclosure_date") or "?")[:4]
        draft = " (draft)" if e.get("draft") else ""
        print(f"  {year}  {e['canonical_name']:<45.45} score={s} {e.get('ip_status', '?'):<14} {e['id']}{draft}")
        if mt:
            print(f"        tags: {', '.join(sorted(mt))}")
        if e.get("disclosure_citation"):
            cite = e["disclosure_citation"]
            if len(cite) > 200:
                cite = cite[:200] + "…"
            print(f"        cite: {cite}")
        print()


if __name__ == "__main__":
    main()
