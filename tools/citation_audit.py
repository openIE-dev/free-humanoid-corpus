#!/usr/bin/env python3
"""citation_audit.py — find systems cited in prior_art_notes that don't exist as corpus entries.

The corpus is only as strong as its citation chains. When a prior_art_notes
field references "RT-2" or "π₀" or "Mobile ALOHA" but no corpus entry has
those names, the chain is fictional — it cites prior art that, from the
corpus's perspective, doesn't exist.

This script reads corpus.jsonl, builds a name index from every entry's
id + canonical_name + aliases, then scans every entry's prior_art_notes
(plus disclosure_citation, notes, control_architecture, actuator_details
for completeness) for known system names. Any name that's cited but
doesn't resolve to an entry is reported, ranked by citation count.

Usage:
    python3 tools/citation_audit.py [corpus.jsonl]

Output: ranked list of unresolved citations, suitable for driving a
backfill round.
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Curated list of system / paper names commonly cited in robotic prior art.
# Each entry is a tuple (canonical_match_string, [aliases]). The canonical
# is the form that appears in the report; aliases are alternative spellings
# that should also count as a match. All matching is case-insensitive and
# tolerates standard punctuation variants (hyphen/space).
#
# Adding a name here means: "this is a real system or paper that some
# prior_art_notes might cite; if it's cited but missing from the corpus,
# flag it." Names already in the corpus will resolve and be silently
# ignored.
KNOWN_SYSTEMS: list[tuple[str, list[str]]] = [
    # === VLA / foundation policies ===
    ("RT-1",                        ["RT 1"]),
    ("RT-2",                        ["RT 2"]),
    ("RT-X",                        ["RT X"]),
    ("Open X-Embodiment",           ["Open-X-Embodiment", "OpenX-Embodiment", "OpenX"]),
    ("OpenVLA",                     []),
    ("OpenVLA-OFT",                 ["OpenVLA OFT"]),
    ("SayCan",                      ["Say-Can", "Do As I Can"]),
    ("PaLM-E",                      ["PaLM E"]),
    ("RoboCat",                     []),
    ("Gato",                        []),  # likely false-positive risk; tighten word boundary
    ("π₀",                          ["pi0", "pi-zero", "pi-0"]),
    ("π₀.₅",                        ["pi0.5", "pi-0.5", "pi05"]),
    ("RDT-1B",                      ["RDT 1B"]),
    ("GR00T N1",                    ["GR00T-N1", "GR00T"]),
    ("Diffusion Policy",            ["Diffusion-Policy"]),
    ("ACT",                         []),  # word-boundary risk
    ("ALOHA",                       []),
    ("Mobile ALOHA",                ["Mobile-ALOHA"]),
    ("Aloha 2",                     ["ALOHA-2"]),
    # === SLAM / perception ===
    ("RAFT",                        []),  # word-boundary risk
    ("DROID-SLAM",                  ["DROID SLAM"]),
    ("ORB-SLAM3",                   ["ORB SLAM 3"]),
    ("ORB-SLAM2",                   ["ORB SLAM 2"]),
    ("ORB-SLAM",                    ["ORB SLAM"]),
    ("ViPE",                        []),  # case-sensitive, distinct from RADIO-ViPE
    ("RADIO-ViPE",                  ["RADIO ViPE"]),
    ("MegaSAM",                     ["Mega-SAM"]),
    ("DUSt3R",                      ["DUST3R"]),
    ("VGGT",                        []),
    ("Kimera",                      []),
    ("RVWO",                        []),
    ("RGBDS",                       []),
    ("BBQ",                         []),
    ("ConceptGraphs",               ["Concept-Graphs"]),
    ("HOV-SG",                      []),
    ("OpenScene",                   []),
    ("OpenMask3D",                  []),
    ("CLIO",                        []),
    ("OVO-SLAM",                    ["OVO SLAM"]),
    ("Rayfronts",                   ["RayFronts"]),
    ("Dyna-SLAM",                   ["DynaSLAM"]),
    ("DLD-SLAM",                    []),
    ("V3D-SLAM",                    []),
    ("DGS-SLAM",                    []),
    ("RoDyn-SLAM",                  []),
    ("DynaMON",                     []),
    ("WildGS-SLAM",                 ["Wild-GS-SLAM"]),
    ("LEG-SLAM",                    []),
    ("LEGO-SLAM",                   []),
    ("LEGS",                        []),
    ("LERF",                        []),
    ("OpenSplat3D",                 []),
    ("Online Language Splatting",   []),
    ("SemGauss-SLAM",               ["SemGauss SLAM"]),
    # === Foundation embeddings / vision-language ===
    ("CLIP",                        []),  # word-boundary risk
    ("SigLIP",                      []),
    ("DINOv2",                      ["DINO v2"]),
    ("DINO",                        []),  # word-boundary risk
    ("RADIO",                       []),  # NVIDIA RADIO; word-boundary risk
    ("LLaMA",                       ["Llama-2", "Llama 2", "Llama-3"]),
    # === Whole-body MPC / controllers ===
    ("Crocoddyl",                   []),
    ("OCS2",                        []),
    ("TSID",                        []),
    ("MOMA",                        []),
    # === Foundational humanoids / hardware ===
    ("Atlas",                       []),  # Boston Dynamics; word-boundary risk
    ("Spot",                        []),  # word-boundary risk
    ("Cassie",                      []),
    ("Digit",                       []),  # word-boundary risk
    ("HRP-2",                       ["HRP 2"]),
    ("HRP-4",                       ["HRP 4"]),
    ("HRP-5P",                      ["HRP 5P"]),
    ("Asimo",                       ["ASIMO"]),
    ("iCub",                        []),
    ("WALK-MAN",                    ["WALKMAN"]),
    ("Justin",                      []),
    ("DLR Justin",                  []),
    ("Toro",                        []),  # DLR
    ("HERB",                        []),  # CMU
    ("Romeo",                       []),  # Aldebaran/Softbank
    ("NAO",                         []),
    ("Pepper",                      []),
    ("PR2",                         []),
    # === Hands ===
    ("Shadow Hand",                 ["Shadow Dexterous Hand"]),
    ("DLR Hand-II",                 ["DLR Hand II", "DLR-Hand-II"]),
    ("DLR Hand-Arm System",         ["DLR Hand Arm"]),
    ("Pisa-IIT SoftHand",           ["Pisa/IIT SoftHand"]),
    ("Pisa-IIT SoftHand 2",         ["Pisa/IIT SoftHand 2"]),
    ("Tactile SoftHand-A",          []),
    ("Educational SoftHand-A",      []),
    ("InMoov",                      ["Inmoov"]),
    ("Reflex SF",                   ["ReFlex SF"]),
    ("Yale OpenHand",               ["Yale Open-Hand"]),
    ("Salisbury Stanford-JPL hand", ["Salisbury hand"]),
    # === Teleop / imitation learning ===
    ("DAgger",                      []),
    ("ALVINN",                      []),
    ("BRETT",                       []),
    ("Dactyl",                      []),  # OpenAI; word-boundary risk
    # === Sim / training ===
    ("MuJoCo",                      []),
    ("MJX",                         []),  # word-boundary risk
    ("Isaac Lab",                   ["Isaac-Lab"]),
    ("Isaac Gym",                   ["Isaac-Gym"]),
    ("Isaac Sim",                   ["Isaac-Sim"]),
    ("Drake",                       []),  # word-boundary risk; very common word
    ("Gazebo",                      []),
    ("LeRobot",                     ["Le-Robot", "Le Robot"]),
    ("Habitat",                     []),  # FAIR
    ("OmniGibson",                  []),
    ("iGibson",                     []),
    ("BEHAVIOR-1K",                 ["BEHAVIOR 1K"]),
    ("Stonefish",                   []),
    ("Genesis",                     []),  # GS sim, word-boundary risk
    # === Locomotion / quadruped (relevant for shielding) ===
    ("ANYmal",                      []),
    ("MIT Cheetah",                 []),
    ("MIT Cheetah 3",               []),
    ("Spot Mini",                   ["SpotMini"]),
    ("BigDog",                      ["Big Dog"]),
    ("LittleDog",                   ["Little Dog"]),
    # === Underwater ===
    ("Aquanaut",                    []),
    ("OceanOne",                    ["Ocean One"]),
    ("OceanOneK",                   ["Ocean OneK", "Ocean-OneK"]),
    ("Bluefin",                     []),
    ("REMUS",                       []),
    ("Slocum",                      []),
    ("Seaglider",                   []),
    ("Alvin",                       []),
    ("Jason",                       []),  # word-boundary risk; common name
    ("Nereus",                      []),
    # === Wheel-leg ===
    ("STAR",                        []),  # word-boundary risk; tighten
    ("RSTAR",                       []),
    ("TSTAR",                       []),
    ("FSTAR",                       []),
    ("FCSTAR",                      []),
    ("AmphiSTAR",                   []),
    ("DSTAR",                       []),
    ("FLORES",                      []),  # word-boundary risk
    # === Frameworks / Languages ===
    ("ROS 2",                       ["ROS2"]),
    ("ROS",                         []),
    ("CRoco-DDP",                   []),
    # === Recent commercial humanoids ===
    ("Tesla Optimus",               []),
    ("Optimus Gen 2",               []),
    ("Figure 01",                   []),
    ("Figure 02",                   []),
    ("1X NEO",                      ["NEO Beta"]),
    ("Apollo",                      []),  # Apptronik
    ("Apptronik Apollo",            []),
    ("Sanctuary Phoenix",           []),
    ("UBTECH Walker",               []),
    ("Unitree H1",                  []),
    ("Unitree G1",                  []),
    ("Boston Dynamics Atlas",       []),
    ("Honda ASIMO",                 []),
    ("Boston Dynamics",             []),  # the company
    ("Physical Intelligence",       []),  # the company
]


def normalize(name: str) -> str:
    """Lowercase and replace runs of non-alphanumerics with a single space."""
    n = name.lower()
    n = re.sub(r"[^a-z0-9π₀.₅]+", " ", n)
    n = re.sub(r"\s+", " ", n).strip()
    return n


def build_corpus_index(entries: list[dict]) -> dict[str, str]:
    """Map normalized name → entry id, drawn from each entry's id +
    canonical_name + aliases."""
    idx: dict[str, str] = {}
    for e in entries:
        names = [e["id"], e["canonical_name"], *e.get("aliases", [])]
        for name in names:
            n = normalize(name)
            if n and n not in idx:
                idx[n] = e["id"]
    return idx


# Names that genuinely have a high false-positive rate (common English
# words, ambiguous acronyms). For these, require a stricter context
# match — the word must appear in a recognizably-citation-y context
# (parens-and-year, "et al.", "X policy", "X model", "X system").
WORD_BOUNDARY_RISK = {
    "act", "aloha", "atlas", "spot", "digit", "drake", "gato",
    "raft", "clip", "dino", "radio", "mjx", "dactyl", "genesis",
    "ros", "dagger", "jason", "star", "flores", "neo",
}


def system_match_pattern(name: str) -> re.Pattern:
    """Build a case-insensitive regex matching `name` with appropriate
    word boundaries. For names containing only lowercase ASCII letters
    that hit WORD_BOUNDARY_RISK, require uppercase or surrounding
    punctuation to reduce false positives."""
    pat = re.escape(name)
    pat = pat.replace(r"\-", r"[-\s]")  # hyphen ↔ space tolerated
    if normalize(name) in WORD_BOUNDARY_RISK:
        # Require uppercase first letter or all-caps to match in text
        # — most narrative prose for these systems uses the proper-noun
        # form. This filters out e.g. "act" the verb.
        pat = r"(?<![A-Za-z])" + pat + r"(?![A-Za-z])"
        return re.compile(pat)
    return re.compile(r"\b" + pat + r"\b", re.IGNORECASE)


def collect_claim_text(entry: dict) -> str:
    """Concatenate the fields where citations live."""
    parts = [
        entry.get("prior_art_notes", "") or "",
        entry.get("disclosure_citation", "") or "",
        entry.get("notes", "") or "",
        entry.get("control_architecture", "") or "",
        entry.get("actuator_details", "") or "",
    ]
    return "\n".join(parts)


def main(argv: list[str]) -> int:
    corpus_path = Path(argv[1]) if len(argv) > 1 else ROOT / "corpus.jsonl"
    if not corpus_path.exists():
        print(f"corpus not found: {corpus_path}", file=sys.stderr)
        return 2

    entries = []
    with open(corpus_path) as f:
        for line in f:
            line = line.strip()
            if line:
                entries.append(json.loads(line))

    idx = build_corpus_index(entries)

    # For each known system, check if it resolves in the corpus name index
    # using any of its variant forms, and whether it appears in any
    # prior_art_notes.
    citers: dict[str, list[str]] = defaultdict(list)
    for canonical, aliases in KNOWN_SYSTEMS:
        all_forms = [canonical, *aliases]
        # Resolution: does any form appear in the corpus name index?
        resolves = any(normalize(f) in idx for f in all_forms)

        # Look for citations in entry text (regardless of resolution —
        # even-resolved citations are useful for connectivity stats).
        patterns = [system_match_pattern(f) for f in all_forms]
        for e in entries:
            text = collect_claim_text(e)
            if any(p.search(text) for p in patterns):
                citers[canonical].append(e["id"])

        # Annotate resolution
        citers[canonical] = (resolves, citers[canonical])  # type: ignore

    # Build report
    missing: list[tuple[str, list[str]]] = []
    resolved: list[tuple[str, list[str]]] = []
    for canonical, (resolves, ids) in sorted(
        citers.items(), key=lambda kv: -len(kv[1][1])
    ):
        if not ids:
            continue
        if resolves:
            resolved.append((canonical, ids))
        else:
            missing.append((canonical, ids))

    print(f"Citation audit — corpus: {corpus_path.name} ({len(entries)} entries)")
    print(f"Known systems checked: {len(KNOWN_SYSTEMS)}")
    print()
    print(f"=== UNRESOLVED CITATIONS ({len(missing)}) ===")
    print("System name → cited by N entries → first 5 citers")
    for canonical, ids in missing:
        head = ", ".join(ids[:5])
        more = f" … (+{len(ids) - 5})" if len(ids) > 5 else ""
        print(f"  {canonical:30s}  {len(ids):3d}  {head}{more}")
    print()
    print(f"=== RESOLVED CITATIONS ({len(resolved)}) ===")
    for canonical, ids in resolved:
        print(f"  {canonical:30s}  {len(ids):3d}")
    print()
    print(
        f"Summary: {len(missing)} unresolved, {len(resolved)} resolved, "
        f"out of {len(KNOWN_SYSTEMS)} systems checked."
    )
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
