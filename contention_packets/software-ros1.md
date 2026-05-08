---
title: "software-ros1"
parent: "Invalidity Contentions"
nav_order: 152
layout: default
---

# Invalidity Contention Packet — `software-ros1`

**Generated:** 2026-05-08  
**Cross-cut tag:** `software-ros1`  
**Entries:** 18 (18 commons-grade, 0 draft)  
**Earliest disclosure:** 2002  
**Most recent disclosure:** 2019-09

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `software-ros1`.

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

### 2002 — HRP-2

- **id:** `hrp-2`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** AIST (National Institute of Advanced Industrial Science and Technology), Kawada Industries
- **disclosure citation:** Kaneko, K. et al. 'Design of prototype humanoid robotics platform for HRP.' IROS 2002.
- **disclosed subsystems:** `actuator-electric-harmonic-drive`, `mechanism-bipedal-locomotion`, `control-zmp-balancing`, `sensing-stereo-camera`, `sensing-force-torque`, `sensing-imu`, `software-openhrp`, `software-ros1`

**Prior art notes:**

> OpenHRP is itself foundational prior art for open robotics simulation frameworks. HRP-2 was among the first humanoids to publicly demonstrate falling-and-recovering behaviors.

**Sources:**

1. Kaneko, K. et al. IROS 2002.
2. Kanehiro, F. et al. 'OpenHRP: Open Architecture Humanoid Robotics Platform.' IJRR 23(2), 2004.

---

### 2006 — NAO

- **id:** `nao`
- **corpus:** private
- **ip status:** patented
- **creator:** Aldebaran Robotics (later SoftBank Robotics, then UBT)
- **disclosure citation:** Gouaillier, D. et al. 'Mechatronic design of NAO humanoid.' ICRA 2009.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `control-zmp-balancing`, `control-behavior-tree`, `sensing-stereo-camera`, `sensing-imu`, `power-li-ion`, `software-ros1`

**Prior art notes:**

> NAO's mechatronic design publication is well-cited prior art. The platform's wide academic distribution since 2006 makes its design choices broadly disclosed.

**Sources:**

1. Gouaillier, D. et al. ICRA 2009.
2. Aldebaran/SoftBank technical materials.

---

### 2010 — DARwIn-OP

- **id:** `darwin-op`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** Robotis Co. with University of Pennsylvania, Virginia Tech, Purdue
- **disclosure citation:** Ha, I. et al. 'Development of Open Humanoid Platform DARwIn-OP.' SICE 2011.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `mechanism-bipedal-locomotion`, `control-behavior-tree`, `control-zmp-balancing`, `sensing-stereo-camera`, `sensing-imu`, `power-li-po`, `software-ros1`

**Prior art notes:**

> DARwIn-OP is foundational prior art for fully-open small-scale humanoid platforms. Predates Poppy by several years for the academic-open category.

**Sources:**

1. Ha, I. et al. SICE 2011.
2. DARwIn-OP project documentation.

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

### 2012-04 — CMU HERB (Home Exploring Robotic Butler)

- **id:** `cmu-herb-srinivasa-2012`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Siddhartha Srinivasa et al., Carnegie Mellon Personal Robotics Lab / Intel Labs Pittsburgh
- **disclosure citation:** Srinivasa, Siddhartha S., Berenson, Dmitry, Cakmak, Maya, Collet, Alvaro, Dogar, Mehmet R., Dragan, Anca D., Knepper, Ross A., Niemueller, Tim, Strabala, Kyle, Vande Weghe, Mike, Ziegler, Julius. 'HERB 2.0: Lessons Learned from Developing a Mobile Manipulator for the Home.' Proceedings of the IEEE 100(8): 2410-2428, August 2012. Original disclosure: Srinivasa, S. et al. 'HERB: a home exploring robotic butler.' Autonomous Robots 28(1): 5-20, January 2010.
- **disclosed subsystems:** `actuator-electric-tendon-driven`, `mechanism-anthropomorphic-hand`, `mechanism-underactuated-grasping`, `control-mpc`, `sensing-stereo-camera`, `sensing-force-torque`, `software-ros1`

**Prior art notes:**

> CMU HERB is one of the most extensively-published academic mobile-manipulator humanoid platforms (>50 papers across 2008-2018). Anticipates with full specificity: (1) claims on home-environment dual-arm humanoid manipulation — HERB's headline contribution including kitchen/office task suite, fridge/microwave/dishwasher manipulation; (2) claims on legible/predictable HRI motion synthesis — Dragan-Srinivasa 2013 'Legibility and Predictability of Robot Motion' is part of the HERB program and anticipates current humanoid social-motion IP; (3) claims on cable-driven backdrivable arms with underactuated 3-finger hands for home manipulation — Barrett WAM + BH-280 are the explicit instantiation; (4) claims on manipulation-among-movable-obstacles planning. Proceedings of IEEE article and Autonomous Robots paper provide deeply-cited timestamped disclosure. Modern home-humanoid IP filings (1X NEO Gamma, Figure 02 home demos) face this 14-year-deep academic anchor.

**Sources:**

1. Srinivasa, S. et al. 'HERB 2.0.' Proc. IEEE 100(8): 2410-2428, 2012.
2. Srinivasa, S. et al. 'HERB: a home exploring robotic butler.' Autonomous Robots 28(1): 5-20, 2010.
3. Dragan, A., Lee, K., Srinivasa, S. 'Legibility and Predictability of Robot Motion.' HRI 2013.

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

### 2013 — REEM-C

- **id:** `reem-c`
- **corpus:** private
- **ip status:** patented
- **creator:** PAL Robotics
- **disclosure citation:** PAL Robotics REEM-C release, 2013.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `control-zmp-balancing`, `sensing-stereo-camera`, `sensing-force-torque`, `power-li-ion`, `software-ros1`

**Prior art notes:**

> REEM-C distributed to multiple research labs; design characteristics openly published.

**Sources:**

1. PAL Robotics company materials.
2. Academic publications by REEM-C users.

---

### 2014-05 — CMU Personal Robotics Lab Andy / HERB-2 follow-on platform

- **id:** `cmu-andy-herb2-srinivasa-2014`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Siddhartha Srinivasa, Anca Dragan, J. Andrew Bagnell, and the CMU Personal Robotics Lab
- **disclosure citation:** Srinivasa, Siddhartha S. et al. 'HERB 2.0: Lessons Learned from Developing a Mobile Manipulator for the Home.' Proceedings of the IEEE, vol. 100, no. 8, 2012; subsequent Andy disclosures: Dragan, Anca and Srinivasa, S. 'A Policy-Blending Formalism for Shared Control.' IJRR 32(7), 2013; Bagnell et al. CHIMP/Andy whole-body manipulation reports 2013-2015.
- **disclosed subsystems:** `mechanism-underactuated-grasping`, `actuator-electric-tendon-driven`, `sensing-force-torque`, `sensing-stereo-camera`, `control-teleoperation`, `software-ros1`

**Prior art notes:**

> The Andy / HERB-2 generation extends HERB-1 with formal shared-autonomy theory and is the survey-of-record for bimanual mobile-manipulator home robots in 2012-2015. It anticipates with full specificity: (1) claims on shared-autonomy arbitration between operator and policy — Dragan-Srinivasa policy-blending IJRR 2013 publishes the closed-form linear arbitration in confidence space; (2) claims on task-space-region constraint encoding for manipulation planning — Berenson-Srinivasa-Kuffner ICRA 2009 publishes TSR formalism executed on this platform; (3) claims on underactuated cable-driven grasping for unstructured pick-and-place — Barrett BH-280 deployment is the canonical published baseline. Modern humanoid manipulation IP claiming shared-autonomy or constraint-region planning faces these timestamped CMU disclosures.

**Sources:**

1. Srinivasa, S. et al. 'HERB 2.0' Proc. IEEE 100(8), 2012.
2. Dragan, A. and Srinivasa, S. 'A Policy-Blending Formalism for Shared Control.' IJRR 32(7), 2013.
3. Berenson, D., Srinivasa, S., Kuffner, J. 'Task Space Regions: A Framework for Pose-Constrained Manipulation Planning.' IJRR 2011.

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

### 2015-04 — Levine Guided Policy Search end-to-end manipulation on PR2/BRETT

- **id:** `levine-gps-pr2-2016`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Sergey Levine, Chelsea Finn, Trevor Darrell, Pieter Abbeel, UC Berkeley
- **disclosure citation:** Levine, Sergey, Finn, Chelsea, Darrell, Trevor, Abbeel, Pieter. 'End-to-End Training of Deep Visuomotor Policies.' Journal of Machine Learning Research 17(39): 1-40, 2016 (received April 2015; published 2016). Earlier: Levine, S., Wagener, N., Abbeel, P. 'Learning Contact-Rich Manipulation Skills with Guided Policy Search.' ICRA 2015.
- **disclosed subsystems:** `control-rl-policy`, `control-vla-vision-language-action`, `sensing-stereo-camera`, `sensing-force-torque`, `software-ros1`

**Prior art notes:**

> Levine et al. 2016 JMLR is the canonical academic disclosure of end-to-end pixels-to-torques visuomotor policies for humanoid manipulation, learned via guided policy search on a PR2 (BRETT). Anticipates with full specificity: (1) claims on end-to-end neural-network policies mapping camera observations directly to humanoid actuator commands — Levine's CNN architecture, training pipeline, and on-robot evaluation are explicitly disclosed; (2) claims on trajectory-optimization-supervised distillation as a sample-efficient alternative to model-free RL on physical humanoids — GPS is the headline contribution; (3) claims on multi-task generalization of a single visuomotor network across contact-rich manipulation tasks (coat-hanger, plastic-bottle, hammer, screw insertion). >3500 citations; JMLR open access; arXiv preprint 2015. The lineage runs directly forward to RT-1, RT-2, OpenVLA, and modern humanoid VLA systems. Modern humanoid end-to-end visuomotor IP filings face this 11-year-deep anchor with full architecture disclosure.

**Sources:**

1. Levine, S., Finn, C., Darrell, T., Abbeel, P. 'End-to-End Training of Deep Visuomotor Policies.' JMLR 17(39): 1-40, 2016.
2. Levine, S., Wagener, N., Abbeel, P. 'Learning Contact-Rich Manipulation Skills with Guided Policy Search.' ICRA 2015.
3. BRETT video archive, UC Berkeley RAIL Lab, 2015.

---

### 2017 — Cassie

- **id:** `cassie-osu`
- **corpus:** academic
- **ip status:** patented
- **creator:** Oregon State University, Dynamic Robotics Laboratory (Jonathan Hurst)
- **disclosure citation:** Agility Robotics / Oregon State University Cassie release, 2017.
- **disclosed subsystems:** `actuator-electric-series-elastic`, `mechanism-bipedal-locomotion`, `mechanism-passive-dynamic-walking`, `control-reduced-order-model`, `control-rl-policy`, `control-sim-to-real`, `sensing-imu`, `software-ros1`

**Prior art notes:**

> Cassie and the broader Hurst lab work on reduced-order locomotion models is significant prior art for bipedal control claims industry-wide.

**Sources:**

1. Hurst Lab publications.
2. Agility Robotics technical materials.

---

### 2017 — PAL TALOS

- **id:** `pal-talos`
- **corpus:** private
- **ip status:** patented
- **creator:** PAL Robotics, in collaboration with LAAS-CNRS
- **disclosure citation:** Stasse, O. et al. 'TALOS: A new humanoid research platform targeted for industrial applications.' IEEE Humanoids 2017.
- **disclosed subsystems:** `actuator-electric-harmonic-drive`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `control-mpc`, `sensing-stereo-camera`, `sensing-force-torque`, `sensing-imu`, `power-li-ion`, `software-ros1`

**Prior art notes:**

> TALOS is among the better-published European industrial humanoids. Stasse 2017 IEEE Humanoids paper provides comprehensive design disclosure.

**Sources:**

1. Stasse, O. et al. IEEE Humanoids 2017.
2. PAL Robotics company materials.

---

### 2017-09 — Reachy 1 (Pollen Robotics open-source humanoid)

- **id:** `reachy-1-pollen-2017`
- **corpus:** open
- **ip status:** open-source
- **creator:** Pollen Robotics / INRIA Flowers (Pierre Rouanet, Matthieu Lapeyre, Pierre-Yves Oudeyer)
- **disclosure citation:** Mick, Sébastien, Lapeyre, Matthieu, Rouanet, Pierre, Halgand, Christophe, Benois-Pineau, Jenny, Paclet, Florent, Cattaert, Daniel, Oudeyer, Pierre-Yves, de Rugy, Aymar. 'Reachy, a 3D-Printed Human-Like Robotic Arm as a Testbed for Human-Robot Control Strategies.' Frontiers in Neurorobotics 13:65, September 2019. Original release: Pollen Robotics / INRIA Flowers, 2017 GitHub release of Reachy v1 (poppy-project lineage).
- **disclosed subsystems:** `actuator-electric-direct-drive`, `mechanism-anthropomorphic-hand`, `sensing-stereo-camera`, `sensing-imu`, `sensing-proprioceptive-actuator`, `software-ros1`, `software-ros2`

**Prior art notes:**

> Reachy 1 (Pollen Robotics 2017, INRIA Flowers lineage) is one of the earliest fully-open-hardware humanoid torso platforms with a published research-grade SDK predating commercial offerings. Anticipates with full specificity: (1) claims on 3D-printed open-hardware humanoid arms with Dynamixel-class actuation — Reachy 1's STL/STEP CAD and firmware are publicly archived since 2017; (2) claims on research-substrate Python SDKs for humanoid telemanipulation — reachy-sdk on GitHub at v0.x predates most commercial humanoid SDK offerings; (3) claims on dual-arm research-platform configurations with anthropomorphic spherical wrists. The 2019 Frontiers paper provides peer-reviewed timestamped disclosure; GitHub commits provide finer-grained 2016-2017 priority. Existing corpus 'reachy' entry should reference this v1 ancestor. Modern open-humanoid IP filings face Reachy 1 at 9-year-deep anchor.

**Sources:**

1. Mick, S. et al. 'Reachy, a 3D-Printed Human-Like Robotic Arm.' Frontiers in Neurorobotics 13:65, 2019.
2. Pollen Robotics GitHub: github.com/pollen-robotics/reachy
3. Lapeyre, M. PhD Thesis (Poppy lineage). INRIA Flowers, 2014.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `4440aa4`.*
