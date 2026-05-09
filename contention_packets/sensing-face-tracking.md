---
title: "sensing-face-tracking"
parent: "Invalidity Contentions"
nav_order: 227
layout: default
---

# Invalidity Contention Packet — `sensing-face-tracking`

**Generated:** 2026-05-09  
**Cross-cut tag:** `sensing-face-tracking`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 1998-09  
**Most recent disclosure:** 2019-06

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `sensing-face-tracking`.

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

### 1998-09 — MIT Kismet (sociable robot)

- **id:** `mit-kismet-breazeal-1998`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** MIT AI Lab; Cynthia Breazeal (PhD student of Rodney Brooks)
- **disclosure citation:** Breazeal, C. 'Designing Sociable Robots'. MIT Press 2002 (book covering 1997-2002 development). Earlier: Breazeal, C. 'Sociable machines: expressive social exchange between humans and robots'. PhD thesis, MIT 2000. The Kismet robot: animatronic head + shoulders with 21 degrees of freedom for facial expression + neck + auditory recognition. MIT AI Lab; Rodney Brooks supervised.
- **disclosed subsystems:** `mechanism-animatronic-head`, `control-affective-computing`, `control-social-robot`, `control-facial-expression`, `sensing-face-tracking`

**Prior art notes:**

> MIT Kismet is the canonical foundational sociable-robot academic platform (Breazeal MIT 1998-2000). 27-year-deep public-domain prior art for: 21-DoF emotive-head animatronics, face-to-face human-robot social interaction, biologically-inspired motivational-emotion-behavior architecture. **The architectural ancestor of all subsequent social-robot research** including NAO (corpus entry), Pepper (corpus entry), Jibo (Breazeal's 2017 commercial spinoff), and any modern humanoid claim on social interaction or emotive expression. Direct shielding for any commercial humanoid claim on emotive expression or affective human-robot interaction (Tesla Optimus, 1X NEO, Sanctuary Phoenix, Apptronik Apollo all market 'natural HRI' which faces this 27-year-deep academic chain).

**Sources:**

1. Breazeal, C. 'Designing Sociable Robots'. MIT Press 2002.
2. Breazeal, C. PhD thesis, MIT 2000.
3. MIT Kismet project page (web.media.mit.edu/~cynthiab/Kismet).

---

### 2019-06 — MediaPipe (Google on-device perception)

- **id:** `mediapipe-google-2019`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Google Research; Camillo Lugaresi et al.
- **disclosure citation:** Lugaresi, C., Tang, J., Nash, H., et al. 'MediaPipe: A Framework for Building Perception Pipelines'. arXiv:1906.08172, June 2019. Google Research. Apache-2.0 release. Subsequent: MediaPipe Hands (2020), MediaPipe Holistic (2020), MediaPipe Solutions (2023+).
- **disclosed subsystems:** `sensing-hand-pose-tracking`, `sensing-face-tracking`, `sensing-body-pose`, `control-perception-pipeline`

**Prior art notes:**

> MediaPipe (Lugaresi et al. Google 2019+) is the foundational on-device perception library. 6-year-deep open-permissive prior art for: real-time hand-pose + body-pose + face-mesh estimation, on-device perception pipeline framework. **The de facto hand-pose library used in DexMV (round-17), Open-TeleVision (round-16), and most academic teleoperation papers**. Direct shielding for any commercial humanoid claim on real-time hand-pose-driven teleoperation.

**Sources:**

1. Lugaresi et al. arXiv:1906.08172 June 2019.
2. Google MediaPipe site (mediapipe.dev).
3. GitHub: github.com/google-ai-edge/mediapipe.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `073503d`.*
