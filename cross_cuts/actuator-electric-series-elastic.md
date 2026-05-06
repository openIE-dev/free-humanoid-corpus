---
title: actuator-electric-series-elastic
parent: Cross-cuts
layout: default
---

# Cross-cut: `actuator-electric-series-elastic`

**11 corpus entries disclose this subsystem.**

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
