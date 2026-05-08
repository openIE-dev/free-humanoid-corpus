---
title: control-sim-to-real
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-sim-to-real`

**30 corpus entries disclose this subsystem.**

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

## OmniGibson / iGibson (Stanford SVL) (2018-04)

- **id**: `stanford-omnigibson-2023`
- **corpus**: academic
- **creator**: Stanford Vision and Learning Lab (Silvio Savarese, Fei-Fei Li); lead authors include Fei Xia, Chengshu Li, Roberto Martín-Martín, Sanjana Srivastava, Cem Gokmen
- **disclosure**: Xia, Fei; Zamir, Amir R.; He, Zhiyang; Sax, Alexander; Malik, Jitendra; Savarese, Silvio. 'Gibson Env: Real-World Perception for Embodied Agents.' IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Salt Lake City, June 2018, pp. 9068-9079. DOI: 10.1109/CVPR.2018.00945. iGibson 2.0: Li, Chengshu et al. 'iGibson 2.0: Object-Centric Simulation for Robot Learning of Everyday Household Tasks.' Conference on Robot Learning (CoRL) 2021. OmniGibson: Li, Chengshu et al. 'BEHAVIOR-1K: A Benchmark for Embodied AI with 1,000 Everyday Activities and Realistic Simulation.' CoRL 2022. Source: https://github.com/StanfordVL/OmniGibson, MIT license.
- **ip status**: open-permissive
- **prior art notes**: Stanford OmniGibson / iGibson / Gibson (Xia et al. CVPR 2018; Li et al. CoRL 2021; BEHAVIOR-1K CoRL 2022) is the canonical academic disclosure of large-scale photorealistic household-task embodied-AI simulation, published MIT-licensed by Stanford SVL. Anticipates with full source-level specificity: (1) 1,000-task ADL benchmark for household humanoid IP — directly relevant to commercial claims on home-task humanoid VLA training (Tesla Optimus household demo set, Figure 02 home tasks, 1X NEO domestic operation, Genesis AI cooking demos); (2) the articulated-object household scene corpus with 50K+ objects — relevant to claims on simulated-household-data humanoid training; (3) predicate-based goal specification ('apple is on table', 'cabinet is open') — relevant to claims on language-and-state-grounded humanoid task specification; (4) the photorealistic-rendering-for-RL pipeline established by Gibson 2018 — anticipates claims on photorealistic-sim-to-real humanoid pipelines. Modern household-humanoid VLA training pipeline IP filings face this 8-year-deep open-source academic anchor (or shorter for OmniGibson/BEHAVIOR-1K specifically).

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

## Stonefish underwater robotics simulator (2018-10)

- **id**: `stonefish-sim-2018`
- **corpus**: open
- **creator**: Patryk Cieslak (University of Girona / Computer Vision and Robotics group)
- **disclosure**: Cieslak, P. 'Stonefish: An Advanced Open-Source Simulation Tool Designed for Marine Robotics'. OCEANS 2019 IEEE/MTS, Marseille; preceded by IROS 2018 workshop demo. Open-source under CC-BY-NC-SA initially; later relicensed Apache-2.0 for upstream merge into ROS Underwater (2021).
- **ip status**: open-permissive
- **prior art notes**: Stonefish is the canonical open-source academic underwater robotics simulator. 7 years of public-academic publication and Apache-2.0 source. Establishes prior art for: fluid-drag-aware AUV/ROV simulation, simulated sonar return modeling, tether-dynamics simulation, ROS-integrated policy training for marine robotics. Directly shields free-humanoid-submersible's Phase-1 sim-to-real workflow (alongside Genesis MPM/fluid for higher-fidelity hydrodynamics). Any commercial claim on 'underwater-physics-aware sim-to-real for AUVs' faces 7 years of full-source open prior art.

## Hwangbo ANYmal Sim-to-Real Locomotion (2019-01-16)

- **id**: `hwangbo-anymal-sim2real`
- **corpus**: academic
- **creator**: Hwangbo, Lee, Dosovitskiy, Bellicoso, Tsounis, Koltun, Hutter; ETH Zürich Robotic Systems Lab + Intel Intelligent Systems Lab
- **disclosure**: Hwangbo, Jemin, Lee, Joonho, Dosovitskiy, Alexey, Bellicoso, Dario, Tsounis, Vassilios, Koltun, Vladlen, Hutter, Marco. 'Learning agile and dynamic motor skills for legged robots.' Science Robotics 4(26): eaau5872, January 16, 2019.
- **ip status**: open-permissive
- **prior art notes**: Hwangbo et al. 2019 is the foundational academic disclosure of practical RL-based sim-to-real legged locomotion. Anticipates with full architectural specificity: (1) actuator-network-based high-fidelity simulation (neural network as drop-in actuator dynamics) — directly relevant to claims on humanoid sim-to-real pipelines (Berkeley Humanoid, Apptronik Apollo, Tesla Optimus all use derivatives); (2) zero-shot policy transfer from RL-in-sim to legged hardware — anticipates virtually every modern legged-RL-policy patent; (3) recovery from arbitrary falls via single learned policy — relevant to fall-recovery IP for humanoids. Published in Science Robotics; one of the most-cited robotics RL papers (>2000 citations). Modern humanoid sim-to-real claims face this 7-year-deep anchor with full peer-review defensibility.

## Habitat-Sim (Facebook AI Research) (2019-04)

- **id**: `fair-habitat-sim-2019`
- **corpus**: academic
- **creator**: Facebook AI Research (FAIR) and Georgia Tech (Dhruv Batra), Simon Fraser University (Manolis Savva); collaborative team including Jitendra Malik (Berkeley), Vladlen Koltun (Intel)
- **disclosure**: Savva, Manolis; Kadian, Abhishek; Maksymets, Oleksandr; Zhao, Yili; Wijmans, Erik; Jain, Bhavana; Straub, Julian; Liu, Jia; Koltun, Vladlen; Malik, Jitendra; Parikh, Devi; Batra, Dhruv. 'Habitat: A Platform for Embodied AI Research.' IEEE/CVF International Conference on Computer Vision (ICCV), Seoul, October-November 2019, pp. 9339-9347. DOI: 10.1109/ICCV.2019.00943. arXiv:1904.01201, April 2019. Source code at https://github.com/facebookresearch/habitat-sim. MIT license.
- **ip status**: open-permissive
- **prior art notes**: Habitat-Sim (Savva et al. ICCV 2019; Habitat 2.0 NeurIPS 2021; Habitat 3.0 ICLR 2024) is the canonical academic disclosure of large-scale GPU-accelerated 3D-scanned indoor embodied-AI simulation, published MIT-licensed by FAIR. Anticipates with element-by-element specificity: (1) >10,000 fps rendering of photorealistic indoor scenes for RL training — directly relevant to commercial claims on simulation-at-scale humanoid embodied-AI pipelines; (2) the navigation-benchmark task suite (PointGoal, ObjectGoal, ImageGoal) that is now standard in embodied-AI literature — relevant to claims on humanoid navigation policy IP; (3) Habitat 3.0's humanoid-avatar simulation for social robot interaction — relevant to claims on human-aware humanoid IP and home-deployment humanoid VLA pipelines; (4) integration of large-scale 3D-scan corpora (Matterport, HM3D) with MIT-licensed renderers — relevant to claims on commercial-grade photorealistic simulation. Habitat is the most-cited embodied-AI simulator (>2000 citations on the 2019 paper alone). Modern household-deployment humanoid VLA pipeline IP filings face this 7-year-deep open-source academic anchor.

## SAPIEN simulator (2020-03)

- **id**: `sapien-xiang-cvpr-2020`
- **corpus**: academic
- **creator**: UC San Diego + Stanford; Hao Su, Leonidas Guibas, Angel Chang group
- **disclosure**: Xiang, F., Qin, Y., Mo, K., Xia, Y., Zhu, H., Liu, F., Liu, M., Jiang, H., Yuan, Y., Wang, H., Yi, L., Chang, A. X., Guibas, L. J., Su, H. 'SAPIEN: A SimulAted Part-based Interactive ENvironment'. arXiv:2003.08515, March 2020. CVPR 2020. UC San Diego + Stanford. ManiSkill follow-up framework via haosulab/ManiSkill (Hillbot Inc.).
- **ip status**: open-permissive
- **prior art notes**: SAPIEN is the canonical PartNet-Mobility-based articulated-object simulator (Xiang et al. CVPR 2020). 5-year-deep open-permissive prior art for: part-level mobility annotation in robotic simulation, depth-noise modeling for sim-to-real, ManiSkill manipulation benchmark suite. Distinct from MuJoCo (rigid-body baseline), Isaac Gym (GPU-parallelized), and Genesis (multi-physics) by emphasis on articulated-object interaction. Direct shielding for any commercial humanoid claim on articulated-object manipulation training simulation.

## NVIDIA Isaac Gym (2021-08)

- **id**: `nvidia-isaac-gym-2021`
- **corpus**: academic
- **creator**: NVIDIA + ETH Zürich Robotic Systems Lab; Makoviychuk et al.
- **disclosure**: Makoviychuk, V., Wawrzyniak, L., Guo, Y., Lu, M., Storey, K., Macklin, M., Hoeller, D., Rudin, N., Allshire, A., Handa, A., State, G. 'Isaac Gym: High-Performance GPU-Based Physics Simulation For Robot Learning'. NeurIPS 2021 Track on Datasets and Benchmarks. arXiv:2108.10470.
- **ip status**: open-permissive
- **prior art notes**: Isaac Gym is the canonical first-generation NVIDIA GPU-parallelized robotic RL simulator (NeurIPS 2021). 4-year-deep open-permissive prior art. Direct ancestor of Isaac Lab (round-8 entry nvidia-isaac-lab-2024) and the substrate for the canonical sim-to-real ANYmal perceptive-locomotion papers. Direct shielding for any commercial humanoid claim on GPU-parallelized RL training; particularly the thousands-of-parallel-envs scaling that commercial humanoid vendors cite as proprietary.

## ANYmal-D industrial quadruped (ETH RSL / ANYbotics) (2022-09)

- **id**: `anymal-d-eth-rsl-2022`
- **corpus**: academic
- **creator**: ANYbotics AG / ETH Zürich Robotic Systems Lab (Marco Hutter)
- **disclosure**: ANYbotics product disclosure ANYmal D, September 2022; technical updates in Miki, Takahiro et al. 'Learning robust perceptive locomotion for quadrupedal robots in the wild.' Science Robotics 7(62), 2022; Hoeller, David et al. 'ANYmal Parkour: Learning agile navigation for quadrupedal robots.' Science Robotics 9(88), 2024.
- **ip status**: public-domain
- **prior art notes**: ANYmal-D is the production-deployed industrial quadruped of the 2022-2024 period and the platform for the headline RSL/ANYbotics RL-locomotion papers in Science Robotics. It anticipates with full specificity: (1) claims on perceptive-locomotion RL policies trained in simulation and transferred to outdoor industrial terrain — Miki Sci.Rob. 2022 publishes the teacher-student distillation pipeline running on this hardware; (2) claims on agile parkour-class learned locomotion — Hoeller Sci.Rob. 2024 publishes the policy on ANYmal-D; (3) claims on series-elastic torque-controlled quadruped joints in IP67 industrial enclosures — ANYdrive disclosed at IROS 2018 with hardware refresh on D-variant. Modern legged-robot IP claims face this timestamped industrial-deployment anchor.

## Dreamer V3 (2023-01-10)

- **id**: `hafner-dreamer-v3-2023`
- **corpus**: academic
- **creator**: Danijar Hafner, Jurgis Pasukonis, Jimmy Ba, Timothy Lillicrap; Google DeepMind, University of Toronto
- **disclosure**: Hafner, Danijar; Pasukonis, Jurgis; Ba, Jimmy; Lillicrap, Timothy. 'Mastering diverse domains through world models'. arXiv:2301.04104, January 10, 2023. Earlier Dreamer (Hafner et al. 2019/2020) at arXiv:1912.01603.
- **ip status**: open-permissive
- **prior art notes**: Dreamer V3 (2023) is one of the strongest academic disclosures of model-based RL for cross-domain generalization. Anticipates: (1) world-model RL (RSSM) as the policy-learning substrate for humanoid platforms — relevant to modern model-based humanoid IP; (2) imagination-rollout-based policy training — relevant to claims on data-efficient humanoid RL; (3) cross-domain generalization without per-task hyperparameter tuning — relevant to platform-agnostic humanoid policy IP. The 2023 arXiv preprint plus the open-source DreamerV3 reference implementation provide deep prior art coverage. Modern world-model-based humanoid IP face this 3-year academic anchor.

## RoboCat (Self-Improving Generalist Agent) (2023-06-20)

- **id**: `robocat`
- **corpus**: academic
- **creator**: DeepMind (Bousmalis et al.)
- **disclosure**: Bousmalis, Konstantinos et al. 'RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation.' arXiv:2306.11706, June 20, 2023. Transactions on Machine Learning Research, 2024. Authors: Bousmalis, K., Vezzani, G., Rao, D., Devin, C., Lee, A.X., Bauza, M., Davchev, T., Zhou, Y., Gupta, A., Raju, A., Laurens, A., Fantacci, C., Dalibard, V., Zambelli, M., Martins, M., Pevceviciute, R., Blokzijl, M., Denil, M., Batchelor, N., Lampe, T., Parisotto, E., Zolna, K., Reed, S., Colmenarejo, S.G., Scholz, J., Abdolmaleki, A., Groth, O., Regli, J-B., Sushkov, O., Rothorl, T., Chen, J.E., Aytar, Y., Barker, D., Ortiz, J., Riedmiller, M., Springenberg, J.T., Hadsell, R., Nori, F., Heess, N. (DeepMind).
- **ip status**: open-permissive
- **prior art notes**: RoboCat is the canonical academic disclosure of self-improving multi-embodiment generalist robotic policies. Anticipates: (1) the cross-embodiment training loop where one model generalizes across distinct robot platforms — directly relevant to claims on humanoid policies trained on heterogeneous robot data (a core selling point of every commercial humanoid VLA); (2) self-collected-data improvement loop — relevant to autonomous-data-flywheel claims (Tesla Dojo + Optimus, Figure's data pipeline); (3) image-goal-conditioned policy as a unified interface — relevant to goal-image-conditioned manipulation IP. Published TMLR + arXiv June 2023; partial code release. Modern humanoid 'data flywheel' patent claims face this anchor.

## NVIDIA Isaac Lab (2023-08)

- **id**: `nvidia-isaac-lab-2024`
- **corpus**: academic
- **creator**: Mittal et al.; NVIDIA Corporation, ETH Zürich Robotic Systems Lab (Hutter), and University of Toronto Vector Institute (Garg)
- **disclosure**: Mittal, Mayank; Yu, Calvin; Yu, Qinxi; Liu, Jingzhou; Rudin, Nikita; Hoeller, David; Yuan, Jia Lin; Tehrani, Pooria S.; Singh, Ritvik; Guo, Yunrong; Mazhar, Hammad; Mandlekar, Ajay; Babich, Buck; State, Gavriel; Hutter, Marco; Garg, Animesh. 'ORBIT: A Unified Simulation Framework for Interactive Robot Learning Environments.' IEEE Robotics and Automation Letters (RA-L), August 2023; later released and rebranded as Isaac Lab in 2024. Repository at https://github.com/isaac-sim/IsaacLab.
- **ip status**: open-permissive
- **prior art notes**: Isaac Lab (formerly ORBIT, 2023) is the canonical academic-published GPU-parallelized simulation framework for robot learning, published BSD-3-Clause by NVIDIA + ETH Zürich + University of Toronto. Anticipates with full architectural specificity: (1) thousands-of-parallel-environments humanoid RL training on a single GPU — directly relevant to commercial claims on simulation-at-scale humanoid training pipelines (NVIDIA GR00T, Tesla Optimus, Figure 02 all use this paradigm); (2) URDF/USD-asset interoperability surface enabling cross-platform humanoid descriptors — relevant to claims on cross-platform humanoid descriptor IP; (3) the standardized RL task interface (gym-like API with vectorized environments) — relevant to claims on humanoid-task-curriculum IP; (4) integrated sensor simulation with domain randomization — relevant to claims on sim-to-real-via-randomization humanoid pipelines (anticipated already by OpenAI Dactyl 2018 but Isaac Lab provides the GPU-scale implementation). Mittal et al. RA-L 2023 paper has been cited >300 times by 2026 and underpins essentially every recent humanoid-RL publication. Modern sim-to-real-at-scale humanoid IP filings face this 3-year-deep open-source academic anchor.

## MuJoCo MJX (2023-08)

- **id**: `deepmind-mujoco-mjx-2023`
- **corpus**: academic
- **creator**: DeepMind / Google Research MuJoCo team (lead: Yuval Tassa, Tom Erez, with engineering contributions from Taylor Howell, Kevin Zakka, Erik Frey and the broader DeepMind robotics group; original MuJoCo by Emo Todorov)
- **disclosure**: DeepMind / Google Research MuJoCo team. 'MuJoCo MJX: A JAX implementation of the MuJoCo physics engine.' MuJoCo 3.0.0 release, August 2023; documented in MuJoCo 3.x documentation (https://mujoco.readthedocs.io/en/stable/mjx.html). Source code at https://github.com/google-deepmind/mujoco/tree/main/mjx. Originally MuJoCo: Todorov, Erez, and Tassa, 'MuJoCo: A physics engine for model-based control,' IEEE/RSJ IROS 2012, 5026-5033. Apache-2.0 license.
- **ip status**: open-permissive
- **prior art notes**: MuJoCo MJX (August 2023) is the canonical academic disclosure of GPU/TPU-parallelized differentiable physics simulation for robotics, published Apache-2.0 by DeepMind. Anticipates with full specificity: (1) gradient-based humanoid policy optimization through the simulator end-to-end — directly relevant to claims on differentiable-physics humanoid IP (NVIDIA GR00T, Genesis simulator, and several Tesla / Figure / 1X commercial pipelines use the same paradigm); (2) JAX vmap/pmap vectorized rollouts at >10,000 envs scale — relevant to claims on massively-parallel humanoid simulation pipelines; (3) soft-contact regularization for differentiability through contact — anticipates claims on smoothed-contact humanoid trajectory optimization; (4) MJCF as a vendor-neutral robot description format — anticipates claims on cross-vendor humanoid descriptors. The original MuJoCo (Todorov-Erez-Tassa IROS 2012) provides 14-year-deep prior art on the underlying physics; MJX adds 3-year-deep prior art on the GPU-differentiable port. Modern claims on differentiable simulation for humanoid training face this academic anchor.

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

## LeRobot (HuggingFace) (2024-03)

- **id**: `huggingface-lerobot-2024`
- **corpus**: academic
- **creator**: Remi Cadene and contributors; HuggingFace, Inc. (with extensive academic contributions from Stanford, CMU, NYU, MIT, IIIT-Hyderabad, ETH Zurich research groups via upstream policies)
- **disclosure**: Cadene, Remi et al. 'LeRobot: State-of-the-art AI for real-world robotics in PyTorch.' HuggingFace blog announcement and GitHub repository launch, March 13, 2024 (https://github.com/huggingface/lerobot). Cadene was previously a research engineer at Tesla AI / formerly at FAIR Paris before joining HuggingFace; the LeRobot framework consolidates open-source implementations of policies (ACT, Diffusion Policy, TDMPC, VQ-BeT, Pi0, SmolVLA) and datasets in a unified Apache-2.0 PyTorch substrate.
- **ip status**: open-permissive
- **prior art notes**: LeRobot (March 2024) is the canonical open-source unified framework for training and deploying imitation-learning and reinforcement-learning robot policies, published Apache-2.0 by HuggingFace. Anticipates with full architectural specificity: (1) multi-policy training and evaluation framework with a common interface — directly relevant to commercial claims on policy-architecture-agnostic VLA training pipelines (1X, Figure, Tesla Optimus, Genesis AI all build training pipelines that resemble this structure); (2) standardized dataset format for teleoperated demonstrations across heterogeneous embodiments (LeRobotDataset) — relevant to claims on cross-embodiment data unification, anticipating Open X-Embodiment-style aggregation patents; (3) the model-zoo pattern (pre-trained policy checkpoints downloadable via the HuggingFace Hub) — relevant to claims on commercial-grade pre-trained robot policy distribution; (4) real-robot inference on commodity hardware via PyTorch — relevant to claims on edge-deployable VLA systems. The Apache-2.0 license combined with extensive third-party contributions (Stanford Aloha team, Princeton Diffusion Policy, NYU/Cycle's TDMPC2, Physical Intelligence Pi0) makes this entry the consolidated prior art anchor for the entire 2024-2026 VLA-training-stack patent space. Modern VLA pipeline IP filings face this 2-year-deep anchor with full source disclosure.

## NVIDIA GR00T (Generalist Robot 00 Technology) (2024-03-18)

- **id**: `nvidia-groot-2024`
- **corpus**: academic
- **creator**: NVIDIA Research, GEAR Lab
- **disclosure**: Huang, Jensen et al. NVIDIA GR00T announcement at GTC 2024 keynote, March 18, 2024. Technical disclosure: Reddit Project GR00T technical blog, March 2024. GR00T N1 paper published 2025-03 (arXiv:2503.14734).
- **ip status**: open-permissive
- **prior art notes**: NVIDIA GR00T's 2024 disclosure is the canonical foundation-model-for-humanoids announcement. Anticipates: (1) dual-system fast/slow policy architecture for humanoid platforms — directly relevant to modern humanoid foundation-model IP (every major humanoid manufacturer is developing equivalent architectures); (2) cross-embodiment generalization across multiple humanoid platforms — relevant to platform-agnostic policy IP; (3) open-weights humanoid foundation model release — provides defensive baseline against closed-weights claims. The March 2024 GTC keynote announcement plus the subsequent GR00T N1 paper (March 2025) and open-weights release provide extensive prior art coverage.

## Berkeley Humanoid (2024-07)

- **id**: `berkeley-humanoid-2024`
- **corpus**: academic
- **creator**: UC Berkeley Hybrid Robotics Lab; Liao, Zhang, X. Huang, X. Huang, Li, Sreenath
- **disclosure**: Liao, Q., Zhang, B., Huang, X., Huang, X., Li, Z., Sreenath, K. 'Berkeley Humanoid: A Research Platform for Learning-based Control'. arXiv:2407.21781, July 2024. IEEE International Conference on Robotics and Automation (ICRA) 2025. UC Berkeley Hybrid Robotics Lab.
- **ip status**: open-permissive
- **prior art notes**: Berkeley Humanoid is the open academic mid-scale bipedal humanoid research platform from the Sreenath group, ICRA 2025. Open-permissive. Establishes 1-year-deep prior art for: RL-trained locomotion with sim-to-real zero-shot transfer at humanoid scale, low-cost in-house-built humanoid for learning research, anthropomorphic kinematics optimized for sim-to-real. Direct shielding for free-humanoid-platform commitments on bipedal RL locomotion and any commercial humanoid claim on RL-trained outdoor walking. Parent of Berkeley Humanoid Lite (round-11 entry below).

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

## Genesis (open-source physics simulator) (2024-12)

- **id**: `genesis-embodied-ai-simulator`
- **corpus**: open
- **creator**: Genesis Authors collaboration (multi-institution: CMU, Stanford, MIT CSAIL, Tsinghua, Peking, ETH Zürich, UMD, et al.)
- **disclosure**: Genesis Authors. 'Genesis: A Generative and Universal Physics Engine for Robotics and Beyond'. GitHub release at https://github.com/Genesis-Embodied-AI/Genesis, December 19, 2024. Multi-institution collaboration including Carnegie Mellon University, Stanford University, MIT CSAIL, Tsinghua University, Peking University, ETH Zürich, University of Maryland.
- **ip status**: open-permissive
- **prior art notes**: The Genesis simulator (Genesis-Embodied-AI/Genesis, December 2024) is the most recent and highest-throughput academic-grade open-source physics engine for robotics simulation, published Apache-2.0 by a multi-institution academic collaboration. Anticipates with full architectural specificity: (1) GPU-parallelized robotics simulation at 43M-FPS scale — directly relevant to commercial claims on sim-to-real-at-scale humanoid IP (notably Genesis AI Inc.'s GENE-26.5 product, with which this open-source project shares a name); (2) unified multi-physics architecture (rigid + soft + MPM + FEM + fluid) — relevant to claims on multi-domain humanoid simulation; (3) differentiable simulation for gradient-based policy optimization — relevant to claims on policy-gradient humanoid training at scale; (4) the URDF/MJCF interoperability surface that permits OpenLoco-class descriptors to be simulated without modification. Modern claims on sim-to-real-at-scale, multi-physics simulation, or differentiable physics for humanoid training all face this 1.5-year-deep open-source academic prior art with full source disclosure under Apache-2.0.

## ToddlerBot (2025-02)

- **id**: `stanford-toddlerbot-2025`
- **corpus**: academic
- **creator**: Stanford Robotics Lab; Haochen Shi, Weizhuo Wang, Shuran Song, C. Karen Liu
- **disclosure**: Shi, H., Wang, W., Song, S., Liu, C. K. 'ToddlerBot: Open-Source ML-Compatible Humanoid Platform for Loco-Manipulation'. arXiv:2502.00893, February 2025. Conference on Robot Learning (CoRL) 2025 oral. Stanford Robotics Lab.
- **ip status**: open-permissive
- **prior art notes**: ToddlerBot is Stanford's canonical sub-$6k open-hardware ML-compatible humanoid (CoRL 2025 oral). Establishes 1-year-deep open-academic prior art for: integrated loco-manipulation policy training on an open humanoid platform, transferable motor system-ID for sim-to-real without hand-tuning, 30-DoF anthropomorphic full-body at sub-$6k. Direct shielding for any commercial claim on integrated full-body humanoid policy training, particularly any 'one policy controls the whole body' claim. Together with Berkeley Humanoid Lite, establishes the open-academic baseline for sub-$10k humanoid robotics.

## Berkeley Humanoid Lite (2025-04)

- **id**: `berkeley-humanoid-lite-2025`
- **corpus**: academic
- **creator**: UC Berkeley Hybrid Robotics Lab; Sreenath group
- **disclosure**: Cui, F., Sayle, J., Karydis, K., Liao, Q., et al. 'Demonstrating Berkeley Humanoid Lite: An Open-source, Accessible, and Customizable 3D-printed Humanoid Robot'. arXiv:2504.17249, April 2025. Robotics: Science and Systems (RSS) 2025. UC Berkeley Hybrid Robotics Lab.
- **ip status**: open-permissive
- **prior art notes**: Berkeley Humanoid Lite is the canonical sub-$5k open-hardware academic bipedal humanoid (RSS 2025). 1-year-deep prior art on: 3D-printed cycloidal reducer humanoid actuator (a specific architectural commitment), full open-source release of hardware + firmware + training, sub-$5k humanoid BOM, RL-controlled walking on a 3D-printed platform. **Direct shielding for free-humanoid-platform** — particularly the 3D-printed actuator path and any commercial claim on accessible humanoid hardware. Together with ToddlerBot and Berkeley Humanoid (full-size), establishes a deep open-academic substrate for any commercial humanoid platform claim.

## Genesis AI GENE-26.5 (2026-04)

- **id**: `genesis-ai-gene-26-5`
- **corpus**: private
- **creator**: Genesis AI Inc.
- **disclosure**: Genesis AI Inc. corporate website at https://www.genesis.ai/, GENE-26.5 product page (April 2026 surface). Demo videos showing cooking, lab pipetting, beverage preparation, puzzle-solving, object manipulation, assembly, and fine-motor tasks.
- **ip status**: trade-secret
- **prior art notes**: Genesis AI's GENE-26.5 platform is a closed-source commercial robotics product whose public disclosure surface (corporate website + demo videos) does not reveal specific mechanism. The capability set claimed — multi-task vision-language-action manipulation, sim-to-real generalization, dexterous fine-motor — is fully covered by deep open academic prior art chains in the corpus: Pomerleau ALVINN (1989) → Levine GPS PR2/BRETT (2016) for end-to-end visuomotor policy; CLIP (Radford 2021) for vision-language alignment; RT-1 (2022), RT-2 (2023), Open X-Embodiment (2023), OpenVLA (2024), π-zero (2024), NVIDIA GR00T N1 (2025) for VLA architecture; OpenAI Dactyl (2018-2019), Hwangbo ANYmal sim-to-real (2019), Tan quadruped sim-to-real (2018) for sim-to-real; Mobile ALOHA (2024), ACT/ALOHA (2023), Diffusion Policy (2023) for bimanual fine manipulation; Salisbury Stanford-JPL hand (1982), DLR Hand-II (2001), Shadow Hand (2002), Pisa-IIT SoftHand (2014) for dexterous hand mechanism; Park's transformation (1929) for any FOC actuator control. Claims that GENE represents novel art in any of these subsystems face element-by-element prior art at depths from 4 years (Diffusion Policy) to 97 years (Park) to 530 years (Da Vinci's Knight, anthropomorphic tendon-driven hand). Demo task set (cooking, beverage preparation, lab manipulation) maps directly to Mobile ALOHA (2024), DLR Justin (2009), CMU HERB (2012), and the PR2 lineage.
