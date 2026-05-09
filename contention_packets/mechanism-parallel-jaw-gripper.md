---
title: "mechanism-parallel-jaw-gripper"
parent: "Invalidity Contentions"
nav_order: 184
layout: default
---

# Invalidity Contention Packet — `mechanism-parallel-jaw-gripper`

**Generated:** 2026-05-09  
**Cross-cut tag:** `mechanism-parallel-jaw-gripper`  
**Entries:** 5 (5 commons-grade, 0 draft)  
**Earliest disclosure:** 2008-01  
**Most recent disclosure:** 2025-11

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `mechanism-parallel-jaw-gripper`.

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

### 2009-01 — Festo FinGripper / Adaptive Bionic Gripper (Fin Ray Effect)

- **id:** `festo-finray-fingripper-2009`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Festo Bionic Learning Network + EvoLogics GmbH (Berlin); Leif Kniese (Fin Ray Effect inventor)
- **disclosure citation:** Festo AG & Co. KG Bionic Learning Network (Esslingen, Germany). Adaptive Bionic Gripper / FinGripper reveal 2009. Based on the Fin Ray Effect® mechanical principle developed by EvoLogics GmbH (Berlin) and Leif Kniese, derived from study of fish-fin biomechanics. Fin Ray Effect now ubiquitous across global soft-finger gripper market.
- **disclosed subsystems:** `mechanism-fin-ray-finger`, `mechanism-passive-compliant-gripper`, `mechanism-parallel-jaw-gripper`

**Prior art notes:**

> Festo FinGripper / Adaptive Bionic Gripper (Festo + EvoLogics Berlin 2009+) commercialized the Fin Ray Effect adaptive finger geometry. 16-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from passive-compliant fish-fin-inspired adaptive fingers. The Fin Ray Effect mechanism now appears in dozens of academic + commercial soft-finger grippers worldwide.

**Sources:**

1. festo.com/us/en/e/about-festo/research-and-development/bionic-learning-network/
2. EvoLogics GmbH (Berlin) Fin Ray Effect® documentation.

---

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

### 2016-09 — SCHUNK Co-act JL1 collaborative gripper

- **id:** `schunk-coact-jl1-2016`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** SCHUNK GmbH & Co. KG (Lauffen am Neckar, Germany)
- **disclosure citation:** SCHUNK GmbH & Co. KG (Lauffen am Neckar, Germany; founded 1945). Co-act JL1 reveal Hannover Messe 2016 (Hermes Award winner 2017). EGP-C collaborative-classified electric gripper 2018. The first DGUV-certified gripping module for human-robot collaboration with intent-display LEDs (ISO/TS 15066 compliant).
- **disclosed subsystems:** `mechanism-parallel-jaw-gripper`, `mechanism-collaborative-gripper`, `sensing-capacitive-proximity`, `control-collaborative-safety`

**Prior art notes:**

> SCHUNK Co-act JL1 (SCHUNK Lauffen 2016+) is the first DGUV-certified collaborative gripper module. 9-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from intent-display gripper interfaces, capacitive-proximity collaborative grippers, or ISO/TS 15066-compliant biomechanical-limit grasping. SCHUNK SVH (corpus entry) is the dexterous-hand counterpart; Co-act JL1 is the simple-collaborative-gripper counterpart.

**Sources:**

1. schunk.com/de_en/gripping-systems/30-years-schunk-grippers/
2. schunk.com/us/en/gripping-systems/parallel-gripper/co-act-egp-c/c/PGR_3995

---

### 2025-11 — LeFlexiTac (Columbia RoboPIL tactile-LeRobot)

- **id:** `leflexitac-columbia-2025`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** Columbia University RoboPIL lab; Naian Tao, Yifan He, Wesley Maa, Binghao Huang, Yunzhu Li
- **disclosure citation:** Tao, N., He, Y., Maa, W., Huang, B., Li, Y. 'LeFlexiTac: Giving Robots a Sense of Touch'. Columbia University RoboPIL Blog, May 2026. Public GitHub fork of HuggingFace LeRobot at github.com/TNA001-AI/lerobot_tactile, repo created 2025-11-14, Apache License 2.0. Project page: tna001-ai.github.io/LeFlexiTac/.
- **disclosed subsystems:** `sensing-tactile-fingertip`, `sensing-vision-tactile`, `control-vla-tactile-augmented`, `control-imitation-learning`, `mechanism-parallel-jaw-gripper`

**Prior art notes:**

> LeFlexiTac (Columbia RoboPIL November 2025+; blog disclosure May 2026) is the canonical open-source tactile-augmented LeRobot extension demonstrating tactile sensing as an additive modality across four distinct policy architectures (ACT, Diffusion Policy, Pi0.5, SmolVLA). Apache 2.0 open-permissive prior art. Direct shielding for any commercial humanoid claim deriving from: (1) tactile observation channels in VLA / imitation-learning policy frameworks; (2) tactile-augmented LeRobot / SO-ARM platforms; (3) the architectural pattern of feeding a single tactile stream into multiple policy backbones. Lineage descends from GelSight (corpus gelsight, MIT 2009) for vision-tactile sensing and from HuggingFace LeRobot (corpus huggingface-lerobot-2024) for the framework substrate.

**Sources:**

1. github.com/TNA001-AI/lerobot_tactile (Apache 2.0; created 2025-11-14).
2. tna001-ai.github.io/LeFlexiTac/ (project page).
3. Tao, N., He, Y., Maa, W., Huang, B., Li, Y. 'LeFlexiTac: Giving Robots a Sense of Touch'. Columbia University RoboPIL Blog, 2026.
4. Parent repo: github.com/huggingface/lerobot.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `2fbde5f`.*
