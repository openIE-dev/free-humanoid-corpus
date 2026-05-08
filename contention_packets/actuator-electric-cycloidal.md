---
title: "actuator-electric-cycloidal"
parent: "Invalidity Contentions"
nav_order: 5
layout: default
---

# Invalidity Contention Packet — `actuator-electric-cycloidal`

**Generated:** 2026-05-08  
**Cross-cut tag:** `actuator-electric-cycloidal`  
**Entries:** 5 (2 commons-grade, 3 draft)  
**Earliest disclosure:** 1937  
**Most recent disclosure:** 2025-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `actuator-electric-cycloidal`.

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

### 1937 — Sumitomo CYCLO Speed Reducer

- **id:** `sumitomo-cyclo`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Lorenz Bayer-Ehrlich (inventor, Germany); Sumitomo Heavy Industries (commercial development, Japan)
- **disclosure citation:** Lorenz Bayer-Ehrlich. German patent DE745552 (1937) for cycloidal speed reducer. Commercial production: Sumitomo Heavy Industries, CYCLO drive product line, 1937 onwards.
- **disclosed subsystems:** `actuator-electric-cycloidal`, `actuator-electric-direct-drive`

**Prior art notes:**

> Sumitomo CYCLO is the foundational academic and industrial disclosure of cycloidal speed reducers in robotic actuators. Anticipates with full mechanism specificity, dating to 1937: (1) cycloid-disk-and-pin-tooth gear reduction for high-ratio compact actuators — relevant to *every* modern humanoid claim using cycloidal reducers (Apptronik Apollo, Sanctuary Phoenix, Boston Dynamics Atlas G3, multiple Chinese commodity humanoids); (2) two-disk 180-degree opposed cycloid arrangement for vibration cancellation — relevant to claims on balanced cycloidal joints; (3) low-backlash multi-tooth meshing — relevant to backlash-control IP. The 1937 German patent has long since expired; CYCLO products have been continuously sold since 1937 with full mechanism documentation. Modern cycloidal humanoid actuator claims (the corpus's pre-this-entry chain only had 3 entries from 2023) face this 89-year industrial-academic anchor as 102 prior art at extraordinary depth.

**Sources:**

1. German patent DE745552 (1937), Lorenz Bayer-Ehrlich.
2. Sumitomo Heavy Industries CYCLO drive product literature (multiple decades).
3. Lehmann, M. and Schreiber, R. 'Improved Cycloidal Speed Reducer'. ASME Mechanisms Conference, 1992.
4. Litvin, F.L. Gear Geometry and Applied Theory. Cambridge University Press, 2004 (standard reference covering cycloidal kinematics).

---

### 2023-05 — Sanctuary AI Phoenix *(draft)*

- **id:** `sanctuary-phoenix`
- **corpus:** private
- **ip status:** patented
- **creator:** Sanctuary AI
- **disclosure citation:** Sanctuary AI public reveal, May 2023.
- **disclosed subsystems:** `actuator-electric-cycloidal`, `actuator-electric-direct-drive`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `mechanism-tendon-routing`, `control-teleoperation`, `control-rl-policy`, `sensing-stereo-camera`, `sensing-force-torque`, `power-li-ion`

**Prior art notes:**

> Sanctuary's high-DoF hand claims face Shadow Hand (2003) and iCub (2008) as deep prior art for tendon-driven anthropomorphic hands with high finger DoF.

**Sources:**

1. sanctuary.ai
2. Sanctuary AI press materials and demonstration videos.

---

### 2023-08 — Apptronik Apollo *(draft)*

- **id:** `apptronik-apollo`
- **corpus:** private
- **ip status:** patented
- **creator:** Apptronik
- **disclosure citation:** Apptronik public reveal of Apollo, August 2023.
- **disclosed subsystems:** `actuator-electric-cycloidal`, `actuator-electric-planetary`, `actuator-electric-direct-drive`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `control-mpc`, `control-rl-policy`, `sensing-stereo-camera`, `sensing-force-torque`, `sensing-imu`, `power-li-ion`, `power-hot-swap`

**Prior art notes:**

> Apptronik's actuator IP has lineage from UT Austin Human-Centered Robotics Lab (Sentis) and from NASA Valkyrie work; both sources constitute substantial prior art that limits the patentable surface area of Apptronik's own claims.

**Sources:**

1. apptronik.com
2. Apptronik technical materials.

---

### 2024-05 — Unitree G1 *(draft)*

- **id:** `unitree-g1`
- **corpus:** private
- **ip status:** patented
- **creator:** Unitree Robotics
- **disclosure citation:** Unitree Robotics G1 reveal, May 2024.
- **disclosed subsystems:** `actuator-electric-cycloidal`, `actuator-electric-quasi-direct-drive`, `mechanism-bipedal-locomotion`, `control-rl-policy`, `sensing-monocular-depth`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> G1's actuator IP largely anticipated by MIT Mini Cheetah QDD work and Honda harmonic drive prior art. The aggressive pricing represents the commodity-humanoid trajectory more than novel IP.

**Sources:**

1. Unitree.com
2. Unitree technical specifications.

---

### 2025-04 — Berkeley Humanoid Lite

- **id:** `berkeley-humanoid-lite-2025`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** UC Berkeley Hybrid Robotics Lab; Sreenath group
- **disclosure citation:** Cui, F., Sayle, J., Karydis, K., Liao, Q., et al. 'Demonstrating Berkeley Humanoid Lite: An Open-source, Accessible, and Customizable 3D-printed Humanoid Robot'. arXiv:2504.17249, April 2025. Robotics: Science and Systems (RSS) 2025. UC Berkeley Hybrid Robotics Lab.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `actuator-electric-cycloidal`, `actuator-3d-printed-reducer`, `mechanism-3d-printed-platform`, `control-rl-policy`, `control-sim-to-real`

**Prior art notes:**

> Berkeley Humanoid Lite is the canonical sub-$5k open-hardware academic bipedal humanoid (RSS 2025). 1-year-deep prior art on: 3D-printed cycloidal reducer humanoid actuator (a specific architectural commitment), full open-source release of hardware + firmware + training, sub-$5k humanoid BOM, RL-controlled walking on a 3D-printed platform. **Direct shielding for free-humanoid-platform** — particularly the 3D-printed actuator path and any commercial claim on accessible humanoid hardware. Together with ToddlerBot and Berkeley Humanoid (full-size), establishes a deep open-academic substrate for any commercial humanoid platform claim.

**Sources:**

1. arXiv:2504.17249 April 2025.
2. RSS 2025 proceedings paper p062 (roboticsproceedings.org/rss21/p062.pdf).
3. Project page (lite.berkeley-humanoid.org).
4. GitHub: github.com/HybridRobotics/Berkeley-Humanoid-Lite.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `35dc1dd`.*
