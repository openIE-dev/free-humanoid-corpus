---
title: "mechanism-gecko-microhair-adhesion"
parent: "Invalidity Contentions"
nav_order: 206
layout: default
---

# Invalidity Contention Packet — `mechanism-gecko-microhair-adhesion`

**Generated:** 2026-05-15  
**Cross-cut tag:** `mechanism-gecko-microhair-adhesion`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2015-01  
**Most recent disclosure:** 2015-05

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `mechanism-gecko-microhair-adhesion`.

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

### 2015-01 — OnRobot RG2 / RG6 / VGC10 cobot grippers

- **id:** `onrobot-rg-grippers-2015`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** On Robot A/S (Odense, Denmark); Christiansen + Fuglsang; absorbed Perception Robotics + OptoForce 2018
- **disclosure citation:** On Robot A/S (Odense, Denmark). Founded 2015 by Bilge J. Christiansen + Ebbe O. Fuglsang. RG2 (2015) and RG6 (2016) electric parallel grippers; VG10 / VGC10 compressor-free electric vacuum grippers (2017-2019). Merged with Perception Robotics (NASA-JPL gecko-microhair-licensed) and OptoForce (Hungarian F/T sensor) 2018.
- **disclosed subsystems:** `mechanism-parallel-jaw-gripper`, `mechanism-vacuum-gripper`, `mechanism-gecko-microhair-adhesion`, `actuator-electric`

**Prior art notes:**

> OnRobot RG-line and VGC-line grippers (Odense Denmark 2015+) are the canonical 'cable-free cobot tool' commercial category. 11-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from plug-and-play electric parallel grippers, compressor-free electric vacuum grippers, or gecko-microhair dry-adhesion grippers. Together with Robotiq (round-42) and SCHUNK Co-act (round-42), establishes the global cobot-gripper prior-art chain across CA / DK / DE.

**Sources:**

1. onrobot.com/en/about
2. onrobot.com/en/products/gecko-gripper

---

### 2015-05 — Stanford gecko-adhesive gripper (Cutkosky BDML)

- **id:** `stanford-gecko-cutkosky-2015`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** Stanford University Biomimetics and Dexterous Manipulation Lab (BDML); Elliot Hawkes, David Christensen, Mark Cutkosky
- **disclosure citation:** Hawkes, E.W., Christensen, D.L., Cutkosky, M.R. 'Vertical dry adhesion climbing with a 100× body-weight payload'. IEEE International Conference on Robotics and Automation (ICRA) 2015. Stanford University Biomimetics and Dexterous Manipulation Lab (BDML) under Mark Cutkosky.
- **disclosed subsystems:** `mechanism-gecko-microhair-adhesion`, `mechanism-dry-adhesive-gripper`, `mechanism-tendon-drive`

**Prior art notes:**

> Stanford gecko-adhesive gripper (Hawkes / Christensen / Cutkosky BDML ICRA 2015) is the foundational directional dry-adhesive (gecko-microhair) gripper. 10-year-deep academic-publication prior art. Direct shielding for any commercial humanoid claim deriving from gecko-microhair / dry-adhesive grippers. Sister to NASA JPL space-rated gecko gripper (Parness 2014-2017); commercialized via OnRobot Gecko Gripper (round-42).

**Sources:**

1. news.stanford.edu/news/2015/may/grabber-robot-gecko-052715.html
2. Hawkes, E.W., Christensen, D.L., Cutkosky, M.R. ICRA 2015.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `cd2f551`.*
