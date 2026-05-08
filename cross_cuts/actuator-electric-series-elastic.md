---
title: actuator-electric-series-elastic
parent: Cross-cuts
layout: default
---

# Cross-cut: `actuator-electric-series-elastic`

**18 corpus entries disclose this subsystem.**

Earliest disclosure: 1995-08

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Pratt-Williamson Series Elastic Actuator (1995-08)

- **id**: `pratt-williamson-sea`
- **corpus**: academic
- **creator**: Gill A. Pratt and Matthew M. Williamson, MIT Leg Laboratory and MIT AI Lab
- **disclosure**: Pratt, Gill A. and Williamson, Matthew M. 'Series elastic actuators.' IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Pittsburgh PA, August 5-9, 1995: 399-406.
- **ip status**: public-domain
- **prior art notes**: The Pratt-Williamson 1995 paper is the foundational academic disclosure of series-elastic actuators (SEA) — the dominant compliant-actuator architecture in legged and humanoid robotics. Anticipates with full specificity: (1) intentional series mechanical spring as the force-sensing element — directly relevant to claims on compliant humanoid actuators (Cassie, Digit, Apollo SEA derivatives); (2) spring-deflection-based force control without strain gauges — relevant to claims on encoder-only force feedback; (3) the bandwidth/stiffness tradeoff disclosure — anticipates SEA-design IP. Pratt's later commercial work (Yobotics, then Boston Dynamics' Atlas SEA) is grounded in this paper. Heavily cited (>3000 citations); SEA is now a textbook concept. 31-year-deep 102 anchor against any 'compliant humanoid actuator' patent.

## Pratt Virtual Model Control (2001-04)

- **id**: `pratt-virtual-model-control`
- **corpus**: academic
- **creator**: Jerry Pratt, Chee-Meng Chew, Ann Torres, Peter Dilworth, Gill Pratt; MIT Leg Laboratory
- **disclosure**: Pratt, Jerry, Chew, Chee-Meng, Torres, Ann, Dilworth, Peter, Pratt, Gill. 'Virtual model control: An intuitive approach for bipedal locomotion.' International Journal of Robotics Research 20(2): 129-143, February 2001. Earlier: Pratt, J.E. and Pratt, G.A. 'Intuitive control of a planar bipedal walking robot.' IEEE ICRA 1998: 2014-2021.
- **ip status**: public-domain
- **prior art notes**: Pratt's Virtual Model Control is a canonical alternative paradigm to ZMP for bipedal control, preserving compliance and intuitive task-space specification. Anticipates: (1) virtual-element-based humanoid torque control — directly relevant to claims on intuitive task-space bipedal controllers; (2) Jacobian-projected virtual force generation — relevant to whole-body humanoid IP that uses 'virtual' or 'imagined' references (every model-based controller for SEA-equipped humanoids descends from this); (3) integration with series-elastic compliance — relevant to compliant-humanoid claims. Pratt's 2000 PhD thesis ('Exploiting natural dynamics in the control of a planar bipedal walking robot,' MIT) extends the framework. Jerry Pratt later led IHMC's humanoid work (DRC Atlas, NASA Valkyrie controller). >1000 citations. 25-year-deep anchor against intuitive-bipedal-control patents.

## Variable Stiffness Actuator (Tonietti VSA) (2005-04)

- **id**: `tonietti-vsa-pisa-iit-2005`
- **corpus**: academic
- **creator**: Pisa University + IIT (Italian Institute of Technology); Giovanni Tonietti, Riccardo Schiavi, Antonio Bicchi
- **disclosure**: Tonietti, G., Schiavi, R., Bicchi, A. 'Design and Control of a Variable Stiffness Actuator for Safe and Fast Physical Human/Robot Interaction'. ICRA 2005. Pisa-IIT (later: IIT-Pisa joint lab; antecedent of Pisa-IIT SoftHand corpus entry).
- **ip status**: public-domain
- **prior art notes**: The Pisa-IIT Tonietti VSA (ICRA 2005) is the canonical academic variable-stiffness actuator. 20-year-deep public-domain prior art for: mechanically-adjustable joint compliance, two-motor co-control of position + stiffness. Architectural cousin of Pratt-Williamson SEA (corpus entry, 1995, fixed compliance). Direct ancestor of: DLR Hand-Arm System variable-impedance joints (corpus entry dlr-hand-arm-system-2011); EPFL spring-driven exoskeletons; modern compliant-actuator commercial products. Direct shielding for any commercial humanoid claim on real-time-adjustable compliance or variable-stiffness joint control.

## BiOM / iWalk / BionX → Empower Ankle (Hugh Herr) (2007-01)

- **id**: `biom-empower-herr-mit-2007`
- **corpus**: private
- **creator**: iWalk Inc. → BionX → Otto Bock Empower; Hugh Herr (MIT Media Lab Biomechatronics)
- **disclosure**: iWalk Inc. (Bedford, MA, USA; founded 2007 by Hugh Herr, MIT Media Lab Biomechatronics). BiOM commercial launch 2011. Renamed BionX 2014. Acquired by Otto Bock HealthCare 2017; rebranded as Otto Bock Empower.
- **ip status**: trade-secret
- **prior art notes**: BiOM / iWalk / Empower Ankle (Hugh Herr MIT Media Lab + iWalk 2007 → BiOM 2011 → BionX 2014 → Otto Bock Empower 2017) is the first powered ankle-foot prosthesis with positive net work. 18-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from powered ankle-foot prostheses or active gait push-off actuation. Lineage descends from Pratt-Williamson series-elastic actuator (corpus pratt-williamson-sea).

## MIT Domo + Meka Robotics (Aaron Edsinger) (2007-07)

- **id**: `edsinger-meka-mit-domo-2008`
- **corpus**: academic
- **creator**: MIT CSAIL Brooks group + Meka Robotics; Aaron Edsinger + Jeff Weber
- **disclosure**: Edsinger, A. PhD thesis 'Robot Manipulation in Human Environments' MIT 2007. Domo humanoid demonstrator in Brooks group MIT CSAIL. Meka Robotics commercial spinout founded 2006 by Edsinger + Jeff Weber. Acquired by Google December 2013 (one of 8 robotics startups acquired by Google that month). Lineage continues through Hello Robot (Edsinger co-founded with Charles Kemp 2017).
- **ip status**: public-domain
- **prior art notes**: Edsinger's MIT Domo + Meka Robotics (MIT 2007 + Meka 2006-2013) is the foundational compliant-humanoid academic + commercial lineage. 18-year-deep public-domain prior art. **Direct architectural ancestor of Hello Robot Stretch (round-17)** — Edsinger founded Hello Robot 2017 with Charles Kemp. Series-elastic actuator commercial deployment via Meka predates Pratt-Williamson commercial-deployment narrative. Direct shielding for any commercial humanoid claim deriving from compliant-actuator humanoids or Edsinger lineage.

## PR2 (2010)

- **id**: `pr2`
- **corpus**: open
- **creator**: Willow Garage
- **disclosure**: Willow Garage. PR2 platform release, 2010.
- **ip status**: open-permissive
- **prior art notes**: PR2 was the platform around which ROS was originally built. Its hardware is significant prior art for omnidirectional wheeled mobile manipulation. ROS itself is even more significant prior art for robotics middleware.

## Robonaut 2 (2010-02)

- **id**: `robonaut-2`
- **corpus**: academic
- **creator**: NASA Johnson Space Center, in partnership with General Motors
- **disclosure**: Diftler, M.A. et al. 'Robonaut 2 — The First Humanoid Robot in Space.' ICRA 2011.
- **ip status**: patented
- **prior art notes**: Robonaut 2's hand design, with 12 DoF per hand and tendon routing through the forearm, is foundational prior art for high-DoF tendon-driven humanoid hands. The NASA-GM patent portfolio has been extensively cited.

## NASA Valkyrie (2013)

- **id**: `nasa-valkyrie`
- **corpus**: academic
- **creator**: NASA Johnson Space Center, in collaboration with University of Texas at Austin and others
- **disclosure**: NASA Johnson Space Center, DARPA Robotics Challenge entry, 2013.
- **ip status**: open-permissive
- **prior art notes**: NASA Valkyrie's series-elastic actuator implementations and the IHMC-derived whole-body control work are foundational prior art. The robot was distributed to multiple universities and produced extensive open publications.

## ATRIAS (2013)

- **id**: `atrias`
- **corpus**: academic
- **creator**: Oregon State University, Dynamic Robotics Laboratory (Jonathan Hurst)
- **disclosure**: Hubicki, C. et al. 'ATRIAS: Design and validation of a tether-free 3D-capable spring-mass bipedal robot.' International Journal of Robotics Research 35(12), 2016.
- **ip status**: open-permissive
- **prior art notes**: ATRIAS is foundational prior art for spring-mass bipedal locomotion. The SLIP-based reduced-order control approach has become a dominant paradigm in dynamic bipedal walking, anticipating many subsequent commercial control claims.

## IIT WALK-MAN + R1 personal humanoid (Italy) (2015-06)

- **id**: `iit-walk-man-r1-italy-2015`
- **corpus**: academic
- **creator**: Istituto Italiano di Tecnologia (IIT, Genoa); Nikos Tsagarakis + Darwin Caldwell groups
- **disclosure**: Istituto Italiano di Tecnologia (IIT), Genoa, Italy. WALK-MAN humanoid reveal June 2015 for DARPA Robotics Challenge competition (5th place). Subsequent: COMAN+ (Compliant Humanoid), **R1 personal humanoid** (2017-2020) targeted at home + service applications. iit.it. Tsagarakis + Caldwell + Bicchi groups.
- **ip status**: public-domain
- **prior art notes**: IIT WALK-MAN + R1 are the canonical Italian academic humanoid platforms (IIT Genoa, 2015-2020+). 10-year-deep public-domain prior art for: SEA + VSA-actuated compliant whole-body humanoid, personal humanoid form factor (130cm/50kg/sub-€30k), DARPA-class disaster-response humanoid. Direct architectural descendant of: Pratt-Williamson SEA (1995, in corpus), Tonietti VSA (2005, round-21), Pisa-IIT SoftHand (in corpus). Together with iCub (corpus entry), establishes the Italian academic humanoid + compliant-actuator prior-art chain. Brings Italian depth from 5 to 6 entries.

## ANYmal (2016)

- **id**: `anymal`
- **corpus**: private
- **creator**: ANYbotics, ETH Zurich Robotic Systems Lab
- **disclosure**: Hutter, M. et al. 'ANYmal — a highly mobile and dynamic quadrupedal robot.' IROS 2016.
- **ip status**: patented
- **prior art notes**: ANYbotics SEA design heavily anticipated by NASA Valkyrie and Robonaut SEA work. ETH RSL academic publications provide open prior art for many control claims.

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

## Hwangbo ANYmal Sim-to-Real Locomotion (2019-01-16)

- **id**: `hwangbo-anymal-sim2real`
- **corpus**: academic
- **creator**: Hwangbo, Lee, Dosovitskiy, Bellicoso, Tsounis, Koltun, Hutter; ETH Zürich Robotic Systems Lab + Intel Intelligent Systems Lab
- **disclosure**: Hwangbo, Jemin, Lee, Joonho, Dosovitskiy, Alexey, Bellicoso, Dario, Tsounis, Vassilios, Koltun, Vladlen, Hutter, Marco. 'Learning agile and dynamic motor skills for legged robots.' Science Robotics 4(26): eaau5872, January 16, 2019.
- **ip status**: open-permissive
- **prior art notes**: Hwangbo et al. 2019 is the foundational academic disclosure of practical RL-based sim-to-real legged locomotion. Anticipates with full architectural specificity: (1) actuator-network-based high-fidelity simulation (neural network as drop-in actuator dynamics) — directly relevant to claims on humanoid sim-to-real pipelines (Berkeley Humanoid, Apptronik Apollo, Tesla Optimus all use derivatives); (2) zero-shot policy transfer from RL-in-sim to legged hardware — anticipates virtually every modern legged-RL-policy patent; (3) recovery from arbitrary falls via single learned policy — relevant to fall-recovery IP for humanoids. Published in Science Robotics; one of the most-cited robotics RL papers (>2000 citations). Modern humanoid sim-to-real claims face this 7-year-deep anchor with full peer-review defensibility.

## Caltech CAST Hank bipedal platform (2019-05)

- **id**: `caltech-hank-cast-2019`
- **corpus**: academic
- **creator**: Aaron D. Ames and the Caltech AMBER Lab / CAST
- **disclosure**: Reher, Jenna and Ames, Aaron D. 'Inverse Dynamics Control of Compliant Hybrid Zero Dynamic Walking.' ICRA 2021; Csomay-Shanklin, Noel et al. 'Episodic Learning for Safe Bipedal Locomotion with Control Barrier Functions and Projection-to-State Safety.' L4DC 2021; CAST (Center for Autonomous Systems and Technologies) Caltech Hank reveal 2019.
- **ip status**: public-domain
- **prior art notes**: Hank is the Caltech CAST flagship humanoid biped of the late-2010s and is the canonical platform for HZD + CBF formal-method bipedal locomotion publications by the Ames group. It anticipates with full specificity: (1) claims on hybrid-zero-dynamics low-dimensional gait manifolds for humanoids — Reher-Ames ICRA 2021 publishes the formal HZD+ID-CLF-QP stack on Hank; (2) claims on control-barrier-function safety supervision for legged locomotion — Csomay-Shanklin L4DC 2021 publishes episodic CBF learning on Hank; (3) claims on quasi-direct-drive proprioceptive humanoid biped hardware — Hank's actuator topology predates and parallels Tesla Optimus and Apptronik Apollo public claims. All Hank publications are open-access with timestamped arXiv.

## ANYmal-D industrial quadruped (ETH RSL / ANYbotics) (2022-09)

- **id**: `anymal-d-eth-rsl-2022`
- **corpus**: academic
- **creator**: ANYbotics AG / ETH Zürich Robotic Systems Lab (Marco Hutter)
- **disclosure**: ANYbotics product disclosure ANYmal D, September 2022; technical updates in Miki, Takahiro et al. 'Learning robust perceptive locomotion for quadrupedal robots in the wild.' Science Robotics 7(62), 2022; Hoeller, David et al. 'ANYmal Parkour: Learning agile navigation for quadrupedal robots.' Science Robotics 9(88), 2024.
- **ip status**: public-domain
- **prior art notes**: ANYmal-D is the production-deployed industrial quadruped of the 2022-2024 period and the platform for the headline RSL/ANYbotics RL-locomotion papers in Science Robotics. It anticipates with full specificity: (1) claims on perceptive-locomotion RL policies trained in simulation and transferred to outdoor industrial terrain — Miki Sci.Rob. 2022 publishes the teacher-student distillation pipeline running on this hardware; (2) claims on agile parkour-class learned locomotion — Hoeller Sci.Rob. 2024 publishes the policy on ANYmal-D; (3) claims on series-elastic torque-controlled quadruped joints in IP67 industrial enclosures — ANYdrive disclosed at IROS 2018 with hardware refresh on D-variant. Modern legged-robot IP claims face this timestamped industrial-deployment anchor.

## Apptronik Apollo academic and technical disclosures (2023-2024) (2023-08)

- **id**: `apptronik-apollo-publications-2024`
- **corpus**: academic
- **creator**: Apptronik Inc. (Jeff Cardenas, Nick Paine, Luis Sentis lineage from UT Austin Human-Centered Robotics Lab)
- **disclosure**: Apptronik. 'Apollo: A Commercial Humanoid Robot for the Workforce.' Apptronik whitepaper, August 2023; Knabe, Coleman et al. 'Designing a Force-Controlled Linear Series Elastic Actuator.' (NASA Valkyrie / Apptronik lineage) IROS 2014; Apptronik-NASA JSC disclosures 2023-2024 including SAFFiR/Valkyrie genealogy white-papers.
- **ip status**: public-domain
- **prior art notes**: This entry isolates the academic-publication and technical-disclosure trail behind Apptronik Apollo (distinct from the Apollo product seed entry). It anticipates with full specificity: (1) claims on humanoid SEA actuator topology — Knabe-Paine et al. IROS 2014 publishes the linear-SEA design that lineally seeds Apollo; (2) claims on whole-body operational-space control for force-interactive humanoid manipulation — Sentis-Khatib WBOSC 2007/2010 papers (UT Austin lineage carried into Apptronik) are foundational and timestamped; (3) claims on hot-swap-battery torso integration with regenerative power electronics on humanoid platforms — Apollo whitepaper August 2023 discloses publicly. Modern humanoid commercial-platform IP claims to SEA torque control or WBOSC face this Apptronik publication trail at element-by-element specificity.
