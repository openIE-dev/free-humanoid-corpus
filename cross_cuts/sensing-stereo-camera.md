---
title: sensing-stereo-camera
parent: Cross-cuts
layout: default
---

# Cross-cut: `sensing-stereo-camera`

**83 corpus entries disclose this subsystem.**

Earliest disclosure: 1973

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## WABOT-1 (1973)

- **id**: `wabot-1`
- **corpus**: academic
- **creator**: Waseda University, Kato Laboratory
- **disclosure**: Kato, Ichiro et al. 'Information-Power Machine with Senses and Limbs (WABOT-1).' Proceedings of First CISM-IFToMM Symposium on Theory and Practice of Robots and Manipulators, 1973.
- **ip status**: public-domain
- **prior art notes**: First full-scale humanoid in academic record. Anticipates virtually every subsystem of modern humanoids at concept level: bipedal locomotion, bimanual manipulation, multimodal sensing, natural language interface. Specific implementations are crude by modern standards but the architectural decomposition is foundational.

## Lucas-Kanade Optical Flow (1981-08)

- **id**: `lucas-kanade-1981`
- **corpus**: academic
- **creator**: Bruce D. Lucas and Takeo Kanade, Carnegie Mellon University
- **disclosure**: Lucas, Bruce D. and Kanade, Takeo. 'An iterative image registration technique with an application to stereo vision'. Proceedings of the 7th International Joint Conference on Artificial Intelligence (IJCAI), Vancouver, August 1981, pp. 674-679.
- **ip status**: public-domain
- **prior art notes**: Lucas-Kanade 1981 is the foundational academic disclosure of dense optical flow estimation for robotic vision. Anticipates with 45 years of prior art: (1) optical-flow-based visual servoing for humanoid manipulation and locomotion — relevant to claims on visual-tracking-based humanoid policies; (2) iterative least-squares formulation that extends to modern KLT and PWC-style optical flow networks; (3) image-pyramid for multi-scale flow estimation. The KLT tracker is essentially the universal default for visual feature tracking and underlies SLAM, visual odometry, and many manipulation control loops. Modern visual humanoid IP all face this 1981 academic anchor.

## RoboCop (Alex Murphy) (1987-07-17)

- **id**: `robocop-1987`
- **corpus**: fictional
- **creator**: Paul Verhoeven; Edward Neumeier and Michael Miner (writers); Omni Consumer Products (in-fiction)
- **disclosure**: Verhoeven, Paul (dir.); Neumeier, Edward and Miner, Michael (writers). RoboCop. Orion Pictures, July 17, 1987.
- **ip status**: fictional
- **prior art notes**: RoboCop's Prime Directives architecture is a foundational fictional disclosure of *enumerated, prioritized, hard-constraint safety supervisors with disclosed backdoors*. Anticipates with notable specificity: (1) explicit prioritized list of safety directives operating as hard constraints — relevant to modern Simplex/CBF/RTA-style safety supervisor IP; (2) the *failure mode* of operator-installed backdoors in safety supervisors (Directive 4 prevents arrest of OCP senior staff) — directly relevant to claims on tamper-resistant safety policies; this is the single most prescient pre-2010 fictional disclosure of the alignment-failure modes that modern safety-supervisor IP attempts to address; (3) integrated armed humanoid for civic deployment — relevant to law-enforcement humanoid IP. Continuously available since 1987; the Prime Directives sequence is widely cited in safety-architecture pedagogy.

## ALVINN (Autonomous Land Vehicle in a Neural Network) (1989)

- **id**: `pomerleau-alvinn`
- **corpus**: academic
- **creator**: Dean Pomerleau; Carnegie Mellon University Robotics Institute
- **disclosure**: Pomerleau, Dean A. 'ALVINN: An Autonomous Land Vehicle in a Neural Network'. NIPS 1988 (December 1988); published in Touretzky, D.S. (ed.), Advances in Neural Information Processing Systems 1: 305-313, Morgan Kaufmann, 1989.
- **ip status**: public-domain
- **prior art notes**: Pomerleau's ALVINN is the foundational academic disclosure of end-to-end vision-to-action neural network policies — the architectural pattern that modern VLA models implement at scale. Anticipates: (1) end-to-end vision-to-action neural policy as a deployable control architecture — directly relevant to RT-1, RT-2, OpenVLA, Octo, and every subsequent foundation-model-policy claim; (2) training data augmentation via simulated variation — relevant to sim-to-real claims; (3) deploying neural policies on real-world hardware — relevant to deployment-on-robot patents. The 1989 NIPS paper and subsequent CMU technical reports establish the lineage that culminates in modern VLA systems. Modern VLA claims face this 35-year academic anchor as 102 prior art.

## Robonaut 1 (1996)

- **id**: `robonaut-1`
- **corpus**: academic
- **creator**: Robert O. Ambrose, Myron A. Diftler, et al.; NASA Johnson Space Center, with DARPA
- **disclosure**: Diftler, M.A., Ambrose, R.O. 'Robonaut: A Robotic Astronaut Assistant'. International Symposium on Artificial Intelligence, Robotics and Automation in Space (i-SAIRAS) 2001 (consolidated paper); earlier disclosures NASA JSC 1996 onwards.
- **ip status**: public-domain
- **prior art notes**: Robonaut 1 is the academic predecessor to Robonaut 2 and the deepest NASA-side disclosure of humanoid platform IP for space applications. Anticipates: (1) torso-only humanoid form factor for collaborative work with humans — relevant to current commercial torso-only humanoid claims; (2) VR teleoperation with force-feedback gloves as the operator interface — relevant to teleoperation IP; (3) tendon-driven anthropomorphic hands integrated with harmonic-drive arms — relevant to integrated-hand-arm claims. NASA JSC publications and i-SAIRAS proceedings are publicly accessible. Modern humanoid hand claims face this 1996 academic anchor.

## Sony AIBO (1999-05-11)

- **id**: `sony-aibo`
- **corpus**: private
- **creator**: Sony Corporation
- **disclosure**: Sony Corporation announcement of AIBO ERS-110, May 11, 1999.
- **ip status**: patented
- **prior art notes**: AIBO is foundational prior art for consumer quadruped robots. Sony's 1990s-2000s patents cover quadruped behavior architecture, learning systems, and small-form-factor actuators. Many expired or near expiration.

## SIFT (Scale-Invariant Feature Transform) (1999-09)

- **id**: `lowe-sift-1999`
- **corpus**: academic
- **creator**: David G. Lowe, University of British Columbia
- **disclosure**: Lowe, David G. 'Object recognition from local scale-invariant features'. Proceedings of the IEEE International Conference on Computer Vision (ICCV), Corfu, September 1999, pp. 1150-1157. Extended in Lowe, D.G. 'Distinctive image features from scale-invariant keypoints'. IJCV 60(2): 91-110, 2004.
- **ip status**: patented
- **prior art notes**: SIFT 1999 (and the canonical 2004 IJCV paper) is one of the most-cited algorithms in computer vision and a foundational visual-feature anchor for humanoid perception. Anticipates: (1) scale-invariant feature detection and matching — relevant to claims on visual humanoid perception that use feature-based localization (every visual SLAM system pre-deep-learning, and many modern hybrid systems, use SIFT or its descendants ORB / SURF); (2) the 128-D local-gradient histogram descriptor architecture. Patented (US6711293, expired 2020); the 2004 IJCV paper is the standard citation. Modern visual humanoid IP that uses local-feature matching faces this 27-year academic anchor.

## ASIMO (2000-10-31)

- **id**: `asimo`
- **corpus**: private
- **creator**: Honda Motor Co.
- **disclosure**: Honda Motor Co. press conference, Tokyo, October 31, 2000.
- **ip status**: patented
- **prior art notes**: ASIMO's public disclosures and Honda's published papers anticipate most claimed innovations in modern bipedal humanoids. The Hirose/Ogawa 2007 Phil. Trans. paper is a particularly comprehensive disclosure that should be referenced when reading current humanoid patent claims.

## HRP-2 (2002)

- **id**: `hrp-2`
- **corpus**: academic
- **creator**: AIST (National Institute of Advanced Industrial Science and Technology), Kawada Industries
- **disclosure**: Kaneko, K. et al. 'Design of prototype humanoid robotics platform for HRP.' IROS 2002.
- **ip status**: open-permissive
- **prior art notes**: OpenHRP is itself foundational prior art for open robotics simulation frameworks. HRP-2 was among the first humanoids to publicly demonstrate falling-and-recovering behaviors.

## Sony QRIO (2003-03)

- **id**: `sony-qrio`
- **corpus**: private
- **creator**: Sony Corporation
- **disclosure**: Sony Corporation public reveal of QRIO, March 2003.
- **ip status**: patented
- **prior art notes**: QRIO's intelligent servo actuator architecture (embedded control in each joint module) is significant prior art for distributed-control humanoid actuator claims. Sony's now-expiring patents are a deep prior art well.

## HUBO (2004)

- **id**: `hubo`
- **corpus**: academic
- **creator**: KAIST, Hubo Lab (Jun-Ho Oh)
- **disclosure**: Park, Ill-Woo et al. 'Mechanical Design of Humanoid Robot Platform KHR-3 (HUBO).' IEEE-RAS Humanoids 2005.
- **ip status**: open-permissive
- **prior art notes**: DRC-Hubo's 2015 win demonstrated transformer-style transitioning between bipedal and wheeled-knee modes for navigating both stairs and flat ground. Anticipates: hybrid locomotion modes in humanoids.

## NAO (2006)

- **id**: `nao`
- **corpus**: private
- **creator**: Aldebaran Robotics (later SoftBank Robotics, then UBT)
- **disclosure**: Gouaillier, D. et al. 'Mechatronic design of NAO humanoid.' ICRA 2009.
- **ip status**: patented
- **prior art notes**: NAO's mechatronic design publication is well-cited prior art. The platform's wide academic distribution since 2006 makes its design choices broadly disclosed.

## Toyota Partner Robot (Violin) (2007)

- **id**: `toyota-partner-robot-violin`
- **corpus**: private
- **creator**: Toyota Motor Corporation Partner Robot Division
- **disclosure**: Toyota Motor Corporation public reveal, 2007.
- **ip status**: patented
- **prior art notes**: Toyota's high-precision finger control disclosures are significant prior art for fine motor control humanoid claims.

## iCub (2008)

- **id**: `icub`
- **corpus**: academic
- **creator**: Italian Institute of Technology (IIT) and the RobotCub Consortium
- **disclosure**: Metta, G. et al. 'The iCub humanoid robot: an open platform for research in embodied cognition.' PerMIS 2008.
- **ip status**: open-permissive
- **prior art notes**: Among the earliest fully open-source humanoid platforms with hardware design released. Anticipates: tendon-driven anthropomorphic hands, full-body artificial skin, open robotics middleware.

## HRP-3 (2008)

- **id**: `hrp-3`
- **corpus**: academic
- **creator**: AIST and Kawada Industries
- **disclosure**: Kaneko, K. et al. 'Humanoid Robot HRP-3.' IROS 2008.
- **ip status**: open-permissive
- **prior art notes**: HRP-3's environmental sealing disclosures anticipate subsequent IP-rated humanoid claims. The HRP series is a deep commons asset because of consistent open academic disclosure across generations.

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

## DARwIn-OP (2010)

- **id**: `darwin-op`
- **corpus**: open
- **creator**: Robotis Co. with University of Pennsylvania, Virginia Tech, Purdue
- **disclosure**: Ha, I. et al. 'Development of Open Humanoid Platform DARwIn-OP.' SICE 2011.
- **ip status**: open-permissive
- **prior art notes**: DARwIn-OP is foundational prior art for fully-open small-scale humanoid platforms. Predates Poppy by several years for the academic-open category.

## PR2 (2010)

- **id**: `pr2`
- **corpus**: open
- **creator**: Willow Garage
- **disclosure**: Willow Garage. PR2 platform release, 2010.
- **ip status**: open-permissive
- **prior art notes**: PR2 was the platform around which ROS was originally built. Its hardware is significant prior art for omnidirectional wheeled mobile manipulation. ROS itself is even more significant prior art for robotics middleware.

## HRP-4 (2010)

- **id**: `hrp-4`
- **corpus**: academic
- **creator**: AIST and Kawada Industries
- **disclosure**: Kaneko, K. et al. 'Humanoid Robot HRP-4: Humanoid Robotics Platform with Lightweight and Slim Body.' IROS 2010.
- **ip status**: open-permissive
- **prior art notes**: HRP-4 lightweight design anticipates subsequent slim-form humanoid claims. The 2010 IROS paper provides full mechanical specifications openly.

## Robonaut 2 (2010-02)

- **id**: `robonaut-2`
- **corpus**: academic
- **creator**: NASA Johnson Space Center, in partnership with General Motors
- **disclosure**: Diftler, M.A. et al. 'Robonaut 2 — The First Humanoid Robot in Space.' ICRA 2011.
- **ip status**: patented
- **prior art notes**: Robonaut 2's hand design, with 12 DoF per hand and tendon routing through the forearm, is foundational prior art for high-DoF tendon-driven humanoid hands. The NASA-GM patent portfolio has been extensively cited.

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

## REEM-C (2013)

- **id**: `reem-c`
- **corpus**: private
- **creator**: PAL Robotics
- **disclosure**: PAL Robotics REEM-C release, 2013.
- **ip status**: patented
- **prior art notes**: REEM-C distributed to multiple research labs; design characteristics openly published.

## Atlas (2013-07)

- **id**: `atlas-boston-dynamics`
- **corpus**: private
- **creator**: Boston Dynamics
- **disclosure**: DARPA press release, July 2013, announcing Atlas as DRC platform.
- **ip status**: patented
- **prior art notes**: Boston Dynamics' patents are among the most-cited in the humanoid space and also among the most likely to be challenged on 102/103 grounds given the long academic prior art chain (Honda, AIST, KAIST, MIT). Worth dedicated patent-by-patent analysis.

## Poppy Humanoid (2014)

- **id**: `poppy-humanoid`
- **corpus**: open
- **creator**: Inria Flowers Team / Poppy Project
- **disclosure**: Lapeyre, Matthieu et al. 'Poppy Humanoid Platform: Experimental Evaluation of the Role of a Bio-inspired Thigh Shape.' IEEE Humanoids 2013.
- **ip status**: open-permissive
- **prior art notes**: Among the earliest fully-open 3D-printable humanoids. Anticipates open-source educational humanoid platforms broadly.

## CMU Personal Robotics Lab Andy / HERB-2 follow-on platform (2014-05)

- **id**: `cmu-andy-herb2-srinivasa-2014`
- **corpus**: academic
- **creator**: Siddhartha Srinivasa, Anca Dragan, J. Andrew Bagnell, and the CMU Personal Robotics Lab
- **disclosure**: Srinivasa, Siddhartha S. et al. 'HERB 2.0: Lessons Learned from Developing a Mobile Manipulator for the Home.' Proceedings of the IEEE, vol. 100, no. 8, 2012; subsequent Andy disclosures: Dragan, Anca and Srinivasa, S. 'A Policy-Blending Formalism for Shared Control.' IJRR 32(7), 2013; Bagnell et al. CHIMP/Andy whole-body manipulation reports 2013-2015.
- **ip status**: public-domain
- **prior art notes**: The Andy / HERB-2 generation extends HERB-1 with formal shared-autonomy theory and is the survey-of-record for bimanual mobile-manipulator home robots in 2012-2015. It anticipates with full specificity: (1) claims on shared-autonomy arbitration between operator and policy — Dragan-Srinivasa policy-blending IJRR 2013 publishes the closed-form linear arbitration in confidence space; (2) claims on task-space-region constraint encoding for manipulation planning — Berenson-Srinivasa-Kuffner ICRA 2009 publishes TSR formalism executed on this platform; (3) claims on underactuated cable-driven grasping for unstructured pick-and-place — Barrett BH-280 deployment is the canonical published baseline. Modern humanoid manipulation IP claiming shared-autonomy or constraint-region planning faces these timestamped CMU disclosures.

## Pepper (2014-06)

- **id**: `pepper-softbank`
- **corpus**: private
- **creator**: SoftBank Robotics (formerly Aldebaran)
- **disclosure**: SoftBank Robotics public reveal of Pepper, June 2014.
- **ip status**: patented
- **prior art notes**: Pepper is foundational prior art for wheeled-base humanoid social robots. The omnidirectional wheeled base design has been widely cited.

## Atlas academic publications (Kuindersma et al., DRC era) (2014-06)

- **id**: `atlas-academic-disclosures`
- **corpus**: academic
- **creator**: Scott Kuindersma, Russ Tedrake, Robin Deits, Maurice Fallon, Andrés Valenzuela, Hongkai Dai, Frank Permenter, Twan Koolen, Pat Marion; MIT CSAIL Robot Locomotion Group (DRC Atlas team)
- **disclosure**: Kuindersma, Scott; Permenter, Frank; Tedrake, Russ. 'An efficiently solvable quadratic program for stabilizing dynamic locomotion.' IEEE International Conference on Robotics and Automation (ICRA), Hong Kong, June 2014, pp. 2589-2594. DOI: 10.1109/ICRA.2014.6907230. Consolidated Atlas-on-DRC paper: Kuindersma, S.; Deits, R.; Fallon, M.; Valenzuela, A.; Dai, H.; Permenter, F.; Koolen, T.; Marion, P.; Tedrake, R. 'Optimization-based locomotion planning, estimation, and control design for the Atlas humanoid robot.' Autonomous Robots 40(3): 429-455, March 2016. DOI: 10.1007/s10514-015-9479-3.
- **ip status**: public-domain
- **prior art notes**: The MIT DRC Atlas academic publication trail (Kuindersma-Tedrake et al. 2014-2016) is distinct from the Boston Dynamics Atlas product entry (atlas-boston-dynamics) and from the Sentis-Khatib WBOSC entry: it is the canonical academic disclosure of the actually-deployed Atlas controller stack as fielded at the DARPA Robotics Challenge Finals (June 2015). Anticipates with element-by-element specificity: (1) whole-body QP-based inverse-dynamics control on a hydraulically-actuated humanoid platform — directly relevant to commercial claims on QP-based humanoid IP (every modern humanoid runs a derivative); (2) the IRIS-regions mixed-integer convex footstep planner — relevant to claims on footstep-planning humanoid IP; (3) iterative SQP trajectory optimization with contact schedule — anticipates claims overlapping Crocoddyl (mastalli-crocoddyl-2020) and DDP approaches; (4) the consolidated end-to-end stack documentation in AURO 2016 — the most complete public disclosure of a working DRC-class humanoid control architecture. Drake source code accompanies the publications under BSD license. Modern QP-IDC-based humanoid IP filings face this 12-year-deep academic anchor with full implementation disclosure.

## Boston Dynamics Spot (2015-02)

- **id**: `hyundai-boston-dynamics-spot`
- **corpus**: private
- **creator**: Boston Dynamics (now Hyundai Motor Group subsidiary)
- **disclosure**: Boston Dynamics public reveal of Spot, February 2015.
- **ip status**: patented
- **prior art notes**: Spot is the most commercially deployed quadruped robot. BD's Spot patents face deep prior art from MIT Cheetah series, ANYmal lineage, and academic quadruped literature.

## Levine Guided Policy Search end-to-end manipulation on PR2/BRETT (2015-04)

- **id**: `levine-gps-pr2-2016`
- **corpus**: academic
- **creator**: Sergey Levine, Chelsea Finn, Trevor Darrell, Pieter Abbeel, UC Berkeley
- **disclosure**: Levine, Sergey, Finn, Chelsea, Darrell, Trevor, Abbeel, Pieter. 'End-to-End Training of Deep Visuomotor Policies.' Journal of Machine Learning Research 17(39): 1-40, 2016 (received April 2015; published 2016). Earlier: Levine, S., Wagener, N., Abbeel, P. 'Learning Contact-Rich Manipulation Skills with Guided Policy Search.' ICRA 2015.
- **ip status**: public-domain
- **prior art notes**: Levine et al. 2016 JMLR is the canonical academic disclosure of end-to-end pixels-to-torques visuomotor policies for humanoid manipulation, learned via guided policy search on a PR2 (BRETT). Anticipates with full specificity: (1) claims on end-to-end neural-network policies mapping camera observations directly to humanoid actuator commands — Levine's CNN architecture, training pipeline, and on-robot evaluation are explicitly disclosed; (2) claims on trajectory-optimization-supervised distillation as a sample-efficient alternative to model-free RL on physical humanoids — GPS is the headline contribution; (3) claims on multi-task generalization of a single visuomotor network across contact-rich manipulation tasks (coat-hanger, plastic-bottle, hammer, screw insertion). >3500 citations; JMLR open access; arXiv preprint 2015. The lineage runs directly forward to RT-1, RT-2, OpenVLA, and modern humanoid VLA systems. Modern humanoid end-to-end visuomotor IP filings face this 11-year-deep anchor with full architecture disclosure.

## ORB-SLAM (2015-04)

- **id**: `orb-slam-mur-artal-2015`
- **corpus**: academic
- **creator**: Raul Mur-Artal, J.M.M. Montiel, Juan D. Tardós; University of Zaragoza
- **disclosure**: Mur-Artal, Raul; Montiel, J.M.M.; Tardós, Juan D. 'ORB-SLAM: a versatile and accurate monocular SLAM system'. IEEE Transactions on Robotics 31(5): 1147-1163, October 2015. Extended: ORB-SLAM2 (RGB-D + stereo, 2017); ORB-SLAM3 (visual-inertial + multi-map, 2021).
- **ip status**: open-permissive
- **prior art notes**: ORB-SLAM is one of the standard reference visual SLAM systems for humanoid platforms. Anticipates: (1) real-time monocular SLAM as a deployable architecture — relevant to claims on humanoid visual localization; (2) the three-thread tracking + mapping + loop-closing architecture — relevant to multi-thread perception humanoid IP; (3) ORB-feature-based place recognition for loop closure — relevant to scene-recognition humanoid claims. The 2015 T-RO paper plus subsequent ORB-SLAM2 (2017) and ORB-SLAM3 (2021) extensions provide deep prior art coverage; the GitHub release (GPL-v3) makes the architecture defensively-published.

## ANYmal (2016)

- **id**: `anymal`
- **corpus**: private
- **creator**: ANYbotics, ETH Zurich Robotic Systems Lab
- **disclosure**: Hutter, M. et al. 'ANYmal — a highly mobile and dynamic quadrupedal robot.' IROS 2016.
- **ip status**: patented
- **prior art notes**: ANYbotics SEA design heavily anticipated by NASA Valkyrie and Robonaut SEA work. ETH RSL academic publications provide open prior art for many control claims.

## Sophia (2016-04)

- **id**: `hanson-sophia`
- **corpus**: private
- **creator**: Hanson Robotics
- **disclosure**: Hanson Robotics public reveal of Sophia, April 2016.
- **ip status**: patented
- **prior art notes**: Hanson's Frubber synthetic skin material and facial actuation prior art is significant for any claim around expressive humanoid faces. Disney Imagineering's earlier work is the deeper prior art.

## The Wild Robot — ROZZUM unit 7134 (2016-04)

- **id**: `wild-robot-rozzum-7134-brown-2016`
- **corpus**: fictional
- **creator**: Peter Brown (novelist); Chris Sanders (DreamWorks adaptation)
- **disclosure**: Brown, Peter. 'The Wild Robot.' Little, Brown Books for Young Readers, 5 April 2016; ISBN 978-0316382007. DreamWorks Animation theatrical adaptation directed by Chris Sanders, released 27 September 2024.
- **ip status**: public-domain
- **prior art notes**: Peter Brown's 'The Wild Robot' (2016) and the DreamWorks 2024 theatrical adaptation form the canonical mass-media anchor for mass-produced general-purpose service humanoids that dramatically refine their objective functions through wilderness-environment adaptation. It anticipates with full specificity: (1) claims on mass-produced bipedal service humanoids with weatherproof construction and multi-arm tool-changer configurations — ROZZUM datasheet language used in the novel; (2) claims on adaptive policy revision in service humanoids exposed to long-duration unstructured environments — Roz's three-year island arc dramatizes exactly this; (3) claims on cross-species or cross-cultural communication acquisition by a service humanoid — Roz's animal-language acquisition is the second-act core. Children's-book bestseller 2016; DreamWorks theatrical release 27 September 2024 reached ~$330M box office.

## KX-series Imperial Security Droids (K-2SO) (2016-12)

- **id**: `kx-series-k2so-2016`
- **corpus**: fictional
- **creator**: Lucasfilm / Disney (Gareth Edwards director, Tony Gilroy writer for Andor)
- **disclosure**: Edwards, Gareth (dir.). Rogue One: A Star Wars Story. Lucasfilm / Disney, December 16, 2016. Subsequent appearances: Andor (Disney+ TV series), 2022; Star Wars: From a Certain Point of View, Del Rey, 2017.
- **ip status**: fictional
- **prior art notes**: The KX-series Imperial security droid (Rogue One 2016, Andor 2022) provides a high-visibility fictional disclosure of mass-deployed humanoid security/combat droids with explicit reprogramming and behavioral-mode architecture. Anticipates with full specificity: (1) claims on humanoid security platforms with checkpoint-officer / combat-infantry dual-mode behavioral architecture — K-2SO's mode-switching is explicit in Rogue One and central to Andor; (2) claims on reprogrammable humanoid platforms where the OEM identity (Imperial) is overwritten by post-deployment reprogramming (Rebellion service); (3) claims on humanoid platforms with integrated language-affect modules (the sarcasm/dry-wit subsystem); (4) claims on native infantry-weapon-handling humanoid droids as part of standardized fleet equipment loadouts. Worldwide theatrical release Dec 2016 + Disney+ Andor 2022-2025 + Lucasfilm visual dictionaries provide deep timestamped disclosure with technical specifications in companion publications.

## PAL TALOS (2017)

- **id**: `pal-talos`
- **corpus**: private
- **creator**: PAL Robotics, in collaboration with LAAS-CNRS
- **disclosure**: Stasse, O. et al. 'TALOS: A new humanoid research platform targeted for industrial applications.' IEEE Humanoids 2017.
- **ip status**: patented
- **prior art notes**: TALOS is among the better-published European industrial humanoids. Stasse 2017 IEEE Humanoids paper provides comprehensive design disclosure.

## Reachy 1 (Pollen Robotics open-source humanoid) (2017-09)

- **id**: `reachy-1-pollen-2017`
- **corpus**: open
- **creator**: Pollen Robotics / INRIA Flowers (Pierre Rouanet, Matthieu Lapeyre, Pierre-Yves Oudeyer)
- **disclosure**: Mick, Sébastien, Lapeyre, Matthieu, Rouanet, Pierre, Halgand, Christophe, Benois-Pineau, Jenny, Paclet, Florent, Cattaert, Daniel, Oudeyer, Pierre-Yves, de Rugy, Aymar. 'Reachy, a 3D-Printed Human-Like Robotic Arm as a Testbed for Human-Robot Control Strategies.' Frontiers in Neurorobotics 13:65, September 2019. Original release: Pollen Robotics / INRIA Flowers, 2017 GitHub release of Reachy v1 (poppy-project lineage).
- **ip status**: open-source
- **prior art notes**: Reachy 1 (Pollen Robotics 2017, INRIA Flowers lineage) is one of the earliest fully-open-hardware humanoid torso platforms with a published research-grade SDK predating commercial offerings. Anticipates with full specificity: (1) claims on 3D-printed open-hardware humanoid arms with Dynamixel-class actuation — Reachy 1's STL/STEP CAD and firmware are publicly archived since 2017; (2) claims on research-substrate Python SDKs for humanoid telemanipulation — reachy-sdk on GitHub at v0.x predates most commercial humanoid SDK offerings; (3) claims on dual-arm research-platform configurations with anthropomorphic spherical wrists. The 2019 Frontiers paper provides peer-reviewed timestamped disclosure; GitHub commits provide finer-grained 2016-2017 priority. Existing corpus 'reachy' entry should reference this v1 ancestor. Modern open-humanoid IP filings face Reachy 1 at 9-year-deep anchor.

## Toyota T-HR3 (2017-11)

- **id**: `toyota-thr3`
- **corpus**: private
- **creator**: Toyota Motor Corporation Partner Robot Division
- **disclosure**: Toyota Motor Corporation public reveal, November 2017.
- **ip status**: patented
- **prior art notes**: T-HR3 is significant prior art for whole-body teleoperated humanoids with force feedback. The Master Maneuvering System teleoperation interface anticipates many modern humanoid teleop claims.

## Kawasaki Kaleido (2017-11)

- **id**: `kawasaki-kaleido`
- **corpus**: private
- **creator**: Kawasaki Heavy Industries
- **disclosure**: Kawasaki Heavy Industries public reveal of Kaleido, iREX November 2017.
- **ip status**: patented
- **prior art notes**: Kawasaki's deep industrial robotics IP base means much of their humanoid claims are anticipated by their own prior industrial robotics disclosures, plus AIST HRP series prior art.

## Black Mirror 'Metalhead' autonomous quadruped killer (2017-12)

- **id**: `black-mirror-metalhead-2017`
- **corpus**: fictional
- **creator**: Charlie Brooker (writer), David Slade (director), House of Tomorrow / Netflix
- **disclosure**: Black Mirror, Series 4, Episode 5, 'Metalhead.' Written by Charlie Brooker; directed by David Slade; released on Netflix 29 December 2017.
- **ip status**: public-domain
- **prior art notes**: 'Metalhead' is the canonical 2017 mass-media anchor for autonomous quadruped lethal-defense robots and was directly modeled on the Boston Dynamics SpotMini reveal. It anticipates with full specificity: (1) claims on quadruped robots equipped with weapon payloads operating in fully-autonomous lethal-engagement mode — the episode dramatizes exactly this throughout 41 minutes; (2) claims on shrapnel-tag persistent-tracker payloads that mark a target for prolonged pursuit — this is the headline mechanism of the second act; (3) claims on SpotMini-class compact electric quadruped morphology with integrated manipulator arm — the visual design and Brooker's published commentary explicitly cite Boston Dynamics inspiration. Released on Netflix with timestamped 29 December 2017 distribution to ~109 million subscribers.

## Ghost Robotics Vision 60 (2018)

- **id**: `ghost-robotics-vision-60`
- **corpus**: private
- **creator**: Ghost Robotics
- **disclosure**: Ghost Robotics Vision 60 release, 2018.
- **ip status**: patented
- **prior art notes**: Ghost Robotics derives from Penn's Kod*lab academic quadruped work. The legged-robot patents face the same MIT Cheetah / ANYmal / Penn Kod*lab prior art chain as other quadrupeds.

## UBTech Walker (2018-01)

- **id**: `ubtech-walker`
- **corpus**: private
- **creator**: UBTech Robotics
- **disclosure**: UBTech public reveal of Walker, CES January 2018.
- **ip status**: patented
- **prior art notes**: UBTech's bipedal locomotion claims anticipated by Honda P-series and ASIMO disclosures.

## OmniGibson / iGibson (Stanford SVL) (2018-04)

- **id**: `stanford-omnigibson-2023`
- **corpus**: academic
- **creator**: Stanford Vision and Learning Lab (Silvio Savarese, Fei-Fei Li); lead authors include Fei Xia, Chengshu Li, Roberto Martín-Martín, Sanjana Srivastava, Cem Gokmen
- **disclosure**: Xia, Fei; Zamir, Amir R.; He, Zhiyang; Sax, Alexander; Malik, Jitendra; Savarese, Silvio. 'Gibson Env: Real-World Perception for Embodied Agents.' IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Salt Lake City, June 2018, pp. 9068-9079. DOI: 10.1109/CVPR.2018.00945. iGibson 2.0: Li, Chengshu et al. 'iGibson 2.0: Object-Centric Simulation for Robot Learning of Everyday Household Tasks.' Conference on Robot Learning (CoRL) 2021. OmniGibson: Li, Chengshu et al. 'BEHAVIOR-1K: A Benchmark for Embodied AI with 1,000 Everyday Activities and Realistic Simulation.' CoRL 2022. Source: https://github.com/StanfordVL/OmniGibson, MIT license.
- **ip status**: open-permissive
- **prior art notes**: Stanford OmniGibson / iGibson / Gibson (Xia et al. CVPR 2018; Li et al. CoRL 2021; BEHAVIOR-1K CoRL 2022) is the canonical academic disclosure of large-scale photorealistic household-task embodied-AI simulation, published MIT-licensed by Stanford SVL. Anticipates with full source-level specificity: (1) 1,000-task ADL benchmark for household humanoid IP — directly relevant to commercial claims on home-task humanoid VLA training (Tesla Optimus household demo set, Figure 02 home tasks, 1X NEO domestic operation, Genesis AI cooking demos); (2) the articulated-object household scene corpus with 50K+ objects — relevant to claims on simulated-household-data humanoid training; (3) predicate-based goal specification ('apple is on table', 'cabinet is open') — relevant to claims on language-and-state-grounded humanoid task specification; (4) the photorealistic-rendering-for-RL pipeline established by Gibson 2018 — anticipates claims on photorealistic-sim-to-real humanoid pipelines. Modern household-humanoid VLA training pipeline IP filings face this 8-year-deep open-source academic anchor (or shorter for OmniGibson/BEHAVIOR-1K specifically).

## HRP-5P (2018-09)

- **id**: `hrp-5p`
- **corpus**: academic
- **creator**: AIST and Kawada Industries
- **disclosure**: Kaneko, K. et al. 'Humanoid Robot HRP-5P: An Electrically Actuated Humanoid Robot With High-Power and Wide-Range Joints.' IEEE Robotics and Automation Letters 4(2), 2019.
- **ip status**: open-permissive
- **prior art notes**: HRP-5P's construction-task demonstrations and high-power actuator disclosures are among the most thoroughly published examples of humanoid construction work. Anticipates many subsequent industrial humanoid claims.

## Stanford JackRabbot 2 (JR-2) wheeled-arm research robot (2018-10)

- **id**: `stanford-jr2-2018`
- **corpus**: academic
- **creator**: Stanford Vision and Learning Lab (Silvio Savarese et al.)
- **disclosure**: Martín-Martín, Roberto, Patel, Mihir, Rezatofighi, Hamid, Shenoi, Abhijeet, Gwak, JunYoung, Frankel, Eric, Sadeghian, Amir, Savarese, Silvio. 'JRDB: A Dataset and Benchmark for Visual Perception for Navigation in Human Environments.' arXiv:1910.11792, October 2019. Robot platform first disclosed: Stanford Vision and Learning Lab, October 2018 release announcement; JRDB dataset released alongside.
- **ip status**: public-domain
- **prior art notes**: Stanford JR-2 (2018) is a canonical academic wheeled-arm research humanoid for social navigation research, with associated public benchmark dataset (JRDB). Anticipates with full specificity: (1) claims on wheeled-balancing humanoids with dual mounted manipulators at human shoulder height — JR-2's Segway-base + dual Kinova architecture is a published exemplar; (2) claims on 360° multi-modal sensor fusion (lidar+cameras+audio) for human-environment navigation — JR-2 carries the full sensor stack; (3) claims on human-aware social navigation benchmarks paired with platform — JRDB releases 64 minutes of annotated multi-modal data alongside the platform. Stanford SVL hosts CAD/sensor specs and the JRDB benchmark openly. Modern wheeled-humanoid IP filings (Apptronik Apollo, Agility Cassie/Digit base, 1X NEO) face this 8-year-deep academic anchor.

## Digit (2019-01)

- **id**: `agility-digit`
- **corpus**: private
- **creator**: Agility Robotics
- **disclosure**: Agility Robotics public reveal, CES January 2019.
- **ip status**: patented
- **prior art notes**: Cassie/Digit derive from Oregon State University academic work (Hurst lab); the academic publications constitute substantial prior art for the bipedal control claims.

## Habitat-Sim (Facebook AI Research) (2019-04)

- **id**: `fair-habitat-sim-2019`
- **corpus**: academic
- **creator**: Facebook AI Research (FAIR) and Georgia Tech (Dhruv Batra), Simon Fraser University (Manolis Savva); collaborative team including Jitendra Malik (Berkeley), Vladlen Koltun (Intel)
- **disclosure**: Savva, Manolis; Kadian, Abhishek; Maksymets, Oleksandr; Zhao, Yili; Wijmans, Erik; Jain, Bhavana; Straub, Julian; Liu, Jia; Koltun, Vladlen; Malik, Jitendra; Parikh, Devi; Batra, Dhruv. 'Habitat: A Platform for Embodied AI Research.' IEEE/CVF International Conference on Computer Vision (ICCV), Seoul, October-November 2019, pp. 9339-9347. DOI: 10.1109/ICCV.2019.00943. arXiv:1904.01201, April 2019. Source code at https://github.com/facebookresearch/habitat-sim. MIT license.
- **ip status**: open-permissive
- **prior art notes**: Habitat-Sim (Savva et al. ICCV 2019; Habitat 2.0 NeurIPS 2021; Habitat 3.0 ICLR 2024) is the canonical academic disclosure of large-scale GPU-accelerated 3D-scanned indoor embodied-AI simulation, published MIT-licensed by FAIR. Anticipates with element-by-element specificity: (1) >10,000 fps rendering of photorealistic indoor scenes for RL training — directly relevant to commercial claims on simulation-at-scale humanoid embodied-AI pipelines; (2) the navigation-benchmark task suite (PointGoal, ObjectGoal, ImageGoal) that is now standard in embodied-AI literature — relevant to claims on humanoid navigation policy IP; (3) Habitat 3.0's humanoid-avatar simulation for social robot interaction — relevant to claims on human-aware humanoid IP and home-deployment humanoid VLA pipelines; (4) integration of large-scale 3D-scan corpora (Matterport, HM3D) with MIT-licensed renderers — relevant to claims on commercial-grade photorealistic simulation. Habitat is the most-cited embodied-AI simulator (>2000 citations on the 2019 paper alone). Modern household-deployment humanoid VLA pipeline IP filings face this 7-year-deep open-source academic anchor.

## Diligent Moxi (2019-09)

- **id**: `diligent-moxi`
- **corpus**: private
- **creator**: Diligent Robotics
- **disclosure**: Diligent Robotics public reveal of Moxi, September 2019.
- **ip status**: patented
- **prior art notes**: Diligent's claims around mobile manipulation in healthcare environments face extensive prior art from PR2, HSR, and academic mobile manipulation literature.

## Reachy (2020)

- **id**: `reachy`
- **corpus**: open
- **creator**: Pollen Robotics
- **disclosure**: Pollen Robotics. Reachy public release, 2020.
- **ip status**: open-permissive
- **prior art notes**: Reachy's Orbita 3-DoF spherical actuator is novel-ish but anticipated by extensive academic spherical-motor literature. Open hardware files constitute prior art for the specific implementation.

## Boston Dynamics Spot (fuel-cell variant) (2020)

- **id**: `spot-fuel-cell`
- **corpus**: private
- **creator**: Boston Dynamics
- **disclosure**: Boston Dynamics partnership announcements with fuel cell vendors, 2020.
- **ip status**: patented
- **prior art notes**: Demonstrates fuel-cell-powered legged robotics at commercial scale. Anticipates fuel-cell power claims in field robotics applications.

## Klara and the Sun — Artificial Friend (AF) child companion (2021-03)

- **id**: `ishiguro-klara-and-the-sun-2021`
- **corpus**: fictional
- **creator**: Kazuo Ishiguro
- **disclosure**: Ishiguro, Kazuo. 'Klara and the Sun.' Faber & Faber (UK) / Alfred A. Knopf (US), 2 March 2021; ISBN 978-0593318171.
- **ip status**: public-domain
- **prior art notes**: Ishiguro's 'Klara and the Sun' (2021) is the canonical literary-fiction anchor for solar-powered child-companion AFs by a Nobel-laureate author. It anticipates with full specificity: (1) claims on solar-powered humanoid child-companion robots with continually-learning observation policies — Klara's solar dependence and observational learning are core to the novel; (2) claims on model-generation lineage with successive sensorimotor refinement (B1/B2/B3) — explicit market-segmentation language used; (3) claims on companion humanoids designed as 'continuation' substitutes for ill or deceased humans — the Josie subplot dramatizes exactly this proposed substitution. Published with hardcover ISBN and timestamped 2 March 2021 release; international literary distribution; Nobel-laureate author elevates evidentiary weight.

## Tesla Optimus (2021-08-19)

- **id**: `tesla-optimus`
- **corpus**: private
- **creator**: Tesla, Inc.
- **disclosure**: Tesla AI Day 1, August 19, 2021, Palo Alto.
- **ip status**: patented
- **prior art notes**: Tesla's claims around vision-only humanoid perception are heavily anticipated by academic vision-based humanoid work. Actuator IP claims should be examined against Honda harmonic drive prior art.

## Ameca (2021-12)

- **id**: `ameca`
- **corpus**: private
- **creator**: Engineered Arts
- **disclosure**: Engineered Arts public reveal, December 2021.
- **ip status**: patented
- **prior art notes**: Engineered Arts' animatronic facial expression IP is heavily anticipated by Disney Imagineering work and by academic facial-animation robotics.

## Sanctuary Phoenix Gen 6 (2022)

- **id**: `sanctuary-phoenix-gen6`
- **corpus**: private
- **creator**: Sanctuary AI
- **disclosure**: Sanctuary AI public reveals of Phoenix predecessors, 2020-2022.
- **ip status**: patented
- **prior art notes**: Sanctuary's hybrid hydraulic-electric actuation faces extensive prior art from Boston Dynamics Atlas (hydraulic), Honda (electric), and academic hybrid actuation literature.

## ANYmal-D industrial quadruped (ETH RSL / ANYbotics) (2022-09)

- **id**: `anymal-d-eth-rsl-2022`
- **corpus**: academic
- **creator**: ANYbotics AG / ETH Zürich Robotic Systems Lab (Marco Hutter)
- **disclosure**: ANYbotics product disclosure ANYmal D, September 2022; technical updates in Miki, Takahiro et al. 'Learning robust perceptive locomotion for quadrupedal robots in the wild.' Science Robotics 7(62), 2022; Hoeller, David et al. 'ANYmal Parkour: Learning agile navigation for quadrupedal robots.' Science Robotics 9(88), 2024.
- **ip status**: public-domain
- **prior art notes**: ANYmal-D is the production-deployed industrial quadruped of the 2022-2024 period and the platform for the headline RSL/ANYbotics RL-locomotion papers in Science Robotics. It anticipates with full specificity: (1) claims on perceptive-locomotion RL policies trained in simulation and transferred to outdoor industrial terrain — Miki Sci.Rob. 2022 publishes the teacher-student distillation pipeline running on this hardware; (2) claims on agile parkour-class learned locomotion — Hoeller Sci.Rob. 2024 publishes the policy on ANYmal-D; (3) claims on series-elastic torque-controlled quadruped joints in IP67 industrial enclosures — ANYdrive disclosed at IROS 2018 with hardware refresh on D-variant. Modern legged-robot IP claims face this timestamped industrial-deployment anchor.

## RT-1 (Robotics Transformer 1) (2022-12-13)

- **id**: `rt-1`
- **corpus**: academic
- **creator**: Google Robotics (Brohan et al.)
- **disclosure**: Brohan, Anthony et al. 'RT-1: Robotics Transformer for Real-World Control at Scale.' arXiv:2212.06817, December 13, 2022. Authors: Brohan, A., Brown, N., Carbajal, J., Chebotar, Y., Dabis, J., Finn, C., Gopalakrishnan, K., Hausman, K., Herzog, A., Hsu, J., Ibarz, J., Ichter, B., Irpan, A., Jackson, T., Jesmonth, S., Joshi, N.J., Julian, R., Kalashnikov, D., Kuang, Y., Leal, I., Lee, K-H., Levine, S., Lu, Y., Malla, U., Manjunath, D., Mordatch, I., Nachum, O., Parada, C., Peralta, J., Perez, E., Pertsch, K., Quiambao, J., Rao, K., Ryoo, M., Salazar, G., Sanketi, P., Sayed, K., Singh, J., Sontakke, S., Stewart, A., Tan, J., Tompson, J., Vanhoucke, V., Vuong, Q., Wahid, A., Welker, S., Wohlhart, P., Wu, J., Xia, F., Xiao, T., Xu, P., Xu, S., Yu, T., Zitkovich, B. (Google).
- **ip status**: open-permissive
- **prior art notes**: RT-1 is the foundational academic disclosure of large-scale Transformer-based vision-language-action policy for real robot control, predating RT-2 (2023) and OpenVLA (2024). Anticipates with full architectural specificity: (1) tokenized action space for cross-task transformer policies — directly relevant to claims on action-tokenization in modern VLAs (Tesla Optimus, Figure 02, 1X NEO, Physical Intelligence π-zero all employ derivatives); (2) language-conditioned manipulation policy with multi-image history — relevant to instruction-following manipulation IP; (3) the data-scaling law showing performance vs. dataset size for robot policies — relevant to claims on data-driven policy training. Code and data partially released under permissive licenses; arXiv preprint available since December 2022. Brohan et al. paper foundational for the entire VLA lineage.

## Sanctuary AI Phoenix (2023-05)

- **id**: `sanctuary-phoenix`
- **corpus**: private
- **creator**: Sanctuary AI
- **disclosure**: Sanctuary AI public reveal, May 2023.
- **ip status**: patented
- **prior art notes**: Sanctuary's high-DoF hand claims face Shadow Hand (2003) and iCub (2008) as deep prior art for tendon-driven anthropomorphic hands with high finger DoF.

## Fourier GR-1 (2023-07)

- **id**: `fourier-gr1`
- **corpus**: private
- **creator**: Fourier Intelligence
- **disclosure**: Fourier Intelligence public reveal of GR-1, July 2023, World AI Conference Shanghai.
- **ip status**: patented
- **prior art notes**: Fourier transitions from rehabilitation exoskeletons to humanoids; actuator IP from exoskeleton work potentially anticipates some humanoid actuator claims by other companies.

## RH20T heterogeneous robot trajectory dataset (2023-07)

- **id**: `rh20t-fang-2024`
- **corpus**: academic
- **creator**: Hao-Shu Fang et al., Shanghai Jiao Tong University Machine Vision and Intelligence Group
- **disclosure**: Fang, Hao-Shu, Fang, Hongjie, Tang, Zhenyu, Liu, Jirong, Wang, Junbo, Zhu, Haoyi, Lu, Cewu. 'RH20T: A Comprehensive Robotic Dataset for Learning Diverse Skills in One-Shot.' arXiv:2307.00595, July 2023; ICRA 2024 workshop and project release.
- **ip status**: public-domain
- **prior art notes**: RH20T is one of the largest publicly-released heterogeneous robot trajectory datasets prior to OpenX-Embodiment. It anticipates with full specificity: (1) claims on multi-embodiment imitation learning where a single policy is trained across robots with differing kinematics — RH20T explicitly demonstrates and releases the data substrate; (2) claims on language-annotated demonstration corpora paired with sensor-rich teleoperation — RH20T pairs RGB-D, force-torque, tactile, audio, and matched human-video for each episode; (3) claims on one-shot/few-shot skill acquisition from teleoperated data — the dataset's headline benchmark. Released CC-BY 4.0 with timestamped arXiv and project page; broadly indexed. Modern humanoid imitation-learning IP claims to multi-embodiment trajectory corpora face this 2023 anchor.

## Unitree H1 (2023-08)

- **id**: `unitree-h1`
- **corpus**: private
- **creator**: Unitree Robotics
- **disclosure**: Unitree Robotics public reveal, August 2023.
- **ip status**: patented
- **prior art notes**: Unitree's actuator IP largely derives from quadruped work (Go1, Aliengo) which is itself heavily anticipated by MIT Mini Cheetah QDD lineage.

## Apptronik Apollo (2023-08)

- **id**: `apptronik-apollo`
- **corpus**: private
- **creator**: Apptronik
- **disclosure**: Apptronik public reveal of Apollo, August 2023.
- **ip status**: patented
- **prior art notes**: Apptronik's actuator IP has lineage from UT Austin Human-Centered Robotics Lab (Sentis) and from NASA Valkyrie work; both sources constitute substantial prior art that limits the patentable surface area of Apptronik's own claims.

## AgiBot A1 (2023-08)

- **id**: `agibot-a1`
- **corpus**: private
- **creator**: AgiBot (Shanghai Zhiyuan New Technology Co.)
- **disclosure**: AgiBot (Shanghai Zhiyuan New Technology) public reveal, August 2023.
- **ip status**: patented
- **prior art notes**: AgiBot's actuator IP heavily anticipated by Honda P-series harmonic drive work and MIT Cheetah QDD lineage. Chinese-language patent filings should be enumerated in strengthening pass.

## BridgeData V2 multi-robot trajectory dataset (2023-08)

- **id**: `bridgedata-v2-walke-2023`
- **corpus**: academic
- **creator**: Homer Walke et al., UC Berkeley RAIL / Stanford IRIS
- **disclosure**: Walke, Homer, Black, Kevin, Zhao, Tony, Vuong, Quan, Zheng, Chongyi, Hansen-Estruch, Philippe, He, Andre Wang, Myers, Vivek, Kim, Moo Jin, Du, Max, Lee, Abraham, Fang, Kuan, Finn, Chelsea, Levine, Sergey. 'BridgeData V2: A Dataset for Robot Learning at Scale.' Conference on Robot Learning (CoRL) 2023; arXiv:2308.12952, August 2023.
- **ip status**: public-domain
- **prior art notes**: BridgeData V2 is the canonical scaled trajectory dataset for low-cost manipulator imitation learning prior to the foundation-model robotic policy era. It anticipates with full specificity: (1) claims on language-conditioned manipulation policies trained from scaled demonstration data — BridgeV2 pairs natural-language instructions with each episode and is the headline training corpus for RT-1, RT-2 and Octo follow-ons; (2) claims on cross-environment generalization of imitation policies — the 24-environment span is its core benchmark; (3) claims on affordable-platform shared trajectory infrastructure (the WidowX 250s standardization) anticipating community-platform humanoid IP. Released under CC-BY-4.0 with timestamped arXiv. Modern humanoid VLA training-data claims face this 2023 anchor at element-by-element specificity.

## Apptronik Apollo academic and technical disclosures (2023-2024) (2023-08)

- **id**: `apptronik-apollo-publications-2024`
- **corpus**: academic
- **creator**: Apptronik Inc. (Jeff Cardenas, Nick Paine, Luis Sentis lineage from UT Austin Human-Centered Robotics Lab)
- **disclosure**: Apptronik. 'Apollo: A Commercial Humanoid Robot for the Workforce.' Apptronik whitepaper, August 2023; Knabe, Coleman et al. 'Designing a Force-Controlled Linear Series Elastic Actuator.' (NASA Valkyrie / Apptronik lineage) IROS 2014; Apptronik-NASA JSC disclosures 2023-2024 including SAFFiR/Valkyrie genealogy white-papers.
- **ip status**: public-domain
- **prior art notes**: This entry isolates the academic-publication and technical-disclosure trail behind Apptronik Apollo (distinct from the Apollo product seed entry). It anticipates with full specificity: (1) claims on humanoid SEA actuator topology — Knabe-Paine et al. IROS 2014 publishes the linear-SEA design that lineally seeds Apollo; (2) claims on whole-body operational-space control for force-interactive humanoid manipulation — Sentis-Khatib WBOSC 2007/2010 papers (UT Austin lineage carried into Apptronik) are foundational and timestamped; (3) claims on hot-swap-battery torso integration with regenerative power electronics on humanoid platforms — Apollo whitepaper August 2023 discloses publicly. Modern humanoid commercial-platform IP claims to SEA torque control or WBOSC face this Apptronik publication trail at element-by-element specificity.

## NVIDIA Isaac Lab (2023-08)

- **id**: `nvidia-isaac-lab-2024`
- **corpus**: academic
- **creator**: Mittal et al.; NVIDIA Corporation, ETH Zürich Robotic Systems Lab (Hutter), and University of Toronto Vector Institute (Garg)
- **disclosure**: Mittal, Mayank; Yu, Calvin; Yu, Qinxi; Liu, Jingzhou; Rudin, Nikita; Hoeller, David; Yuan, Jia Lin; Tehrani, Pooria S.; Singh, Ritvik; Guo, Yunrong; Mazhar, Hammad; Mandlekar, Ajay; Babich, Buck; State, Gavriel; Hutter, Marco; Garg, Animesh. 'ORBIT: A Unified Simulation Framework for Interactive Robot Learning Environments.' IEEE Robotics and Automation Letters (RA-L), August 2023; later released and rebranded as Isaac Lab in 2024. Repository at https://github.com/isaac-sim/IsaacLab.
- **ip status**: open-permissive
- **prior art notes**: Isaac Lab (formerly ORBIT, 2023) is the canonical academic-published GPU-parallelized simulation framework for robot learning, published BSD-3-Clause by NVIDIA + ETH Zürich + University of Toronto. Anticipates with full architectural specificity: (1) thousands-of-parallel-environments humanoid RL training on a single GPU — directly relevant to commercial claims on simulation-at-scale humanoid training pipelines (NVIDIA GR00T, Tesla Optimus, Figure 02 all use this paradigm); (2) URDF/USD-asset interoperability surface enabling cross-platform humanoid descriptors — relevant to claims on cross-platform humanoid descriptor IP; (3) the standardized RL task interface (gym-like API with vectorized environments) — relevant to claims on humanoid-task-curriculum IP; (4) integrated sensor simulation with domain randomization — relevant to claims on sim-to-real-via-randomization humanoid pipelines (anticipated already by OpenAI Dactyl 2018 but Isaac Lab provides the GPU-scale implementation). Mittal et al. RA-L 2023 paper has been cited >300 times by 2026 and underpins essentially every recent humanoid-RL publication. Modern sim-to-real-at-scale humanoid IP filings face this 3-year-deep open-source academic anchor.

## Figure 01 (2023-10)

- **id**: `figure-01`
- **corpus**: private
- **creator**: Figure AI
- **disclosure**: Figure AI public reveal, October 2023.
- **ip status**: patented
- **prior art notes**: Figure's claimed innovations in electric humanoid actuation are heavily anticipated by Honda's E-series and ASIMO publications, by KAIST HUBO papers, and by the entire academic literature.

## Reachy-2 open-source humanoid platform (Pollen Robotics) (2023-10)

- **id**: `reachy-2-pollen-2023`
- **corpus**: academic
- **creator**: Pollen Robotics SAS (Matthieu Lapeyre, Pierre Rouanet et al.)
- **disclosure**: Pollen Robotics. 'Introducing Reachy 2.' Pollen Robotics blog and product launch, October 2023; technical hardware repository pollen-robotics/reachy2_sdk, GitHub, 2023-2024.
- **ip status**: public-domain
- **prior art notes**: Reachy-2 is the 2023 successor to the open-source Reachy-1 platform and is one of the few European-origin commercial humanoid upper-bodies released with full open hardware/firmware. It anticipates with full specificity: (1) claims on open-source humanoid SDKs with VR-teleoperation for imitation-learning data collection — Pollen publishes the SDK and Quest-Pro tele-op pipeline on GitHub Apache-2.0; (2) claims on parallel-spherical-mechanism necks (Orbita 3-DoF) — Reachy-2 ships and documents the kinematic with patent-expired joint topology; (3) claims on quasi-direct-drive humanoid arm modules at sub-40kg torso mass — Reachy-2 datasheet and CAD release. Modern humanoid commercial platforms claiming open-hardware tele-op pipelines face this timestamped 2023 anchor.

## LimX Dynamics CL-1 (2023-12)

- **id**: `limx-cl1`
- **corpus**: private
- **creator**: LimX Dynamics
- **disclosure**: LimX Dynamics public reveal, December 2023.
- **ip status**: patented
- **prior art notes**: LimX QDD actuation derives from MIT Cheetah lineage; bipedal control claims anticipated by Cassie/ATRIAS work.

## 1X NEO (2024)

- **id**: `1x-neo`
- **corpus**: private
- **creator**: 1X Technologies (formerly Halodi Robotics)
- **disclosure**: 1X Technologies public reveal, 2024.
- **ip status**: patented
- **prior art notes**: Tendon-driven compliant actuation is heavily anticipated by iCub, by Shadow Robot Hand work, and by decades of academic compliant-actuation literature.

## K-Scale Labs Open Source Humanoid (2024)

- **id**: `k-scale-os`
- **corpus**: open
- **creator**: K-Scale Labs
- **disclosure**: K-Scale Labs project launch, 2024.
- **ip status**: open-permissive
- **prior art notes**: Among the most ambitious recent fully-open humanoid efforts. Direct peer to Free Humanoid in scope.

## Berkeley Humanoid (2024)

- **id**: `berkeley-humanoid`
- **corpus**: academic
- **creator**: UC Berkeley, Hybrid Robotics Lab
- **disclosure**: Liao, Q. et al. 'Berkeley Humanoid: A Research Platform for Learning-based Control.' arXiv 2024.
- **ip status**: open-permissive
- **prior art notes**: Berkeley quasi-direct-drive lineage (predates the humanoid; comes from the Mini Cheetah / leg work) anticipates many actuator architecture claims.

## Persona AI Mentee (2024)

- **id**: `persona-ai-mentee`
- **corpus**: private
- **creator**: Persona AI
- **disclosure**: Persona AI public reveal, 2024.
- **ip status**: trade-secret
- **prior art notes**: Public technical disclosure is thin; strengthening pass needed.

## ALOHA-2 enhanced bimanual teleoperation platform (2024-02)

- **id**: `aloha-2-aldaco-2024`
- **corpus**: academic
- **creator**: Aldaco, Armstrong, Bingham, Florence, Ichter, Finn, Levine, Zhao et al. (Google DeepMind + Stanford)
- **disclosure**: Aldaco, Jorge, Armstrong, Travis, Baruch, Robert, Bingham, Jennifer, Chan, Sanky, Dwibedi, Debidatta, Finn, Chelsea, Florence, Pete, Ichter, Brian, et al. 'ALOHA 2: An Enhanced Low-Cost Hardware for Bimanual Teleoperation.' arXiv:2405.02292, May 2024; Google DeepMind/Stanford joint disclosure February 2024.
- **ip status**: public-domain
- **prior art notes**: ALOHA-2 is the canonical 2024 successor of the ALOHA bimanual teleoperation hardware and is the platform-of-record for Google DeepMind / Stanford bimanual imitation-learning papers from 2024 onward. It anticipates with full specificity: (1) claims on low-cost open-hardware bimanual teleoperation kits for imitation-learning data collection — ALOHA-2 publishes complete CAD, BOM, and firmware under Apache-2.0; (2) claims on rubber-compliant parallel-jaw fingertips for delicate-manipulation imitation data — explicitly described in Aldaco et al. 2024; (3) claims on leader-follower puppeteering protocols with friction-compensated gravity models — published with timestamped arXiv. Modern humanoid bimanual data-collection IP faces this anchor at hardware-element specificity.

## Universal Manipulation Interface (UMI) (2024-02-15)

- **id**: `umi-stanford`
- **corpus**: academic
- **creator**: Stanford + TRI + Columbia (Chi, Xu, Pan, Cousineau, Burchfiel, Feng, Tedrake, Song)
- **disclosure**: Chi, Cheng, Xu, Zhenjia, Pan, Chuer, Cousineau, Eric, Burchfiel, Benjamin, Feng, Siyuan, Tedrake, Russ, Song, Shuran. 'Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots.' arXiv:2402.10329, February 15, 2024. Robotics: Science and Systems (RSS) 2024. Stanford University + Toyota Research Institute + Columbia University.
- **ip status**: open-permissive
- **prior art notes**: UMI is the canonical academic disclosure of embodiment-decoupled manipulation data collection via hand-held wrist-camera devices. Anticipates: (1) data collection with a portable hand-held gripper-replica without the robot present — directly relevant to claims on low-cost humanoid data collection (this paradigm is now used by Stanford ALOHA's portable variants, Tesla operator-glove proposals, several other commercial programs); (2) wrist-camera SLAM as the substrate for trajectory reconstruction — relevant to vision-based teleoperation IP; (3) embodiment-matching gripper geometry between collection rig and deployment robot — relevant to claims on cross-embodiment manipulation training. Open-source hardware (3D print files), software, and data under permissive license. Modern humanoid 'in-the-wild data' patent claims face this 2-year-deep anchor with full DIY-buildable defensibility.

## Rainbow Robotics RB-Y1 (2024-03)

- **id**: `rainbow-robotics-rb-y1`
- **corpus**: private
- **creator**: Rainbow Robotics
- **disclosure**: Rainbow Robotics public reveal of RB-Y1, March 2024.
- **ip status**: patented
- **prior art notes**: Rainbow Robotics has direct lineage from KAIST HUBO program; HUBO academic publications constitute prior art for many of their humanoid claims.

## DROID Dataset (2024-03-19)

- **id**: `droid-dataset`
- **corpus**: academic
- **creator**: DROID Consortium (Khazatsky et al., 18 academic + industry institutions)
- **disclosure**: Khazatsky, Alexander et al. 'DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset.' arXiv:2403.12945, March 19, 2024. Robotics: Science and Systems (RSS) 2024. Authors: Khazatsky, A., Pertsch, K., Nair, S., Balakrishna, A., Dasari, S., Karamcheti, S., Nasiriany, S., Srirama, M.K., Chen, L.Y., Ellis, K., Fagan, P.D., Hejna, J., Itkina, M., Lepert, M., Ma, Y.J., Miller, P.T., Wu, J., Belkhale, S., Dass, S., Ha, H., Jain, A., Lee, A., Lee, Y., Memmel, M., Park, S., Radosavovic, I., Wang, K., Zhan, A., Black, K., Chi, C., Hatch, K.B., Lin, S., Lu, J., Mercat, J., Rehman, A., Sanketi, P.R., Sharma, A., Simpson, C., Vuong, Q., Walke, H.R., Wulfe, B., Xiao, T., Yang, J.H., Yavary, A., Zhao, T.Z., Agia, C., Baijal, R., Castro, M.G., Chen, D., Chen, Q., Chung, T., Drake, J., Foster, E.P., Gao, J., Garcia Herrera, D.A., Heo, M., Hsu, K., Hu, J., Jackson, D., Le, C., Li, Y., Lin, K., Lin, R., Ma, Z., Maddukuri, A., Mirchandani, S., Morton, D., Nguyen, T., O'Neill, A., Scalise, R., Seale, D., Son, V., Tian, S., Tran, E., Wang, A.E., Wu, Y., Xie, A., Yang, J., Yin, P., Zhang, Y., Bastani, O., Berseth, G., Bohg, J., Goldberg, K., Gupta, A., Gupta, A., Jayaraman, D., Lim, J.J., Malik, J., Martín-Martín, R., Ramamoorthy, S., Sadigh, D., Song, S., Wu, J., Yip, M.C., Zhu, Y., Kollar, T., Levine, S., Finn, C. (Stanford / Berkeley / TRI / GoogleDeepMind / 18-institution academic consortium).
- **ip status**: open-permissive
- **prior art notes**: DROID is the canonical academic disclosure of large-scale standardized robot manipulation data collection across diverse environments. Anticipates: (1) standardized hardware-stack-based data collection at multi-institutional scale — directly relevant to claims on 'data-flywheel' humanoid programs (Tesla Optimus operator floor, Figure data pipeline, 1X data-collection program); (2) teleoperated demonstration data as the substrate for VLA training — relevant to claims on imitation-learning-based humanoid IP; (3) the open data + open hardware spec combination — establishes prior art for any 'standardized fleet for robot data' patent claim. Released under permissive license (CC-BY 4.0 for data); 76k trajectories, 564 scenes, full hardware spec. Modern humanoid data-collection patent claims face this 2-year-deep anchor.

## Neura 4NE-1 (2024-05)

- **id**: `neura-4ne1`
- **corpus**: private
- **creator**: Neura Robotics
- **disclosure**: Neura Robotics public reveal of 4NE-1, May 2024.
- **ip status**: patented
- **prior art notes**: Neura's cognitive-AI claims overlap with academic VLA literature.

## Kepler K2 (2024-07)

- **id**: `kepler-k2`
- **corpus**: private
- **creator**: Kepler Exploration Robotics
- **disclosure**: Kepler Exploration Robotics public reveal, July 2024.
- **ip status**: patented
- **prior art notes**: Kepler's planetary-reducer actuator claims are anticipated by extensive prior art in industrial robotics planetary-gearing literature.

## Figure 02 (2024-08)

- **id**: `figure-02`
- **corpus**: private
- **creator**: Figure AI
- **disclosure**: Figure AI public reveal of Figure 02, August 2024.
- **ip status**: patented
- **prior art notes**: Figure 02 actuator and hand claims are heavily anticipated by Honda P-series, Robonaut 2, Shadow Hand, and iCub work. The 16-DoF hand is in the same design space as Robonaut 2's 12-DoF and Sanctuary's 21-DoF.

## Robot Era STAR1 (2024-10)

- **id**: `robot-era-star1`
- **corpus**: private
- **creator**: Robot Era
- **disclosure**: Robot Era public reveal of STAR1, October 2024.
- **ip status**: patented
- **prior art notes**: Bipedal running speed claims anticipated by Cassie's Guinness record work.

## XPeng Iron (2024-11)

- **id**: `xpeng-iron`
- **corpus**: private
- **creator**: XPeng Motors (Robotics division)
- **disclosure**: XPeng AeroHT and XPeng Robotics reveal, November 2024.
- **ip status**: patented
- **prior art notes**: XPeng's leveraging of automotive ML stack for humanoid perception is heavily anticipated by Tesla Optimus's same approach (which is itself anticipated by academic vision-based humanoid work).
