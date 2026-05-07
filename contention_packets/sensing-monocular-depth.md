---
title: "sensing-monocular-depth"
parent: "Invalidity Contentions"
nav_order: 41
layout: default
---

# Invalidity Contention Packet — `sensing-monocular-depth`

**Generated:** 2026-05-06  
**Cross-cut tag:** `sensing-monocular-depth`  
**Entries:** 7 (4 commons-grade, 3 draft)  
**Earliest disclosure:** 2009-09  
**Most recent disclosure:** 2025-10

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `sensing-monocular-depth`.

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

### 2009-09 — GelSight

- **id:** `gelsight`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Micah Kimo Johnson, Edward Adelson; later Wenzhen Yuan, Siyuan Dong; MIT Media Lab and CSAIL
- **disclosure citation:** Johnson, M.K. and Adelson, E.H. 'Retrographic sensing for the measurement of surface texture and shape'. IEEE CVPR 2009, June 2009; consolidated in Yuan, W., Dong, S., Adelson, E.H. 'GelSight: high-resolution robot tactile sensors for estimating geometry and force'. Sensors 17(12): 2762, 2017.
- **disclosed subsystems:** `sensing-tactile-fingertip`, `sensing-monocular-depth`

**Prior art notes:**

> GelSight is the foundational academic disclosure of vision-based tactile sensing. Anticipates: (1) vision-based fingertip tactile sensing using photometric stereo — directly relevant to all modern vision-tactile humanoid claims (DIGIT, MetaTouch, etc.); (2) sub-millimeter 3D-surface-from-image as the canonical sensor output — relevant to high-resolution-tactile claims; (3) gel-elastomer with oblique multi-color illumination as the sensor architecture — relevant to vision-tactile sensor claims. The 2009 CVPR paper and 2017 Sensors paper are heavily cited; the design has been replicated in ~50 academic publications. Modern vision-tactile humanoid IP faces this as 102 prior art.

**Sources:**

1. Johnson, M.K. and Adelson, E.H. 'Retrographic sensing'. IEEE CVPR 2009.
2. Yuan, W. et al. 'GelSight'. Sensors 17(12), 2017.
3. Li, R. and Adelson, E.H. 'Sensing and recognizing surface textures using a GelSight sensor'. IEEE CVPR 2013.

---

### 2013 — Crazyflie

- **id:** `crazyflie`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** Bitcraze AB
- **disclosure citation:** Bitcraze AB. Crazyflie 1.0 release, 2013.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `sensing-imu`, `sensing-monocular-depth`, `power-li-po`

**Prior art notes:**

> Open hardware aerial platform with extensive academic citation. Anticipates: open nano-UAV designs broadly.

**Sources:**

1. bitcraze.io
2. Crazyflie GitHub repositories.

---

### 2020-12 — DIGIT

- **id:** `digit-meta`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Lambeta, Chou, Tian, Yang, Maloon, Most, Stroud, Santos, Byagowi, Kammerer, Jayaraman, Calandra; Facebook AI Research (now Meta AI)
- **disclosure citation:** Lambeta, M., Chou, P.-W., Tian, S., Yang, B., Maloon, B., Most, V.R., Stroud, D., Santos, R., Byagowi, A., Kammerer, G., Jayaraman, D., Calandra, R. 'DIGIT: a novel design for a low-cost compact high-resolution tactile sensor with application to in-hand manipulation'. IEEE Robotics and Automation Letters 5(3): 3838-3845, 2020.
- **disclosed subsystems:** `sensing-tactile-fingertip`, `sensing-monocular-depth`

**Prior art notes:**

> DIGIT extends GelSight to a low-cost open-source form factor. Anticipates: (1) low-cost open-source vision-tactile fingertip — directly relevant to claims on commercial humanoid hand patents that incorporate vision-tactile sensing; (2) form-factor integration of vision-tactile sensors into commodity robot hands — relevant to integrated humanoid hand IP. DIGIT's open-source release (CAD, firmware, software stack on GitHub) creates substantial prior art coverage of integration patterns. Heavily cited in subsequent dexterous-manipulation work.

**Sources:**

1. Lambeta, M. et al. 'DIGIT'. IEEE RA-L 5(3), 2020.
2. DIGIT GitHub repository: https://github.com/facebookresearch/digit-design

---

### 2021-06 — Unitree Go1

- **id:** `unitree-go1`
- **corpus:** private
- **ip status:** patented
- **creator:** Unitree Robotics
- **disclosure citation:** Unitree Robotics Go1 reveal, June 2021.
- **disclosed subsystems:** `actuator-electric-quasi-direct-drive`, `actuator-bldc-controller`, `mechanism-quadrupedal-locomotion`, `control-mpc`, `control-rl-policy`, `sensing-monocular-depth`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> Unitree Go1 actuator design is heavily anticipated by MIT Cheetah QDD prior art (Wensing 2017, Katz 2019). Pricing-driven commodification rather than novel IP.

**Sources:**

1. Unitree.com
2. Unitree technical specifications.

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

### 2024-12 — EngineAI PM01 *(draft)*

- **id:** `engineai-pm01`
- **corpus:** private
- **ip status:** patented
- **creator:** EngineAI
- **disclosure citation:** EngineAI public reveal of PM01, December 2024.
- **disclosed subsystems:** `actuator-electric-quasi-direct-drive`, `mechanism-bipedal-locomotion`, `control-rl-policy`, `control-sim-to-real`, `sensing-monocular-depth`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> EngineAI QDD actuation anticipated by MIT Cheetah lineage.

**Sources:**

1. EngineAI company materials.
2. Chinese-language tech press coverage.

---

### 2025-10 — Unitree H2 *(draft)*

- **id:** `unitree-h2`
- **corpus:** private
- **ip status:** patented
- **creator:** Unitree Robotics
- **disclosure citation:** Unitree Robotics H2 reveal, October 2025.
- **disclosed subsystems:** `actuator-electric-quasi-direct-drive`, `actuator-electric-harmonic-drive`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `control-rl-policy`, `sensing-monocular-depth`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> H2 builds on H1 architecture; same prior art chain back through Mini Cheetah.

**Sources:**

1. Unitree Robotics public materials, October 2025.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `0249808`.*
