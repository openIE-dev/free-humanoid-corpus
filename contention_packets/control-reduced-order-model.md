---
title: "control-reduced-order-model"
parent: "Invalidity Contentions"
nav_order: 55
layout: default
---

# Invalidity Contention Packet — `control-reduced-order-model`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-reduced-order-model`  
**Entries:** 28 (27 commons-grade, 1 draft)  
**Earliest disclosure:** 1979-04-07  
**Most recent disclosure:** 2023-08

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `bf892af`.*
