---
title: "sensing-proprioceptive-actuator"
parent: "Invalidity Contentions"
nav_order: 170
layout: default
---

# Invalidity Contention Packet — `sensing-proprioceptive-actuator`

**Generated:** 2026-05-08  
**Cross-cut tag:** `sensing-proprioceptive-actuator`  
**Entries:** 20 (20 commons-grade, 0 draft)  
**Earliest disclosure:** 1980-11  
**Most recent disclosure:** 2024-02

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `sensing-proprioceptive-actuator`.

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

### 2004 — DLR Hand-II

- **id:** `dlr-hand-ii`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Butterfass, Grebenstein, Liu, Hirzinger; DLR Institute of Robotics and Mechatronics, Oberpfaffenhofen, Germany
- **disclosure citation:** Butterfass, J., Grebenstein, M., Liu, H., Hirzinger, G. 'DLR-Hand II: next generation of a dextrous robot hand'. IEEE ICRA, 2001 (early disclosure); Butterfass, J. et al. 'Design and Experiences with DLR Hand II'. World Automation Congress, 2004.
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `actuator-electric-harmonic-drive`, `actuator-electric-tendon-driven`, `sensing-tactile-fingertip`, `sensing-force-torque`, `sensing-proprioceptive-actuator`

**Prior art notes:**

> DLR Hand-II is the canonical academic disclosure of joint-torque-sensing dexterous hands with compact actuator integration. Anticipates: (1) impedance-controlled dexterous manipulation with proprioceptive sensing — directly relevant to claims on torque-controlled humanoid hands (every modern humanoid hand IP); (2) cable-tendon transmission with harmonic-drive primary reducer — relevant to combined-mechanism actuator claims; (3) per-joint integrated torque sensor with calibrated absolute position — anticipates proprioceptive-actuator IP. The DLR series (Hand-II, then Hand-III, then Hand Arm System) is one of the deepest academic technical lineages in dexterous manipulation. Continuously published in IEEE proceedings since 2001.

**Sources:**

1. Butterfass, J. et al. 'DLR-Hand II: next generation of a dextrous robot hand'. IEEE ICRA 2001.
2. Butterfass, J. et al. 'Design and Experiences with DLR Hand II'. World Automation Congress 2004.

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

### 2011-05 — DLR Hand-Arm System

- **id:** `dlr-hand-arm-system-2011`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Markus Grebenstein, Alin Albu-Schäffer, Antonio Bicchi (collaboration), Gerd Hirzinger; DLR Institute of Robotics and Mechatronics, Oberpfaffenhofen
- **disclosure citation:** Grebenstein, Markus; Albu-Schäffer, Alin; Bahls, Thomas; Chalon, Maxime; Eiberger, Oliver; Friedl, Werner; Gruber, Robin; Haddadin, Sami; Hagn, Ulrich; Haslinger, Robert; Höppner, Hannes; Jörg, Stefan; Nickl, Mathias; Nothhelfer, Alexander; Petit, Florian; Reill, Josef; Seitz, Norbert; Wimböck, Thomas; Wolf, Sebastian; Wüsthoff, Tilo; Hirzinger, Gerd. 'The DLR Hand Arm System.' IEEE International Conference on Robotics and Automation (ICRA), Shanghai, May 2011, pp. 3175-3182. DOI: 10.1109/ICRA.2011.5980371. Companion thesis: Grebenstein, M. 'Approaching Human Performance: The Functionality-Driven Awiwi Robot Hand.' PhD thesis, ETH Zurich, 2012; published Springer Tracts in Advanced Robotics 98, 2014. ISBN 978-3-319-03592-9.
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `mechanism-tendon-routing`, `mechanism-underactuated-grasping`, `actuator-electric-tendon-driven`, `sensing-tactile-fingertip`, `sensing-force-torque`, `sensing-proprioceptive-actuator`

**Prior art notes:**

> The DLR Hand-Arm System (Grebenstein et al. ICRA 2011, Grebenstein PhD/STAR 2014) is the canonical academic disclosure of variable-impedance antagonistically-tendon-driven anthropomorphic hand-arm hardware. Anticipates with element-by-element mechanism-level specificity: (1) mechanically programmable variable joint stiffness via antagonistic tendons with nonlinear elastic elements — directly relevant to commercial claims on variable-stiffness humanoid hand IP; (2) the 19-DoF, 38-tendon, 38-motor architecture with motors in the forearm — relevant to claims on tendon-driven hand-with-forearm-actuation humanoid IP (Tesla Optimus Gen-3, Figure-02, Apptronik Apollo, Sanctuary Phoenix all show variations of this topology); (3) impact-survival via mechanical compliance absorption — anticipates claims on collision-tolerant humanoid hand IP; (4) the biomimetic muscle-tendon co-contraction analogue — relevant to claims on biomimetic humanoid manipulation. Grebenstein's PhD thesis (200+ pages) provides the deepest single-source mechanism disclosure in dexterous robotic hand history. Modern variable-impedance anthropomorphic hand IP filings face this 15-year-deep academic anchor with mechanical-drawing-level specificity.

**Sources:**

1. Grebenstein, M. et al. 'The DLR Hand Arm System.' IEEE ICRA 2011: 3175-3182. DOI: 10.1109/ICRA.2011.5980371.
2. Grebenstein, M. 'Approaching Human Performance: The Functionality-Driven Awiwi Robot Hand.' Springer Tracts in Advanced Robotics 98, 2014. ISBN 978-3-319-03592-9.
3. Wolf, S. et al. 'The DLR FSJ: Energy based design of a variable stiffness joint.' IEEE ICRA 2011 (companion paper on the variable-stiffness joint mechanism).

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

### 2023-08 — BridgeData V2 multi-robot trajectory dataset

- **id:** `bridgedata-v2-walke-2023`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Homer Walke et al., UC Berkeley RAIL / Stanford IRIS
- **disclosure citation:** Walke, Homer, Black, Kevin, Zhao, Tony, Vuong, Quan, Zheng, Chongyi, Hansen-Estruch, Philippe, He, Andre Wang, Myers, Vivek, Kim, Moo Jin, Du, Max, Lee, Abraham, Fang, Kuan, Finn, Chelsea, Levine, Sergey. 'BridgeData V2: A Dataset for Robot Learning at Scale.' Conference on Robot Learning (CoRL) 2023; arXiv:2308.12952, August 2023.
- **disclosed subsystems:** `control-vla-vision-language-action`, `sensing-stereo-camera`, `sensing-proprioceptive-actuator`

**Prior art notes:**

> BridgeData V2 is the canonical scaled trajectory dataset for low-cost manipulator imitation learning prior to the foundation-model robotic policy era. It anticipates with full specificity: (1) claims on language-conditioned manipulation policies trained from scaled demonstration data — BridgeV2 pairs natural-language instructions with each episode and is the headline training corpus for RT-1, RT-2 and Octo follow-ons; (2) claims on cross-environment generalization of imitation policies — the 24-environment span is its core benchmark; (3) claims on affordable-platform shared trajectory infrastructure (the WidowX 250s standardization) anticipating community-platform humanoid IP. Released under CC-BY-4.0 with timestamped arXiv. Modern humanoid VLA training-data claims face this 2023 anchor at element-by-element specificity.

**Sources:**

1. Walke, H. et al. 'BridgeData V2: A Dataset for Robot Learning at Scale.' CoRL 2023; arXiv:2308.12952.
2. BridgeData V2 project page: rail-berkeley.github.io/bridgedata

---

### 2023-10 — Reachy-2 open-source humanoid platform (Pollen Robotics)

- **id:** `reachy-2-pollen-2023`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Pollen Robotics SAS (Matthieu Lapeyre, Pierre Rouanet et al.)
- **disclosure citation:** Pollen Robotics. 'Introducing Reachy 2.' Pollen Robotics blog and product launch, October 2023; technical hardware repository pollen-robotics/reachy2_sdk, GitHub, 2023-2024.
- **disclosed subsystems:** `actuator-electric-quasi-direct-drive`, `actuator-spherical-multi-dof`, `sensing-stereo-camera`, `sensing-imu`, `sensing-proprioceptive-actuator`, `control-teleoperation`, `software-ros2`

**Prior art notes:**

> Reachy-2 is the 2023 successor to the open-source Reachy-1 platform and is one of the few European-origin commercial humanoid upper-bodies released with full open hardware/firmware. It anticipates with full specificity: (1) claims on open-source humanoid SDKs with VR-teleoperation for imitation-learning data collection — Pollen publishes the SDK and Quest-Pro tele-op pipeline on GitHub Apache-2.0; (2) claims on parallel-spherical-mechanism necks (Orbita 3-DoF) — Reachy-2 ships and documents the kinematic with patent-expired joint topology; (3) claims on quasi-direct-drive humanoid arm modules at sub-40kg torso mass — Reachy-2 datasheet and CAD release. Modern humanoid commercial platforms claiming open-hardware tele-op pipelines face this timestamped 2023 anchor.

**Sources:**

1. Pollen Robotics. 'Reachy 2 product launch.' October 2023.
2. GitHub: pollen-robotics/reachy2_sdk, 2023-2024.
3. Reachy 2 hardware documentation (CC-BY-4.0 / Apache-2.0).

---

### 2024-02 — ALOHA-2 enhanced bimanual teleoperation platform

- **id:** `aloha-2-aldaco-2024`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Aldaco, Armstrong, Bingham, Florence, Ichter, Finn, Levine, Zhao et al. (Google DeepMind + Stanford)
- **disclosure citation:** Aldaco, Jorge, Armstrong, Travis, Baruch, Robert, Bingham, Jennifer, Chan, Sanky, Dwibedi, Debidatta, Finn, Chelsea, Florence, Pete, Ichter, Brian, et al. 'ALOHA 2: An Enhanced Low-Cost Hardware for Bimanual Teleoperation.' arXiv:2405.02292, May 2024; Google DeepMind/Stanford joint disclosure February 2024.
- **disclosed subsystems:** `control-teleoperation`, `control-vla-vision-language-action`, `sensing-stereo-camera`, `sensing-proprioceptive-actuator`

**Prior art notes:**

> ALOHA-2 is the canonical 2024 successor of the ALOHA bimanual teleoperation hardware and is the platform-of-record for Google DeepMind / Stanford bimanual imitation-learning papers from 2024 onward. It anticipates with full specificity: (1) claims on low-cost open-hardware bimanual teleoperation kits for imitation-learning data collection — ALOHA-2 publishes complete CAD, BOM, and firmware under Apache-2.0; (2) claims on rubber-compliant parallel-jaw fingertips for delicate-manipulation imitation data — explicitly described in Aldaco et al. 2024; (3) claims on leader-follower puppeteering protocols with friction-compensated gravity models — published with timestamped arXiv. Modern humanoid bimanual data-collection IP faces this anchor at hardware-element specificity.

**Sources:**

1. Aldaco, J. et al. 'ALOHA 2: An Enhanced Low-Cost Hardware for Bimanual Teleoperation.' arXiv:2405.02292, 2024.
2. ALOHA 2 project page: aloha-2.github.io

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `664769a`.*
