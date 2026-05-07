---
title: software-ros1
parent: Cross-cuts
layout: default
---

# Cross-cut: `software-ros1`

**17 corpus entries disclose this subsystem.**

Earliest disclosure: 2002

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## HRP-2 (2002)

- **id**: `hrp-2`
- **corpus**: academic
- **creator**: AIST (National Institute of Advanced Industrial Science and Technology), Kawada Industries
- **disclosure**: Kaneko, K. et al. 'Design of prototype humanoid robotics platform for HRP.' IROS 2002.
- **ip status**: open-permissive
- **prior art notes**: OpenHRP is itself foundational prior art for open robotics simulation frameworks. HRP-2 was among the first humanoids to publicly demonstrate falling-and-recovering behaviors.

## NAO (2006)

- **id**: `nao`
- **corpus**: private
- **creator**: Aldebaran Robotics (later SoftBank Robotics, then UBT)
- **disclosure**: Gouaillier, D. et al. 'Mechatronic design of NAO humanoid.' ICRA 2009.
- **ip status**: patented
- **prior art notes**: NAO's mechatronic design publication is well-cited prior art. The platform's wide academic distribution since 2006 makes its design choices broadly disclosed.

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

## Pepper (2014-06)

- **id**: `pepper-softbank`
- **corpus**: private
- **creator**: SoftBank Robotics (formerly Aldebaran)
- **disclosure**: SoftBank Robotics public reveal of Pepper, June 2014.
- **ip status**: patented
- **prior art notes**: Pepper is foundational prior art for wheeled-base humanoid social robots. The omnidirectional wheeled base design has been widely cited.

## Levine Guided Policy Search end-to-end manipulation on PR2/BRETT (2015-04)

- **id**: `levine-gps-pr2-2016`
- **corpus**: academic
- **creator**: Sergey Levine, Chelsea Finn, Trevor Darrell, Pieter Abbeel, UC Berkeley
- **disclosure**: Levine, Sergey, Finn, Chelsea, Darrell, Trevor, Abbeel, Pieter. 'End-to-End Training of Deep Visuomotor Policies.' Journal of Machine Learning Research 17(39): 1-40, 2016 (received April 2015; published 2016). Earlier: Levine, S., Wagener, N., Abbeel, P. 'Learning Contact-Rich Manipulation Skills with Guided Policy Search.' ICRA 2015.
- **ip status**: public-domain
- **prior art notes**: Levine et al. 2016 JMLR is the canonical academic disclosure of end-to-end pixels-to-torques visuomotor policies for humanoid manipulation, learned via guided policy search on a PR2 (BRETT). Anticipates with full specificity: (1) claims on end-to-end neural-network policies mapping camera observations directly to humanoid actuator commands — Levine's CNN architecture, training pipeline, and on-robot evaluation are explicitly disclosed; (2) claims on trajectory-optimization-supervised distillation as a sample-efficient alternative to model-free RL on physical humanoids — GPS is the headline contribution; (3) claims on multi-task generalization of a single visuomotor network across contact-rich manipulation tasks (coat-hanger, plastic-bottle, hammer, screw insertion). >3500 citations; JMLR open access; arXiv preprint 2015. The lineage runs directly forward to RT-1, RT-2, OpenVLA, and modern humanoid VLA systems. Modern humanoid end-to-end visuomotor IP filings face this 11-year-deep anchor with full architecture disclosure.

## Cassie (2017)

- **id**: `cassie-osu`
- **corpus**: academic
- **creator**: Oregon State University, Dynamic Robotics Laboratory (Jonathan Hurst)
- **disclosure**: Agility Robotics / Oregon State University Cassie release, 2017.
- **ip status**: patented
- **prior art notes**: Cassie and the broader Hurst lab work on reduced-order locomotion models is significant prior art for bipedal control claims industry-wide.

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

## Ghost Robotics Vision 60 (2018)

- **id**: `ghost-robotics-vision-60`
- **corpus**: private
- **creator**: Ghost Robotics
- **disclosure**: Ghost Robotics Vision 60 release, 2018.
- **ip status**: patented
- **prior art notes**: Ghost Robotics derives from Penn's Kod*lab academic quadruped work. The legged-robot patents face the same MIT Cheetah / ANYmal / Penn Kod*lab prior art chain as other quadrupeds.

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

## Diligent Moxi (2019-09)

- **id**: `diligent-moxi`
- **corpus**: private
- **creator**: Diligent Robotics
- **disclosure**: Diligent Robotics public reveal of Moxi, September 2019.
- **ip status**: patented
- **prior art notes**: Diligent's claims around mobile manipulation in healthcare environments face extensive prior art from PR2, HSR, and academic mobile manipulation literature.
