---
title: actuator-electric-quasi-direct-drive
parent: Cross-cuts
layout: default
---

# Cross-cut: `actuator-electric-quasi-direct-drive`

**16 corpus entries disclose this subsystem.**

Earliest disclosure: 2014

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## MIT Cheetah 2 (2014)

- **id**: `mit-cheetah-2`
- **corpus**: academic
- **creator**: MIT Biomimetic Robotics Lab (Sangbae Kim)
- **disclosure**: Park, H.-W. et al. 'High-speed bounding with the MIT Cheetah 2: Control design and experiments.' International Journal of Robotics Research 36(2), 2017. Earlier ICRA disclosure 2014.
- **ip status**: open-permissive
- **prior art notes**: MIT Cheetah 2 establishes the QDD actuator topology in a working high-speed legged robot. The Wensing 2017 T-RO paper 'Proprioceptive actuator design in the MIT Cheetah' is the foundational actuator design disclosure.

## Black Mirror 'Metalhead' autonomous quadruped killer (2017-12)

- **id**: `black-mirror-metalhead-2017`
- **corpus**: fictional
- **creator**: Charlie Brooker (writer), David Slade (director), House of Tomorrow / Netflix
- **disclosure**: Black Mirror, Series 4, Episode 5, 'Metalhead.' Written by Charlie Brooker; directed by David Slade; released on Netflix 29 December 2017.
- **ip status**: public-domain
- **prior art notes**: 'Metalhead' is the canonical 2017 mass-media anchor for autonomous quadruped lethal-defense robots and was directly modeled on the Boston Dynamics SpotMini reveal. It anticipates with full specificity: (1) claims on quadruped robots equipped with weapon payloads operating in fully-autonomous lethal-engagement mode — the episode dramatizes exactly this throughout 41 minutes; (2) claims on shrapnel-tag persistent-tracker payloads that mark a target for prolonged pursuit — this is the headline mechanism of the second act; (3) claims on SpotMini-class compact electric quadruped morphology with integrated manipulator arm — the visual design and Brooker's published commentary explicitly cite Boston Dynamics inspiration. Released on Netflix with timestamped 29 December 2017 distribution to ~109 million subscribers.

## MIT Cheetah 3 (2018)

- **id**: `mit-cheetah-3`
- **corpus**: academic
- **creator**: MIT Biomimetic Robotics Lab (Sangbae Kim)
- **disclosure**: Bledt, G. et al. 'MIT Cheetah 3: Design and Control of a Robust, Dynamic Quadruped Robot.' IROS 2018.
- **ip status**: open-permissive
- **prior art notes**: Cheetah 3 establishes blind robust legged locomotion using only proprioceptive sensing — a significant prior art point against later vision-dependent legged-robot claims.

## Tan et al. Quadruped Sim-to-Real (2018-04-28)

- **id**: `tan-quadruped-sim2real`
- **corpus**: academic
- **creator**: Google Brain + Google Robotics (Tan, Zhang, Coumans, Iscen, Bai, Hafner, Bohez, Vanhoucke)
- **disclosure**: Tan, Jie, Zhang, Tingnan, Coumans, Erwin, Iscen, Atil, Bai, Yunfei, Hafner, Danijar, Bohez, Steven, Vanhoucke, Vincent. 'Sim-to-Real: Learning Agile Locomotion For Quadruped Robots.' arXiv:1804.10332, April 28, 2018. Robotics: Science and Systems (RSS) 2018.
- **ip status**: open-permissive
- **prior art notes**: Tan et al. 2018 is one of the earliest academic disclosures of practical sim-to-real RL for quadrupedal locomotion, predating Hwangbo 2019 by ~9 months and establishing the system-identification + domain-randomization paradigm for legged sim-to-real. Anticipates: (1) PPO-based RL for legged locomotion with subsequent zero-shot hardware transfer — relevant to RL-locomotion-policy patents (Boston Dynamics, Unitree, every commercial quadruped); (2) explicit actuator-latency modeling as a sim-to-real bridge — relevant to claims on real-time sim-to-real techniques; (3) the quasi-direct-drive Minitaur platform combined with sim-to-real — relevant to QDD-actuator+RL humanoid claims. Open-source code via PyBullet repository. RSS 2018 publication. Modern legged sim-to-real claims face an 8-year-deep anchor.

## MIT Mini Cheetah (2019)

- **id**: `mini-cheetah`
- **corpus**: academic
- **creator**: MIT Biomimetic Robotics Lab (Sangbae Kim)
- **disclosure**: Katz, B. et al. 'Mini Cheetah: A Platform for Pushing the Limits of Dynamic Quadruped Control.' ICRA 2019.
- **ip status**: open-permissive
- **prior art notes**: The QDD actuator topology (low gear ratio, high-torque BLDC, transparent backdrivability) is a foundational contribution. Establishes the design space for affordable dynamic legged robots.

## Caltech CAST Hank bipedal platform (2019-05)

- **id**: `caltech-hank-cast-2019`
- **corpus**: academic
- **creator**: Aaron D. Ames and the Caltech AMBER Lab / CAST
- **disclosure**: Reher, Jenna and Ames, Aaron D. 'Inverse Dynamics Control of Compliant Hybrid Zero Dynamic Walking.' ICRA 2021; Csomay-Shanklin, Noel et al. 'Episodic Learning for Safe Bipedal Locomotion with Control Barrier Functions and Projection-to-State Safety.' L4DC 2021; CAST (Center for Autonomous Systems and Technologies) Caltech Hank reveal 2019.
- **ip status**: public-domain
- **prior art notes**: Hank is the Caltech CAST flagship humanoid biped of the late-2010s and is the canonical platform for HZD + CBF formal-method bipedal locomotion publications by the Ames group. It anticipates with full specificity: (1) claims on hybrid-zero-dynamics low-dimensional gait manifolds for humanoids — Reher-Ames ICRA 2021 publishes the formal HZD+ID-CLF-QP stack on Hank; (2) claims on control-barrier-function safety supervision for legged locomotion — Csomay-Shanklin L4DC 2021 publishes episodic CBF learning on Hank; (3) claims on quasi-direct-drive proprioceptive humanoid biped hardware — Hank's actuator topology predates and parallels Tesla Optimus and Apptronik Apollo public claims. All Hank publications are open-access with timestamped arXiv.

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

## Unitree H1 (2023-08)

- **id**: `unitree-h1`
- **corpus**: private
- **creator**: Unitree Robotics
- **disclosure**: Unitree Robotics public reveal, August 2023.
- **ip status**: patented
- **prior art notes**: Unitree's actuator IP largely derives from quadruped work (Go1, Aliengo) which is itself heavily anticipated by MIT Mini Cheetah QDD lineage.

## AgiBot A1 (2023-08)

- **id**: `agibot-a1`
- **corpus**: private
- **creator**: AgiBot (Shanghai Zhiyuan New Technology Co.)
- **disclosure**: AgiBot (Shanghai Zhiyuan New Technology) public reveal, August 2023.
- **ip status**: patented
- **prior art notes**: AgiBot's actuator IP heavily anticipated by Honda P-series harmonic drive work and MIT Cheetah QDD lineage. Chinese-language patent filings should be enumerated in strengthening pass.

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

## Berkeley Humanoid (2024)

- **id**: `berkeley-humanoid`
- **corpus**: academic
- **creator**: UC Berkeley, Hybrid Robotics Lab
- **disclosure**: Liao, Q. et al. 'Berkeley Humanoid: A Research Platform for Learning-based Control.' arXiv 2024.
- **ip status**: open-permissive
- **prior art notes**: Berkeley quasi-direct-drive lineage (predates the humanoid; comes from the Mini Cheetah / leg work) anticipates many actuator architecture claims.

## Unitree G1 (2024-05)

- **id**: `unitree-g1`
- **corpus**: private
- **creator**: Unitree Robotics
- **disclosure**: Unitree Robotics G1 reveal, May 2024.
- **ip status**: patented
- **prior art notes**: G1's actuator IP largely anticipated by MIT Mini Cheetah QDD work and Honda harmonic drive prior art. The aggressive pricing represents the commodity-humanoid trajectory more than novel IP.

## EngineAI PM01 (2024-12)

- **id**: `engineai-pm01`
- **corpus**: private
- **creator**: EngineAI
- **disclosure**: EngineAI public reveal of PM01, December 2024.
- **ip status**: patented
- **prior art notes**: EngineAI QDD actuation anticipated by MIT Cheetah lineage.

## Unitree H2 (2025-10)

- **id**: `unitree-h2`
- **corpus**: private
- **creator**: Unitree Robotics
- **disclosure**: Unitree Robotics H2 reveal, October 2025.
- **ip status**: patented
- **prior art notes**: H2 builds on H1 architecture; same prior art chain back through Mini Cheetah.
