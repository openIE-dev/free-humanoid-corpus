---
title: control-reduced-order-model
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-reduced-order-model`

**16 corpus entries disclose this subsystem.**

Earliest disclosure: 1979-04-07

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## RX-78-2 Gundam (additional Gundam mecha disclosures) (1979-04-07)

- **id**: `rx-78-2-gundam-2`
- **corpus**: fictional
- **creator**: Yoshiyuki Tomino, Sunrise studio
- **disclosure**: Tomino, Yoshiyuki et al. Mobile Suit Gundam. Nagoya Broadcasting, April 7, 1979 - January 26, 1980 (43 episodes).
- **ip status**: fictional
- **prior art notes**: Note: this entry is separate from the original RX-78-2 Gundam entry (rx-78-2-gundam) in the seed slice; this one disclosures additional engineering-flavored elements that the seed entry treated lightly. AMBAC (Active Mass Balance Auto-Control) is the disclosed mechanism for orientation in zero gravity using limb articulation as reaction mass — a clear anticipation of reduced-order-model approaches that exploit limb dynamics for whole-body control in modern humanoids.

## Raibert One-Legged Hopper (1983)

- **id**: `raibert-hopping-1leg`
- **corpus**: academic
- **creator**: Marc H. Raibert; CMU Leg Laboratory, then MIT Leg Laboratory
- **disclosure**: Raibert, Marc H. 'Hopping in legged systems — modeling and simulation for the two-dimensional one-legged case'. IEEE Transactions on Systems, Man, and Cybernetics SMC-14(3): 451-463, May/June 1984. Earlier: Raibert, M.H. and Brown, H.B. 'Experiments in balance with a 2D one-legged machine'. Trans. ASME, J. Dyn. Sys., Meas., Cont., 106:75-81, 1984.
- **ip status**: public-domain
- **prior art notes**: Raibert's hoppers are the foundational academic disclosure of dynamic legged balance and reduced-order-model control. The three-part decoupling (leg height / foot placement / body attitude) is the *exact* control architecture used by every subsequent dynamic-legged academic and commercial system, from Cassie to Atlas to MIT Mini Cheetah. Modern claims on reduced-order-model legged control all face Raibert's 1984 disclosure as 102 prior art. The 1985 book (Legged Robots that Balance, MIT Press) extends the disclosure to 2-legged and 4-legged versions and is one of the most-cited works in legged robotics. Publicly funded research; open publication.

## Yoshikawa Manipulability Ellipsoid (1985-06)

- **id**: `yoshikawa-manipulability`
- **corpus**: academic
- **creator**: Tsuneo Yoshikawa, Kyoto University
- **disclosure**: Yoshikawa, Tsuneo. 'Manipulability of robotic mechanisms.' International Journal of Robotics Research 4(2): 3-9, June 1985. Earlier conference: Yoshikawa, T. 'Analysis and control of robot manipulators with redundancy.' First Int. Symp. on Robotics Research, MIT Press, 1984: 735-747.
- **ip status**: public-domain
- **prior art notes**: Yoshikawa's manipulability formulation is the foundational academic disclosure of configuration-quality metrics and redundancy resolution for redundant manipulators. Anticipates: (1) manipulability-based redundancy resolution — directly relevant to claims on humanoid arm posture optimization (every dual-arm humanoid relies on a derivative); (2) the manipulability ellipsoid as a design and analysis tool — relevant to claims on optimization of humanoid arm/leg topology; (3) configuration-aware null-space optimization — relevant to whole-body humanoid posture control IP. Heavily cited (>5000 citations); standard reference in every robotics textbook. Modern humanoid arm-posture-optimization patents face this 40-year-deep 102 anchor.

## Featherstone Robot Dynamics Algorithms (1987)

- **id**: `featherstone-rdf`
- **corpus**: academic
- **creator**: Roy Featherstone, University of Edinburgh and ANU
- **disclosure**: Featherstone, Roy. Robot Dynamics Algorithms. Kluwer Academic Publishers, Boston, 1987. ISBN 0-89838-230-0. Foundational paper: Featherstone, R. 'The calculation of robot dynamics using articulated-body inertias.' International Journal of Robotics Research 2(1): 13-30, March 1983.
- **ip status**: public-domain
- **prior art notes**: Featherstone's 1987 monograph is the canonical academic disclosure of efficient rigid-body-dynamics algorithms underpinning every modern humanoid simulator and MPC controller. Anticipates: (1) O(n) articulated-body forward dynamics (ABA) — directly relevant to claims on real-time humanoid simulation/MPC; the algorithm is implemented in MuJoCo, RaiSim, IsaacGym, Pinocchio, RBDL, Drake — every modern humanoid stack; (2) RNEA inverse dynamics for feedforward torque computation — relevant to torque-control claims; (3) floating-base spatial-vector formulation — relevant to free-floating humanoid dynamics claims. Featherstone's 2008 second edition (Rigid Body Dynamics Algorithms, Springer) further consolidates. Continuously cited; baseline reference for all whole-body humanoid dynamics IP. Modern claims that 'compute humanoid joint torques via a recursive algorithm' face this 39-year-deep anchor.

## Khatib Operational Space Formulation (1987-02)

- **id**: `khatib-operational-space`
- **corpus**: academic
- **creator**: Oussama Khatib, Stanford Artificial Intelligence Laboratory
- **disclosure**: Khatib, Oussama. 'A unified approach for motion and force control of robot manipulators: The operational space formulation.' IEEE Journal of Robotics and Automation, RA-3(1): 43-53, February 1987. Earlier: Khatib, O. 'Dynamic control of manipulators in operational space.' 6th IFToMM Congress on Theory of Machines and Mechanisms, New Delhi, December 1983.
- **ip status**: public-domain
- **prior art notes**: Khatib's 1987 operational-space formulation is the canonical academic disclosure of task-space inverse-dynamics control with null-space projection. It anticipates with full mathematical specificity: (1) the operational-space inertia matrix Λ(x) and its closed-form expression — directly relevant to whole-body torque-control claims for humanoid platforms; (2) null-space projection for redundancy resolution and prioritized task hierarchies — anticipates virtually every whole-body humanoid controller filed since 2010 (Tesla Optimus, Figure 02, 1X NEO, Apptronik Apollo all employ derivatives); (3) unified motion-and-force impedance control via task-space coordinates — anticipates compliant manipulation IP. Continuously cited (>10,000 citations); the IEEE J-RA paper is freely available through IEEE Xplore. Modern claims on task-space humanoid control face a 39-year-deep 102 anchor here.

## Pratt Virtual Model Control (2001-04)

- **id**: `pratt-virtual-model-control`
- **corpus**: academic
- **creator**: Jerry Pratt, Chee-Meng Chew, Ann Torres, Peter Dilworth, Gill Pratt; MIT Leg Laboratory
- **disclosure**: Pratt, Jerry, Chew, Chee-Meng, Torres, Ann, Dilworth, Peter, Pratt, Gill. 'Virtual model control: An intuitive approach for bipedal locomotion.' International Journal of Robotics Research 20(2): 129-143, February 2001. Earlier: Pratt, J.E. and Pratt, G.A. 'Intuitive control of a planar bipedal walking robot.' IEEE ICRA 1998: 2014-2021.
- **ip status**: public-domain
- **prior art notes**: Pratt's Virtual Model Control is a canonical alternative paradigm to ZMP for bipedal control, preserving compliance and intuitive task-space specification. Anticipates: (1) virtual-element-based humanoid torque control — directly relevant to claims on intuitive task-space bipedal controllers; (2) Jacobian-projected virtual force generation — relevant to whole-body humanoid IP that uses 'virtual' or 'imagined' references (every model-based controller for SEA-equipped humanoids descends from this); (3) integration with series-elastic compliance — relevant to compliant-humanoid claims. Pratt's 2000 PhD thesis ('Exploiting natural dynamics in the control of a planar bipedal walking robot,' MIT) extends the framework. Jerry Pratt later led IHMC's humanoid work (DRC Atlas, NASA Valkyrie controller). >1000 citations. 25-year-deep anchor against intuitive-bipedal-control patents.

## Kajita Linear Inverted Pendulum Model (2001-10)

- **id**: `kajita-lipm`
- **corpus**: academic
- **creator**: Shuuji Kajita, Fumio Kanehiro, Kenji Kaneko, Kazuhito Yokoi, Hirohisa Hirukawa; AIST National Institute of Advanced Industrial Science and Technology, Japan
- **disclosure**: Kajita, Shuuji, Kanehiro, F., Kaneko, K., Yokoi, K., Hirukawa, H. 'The 3D Linear Inverted Pendulum Mode: A simple modeling for a biped walking pattern generation.' IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Maui HI, October 29-November 3, 2001: 239-246.
- **ip status**: public-domain
- **prior art notes**: Kajita's 3D-LIPM is the canonical academic disclosure of real-time humanoid walking pattern generation via reduced-order model. Anticipates: (1) the LIPM ẍ = (g/h)(x - p) reduction — directly relevant to claims on real-time bipedal pattern generation in essentially every academic and commercial humanoid since 2001 (HRP series, NAO, ASIMO derivatives, Atlas-class, Optimus, Figure 02 all use LIPM-derivative real-time planners); (2) preview-control-based ZMP tracking (Kajita-Kanehiro 2003 ICRA paper extending this) — relevant to model-predictive bipedal walking IP; (3) the constant-height constraint as a real-time-tractable simplification — relevant to humanoid walking-controller claims. Heavily cited (>4000 citations between LIPM 2001 and preview-control 2003 papers). Basis for the textbook Kajita et al. 'Introduction to Humanoid Robotics' (Springer 2014).

## Dynamic Movement Primitives (DMP) (2002)

- **id**: `dmp-schaal-ijspeert`
- **corpus**: academic
- **creator**: Auke Jan Ijspeert, Jun Nakanishi, Stefan Schaal; USC + ATR Computational Neuroscience Laboratories
- **disclosure**: Ijspeert, Auke Jan, Nakanishi, Jun, Schaal, Stefan. 'Movement imitation with nonlinear dynamical systems in humanoid robots.' IEEE International Conference on Robotics and Automation (ICRA), Washington DC, May 2002: 1398-1403. Foundational consolidation: Ijspeert, A.J., Nakanishi, J., Hoffmann, H., Pastor, P., Schaal, S. 'Dynamical movement primitives: Learning attractor models for motor behaviors.' Neural Computation 25(2): 328-373, February 2013.
- **ip status**: public-domain
- **prior art notes**: DMPs are the canonical academic disclosure of stability-guaranteed learnable motor primitives for humanoid robotics. Anticipates: (1) one-shot trajectory-from-demonstration learning with stability guarantees — directly relevant to claims on humanoid skill libraries built from human demonstration (a foundational pattern in every commercial humanoid program); (2) goal-parameterizable motor primitives — relevant to claims on adaptable humanoid skills; (3) compositional skill chaining — relevant to claims on humanoid behavior trees built from learned primitives. Heavily cited (>3000 citations across the series); the 2013 Neural Computation paper is the canonical reference. Modern humanoid skill-library patents face this 24-year-deep 102 anchor.

## Sentis-Khatib Whole-Body Prioritized Task Control (2005)

- **id**: `sentis-khatib-whole-body`
- **corpus**: academic
- **creator**: Luis Sentis and Oussama Khatib, Stanford AI Laboratory
- **disclosure**: Sentis, Luis and Khatib, Oussama. 'Synthesis of whole-body behaviors through hierarchical control of behavioral primitives.' International Journal of Humanoid Robotics 2(4): 505-518, December 2005. Extended in: Sentis, L. and Khatib, O. 'A whole-body control framework for humanoids operating in human environments.' IEEE ICRA, May 2006: 2641-2648.
- **ip status**: public-domain
- **prior art notes**: Sentis-Khatib whole-body operational-space control extends Khatib 1987 to free-floating humanoids with constraint-aware prioritized task stacks. Anticipates with full specificity: (1) whole-body humanoid task-priority controllers — every modern humanoid (Atlas, TORO, HRP-5P, Optimus, Figure 02) executes a derivative of this stack; (2) contact-consistent dynamics where stance-foot constraints are projected out of the task space — directly relevant to claims on multi-contact humanoid balancing; (3) the formal hierarchical-stack structure (high > mid > low priority via null-space chaining) used in essentially every whole-body humanoid controller since 2010. Sentis's 2007 PhD thesis and the IJHR/ICRA papers are heavily cited (>4000 citations combined). Modern whole-body humanoid IP filings face this academic anchor at 21 years' depth.

## Ott Cartesian Impedance Control (2008)

- **id**: `ott-impedance-control`
- **corpus**: academic
- **creator**: Christian Ott, Alin Albu-Schäffer, Gerd Hirzinger; DLR Institute of Robotics and Mechatronics
- **disclosure**: Ott, Christian. Cartesian Impedance Control of Redundant and Flexible-Joint Robots. Springer Tracts in Advanced Robotics 49, Springer, 2008. ISBN 978-3-540-69253-9. Earlier: Albu-Schäffer, A., Ott, C., Hirzinger, G. 'A unified passivity-based control framework for position, torque and impedance control of flexible joint robots.' International Journal of Robotics Research 26(1): 23-39, January 2007.
- **ip status**: open-permissive
- **prior art notes**: Ott's impedance-control framework is the canonical academic disclosure of Cartesian impedance with explicit joint-flexibility modeling — the foundation of every modern collaborative torque-controlled robot (KUKA LBR iiwa, Franka Emika Panda, all DLR-derived humanoids including TORO and Justin). Anticipates: (1) passivity-based Cartesian impedance with provable stability — directly relevant to claims on safe-interaction humanoid IP; (2) flexible-joint compensation via post-reducer torque sensing — relevant to harmonic-drive actuator claims (every modern humanoid arm uses post-reducer torque sensing); (3) redundancy-resolved Cartesian impedance — relevant to whole-body compliance claims. Springer monograph and IJRR paper heavily cited (>2000 citations). Direct lineage to Franka Panda, KUKA iiwa, and modern humanoid platforms.

## ATRIAS (2013)

- **id**: `atrias`
- **corpus**: academic
- **creator**: Oregon State University, Dynamic Robotics Laboratory (Jonathan Hurst)
- **disclosure**: Hubicki, C. et al. 'ATRIAS: Design and validation of a tether-free 3D-capable spring-mass bipedal robot.' International Journal of Robotics Research 35(12), 2016.
- **ip status**: open-permissive
- **prior art notes**: ATRIAS is foundational prior art for spring-mass bipedal locomotion. The SLIP-based reduced-order control approach has become a dominant paradigm in dynamic bipedal walking, anticipating many subsequent commercial control claims.

## DLR TORO (2014-07)

- **id**: `dlr-toro`
- **corpus**: academic
- **creator**: Englsberger, Werner, Ott, Henze, Roa, Garofalo, Burger, Beyer, Eiberger, Schmid, Albu-Schäffer; DLR Institute of Robotics and Mechatronics
- **disclosure**: Englsberger, J., Werner, A., Ott, C., Henze, B., Roa, M.A., Garofalo, G., Burger, R., Beyer, A., Eiberger, O., Schmid, K., Albu-Schäffer, A. 'Overview of the torque-controlled humanoid robot TORO'. IEEE-RAS Humanoids, July 2014.
- **ip status**: open-permissive
- **prior art notes**: TORO is the canonical academic disclosure of full-body torque-controlled bipedal humanoid with DCM (Divergent Component of Motion) walking control. Anticipates: (1) torque-controlled whole-body bipedal walking — directly relevant to claims on whole-body torque-controlled humanoid platforms; (2) DCM walking as an alternative to ZMP — relevant to walking-control IP; (3) impedance-control whole-body interaction with humans — relevant to safe-human-interaction humanoid claims. DLR's Englsberger paper introduced the DCM formulation that subsequent humanoids (HRP-5P, several private platforms) adopted. Publicly funded research with extensive IEEE-proceedings publication.

## Cassie (2017)

- **id**: `cassie-osu`
- **corpus**: academic
- **creator**: Oregon State University, Dynamic Robotics Laboratory (Jonathan Hurst)
- **disclosure**: Agility Robotics / Oregon State University Cassie release, 2017.
- **ip status**: patented
- **prior art notes**: Cassie and the broader Hurst lab work on reduced-order locomotion models is significant prior art for bipedal control claims industry-wide.

## Ascento (2019)

- **id**: `ascento`
- **corpus**: academic
- **creator**: ETH Zurich, RSL
- **disclosure**: Klemm, V. et al. 'Ascento: A Two-Wheeled Jumping Robot.' ICRA 2019.
- **ip status**: open-permissive
- **prior art notes**: Ascento is foundational prior art for wheeled-bipedal-with-jumping morphology. Anticipates designs combining wheeled efficiency with leg-based obstacle traversal.

## Digit (2019-01)

- **id**: `agility-digit`
- **corpus**: private
- **creator**: Agility Robotics
- **disclosure**: Agility Robotics public reveal, CES January 2019.
- **ip status**: patented
- **prior art notes**: Cassie/Digit derive from Oregon State University academic work (Hurst lab); the academic publications constitute substantial prior art for the bipedal control claims.

## Upkie (2022)

- **id**: `upkie`
- **corpus**: open
- **creator**: Stéphane Caron and contributors
- **disclosure**: Caron, S. et al. Upkie public release, 2022.
- **ip status**: open-permissive
- **prior art notes**: Upkie demonstrates fully-open wheeled-bipedal balancing using commodity mjbots actuators. Anticipates cost-effective wheeled-humanoid designs.
