---
title: "control-mpc"
parent: "Invalidity Contentions"
nav_order: 15
layout: default
---

# Invalidity Contention Packet — `control-mpc`

**Generated:** 2026-05-07  
**Cross-cut tag:** `control-mpc`  
**Entries:** 29 (26 commons-grade, 3 draft)  
**Earliest disclosure:** 1980-11  
**Most recent disclosure:** 2024-12

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-mpc`.

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

### 1980-11 — Hollerbach Recursive Lagrangian Manipulator Dynamics

- **id:** `hollerbach-manipulator-1980`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** John M. Hollerbach, MIT Artificial Intelligence Laboratory
- **disclosure citation:** Hollerbach, John M. 'A Recursive Lagrangian Formulation of Manipulator Dynamics and a Comparative Study of Dynamics Formulation Complexity.' IEEE Transactions on Systems, Man, and Cybernetics SMC-10(11): 730-736, November 1980.
- **disclosed subsystems:** `control-mpc`, `control-reduced-order-model`, `sensing-proprioceptive-actuator`

**Prior art notes:**

> Hollerbach 1980 is the canonical academic disclosure of efficient recursive Lagrangian manipulator dynamics, alongside Luh-Walker-Paul 1980 Newton-Euler. Anticipates with full specificity: (1) claims on real-time computed-torque inverse-dynamics for humanoid arms — Hollerbach's O(n³) recursion is the basis for every embedded humanoid arm controller since the early 1980s; (2) claims on per-link recursive computation enabling distributed/parallel inverse-dynamics — Hollerbach's structure is explicitly recursive forward-and-backward; (3) the comparative-complexity tabulation enabling design-time formulation selection. >2500 citations; IEEE TSMC archive openly indexed. Lineage runs forward to Featherstone spatial-vector algebra (existing corpus entry) and Articulated-Body Algorithms. Modern humanoid arm-dynamics IP claims face this 46-year-deep anchor.

**Sources:**

1. Hollerbach, J. M. 'A Recursive Lagrangian Formulation of Manipulator Dynamics.' IEEE TSMC SMC-10(11): 730-736, 1980.
2. Luh, J. Y. S., Walker, M. W., Paul, R. P. 'On-line computational scheme for mechanical manipulators.' ASME J. Dyn. Sys. 102(2): 69-76, 1980 (companion Newton-Euler).

---

### 1983 — Brockett's Necessary Condition for Stabilizability

- **id:** `brockett-condition-1983`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Roger W. Brockett, Harvard University
- **disclosure citation:** Brockett, Roger W. 'Asymptotic stability and feedback stabilization'. In Differential Geometric Control Theory (Brockett, Millman, Sussmann eds.), Birkhäuser, 1983, pp. 181-191.
- **disclosed subsystems:** `control-reduced-order-model`, `control-mpc`, `mechanism-bipedal-locomotion`, `mechanism-wheeled-balancing`

**Prior art notes:**

> Brockett's 1983 condition is the theoretical foundation for understanding why certain humanoid and wheeled-robot systems cannot be stabilized with continuous time-invariant feedback. Modern claims on humanoid walking controllers, wheeled-balance controllers, and switched-system humanoid policies all rest on the design space Brockett's condition characterizes. Anticipates with 43 years of prior art: (1) theoretical justification for time-varying controllers in nonholonomic systems — relevant to wheeled-base humanoid IP; (2) the foundational characterization that motivates ZMP-based walking, LIPM-based walking, and modern reduced-order-model control. Heavily cited; canonical reference in nonlinear control textbooks.

**Sources:**

1. Brockett, R.W. 'Asymptotic stability and feedback stabilization'. Differential Geometric Control Theory, Birkhäuser, 1983.
2. Khalil, H. Nonlinear Systems (textbook reference for Brockett's condition).

---

### 1987 — Featherstone Robot Dynamics Algorithms

- **id:** `featherstone-rdf`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Roy Featherstone, University of Edinburgh and ANU
- **disclosure citation:** Featherstone, Roy. Robot Dynamics Algorithms. Kluwer Academic Publishers, Boston, 1987. ISBN 0-89838-230-0. Foundational paper: Featherstone, R. 'The calculation of robot dynamics using articulated-body inertias.' International Journal of Robotics Research 2(1): 13-30, March 1983.
- **disclosed subsystems:** `control-mpc`, `control-reduced-order-model`

**Prior art notes:**

> Featherstone's 1987 monograph is the canonical academic disclosure of efficient rigid-body-dynamics algorithms underpinning every modern humanoid simulator and MPC controller. Anticipates: (1) O(n) articulated-body forward dynamics (ABA) — directly relevant to claims on real-time humanoid simulation/MPC; the algorithm is implemented in MuJoCo, RaiSim, IsaacGym, Pinocchio, RBDL, Drake — every modern humanoid stack; (2) RNEA inverse dynamics for feedforward torque computation — relevant to torque-control claims; (3) floating-base spatial-vector formulation — relevant to free-floating humanoid dynamics claims. Featherstone's 2008 second edition (Rigid Body Dynamics Algorithms, Springer) further consolidates. Continuously cited; baseline reference for all whole-body humanoid dynamics IP. Modern claims that 'compute humanoid joint torques via a recursive algorithm' face this 39-year-deep anchor.

**Sources:**

1. Featherstone, R. Robot Dynamics Algorithms. Kluwer, 1987.
2. Featherstone, R. 'The calculation of robot dynamics using articulated-body inertias.' IJRR 2(1): 13-30, 1983.
3. Featherstone, R. Rigid Body Dynamics Algorithms. Springer, 2008 (second edition).

---

### 1987-02 — Khatib Operational Space Formulation

- **id:** `khatib-operational-space`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Oussama Khatib, Stanford Artificial Intelligence Laboratory
- **disclosure citation:** Khatib, Oussama. 'A unified approach for motion and force control of robot manipulators: The operational space formulation.' IEEE Journal of Robotics and Automation, RA-3(1): 43-53, February 1987. Earlier: Khatib, O. 'Dynamic control of manipulators in operational space.' 6th IFToMM Congress on Theory of Machines and Mechanisms, New Delhi, December 1983.
- **disclosed subsystems:** `control-mpc`, `control-reduced-order-model`, `sensing-force-torque`, `sensing-proprioceptive-actuator`

**Prior art notes:**

> Khatib's 1987 operational-space formulation is the canonical academic disclosure of task-space inverse-dynamics control with null-space projection. It anticipates with full mathematical specificity: (1) the operational-space inertia matrix Λ(x) and its closed-form expression — directly relevant to whole-body torque-control claims for humanoid platforms; (2) null-space projection for redundancy resolution and prioritized task hierarchies — anticipates virtually every whole-body humanoid controller filed since 2010 (Tesla Optimus, Figure 02, 1X NEO, Apptronik Apollo all employ derivatives); (3) unified motion-and-force impedance control via task-space coordinates — anticipates compliant manipulation IP. Continuously cited (>10,000 citations); the IEEE J-RA paper is freely available through IEEE Xplore. Modern claims on task-space humanoid control face a 39-year-deep 102 anchor here.

**Sources:**

1. Khatib, O. 'A unified approach for motion and force control of robot manipulators.' IEEE J. Robotics and Automation 3(1): 43-53, 1987.
2. Khatib, O. 'Dynamic control of manipulators in operational space.' 6th IFToMM Congress, 1983.

---

### 2005 — Sentis-Khatib Whole-Body Prioritized Task Control

- **id:** `sentis-khatib-whole-body`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Luis Sentis and Oussama Khatib, Stanford AI Laboratory
- **disclosure citation:** Sentis, Luis and Khatib, Oussama. 'Synthesis of whole-body behaviors through hierarchical control of behavioral primitives.' International Journal of Humanoid Robotics 2(4): 505-518, December 2005. Extended in: Sentis, L. and Khatib, O. 'A whole-body control framework for humanoids operating in human environments.' IEEE ICRA, May 2006: 2641-2648.
- **disclosed subsystems:** `control-mpc`, `control-reduced-order-model`, `sensing-proprioceptive-actuator`, `sensing-force-torque`, `mechanism-bipedal-locomotion`

**Prior art notes:**

> Sentis-Khatib whole-body operational-space control extends Khatib 1987 to free-floating humanoids with constraint-aware prioritized task stacks. Anticipates with full specificity: (1) whole-body humanoid task-priority controllers — every modern humanoid (Atlas, TORO, HRP-5P, Optimus, Figure 02) executes a derivative of this stack; (2) contact-consistent dynamics where stance-foot constraints are projected out of the task space — directly relevant to claims on multi-contact humanoid balancing; (3) the formal hierarchical-stack structure (high > mid > low priority via null-space chaining) used in essentially every whole-body humanoid controller since 2010. Sentis's 2007 PhD thesis and the IJHR/ICRA papers are heavily cited (>4000 citations combined). Modern whole-body humanoid IP filings face this academic anchor at 21 years' depth.

**Sources:**

1. Sentis, L. and Khatib, O. 'Synthesis of whole-body behaviors.' Int. J. Humanoid Robotics 2(4): 505-518, 2005.
2. Sentis, L. and Khatib, O. 'A whole-body control framework for humanoids.' IEEE ICRA 2006: 2641-2648.
3. Sentis, L. PhD Thesis: 'Synthesis and control of whole-body behaviors in humanoid systems.' Stanford University, 2007.

---

### 2008 — Willow Garage PR1

- **id:** `willow-pr1`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Willow Garage / Stanford (Ken Salisbury group)
- **disclosure citation:** Wyrobek, K.A. et al. 'Towards a Personal Robotics Development Platform: Rationale and Design of an Intrinsically Safe Personal Robot.' ICRA 2008.
- **disclosed subsystems:** `actuator-electric-tendon-driven`, `mechanism-tendon-routing`, `mechanism-anthropomorphic-hand`, `control-mpc`, `sensing-stereo-camera`, `sensing-force-torque`, `power-tethered`, `safety-hard-constraint`

**Prior art notes:**

> PR1 is significant prior art for safety-by-design humanoid robotics. Cable-driven intrinsically-safe architecture anticipates several modern compliant-actuator humanoid claims.

**Sources:**

1. Wyrobek, K.A. et al. ICRA 2008.
2. Willow Garage technical materials.

---

### 2009-05 — DLR Justin (Rollin' Justin)

- **id:** `dlr-justin`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Borst, Wimboeck, Schmidt, Fuchs, Brunner, Zacharias, Giordano, Konietschke, Sepp, Fuchs, Rink, Albu-Schäffer, Hirzinger; DLR Institute of Robotics and Mechatronics
- **disclosure citation:** Borst, C., Wimboeck, T., Schmidt, F., Fuchs, M., Brunner, B., Zacharias, F., Giordano, P. R., Konietschke, R., Sepp, W., Fuchs, S., Rink, C., Albu-Schäffer, A., Hirzinger, G. 'Rollin' Justin — Mobile platform with variable base'. IEEE ICRA, May 2009.
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `actuator-electric-harmonic-drive`, `control-mpc`, `sensing-stereo-camera`, `sensing-proprioceptive-actuator`

**Prior art notes:**

> Justin is the canonical academic disclosure of wheeled humanoid mobile manipulation with full impedance control. Anticipates and provides extensive prior art for: (1) wheeled humanoid platform for service tasks — relevant to claims on wheeled humanoid IP (Diligent Moxi, NEXTAGE follow this paradigm); (2) torque-controlled dual-arm coordination — relevant to bimanual humanoid manipulation IP; (3) variable-wheelbase mobile base — relevant to morphology-changing wheeled platform claims. DLR has published Justin disclosures in ICRA, IROS, Humanoids continuously since 2009. Modern wheeled humanoid claims face this deep academic anchor.

**Sources:**

1. Borst, C. et al. 'Rollin' Justin'. IEEE ICRA 2009.
2. Bäuml, B. et al. 'Catching flying balls and preparing coffee: humanoid Rollin' Justin performs dynamic and sensitive tasks'. IEEE ICRA 2011.

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

### 2013 — MIT Cheetah

- **id:** `mit-cheetah`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** MIT Biomimetic Robotics Lab (Sangbae Kim)
- **disclosure citation:** Seok, S. et al. 'Design principles for energy-efficient legged locomotion and implementation on the MIT Cheetah robot.' IEEE/ASME Transactions on Mechatronics 20(3), 2015. Earlier ICRA 2013 disclosure.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `actuator-bldc-controller`, `mechanism-quadrupedal-locomotion`, `control-mpc`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> First-generation MIT Cheetah established the design principles for high-torque electric quadrupeds. Seok 2015 T-Mech paper provides foundational design-principles disclosure that anticipates many subsequent legged-robot actuation claims.

**Sources:**

1. Seok, S. et al. IEEE/ASME T-Mech 20(3), 2015.
2. MIT Biomimetic Robotics Lab publications.

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

### 2014 — MIT Cheetah 2

- **id:** `mit-cheetah-2`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** MIT Biomimetic Robotics Lab (Sangbae Kim)
- **disclosure citation:** Park, H.-W. et al. 'High-speed bounding with the MIT Cheetah 2: Control design and experiments.' International Journal of Robotics Research 36(2), 2017. Earlier ICRA disclosure 2014.
- **disclosed subsystems:** `actuator-electric-quasi-direct-drive`, `actuator-bldc-controller`, `sensing-proprioceptive-actuator`, `mechanism-quadrupedal-locomotion`, `control-mpc`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> MIT Cheetah 2 establishes the QDD actuator topology in a working high-speed legged robot. The Wensing 2017 T-RO paper 'Proprioceptive actuator design in the MIT Cheetah' is the foundational actuator design disclosure.

**Sources:**

1. Park, H.-W. et al. IJRR 36(2), 2017.
2. Wensing, P.M. et al. 'Proprioceptive actuator design in the MIT Cheetah.' IEEE T-RO 33(3), 2017.

---

### 2015-02 — Boston Dynamics Spot

- **id:** `hyundai-boston-dynamics-spot`
- **corpus:** private
- **ip status:** patented
- **creator:** Boston Dynamics (now Hyundai Motor Group subsidiary)
- **disclosure citation:** Boston Dynamics public reveal of Spot, February 2015.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `mechanism-quadrupedal-locomotion`, `control-mpc`, `sensing-stereo-camera`, `sensing-imu`, `power-li-ion`, `power-hot-swap`

**Prior art notes:**

> Spot is the most commercially deployed quadruped robot. BD's Spot patents face deep prior art from MIT Cheetah series, ANYmal lineage, and academic quadruped literature.

**Sources:**

1. Boston Dynamics product materials.
2. Boston Dynamics technical blog.

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

### 2017-11 — Kawasaki Kaleido

- **id:** `kawasaki-kaleido`
- **corpus:** private
- **ip status:** patented
- **creator:** Kawasaki Heavy Industries
- **disclosure citation:** Kawasaki Heavy Industries public reveal of Kaleido, iREX November 2017.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `control-mpc`, `sensing-stereo-camera`, `sensing-force-torque`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> Kawasaki's deep industrial robotics IP base means much of their humanoid claims are anticipated by their own prior industrial robotics disclosures, plus AIST HRP series prior art.

**Sources:**

1. Kawasaki Heavy Industries materials.
2. iREX 2017 demonstration coverage.

---

### 2018 — MIT Cheetah 3

- **id:** `mit-cheetah-3`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** MIT Biomimetic Robotics Lab (Sangbae Kim)
- **disclosure citation:** Bledt, G. et al. 'MIT Cheetah 3: Design and Control of a Robust, Dynamic Quadruped Robot.' IROS 2018.
- **disclosed subsystems:** `actuator-electric-quasi-direct-drive`, `actuator-bldc-controller`, `sensing-proprioceptive-actuator`, `mechanism-quadrupedal-locomotion`, `control-mpc`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> Cheetah 3 establishes blind robust legged locomotion using only proprioceptive sensing — a significant prior art point against later vision-dependent legged-robot claims.

**Sources:**

1. Bledt, G. et al. IROS 2018.

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

### 2018-11 — Sutton & Barto, Reinforcement Learning: An Introduction (2nd edition)

- **id:** `sutton-barto-rl-2nd-edition-2018`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Richard S. Sutton, Andrew G. Barto
- **disclosure citation:** Sutton, Richard S. and Barto, Andrew G. 'Reinforcement Learning: An Introduction.' 2nd edition, MIT Press, November 2018; ISBN 978-0262039246; freely available online at incompleteideas.net/book.
- **disclosed subsystems:** `control-rl-policy`, `control-mpc`

**Prior art notes:**

> Sutton & Barto 2nd edition is the canonical textbook anchor for reinforcement-learning claims and is the citation-of-record across robotics RL papers 2018-2026. It anticipates with full specificity: (1) claims on temporal-difference learning, Q-learning, SARSA, and n-step bootstrapping — all derived with closed-form pseudocode in Chapters 6-7; (2) claims on policy-gradient and actor-critic methods — Chapter 13 contains the REINFORCE and natural-actor-critic formulations; (3) claims on function-approximation RL with linear features and neural-network state representations — Chapters 9-12 lay the formal substrate. Freely distributed online by the authors at incompleteideas.net/book under unrestricted educational use. Modern humanoid RL-policy IP claiming any TD/PG/AC pattern faces this canonical 2018 anchor.

**Sources:**

1. Sutton, R.S. and Barto, A.G. 'Reinforcement Learning: An Introduction.' 2nd ed., MIT Press, 2018.
2. Free online distribution: incompleteideas.net/book/the-book-2nd.html

---

### 2019 — MIT Mini Cheetah

- **id:** `mini-cheetah`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** MIT Biomimetic Robotics Lab (Sangbae Kim)
- **disclosure citation:** Katz, B. et al. 'Mini Cheetah: A Platform for Pushing the Limits of Dynamic Quadruped Control.' ICRA 2019.
- **disclosed subsystems:** `actuator-electric-quasi-direct-drive`, `actuator-bldc-controller`, `sensing-proprioceptive-actuator`, `mechanism-quadrupedal-locomotion`, `control-mpc`, `control-rl-policy`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> The QDD actuator topology (low gear ratio, high-torque BLDC, transparent backdrivability) is a foundational contribution. Establishes the design space for affordable dynamic legged robots.

**Sources:**

1. Katz, B. et al. ICRA 2019.
2. Wensing, P. et al. 'Proprioceptive actuator design in the MIT Cheetah.' IEEE T-RO 2017.

---

### 2020 — Boston Dynamics Spot (fuel-cell variant) *(draft)*

- **id:** `spot-fuel-cell`
- **corpus:** private
- **ip status:** patented
- **creator:** Boston Dynamics
- **disclosure citation:** Boston Dynamics partnership announcements with fuel cell vendors, 2020.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `mechanism-quadrupedal-locomotion`, `control-mpc`, `sensing-stereo-camera`, `sensing-imu`, `power-fuel-cell`

**Prior art notes:**

> Demonstrates fuel-cell-powered legged robotics at commercial scale. Anticipates fuel-cell power claims in field robotics applications.

**Sources:**

1. Boston Dynamics partnership announcements.
2. Industrial deployment case studies.

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

### 2022 — Upkie

- **id:** `upkie`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** Stéphane Caron and contributors
- **disclosure citation:** Caron, S. et al. Upkie public release, 2022.
- **disclosed subsystems:** `actuator-electric-quasi-direct-drive`, `actuator-bldc-controller`, `actuator-foc-controller`, `mechanism-wheeled-balancing`, `control-reduced-order-model`, `control-mpc`, `sensing-imu`, `power-li-po`, `software-mjbots-stack`, `software-ros2`

**Prior art notes:**

> Upkie demonstrates fully-open wheeled-bipedal balancing using commodity mjbots actuators. Anticipates cost-effective wheeled-humanoid designs.

**Sources:**

1. github.com/upkie
2. Caron, S. publications and project documentation.

---

### 2022-05 — Janner Diffuser planning with diffusion

- **id:** `janner-diffuser-2022`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Michael Janner, Yilun Du, Joshua Tenenbaum, Sergey Levine, MIT/UC Berkeley
- **disclosure citation:** Janner, Michael, Du, Yilun, Tenenbaum, Joshua B., Levine, Sergey. 'Planning with Diffusion for Flexible Behavior Synthesis.' Proceedings of the 39th International Conference on Machine Learning (ICML 2022), Baltimore, July 2022; arXiv:2205.09991, May 2022.
- **disclosed subsystems:** `control-mpc`, `control-rl-policy`, `control-vla-vision-language-action`

**Prior art notes:**

> Janner Diffuser is the foundational academic disclosure of trajectory-level diffusion as a planner/policy substrate for robotic control, predating Chi et al.'s Diffusion Policy by ~6 months. Anticipates with full specificity: (1) claims on diffusion models trained over state-action trajectories for robotic motion generation — Diffuser discloses the joint state-action trajectory diffusion architecture; (2) claims on classifier-guided sample-time reward/goal conditioning — Diffuser discloses gradient-guided sampling for arbitrary objective composition; (3) claims on receding-horizon diffusion replanning (MPC-style) — Diffuser discloses replan-each-step. >1500 citations; ICML 2022 proceedings and arXiv timestamped. Modern humanoid diffusion-policy IP claims face this 4-year-deep anchor — and importantly Diffuser predates the modern diffusion-policy boom and discloses generic trajectory diffusion before manipulator-specific patents filed in 2023+.

**Sources:**

1. Janner, M., Du, Y., Tenenbaum, J. B., Levine, S. 'Planning with Diffusion for Flexible Behavior Synthesis.' ICML 2022; arXiv:2205.09991.
2. Project page: diffusion-planning.github.io

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

### 2024-03 — Rainbow Robotics RB-Y1

- **id:** `rainbow-robotics-rb-y1`
- **corpus:** private
- **ip status:** patented
- **creator:** Rainbow Robotics
- **disclosure citation:** Rainbow Robotics public reveal of RB-Y1, March 2024.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `mechanism-anthropomorphic-hand`, `control-mpc`, `sensing-stereo-camera`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> Rainbow Robotics has direct lineage from KAIST HUBO program; HUBO academic publications constitute prior art for many of their humanoid claims.

**Sources:**

1. Rainbow Robotics company materials.

---

### 2024-12 — Genesis (open-source physics simulator)

- **id:** `genesis-embodied-ai-simulator`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** Genesis Authors collaboration (multi-institution: CMU, Stanford, MIT CSAIL, Tsinghua, Peking, ETH Zürich, UMD, et al.)
- **disclosure citation:** Genesis Authors. 'Genesis: A Generative and Universal Physics Engine for Robotics and Beyond'. GitHub release at https://github.com/Genesis-Embodied-AI/Genesis, December 19, 2024. Multi-institution collaboration including Carnegie Mellon University, Stanford University, MIT CSAIL, Tsinghua University, Peking University, ETH Zürich, University of Maryland.
- **disclosed subsystems:** `control-sim-to-real`, `control-rl-policy`, `control-mpc`

**Prior art notes:**

> The Genesis simulator (Genesis-Embodied-AI/Genesis, December 2024) is the most recent and highest-throughput academic-grade open-source physics engine for robotics simulation, published Apache-2.0 by a multi-institution academic collaboration. Anticipates with full architectural specificity: (1) GPU-parallelized robotics simulation at 43M-FPS scale — directly relevant to commercial claims on sim-to-real-at-scale humanoid IP (notably Genesis AI Inc.'s GENE-26.5 product, with which this open-source project shares a name); (2) unified multi-physics architecture (rigid + soft + MPM + FEM + fluid) — relevant to claims on multi-domain humanoid simulation; (3) differentiable simulation for gradient-based policy optimization — relevant to claims on policy-gradient humanoid training at scale; (4) the URDF/MJCF interoperability surface that permits OpenLoco-class descriptors to be simulated without modification. Modern claims on sim-to-real-at-scale, multi-physics simulation, or differentiable physics for humanoid training all face this 1.5-year-deep open-source academic prior art with full source disclosure under Apache-2.0.

**Sources:**

1. Genesis-Embodied-AI/Genesis GitHub repository (https://github.com/Genesis-Embodied-AI/Genesis), December 2024.
2. Genesis project website (https://genesis-embodied-ai.github.io/), December 2024.
3. Genesis benchmark report (rigid-body 43M FPS on RTX 4090) included with the December 2024 release.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `559a8b5`.*
