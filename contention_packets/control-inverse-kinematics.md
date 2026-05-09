---
title: "control-inverse-kinematics"
parent: "Invalidity Contentions"
nav_order: 58
layout: default
---

# Invalidity Contention Packet — `control-inverse-kinematics`

**Generated:** 2026-05-09  
**Cross-cut tag:** `control-inverse-kinematics`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 1955-06  
**Most recent disclosure:** 1969-06

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-inverse-kinematics`.

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

### 1955-06 — Denavit-Hartenberg parameters

- **id:** `denavit-hartenberg-parameters-1955`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Northwestern University; Jacques Denavit, Richard S. Hartenberg
- **disclosure citation:** Denavit, J., Hartenberg, R. S. 'A Kinematic Notation for Lower-Pair Mechanisms Based on Matrices'. ASME Journal of Applied Mechanics 22(2) 1955. Northwestern University.
- **disclosed subsystems:** `control-kinematics`, `control-forward-kinematics`, `control-inverse-kinematics`

**Prior art notes:**

> The Denavit-Hartenberg parameters (Denavit + Hartenberg ASME 1955) are the foundational kinematic notation for robotics. 70-year-deep public-domain prior art. **Used in every URDF / OpenLoco UDD / MuJoCo MJCF descriptor in the corpus**, every robot kinematic specification ever written. Direct shielding for any commercial humanoid claim that includes kinematic specification.

**Sources:**

1. Denavit, J., Hartenberg, R. S. ASME Journal of Applied Mechanics 22(2) 1955.
2. Craig, J. J. 'Introduction to Robotics: Mechanics and Control' Addison-Wesley 1986 (Modified DH).

---

### 1969-06 — Stanford Arm (Scheinman 1969)

- **id:** `stanford-arm-scheinman-1969`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Stanford AI Laboratory; Victor Scheinman
- **disclosure citation:** Scheinman, V.D. 'Design of a Computer Controlled Manipulator'. Stanford AI Memo 92, June 1969. Stanford Artificial Intelligence Laboratory. Subsequently commercialized as Vicarm (Scheinman's company), then sold to Unimation.
- **disclosed subsystems:** `manipulator-arm`, `actuator-electric`, `control-inverse-kinematics`, `mechanism-spherical-wrist`

**Prior art notes:**

> Stanford Arm (Scheinman Stanford AI Lab 1969) is the foundational all-electric 6-axis arm with closed-form kinematics. 56-year-deep public-domain prior art. The Scheinman spherical wrist became the industrial standard. Direct shielding for any commercial humanoid claim deriving from 6-DoF anthropomorphic arm geometry. Direct ancestor of PUMA (round-45) and every modern 6-DoF industrial arm.

**Sources:**

1. en.wikipedia.org/wiki/Stanford_arm
2. en.wikipedia.org/wiki/Victor_Scheinman

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `bd98079`.*
