---
title: "sensing-lidar"
parent: "Invalidity Contentions"
nav_order: 40
layout: default
---

# Invalidity Contention Packet — `sensing-lidar`

**Generated:** 2026-05-07  
**Cross-cut tag:** `sensing-lidar`  
**Entries:** 16 (14 commons-grade, 2 draft)  
**Earliest disclosure:** 2004  
**Most recent disclosure:** 2023-08

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `sensing-lidar`.

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

### 2004 — HUBO

- **id:** `hubo`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** KAIST, Hubo Lab (Jun-Ho Oh)
- **disclosure citation:** Park, Ill-Woo et al. 'Mechanical Design of Humanoid Robot Platform KHR-3 (HUBO).' IEEE-RAS Humanoids 2005.
- **disclosed subsystems:** `actuator-electric-harmonic-drive`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `mechanism-wheel-leg-hybrid`, `control-zmp-balancing`, `sensing-stereo-camera`, `sensing-lidar`, `sensing-force-torque`

**Prior art notes:**

> DRC-Hubo's 2015 win demonstrated transformer-style transitioning between bipedal and wheeled-knee modes for navigating both stairs and flat ground. Anticipates: hybrid locomotion modes in humanoids.

**Sources:**

1. Park, I.-W. et al. IEEE-RAS Humanoids 2005.
2. DARPA Robotics Challenge final report, 2015.

---

### 2010 — PR2

- **id:** `pr2`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** Willow Garage
- **disclosure citation:** Willow Garage. PR2 platform release, 2010.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `actuator-electric-series-elastic`, `control-mpc`, `sensing-stereo-camera`, `sensing-lidar`, `sensing-force-torque`, `sensing-imu`, `power-li-ion`, `software-ros1`

**Prior art notes:**

> PR2 was the platform around which ROS was originally built. Its hardware is significant prior art for omnidirectional wheeled mobile manipulation. ROS itself is even more significant prior art for robotics middleware.

**Sources:**

1. Willow Garage technical materials.
2. Quigley, M. et al. 'ROS: an open-source Robot Operating System.' ICRA Workshop 2009.

---

### 2012 — Toyota HSR

- **id:** `toyota-hsr`
- **corpus:** private
- **ip status:** patented
- **creator:** Toyota Motor Corporation Partner Robot Division
- **disclosure citation:** Yamamoto, T. et al. 'Development of Human Support Robot as the research platform of a domestic mobile manipulator.' ROBOMECH Journal 6:4, 2019. Earlier 2012 disclosure.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `control-mpc`, `sensing-stereo-camera`, `sensing-lidar`, `sensing-imu`, `power-li-ion`, `software-ros1`

**Prior art notes:**

> HSR's telescoping torso with whole-body control is significant prior art for domestic-context wheeled humanoid claims.

**Sources:**

1. Yamamoto, T. et al. ROBOMECH Journal 6:4, 2019.
2. Toyota HSR distribution program materials.

---

### 2013 — NASA Valkyrie

- **id:** `nasa-valkyrie`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** NASA Johnson Space Center, in collaboration with University of Texas at Austin and others
- **disclosure citation:** NASA Johnson Space Center, DARPA Robotics Challenge entry, 2013.
- **disclosed subsystems:** `actuator-electric-series-elastic`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `control-mpc`, `sensing-stereo-camera`, `sensing-lidar`, `sensing-force-torque`, `sensing-imu`, `software-ros1`, `power-li-ion`, `power-tethered`

**Prior art notes:**

> NASA Valkyrie's series-elastic actuator implementations and the IHMC-derived whole-body control work are foundational prior art. The robot was distributed to multiple universities and produced extensive open publications.

**Sources:**

1. Radford, N. et al. 'Valkyrie: NASA's First Bipedal Humanoid Robot.' Journal of Field Robotics 32(3), 2015.
2. NASA technical reports.

---

### 2013-07 — Atlas *(draft)*

- **id:** `atlas-boston-dynamics`
- **corpus:** private
- **ip status:** patented
- **creator:** Boston Dynamics
- **disclosure citation:** DARPA press release, July 2013, announcing Atlas as DRC platform.
- **disclosed subsystems:** `actuator-hydraulic`, `actuator-electric-direct-drive`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `control-mpc`, `sensing-stereo-camera`, `sensing-lidar`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> Boston Dynamics' patents are among the most-cited in the humanoid space and also among the most likely to be challenged on 102/103 grounds given the long academic prior art chain (Honda, AIST, KAIST, MIT). Worth dedicated patent-by-patent analysis.

**Sources:**

1. DARPA Robotics Challenge documentation.
2. Boston Dynamics technical blog posts.

---

### 2014-06 — Pepper

- **id:** `pepper-softbank`
- **corpus:** private
- **ip status:** patented
- **creator:** SoftBank Robotics (formerly Aldebaran)
- **disclosure citation:** SoftBank Robotics public reveal of Pepper, June 2014.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `mechanism-anthropomorphic-hand`, `control-behavior-tree`, `sensing-stereo-camera`, `sensing-lidar`, `sensing-imu`, `power-li-ion`, `software-ros1`

**Prior art notes:**

> Pepper is foundational prior art for wheeled-base humanoid social robots. The omnidirectional wheeled base design has been widely cited.

**Sources:**

1. SoftBank Robotics technical materials.
2. Pepper deployment case studies.

---

### 2014-06 — Atlas academic publications (Kuindersma et al., DRC era)

- **id:** `atlas-academic-disclosures`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Scott Kuindersma, Russ Tedrake, Robin Deits, Maurice Fallon, Andrés Valenzuela, Hongkai Dai, Frank Permenter, Twan Koolen, Pat Marion; MIT CSAIL Robot Locomotion Group (DRC Atlas team)
- **disclosure citation:** Kuindersma, Scott; Permenter, Frank; Tedrake, Russ. 'An efficiently solvable quadratic program for stabilizing dynamic locomotion.' IEEE International Conference on Robotics and Automation (ICRA), Hong Kong, June 2014, pp. 2589-2594. DOI: 10.1109/ICRA.2014.6907230. Consolidated Atlas-on-DRC paper: Kuindersma, S.; Deits, R.; Fallon, M.; Valenzuela, A.; Dai, H.; Permenter, F.; Koolen, T.; Marion, P.; Tedrake, R. 'Optimization-based locomotion planning, estimation, and control design for the Atlas humanoid robot.' Autonomous Robots 40(3): 429-455, March 2016. DOI: 10.1007/s10514-015-9479-3.
- **disclosed subsystems:** `actuator-hydraulic`, `mechanism-bipedal-locomotion`, `control-mpc`, `control-zmp-balancing`, `control-reduced-order-model`, `sensing-stereo-camera`, `sensing-lidar`, `sensing-imu`, `sensing-force-torque`

**Prior art notes:**

> The MIT DRC Atlas academic publication trail (Kuindersma-Tedrake et al. 2014-2016) is distinct from the Boston Dynamics Atlas product entry (atlas-boston-dynamics) and from the Sentis-Khatib WBOSC entry: it is the canonical academic disclosure of the actually-deployed Atlas controller stack as fielded at the DARPA Robotics Challenge Finals (June 2015). Anticipates with element-by-element specificity: (1) whole-body QP-based inverse-dynamics control on a hydraulically-actuated humanoid platform — directly relevant to commercial claims on QP-based humanoid IP (every modern humanoid runs a derivative); (2) the IRIS-regions mixed-integer convex footstep planner — relevant to claims on footstep-planning humanoid IP; (3) iterative SQP trajectory optimization with contact schedule — anticipates claims overlapping Crocoddyl (mastalli-crocoddyl-2020) and DDP approaches; (4) the consolidated end-to-end stack documentation in AURO 2016 — the most complete public disclosure of a working DRC-class humanoid control architecture. Drake source code accompanies the publications under BSD license. Modern QP-IDC-based humanoid IP filings face this 12-year-deep academic anchor with full implementation disclosure.

**Sources:**

1. Kuindersma, S.; Permenter, F.; Tedrake, R. 'An efficiently solvable quadratic program for stabilizing dynamic locomotion.' ICRA 2014: 2589-2594. DOI: 10.1109/ICRA.2014.6907230.
2. Kuindersma, S. et al. 'Optimization-based locomotion planning, estimation, and control design for the Atlas humanoid robot.' Autonomous Robots 40(3): 429-455, 2016. DOI: 10.1007/s10514-015-9479-3.
3. Deits, R. and Tedrake, R. 'Footstep planning on uneven terrain with mixed-integer convex optimization.' IEEE-RAS Humanoids 2014.
4. Drake source code: https://drake.mit.edu, BSD-3-Clause license (companion to the Atlas papers).

---

### 2016 — ANYmal

- **id:** `anymal`
- **corpus:** private
- **ip status:** patented
- **creator:** ANYbotics, ETH Zurich Robotic Systems Lab
- **disclosure citation:** Hutter, M. et al. 'ANYmal — a highly mobile and dynamic quadrupedal robot.' IROS 2016.
- **disclosed subsystems:** `actuator-electric-series-elastic`, `mechanism-quadrupedal-locomotion`, `control-rl-policy`, `control-sim-to-real`, `sensing-stereo-camera`, `sensing-lidar`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> ANYbotics SEA design heavily anticipated by NASA Valkyrie and Robonaut SEA work. ETH RSL academic publications provide open prior art for many control claims.

**Sources:**

1. Hutter, M. et al. IROS 2016.
2. ANYbotics company materials.

---

### 2017-12 — Black Mirror 'Metalhead' autonomous quadruped killer

- **id:** `black-mirror-metalhead-2017`
- **corpus:** fictional
- **ip status:** public-domain
- **creator:** Charlie Brooker (writer), David Slade (director), House of Tomorrow / Netflix
- **disclosure citation:** Black Mirror, Series 4, Episode 5, 'Metalhead.' Written by Charlie Brooker; directed by David Slade; released on Netflix 29 December 2017.
- **disclosed subsystems:** `mechanism-quadrupedal-locomotion`, `actuator-electric-quasi-direct-drive`, `sensing-lidar`, `sensing-stereo-camera`, `sensing-imu`, `control-rl-policy`, `power-li-ion`

**Prior art notes:**

> 'Metalhead' is the canonical 2017 mass-media anchor for autonomous quadruped lethal-defense robots and was directly modeled on the Boston Dynamics SpotMini reveal. It anticipates with full specificity: (1) claims on quadruped robots equipped with weapon payloads operating in fully-autonomous lethal-engagement mode — the episode dramatizes exactly this throughout 41 minutes; (2) claims on shrapnel-tag persistent-tracker payloads that mark a target for prolonged pursuit — this is the headline mechanism of the second act; (3) claims on SpotMini-class compact electric quadruped morphology with integrated manipulator arm — the visual design and Brooker's published commentary explicitly cite Boston Dynamics inspiration. Released on Netflix with timestamped 29 December 2017 distribution to ~109 million subscribers.

**Sources:**

1. Black Mirror S4E5 'Metalhead', Netflix, 29 December 2017.
2. Brooker, C. interview in 'Inside Black Mirror' (Crown Archetype, 2018) confirming SpotMini visual reference.

---

### 2018 — Ghost Robotics Vision 60

- **id:** `ghost-robotics-vision-60`
- **corpus:** private
- **ip status:** patented
- **creator:** Ghost Robotics
- **disclosure citation:** Ghost Robotics Vision 60 release, 2018.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `mechanism-quadrupedal-locomotion`, `control-mpc`, `sensing-stereo-camera`, `sensing-lidar`, `sensing-imu`, `power-li-ion`, `software-ros1`

**Prior art notes:**

> Ghost Robotics derives from Penn's Kod*lab academic quadruped work. The legged-robot patents face the same MIT Cheetah / ANYmal / Penn Kod*lab prior art chain as other quadrupeds.

**Sources:**

1. Ghost Robotics company materials.

---

### 2018-09 — HRP-5P

- **id:** `hrp-5p`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** AIST and Kawada Industries
- **disclosure citation:** Kaneko, K. et al. 'Humanoid Robot HRP-5P: An Electrically Actuated Humanoid Robot With High-Power and Wide-Range Joints.' IEEE Robotics and Automation Letters 4(2), 2019.
- **disclosed subsystems:** `actuator-electric-harmonic-drive`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `control-mpc`, `sensing-stereo-camera`, `sensing-lidar`, `sensing-force-torque`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> HRP-5P's construction-task demonstrations and high-power actuator disclosures are among the most thoroughly published examples of humanoid construction work. Anticipates many subsequent industrial humanoid claims.

**Sources:**

1. Kaneko, K. et al. IEEE RA-L 4(2), 2019.

---

### 2018-10 — Stanford JackRabbot 2 (JR-2) wheeled-arm research robot

- **id:** `stanford-jr2-2018`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Stanford Vision and Learning Lab (Silvio Savarese et al.)
- **disclosure citation:** Martín-Martín, Roberto, Patel, Mihir, Rezatofighi, Hamid, Shenoi, Abhijeet, Gwak, JunYoung, Frankel, Eric, Sadeghian, Amir, Savarese, Silvio. 'JRDB: A Dataset and Benchmark for Visual Perception for Navigation in Human Environments.' arXiv:1910.11792, October 2019. Robot platform first disclosed: Stanford Vision and Learning Lab, October 2018 release announcement; JRDB dataset released alongside.
- **disclosed subsystems:** `mechanism-wheeled-balancing`, `actuator-electric-harmonic-drive`, `sensing-stereo-camera`, `sensing-lidar`, `sensing-imu`, `software-ros1`

**Prior art notes:**

> Stanford JR-2 (2018) is a canonical academic wheeled-arm research humanoid for social navigation research, with associated public benchmark dataset (JRDB). Anticipates with full specificity: (1) claims on wheeled-balancing humanoids with dual mounted manipulators at human shoulder height — JR-2's Segway-base + dual Kinova architecture is a published exemplar; (2) claims on 360° multi-modal sensor fusion (lidar+cameras+audio) for human-environment navigation — JR-2 carries the full sensor stack; (3) claims on human-aware social navigation benchmarks paired with platform — JRDB releases 64 minutes of annotated multi-modal data alongside the platform. Stanford SVL hosts CAD/sensor specs and the JRDB benchmark openly. Modern wheeled-humanoid IP filings (Apptronik Apollo, Agility Cassie/Digit base, 1X NEO) face this 8-year-deep academic anchor.

**Sources:**

1. Martín-Martín, R. et al. 'JRDB: A Dataset and Benchmark for Visual Perception for Navigation in Human Environments.' arXiv:1910.11792, 2019.
2. Stanford Vision and Learning Lab JR-2 announcement, October 2018.
3. JRDB project page: jrdb.erc.monash.edu

---

### 2019-01 — Digit

- **id:** `agility-digit`
- **corpus:** private
- **ip status:** patented
- **creator:** Agility Robotics
- **disclosure citation:** Agility Robotics public reveal, CES January 2019.
- **disclosed subsystems:** `actuator-electric-series-elastic`, `mechanism-bipedal-locomotion`, `control-reduced-order-model`, `control-rl-policy`, `sensing-lidar`, `sensing-stereo-camera`, `sensing-imu`, `power-li-ion`, `software-ros1`

**Prior art notes:**

> Cassie/Digit derive from Oregon State University academic work (Hurst lab); the academic publications constitute substantial prior art for the bipedal control claims.

**Sources:**

1. Agility Robotics website.
2. Hurst, J. et al. OSU dynamic locomotion publications.

---

### 2019-09 — Diligent Moxi

- **id:** `diligent-moxi`
- **corpus:** private
- **ip status:** patented
- **creator:** Diligent Robotics
- **disclosure citation:** Diligent Robotics public reveal of Moxi, September 2019.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `control-behavior-tree`, `sensing-stereo-camera`, `sensing-lidar`, `power-li-ion`, `software-ros1`

**Prior art notes:**

> Diligent's claims around mobile manipulation in healthcare environments face extensive prior art from PR2, HSR, and academic mobile manipulation literature.

**Sources:**

1. Diligent Robotics company materials.

---

### 2022-09 — ANYmal-D industrial quadruped (ETH RSL / ANYbotics)

- **id:** `anymal-d-eth-rsl-2022`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** ANYbotics AG / ETH Zürich Robotic Systems Lab (Marco Hutter)
- **disclosure citation:** ANYbotics product disclosure ANYmal D, September 2022; technical updates in Miki, Takahiro et al. 'Learning robust perceptive locomotion for quadrupedal robots in the wild.' Science Robotics 7(62), 2022; Hoeller, David et al. 'ANYmal Parkour: Learning agile navigation for quadrupedal robots.' Science Robotics 9(88), 2024.
- **disclosed subsystems:** `mechanism-quadrupedal-locomotion`, `actuator-electric-series-elastic`, `actuator-electric-harmonic-drive`, `sensing-imu`, `sensing-lidar`, `sensing-stereo-camera`, `sensing-proprioceptive-actuator`, `control-rl-policy`, `control-sim-to-real`, `software-ros2`

**Prior art notes:**

> ANYmal-D is the production-deployed industrial quadruped of the 2022-2024 period and the platform for the headline RSL/ANYbotics RL-locomotion papers in Science Robotics. It anticipates with full specificity: (1) claims on perceptive-locomotion RL policies trained in simulation and transferred to outdoor industrial terrain — Miki Sci.Rob. 2022 publishes the teacher-student distillation pipeline running on this hardware; (2) claims on agile parkour-class learned locomotion — Hoeller Sci.Rob. 2024 publishes the policy on ANYmal-D; (3) claims on series-elastic torque-controlled quadruped joints in IP67 industrial enclosures — ANYdrive disclosed at IROS 2018 with hardware refresh on D-variant. Modern legged-robot IP claims face this timestamped industrial-deployment anchor.

**Sources:**

1. Miki, T. et al. 'Learning robust perceptive locomotion for quadrupedal robots in the wild.' Science Robotics 7(62), 2022.
2. Hoeller, D. et al. 'ANYmal Parkour.' Science Robotics 9(88), 2024.
3. ANYbotics ANYmal D datasheet, 2022.

---

### 2023-08 — Unitree H1 *(draft)*

- **id:** `unitree-h1`
- **corpus:** private
- **ip status:** patented
- **creator:** Unitree Robotics
- **disclosure citation:** Unitree Robotics public reveal, August 2023.
- **disclosed subsystems:** `actuator-electric-quasi-direct-drive`, `mechanism-bipedal-locomotion`, `control-rl-policy`, `sensing-stereo-camera`, `sensing-lidar`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> Unitree's actuator IP largely derives from quadruped work (Go1, Aliengo) which is itself heavily anticipated by MIT Mini Cheetah QDD lineage.

**Sources:**

1. Unitree.com
2. Unitree technical specifications.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `f6d8987`.*
