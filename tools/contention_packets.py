#!/usr/bin/env python3
"""contention_packets.py — regenerate per-tag invalidity-contention packets.

Usage:
    python3 tools/contention_packets.py

Reads `corpus.jsonl` and groups entries by each tag in their
`disclosed_subsystems`. For each tag with two or more entries, writes a
markdown packet at `contention_packets/<tag>.md` formatted as a
structured invalidity-contention reference an attorney can use directly
when challenging a patent in that subsystem area.

Each packet:
  - is chronologically ordered, earliest disclosure first
  - reproduces every entry's `prior_art_notes` verbatim (the element-by-
    element 102/103 anticipation analysis)
  - lists `disclosure_citation`, `creator`, `ip_status`, `corpus`, and
    `sources` as citation-ready fields
  - carries a Verification section pointing at the 2026.Q2 release
    timestamp artifacts (FreeTSA, DigiCert, OpenTimestamps Bitcoin)
  - is Jekyll-front-matter wrapped for nav integration

Also writes:
  - `contention_packets/INDEX.md`  — table of contents for all packets
  - `contention_packets/README.md` — what these are and how to use them

These are derived artifacts. The contention_packets/ directory is wiped
at the start of every run. Re-run after any edit to corpus.jsonl.
"""
import json
import subprocess
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent.parent
CORPUS = ROOT / "corpus.jsonl"
OUT_DIR = ROOT / "contention_packets"

RELEASE_TARBALL_SHA256 = "aa9430c6e785a409e3dbb10042b16e0e5677752c85eeffcba2c6b5605cde27ce"
ZENODO_DOI = "https://doi.org/10.5281/zenodo.20049531"
REPO_URL = "https://github.com/openIE-dev/free-humanoid-corpus"
VERIFY_SCRIPT_URL = (
    "https://github.com/openIE-dev/free-humanoid-corpus/blob/main/tools/verify_release.sh"
)
BTC_BLOCK_BOB = 948142
BTC_BLOCK_ETERNITYWALL = 948151
BTC_BLOCK_CATALLAXY = 948161


def load_corpus():
    return [json.loads(l) for l in CORPUS.read_text().splitlines() if l.strip()]


def date_key(e):
    return e.get("first_disclosure_date") or ""


def git_short_sha():
    """Return the current git short SHA for the repo, or '' if unavailable."""
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=str(ROOT),
            stderr=subprocess.DEVNULL,
        )
        return out.decode("utf-8").strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""


def is_draft(e):
    return bool(e.get("draft"))


def fmt_date(d):
    return d if d else "?"


def render_packet(tag, entries, nav_order, generated_iso, git_sha):
    entries_sorted = sorted(entries, key=date_key)
    earliest = entries_sorted[0].get("first_disclosure_date") or "?"
    latest = entries_sorted[-1].get("first_disclosure_date") or "?"
    n = len(entries_sorted)
    n_draft = sum(1 for e in entries_sorted if is_draft(e))
    n_commons = n - n_draft

    lines = []
    # Front matter.
    lines += [
        "---",
        f'title: "{tag}"',
        'parent: "Invalidity Contentions"',
        f"nav_order: {nav_order}",
        "layout: default",
        "---",
        "",
        f"# Invalidity Contention Packet — `{tag}`",
        "",
        f"**Generated:** {generated_iso}  ",
        f"**Cross-cut tag:** `{tag}`  ",
        f"**Entries:** {n} ({n_commons} commons-grade, {n_draft} draft)  ",
        f"**Earliest disclosure:** {fmt_date(earliest)}  ",
        f"**Most recent disclosure:** {fmt_date(latest)}",
        "",
        "---",
        "",
        "## How to use this packet",
        "",
        "This document is an invalidity-contention packet — a chronologically-ordered",
        f"list of every disclosed prior art reference in the Free Humanoid Corpus that",
        f"bears on the subsystem `{tag}`.",
        "",
        "To use it:",
        "",
        "1. Identify the patent claim element being challenged.",
        "2. Match the element against the entries below in chronological order (earliest",
        "   first). The earliest entry that discloses the element is the strongest 102",
        "   anticipation candidate.",
        "3. For 103 obviousness contentions, identify the closest two-or-more entries",
        "   that together disclose all claim elements.",
        "4. Each entry's **prior_art_notes** field is element-by-element 102/103",
        "   anticipation analysis — citable as-is.",
        "5. Verify the timestamp authority via the procedures in Verification (below).",
        "",
        "The Free Humanoid Corpus is licensed CC0 1.0; no permission is required to",
        "cite, copy, or redistribute these contentions.",
        "",
        "---",
        "",
        "## Entries (chronological)",
        "",
    ]

    for e in entries_sorted:
        d = fmt_date(e.get("first_disclosure_date"))
        name = e.get("canonical_name", "?")
        eid = e.get("id", "")
        corpus = e.get("corpus", "")
        ip_status = e.get("ip_status", "")
        creator = e.get("creator", "")
        citation = e.get("disclosure_citation", "")
        notes = e.get("prior_art_notes") or ""
        sources = e.get("sources") or []
        subs = e.get("disclosed_subsystems") or []
        draft_flag = " *(draft)*" if is_draft(e) else ""

        lines.append(f"### {d} — {name}{draft_flag}")
        lines.append("")
        lines.append(f"- **id:** `{eid}`")
        lines.append(f"- **corpus:** {corpus}")
        lines.append(f"- **ip status:** {ip_status}")
        if creator:
            lines.append(f"- **creator:** {creator}")
        if citation:
            lines.append(f"- **disclosure citation:** {citation}")
        if subs:
            lines.append(
                "- **disclosed subsystems:** "
                + ", ".join(f"`{s}`" for s in subs)
            )
        lines.append("")
        lines.append("**Prior art notes:**")
        lines.append("")
        if notes.strip():
            for nl in notes.splitlines() or [notes]:
                lines.append(f"> {nl}".rstrip())
        else:
            lines.append("> *(no prior_art_notes recorded for this entry)*")
        lines.append("")
        lines.append("**Sources:**")
        lines.append("")
        if sources:
            for i, src in enumerate(sources, 1):
                lines.append(f"{i}. {src}")
        else:
            lines.append("*(no sources listed)*")
        lines.append("")
        lines.append("---")
        lines.append("")

    # Verification section.
    lines += [
        "## Verification",
        "",
        "This packet's entries are anchored by the Free Humanoid Corpus 2026.Q2",
        "release with three independent cryptographic timestamps proving",
        "pre-existence:",
        "",
        "- **FreeTSA RFC 3161** — `releases/2026.Q2/freetsa.tsr` in the corpus repo",
        "- **DigiCert RFC 3161** — `releases/2026.Q2/digicert.tsr`",
        "- **OpenTimestamps Bitcoin-anchored** — `releases/2026.Q2/corpus-2026.Q2.tar.gz.ots`,",
        f"  with Bitcoin block headers at heights **{BTC_BLOCK_BOB}** (bob),",
        f"  **{BTC_BLOCK_ETERNITYWALL}** (eternitywall), and **{BTC_BLOCK_CATALLAXY}** (catallaxy).",
        "",
        f"The full release tarball SHA-256 is `{RELEASE_TARBALL_SHA256}`,",
        f"archived on Zenodo at <{ZENODO_DOI}>.",
        "",
        "Anyone with a Bitcoin block explorer can independently verify that the corpus",
        "tarball — containing all entries cited in this packet — existed at or before",
        "the timestamps anchored in those blocks.",
        "",
        f"For verification procedure see <{VERIFY_SCRIPT_URL}>.",
        "",
        "---",
        "",
        "## License",
        "",
        "CC0 1.0 Universal (public domain dedication). No copyright restrictions on",
        "use, citation, copying, or redistribution.",
        "",
        "---",
        "",
        f"*Generated from <{REPO_URL}> at corpus revision "
        f"{('`' + git_sha + '`') if git_sha else '(unknown)'}.*",
        "",
    ]

    return "\n".join(lines)


def write_index(packets_meta, generated_iso, git_sha):
    """packets_meta: list of dicts {tag, count, n_commons, n_draft, earliest, latest}."""
    lines = [
        "---",
        'title: "Invalidity Contentions"',
        "has_children: true",
        "nav_order: 4",
        "permalink: /contention_packets/",
        "layout: default",
        "---",
        "",
        "# Invalidity Contention Packets",
        "",
        f"**Generated:** {generated_iso}  ",
        f"**Packets:** {len(packets_meta)}  ",
        f"**Corpus revision:** {('`' + git_sha + '`') if git_sha else '(unknown)'}",
        "",
        "Each packet below is an attorney-ready invalidity-contention reference for a",
        "specific subsystem. Packets are generated from `corpus.jsonl` and are",
        "regenerated whenever the corpus changes. See [README](README.md) for usage and",
        "PDF conversion instructions.",
        "",
        "Each packet contains every corpus entry tagged with the corresponding",
        "subsystem, in chronological order by first verified public disclosure date,",
        "with `prior_art_notes` reproduced verbatim as element-by-element 102/103",
        "anticipation analysis.",
        "",
        "Only tags with two or more disclosing entries get a packet (single-entry tags",
        "are covered by their cross-cut and do not yet form a contention chain).",
        "",
        "| Packet | Entries | Commons | Draft | Earliest | Most recent |",
        "|---|---|---|---|---|---|",
    ]

    for m in packets_meta:
        lines.append(
            f"| [`{m['tag']}`]({m['tag']}.md) "
            f"| {m['count']} "
            f"| {m['n_commons']} "
            f"| {m['n_draft']} "
            f"| {fmt_date(m['earliest'])} "
            f"| {fmt_date(m['latest'])} |"
        )

    (OUT_DIR / "INDEX.md").write_text("\n".join(lines) + "\n")


def write_readme(packets_meta, generated_iso, git_sha):
    n = len(packets_meta)
    total_entries = sum(m["count"] for m in packets_meta)

    lines = [
        "---",
        'title: "Contentions README"',
        'parent: "Invalidity Contentions"',
        "nav_order: 0",
        "layout: default",
        "---",
        "",
        "# Invalidity Contention Packets — README",
        "",
        "## What these are",
        "",
        "Each markdown file in this directory is an **invalidity-contention packet**:",
        "a chronologically-ordered, attorney-ready prior art reference for a single",
        "humanoid-robotics subsystem. The packets are derived from the Free Humanoid",
        "Corpus (`corpus.jsonl`) by grouping entries on their `disclosed_subsystems`",
        "tags, and reproducing each entry's `prior_art_notes` verbatim alongside the",
        "citation-ready metadata an attorney needs to cite it.",
        "",
        f"This generation produced **{n} packets** covering **{total_entries} entry",
        "references** in total (entries appear in multiple packets when they disclose",
        "multiple subsystems).",
        "",
        "The packets are not a substitute for legal judgment. They are a pre-built",
        "structured reference that collapses the corpus down to the chain of",
        "disclosures relevant to a single claim area, with the timestamp anchors that",
        "establish pre-existence.",
        "",
        "## How to use",
        "",
        "1. **Identify the subsystem area** of the patent claim you want to challenge",
        "   (see [INDEX.md](INDEX.md) for the full list of available packets).",
        "2. **Open the matching packet** — for example, a claim about cycloidal",
        "   actuators in humanoid robots is addressed by",
        "   [`actuator-electric-cycloidal.md`](actuator-electric-cycloidal.md).",
        "3. **Read the entries chronologically** (earliest first). The earliest entry",
        "   that discloses the claim element is the strongest 102 anticipation",
        "   candidate.",
        "4. **For 103 obviousness contentions**, identify the smallest set of entries",
        "   that together disclose all claim elements. Each entry's `prior_art_notes`",
        "   is written as element-by-element analysis to make this fast.",
        "5. **Verify the timestamp authorities** for the corpus release using the",
        "   procedure in the corpus repo's `tools/verify_release.sh`. Three independent",
        "   timestamping layers (FreeTSA RFC 3161, DigiCert RFC 3161, OpenTimestamps",
        "   Bitcoin-anchored) attest pre-existence as of 2026-Q2.",
        "",
        "## Convert a packet to PDF",
        "",
        "These packets are plain CommonMark + GitHub-flavored markdown with Jekyll",
        "front matter. To produce an attorney-ready PDF from any single packet:",
        "",
        "```sh",
        "pandoc -o packet.pdf packet.md",
        "```",
        "",
        "(For a more polished result you may want `pandoc --pdf-engine=xelatex",
        "--toc -V geometry:margin=1in -o packet.pdf packet.md`, but the one-line",
        "invocation above is sufficient.)",
        "",
        "## Licensing posture",
        "",
        "The Free Humanoid Corpus is licensed **CC0 1.0 Universal** (public domain",
        "dedication). These packets are generated artifacts from CC0 source data and",
        "are themselves CC0. No permission is required to cite, copy, redistribute,",
        "or incorporate them into legal filings.",
        "",
        "Cited primary sources (papers, books, episodes, patents) carry their own",
        "rights under separate copyright; the packets cite them as references only.",
        "Citation of a copyrighted work as prior art is fair use in every common-law",
        "jurisdiction the authors are aware of.",
        "",
        "## Regenerating",
        "",
        "Packets are regenerated by running:",
        "",
        "```sh",
        "python3 tools/contention_packets.py",
        "```",
        "",
        "from the repository root. The tool wipes the `contention_packets/` directory",
        "before writing, so every regeneration is a clean slate. The corpus revision",
        f"that produced this set is recorded in each packet's footer ({('`' + git_sha + '`') if git_sha else 'unknown'}).",
        "",
        "## Provenance",
        "",
        f"- **Generated:** {generated_iso}",
        f"- **Source:** <{REPO_URL}>",
        f"- **Release tarball SHA-256:** `{RELEASE_TARBALL_SHA256}`",
        f"- **Zenodo DOI:** <{ZENODO_DOI}>",
        "- **Bitcoin anchor blocks (2026.Q2 release):**",
        f"  bob {BTC_BLOCK_BOB}, eternitywall {BTC_BLOCK_ETERNITYWALL}, catallaxy {BTC_BLOCK_CATALLAXY}",
        "",
    ]

    (OUT_DIR / "README.md").write_text("\n".join(lines) + "\n")


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    # Wipe the directory so removed tags don't linger and the regen is idempotent.
    for f in OUT_DIR.iterdir():
        if f.is_file():
            f.unlink()

    entries = load_corpus()
    by_tag = defaultdict(list)
    for e in entries:
        for tag in e.get("disclosed_subsystems") or []:
            by_tag[tag].append(e)

    # Only emit packets for tags with 2+ entries — singletons don't make a chain.
    eligible = {tag: es for tag, es in by_tag.items() if len(es) >= 2}

    generated_iso = date.today().isoformat()
    git_sha = git_short_sha()

    # Stable nav ordering: alphabetical by tag.
    sorted_tags = sorted(eligible.keys())

    packets_meta = []
    for nav_order, tag in enumerate(sorted_tags, start=1):
        es = eligible[tag]
        es_sorted = sorted(es, key=date_key)
        text = render_packet(tag, es, nav_order, generated_iso, git_sha)
        (OUT_DIR / f"{tag}.md").write_text(text)
        n_draft = sum(1 for e in es if is_draft(e))
        packets_meta.append({
            "tag": tag,
            "count": len(es),
            "n_commons": len(es) - n_draft,
            "n_draft": n_draft,
            "earliest": es_sorted[0].get("first_disclosure_date") or "",
            "latest": es_sorted[-1].get("first_disclosure_date") or "",
        })

    # Sort the index alphabetically for the table of contents.
    packets_meta.sort(key=lambda m: m["tag"])

    write_index(packets_meta, generated_iso, git_sha)
    write_readme(packets_meta, generated_iso, git_sha)

    # Reporting summary.
    skipped = len(by_tag) - len(eligible)
    print(f"  contention_packets: {len(eligible)} packets written "
          f"({skipped} single-entry tags skipped)")
    print(f"  corpus revision: {git_sha or '(unavailable)'}")


if __name__ == "__main__":
    main()
