---
title: control-mpc
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-mpc`

**26 corpus entries disclose this subsystem.**

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

## Sentis-Khatib Whole-Body Prioritized Task Control (2005)

- **id**: `sentis-khatib-whole-body`
- **corpus**: academic
- **creator**: Luis Sentis and Oussama Khatib, Stanford AI Laboratory
- **disclosure**: Sentis, Luis and Khatib, Oussama. 'Synthesis of whole-body behaviors through hierarchical control of behavioral primitives.' International Journal of Humanoid Robotics 2(4): 505-518, December 2005. Extended in: Sentis, L. and Khatib, O. 'A whole-body control framework for humanoids operating in human environments.' IEEE ICRA, May 2006: 2641-2648.
- **ip status**: public-domain
- **prior art notes**: Sentis-Khatib whole-body operational-space control extends Khatib 1987 to free-floating humanoids with constraint-aware prioritized task stacks. Anticipates with full specificity: (1) whole-body humanoid task-priority controllers — every modern humanoid (Atlas, TORO, HRP-5P, Optimus, Figure 02) executes a derivative of this stack; (2) contact-consistent dynamics where stance-foot constraints are projected out of the task space — directly relevant to claims on multi-contact humanoid balancing; (3) the formal hierarchical-stack structure (high > mid > low priority via null-space chaining) used in essentially every whole-body humanoid controller since 2010. Sentis's 2007 PhD thesis and the IJHR/ICRA papers are heavily cited (>4000 citations combined). Modern whole-body humanoid IP filings face this academic anchor at 21 years' depth.

## Willow Garage PR1 (2008)

- **id**: `willow-pr1`
- **corpus**: academic
- **creator**: Willow Garage / Stanford (Ken Salisbury group)
- **disclosure**: Wyrobek, K.A. et al. 'Towards a Personal Robotics Development Platform: Rationale and Design of an Intrinsically Safe Personal Robot.' ICRA 2008.
- **ip status**: open-permissive
- **prior art notes**: PR1 is significant prior art for safety-by-design humanoid robotics. Cable-driven intrinsically-safe architecture anticipates several modern compliant-actuator humanoid claims.

## DLR Justin (Rollin' Justin) (2009-05)

- **id**: `dlr-justin`
- **corpus**: academic
- **creator**: Borst, Wimboeck, Schmidt, Fuchs, Brunner, Zacharias, Giordano, Konietschke, Sepp, Fuchs, Rink, Albu-Schäffer, Hirzinger; DLR Institute of Robotics and Mechatronics
- **disclosure**: Borst, C., Wimboeck, T., Schmidt, F., Fuchs, M., Brunner, B., Zacharias, F., Giordano, P. R., Konietschke, R., Sepp, W., Fuchs, S., Rink, C., Albu-Schäffer, A., Hirzinger, G. 'Rollin' Justin — Mobile platform with variable base'. IEEE ICRA, May 2009.
- **ip status**: open-permissive
- **prior art notes**: Justin is the canonical academic disclosure of wheeled humanoid mobile manipulation with full impedance control. Anticipates and provides extensive prior art for: (1) wheeled humanoid platform for service tasks — relevant to claims on wheeled humanoid IP (Diligent Moxi, NEXTAGE follow this paradigm); (2) torque-controlled dual-arm coordination — relevant to bimanual humanoid manipulation IP; (3) variable-wheelbase mobile base — relevant to morphology-changing wheeled platform claims. DLR has published Justin disclosures in ICRA, IROS, Humanoids continuously since 2009. Modern wheeled humanoid claims face this deep academic anchor.

## PR2 (2010)

- **id**: `pr2`
- **corpus**: open
- **creator**: Willow Garage
- **disclosure**: Willow Garage. PR2 platform release, 2010.
- **ip status**: open-permissive
- **prior art notes**: PR2 was the platform around which ROS was originally built. Its hardware is significant prior art for omnidirectional wheeled mobile manipulation. ROS itself is even more significant prior art for robotics middleware.

## Toyota HSR (2012)

- **id**: `toyota-hsr`
- **corpus**: private
- **creator**: Toyota Motor Corporation Partner Robot Division
- **disclosure**: Yamamoto, T. et al. 'Development of Human Support Robot as the research platform of a domestic mobile manipulator.' ROBOMECH Journal 6:4, 2019. Earlier 2012 disclosure.
- **ip status**: patented
- **prior art notes**: HSR's telescoping torso with whole-body control is significant prior art for domestic-context wheeled humanoid claims.

## CMU HERB (Home Exploring Robotic Butler) (2012-04)

- **id**: `cmu-herb-srinivasa-2012`
- **corpus**: academic
- **creator**: Siddhartha Srinivasa et al., Carnegie Mellon Personal Robotics Lab / Intel Labs Pittsburgh
- **disclosure**: Srinivasa, Siddhartha S., Berenson, Dmitry, Cakmak, Maya, Collet, Alvaro, Dogar, Mehmet R., Dragan, Anca D., Knepper, Ross A., Niemueller, Tim, Strabala, Kyle, Vande Weghe, Mike, Ziegler, Julius. 'HERB 2.0: Lessons Learned from Developing a Mobile Manipulator for the Home.' Proceedings of the IEEE 100(8): 2410-2428, August 2012. Original disclosure: Srinivasa, S. et al. 'HERB: a home exploring robotic butler.' Autonomous Robots 28(1): 5-20, January 2010.
- **ip status**: public-domain
- **prior art notes**: CMU HERB is one of the most extensively-published academic mobile-manipulator humanoid platforms (>50 papers across 2008-2018). Anticipates with full specificity: (1) claims on home-environment dual-arm humanoid manipulation — HERB's headline contribution including kitchen/office task suite, fridge/microwave/dishwasher manipulation; (2) claims on legible/predictable HRI motion synthesis — Dragan-Srinivasa 2013 'Legibility and Predictability of Robot Motion' is part of the HERB program and anticipates current humanoid social-motion IP; (3) claims on cable-driven backdrivable arms with underactuated 3-finger hands for home manipulation — Barrett WAM + BH-280 are the explicit instantiation; (4) claims on manipulation-among-movable-obstacles planning. Proceedings of IEEE article and Autonomous Robots paper provide deeply-cited timestamped disclosure. Modern home-humanoid IP filings (1X NEO Gamma, Figure 02 home demos) face this 14-year-deep academic anchor.

## NASA Valkyrie (2013)

- **id**: `nasa-valkyrie`
- **corpus**: academic
- **creator**: NASA Johnson Space Center, in collaboration with University of Texas at Austin and others
- **disclosure**: NASA Johnson Space Center, DARPA Robotics Challenge entry, 2013.
- **ip status**: open-permissive
- **prior art notes**: NASA Valkyrie's series-elastic actuator implementations and the IHMC-derived whole-body control work are foundational prior art. The robot was distributed to multiple universities and produced extensive open publications.

## MIT Cheetah (2013)

- **id**: `mit-cheetah`
- **corpus**: academic
- **creator**: MIT Biomimetic Robotics Lab (Sangbae Kim)
- **disclosure**: Seok, S. et al. 'Design principles for energy-efficient legged locomotion and implementation on the MIT Cheetah robot.' IEEE/ASME Transactions on Mechatronics 20(3), 2015. Earlier ICRA 2013 disclosure.
- **ip status**: open-permissive
- **prior art notes**: First-generation MIT Cheetah established the design principles for high-torque electric quadrupeds. Seok 2015 T-Mech paper provides foundational design-principles disclosure that anticipates many subsequent legged-robot actuation claims.

## Atlas (2013-07)

- **id**: `atlas-boston-dynamics`
- **corpus**: private
- **creator**: Boston Dynamics
- **disclosure**: DARPA press release, July 2013, announcing Atlas as DRC platform.
- **ip status**: patented
- **prior art notes**: Boston Dynamics' patents are among the most-cited in the humanoid space and also among the most likely to be challenged on 102/103 grounds given the long academic prior art chain (Honda, AIST, KAIST, MIT). Worth dedicated patent-by-patent analysis.

## MIT Cheetah 2 (2014)

- **id**: `mit-cheetah-2`
- **corpus**: academic
- **creator**: MIT Biomimetic Robotics Lab (Sangbae Kim)
- **disclosure**: Park, H.-W. et al. 'High-speed bounding with the MIT Cheetah 2: Control design and experiments.' International Journal of Robotics Research 36(2), 2017. Earlier ICRA disclosure 2014.
- **ip status**: open-permissive
- **prior art notes**: MIT Cheetah 2 establishes the QDD actuator topology in a working high-speed legged robot. The Wensing 2017 T-RO paper 'Proprioceptive actuator design in the MIT Cheetah' is the foundational actuator design disclosure.

## Boston Dynamics Spot (2015-02)

- **id**: `hyundai-boston-dynamics-spot`
- **corpus**: private
- **creator**: Boston Dynamics (now Hyundai Motor Group subsidiary)
- **disclosure**: Boston Dynamics public reveal of Spot, February 2015.
- **ip status**: patented
- **prior art notes**: Spot is the most commercially deployed quadruped robot. BD's Spot patents face deep prior art from MIT Cheetah series, ANYmal lineage, and academic quadruped literature.

## PAL TALOS (2017)

- **id**: `pal-talos`
- **corpus**: private
- **creator**: PAL Robotics, in collaboration with LAAS-CNRS
- **disclosure**: Stasse, O. et al. 'TALOS: A new humanoid research platform targeted for industrial applications.' IEEE Humanoids 2017.
- **ip status**: patented
- **prior art notes**: TALOS is among the better-published European industrial humanoids. Stasse 2017 IEEE Humanoids paper provides comprehensive design disclosure.

## Kawasaki Kaleido (2017-11)

- **id**: `kawasaki-kaleido`
- **corpus**: private
- **creator**: Kawasaki Heavy Industries
- **disclosure**: Kawasaki Heavy Industries public reveal of Kaleido, iREX November 2017.
- **ip status**: patented
- **prior art notes**: Kawasaki's deep industrial robotics IP base means much of their humanoid claims are anticipated by their own prior industrial robotics disclosures, plus AIST HRP series prior art.

## MIT Cheetah 3 (2018)

- **id**: `mit-cheetah-3`
- **corpus**: academic
- **creator**: MIT Biomimetic Robotics Lab (Sangbae Kim)
- **disclosure**: Bledt, G. et al. 'MIT Cheetah 3: Design and Control of a Robust, Dynamic Quadruped Robot.' IROS 2018.
- **ip status**: open-permissive
- **prior art notes**: Cheetah 3 establishes blind robust legged locomotion using only proprioceptive sensing — a significant prior art point against later vision-dependent legged-robot claims.

## Ghost Robotics Vision 60 (2018)

- **id**: `ghost-robotics-vision-60`
- **corpus**: private
- **creator**: Ghost Robotics
- **disclosure**: Ghost Robotics Vision 60 release, 2018.
- **ip status**: patented
- **prior art notes**: Ghost Robotics derives from Penn's Kod*lab academic quadruped work. The legged-robot patents face the same MIT Cheetah / ANYmal / Penn Kod*lab prior art chain as other quadrupeds.

## HRP-5P (2018-09)

- **id**: `hrp-5p`
- **corpus**: academic
- **creator**: AIST and Kawada Industries
- **disclosure**: Kaneko, K. et al. 'Humanoid Robot HRP-5P: An Electrically Actuated Humanoid Robot With High-Power and Wide-Range Joints.' IEEE Robotics and Automation Letters 4(2), 2019.
- **ip status**: open-permissive
- **prior art notes**: HRP-5P's construction-task demonstrations and high-power actuator disclosures are among the most thoroughly published examples of humanoid construction work. Anticipates many subsequent industrial humanoid claims.

## MIT Mini Cheetah (2019)

- **id**: `mini-cheetah`
- **corpus**: academic
- **creator**: MIT Biomimetic Robotics Lab (Sangbae Kim)
- **disclosure**: Katz, B. et al. 'Mini Cheetah: A Platform for Pushing the Limits of Dynamic Quadruped Control.' ICRA 2019.
- **ip status**: open-permissive
- **prior art notes**: The QDD actuator topology (low gear ratio, high-torque BLDC, transparent backdrivability) is a foundational contribution. Establishes the design space for affordable dynamic legged robots.

## Boston Dynamics Spot (fuel-cell variant) (2020)

- **id**: `spot-fuel-cell`
- **corpus**: private
- **creator**: Boston Dynamics
- **disclosure**: Boston Dynamics partnership announcements with fuel cell vendors, 2020.
- **ip status**: patented
- **prior art notes**: Demonstrates fuel-cell-powered legged robotics at commercial scale. Anticipates fuel-cell power claims in field robotics applications.

## Unitree Go1 (2021-06)

- **id**: `unitree-go1`
- **corpus**: private
- **creator**: Unitree Robotics
- **disclosure**: Unitree Robotics Go1 reveal, June 2021.
- **ip status**: patented
- **prior art notes**: Unitree Go1 actuator design is heavily anticipated by MIT Cheetah QDD prior art (Wensing 2017, Katz 2019). Pricing-driven commodification rather than novel IP.

## Upkie (2022)

- **id**: `upkie`
- **corpus**: open
- **creator**: Stéphane Caron and contributors
- **disclosure**: Caron, S. et al. Upkie public release, 2022.
- **ip status**: open-permissive
- **prior art notes**: Upkie demonstrates fully-open wheeled-bipedal balancing using commodity mjbots actuators. Anticipates cost-effective wheeled-humanoid designs.

## Janner Diffuser planning with diffusion (2022-05)

- **id**: `janner-diffuser-2022`
- **corpus**: academic
- **creator**: Michael Janner, Yilun Du, Joshua Tenenbaum, Sergey Levine, MIT/UC Berkeley
- **disclosure**: Janner, Michael, Du, Yilun, Tenenbaum, Joshua B., Levine, Sergey. 'Planning with Diffusion for Flexible Behavior Synthesis.' Proceedings of the 39th International Conference on Machine Learning (ICML 2022), Baltimore, July 2022; arXiv:2205.09991, May 2022.
- **ip status**: public-domain
- **prior art notes**: Janner Diffuser is the foundational academic disclosure of trajectory-level diffusion as a planner/policy substrate for robotic control, predating Chi et al.'s Diffusion Policy by ~6 months. Anticipates with full specificity: (1) claims on diffusion models trained over state-action trajectories for robotic motion generation — Diffuser discloses the joint state-action trajectory diffusion architecture; (2) claims on classifier-guided sample-time reward/goal conditioning — Diffuser discloses gradient-guided sampling for arbitrary objective composition; (3) claims on receding-horizon diffusion replanning (MPC-style) — Diffuser discloses replan-each-step. >1500 citations; ICML 2022 proceedings and arXiv timestamped. Modern humanoid diffusion-policy IP claims face this 4-year-deep anchor — and importantly Diffuser predates the modern diffusion-policy boom and discloses generic trajectory diffusion before manipulator-specific patents filed in 2023+.

## Apptronik Apollo (2023-08)

- **id**: `apptronik-apollo`
- **corpus**: private
- **creator**: Apptronik
- **disclosure**: Apptronik public reveal of Apollo, August 2023.
- **ip status**: patented
- **prior art notes**: Apptronik's actuator IP has lineage from UT Austin Human-Centered Robotics Lab (Sentis) and from NASA Valkyrie work; both sources constitute substantial prior art that limits the patentable surface area of Apptronik's own claims.

## Rainbow Robotics RB-Y1 (2024-03)

- **id**: `rainbow-robotics-rb-y1`
- **corpus**: private
- **creator**: Rainbow Robotics
- **disclosure**: Rainbow Robotics public reveal of RB-Y1, March 2024.
- **ip status**: patented
- **prior art notes**: Rainbow Robotics has direct lineage from KAIST HUBO program; HUBO academic publications constitute prior art for many of their humanoid claims.
