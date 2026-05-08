---
title: "control-agricultural-autonomy"
parent: "Invalidity Contentions"
nav_order: 21
layout: default
---

# Invalidity Contention Packet — `control-agricultural-autonomy`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-agricultural-autonomy`  
**Entries:** 2 (0 commons-grade, 2 draft)  
**Earliest disclosure:** 2010-01  
**Most recent disclosure:** 2010-07

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-agricultural-autonomy`.

To use it:

1. Identify the patent claim element being challenged.
2. Match the element against the entries below in chronological order (earliest
   first). The earliest entry that discloses the element is the strongest 102
   anticipation candidate.
3. For 103 obviousness contentions, identify the closest two-or-more entries
   that together disclose all claim elements.
4. Each entry's **prior_art_notes** field is element-by-element 102/103
   anticipation analysis — citable as-is.
5. Verify the timestamp authority via the procedures in Verification (below).

The Free Humanoid Corpus is licensed CC0 1.0; no permission is required to
cite, copy, or redistribute these contentions.

---

## Entries (chronological)

### 2010-01 — Embrapa Brazilian agritech robotics *(draft)*

- **id:** `embrapa-brazil-agritech-robotics`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Empresa Brasileira de Pesquisa Agropecuária (Embrapa)
- **disclosure citation:** Empresa Brasileira de Pesquisa Agropecuária (Embrapa, founded 1973). Brazilian Federal Government agricultural research corporation; the largest agricultural research organization in the southern hemisphere. embrapa.br. Robotics research concentrated at Embrapa Instrumentation (São Carlos): autonomous tractors, agricultural drones, soil + crop sensing platforms.
- **disclosed subsystems:** `control-research-cluster`, `control-agricultural-autonomy`, `mechanism-mobile-base`

**Prior art notes:**

> Embrapa is the canonical Brazilian agritech robotics research institution. **First entry in the corpus from Brazil** — closes a major regional gap. Direct shielding for any commercial humanoid claim on agricultural-context deployment, particularly for the Latin American market. Aggregator-style entry; specific Embrapa papers should be added in future rounds.

**Sources:**

1. Embrapa corporate site (embrapa.br).
2. Embrapa Instrumentation publications (cnpdia.embrapa.br).

---

### 2010-07 — CSIRO Data61 Robotics and Autonomous Systems *(draft)*

- **id:** `csiro-data61-australia-robotics`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** CSIRO Data61 (Commonwealth Scientific and Industrial Research Organisation, Australia)
- **disclosure citation:** CSIRO Data61 (Commonwealth Scientific and Industrial Research Organisation; Brisbane + Sydney, Australia). Robotics and Autonomous Systems group originally part of CSIRO ICT Centre, merged into Data61 in 2014. Notable projects: **Wildcat** legged robot for DARPA Subterranean Challenge (won 2nd place 2021), **Bobcat** agricultural robot, **Tilt-rotor UAV** development. Continuous robotics research output 2010+.
- **disclosed subsystems:** `control-research-cluster`, `control-vio-slam`, `mechanism-quadrupedal-locomotion`, `control-agricultural-autonomy`

**Prior art notes:**

> CSIRO Data61 is Australia's dominant robotics research institution. 15-year-deep public-domain academic prior art spanning legged robots (DARPA SubT 2021 2nd place), agricultural automation (SwagBot, Bobcat), aerial systems. **First entry in the corpus for Australia** — closes a major regional gap. Aggregator-style entry covering CSIRO RAS broadly; specific papers should be added in future rounds.

**Sources:**

1. CSIRO Data61 corporate site (data61.csiro.au).
2. CSIRO Robotics and Autonomous Systems (research.csiro.au/robotics).
3. DARPA SubT 2021 results.
4. Cordin et al. CSIRO Wildcat / Spotter publications.

---

## Verification

This packet's entries are anchored by the Free Humanoid Corpus 2026.Q2
release with three independent cryptographic timestamps proving
pre-existence:

- **FreeTSA RFC 3161** — `releases/2026.Q2/freetsa.tsr` in the corpus repo
- **DigiCert RFC 3161** — `releases/2026.Q2/digicert.tsr`
- **OpenTimestamps Bitcoin-anchored** — `releases/2026.Q2/corpus-2026.Q2.tar.gz.ots`,
  with Bitcoin block headers at heights **948142** (bob),
  **948151** (eternitywall), and **948161** (catallaxy).

The full release tarball SHA-256 is `aa9430c6e785a409e3dbb10042b16e0e5677752c85eeffcba2c6b5605cde27ce`,
archived on Zenodo at <https://doi.org/10.5281/zenodo.20049531>.

Anyone with a Bitcoin block explorer can independently verify that the corpus
tarball — containing all entries cited in this packet — existed at or before
the timestamps anchored in those blocks.

For verification procedure see <https://github.com/openIE-dev/free-humanoid-corpus/blob/main/tools/verify_release.sh>.

---

## License

CC0 1.0 Universal (public domain dedication). No copyright restrictions on
use, citation, copying, or redistribution.

---

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `147307a`.*
