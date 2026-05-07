---
title: "control-reduced-order-model"
parent: "Invalidity Contentions"
nav_order: 16
layout: default
---

# Invalidity Contention Packet — `control-reduced-order-model`

**Generated:** 2026-05-06  
**Cross-cut tag:** `control-reduced-order-model`  
**Entries:** 20 (19 commons-grade, 1 draft)  
**Earliest disclosure:** 1979-04-07  
**Most recent disclosure:** 2022

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-reduced-order-model`.

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

### 1979-04-07 — RX-78-2 Gundam (additional Gundam mecha disclosures) *(draft)*

- **id:** `rx-78-2-gundam-2`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Yoshiyuki Tomino, Sunrise studio
- **disclosure citation:** Tomino, Yoshiyuki et al. Mobile Suit Gundam. Nagoya Broadcasting, April 7, 1979 - January 26, 1980 (43 episodes).
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `control-teleoperation`, `control-reduced-order-model`

**Prior art notes:**

> Note: this entry is separate from the original RX-78-2 Gundam entry (rx-78-2-gundam) in the seed slice; this one disclosures additional engineering-flavored elements that the seed entry treated lightly. AMBAC (Active Mass Balance Auto-Control) is the disclosed mechanism for orientation in zero gravity using limb articulation as reaction mass — a clear anticipation of reduced-order-model approaches that exploit limb dynamics for whole-body control in modern humanoids.

**Sources:**

1. Tomino, Y. Mobile Suit Gundam (43 episodes). Sunrise / Nagoya Broadcasting, 1979-1980.

---

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

### 1983 — Raibert One-Legged Hopper

- **id:** `raibert-hopping-1leg`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Marc H. Raibert; CMU Leg Laboratory, then MIT Leg Laboratory
- **disclosure citation:** Raibert, Marc H. 'Hopping in legged systems — modeling and simulation for the two-dimensional one-legged case'. IEEE Transactions on Systems, Man, and Cybernetics SMC-14(3): 451-463, May/June 1984. Earlier: Raibert, M.H. and Brown, H.B. 'Experiments in balance with a 2D one-legged machine'. Trans. ASME, J. Dyn. Sys., Meas., Cont., 106:75-81, 1984.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `actuator-pneumatic-muscle`, `control-reduced-order-model`

**Prior art notes:**

> Raibert's hoppers are the foundational academic disclosure of dynamic legged balance and reduced-order-model control. The three-part decoupling (leg height / foot placement / body attitude) is the *exact* control architecture used by every subsequent dynamic-legged academic and commercial system, from Cassie to Atlas to MIT Mini Cheetah. Modern claims on reduced-order-model legged control all face Raibert's 1984 disclosure as 102 prior art. The 1985 book (Legged Robots that Balance, MIT Press) extends the disclosure to 2-legged and 4-legged versions and is one of the most-cited works in legged robotics. Publicly funded research; open publication.

**Sources:**

1. Raibert, M.H. 'Hopping in legged systems'. IEEE Trans. SMC, 1984.
2. Raibert, M.H. and Brown, H.B. 'Experiments in balance with a 2D one-legged machine'. ASME J. DSMC, 1984.
3. Raibert, M.H. Legged Robots that Balance. MIT Press, 1986.

---

### 1985-06 — Yoshikawa Manipulability Ellipsoid

- **id:** `yoshikawa-manipulability`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Tsuneo Yoshikawa, Kyoto University
- **disclosure citation:** Yoshikawa, Tsuneo. 'Manipulability of robotic mechanisms.' International Journal of Robotics Research 4(2): 3-9, June 1985. Earlier conference: Yoshikawa, T. 'Analysis and control of robot manipulators with redundancy.' First Int. Symp. on Robotics Research, MIT Press, 1984: 735-747.
- **disclosed subsystems:** `control-reduced-order-model`

**Prior art notes:**

> Yoshikawa's manipulability formulation is the foundational academic disclosure of configuration-quality metrics and redundancy resolution for redundant manipulators. Anticipates: (1) manipulability-based redundancy resolution — directly relevant to claims on humanoid arm posture optimization (every dual-arm humanoid relies on a derivative); (2) the manipulability ellipsoid as a design and analysis tool — relevant to claims on optimization of humanoid arm/leg topology; (3) configuration-aware null-space optimization — relevant to whole-body humanoid posture control IP. Heavily cited (>5000 citations); standard reference in every robotics textbook. Modern humanoid arm-posture-optimization patents face this 40-year-deep 102 anchor.

**Sources:**

1. Yoshikawa, T. 'Manipulability of robotic mechanisms.' IJRR 4(2): 3-9, 1985.
2. Yoshikawa, T. Foundations of Robotics: Analysis and Control. MIT Press, 1990 (textbook consolidation).

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

### 2001-10 — Kajita Linear Inverted Pendulum Model

- **id:** `kajita-lipm`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Shuuji Kajita, Fumio Kanehiro, Kenji Kaneko, Kazuhito Yokoi, Hirohisa Hirukawa; AIST National Institute of Advanced Industrial Science and Technology, Japan
- **disclosure citation:** Kajita, Shuuji, Kanehiro, F., Kaneko, K., Yokoi, K., Hirukawa, H. 'The 3D Linear Inverted Pendulum Mode: A simple modeling for a biped walking pattern generation.' IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Maui HI, October 29-November 3, 2001: 239-246.
- **disclosed subsystems:** `control-zmp-balancing`, `control-reduced-order-model`, `mechanism-bipedal-locomotion`

**Prior art notes:**

> Kajita's 3D-LIPM is the canonical academic disclosure of real-time humanoid walking pattern generation via reduced-order model. Anticipates: (1) the LIPM ẍ = (g/h)(x - p) reduction — directly relevant to claims on real-time bipedal pattern generation in essentially every academic and commercial humanoid since 2001 (HRP series, NAO, ASIMO derivatives, Atlas-class, Optimus, Figure 02 all use LIPM-derivative real-time planners); (2) preview-control-based ZMP tracking (Kajita-Kanehiro 2003 ICRA paper extending this) — relevant to model-predictive bipedal walking IP; (3) the constant-height constraint as a real-time-tractable simplification — relevant to humanoid walking-controller claims. Heavily cited (>4000 citations between LIPM 2001 and preview-control 2003 papers). Basis for the textbook Kajita et al. 'Introduction to Humanoid Robotics' (Springer 2014).

**Sources:**

1. Kajita, S. et al. 'The 3D Linear Inverted Pendulum Mode.' IEEE/RSJ IROS 2001: 239-246.
2. Kajita, S. et al. 'Biped walking pattern generation by using preview control of zero-moment point.' IEEE ICRA 2003: 1620-1626.
3. Kajita, S., Hirukawa, H., Harada, K., Yokoi, K. Introduction to Humanoid Robotics. Springer Tracts in Advanced Robotics 101, 2014.

---

### 2002 — Dynamic Movement Primitives (DMP)

- **id:** `dmp-schaal-ijspeert`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Auke Jan Ijspeert, Jun Nakanishi, Stefan Schaal; USC + ATR Computational Neuroscience Laboratories
- **disclosure citation:** Ijspeert, Auke Jan, Nakanishi, Jun, Schaal, Stefan. 'Movement imitation with nonlinear dynamical systems in humanoid robots.' IEEE International Conference on Robotics and Automation (ICRA), Washington DC, May 2002: 1398-1403. Foundational consolidation: Ijspeert, A.J., Nakanishi, J., Hoffmann, H., Pastor, P., Schaal, S. 'Dynamical movement primitives: Learning attractor models for motor behaviors.' Neural Computation 25(2): 328-373, February 2013.
- **disclosed subsystems:** `control-rl-policy`, `control-reduced-order-model`

**Prior art notes:**

> DMPs are the canonical academic disclosure of stability-guaranteed learnable motor primitives for humanoid robotics. Anticipates: (1) one-shot trajectory-from-demonstration learning with stability guarantees — directly relevant to claims on humanoid skill libraries built from human demonstration (a foundational pattern in every commercial humanoid program); (2) goal-parameterizable motor primitives — relevant to claims on adaptable humanoid skills; (3) compositional skill chaining — relevant to claims on humanoid behavior trees built from learned primitives. Heavily cited (>3000 citations across the series); the 2013 Neural Computation paper is the canonical reference. Modern humanoid skill-library patents face this 24-year-deep 102 anchor.

**Sources:**

1. Ijspeert, A.J., Nakanishi, J., Schaal, S. 'Movement imitation with nonlinear dynamical systems.' IEEE ICRA 2002: 1398-1403.
2. Ijspeert, A.J. et al. 'Dynamical movement primitives.' Neural Computation 25(2): 328-373, 2013.

---

### 2004-07 — Abbeel-Ng Apprenticeship Learning via Inverse Reinforcement Learning

- **id:** `abbeel-ng-irl-2004`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Pieter Abbeel and Andrew Y. Ng, Stanford AI Laboratory
- **disclosure citation:** Abbeel, Pieter and Ng, Andrew Y. 'Apprenticeship learning via inverse reinforcement learning.' Proceedings of the 21st International Conference on Machine Learning (ICML 2004), Banff, Canada, July 2004.
- **disclosed subsystems:** `control-rl-policy`, `control-reduced-order-model`

**Prior art notes:**

> Abbeel-Ng 2004 is the foundational academic disclosure of apprenticeship learning via IRL: recovering reward functions from expert demonstrations to match performance. Anticipates with full specificity: (1) claims on humanoid policy learning from demonstration where the reward is implicit and recovered by matching expert behavior — Abbeel-Ng disclose the feature-expectation-matching algorithm and convergence proof; (2) claims on imitation learning that exceeds direct behavior cloning by recovering an underlying objective — this is the paper's headline contribution; (3) claims on reward-engineering avoidance for complex humanoid tasks via demonstration-driven reward shaping. >5000 citations; openly available through ICML proceedings. The lineage to Ziebart MaxEnt IRL (2008) and modern preference-based RL (DPO, RLHF for robotics) traces directly. Modern humanoid IRL/inverse-RL IP claims face this 22-year-deep anchor.

**Sources:**

1. Abbeel, P. and Ng, A. Y. 'Apprenticeship learning via inverse reinforcement learning.' ICML 2004.
2. Ng, A. Y. and Russell, S. 'Algorithms for inverse reinforcement learning.' ICML 2000 (precursor).

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

### 2008 — Ott Cartesian Impedance Control

- **id:** `ott-impedance-control`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Christian Ott, Alin Albu-Schäffer, Gerd Hirzinger; DLR Institute of Robotics and Mechatronics
- **disclosure citation:** Ott, Christian. Cartesian Impedance Control of Redundant and Flexible-Joint Robots. Springer Tracts in Advanced Robotics 49, Springer, 2008. ISBN 978-3-540-69253-9. Earlier: Albu-Schäffer, A., Ott, C., Hirzinger, G. 'A unified passivity-based control framework for position, torque and impedance control of flexible joint robots.' International Journal of Robotics Research 26(1): 23-39, January 2007.
- **disclosed subsystems:** `actuator-electric-harmonic-drive`, `sensing-proprioceptive-actuator`, `control-reduced-order-model`

**Prior art notes:**

> Ott's impedance-control framework is the canonical academic disclosure of Cartesian impedance with explicit joint-flexibility modeling — the foundation of every modern collaborative torque-controlled robot (KUKA LBR iiwa, Franka Emika Panda, all DLR-derived humanoids including TORO and Justin). Anticipates: (1) passivity-based Cartesian impedance with provable stability — directly relevant to claims on safe-interaction humanoid IP; (2) flexible-joint compensation via post-reducer torque sensing — relevant to harmonic-drive actuator claims (every modern humanoid arm uses post-reducer torque sensing); (3) redundancy-resolved Cartesian impedance — relevant to whole-body compliance claims. Springer monograph and IJRR paper heavily cited (>2000 citations). Direct lineage to Franka Panda, KUKA iiwa, and modern humanoid platforms.

**Sources:**

1. Ott, C. Cartesian Impedance Control of Redundant and Flexible-Joint Robots. Springer 2008.
2. Albu-Schäffer, A., Ott, C., Hirzinger, G. 'A unified passivity-based control framework.' IJRR 26(1): 23-39, 2007.

---

### 2008-07 — Ziebart Maximum Entropy Inverse Reinforcement Learning

- **id:** `ziebart-maxent-irl-2008`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Brian D. Ziebart, Andrew Maas, J. Andrew Bagnell, Anind K. Dey, Carnegie Mellon University
- **disclosure citation:** Ziebart, Brian D., Maas, Andrew, Bagnell, J. Andrew, Dey, Anind K. 'Maximum entropy inverse reinforcement learning.' Proceedings of the AAAI Conference on Artificial Intelligence (AAAI 2008), Chicago, July 2008. Extended in: Ziebart, B. D., PhD Thesis, CMU 2010.
- **disclosed subsystems:** `control-rl-policy`, `control-reduced-order-model`

**Prior art notes:**

> Ziebart MaxEnt IRL is the canonical disambiguation of Abbeel-Ng IRL: choose the maximum-entropy reward consistent with feature expectations, yielding a unique log-linear policy. Anticipates with full specificity: (1) claims on humanoid imitation that handles imperfect/noisy demonstrations — MaxEnt IRL is the foundational principled handling; (2) claims on reward learning where the policy is stochastic over trajectories — the log-linear distribution P(τ) ∝ exp(wᵀφ(τ)) is the explicit form; (3) claims on energy-based / score-based reward models for robotic learning — MaxEnt IRL anticipates the energy-based view embraced by modern guided-cost-learning (Finn et al. 2016) and adversarial IRL. >4000 citations; AAAI proceedings open access. Lineage to Finn-Levine GCL, Fu et al. AIRL, modern preference-tuning. Modern humanoid IRL filings face this 18-year-deep anchor.

**Sources:**

1. Ziebart, B. D., Maas, A., Bagnell, J. A., Dey, A. K. 'Maximum entropy inverse reinforcement learning.' AAAI 2008.
2. Ziebart, B. D. PhD Thesis: 'Modeling Purposeful Adaptive Behavior with the Principle of Maximum Causal Entropy.' CMU, 2010.

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

### 2013-02 — Ijspeert-Schaal Dynamic Movement Primitives (formal extension)

- **id:** `ijspeert-dmp-2013`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Auke Ijspeert, Stefan Schaal, Jun Nakanishi, Heiko Hoffmann, Peter Pastor
- **disclosure citation:** Ijspeert, Auke Jan, Nakanishi, Jun, Hoffmann, Heiko, Pastor, Peter, Schaal, Stefan. 'Dynamical Movement Primitives: Learning Attractor Models for Motor Behaviors.' Neural Computation 25(2): 328-373, February 2013. Earlier foundations: Schaal, S., Peters, J., Nakanishi, J., Ijspeert, A. 'Learning movement primitives.' International Symposium on Robotics Research (ISRR) 2003; Schaal, Mohajerian, Ijspeert. 'Dynamics systems vs. optimal control — a unifying view.' Progress in Brain Research 165: 425-445, 2007.
- **disclosed subsystems:** `control-reduced-order-model`, `control-rl-policy`, `sensing-proprioceptive-actuator`

**Prior art notes:**

> Ijspeert-Schaal DMPs are the canonical academic disclosure of learnable, stable, parameterized motor primitives for robotic motion generation. The 2013 Neural Computation paper consolidates the formal framework; the 2007 Progress in Brain Research extension and the 2002-2003 Schaal/Ijspeert papers establish lineage. Anticipates with full specificity: (1) claims on demonstration-learned humanoid motion primitives with online goal modulation — DMPs disclose the closed-form ODE structure used in essentially every humanoid skill-library paper since 2007; (2) claims on rhythmic locomotion primitives with phase coupling — directly anticipates pattern-generator humanoid IP; (3) claims on obstacle-avoiding modulated motion primitives — the coupling-term extension is explicit in the 2013 paper. >5000 citations; broadly available through open Neural Computation archives. Modern humanoid skill-primitive IP filings face this lineage at 13-23 years' depth.

**Sources:**

1. Ijspeert, A. J., Nakanishi, J., Hoffmann, H., Pastor, P., Schaal, S. 'Dynamical Movement Primitives.' Neural Computation 25(2): 328-373, 2013.
2. Schaal, S., Mohajerian, P., Ijspeert, A. 'Dynamics systems vs. optimal control.' Prog. Brain Res. 165: 425-445, 2007.
3. Ijspeert, A. J., Nakanishi, J., Schaal, S. 'Movement imitation with nonlinear dynamical systems.' IEEE ICRA 2002.

---

### 2014-07 — DLR TORO

- **id:** `dlr-toro`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Englsberger, Werner, Ott, Henze, Roa, Garofalo, Burger, Beyer, Eiberger, Schmid, Albu-Schäffer; DLR Institute of Robotics and Mechatronics
- **disclosure citation:** Englsberger, J., Werner, A., Ott, C., Henze, B., Roa, M.A., Garofalo, G., Burger, R., Beyer, A., Eiberger, O., Schmid, K., Albu-Schäffer, A. 'Overview of the torque-controlled humanoid robot TORO'. IEEE-RAS Humanoids, July 2014.
- **disclosed subsystems:** `actuator-electric-harmonic-drive`, `sensing-proprioceptive-actuator`, `control-zmp-balancing`, `control-reduced-order-model`, `mechanism-bipedal-locomotion`

**Prior art notes:**

> TORO is the canonical academic disclosure of full-body torque-controlled bipedal humanoid with DCM (Divergent Component of Motion) walking control. Anticipates: (1) torque-controlled whole-body bipedal walking — directly relevant to claims on whole-body torque-controlled humanoid platforms; (2) DCM walking as an alternative to ZMP — relevant to walking-control IP; (3) impedance-control whole-body interaction with humans — relevant to safe-human-interaction humanoid claims. DLR's Englsberger paper introduced the DCM formulation that subsequent humanoids (HRP-5P, several private platforms) adopted. Publicly funded research with extensive IEEE-proceedings publication.

**Sources:**

1. Englsberger, J. et al. 'Overview of the torque-controlled humanoid robot TORO'. IEEE Humanoids 2014.
2. Englsberger, J. et al. 'Three-dimensional bipedal walking control based on Divergent Component of Motion'. IEEE T-RO 31(2): 355-368, 2015.

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
