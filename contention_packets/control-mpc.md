---
title: "control-mpc"
parent: "Invalidity Contentions"
nav_order: 41
layout: default
---

# Invalidity Contention Packet — `control-mpc`

**Generated:** 2026-05-07  
**Cross-cut tag:** `control-mpc`  
**Entries:** 40 (37 commons-grade, 3 draft)  
**Earliest disclosure:** 1980-11  
**Most recent disclosure:** 2025-03

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

### 2012-08 — Contact-Invariant Optimization (Mordatch CIO)

- **id:** `mordatch-cio-2012`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Igor Mordatch (University of Washington, then OpenAI/DeepMind), Emanuel Todorov (University of Washington), Zoran Popović (University of Washington)
- **disclosure citation:** Mordatch, Igor; Todorov, Emanuel; Popović, Zoran. 'Discovery of Complex Behaviors through Contact-Invariant Optimization.' ACM Transactions on Graphics (SIGGRAPH 2012), Volume 31, Issue 4, Article 43, July 2012. DOI: 10.1145/2185520.2185539. Companion follow-up: Mordatch, Wang, Todorov, Popović. 'Animating Human Lower Limbs Using Contact-Invariant Optimization.' ACM TOG (SIGGRAPH Asia 2013).
- **disclosed subsystems:** `control-mpc`, `control-reduced-order-model`, `mechanism-bipedal-locomotion`

**Prior art notes:**

> Mordatch-Todorov-Popović 2012 SIGGRAPH is the canonical academic disclosure of contact-invariant optimization for humanoid motion synthesis. Anticipates with full specificity: (1) treating contact existence and contact forces as continuous optimization variables rather than combinatorial mode switches — directly relevant to modern claims on contact-implicit humanoid trajectory optimization (Posa-Tedrake 2014, Manchester 2017, Mastalli 2020 Crocoddyl all build on this); (2) automatic contact-sequence discovery in humanoid locomotion and manipulation — anticipates patents on adaptive footstep planning and automatic grasp placement for humanoid IP; (3) the unified trajectory-optimization formulation that synthesizes diverse behaviors (walking, climbing, getup, manipulation) in a single framework — relevant to claims on multi-task humanoid motion synthesis. SIGGRAPH 2012 paper has >1000 citations and is foundational in both robotics and computer animation. Modern contact-implicit humanoid trajectory optimization IP faces this 14-year-deep academic anchor.

**Sources:**

1. Mordatch, I.; Todorov, E.; Popović, Z. 'Discovery of Complex Behaviors through Contact-Invariant Optimization.' ACM TOG 31(4), Article 43 (SIGGRAPH 2012). DOI: 10.1145/2185520.2185539.
2. Mordatch, I.; Wang, J.; Todorov, E.; Popović, Z. 'Animating Human Lower Limbs Using Contact-Invariant Optimization.' ACM TOG (SIGGRAPH Asia 2013).
3. Posa, M.; Cantu, C.; Tedrake, R. 'A direct method for trajectory optimization of rigid bodies through contact.' IJRR 33(1), 2014 (closely related contact-implicit method).

---

### 2012-10 — Tassa iLQG / Synthesis and Stabilization of Complex Behaviors

- **id:** `tassa-ilqg-2012`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Yuval Tassa, Tom Erez, Emanuel Todorov; Department of Computer Science and Engineering, University of Washington (Todorov lab)
- **disclosure citation:** Tassa, Yuval; Erez, Tom; Todorov, Emanuel. 'Synthesis and Stabilization of Complex Behaviors through Online Trajectory Optimization.' IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Vilamoura, Portugal, October 2012, pp. 4906-4913. DOI: 10.1109/IROS.2012.6386025. Earlier: Tassa, Y.; Erez, T.; Smart, W.D. 'Receding Horizon Differential Dynamic Programming.' NeurIPS 2007. Foundational underlying method: Li, W. and Todorov, E. 'Iterative linear quadratic regulator design for nonlinear biological movement systems.' ICINCO 2004.
- **disclosed subsystems:** `control-mpc`, `control-reduced-order-model`

**Prior art notes:**

> Tassa-Erez-Todorov 2012 IROS is the canonical academic disclosure of online iLQG-based model-predictive control for high-DoF humanoid systems. Anticipates with full mathematical specificity: (1) online receding-horizon trajectory optimization for 28-DoF humanoid models at real-time rates — directly relevant to claims on humanoid MPC IP (Boston Dynamics, Apptronik, Figure, Tesla all employ trajectory-optimization-class controllers); (2) the regularization-and-line-search scheme that enabled iLQG to run online with stable convergence — anticipates implementation-detail patents on regularized DDP/iLQG humanoid controllers; (3) jointly synthesizing feedforward trajectories AND time-varying feedback gains — relevant to claims on closed-loop humanoid trajectory IP. Open-source MuJoCo code release accompanies the paper (the foundational MuJoCo iLQG demo). Modern humanoid trajectory-optimization MPC IP faces this 14-year-deep academic anchor with full implementation disclosure. Foundational lineage: Li-Todorov ICINCO 2004 (iLQR primitive); Jacobson-Mayne 1970 (DDP); Bellman 1957 (dynamic programming). Direct downstream: every major modern humanoid MPC stack.

**Sources:**

1. Tassa, Y.; Erez, T.; Todorov, E. 'Synthesis and Stabilization of Complex Behaviors through Online Trajectory Optimization.' IROS 2012: 4906-4913. DOI: 10.1109/IROS.2012.6386025.
2. Li, W. and Todorov, E. 'Iterative linear quadratic regulator design for nonlinear biological movement systems.' ICINCO 2004 (foundational iLQR).
3. Tassa, Y.; Mansard, N.; Todorov, E. 'Control-Limited Differential Dynamic Programming.' ICRA 2014 (constrained extension).

---

### 2012-10 — MuJoCo (original)

- **id:** `mujoco-todorov-2012`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Emo Todorov, Tom Erez, Yuval Tassa (originally University of Washington / Roboti LLC; now Google DeepMind)
- **disclosure citation:** Todorov, E., Erez, T., Tassa, Y. 'MuJoCo: A physics engine for model-based control'. IROS 2012. Originally proprietary (Roboti LLC); acquired by Google DeepMind October 2021 and released under Apache-2.0.
- **disclosed subsystems:** `control-physics-simulation`, `control-mpc`, `control-trajectory-optimization`

**Prior art notes:**

> MuJoCo is the canonical academic physics engine for model-based robotic control (Todorov-Erez-Tassa 2012). 13-year-deep prior art spanning the proprietary Roboti era (2012-2021) and the open-source DeepMind era (2021+). The substrate that the Tassa iLQG entry, Howell-Tassa MuJoCo MPC entry, MJX entry, and Genesis simulator entry all build on or interop with. Direct shielding for any commercial humanoid claim on contact-rich policy training simulation. MJCF is the format OpenLoco compiles to, so MuJoCo is the reference simulator for the entire free-humanoid-family.

**Sources:**

1. Todorov, Erez, Tassa. IROS 2012.
2. MuJoCo official site (mujoco.org).
3. GitHub: github.com/google-deepmind/mujoco.
4. DeepMind acquisition + open-sourcing announcement, October 2021.

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

### 2019-01 — Drake

- **id:** `drake-tedrake-2019`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** MIT CSAIL Robot Locomotion Group + Toyota Research Institute; Russ Tedrake et al.
- **disclosure citation:** Tedrake, R., the Drake Development Team. 'Drake: Model-Based Design and Verification for Robotics'. drake.mit.edu, project active since ~2010 with formal v1.0 in January 2019. BSD-3-Clause source: github.com/RobotLocomotion/drake. MIT CSAIL + Toyota Research Institute.
- **disclosed subsystems:** `control-physics-simulation`, `control-mpc`, `control-formal-verification`, `control-trajectory-optimization`

**Prior art notes:**

> Drake is the canonical MIT/TRI model-based design + verification toolkit for robotics (Tedrake et al., active since ~2010, v1.0 Jan 2019). 6-year-deep formal-release prior art, 15-year-deep project. Distinct from MuJoCo by emphasis on deterministic verifiable semantics (relevant for safety-critical / certification use cases). Direct shielding for any commercial humanoid claim on verifiable model-based control or whole-body QP/MPC architectures. Free-humanoid-platform/wheeled/centaur/submersible all reference Drake as a tertiary simulator option for whole-body MPC validation.

**Sources:**

1. Tedrake, R. 'Underactuated Robotics' textbook (underactuated.mit.edu).
2. Drake official site (drake.mit.edu).
3. GitHub: github.com/RobotLocomotion/drake.

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

### 2020-05 — Crocoddyl

- **id:** `mastalli-crocoddyl-2020`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Carlos Mastalli, Justin Carpentier, Nicolas Mansard, Sethu Vijayakumar et al.; LAAS-CNRS Toulouse, INRIA Paris (Willow team), University of Edinburgh
- **disclosure citation:** Mastalli, Carlos; Budhiraja, Rohan; Merkt, Wolfgang; Saurel, Guilhem; Hammoud, Bilal; Naveau, Maximilien; Carpentier, Justin; Vijayakumar, Sethu; Mansard, Nicolas. 'Crocoddyl: An Efficient and Versatile Framework for Multi-Contact Optimal Control.' IEEE International Conference on Robotics and Automation (ICRA), Paris, May 2020, pp. 2536-2542. DOI: 10.1109/ICRA40945.2020.9196673. Source code at https://github.com/loco-3d/crocoddyl. BSD-3-Clause license.
- **disclosed subsystems:** `control-mpc`, `control-reduced-order-model`, `mechanism-bipedal-locomotion`

**Prior art notes:**

> Crocoddyl (Mastalli et al. ICRA 2020) is the canonical academic open-source framework for multi-contact differential-dynamic-programming-based optimal control of humanoid and legged systems. Anticipates with full source-level disclosure: (1) real-time MPC on full-body humanoid models with multiple contacts — directly relevant to commercial claims on whole-body humanoid MPC (Apptronik, Figure 02, Boston Dynamics electric Atlas all employ DDP/iLQR-class controllers downstream of this paradigm); (2) analytical rigid-body dynamics derivatives integrated with trajectory optimization (via Pinocchio, Carpentier 2019) — relevant to claims on differentiable-dynamics humanoid IP; (3) the multi-phase contact-schedule framework that handles humanoid double-support / single-support / manipulation transitions — relevant to claims on phase-aware humanoid MPC; (4) the FDDP feasibility-driven extension that handles infeasible warm-starts — anticipates claims on robust-warm-start humanoid trajectory optimization. BSD-3-Clause source release plus the ICRA 2020 paper (>500 citations by 2026) make this entry a deep prior art anchor for the humanoid MPC patent space.

**Sources:**

1. Mastalli, C. et al. 'Crocoddyl: An Efficient and Versatile Framework for Multi-Contact Optimal Control.' IEEE ICRA 2020: 2536-2542. DOI: 10.1109/ICRA40945.2020.9196673.
2. Carpentier, J. et al. 'The Pinocchio C++ library — A fast and flexible implementation of rigid body dynamics algorithms and their analytical derivatives.' SII 2019.
3. Crocoddyl GitHub repository (https://github.com/loco-3d/crocoddyl), BSD-3-Clause.

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

### 2021-10 — Caltech LEONARDO

- **id:** `caltech-leonardo-2021`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Kyunam Kim, Patrick Spieler, Alireza Ramezani, Soon-Jo Chung; Caltech Aerospace Robotics and Control Lab (Chung group), CAST (Center for Autonomous Systems and Technologies)
- **disclosure citation:** Kim, Kyunam; Spieler, Patrick; Lupu, Elena-Sorina; Ramezani, Alireza; Chung, Soon-Jo. 'A bipedal walking robot that can fly, slackline, and skateboard.' Science Robotics, Volume 6, Issue 59, October 6, 2021, eabf8136. DOI: 10.1126/scirobotics.abf8136. Caltech CAST press release October 6, 2021.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `control-mpc`, `control-reduced-order-model`, `sensing-imu`

**Prior art notes:**

> Caltech LEONARDO (Kim-Chung et al. Science Robotics 2021) is the canonical academic disclosure of bipedal-aerial hybrid morphology with simultaneous walking-and-thrust-balance-assist control. Anticipates with element-by-element specificity: (1) the hybrid-morphology bipedal-aerial platform with propellers integrated into the leg structure — directly relevant to claims on hybrid-locomotion humanoid IP, anticipating any future commercial humanoid that augments walking with thrust assistance; (2) simultaneous use of propeller thrust and leg actuation for balance during walking — relevant to claims on multi-modal balance authority for humanoid platforms (separate from ZMP-only or angular-momentum-only approaches); (3) the demonstration on extreme tasks (slackline traversal, skateboarding) that exceed the capability set of pure bipedal robots — relevant to claims on extreme-environment humanoid mobility IP. Science Robotics paper provides full design and control disclosure. Modern hybrid-locomotion humanoid IP faces this 5-year-deep academic anchor.

**Sources:**

1. Kim, K. et al. 'A bipedal walking robot that can fly, slackline, and skateboard.' Science Robotics 6(59), eabf8136, October 2021. DOI: 10.1126/scirobotics.abf8136.
2. Caltech CAST press release: 'Meet LEO, the Bipedal Robot That Can Skateboard and Fly,' October 6, 2021.

---

### 2021-11 — MIT Humanoid

- **id:** `mit-humanoid-2021`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Matthew Chignoli, Donghyun Kim, Elijah Stanger-Jones, Sangbae Kim; MIT Biomimetic Robotics Lab
- **disclosure citation:** Chignoli, Matthew; Kim, Donghyun; Stanger-Jones, Elijah; Kim, Sangbae. 'The MIT Humanoid Robot: Design, Motion Planning, and Control For Acrobatic Behaviors.' IEEE-RAS International Conference on Humanoid Robots (Humanoids 2020, virtual; presented November 2021), pp. 1-8. arXiv:2104.09025, April 2021.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `actuator-electric-quasi-direct-drive`, `actuator-bldc-controller`, `sensing-proprioceptive-actuator`, `sensing-imu`, `control-mpc`, `control-reduced-order-model`

**Prior art notes:**

> The MIT Humanoid (Chignoli-Kim et al. Humanoids 2020/arXiv 2021) is the canonical academic disclosure of dynamic whole-body humanoid locomotion using a quasi-direct-drive actuator topology with explicit actuator-dynamics-aware MPC, from the Sangbae Kim group (MIT Biomimetic Robotics Lab) that previously produced Mini Cheetah and Cheetah 3. Anticipates with element-by-element specificity: (1) QDD actuator topology extended from quadruped (Mini Cheetah, 2019) to humanoid biped — directly relevant to commercial claims on QDD humanoid IP (Berkeley Humanoid, Unitree H1/G1, Booster T1, much of the 2024-2026 humanoid wave employs QDD); (2) explicit actuator-dynamics-model integration into humanoid MPC (motor inertia, torque limits, current limits enter the OCP directly) — anticipates commercial claims on actuator-aware humanoid control; (3) acrobatic-capable lightweight (~24 kg) electric humanoid as a research platform — anticipates the lightweight-humanoid commercial form factor. The Sangbae Kim lineage (Cheetah 1/2/3 → Mini Cheetah → MIT Humanoid) is one of the deepest legged-robot academic chains and the MIT Humanoid arXiv preprint provides full design documentation. Modern QDD-humanoid IP filings face this 5-year-deep academic anchor.

**Sources:**

1. Chignoli, M.; Kim, D.; Stanger-Jones, E.; Kim, S. 'The MIT Humanoid Robot: Design, Motion Planning, and Control For Acrobatic Behaviors.' IEEE-RAS Humanoids 2020 (presented Nov 2021); arXiv:2104.09025.
2. Katz, B.; Di Carlo, J.; Kim, S. 'Mini Cheetah: A Platform for Pushing the Limits of Dynamic Quadruped Control.' IEEE ICRA 2019 (lineage: QDD actuator).
3. Wensing, P. et al. 'Proprioceptive actuator design in the MIT Cheetah: Impact mitigation and high-bandwidth physical interaction for dynamic legged robots.' IEEE T-RO 33(3), 2017.

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

### 2023-08 — NVIDIA Isaac Lab

- **id:** `nvidia-isaac-lab-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Mittal et al.; NVIDIA Corporation, ETH Zürich Robotic Systems Lab (Hutter), and University of Toronto Vector Institute (Garg)
- **disclosure citation:** Mittal, Mayank; Yu, Calvin; Yu, Qinxi; Liu, Jingzhou; Rudin, Nikita; Hoeller, David; Yuan, Jia Lin; Tehrani, Pooria S.; Singh, Ritvik; Guo, Yunrong; Mazhar, Hammad; Mandlekar, Ajay; Babich, Buck; State, Gavriel; Hutter, Marco; Garg, Animesh. 'ORBIT: A Unified Simulation Framework for Interactive Robot Learning Environments.' IEEE Robotics and Automation Letters (RA-L), August 2023; later released and rebranded as Isaac Lab in 2024. Repository at https://github.com/isaac-sim/IsaacLab.
- **disclosed subsystems:** `control-sim-to-real`, `control-rl-policy`, `control-mpc`, `sensing-stereo-camera`, `sensing-imu`

**Prior art notes:**

> Isaac Lab (formerly ORBIT, 2023) is the canonical academic-published GPU-parallelized simulation framework for robot learning, published BSD-3-Clause by NVIDIA + ETH Zürich + University of Toronto. Anticipates with full architectural specificity: (1) thousands-of-parallel-environments humanoid RL training on a single GPU — directly relevant to commercial claims on simulation-at-scale humanoid training pipelines (NVIDIA GR00T, Tesla Optimus, Figure 02 all use this paradigm); (2) URDF/USD-asset interoperability surface enabling cross-platform humanoid descriptors — relevant to claims on cross-platform humanoid descriptor IP; (3) the standardized RL task interface (gym-like API with vectorized environments) — relevant to claims on humanoid-task-curriculum IP; (4) integrated sensor simulation with domain randomization — relevant to claims on sim-to-real-via-randomization humanoid pipelines (anticipated already by OpenAI Dactyl 2018 but Isaac Lab provides the GPU-scale implementation). Mittal et al. RA-L 2023 paper has been cited >300 times by 2026 and underpins essentially every recent humanoid-RL publication. Modern sim-to-real-at-scale humanoid IP filings face this 3-year-deep open-source academic anchor.

**Sources:**

1. Mittal, M. et al. 'ORBIT: A Unified Simulation Framework for Interactive Robot Learning Environments.' IEEE RA-L, 2023; arXiv:2301.04195.
2. Isaac Lab GitHub repository (https://github.com/isaac-sim/IsaacLab), 2024 rebrand from ORBIT.
3. Makoviychuk, V. et al. 'Isaac Gym: High Performance GPU-Based Physics Simulation For Robot Learning.' arXiv:2108.10470, NeurIPS 2021 datasets track (predecessor system).

---

### 2023-08 — MuJoCo MJX

- **id:** `deepmind-mujoco-mjx-2023`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** DeepMind / Google Research MuJoCo team (lead: Yuval Tassa, Tom Erez, with engineering contributions from Taylor Howell, Kevin Zakka, Erik Frey and the broader DeepMind robotics group; original MuJoCo by Emo Todorov)
- **disclosure citation:** DeepMind / Google Research MuJoCo team. 'MuJoCo MJX: A JAX implementation of the MuJoCo physics engine.' MuJoCo 3.0.0 release, August 2023; documented in MuJoCo 3.x documentation (https://mujoco.readthedocs.io/en/stable/mjx.html). Source code at https://github.com/google-deepmind/mujoco/tree/main/mjx. Originally MuJoCo: Todorov, Erez, and Tassa, 'MuJoCo: A physics engine for model-based control,' IEEE/RSJ IROS 2012, 5026-5033. Apache-2.0 license.
- **disclosed subsystems:** `control-sim-to-real`, `control-rl-policy`, `control-mpc`, `control-reduced-order-model`

**Prior art notes:**

> MuJoCo MJX (August 2023) is the canonical academic disclosure of GPU/TPU-parallelized differentiable physics simulation for robotics, published Apache-2.0 by DeepMind. Anticipates with full specificity: (1) gradient-based humanoid policy optimization through the simulator end-to-end — directly relevant to claims on differentiable-physics humanoid IP (NVIDIA GR00T, Genesis simulator, and several Tesla / Figure / 1X commercial pipelines use the same paradigm); (2) JAX vmap/pmap vectorized rollouts at >10,000 envs scale — relevant to claims on massively-parallel humanoid simulation pipelines; (3) soft-contact regularization for differentiability through contact — anticipates claims on smoothed-contact humanoid trajectory optimization; (4) MJCF as a vendor-neutral robot description format — anticipates claims on cross-vendor humanoid descriptors. The original MuJoCo (Todorov-Erez-Tassa IROS 2012) provides 14-year-deep prior art on the underlying physics; MJX adds 3-year-deep prior art on the GPU-differentiable port. Modern claims on differentiable simulation for humanoid training face this academic anchor.

**Sources:**

1. Todorov, E., Erez, T., Tassa, Y. 'MuJoCo: A physics engine for model-based control.' IROS 2012: 5026-5033.
2. MuJoCo MJX documentation: https://mujoco.readthedocs.io/en/stable/mjx.html (MuJoCo 3.0.0 release, August 2023).
3. MJX source code: https://github.com/google-deepmind/mujoco/tree/main/mjx
4. Howell, T. et al. 'Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo.' arXiv:2212.00541, 2022 (MJX-driven MPC at DeepMind).

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

### 2025-03 — MuJoCo MPC (Howell-Tassa)

- **id:** `howell-tassa-mujoco-mpc-2025`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Google DeepMind; Howell, Lutter, Tassa et al.
- **disclosure citation:** Howell, T., Lutter, M., Acero, F., Yuan, M., Tassa, Y., et al. 'Whole-Body Model-Predictive Control of Legged Robots with MuJoCo'. arXiv:2503.04613, March 2025. Google DeepMind / Tassa group.
- **disclosed subsystems:** `control-mpc`, `control-trajectory-optimization`, `control-real-time-control`, `actuator-foc-controller`

**Prior art notes:**

> Howell-Tassa MuJoCo MPC is the direct 2025 successor to the Tassa iLQG 2012 entry already in the corpus. 14-month-deep open-permissive prior art for: real-time whole-body humanoid MPC using MuJoCo dynamics + finite-difference iLQR. Demonstrated on full-sized humanoid hardware, which closes the simulation-to-real gap that the 2012 Tassa work left open. Direct shielding for any commercial humanoid claim on real-time whole-body trajectory optimization.

**Sources:**

1. Howell et al. arXiv:2503.04613 March 2025.
2. GitHub: github.com/google-deepmind/mujoco_mpc.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `b51f194`.*
