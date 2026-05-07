---
title: "control-sim-to-real"
parent: "Invalidity Contentions"
nav_order: 18
layout: default
---

# Invalidity Contention Packet — `control-sim-to-real`

**Generated:** 2026-05-07  
**Cross-cut tag:** `control-sim-to-real`  
**Entries:** 19 (14 commons-grade, 5 draft)  
**Earliest disclosure:** 2014-12-11  
**Most recent disclosure:** 2026-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-sim-to-real`.

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

### 2014-12-11 — Talos Principle Robots

- **id:** `talos-principle-robots`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Croteam (game); Tom Jubert and Jonas Kyratzes (story)
- **disclosure citation:** Croteam. The Talos Principle. Devolver Digital, December 11, 2014. Story by Tom Jubert and Jonas Kyratzes.
- **disclosed subsystems:** `control-rl-policy`, `control-sim-to-real`, `mechanism-bipedal-locomotion`

**Prior art notes:**

> The Talos Principle is one of the most engineering-philosophical fictional disclosures of *sim-to-real training as the explicit deployment paradigm* for humanoid policies. Anticipates: (1) deliberately-constructed simulation training environment as the policy-acquisition substrate — directly relevant to modern sim-to-real humanoid IP (every commercial humanoid uses some variant of this paradigm); (2) curriculum design for progressive task difficulty — relevant to curriculum-learning humanoid claims; (3) ethical/philosophical reasoning as part of the training curriculum — relevant to alignment-supervision humanoid IP. The 2014 release predates much of the academic literature on sim-to-real humanoid policies. Continuously available since 2014.

**Sources:**

1. Croteam. The Talos Principle. Devolver Digital, 2014.
2. Jubert, T. and Kyratzes, J. The Talos Principle (story documentation).

---

### 2016 — ANYmal

- **id:** `anymal`
- **corpus:** private
- **ip status:** patented
- **creator:** ANYbotics, ETH Zurich Robotic Systems Lab
- **disclosure citation:** Hutter, M. et al. 'ANYmal — a highly mobile and dynamic quadrupedal robot.' IROS 2016.
- **disclosed subsystems:** `actuator-electric-series-elastic`, `mechanism-quadrupedal-locomotion`, `control-rl-policy`, `control-sim-to-real`, `sensing-stereo-camera`, `sensing-lidar`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> ANYbotics SEA design heavily anticipated by NASA Valkyrie and Robonaut SEA work. ETH RSL academic publications provide open prior art for many control claims.

**Sources:**

1. Hutter, M. et al. IROS 2016.
2. ANYbotics company materials.

---

### 2017 — Cassie

- **id:** `cassie-osu`
- **corpus:** academic
- **ip status:** patented
- **creator:** Oregon State University, Dynamic Robotics Laboratory (Jonathan Hurst)
- **disclosure citation:** Agility Robotics / Oregon State University Cassie release, 2017.
- **disclosed subsystems:** `actuator-electric-series-elastic`, `mechanism-bipedal-locomotion`, `mechanism-passive-dynamic-walking`, `control-reduced-order-model`, `control-rl-policy`, `control-sim-to-real`, `sensing-imu`, `software-ros1`

**Prior art notes:**

> Cassie and the broader Hurst lab work on reduced-order locomotion models is significant prior art for bipedal control claims industry-wide.

**Sources:**

1. Hurst Lab publications.
2. Agility Robotics technical materials.

---

### 2018-04-28 — Tan et al. Quadruped Sim-to-Real

- **id:** `tan-quadruped-sim2real`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Google Brain + Google Robotics (Tan, Zhang, Coumans, Iscen, Bai, Hafner, Bohez, Vanhoucke)
- **disclosure citation:** Tan, Jie, Zhang, Tingnan, Coumans, Erwin, Iscen, Atil, Bai, Yunfei, Hafner, Danijar, Bohez, Steven, Vanhoucke, Vincent. 'Sim-to-Real: Learning Agile Locomotion For Quadruped Robots.' arXiv:1804.10332, April 28, 2018. Robotics: Science and Systems (RSS) 2018.
- **disclosed subsystems:** `control-rl-policy`, `control-sim-to-real`, `actuator-electric-quasi-direct-drive`, `mechanism-quadrupedal-locomotion`, `sensing-imu`

**Prior art notes:**

> Tan et al. 2018 is one of the earliest academic disclosures of practical sim-to-real RL for quadrupedal locomotion, predating Hwangbo 2019 by ~9 months and establishing the system-identification + domain-randomization paradigm for legged sim-to-real. Anticipates: (1) PPO-based RL for legged locomotion with subsequent zero-shot hardware transfer — relevant to RL-locomotion-policy patents (Boston Dynamics, Unitree, every commercial quadruped); (2) explicit actuator-latency modeling as a sim-to-real bridge — relevant to claims on real-time sim-to-real techniques; (3) the quasi-direct-drive Minitaur platform combined with sim-to-real — relevant to QDD-actuator+RL humanoid claims. Open-source code via PyBullet repository. RSS 2018 publication. Modern legged sim-to-real claims face an 8-year-deep anchor.

**Sources:**

1. Tan, J. et al. 'Sim-to-Real: Learning Agile Locomotion For Quadruped Robots.' RSS 2018; arXiv:1804.10332.
2. Coumans, E. and Bai, Y. PyBullet, 2017-present (simulator used).

---

### 2018-07-30 — OpenAI Dactyl

- **id:** `openai-dactyl`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Andrychowicz, Akkaya, Mordatch, Plappert, Petron, Powell, Wong, Schneider, Tezak, Tobin, et al.; OpenAI
- **disclosure citation:** Andrychowicz, M. et al. 'Learning Dexterous In-Hand Manipulation'. arXiv:1808.00177, July 30, 2018; OpenAI. Akkaya, I. et al. 'Solving Rubik's Cube with a Robot Hand'. arXiv:1910.07113, October 16, 2019.
- **disclosed subsystems:** `control-rl-policy`, `control-sim-to-real`, `mechanism-anthropomorphic-hand`, `actuator-pneumatic-muscle`

**Prior art notes:**

> Dactyl is the foundational academic disclosure of large-scale sim-to-real RL for in-hand dexterous manipulation. Anticipates: (1) zero-shot policy transfer from massively-randomized simulation to real hardware — directly relevant to claims on sim-to-real humanoid manipulation IP (every modern humanoid hand uses this paradigm); (2) automatic domain randomization (ADR) as a self-tuning training procedure — relevant to claims on adaptive-randomization training; (3) LSTM-based policies for partial-observability manipulation — relevant to recurrent-policy IP. OpenAI's open-source code release plus the arXiv preprints provide deep prior art coverage. Modern in-hand-manipulation claims face this 2018-2019 anchor.

**Sources:**

1. Andrychowicz, M. et al. 'Learning Dexterous In-Hand Manipulation'. arXiv:1808.00177, 2018.
2. Akkaya, I. et al. 'Solving Rubik's Cube with a Robot Hand'. arXiv:1910.07113, 2019.
3. OpenAI Dactyl GitHub releases.

---

### 2019-01-16 — Hwangbo ANYmal Sim-to-Real Locomotion

- **id:** `hwangbo-anymal-sim2real`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Hwangbo, Lee, Dosovitskiy, Bellicoso, Tsounis, Koltun, Hutter; ETH Zürich Robotic Systems Lab + Intel Intelligent Systems Lab
- **disclosure citation:** Hwangbo, Jemin, Lee, Joonho, Dosovitskiy, Alexey, Bellicoso, Dario, Tsounis, Vassilios, Koltun, Vladlen, Hutter, Marco. 'Learning agile and dynamic motor skills for legged robots.' Science Robotics 4(26): eaau5872, January 16, 2019.
- **disclosed subsystems:** `control-rl-policy`, `control-sim-to-real`, `actuator-electric-series-elastic`, `mechanism-quadrupedal-locomotion`, `sensing-imu`

**Prior art notes:**

> Hwangbo et al. 2019 is the foundational academic disclosure of practical RL-based sim-to-real legged locomotion. Anticipates with full architectural specificity: (1) actuator-network-based high-fidelity simulation (neural network as drop-in actuator dynamics) — directly relevant to claims on humanoid sim-to-real pipelines (Berkeley Humanoid, Apptronik Apollo, Tesla Optimus all use derivatives); (2) zero-shot policy transfer from RL-in-sim to legged hardware — anticipates virtually every modern legged-RL-policy patent; (3) recovery from arbitrary falls via single learned policy — relevant to fall-recovery IP for humanoids. Published in Science Robotics; one of the most-cited robotics RL papers (>2000 citations). Modern humanoid sim-to-real claims face this 7-year-deep anchor with full peer-review defensibility.

**Sources:**

1. Hwangbo, J. et al. 'Learning agile and dynamic motor skills for legged robots.' Science Robotics 4(26), 2019.
2. Lee, J. et al. 'Learning quadrupedal locomotion over challenging terrain.' Science Robotics 5(47), 2020 (sequel).

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

### 2023-01-10 — Dreamer V3

- **id:** `hafner-dreamer-v3-2023`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Danijar Hafner, Jurgis Pasukonis, Jimmy Ba, Timothy Lillicrap; Google DeepMind, University of Toronto
- **disclosure citation:** Hafner, Danijar; Pasukonis, Jurgis; Ba, Jimmy; Lillicrap, Timothy. 'Mastering diverse domains through world models'. arXiv:2301.04104, January 10, 2023. Earlier Dreamer (Hafner et al. 2019/2020) at arXiv:1912.01603.
- **disclosed subsystems:** `control-rl-policy`, `control-sim-to-real`

**Prior art notes:**

> Dreamer V3 (2023) is one of the strongest academic disclosures of model-based RL for cross-domain generalization. Anticipates: (1) world-model RL (RSSM) as the policy-learning substrate for humanoid platforms — relevant to modern model-based humanoid IP; (2) imagination-rollout-based policy training — relevant to claims on data-efficient humanoid RL; (3) cross-domain generalization without per-task hyperparameter tuning — relevant to platform-agnostic humanoid policy IP. The 2023 arXiv preprint plus the open-source DreamerV3 reference implementation provide deep prior art coverage. Modern world-model-based humanoid IP face this 3-year academic anchor.

**Sources:**

1. Hafner, D. et al. 'Mastering diverse domains through world models'. arXiv:2301.04104, 2023.
2. Hafner, D. et al. 'Dream to control'. arXiv:1912.01603, ICLR 2020 (predecessor).

---

### 2023-06-20 — RoboCat (Self-Improving Generalist Agent)

- **id:** `robocat`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** DeepMind (Bousmalis et al.)
- **disclosure citation:** Bousmalis, Konstantinos et al. 'RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation.' arXiv:2306.11706, June 20, 2023. Transactions on Machine Learning Research, 2024. Authors: Bousmalis, K., Vezzani, G., Rao, D., Devin, C., Lee, A.X., Bauza, M., Davchev, T., Zhou, Y., Gupta, A., Raju, A., Laurens, A., Fantacci, C., Dalibard, V., Zambelli, M., Martins, M., Pevceviciute, R., Blokzijl, M., Denil, M., Batchelor, N., Lampe, T., Parisotto, E., Zolna, K., Reed, S., Colmenarejo, S.G., Scholz, J., Abdolmaleki, A., Groth, O., Regli, J-B., Sushkov, O., Rothorl, T., Chen, J.E., Aytar, Y., Barker, D., Ortiz, J., Riedmiller, M., Springenberg, J.T., Hadsell, R., Nori, F., Heess, N. (DeepMind).
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-rl-policy`, `control-sim-to-real`

**Prior art notes:**

> RoboCat is the canonical academic disclosure of self-improving multi-embodiment generalist robotic policies. Anticipates: (1) the cross-embodiment training loop where one model generalizes across distinct robot platforms — directly relevant to claims on humanoid policies trained on heterogeneous robot data (a core selling point of every commercial humanoid VLA); (2) self-collected-data improvement loop — relevant to autonomous-data-flywheel claims (Tesla Dojo + Optimus, Figure's data pipeline); (3) image-goal-conditioned policy as a unified interface — relevant to goal-image-conditioned manipulation IP. Published TMLR + arXiv June 2023; partial code release. Modern humanoid 'data flywheel' patent claims face this anchor.

**Sources:**

1. Bousmalis, K. et al. 'RoboCat: A Self-Improving Generalist Agent.' TMLR 2024; arXiv:2306.11706.
2. DeepMind blog: https://deepmind.google/discover/blog/robocat-a-self-improving-robotic-agent/

---

### 2023-10 — Open X-Embodiment

- **id:** `open-x-embodiment`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** 34-lab international collaboration coordinated by Google DeepMind
- **disclosure citation:** Open X-Embodiment Collaboration. 'Open X-Embodiment: Robotic Learning Datasets and RT-X Models.' arXiv 2310.08864, October 2023.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-rl-policy`, `control-sim-to-real`

**Prior art notes:**

> Open X-Embodiment is the dominant publicly-disclosed prior art for cross-embodiment learning. The dataset itself plus the architectural paper anticipate broad swaths of cross-platform manipulation foundation model claims.

**Sources:**

1. arXiv 2310.08864.
2. robotics-transformer-x.github.io

---

### 2023-10 — Eureka LLM-driven reward design

- **id:** `eureka-ma-2023`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Yecheng Jason Ma et al., NVIDIA / UPenn / Caltech / UT Austin
- **disclosure citation:** Ma, Yecheng Jason, Liang, William, Wang, Guanzhi, Huang, De-An, Bastani, Osbert, Jayaraman, Dinesh, Zhu, Yuke, Fan, Linxi, Anandkumar, Anima. 'Eureka: Human-Level Reward Design via Coding Large Language Models.' arXiv:2310.12931, October 2023; ICLR 2024.
- **disclosed subsystems:** `control-rl-policy`, `control-sim-to-real`, `control-vla-vision-language-action`

**Prior art notes:**

> Eureka is the canonical academic disclosure of LLM-authored reward functions for robotic RL, an entire engineering layer that prior IP and academic work treated as human craftsmanship. Anticipates with full specificity: (1) claims on automatic reward function generation for humanoid skill learning — Eureka discloses the LLM-authoring + sim-evaluation + reflective-rewriting closed loop; (2) claims on evolutionary refinement of reward code — Eureka's headline contribution; (3) claims on LLM-in-the-loop sim-to-real pipelines for dexterous and locomotion tasks — Eureka demonstrates Shadow Hand pen-spinning at human-comparable performance. Code and prompts released open-source on GitHub (NVlabs/Eureka). >800 citations within 18 months. Modern humanoid LLM-reward-design IP claims face this 2.5-year-deep anchor with full code disclosure.

**Sources:**

1. Ma, Y. J. et al. 'Eureka: Human-Level Reward Design via Coding Large Language Models.' arXiv:2310.12931, 2023.
2. Eureka GitHub: github.com/eureka-research/Eureka

---

### 2023-12 — LimX Dynamics CL-1 *(draft)*

- **id:** `limx-cl1`
- **corpus:** private
- **ip status:** patented
- **creator:** LimX Dynamics
- **disclosure citation:** LimX Dynamics public reveal, December 2023.
- **disclosed subsystems:** `actuator-electric-quasi-direct-drive`, `mechanism-bipedal-locomotion`, `control-rl-policy`, `control-sim-to-real`, `sensing-stereo-camera`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> LimX QDD actuation derives from MIT Cheetah lineage; bipedal control claims anticipated by Cassie/ATRIAS work.

**Sources:**

1. LimX Dynamics website.

---

### 2024 — K-Scale Labs Open Source Humanoid *(draft)*

- **id:** `k-scale-os`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** K-Scale Labs
- **disclosure citation:** K-Scale Labs project launch, 2024.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `mechanism-bipedal-locomotion`, `control-rl-policy`, `control-sim-to-real`, `sensing-stereo-camera`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> Among the most ambitious recent fully-open humanoid efforts. Direct peer to Free Humanoid in scope.

**Sources:**

1. kscale.dev

---

### 2024 — Berkeley Humanoid

- **id:** `berkeley-humanoid`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** UC Berkeley, Hybrid Robotics Lab
- **disclosure citation:** Liao, Q. et al. 'Berkeley Humanoid: A Research Platform for Learning-based Control.' arXiv 2024.
- **disclosed subsystems:** `actuator-electric-quasi-direct-drive`, `mechanism-bipedal-locomotion`, `control-rl-policy`, `control-sim-to-real`, `sensing-stereo-camera`, `sensing-imu`

**Prior art notes:**

> Berkeley quasi-direct-drive lineage (predates the humanoid; comes from the Mini Cheetah / leg work) anticipates many actuator architecture claims.

**Sources:**

1. arXiv preprint, 2024.
2. Hybrid Robotics Lab page.

---

### 2024-03-18 — NVIDIA GR00T (Generalist Robot 00 Technology)

- **id:** `nvidia-groot-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** NVIDIA Research, GEAR Lab
- **disclosure citation:** Huang, Jensen et al. NVIDIA GR00T announcement at GTC 2024 keynote, March 18, 2024. Technical disclosure: Reddit Project GR00T technical blog, March 2024. GR00T N1 paper published 2025-03 (arXiv:2503.14734).
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-rl-policy`, `control-sim-to-real`

**Prior art notes:**

> NVIDIA GR00T's 2024 disclosure is the canonical foundation-model-for-humanoids announcement. Anticipates: (1) dual-system fast/slow policy architecture for humanoid platforms — directly relevant to modern humanoid foundation-model IP (every major humanoid manufacturer is developing equivalent architectures); (2) cross-embodiment generalization across multiple humanoid platforms — relevant to platform-agnostic policy IP; (3) open-weights humanoid foundation model release — provides defensive baseline against closed-weights claims. The March 2024 GTC keynote announcement plus the subsequent GR00T N1 paper (March 2025) and open-weights release provide extensive prior art coverage.

**Sources:**

1. NVIDIA. Project GR00T technical blog. NVIDIA Developer, March 2024.
2. NVIDIA GEAR Lab. 'GR00T N1: An Open Foundation Model for Generalist Humanoid Robots'. arXiv:2503.14734, March 2025.

---

### 2024-10 — Robot Era STAR1 *(draft)*

- **id:** `robot-era-star1`
- **corpus:** private
- **ip status:** patented
- **creator:** Robot Era
- **disclosure citation:** Robot Era public reveal of STAR1, October 2024.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `control-rl-policy`, `control-sim-to-real`, `sensing-stereo-camera`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> Bipedal running speed claims anticipated by Cassie's Guinness record work.

**Sources:**

1. Robot Era company materials.
2. Tsinghua University announcements.

---

### 2024-12 — EngineAI PM01 *(draft)*

- **id:** `engineai-pm01`
- **corpus:** private
- **ip status:** patented
- **creator:** EngineAI
- **disclosure citation:** EngineAI public reveal of PM01, December 2024.
- **disclosed subsystems:** `actuator-electric-quasi-direct-drive`, `mechanism-bipedal-locomotion`, `control-rl-policy`, `control-sim-to-real`, `sensing-monocular-depth`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> EngineAI QDD actuation anticipated by MIT Cheetah lineage.

**Sources:**

1. EngineAI company materials.
2. Chinese-language tech press coverage.

---

### 2024-12 — Genesis (open-source physics simulator)

- **id:** `genesis-embodied-ai-simulator`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** Genesis Authors collaboration (multi-institution: CMU, Stanford, MIT CSAIL, Tsinghua, Peking, ETH Zürich, UMD, et al.)
- **disclosure citation:** Genesis Authors. 'Genesis: A Generative and Universal Physics Engine for Robotics and Beyond'. GitHub release at https://github.com/Genesis-Embodied-AI/Genesis, December 19, 2024. Multi-institution collaboration including Carnegie Mellon University, Stanford University, MIT CSAIL, Tsinghua University, Peking University, ETH Zürich, University of Maryland.
- **disclosed subsystems:** `control-sim-to-real`, `control-rl-policy`, `control-mpc`

**Prior art notes:**

> The Genesis simulator (Genesis-Embodied-AI/Genesis, December 2024) is the most recent and highest-throughput academic-grade open-source physics engine for robotics simulation, published Apache-2.0 by a multi-institution academic collaboration. Anticipates with full architectural specificity: (1) GPU-parallelized robotics simulation at 43M-FPS scale — directly relevant to commercial claims on sim-to-real-at-scale humanoid IP (notably Genesis AI Inc.'s GENE-26.5 product, with which this open-source project shares a name); (2) unified multi-physics architecture (rigid + soft + MPM + FEM + fluid) — relevant to claims on multi-domain humanoid simulation; (3) differentiable simulation for gradient-based policy optimization — relevant to claims on policy-gradient humanoid training at scale; (4) the URDF/MJCF interoperability surface that permits OpenLoco-class descriptors to be simulated without modification. Modern claims on sim-to-real-at-scale, multi-physics simulation, or differentiable physics for humanoid training all face this 1.5-year-deep open-source academic prior art with full source disclosure under Apache-2.0.

**Sources:**

1. Genesis-Embodied-AI/Genesis GitHub repository (https://github.com/Genesis-Embodied-AI/Genesis), December 2024.
2. Genesis project website (https://genesis-embodied-ai.github.io/), December 2024.
3. Genesis benchmark report (rigid-body 43M FPS on RTX 4090) included with the December 2024 release.

---

### 2026-04 — Genesis AI GENE-26.5 *(draft)*

- **id:** `genesis-ai-gene-26-5`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Genesis AI Inc.
- **disclosure citation:** Genesis AI Inc. corporate website at https://www.genesis.ai/, GENE-26.5 product page (April 2026 surface). Demo videos showing cooking, lab pipetting, beverage preparation, puzzle-solving, object manipulation, assembly, and fine-motor tasks.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-rl-policy`, `control-sim-to-real`, `mechanism-anthropomorphic-hand`, `mechanism-bipedal-locomotion`

**Prior art notes:**

> Genesis AI's GENE-26.5 platform is a closed-source commercial robotics product whose public disclosure surface (corporate website + demo videos) does not reveal specific mechanism. The capability set claimed — multi-task vision-language-action manipulation, sim-to-real generalization, dexterous fine-motor — is fully covered by deep open academic prior art chains in the corpus: Pomerleau ALVINN (1989) → Levine GPS PR2/BRETT (2016) for end-to-end visuomotor policy; CLIP (Radford 2021) for vision-language alignment; RT-1 (2022), RT-2 (2023), Open X-Embodiment (2023), OpenVLA (2024), π-zero (2024), NVIDIA GR00T N1 (2025) for VLA architecture; OpenAI Dactyl (2018-2019), Hwangbo ANYmal sim-to-real (2019), Tan quadruped sim-to-real (2018) for sim-to-real; Mobile ALOHA (2024), ACT/ALOHA (2023), Diffusion Policy (2023) for bimanual fine manipulation; Salisbury Stanford-JPL hand (1982), DLR Hand-II (2001), Shadow Hand (2002), Pisa-IIT SoftHand (2014) for dexterous hand mechanism; Park's transformation (1929) for any FOC actuator control. Claims that GENE represents novel art in any of these subsystems face element-by-element prior art at depths from 4 years (Diffusion Policy) to 97 years (Park) to 530 years (Da Vinci's Knight, anthropomorphic tendon-driven hand). Demo task set (cooking, beverage preparation, lab manipulation) maps directly to Mobile ALOHA (2024), DLR Justin (2009), CMU HERB (2012), and the PR2 lineage.

**Sources:**

1. Genesis AI Inc. corporate website (https://www.genesis.ai/), April 2026 surface.
2. GENE-26.5 demonstration videos on the Genesis AI corporate website.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `559a8b5`.*
