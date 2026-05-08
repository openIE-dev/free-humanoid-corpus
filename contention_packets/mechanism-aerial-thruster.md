---
title: "mechanism-aerial-thruster"
parent: "Invalidity Contentions"
nav_order: 88
layout: default
---

# Invalidity Contention Packet — `mechanism-aerial-thruster`

**Generated:** 2026-05-08  
**Cross-cut tag:** `mechanism-aerial-thruster`  
**Entries:** 2 (0 commons-grade, 2 draft)  
**Earliest disclosure:** 2019-05  
**Most recent disclosure:** 2021-07

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `mechanism-aerial-thruster`.

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

### 2019-05 — FSTAR (Flying STAR) *(draft)*

- **id:** `fstar-zarrouk-2019`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Ben-Gurion University; David Zarrouk group
- **disclosure citation:** Zarrouk, D., et al. 'Flying STAR (FSTAR): a hybrid flying-and-running quadcopter with sprawl-tuned mechanism'. Ben-Gurion University, ICRA 2019 era.
- **disclosed subsystems:** `mechanism-sprawl-tunable`, `mechanism-wheel-leg-hybrid`, `mechanism-aerial-thruster`, `mechanism-hybrid-locomotion`, `mechanism-reconfigurable`, `control-mode-switching`

**Prior art notes:**

> FSTAR (Ben-Gurion Zarrouk lab, ~2019) is the first hybrid flying + ground-running STAR-family member. 6-year-deep open-academic prior art for: shared-motor-pool hybrid aerial-ground locomotion, sprawl-tuned wheel-leg + propeller integration. Architectural cousin of Caltech LEONARDO (round-8/round-12 entry caltech-leonardo-2021): FSTAR is quadruped+thrust, LEONARDO is bipedal+thrust. Together they establish the hybrid-locomotion academic substrate.

**Sources:**

1. Zarrouk lab publications (bgu.ac.il/zarrouklab).
2. Times of Israel coverage (timesofisrael.com).

---

### 2021-07 — FCSTAR (Flying-Climbing STAR) *(draft)*

- **id:** `fcstar-zarrouk-2021`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Ben-Gurion University; David Zarrouk group
- **disclosure citation:** Zarrouk, D., et al. 'FCSTAR: Design and Analysis of a Hybrid Flying and Climbing Sprawl-Tuned Robot'. ResearchGate publication 353205537, July 2021. Ben-Gurion University. Builds on FSTAR with thrust-reversal wall-climbing capability.
- **disclosed subsystems:** `mechanism-sprawl-tunable`, `mechanism-wheel-leg-hybrid`, `mechanism-aerial-thruster`, `mechanism-thrust-reversal`, `mechanism-wall-climbing`, `mechanism-reconfigurable`, `control-mode-switching`

**Prior art notes:**

> FCSTAR (Ben-Gurion Zarrouk lab, ~2021) is the most architecturally ambitious STAR-family member: 4 modes (ground, wall-climb, pipe, flight) on a single actuator pool. 4-year-deep open-academic prior art for: thrust-reversal wall-climbing, multi-mode-on-shared-actuator-pool reconfiguration, narrow-pipe traversal. Closes the STAR family lineage chain that begins at star-fearing-2013 and ends with dstar-zarrouk-2026 (decoupled FBEM, Jan 2026). The full 13-year-deep STAR family chain: STAR (Berkeley 2013) → RSTAR (Zarrouk 2019) → TSTAR → FSTAR → FCSTAR → AmphiSTAR → DSTAR.

**Sources:**

1. ResearchGate publication 353205537 (July 2021).
2. Zarrouk lab publications (bgu.ac.il/zarrouklab).
3. ISRAEL21c coverage (israel21c.org).

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
