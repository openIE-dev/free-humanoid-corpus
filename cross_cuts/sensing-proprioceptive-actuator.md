---
title: sensing-proprioceptive-actuator
parent: Cross-cuts
layout: default
---

# Cross-cut: `sensing-proprioceptive-actuator`

**14 corpus entries disclose this subsystem.**

Earliest disclosure: 1980-11

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Hollerbach Recursive Lagrangian Manipulator Dynamics (1980-11)

- **id**: `hollerbach-manipulator-1980`
- **corpus**: academic
- **creator**: John M. Hollerbach, MIT Artificial Intelligence Laboratory
- **disclosure**: Hollerbach, John M. 'A Recursive Lagrangian Formulation of Manipulator Dynamics and a Comparative Study of Dynamics Formulation Complexity.' IEEE Transactions on Systems, Man, and Cybernetics SMC-10(11): 730-736, November 1980.
- **ip status**: public-domain
- **prior art notes**: Hollerbach 1980 is the canonical academic disclosure of efficient recursive Lagrangian manipulator dynamics, alongside Luh-Walker-Paul 1980 Newton-Euler. Anticipates with full specificity: (1) claims on real-time computed-torque inverse-dynamics for humanoid arms — Hollerbach's O(n³) recursion is the basis for every embedded humanoid arm controller since the early 1980s; (2) claims on per-link recursive computation enabling distributed/parallel inverse-dynamics — Hollerbach's structure is explicitly recursive forward-and-backward; (3) the comparative-complexity tabulation enabling design-time formulation selection. >2500 citations; IEEE TSMC archive openly indexed. Lineage runs forward to Featherstone spatial-vector algebra (existing corpus entry) and Articulated-Body Algorithms. Modern humanoid arm-dynamics IP claims face this 46-year-deep anchor.

## Khatib Operational Space Formulation (1987-02)

- **id**: `khatib-operational-space`
- **corpus**: academic
- **creator**: Oussama Khatib, Stanford Artificial Intelligence Laboratory
- **disclosure**: Khatib, Oussama. 'A unified approach for motion and force control of robot manipulators: The operational space formulation.' IEEE Journal of Robotics and Automation, RA-3(1): 43-53, February 1987. Earlier: Khatib, O. 'Dynamic control of manipulators in operational space.' 6th IFToMM Congress on Theory of Machines and Mechanisms, New Delhi, December 1983.
- **ip status**: public-domain
- **prior art notes**: Khatib's 1987 operational-space formulation is the canonical academic disclosure of task-space inverse-dynamics control with null-space projection. It anticipates with full mathematical specificity: (1) the operational-space inertia matrix Λ(x) and its closed-form expression — directly relevant to whole-body torque-control claims for humanoid platforms; (2) null-space projection for redundancy resolution and prioritized task hierarchies — anticipates virtually every whole-body humanoid controller filed since 2010 (Tesla Optimus, Figure 02, 1X NEO, Apptronik Apollo all employ derivatives); (3) unified motion-and-force impedance control via task-space coordinates — anticipates compliant manipulation IP. Continuously cited (>10,000 citations); the IEEE J-RA paper is freely available through IEEE Xplore. Modern claims on task-space humanoid control face a 39-year-deep 102 anchor here.

## Pratt-Williamson Series Elastic Actuator (1995-08)

- **id**: `pratt-williamson-sea`
- **corpus**: academic
- **creator**: Gill A. Pratt and Matthew M. Williamson, MIT Leg Laboratory and MIT AI Lab
- **disclosure**: Pratt, Gill A. and Williamson, Matthew M. 'Series elastic actuators.' IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Pittsburgh PA, August 5-9, 1995: 399-406.
- **ip status**: public-domain
- **prior art notes**: The Pratt-Williamson 1995 paper is the foundational academic disclosure of series-elastic actuators (SEA) — the dominant compliant-actuator architecture in legged and humanoid robotics. Anticipates with full specificity: (1) intentional series mechanical spring as the force-sensing element — directly relevant to claims on compliant humanoid actuators (Cassie, Digit, Apollo SEA derivatives); (2) spring-deflection-based force control without strain gauges — relevant to claims on encoder-only force feedback; (3) the bandwidth/stiffness tradeoff disclosure — anticipates SEA-design IP. Pratt's later commercial work (Yobotics, then Boston Dynamics' Atlas SEA) is grounded in this paper. Heavily cited (>3000 citations); SEA is now a textbook concept. 31-year-deep 102 anchor against any 'compliant humanoid actuator' patent.

## DLR Hand-II (2004)

- **id**: `dlr-hand-ii`
- **corpus**: academic
- **creator**: Butterfass, Grebenstein, Liu, Hirzinger; DLR Institute of Robotics and Mechatronics, Oberpfaffenhofen, Germany
- **disclosure**: Butterfass, J., Grebenstein, M., Liu, H., Hirzinger, G. 'DLR-Hand II: next generation of a dextrous robot hand'. IEEE ICRA, 2001 (early disclosure); Butterfass, J. et al. 'Design and Experiences with DLR Hand II'. World Automation Congress, 2004.
- **ip status**: open-permissive
- **prior art notes**: DLR Hand-II is the canonical academic disclosure of joint-torque-sensing dexterous hands with compact actuator integration. Anticipates: (1) impedance-controlled dexterous manipulation with proprioceptive sensing — directly relevant to claims on torque-controlled humanoid hands (every modern humanoid hand IP); (2) cable-tendon transmission with harmonic-drive primary reducer — relevant to combined-mechanism actuator claims; (3) per-joint integrated torque sensor with calibrated absolute position — anticipates proprioceptive-actuator IP. The DLR series (Hand-II, then Hand-III, then Hand Arm System) is one of the deepest academic technical lineages in dexterous manipulation. Continuously published in IEEE proceedings since 2001.

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

## DLR Justin (Rollin' Justin) (2009-05)

- **id**: `dlr-justin`
- **corpus**: academic
- **creator**: Borst, Wimboeck, Schmidt, Fuchs, Brunner, Zacharias, Giordano, Konietschke, Sepp, Fuchs, Rink, Albu-Schäffer, Hirzinger; DLR Institute of Robotics and Mechatronics
- **disclosure**: Borst, C., Wimboeck, T., Schmidt, F., Fuchs, M., Brunner, B., Zacharias, F., Giordano, P. R., Konietschke, R., Sepp, W., Fuchs, S., Rink, C., Albu-Schäffer, A., Hirzinger, G. 'Rollin' Justin — Mobile platform with variable base'. IEEE ICRA, May 2009.
- **ip status**: open-permissive
- **prior art notes**: Justin is the canonical academic disclosure of wheeled humanoid mobile manipulation with full impedance control. Anticipates and provides extensive prior art for: (1) wheeled humanoid platform for service tasks — relevant to claims on wheeled humanoid IP (Diligent Moxi, NEXTAGE follow this paradigm); (2) torque-controlled dual-arm coordination — relevant to bimanual humanoid manipulation IP; (3) variable-wheelbase mobile base — relevant to morphology-changing wheeled platform claims. DLR has published Justin disclosures in ICRA, IROS, Humanoids continuously since 2009. Modern wheeled humanoid claims face this deep academic anchor.

## Ijspeert-Schaal Dynamic Movement Primitives (formal extension) (2013-02)

- **id**: `ijspeert-dmp-2013`
- **corpus**: academic
- **creator**: Auke Ijspeert, Stefan Schaal, Jun Nakanishi, Heiko Hoffmann, Peter Pastor
- **disclosure**: Ijspeert, Auke Jan, Nakanishi, Jun, Hoffmann, Heiko, Pastor, Peter, Schaal, Stefan. 'Dynamical Movement Primitives: Learning Attractor Models for Motor Behaviors.' Neural Computation 25(2): 328-373, February 2013. Earlier foundations: Schaal, S., Peters, J., Nakanishi, J., Ijspeert, A. 'Learning movement primitives.' International Symposium on Robotics Research (ISRR) 2003; Schaal, Mohajerian, Ijspeert. 'Dynamics systems vs. optimal control — a unifying view.' Progress in Brain Research 165: 425-445, 2007.
- **ip status**: public-domain
- **prior art notes**: Ijspeert-Schaal DMPs are the canonical academic disclosure of learnable, stable, parameterized motor primitives for robotic motion generation. The 2013 Neural Computation paper consolidates the formal framework; the 2007 Progress in Brain Research extension and the 2002-2003 Schaal/Ijspeert papers establish lineage. Anticipates with full specificity: (1) claims on demonstration-learned humanoid motion primitives with online goal modulation — DMPs disclose the closed-form ODE structure used in essentially every humanoid skill-library paper since 2007; (2) claims on rhythmic locomotion primitives with phase coupling — directly anticipates pattern-generator humanoid IP; (3) claims on obstacle-avoiding modulated motion primitives — the coupling-term extension is explicit in the 2013 paper. >5000 citations; broadly available through open Neural Computation archives. Modern humanoid skill-primitive IP filings face this lineage at 13-23 years' depth.

## MIT Cheetah 2 (2014)

- **id**: `mit-cheetah-2`
- **corpus**: academic
- **creator**: MIT Biomimetic Robotics Lab (Sangbae Kim)
- **disclosure**: Park, H.-W. et al. 'High-speed bounding with the MIT Cheetah 2: Control design and experiments.' International Journal of Robotics Research 36(2), 2017. Earlier ICRA disclosure 2014.
- **ip status**: open-permissive
- **prior art notes**: MIT Cheetah 2 establishes the QDD actuator topology in a working high-speed legged robot. The Wensing 2017 T-RO paper 'Proprioceptive actuator design in the MIT Cheetah' is the foundational actuator design disclosure.

## DLR TORO (2014-07)

- **id**: `dlr-toro`
- **corpus**: academic
- **creator**: Englsberger, Werner, Ott, Henze, Roa, Garofalo, Burger, Beyer, Eiberger, Schmid, Albu-Schäffer; DLR Institute of Robotics and Mechatronics
- **disclosure**: Englsberger, J., Werner, A., Ott, C., Henze, B., Roa, M.A., Garofalo, G., Burger, R., Beyer, A., Eiberger, O., Schmid, K., Albu-Schäffer, A. 'Overview of the torque-controlled humanoid robot TORO'. IEEE-RAS Humanoids, July 2014.
- **ip status**: open-permissive
- **prior art notes**: TORO is the canonical academic disclosure of full-body torque-controlled bipedal humanoid with DCM (Divergent Component of Motion) walking control. Anticipates: (1) torque-controlled whole-body bipedal walking — directly relevant to claims on whole-body torque-controlled humanoid platforms; (2) DCM walking as an alternative to ZMP — relevant to walking-control IP; (3) impedance-control whole-body interaction with humans — relevant to safe-human-interaction humanoid claims. DLR's Englsberger paper introduced the DCM formulation that subsequent humanoids (HRP-5P, several private platforms) adopted. Publicly funded research with extensive IEEE-proceedings publication.

## Reachy 1 (Pollen Robotics open-source humanoid) (2017-09)

- **id**: `reachy-1-pollen-2017`
- **corpus**: open
- **creator**: Pollen Robotics / INRIA Flowers (Pierre Rouanet, Matthieu Lapeyre, Pierre-Yves Oudeyer)
- **disclosure**: Mick, Sébastien, Lapeyre, Matthieu, Rouanet, Pierre, Halgand, Christophe, Benois-Pineau, Jenny, Paclet, Florent, Cattaert, Daniel, Oudeyer, Pierre-Yves, de Rugy, Aymar. 'Reachy, a 3D-Printed Human-Like Robotic Arm as a Testbed for Human-Robot Control Strategies.' Frontiers in Neurorobotics 13:65, September 2019. Original release: Pollen Robotics / INRIA Flowers, 2017 GitHub release of Reachy v1 (poppy-project lineage).
- **ip status**: open-source
- **prior art notes**: Reachy 1 (Pollen Robotics 2017, INRIA Flowers lineage) is one of the earliest fully-open-hardware humanoid torso platforms with a published research-grade SDK predating commercial offerings. Anticipates with full specificity: (1) claims on 3D-printed open-hardware humanoid arms with Dynamixel-class actuation — Reachy 1's STL/STEP CAD and firmware are publicly archived since 2017; (2) claims on research-substrate Python SDKs for humanoid telemanipulation — reachy-sdk on GitHub at v0.x predates most commercial humanoid SDK offerings; (3) claims on dual-arm research-platform configurations with anthropomorphic spherical wrists. The 2019 Frontiers paper provides peer-reviewed timestamped disclosure; GitHub commits provide finer-grained 2016-2017 priority. Existing corpus 'reachy' entry should reference this v1 ancestor. Modern open-humanoid IP filings face Reachy 1 at 9-year-deep anchor.

## MIT Cheetah 3 (2018)

- **id**: `mit-cheetah-3`
- **corpus**: academic
- **creator**: MIT Biomimetic Robotics Lab (Sangbae Kim)
- **disclosure**: Bledt, G. et al. 'MIT Cheetah 3: Design and Control of a Robust, Dynamic Quadruped Robot.' IROS 2018.
- **ip status**: open-permissive
- **prior art notes**: Cheetah 3 establishes blind robust legged locomotion using only proprioceptive sensing — a significant prior art point against later vision-dependent legged-robot claims.

## MIT Mini Cheetah (2019)

- **id**: `mini-cheetah`
- **corpus**: academic
- **creator**: MIT Biomimetic Robotics Lab (Sangbae Kim)
- **disclosure**: Katz, B. et al. 'Mini Cheetah: A Platform for Pushing the Limits of Dynamic Quadruped Control.' ICRA 2019.
- **ip status**: open-permissive
- **prior art notes**: The QDD actuator topology (low gear ratio, high-torque BLDC, transparent backdrivability) is a foundational contribution. Establishes the design space for affordable dynamic legged robots.

## BridgeData V2 multi-robot trajectory dataset (2023-08)

- **id**: `bridgedata-v2-walke-2023`
- **corpus**: academic
- **creator**: Homer Walke et al., UC Berkeley RAIL / Stanford IRIS
- **disclosure**: Walke, Homer, Black, Kevin, Zhao, Tony, Vuong, Quan, Zheng, Chongyi, Hansen-Estruch, Philippe, He, Andre Wang, Myers, Vivek, Kim, Moo Jin, Du, Max, Lee, Abraham, Fang, Kuan, Finn, Chelsea, Levine, Sergey. 'BridgeData V2: A Dataset for Robot Learning at Scale.' Conference on Robot Learning (CoRL) 2023; arXiv:2308.12952, August 2023.
- **ip status**: public-domain
- **prior art notes**: BridgeData V2 is the canonical scaled trajectory dataset for low-cost manipulator imitation learning prior to the foundation-model robotic policy era. It anticipates with full specificity: (1) claims on language-conditioned manipulation policies trained from scaled demonstration data — BridgeV2 pairs natural-language instructions with each episode and is the headline training corpus for RT-1, RT-2 and Octo follow-ons; (2) claims on cross-environment generalization of imitation policies — the 24-environment span is its core benchmark; (3) claims on affordable-platform shared trajectory infrastructure (the WidowX 250s standardization) anticipating community-platform humanoid IP. Released under CC-BY-4.0 with timestamped arXiv. Modern humanoid VLA training-data claims face this 2023 anchor at element-by-element specificity.
