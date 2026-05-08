---
title: "mechanism-3d-printed-platform"
parent: "Invalidity Contentions"
nav_order: 116
layout: default
---

# Invalidity Contention Packet — `mechanism-3d-printed-platform`

**Generated:** 2026-05-08  
**Cross-cut tag:** `mechanism-3d-printed-platform`  
**Entries:** 4 (4 commons-grade, 0 draft)  
**Earliest disclosure:** 2019-04  
**Most recent disclosure:** 2026-01

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `mechanism-3d-printed-platform`.

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

### 2019-04 — Stanford Pupper / Doggo open-source quadruped

- **id:** `stanford-pupper-doggo-2019`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Stanford Student Robotics; Nathan Kau, Aaron Schultz et al.
- **disclosure citation:** Stanford Student Robotics. Stanford Doggo open-source quadruped reveal April 2019. Subsequent: Stanford Pupper (smaller variant). stanfordstudentrobotics.org / hands-on-robotics.stanford.edu. Open-hardware design under MIT license.
- **disclosed subsystems:** `mechanism-quadrupedal-locomotion`, `actuator-electric`, `mechanism-3d-printed-platform`

**Prior art notes:**

> Stanford Pupper / Doggo (Stanford Student Robotics 2019+) is the canonical Stanford educational open-source quadruped. 6-year-deep open-permissive prior art. The Stanford academic counterpart to Unitree Go1/Go2 (corpus) for educational quadruped robotics. Direct shielding for any commercial quadruped claim deriving from low-cost open-hardware educational platforms.

**Sources:**

1. Stanford Student Robotics (stanfordstudentrobotics.org).
2. Hands-on-Robotics Stanford (hands-on-robotics.stanford.edu).
3. GitHub: github.com/Nate711/StanfordDoggoProject.

---

### 2025-02 — ToddlerBot

- **id:** `stanford-toddlerbot-2025`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Stanford Robotics Lab; Haochen Shi, Weizhuo Wang, Shuran Song, C. Karen Liu
- **disclosure citation:** Shi, H., Wang, W., Song, S., Liu, C. K. 'ToddlerBot: Open-Source ML-Compatible Humanoid Platform for Loco-Manipulation'. arXiv:2502.00893, February 2025. Conference on Robot Learning (CoRL) 2025 oral. Stanford Robotics Lab.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-arm`, `mechanism-3d-printed-platform`, `control-rl-policy`, `control-imitation-learning`, `control-sim-to-real`, `control-loco-manipulation`

**Prior art notes:**

> ToddlerBot is Stanford's canonical sub-$6k open-hardware ML-compatible humanoid (CoRL 2025 oral). Establishes 1-year-deep open-academic prior art for: integrated loco-manipulation policy training on an open humanoid platform, transferable motor system-ID for sim-to-real without hand-tuning, 30-DoF anthropomorphic full-body at sub-$6k. Direct shielding for any commercial claim on integrated full-body humanoid policy training, particularly any 'one policy controls the whole body' claim. Together with Berkeley Humanoid Lite, establishes the open-academic baseline for sub-$10k humanoid robotics.

**Sources:**

1. Shi, Wang, Song, Liu. arXiv:2502.00893 February 2025.
2. CoRL 2025 proceedings (proceedings.mlr.press/v305/shi25a.html).
3. Project page (toddlerbot.github.io).
4. GitHub: github.com/hshi74/toddlerbot.

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

### 2026-01 — Decoupled STAR (DSTAR)

- **id:** `dstar-zarrouk-2026`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Ben-Gurion University; Tomer Siboni, Matan Coronel, David Zarrouk
- **disclosure citation:** Siboni, T., Coronel, M., Zarrouk, D. 'Design and Modeling of a Reconfigurable Robot: Decoupled STAR (DSTAR)'. IEEE Robotics and Automation Letters vol. 11 no. 1, January 2026, pp. 882-889. DOI: 10.1109/LRA.2025.3634888. Ben-Gurion University, Department of Mechanical Engineering / Bio-inspired Robotics Lab. Funded by Helmsley Charitable Trust + Marcus Endowment Fund.
- **disclosed subsystems:** `mechanism-sprawl-tunable`, `mechanism-wheel-leg-hybrid`, `mechanism-four-bar-extension`, `mechanism-reconfigurable`, `mechanism-3d-printed-platform`, `control-mode-switching`, `control-open-loop-gait`

**Prior art notes:**

> DSTAR is the most recent STAR-family member, published IEEE RA-L January 2026. Establishes very-recent (4-month-deep) open-academic prior art for: decoupled-FBEM wheel-leg reconfigurable robotics, sideways rolling via asymmetric mechanical configuration, COM-shifting via independent left/right leg actuation, 18-20 cm obstacle traversal in palm-sized class. Directly anticipates free-humanoid-centaur's wheel-leg hybrid mode-switching commitment, free-humanoid-wheeled's obstacle-climbing requirement, and any commercial humanoid claim on reconfigurable wheel-leg architectures (including any mid-size extrapolation of DSTAR to humanoid scale). The full STAR family lineage (Berkeley original 2013 → Zarrouk RSTAR 2019 → AmphiSTAR 2023 → DSTAR 2026) provides 13-year-deep open-academic continuous publication coverage of every architectural element. Highly relevant for shoal dock-A wetland service: DSTAR's terrain-adaptation gait library is a published reference design for centaur-class wetland mode-transition.

**Sources:**

1. Siboni, T., Coronel, M., Zarrouk, D. IEEE RA-L 11(1) January 2026, pp. 882-889. DOI 10.1109/LRA.2025.3634888.
2. Ben-Gurion University Bio-inspired and Medical Robotics Lab (bgu.ac.il/zarrouklab).
3. Supplementary video material via IEEE Xplore.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `bf3c8f5`.*
