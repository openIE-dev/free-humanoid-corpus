---
title: "actuator-electric-series-elastic"
parent: "Invalidity Contentions"
nav_order: 8
layout: default
---

# Invalidity Contention Packet — `actuator-electric-series-elastic`

**Generated:** 2026-05-07  
**Cross-cut tag:** `actuator-electric-series-elastic`  
**Entries:** 14 (14 commons-grade, 0 draft)  
**Earliest disclosure:** 1995-08  
**Most recent disclosure:** 2023-08

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `actuator-electric-series-elastic`.

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

### 1995-08 — Pratt-Williamson Series Elastic Actuator

- **id:** `pratt-williamson-sea`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Gill A. Pratt and Matthew M. Williamson, MIT Leg Laboratory and MIT AI Lab
- **disclosure citation:** Pratt, Gill A. and Williamson, Matthew M. 'Series elastic actuators.' IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Pittsburgh PA, August 5-9, 1995: 399-406.
- **disclosed subsystems:** `actuator-electric-series-elastic`, `sensing-force-torque`, `sensing-proprioceptive-actuator`

**Prior art notes:**

> The Pratt-Williamson 1995 paper is the foundational academic disclosure of series-elastic actuators (SEA) — the dominant compliant-actuator architecture in legged and humanoid robotics. Anticipates with full specificity: (1) intentional series mechanical spring as the force-sensing element — directly relevant to claims on compliant humanoid actuators (Cassie, Digit, Apollo SEA derivatives); (2) spring-deflection-based force control without strain gauges — relevant to claims on encoder-only force feedback; (3) the bandwidth/stiffness tradeoff disclosure — anticipates SEA-design IP. Pratt's later commercial work (Yobotics, then Boston Dynamics' Atlas SEA) is grounded in this paper. Heavily cited (>3000 citations); SEA is now a textbook concept. 31-year-deep 102 anchor against any 'compliant humanoid actuator' patent.

**Sources:**

1. Pratt, G.A. and Williamson, M.M. 'Series elastic actuators.' IEEE/RSJ IROS 1995: 399-406.
2. Robinson, D.W. 'Design and analysis of series elasticity in closed-loop actuator force control.' PhD Thesis, MIT, 2000 (extension).

---

### 2001-04 — Pratt Virtual Model Control

- **id:** `pratt-virtual-model-control`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Jerry Pratt, Chee-Meng Chew, Ann Torres, Peter Dilworth, Gill Pratt; MIT Leg Laboratory
- **disclosure citation:** Pratt, Jerry, Chew, Chee-Meng, Torres, Ann, Dilworth, Peter, Pratt, Gill. 'Virtual model control: An intuitive approach for bipedal locomotion.' International Journal of Robotics Research 20(2): 129-143, February 2001. Earlier: Pratt, J.E. and Pratt, G.A. 'Intuitive control of a planar bipedal walking robot.' IEEE ICRA 1998: 2014-2021.
- **disclosed subsystems:** `actuator-electric-series-elastic`, `control-reduced-order-model`, `mechanism-bipedal-locomotion`

**Prior art notes:**

> Pratt's Virtual Model Control is a canonical alternative paradigm to ZMP for bipedal control, preserving compliance and intuitive task-space specification. Anticipates: (1) virtual-element-based humanoid torque control — directly relevant to claims on intuitive task-space bipedal controllers; (2) Jacobian-projected virtual force generation — relevant to whole-body humanoid IP that uses 'virtual' or 'imagined' references (every model-based controller for SEA-equipped humanoids descends from this); (3) integration with series-elastic compliance — relevant to compliant-humanoid claims. Pratt's 2000 PhD thesis ('Exploiting natural dynamics in the control of a planar bipedal walking robot,' MIT) extends the framework. Jerry Pratt later led IHMC's humanoid work (DRC Atlas, NASA Valkyrie controller). >1000 citations. 25-year-deep anchor against intuitive-bipedal-control patents.

**Sources:**

1. Pratt, J. et al. 'Virtual model control.' IJRR 20(2): 129-143, 2001.
2. Pratt, J.E. PhD Thesis: 'Exploiting natural dynamics in the control of a planar bipedal walking robot.' MIT, 2000.

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

### 2010-02 — Robonaut 2

- **id:** `robonaut-2`
- **corpus:** academic
- **ip status:** patented
- **creator:** NASA Johnson Space Center, in partnership with General Motors
- **disclosure citation:** Diftler, M.A. et al. 'Robonaut 2 — The First Humanoid Robot in Space.' ICRA 2011.
- **disclosed subsystems:** `actuator-electric-tendon-driven`, `actuator-electric-series-elastic`, `mechanism-anthropomorphic-hand`, `mechanism-tendon-routing`, `sensing-stereo-camera`, `sensing-force-torque`, `sensing-tactile-fingertip`, `power-tethered`

**Prior art notes:**

> Robonaut 2's hand design, with 12 DoF per hand and tendon routing through the forearm, is foundational prior art for high-DoF tendon-driven humanoid hands. The NASA-GM patent portfolio has been extensively cited.

**Sources:**

1. Diftler, M.A. et al. ICRA 2011.
2. Bridgwater, L.B. et al. 'The Robonaut 2 Hand — Designed To Do Work With Tools.' ICRA 2012.

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

### 2013 — ATRIAS

- **id:** `atrias`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Oregon State University, Dynamic Robotics Laboratory (Jonathan Hurst)
- **disclosure citation:** Hubicki, C. et al. 'ATRIAS: Design and validation of a tether-free 3D-capable spring-mass bipedal robot.' International Journal of Robotics Research 35(12), 2016.
- **disclosed subsystems:** `actuator-electric-series-elastic`, `mechanism-bipedal-locomotion`, `mechanism-passive-dynamic-walking`, `control-reduced-order-model`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> ATRIAS is foundational prior art for spring-mass bipedal locomotion. The SLIP-based reduced-order control approach has become a dominant paradigm in dynamic bipedal walking, anticipating many subsequent commercial control claims.

**Sources:**

1. Hubicki, C. et al. IJRR 35(12), 2016.
2. Hurst, J. et al. various IROS and ICRA publications, 2012-2015.

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

### 2019 — Ascento

- **id:** `ascento`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** ETH Zurich, RSL
- **disclosure citation:** Klemm, V. et al. 'Ascento: A Two-Wheeled Jumping Robot.' ICRA 2019.
- **disclosed subsystems:** `actuator-electric-series-elastic`, `actuator-electric-direct-drive`, `mechanism-wheeled-balancing`, `control-reduced-order-model`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> Ascento is foundational prior art for wheeled-bipedal-with-jumping morphology. Anticipates designs combining wheeled efficiency with leg-based obstacle traversal.

**Sources:**

1. Klemm, V. et al. ICRA 2019.
2. Ascento spinout company materials.

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

### 2019-01-16 — Hwangbo ANYmal Sim-to-Real Locomotion

- **id:** `hwangbo-anymal-sim2real`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Hwangbo, Lee, Dosovitskiy, Bellicoso, Tsounis, Koltun, Hutter; ETH Zürich Robotic Systems Lab + Intel Intelligent Systems Lab
- **disclosure citation:** Hwangbo, Jemin, Lee, Joonho, Dosovitskiy, Alexey, Bellicoso, Dario, Tsounis, Vassilios, Koltun, Vladlen, Hutter, Marco. 'Learning agile and dynamic motor skills for legged robots.' Science Robotics 4(26): eaau5872, January 16, 2019.
- **disclosed subsystems:** `control-rl-policy`, `control-sim-to-real`, `actuator-electric-series-elastic`, `mechanism-quadrupedal-locomotion`, `sensing-imu`

**Prior art notes:**

> Hwangbo et al. 2019 is the foundational academic disclosure of practical RL-based sim-to-real legged locomotion. Anticipates with full architectural specificity: (1) actuator-network-based high-fidelity simulation (neural network as drop-in actuator dynamics) — directly relevant to claims on humanoid sim-to-real pipelines (Berkeley Humanoid, Apptronik Apollo, Tesla Optimus all use derivatives); (2) zero-shot policy transfer from RL-in-sim to legged hardware — anticipates virtually every modern legged-RL-policy patent; (3) recovery from arbitrary falls via single learned policy — relevant to fall-recovery IP for humanoids. Published in Science Robotics; one of the most-cited robotics RL papers (>2000 citations). Modern humanoid sim-to-real claims face this 7-year-deep anchor with full peer-review defensibility.

**Sources:**

1. Hwangbo, J. et al. 'Learning agile and dynamic motor skills for legged robots.' Science Robotics 4(26), 2019.
2. Lee, J. et al. 'Learning quadrupedal locomotion over challenging terrain.' Science Robotics 5(47), 2020 (sequel).

---

### 2019-05 — Caltech CAST Hank bipedal platform

- **id:** `caltech-hank-cast-2019`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Aaron D. Ames and the Caltech AMBER Lab / CAST
- **disclosure citation:** Reher, Jenna and Ames, Aaron D. 'Inverse Dynamics Control of Compliant Hybrid Zero Dynamic Walking.' ICRA 2021; Csomay-Shanklin, Noel et al. 'Episodic Learning for Safe Bipedal Locomotion with Control Barrier Functions and Projection-to-State Safety.' L4DC 2021; CAST (Center for Autonomous Systems and Technologies) Caltech Hank reveal 2019.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `actuator-electric-quasi-direct-drive`, `actuator-electric-series-elastic`, `sensing-imu`, `sensing-proprioceptive-actuator`, `control-zmp-balancing`, `safety-hard-constraint`, `safety-simplex-supervisor`

**Prior art notes:**

> Hank is the Caltech CAST flagship humanoid biped of the late-2010s and is the canonical platform for HZD + CBF formal-method bipedal locomotion publications by the Ames group. It anticipates with full specificity: (1) claims on hybrid-zero-dynamics low-dimensional gait manifolds for humanoids — Reher-Ames ICRA 2021 publishes the formal HZD+ID-CLF-QP stack on Hank; (2) claims on control-barrier-function safety supervision for legged locomotion — Csomay-Shanklin L4DC 2021 publishes episodic CBF learning on Hank; (3) claims on quasi-direct-drive proprioceptive humanoid biped hardware — Hank's actuator topology predates and parallels Tesla Optimus and Apptronik Apollo public claims. All Hank publications are open-access with timestamped arXiv.

**Sources:**

1. Reher, J. and Ames, A.D. 'Inverse Dynamics Control of Compliant Hybrid Zero Dynamic Walking.' ICRA 2021.
2. Csomay-Shanklin, N. et al. 'Episodic Learning for Safe Bipedal Locomotion with CBFs.' L4DC 2021.
3. Caltech CAST Hank platform page.

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

### 2023-08 — Apptronik Apollo academic and technical disclosures (2023-2024)

- **id:** `apptronik-apollo-publications-2024`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Apptronik Inc. (Jeff Cardenas, Nick Paine, Luis Sentis lineage from UT Austin Human-Centered Robotics Lab)
- **disclosure citation:** Apptronik. 'Apollo: A Commercial Humanoid Robot for the Workforce.' Apptronik whitepaper, August 2023; Knabe, Coleman et al. 'Designing a Force-Controlled Linear Series Elastic Actuator.' (NASA Valkyrie / Apptronik lineage) IROS 2014; Apptronik-NASA JSC disclosures 2023-2024 including SAFFiR/Valkyrie genealogy white-papers.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `actuator-electric-series-elastic`, `actuator-electric-planetary`, `sensing-imu`, `sensing-force-torque`, `sensing-stereo-camera`, `control-zmp-balancing`, `control-teleoperation`, `power-hot-swap`, `power-li-ion`

**Prior art notes:**

> This entry isolates the academic-publication and technical-disclosure trail behind Apptronik Apollo (distinct from the Apollo product seed entry). It anticipates with full specificity: (1) claims on humanoid SEA actuator topology — Knabe-Paine et al. IROS 2014 publishes the linear-SEA design that lineally seeds Apollo; (2) claims on whole-body operational-space control for force-interactive humanoid manipulation — Sentis-Khatib WBOSC 2007/2010 papers (UT Austin lineage carried into Apptronik) are foundational and timestamped; (3) claims on hot-swap-battery torso integration with regenerative power electronics on humanoid platforms — Apollo whitepaper August 2023 discloses publicly. Modern humanoid commercial-platform IP claims to SEA torque control or WBOSC face this Apptronik publication trail at element-by-element specificity.

**Sources:**

1. Apptronik. 'Apollo: A Commercial Humanoid Robot for the Workforce.' Whitepaper, 2023.
2. Knabe, C., Paine, N. et al. 'Designing a Force-Controlled Linear Series Elastic Actuator.' IROS 2014.
3. Sentis, L. and Khatib, O. 'Synthesis of Whole-Body Behaviors through Hierarchical Control of Behavioral Primitives.' IJHR 2(4), 2005.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `94325f7`.*
