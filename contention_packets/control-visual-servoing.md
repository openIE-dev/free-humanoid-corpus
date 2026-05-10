---
title: "control-visual-servoing"
parent: "Invalidity Contentions"
nav_order: 138
layout: default
---

# Invalidity Contention Packet — `control-visual-servoing`

**Generated:** 2026-05-10  
**Cross-cut tag:** `control-visual-servoing`  
**Entries:** 2 (1 commons-grade, 1 draft)  
**Earliest disclosure:** 2000-01  
**Most recent disclosure:** 2002-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-visual-servoing`.

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

### 2000-01 — KTH Royal Institute of Technology robotics *(draft)*

- **id:** `kth-sweden-stockholm-robotics`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** KTH Royal Institute of Technology (Stockholm, Sweden)
- **disclosure citation:** KTH Royal Institute of Technology (Stockholm, Sweden). Robotics research at Robotics, Perception and Learning (RPL) division of the School of Electrical Engineering and Computer Science. Notable: visual servoing + grasping (Kragic + Hellström lab), autonomous vehicles.
- **disclosed subsystems:** `control-research-cluster`, `control-visual-servoing`, `control-grasp-planning`

**Prior art notes:**

> KTH Royal Institute of Technology is Sweden's flagship robotics academic anchor. Brings Sweden depth in the corpus from 2 to 3 entries. Together with VTT Finland (round-24) and Universal Robots Denmark (round-24), establishes the Nordic robotics prior-art baseline.

**Sources:**

1. KTH RPL division (kth.se/rpl).
2. Kragic group publications.

---

### 2002-04 — Kragic-Christensen visual servoing for grasping

- **id:** `kragic-christensen-visual-servoing-2002`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** KTH Royal Institute of Technology Computational Vision and Active Perception Laboratory; Danica Kragic, Henrik I. Christensen
- **disclosure citation:** Kragic, D., Christensen, H. I. 'Survey on Visual Servoing for Manipulation'. Computational Vision and Active Perception Laboratory technical report, KTH Royal Institute of Technology, April 2002. Subsequent: Kragic, D. 'Visual servoing for object manipulation: A survey'. Royal Institute of Technology, Computational Vision and Active Perception Laboratory.
- **disclosed subsystems:** `control-visual-servoing`, `control-grasp-planning`, `control-manipulation`

**Prior art notes:**

> Kragic-Christensen visual servoing (KTH 2002+) is the foundational Swedish academic visual-servoing-for-grasping framework. 23-year-deep public-domain prior art. The specific paper-level anchor for round-25 KTH Sweden aggregator. Direct shielding for any commercial humanoid claim using vision-conditioned grasp control.

**Sources:**

1. Kragic, D., Christensen, H. I. KTH technical report April 2002.
2. KTH RPL division (kth.se/rpl).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `2aee416`.*
