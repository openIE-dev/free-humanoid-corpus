---
title: "mechanism-underactuated-finger"
parent: "Invalidity Contentions"
nav_order: 233
layout: default
---

# Invalidity Contention Packet — `mechanism-underactuated-finger`

**Generated:** 2026-05-14  
**Cross-cut tag:** `mechanism-underactuated-finger`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 1963-01  
**Most recent disclosure:** 2008-01

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `mechanism-underactuated-finger`.

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

### 1963-01 — Belgrade / Belgrade-USC Hand (Tomović + Bekey)

- **id:** `belgrade-usc-tomovic-bekey-hand-1963`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Mihailo Pupin Institute (Belgrade, Yugoslavia); Rajko Tomović + Miodrag Rakić; later Belgrade-USC version with George Bekey at USC
- **disclosure citation:** Tomović, R., Boni, G. 'An Adaptive Artificial Hand'. IRE Transactions on Automatic Control AC-7(3), 1962. Belgrade Hand developed at Mihailo Pupin Institute (Belgrade, Yugoslavia) 1961-1963. Subsequent Belgrade-USC Hand version with George Bekey at University of Southern California ~1988.
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `mechanism-underactuated-finger`, `control-myoelectric`, `actuator-electric`

**Prior art notes:**

> Belgrade / Belgrade-USC Hand (Tomović + Rakić 1963; Bekey USC 1988) is the foundational anthropomorphic prosthetic hand and the world's first externally-powered five-finger myoelectric prosthetic. 62-year-deep public-domain prior art. Direct shielding for any commercial humanoid claim deriving from five-finger anthropomorphic hands, underactuated finger mechanisms, or myoelectric prosthetic control. Foundational to every modern anthropomorphic hand including Robotiq (round-42), Shadow Dexterous Hand (corpus), Salisbury Stanford-JPL Hand (corpus), Utah/MIT Hand (round-42), and the entire dexterous-hand research lineage.

**Sources:**

1. Tomović, R. + Boni, G. 'An Adaptive Artificial Hand'. IRE Transactions on Automatic Control AC-7(3), 1962.
2. en.techfokus.rs/belgrade-hand-first-bionic-prosthetic-robotics/
3. en.wikipedia.org/wiki/Rajko_Tomović

---

### 2008-01 — Robotiq Adaptive Grippers (2F-85, 2F-140, Hand-E, 3-Finger)

- **id:** `robotiq-adaptive-grippers-2008`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Robotiq Inc. (Lévis QC, Canada); Bouchard, Jobin, Duchaine; underactuated finger lineage from Laval University MARS hand
- **disclosure citation:** Robotiq Inc. (Lévis, Québec, Canada). Founded 2008 by Samuel Bouchard, Jean-Philippe Jobin, Vincent Duchaine. Adaptive Gripper product line 2008-2018: 2-Finger 85 (2F-85, 2014), 2-Finger 140 (2F-140, 2017), Hand-E (2018), 3-Finger Adaptive Gripper (2008). Underactuated finger mechanism descended from Laval University MARS hand (Laliberté, Birglen, Gosselin).
- **disclosed subsystems:** `mechanism-parallel-jaw-gripper`, `mechanism-underactuated-finger`, `actuator-electric`

**Prior art notes:**

> Robotiq Adaptive Grippers (Robotiq Lévis QC 2008+) are the canonical commercial cobot end-effector with 17+ years of deployment and 23,000+ units shipped. Direct shielding for any commercial humanoid claim deriving from underactuated parallel-jaw or three-finger adaptive grippers, or from cobot-tool plug-and-play architectures. Lineage descends from Laval University MARS hand (Laliberté / Birglen / Gosselin) underactuated mechanism.

**Sources:**

1. blog.robotiq.com/adaptive-robot-gripper-3-finger-history
2. robotiq.com/products/adaptive-grippers

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `c61fc91`.*
