---
title: control-sim-to-real
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-sim-to-real`

**14 corpus entries disclose this subsystem.**

Earliest disclosure: 2014-12-11

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Talos Principle Robots (2014-12-11)

- **id**: `talos-principle-robots`
- **corpus**: fictional
- **creator**: Croteam (game); Tom Jubert and Jonas Kyratzes (story)
- **disclosure**: Croteam. The Talos Principle. Devolver Digital, December 11, 2014. Story by Tom Jubert and Jonas Kyratzes.
- **ip status**: fictional
- **prior art notes**: The Talos Principle is one of the most engineering-philosophical fictional disclosures of *sim-to-real training as the explicit deployment paradigm* for humanoid policies. Anticipates: (1) deliberately-constructed simulation training environment as the policy-acquisition substrate — directly relevant to modern sim-to-real humanoid IP (every commercial humanoid uses some variant of this paradigm); (2) curriculum design for progressive task difficulty — relevant to curriculum-learning humanoid claims; (3) ethical/philosophical reasoning as part of the training curriculum — relevant to alignment-supervision humanoid IP. The 2014 release predates much of the academic literature on sim-to-real humanoid policies. Continuously available since 2014.

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

## Tan et al. Quadruped Sim-to-Real (2018-04-28)

- **id**: `tan-quadruped-sim2real`
- **corpus**: academic
- **creator**: Google Brain + Google Robotics (Tan, Zhang, Coumans, Iscen, Bai, Hafner, Bohez, Vanhoucke)
- **disclosure**: Tan, Jie, Zhang, Tingnan, Coumans, Erwin, Iscen, Atil, Bai, Yunfei, Hafner, Danijar, Bohez, Steven, Vanhoucke, Vincent. 'Sim-to-Real: Learning Agile Locomotion For Quadruped Robots.' arXiv:1804.10332, April 28, 2018. Robotics: Science and Systems (RSS) 2018.
- **ip status**: open-permissive
- **prior art notes**: Tan et al. 2018 is one of the earliest academic disclosures of practical sim-to-real RL for quadrupedal locomotion, predating Hwangbo 2019 by ~9 months and establishing the system-identification + domain-randomization paradigm for legged sim-to-real. Anticipates: (1) PPO-based RL for legged locomotion with subsequent zero-shot hardware transfer — relevant to RL-locomotion-policy patents (Boston Dynamics, Unitree, every commercial quadruped); (2) explicit actuator-latency modeling as a sim-to-real bridge — relevant to claims on real-time sim-to-real techniques; (3) the quasi-direct-drive Minitaur platform combined with sim-to-real — relevant to QDD-actuator+RL humanoid claims. Open-source code via PyBullet repository. RSS 2018 publication. Modern legged sim-to-real claims face an 8-year-deep anchor.

## OpenAI Dactyl (2018-07-30)

- **id**: `openai-dactyl`
- **corpus**: academic
- **creator**: Andrychowicz, Akkaya, Mordatch, Plappert, Petron, Powell, Wong, Schneider, Tezak, Tobin, et al.; OpenAI
- **disclosure**: Andrychowicz, M. et al. 'Learning Dexterous In-Hand Manipulation'. arXiv:1808.00177, July 30, 2018; OpenAI. Akkaya, I. et al. 'Solving Rubik's Cube with a Robot Hand'. arXiv:1910.07113, October 16, 2019.
- **ip status**: open-permissive
- **prior art notes**: Dactyl is the foundational academic disclosure of large-scale sim-to-real RL for in-hand dexterous manipulation. Anticipates: (1) zero-shot policy transfer from massively-randomized simulation to real hardware — directly relevant to claims on sim-to-real humanoid manipulation IP (every modern humanoid hand uses this paradigm); (2) automatic domain randomization (ADR) as a self-tuning training procedure — relevant to claims on adaptive-randomization training; (3) LSTM-based policies for partial-observability manipulation — relevant to recurrent-policy IP. OpenAI's open-source code release plus the arXiv preprints provide deep prior art coverage. Modern in-hand-manipulation claims face this 2018-2019 anchor.

## Hwangbo ANYmal Sim-to-Real Locomotion (2019-01-16)

- **id**: `hwangbo-anymal-sim2real`
- **corpus**: academic
- **creator**: Hwangbo, Lee, Dosovitskiy, Bellicoso, Tsounis, Koltun, Hutter; ETH Zürich Robotic Systems Lab + Intel Intelligent Systems Lab
- **disclosure**: Hwangbo, Jemin, Lee, Joonho, Dosovitskiy, Alexey, Bellicoso, Dario, Tsounis, Vassilios, Koltun, Vladlen, Hutter, Marco. 'Learning agile and dynamic motor skills for legged robots.' Science Robotics 4(26): eaau5872, January 16, 2019.
- **ip status**: open-permissive
- **prior art notes**: Hwangbo et al. 2019 is the foundational academic disclosure of practical RL-based sim-to-real legged locomotion. Anticipates with full architectural specificity: (1) actuator-network-based high-fidelity simulation (neural network as drop-in actuator dynamics) — directly relevant to claims on humanoid sim-to-real pipelines (Berkeley Humanoid, Apptronik Apollo, Tesla Optimus all use derivatives); (2) zero-shot policy transfer from RL-in-sim to legged hardware — anticipates virtually every modern legged-RL-policy patent; (3) recovery from arbitrary falls via single learned policy — relevant to fall-recovery IP for humanoids. Published in Science Robotics; one of the most-cited robotics RL papers (>2000 citations). Modern humanoid sim-to-real claims face this 7-year-deep anchor with full peer-review defensibility.

## RoboCat (Self-Improving Generalist Agent) (2023-06-20)

- **id**: `robocat`
- **corpus**: academic
- **creator**: DeepMind (Bousmalis et al.)
- **disclosure**: Bousmalis, Konstantinos et al. 'RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation.' arXiv:2306.11706, June 20, 2023. Transactions on Machine Learning Research, 2024. Authors: Bousmalis, K., Vezzani, G., Rao, D., Devin, C., Lee, A.X., Bauza, M., Davchev, T., Zhou, Y., Gupta, A., Raju, A., Laurens, A., Fantacci, C., Dalibard, V., Zambelli, M., Martins, M., Pevceviciute, R., Blokzijl, M., Denil, M., Batchelor, N., Lampe, T., Parisotto, E., Zolna, K., Reed, S., Colmenarejo, S.G., Scholz, J., Abdolmaleki, A., Groth, O., Regli, J-B., Sushkov, O., Rothorl, T., Chen, J.E., Aytar, Y., Barker, D., Ortiz, J., Riedmiller, M., Springenberg, J.T., Hadsell, R., Nori, F., Heess, N. (DeepMind).
- **ip status**: open-permissive
- **prior art notes**: RoboCat is the canonical academic disclosure of self-improving multi-embodiment generalist robotic policies. Anticipates: (1) the cross-embodiment training loop where one model generalizes across distinct robot platforms — directly relevant to claims on humanoid policies trained on heterogeneous robot data (a core selling point of every commercial humanoid VLA); (2) self-collected-data improvement loop — relevant to autonomous-data-flywheel claims (Tesla Dojo + Optimus, Figure's data pipeline); (3) image-goal-conditioned policy as a unified interface — relevant to goal-image-conditioned manipulation IP. Published TMLR + arXiv June 2023; partial code release. Modern humanoid 'data flywheel' patent claims face this anchor.

## Open X-Embodiment (2023-10)

- **id**: `open-x-embodiment`
- **corpus**: academic
- **creator**: 34-lab international collaboration coordinated by Google DeepMind
- **disclosure**: Open X-Embodiment Collaboration. 'Open X-Embodiment: Robotic Learning Datasets and RT-X Models.' arXiv 2310.08864, October 2023.
- **ip status**: open-permissive
- **prior art notes**: Open X-Embodiment is the dominant publicly-disclosed prior art for cross-embodiment learning. The dataset itself plus the architectural paper anticipate broad swaths of cross-platform manipulation foundation model claims.

## Eureka LLM-driven reward design (2023-10)

- **id**: `eureka-ma-2023`
- **corpus**: academic
- **creator**: Yecheng Jason Ma et al., NVIDIA / UPenn / Caltech / UT Austin
- **disclosure**: Ma, Yecheng Jason, Liang, William, Wang, Guanzhi, Huang, De-An, Bastani, Osbert, Jayaraman, Dinesh, Zhu, Yuke, Fan, Linxi, Anandkumar, Anima. 'Eureka: Human-Level Reward Design via Coding Large Language Models.' arXiv:2310.12931, October 2023; ICLR 2024.
- **ip status**: public-domain
- **prior art notes**: Eureka is the canonical academic disclosure of LLM-authored reward functions for robotic RL, an entire engineering layer that prior IP and academic work treated as human craftsmanship. Anticipates with full specificity: (1) claims on automatic reward function generation for humanoid skill learning — Eureka discloses the LLM-authoring + sim-evaluation + reflective-rewriting closed loop; (2) claims on evolutionary refinement of reward code — Eureka's headline contribution; (3) claims on LLM-in-the-loop sim-to-real pipelines for dexterous and locomotion tasks — Eureka demonstrates Shadow Hand pen-spinning at human-comparable performance. Code and prompts released open-source on GitHub (NVlabs/Eureka). >800 citations within 18 months. Modern humanoid LLM-reward-design IP claims face this 2.5-year-deep anchor with full code disclosure.

## LimX Dynamics CL-1 (2023-12)

- **id**: `limx-cl1`
- **corpus**: private
- **creator**: LimX Dynamics
- **disclosure**: LimX Dynamics public reveal, December 2023.
- **ip status**: patented
- **prior art notes**: LimX QDD actuation derives from MIT Cheetah lineage; bipedal control claims anticipated by Cassie/ATRIAS work.

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

## Robot Era STAR1 (2024-10)

- **id**: `robot-era-star1`
- **corpus**: private
- **creator**: Robot Era
- **disclosure**: Robot Era public reveal of STAR1, October 2024.
- **ip status**: patented
- **prior art notes**: Bipedal running speed claims anticipated by Cassie's Guinness record work.

## EngineAI PM01 (2024-12)

- **id**: `engineai-pm01`
- **corpus**: private
- **creator**: EngineAI
- **disclosure**: EngineAI public reveal of PM01, December 2024.
- **ip status**: patented
- **prior art notes**: EngineAI QDD actuation anticipated by MIT Cheetah lineage.
