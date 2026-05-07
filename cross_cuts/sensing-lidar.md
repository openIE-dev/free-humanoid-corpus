---
title: sensing-lidar
parent: Cross-cuts
layout: default
---

# Cross-cut: `sensing-lidar`

**15 corpus entries disclose this subsystem.**

Earliest disclosure: 2004

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## HUBO (2004)

- **id**: `hubo`
- **corpus**: academic
- **creator**: KAIST, Hubo Lab (Jun-Ho Oh)
- **disclosure**: Park, Ill-Woo et al. 'Mechanical Design of Humanoid Robot Platform KHR-3 (HUBO).' IEEE-RAS Humanoids 2005.
- **ip status**: open-permissive
- **prior art notes**: DRC-Hubo's 2015 win demonstrated transformer-style transitioning between bipedal and wheeled-knee modes for navigating both stairs and flat ground. Anticipates: hybrid locomotion modes in humanoids.

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

## NASA Valkyrie (2013)

- **id**: `nasa-valkyrie`
- **corpus**: academic
- **creator**: NASA Johnson Space Center, in collaboration with University of Texas at Austin and others
- **disclosure**: NASA Johnson Space Center, DARPA Robotics Challenge entry, 2013.
- **ip status**: open-permissive
- **prior art notes**: NASA Valkyrie's series-elastic actuator implementations and the IHMC-derived whole-body control work are foundational prior art. The robot was distributed to multiple universities and produced extensive open publications.

## Atlas (2013-07)

- **id**: `atlas-boston-dynamics`
- **corpus**: private
- **creator**: Boston Dynamics
- **disclosure**: DARPA press release, July 2013, announcing Atlas as DRC platform.
- **ip status**: patented
- **prior art notes**: Boston Dynamics' patents are among the most-cited in the humanoid space and also among the most likely to be challenged on 102/103 grounds given the long academic prior art chain (Honda, AIST, KAIST, MIT). Worth dedicated patent-by-patent analysis.

## Pepper (2014-06)

- **id**: `pepper-softbank`
- **corpus**: private
- **creator**: SoftBank Robotics (formerly Aldebaran)
- **disclosure**: SoftBank Robotics public reveal of Pepper, June 2014.
- **ip status**: patented
- **prior art notes**: Pepper is foundational prior art for wheeled-base humanoid social robots. The omnidirectional wheeled base design has been widely cited.

## ANYmal (2016)

- **id**: `anymal`
- **corpus**: private
- **creator**: ANYbotics, ETH Zurich Robotic Systems Lab
- **disclosure**: Hutter, M. et al. 'ANYmal — a highly mobile and dynamic quadrupedal robot.' IROS 2016.
- **ip status**: patented
- **prior art notes**: ANYbotics SEA design heavily anticipated by NASA Valkyrie and Robonaut SEA work. ETH RSL academic publications provide open prior art for many control claims.

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

## Diligent Moxi (2019-09)

- **id**: `diligent-moxi`
- **corpus**: private
- **creator**: Diligent Robotics
- **disclosure**: Diligent Robotics public reveal of Moxi, September 2019.
- **ip status**: patented
- **prior art notes**: Diligent's claims around mobile manipulation in healthcare environments face extensive prior art from PR2, HSR, and academic mobile manipulation literature.

## ANYmal-D industrial quadruped (ETH RSL / ANYbotics) (2022-09)

- **id**: `anymal-d-eth-rsl-2022`
- **corpus**: academic
- **creator**: ANYbotics AG / ETH Zürich Robotic Systems Lab (Marco Hutter)
- **disclosure**: ANYbotics product disclosure ANYmal D, September 2022; technical updates in Miki, Takahiro et al. 'Learning robust perceptive locomotion for quadrupedal robots in the wild.' Science Robotics 7(62), 2022; Hoeller, David et al. 'ANYmal Parkour: Learning agile navigation for quadrupedal robots.' Science Robotics 9(88), 2024.
- **ip status**: public-domain
- **prior art notes**: ANYmal-D is the production-deployed industrial quadruped of the 2022-2024 period and the platform for the headline RSL/ANYbotics RL-locomotion papers in Science Robotics. It anticipates with full specificity: (1) claims on perceptive-locomotion RL policies trained in simulation and transferred to outdoor industrial terrain — Miki Sci.Rob. 2022 publishes the teacher-student distillation pipeline running on this hardware; (2) claims on agile parkour-class learned locomotion — Hoeller Sci.Rob. 2024 publishes the policy on ANYmal-D; (3) claims on series-elastic torque-controlled quadruped joints in IP67 industrial enclosures — ANYdrive disclosed at IROS 2018 with hardware refresh on D-variant. Modern legged-robot IP claims face this timestamped industrial-deployment anchor.

## Unitree H1 (2023-08)

- **id**: `unitree-h1`
- **corpus**: private
- **creator**: Unitree Robotics
- **disclosure**: Unitree Robotics public reveal, August 2023.
- **ip status**: patented
- **prior art notes**: Unitree's actuator IP largely derives from quadruped work (Go1, Aliengo) which is itself heavily anticipated by MIT Mini Cheetah QDD lineage.
