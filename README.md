# Free Humanoid Corpus

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20049531.svg)](https://doi.org/10.5281/zenodo.20049531)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0--1.0-lightgrey.svg)](LICENSE)

A structured prior art commons covering robots, humanoids, and humanoid-adjacent
entities from private companies, open source repositories, science fiction
(film, TV, comics, games, literature), and academia.

**The corpus IS the prior art commons.** Every entry, at the moment of
timestamped commit and quarterly release, is a defensive publication. There
is no separate commons layer above this catalog — the structured data here,
combined with the cryptographic timestamping in `releases/`, is itself the
invalidity-contention material.

## License

CC0-1.0. Public domain dedication. See [LICENSE](LICENSE).

## What's in here

```
SCHEMA.md           — schema spec (currently v0.2)
PLAN.md             — multi-phase build plan
TIMESTAMPING.md     — release ceremony for cryptographic timestamping
MIGRATION_REPORT.md — v1 to v2 migration notes
README.md           — this file

corpus.jsonl        — master corpus (one JSON object per line)
private.jsonl       — generated mirror, entries with corpus="private"
open.jsonl          — generated mirror
fictional.jsonl     — generated mirror
academic.jsonl      — generated mirror

INDEX.md            — generated alphabetical index
lineage.json        — generated ancestor/descendant DAG

cross_cuts/         — generated per-subsystem prior art views
  INDEX.md          — table of all cross-cuts with counts
  <tag>.md          — chronological view of all entries disclosing <tag>

tools/
  validate.py       — schema and quality-bar enforcement
  index.py          — generates INDEX.md, lineage.json, per-corpus mirrors
  cross_cuts.py     — generates cross_cuts/

release.sh          — quarterly release ceremony with timestamping
```

## Quick start

```bash
# Validate the corpus passes structural and quality-bar checks
python3 tools/validate.py corpus.jsonl --strict

# Regenerate all derived artifacts after editing corpus.jsonl
python3 tools/index.py .
python3 tools/cross_cuts.py .

# Run a quarterly release with cryptographic timestamping
./release.sh 2026.Q2
```

## Current state

As of latest commit:

- **56 entries**, 41 commons-grade and 15 draft
- **48 subsystem cross-cuts** generated automatically
- **Lineage DAG** with 0 cycles, 18 to-do items (referenced-but-missing entries)
- **Date range**: 1920 (R.U.R.) to 2024 (multiple)

## Quality bar

An entry is commons-grade (not `draft: true`) when:

1. `disclosure_citation` resolves to a primary source verifiable by a
   third party.
2. `first_disclosure_date` is the earliest verifiable public disclosure,
   defensible against challenge.
3. `prior_art_notes` reads as a 102/103 anticipation analysis someone
   unrelated to us could cite without rewriting.
4. `sources` cite primary references.
5. For patented entries, `ip_citations` lists actual patent numbers.

Entries that don't yet clear this bar are merged with `draft: true` and
have explicit work items in their `notes` field.

## Cross-cuts as the working tool

The cross-cut files (`cross_cuts/<tag>.md`) are the operational form of the
commons. Each file lists every entry disclosing a given subsystem, in
chronological order, with their `prior_art_notes` and `disclosure_citation`
inline.

Use these when assessing patent claims:
- A claim about anthropomorphic robotic hands? Open `mechanism-anthropomorphic-hand.md`
  and read 20 disclosures starting at WABOT-1 (1973).
- A claim about quasi-direct-drive actuators? Open `actuator-electric-quasi-direct-drive.md`
  and read the chain anchored at MIT Mini Cheetah (2019).
- A claim about safety supervisors? Open `safety-hard-constraint.md` and read
  10 disclosures starting at Asimov (1940), through Sha's Simplex (1995),
  HJ reachability (2005), CBFs (2007), ISO 10218 (2006), shielded RL (2018).

## Contributing

Contributions are welcome under CC0-1.0. By submitting an entry you
dedicate the contribution to the public domain.

A good entry is one that holds up as defensive publication. The contribution
guide (see PLAN.md Phase 2) covers what that means in practice. Briefly:

- Cite primary sources, not Wikipedia.
- Identify specific subsystems disclosed using the taxonomy in SCHEMA.md.
- Write `prior_art_notes` as element-by-element anticipation analysis.
- For patented entries, point back at academic or fictional prior art that
  anticipates the claims.

If unsure, mark the entry `draft: true` and document the work needed to
clear the quality bar.

## Provenance

Originated within Open Interface Engineering (OpenIE) as part of the Free
Humanoid project. The corpus is structurally separate from Free Humanoid:
Free Humanoid uses the corpus, but the corpus serves the entire embodied
robotics field, not any specific platform.
