---
title: "control-imitation-learning"
parent: "Invalidity Contentions"
nav_order: 55
layout: default
---

# Invalidity Contention Packet — `control-imitation-learning`

**Generated:** 2026-05-09  
**Cross-cut tag:** `control-imitation-learning`  
**Entries:** 24 (23 commons-grade, 1 draft)  
**Earliest disclosure:** 2018-04  
**Most recent disclosure:** 2025-11

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-imitation-learning`.

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

### 2018-04 — DeepMimic

- **id:** `deepmimic-peng-siggraph-2018`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** UC Berkeley + UBC; Xue Bin (Jason) Peng, Pieter Abbeel, Sergey Levine, Michiel van de Panne
- **disclosure citation:** Peng, X. B., Abbeel, P., Levine, S., van de Panne, M. 'DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills'. ACM Transactions on Graphics 37(4) 2018 (SIGGRAPH 2018). arXiv:1804.02717. UC Berkeley + UBC.
- **disclosed subsystems:** `control-rl-policy`, `control-imitation-learning`, `control-motion-capture-imitation`, `control-physics-based-animation`

**Prior art notes:**

> DeepMimic (Peng et al. SIGGRAPH 2018) is the canonical foundational motion-capture-imitation deep-RL framework. 7-year-deep open-permissive prior art for: deep-RL imitation of motion-capture references, physics-based character animation via RL, complex acrobatic skill (backflip, spin) RL training. **The architectural ancestor of**: Adversarial Motion Priors (round-21 entry below), ASE (Peng et al. 2022), the entire humanoid-from-mocap-data line. Direct shielding for any commercial humanoid claim on motion-capture-trained policies (Tesla Optimus, Figure Helix demos all use mocap-style imitation; this is 7-year-deep prior art).

**Sources:**

1. Peng, X. B. et al. ACM TOG 37(4) 2018; arXiv:1804.02717.
2. Project page (xbpeng.github.io/projects/DeepMimic).
3. BAIR open-source release (github.com/xbpeng/DeepMimic).

---

### 2019-09 — RLBench

- **id:** `rlbench-james-2019`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Imperial College London Dyson Robotics Lab; Stephen James, Andrew Davison
- **disclosure citation:** James, S., Ma, Z., Arrojo, D. R., Davison, A. J. 'RLBench: The Robot Learning Benchmark & Learning Environment'. IEEE Robotics and Automation Letters 5(2) 2020. arXiv:1909.12271. Imperial College London Dyson Robotics Lab.
- **disclosed subsystems:** `control-imitation-learning`, `control-rl-policy`, `control-benchmarking`

**Prior art notes:**

> RLBench is the foundational academic robot manipulation benchmark (James et al. RA-L 2019). 6-year-deep open-permissive prior art. The conceptual ancestor of robomimic (round-16, 2021), Meta-World (2019), LIBERO (round-17, 2023), RoboCasa (round-16, 2024), SimplerEnv (round-17, 2024). Direct shielding for any commercial humanoid manipulation-benchmark claim. Particularly relevant because RLBench tasks have been re-implemented across multiple simulators (CoppeliaSim, MuJoCo, Isaac Gym) — establishing that the task-design itself, not the simulator, is the prior art.

**Sources:**

1. James et al. arXiv:1909.12271 IEEE RA-L 2020.
2. Project page (sites.google.com/view/rlbench).
3. GitHub: github.com/stepjam/RLBench.

---

### 2021-04 — Adversarial Motion Priors (AMP)

- **id:** `amp-peng-siggraph-2021`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** UC Berkeley; Xue Bin (Jason) Peng, Ze Ma, Pieter Abbeel, Sergey Levine, Angjoo Kanazawa
- **disclosure citation:** Peng, X. B., Ma, Z., Abbeel, P., Levine, S., Kanazawa, A. 'AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control'. ACM Transactions on Graphics 40(4) 2021 (SIGGRAPH 2021). arXiv:2104.02180. UC Berkeley.
- **disclosed subsystems:** `control-rl-policy`, `control-imitation-learning`, `control-motion-capture-imitation`, `control-adversarial-style-distillation`

**Prior art notes:**

> Adversarial Motion Priors (Peng et al. SIGGRAPH 2021) is the canonical extension of DeepMimic to GAN-style latent-space motion imitation. 4-year-deep open-permissive prior art for: GAN-distilled motion priors, latent-space mocap style imitation, task-conditioned style-aware humanoid RL. **The architectural ancestor of contemporary humanoid-from-mocap RL** including ASE (Peng et al. 2022), HumanPlus (Stanford 2024), ExBody (Stanford 2024), H1 / G1 humanoid policies (Unitree). Direct shielding for any commercial humanoid claim on 'humanoid moves like a human' style-aware locomotion.

**Sources:**

1. Peng, X. B. et al. ACM TOG 40(4) 2021; arXiv:2104.02180.
2. Project page (xbpeng.github.io/projects/AMP).
3. GitHub: github.com/xbpeng/DeepMimic (AMP integrated).

---

### 2021-08 — robomimic

- **id:** `robomimic-mandlekar-2021`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Stanford + UT Austin; Ajay Mandlekar, Yuke Zhu, Roberto Martín-Martín, Fei-Fei Li, Silvio Savarese et al.
- **disclosure citation:** Mandlekar, A., Xu, D., Wong, J., Nasiriany, S., Wang, C., Kulkarni, R., Fei-Fei, L., Savarese, S., Zhu, Y., Martín-Martín, R. 'What Matters in Learning from Offline Human Demonstrations for Robot Manipulation'. CoRL 2021; arXiv:2108.03298. Stanford + UT Austin. MIT-licensed framework.
- **disclosed subsystems:** `control-imitation-learning`, `control-foundation-model-policy`, `control-benchmarking`

**Prior art notes:**

> robomimic is the canonical IL benchmark + framework (Mandlekar et al. CoRL 2021). 4-year-deep open-permissive prior art for: standardized imitation-learning datasets + reference algorithms for robotic manipulation. Direct shielding for any commercial humanoid claim on IL training infrastructure. Together with RoboCasa (round-16 entry), Octo (round-15), OpenVLA (round-12), establishes the open-academic IL substrate against which all commercial VLA performance must be measured.

**Sources:**

1. Mandlekar et al. CoRL 2021; arXiv:2108.03298.
2. Project page (robomimic.github.io).
3. GitHub: github.com/ARISE-Initiative/robomimic.

---

### 2021-08 — DexMV (Dexterous Manipulation from Videos)

- **id:** `dexmv-qin-cvpr-2022`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** UCSD; Yuzhe Qin, Hao Su, Xiaolong Wang
- **disclosure citation:** Qin, Y., Su, H., Wang, X. 'DexMV: Imitation Learning for Dexterous Manipulation from Human Videos'. ECCV 2022 (also accepted at earlier 2021 venues). arXiv:2108.05877. UC San Diego.
- **disclosed subsystems:** `control-imitation-learning`, `control-egocentric-video-pretraining`, `mechanism-anthropomorphic-hand`

**Prior art notes:**

> DexMV is the canonical academic dexterous-manipulation-from-human-videos system (Qin et al. ECCV 2022). 3-year-deep open-permissive prior art for: training robot manipulation policies directly from in-the-wild human videos, hand-pose retargeting from human to robot. **Direct conceptual ancestor of NVIDIA GR00T N1's 20K-hour EgoScale egocentric-video pre-training** (round-15 entry). Direct shielding for any commercial humanoid claim on 'we trained on YouTube videos' or 'egocentric-video-based policy pretraining'.

**Sources:**

1. Qin et al. arXiv:2108.05877 ECCV 2022.
2. Project page (yzqin.github.io/dexmv).

---

### 2021-12 — CALVIN

- **id:** `calvin-mees-2022`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** University of Freiburg AIS Lab; Oier Mees, Lukas Hermann, Wolfram Burgard
- **disclosure citation:** Mees, O., Hermann, L., Rosete-Beas, E., Burgard, W. 'CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks'. IEEE Robotics and Automation Letters 7(3) 2022. arXiv:2112.03227. University of Freiburg.
- **disclosed subsystems:** `control-language-conditioned-policy`, `control-imitation-learning`, `control-long-horizon-manipulation`, `control-benchmarking`

**Prior art notes:**

> CALVIN is the canonical long-horizon language-conditioned manipulation benchmark (Mees + Burgard Freiburg, RA-L 2022). 4-year-deep open-permissive prior art for: language-conditioned robot manipulation benchmark, teleoperated 'play data' as training distribution, hour-scale unstructured play datasets for language grounding. Direct shielding for any commercial humanoid claim on language-conditioned manipulation training data + benchmarks. Together with LIBERO (round-17), RoboCasa (round-16), robomimic (round-16), establishes the language-conditioned-VLA evaluation substrate.

**Sources:**

1. Mees et al. arXiv:2112.03227 IEEE RA-L 2022.
2. Project page (calvin.cs.uni-freiburg.de).
3. GitHub: github.com/mees/calvin.

---

### 2021-12 — BC-Z

- **id:** `bc-z-jang-2021`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Google Research + Stanford + Everyday Robots; Eric Jang, Sergey Levine, Chelsea Finn et al.
- **disclosure citation:** Jang, E., Irpan, A., Khansari, M., Kappler, D., Ebert, F., Lynch, C., Levine, S., Finn, C. 'BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning'. CoRL 2021. arXiv:2202.02005. Google Research + Stanford + Everyday Robots.
- **disclosed subsystems:** `control-imitation-learning`, `control-language-conditioned-policy`, `control-foundation-model-policy`

**Prior art notes:**

> BC-Z (Jang et al. CoRL 2021) is the foundational language-conditioned manipulation policy paper at Google scale. 4-year-deep public-domain prior art. **Direct architectural ancestor of RT-1** (corpus entry) which transformerized BC-Z's framework. Established the 'large-scale demonstrations + language conditioning' pattern that the entire RT-X lineage descends from. Direct shielding for any commercial humanoid VLA claim on 'large-scale teleop + language conditioning'.

**Sources:**

1. Jang et al. arXiv:2202.02005 CoRL 2021.
2. Project page (sites.google.com/view/bc-z).

---

### 2022-04 — Adversarial Skill Embeddings (ASE)

- **id:** `ase-peng-stanford-2022`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** NVIDIA + Stanford + UC Berkeley + University of Toronto; Xue Bin Peng et al.
- **disclosure citation:** Peng, X. B., Guo, Y., Halper, L., Levine, S., Fidler, S. 'ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters'. ACM Transactions on Graphics 41(4) 2022 (SIGGRAPH 2022). arXiv:2205.01906. NVIDIA + Stanford + UC Berkeley + University of Toronto.
- **disclosed subsystems:** `control-rl-policy`, `control-imitation-learning`, `control-motion-capture-imitation`, `control-latent-skill-embedding`

**Prior art notes:**

> ASE (Peng et al. SIGGRAPH 2022) is the canonical successor to AMP (round-21). 3-year-deep open-permissive prior art for: latent-skill-space adversarial-training for character animation, task-conditioned skill reuse. **Direct ancestor of HumanPlus + ExBody humanoid imitation policies** (round-27 entries below). Together with DeepMimic (round-21) + AMP (round-21), establishes the 7-year mocap-imitation-RL chain DeepMimic 2018 → AMP 2021 → ASE 2022 → HumanPlus 2024 → ExBody 2024.

**Sources:**

1. Peng et al. arXiv:2205.01906 SIGGRAPH 2022.
2. GitHub: github.com/nv-tlabs/ASE.

---

### 2023-05 — FurnitureBench

- **id:** `furniturebench-heo-rss-2023`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** KAIST + USC; Minho Heo, Youngwoon Lee, Doohyun Lee, Joseph J. Lim
- **disclosure citation:** Heo, M., Lee, Y., Lee, D., Lim, J. J. 'FurnitureBench: Reproducible Real-World Benchmark for Long-Horizon Complex Manipulation'. RSS 2023. arXiv:2305.12821. KAIST + USC.
- **disclosed subsystems:** `control-imitation-learning`, `control-long-horizon-manipulation`, `control-benchmarking`, `control-assembly-task`

**Prior art notes:**

> FurnitureBench is the canonical real-world long-horizon manipulation benchmark (Heo et al. RSS 2023). 2-year-deep open-permissive prior art for: furniture-assembly real-robot benchmark, fiducial-based standardization for cross-lab reproducibility. Distinct architectural branch from sim-only benchmarks: FurnitureBench is real-robot, while RLBench/robomimic/LIBERO/RoboCasa are simulated. Direct shielding for any commercial humanoid claim on furniture-assembly or long-horizon real-world benchmark performance.

**Sources:**

1. Heo et al. arXiv:2305.12821 RSS 2023.
2. Project page (clvrai.github.io/furniture-bench).
3. GitHub: github.com/clvrai/furniture-bench.

---

### 2023-06 — LIBERO (Lifelong Robot Learning Benchmark)

- **id:** `libero-liu-neurips-2023`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** UT Austin + Bytedance Research; Bo Liu, Yifeng Zhu, Yuke Zhu, Peter Stone et al.
- **disclosure citation:** Liu, B., Zhu, Y., Gao, C., Feng, Y., Liu, Q., Zhu, Y., Stone, P. 'LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning'. NeurIPS 2023 Track on Datasets and Benchmarks. arXiv:2306.03310. UT Austin + Bytedance Research.
- **disclosed subsystems:** `control-imitation-learning`, `control-benchmarking`, `control-lifelong-learning`

**Prior art notes:**

> LIBERO is the canonical lifelong-robot-learning benchmark (Liu et al. NeurIPS 2023). 2-year-deep prior art on the benchmark surface that **OpenVLA-OFT (round-12), π₀ (round-12), RDT-1B (round-13), and most contemporary VLA papers report results against**. Any commercial humanoid VLA claim of 'we outperform X% on LIBERO' implies the LIBERO benchmark itself is reproducible academic art — that benchmark's 130 tasks plus extendible generation pipeline are 100% open-permissive prior art. Together with robomimic (round-16) and SimplerEnv (round-17 entry), establishes the open-academic VLA evaluation substrate.

**Sources:**

1. Liu et al. arXiv:2306.03310 NeurIPS 2023.
2. Project page (libero-project.github.io).
3. GitHub: github.com/Lifelong-Robot-Learning/LIBERO.

---

### 2023-10 — RT-X / Open X-Embodiment collaboration paper

- **id:** `rt-x-collaboration-2023`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Open X-Embodiment Collaboration (21 institutions, 100+ co-authors)
- **disclosure citation:** Open X-Embodiment Collaboration et al. 'Open X-Embodiment: Robotic Learning Datasets and RT-X Models'. ICRA 2024. arXiv:2310.08864. Cross-institutional collaboration spanning 21 institutions (Google DeepMind, Stanford, UC Berkeley, MIT, CMU, Columbia, NYU, Toyota Research Institute, Imperial College, ETH Zürich, Tokyo Tech, et al.). The paper introducing the dataset now in the corpus as `open-x-embodiment`.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-cross-embodiment`, `control-foundation-model-policy`, `control-imitation-learning`

**Prior art notes:**

> RT-X / Open X-Embodiment collaboration (ICRA 2024) is the canonical 21-institution cross-embodiment VLA collaboration. 1.5-year-deep open-permissive prior art for: publicly-coordinated cross-institutional robot dataset pool, cross-embodiment VLA training methodology, RT-1-X / RT-2-X cross-embodiment models. Direct shielding for any commercial humanoid claim on cross-embodiment VLA training. **The collaboration model itself is novel art** — establishes that open multi-institution dataset pooling for robot learning is well-anticipated public-domain academic practice. Distinct from the dataset entry (`open-x-embodiment` already in corpus) by emphasis on the model-training + collaboration-pattern artifacts.

**Sources:**

1. Open X-Embodiment Collaboration arXiv:2310.08864 ICRA 2024.
2. Project page (robotics-transformer-x.github.io).
3. Open X-Embodiment dataset (robotics-transformer-x.github.io/data).

---

### 2023-11 — RoboFlamingo *(draft)*

- **id:** `roboflamingo-baai-tsinghua-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** BAAI + ByteDance + Tsinghua; Xinghang Li, Tao Kong et al.
- **disclosure citation:** Li, X., Liu, M., Zhang, H., Yu, C., Xu, J., Wu, H., Cheang, C., Jing, Y., Zhang, W., Liu, H., Li, H., Kong, T. 'Vision-Language Foundation Models as Effective Robot Imitators'. ICLR 2024. arXiv:2311.01378. Beijing Academy of Artificial Intelligence (BAAI) + ByteDance + Tsinghua.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-foundation-model-policy`, `control-imitation-learning`

**Prior art notes:**

> RoboFlamingo (Li et al. ICLR 2024) is the canonical Chinese open-source VLM-based VLA. 1.5-year-deep open-permissive prior art. Demonstrates the **frozen-VLM + lightweight-policy paradigm** as an alternative to full VLA fine-tuning (OpenVLA round-12). Direct shielding for any commercial humanoid VLA claim on frozen-foundation-model + light-policy-head architecture.

**Sources:**

1. Li et al. arXiv:2311.01378 ICLR 2024.
2. Project page (roboflamingo.github.io).
3. GitHub: github.com/RoboFlamingo/RoboFlamingo.

---

### 2024-03 — 3D Diffusion Policy (DP3)

- **id:** `dp3-ze-rss-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Stanford + Tsinghua + CMU; Yanjie Ze, Hao Xu, et al.
- **disclosure citation:** Ze, Y., Zhang, G., Zhang, K., Hu, C., Wang, M., Xu, H. '3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations'. RSS 2024. arXiv:2403.03954. Stanford + Tsinghua + CMU.
- **disclosed subsystems:** `control-imitation-learning`, `control-diffusion-policy`, `control-3d-perception`, `control-cross-embodiment`

**Prior art notes:**

> 3D Diffusion Policy (Ze et al. RSS 2024) is the canonical 3D extension of Chi/Song's Diffusion Policy (corpus entry). 1-year-deep open-permissive prior art for: 3D-input diffusion-policy for manipulation, point-cloud-conditioned action generation. Direct shielding for any commercial humanoid claim on 3D-perception-conditioned manipulation policies. Together with Diffusion Policy, RDT-1B (diffusion VLA), and Octo (transformer + diffusion-head), establishes the diffusion-policy family that shields commercial diffusion-VLA claims.

**Sources:**

1. Ze et al. arXiv:2403.03954 RSS 2024.
2. Project page (3d-diffusion-policy.github.io).
3. GitHub: github.com/YanjieZe/3D-Diffusion-Policy.

---

### 2024-04 — Astribot S1

- **id:** `astribot-s1-stardust-2025`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Stardust Intelligence (Shenzhen, China)
- **disclosure citation:** Stardust Intelligence (Shenzhen, China; founded December 2022). Astribot S1 reveal April 2024 via stardust-tech.com / astribot.com demo videos showing 10 m/s arm motion. Stardust Intelligence Astribot Suite paper July 2025 (peer-reviewed; teleop + DuoCore-WB imitation learning achieving 80% task success). Commercial availability late 2025+ in China.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-arm`, `actuator-electric`, `control-imitation-learning`, `control-foundation-model-policy`

**Prior art notes:**

> Astribot S1 is one of the canonical 2024-2025 Chinese commercial humanoid platforms (Stardust Intelligence). 1.5-year-deep public-disclosure prior art for: ≥10 m/s anthropomorphic arm motion (claimed industry-leading), 36-DoF whole-body humanoid, DuoCore-WB whole-body IL framework. Direct shielding for any commercial humanoid claim on extreme arm-speed performance — Astribot's April 2024 viral demo set the public benchmark. Claim surface is peer-reviewed (Astribot Suite paper July 2025), unlike most Chinese commercial humanoid platforms.

**Sources:**

1. Stardust Intelligence corporate site (stardust-tech.com / astribot.com).
2. Astribot Suite paper July 2025 (peer-reviewed; venue TBV).
3. Humanoid Press product database (humanoid.press/database/database-astribot-s1).
4. Origin of Bots, RobotsLATAM, Mike Kalil coverage 2024-2026.

---

### 2024-05 — Octo (Open-Source Generalist Robot Policy)

- **id:** `octo-rss-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Octo Model Team (UC Berkeley + Stanford + CMU + Google DeepMind); Levine + Finn + Sadigh group lineage
- **disclosure citation:** Octo Model Team: Ghosh, D., Walke, H., Pertsch, K., Black, K., Mees, O., Dasari, S., Hejna, J., Kreiman, T., Xu, C., Luo, J., Tan, Y. L., Sanketi, P., Vuong, Q., Xiao, T., Sadigh, D., Finn, C., Levine, S. 'Octo: An Open-Source Generalist Robot Policy'. arXiv:2405.12213, May 2024. Robotics: Science and Systems (RSS) 2024. UC Berkeley + Stanford + Carnegie Mellon + Google DeepMind.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-foundation-model-policy`, `control-diffusion-policy`, `control-cross-embodiment`, `control-imitation-learning`

**Prior art notes:**

> Octo is the canonical first open-source generalist robot policy. 1-year-deep open-permissive academic prior art predating OpenVLA by ~1 month (RSS May 2024 vs OpenVLA arXiv June 2024). Establishes the architectural pattern for: transformer + diffusion-policy action head, Open-X-Embodiment-trained cross-embodiment policy at 27M-93M parameter scale, language-OR-goal-image conditioning. Direct shielding for any commercial humanoid VLA claim on diffusion-policy action heads (RDT-1B, π₀ both build on this) and on Open-X-Embodiment-trained cross-embodiment foundation. Together with OpenVLA, π₀, π₀.₅, OpenVLA-OFT, and RDT-1B, establishes the open academic VLA baseline against which Figure Helix, NVIDIA GR00T N1, Microsoft Magma, and any closed commercial VLA must be evaluated.

**Sources:**

1. Octo Model Team. arXiv:2405.12213 May 2024.
2. RSS 2024 proceedings (roboticsproceedings.org/rss20/p090.pdf).
3. Project page (octo-models.github.io).
4. GitHub: github.com/octo-models/octo.

---

### 2024-06 — OpenVLA

- **id:** `openvla-stanford-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Stanford + Toyota Research Institute + UC Berkeley; Kim, Pertsch, Karamcheti, Liang, Finn, Levine, Tedrake et al.
- **disclosure citation:** Kim, M. J., Pertsch, K., Karamcheti, S., Xiao, T., Balakrishna, A., Nair, S., Rafailov, R., Foster, E., Lam, G., Sanketi, P., Vuong, Q., Kollar, T., Burchfiel, B., Tedrake, R., Sadigh, D., Levine, S., Liang, P., Finn, C. 'OpenVLA: An Open-Source Vision-Language-Action Model'. arXiv:2406.09246, June 2024. CoRL 2024 (PMLR v270, Kim25c). Stanford + Toyota Research Institute + UC Berkeley.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-foundation-model-policy`, `control-imitation-learning`, `control-cross-embodiment`

**Prior art notes:**

> OpenVLA is the canonical first fully-open-source VLA foundation model (CoRL 2024). 23-month-deep open-permissive academic prior art for: 7B-class open-weight VLA, Llama-2-based VLA backbone, Open-X-Embodiment-trained cross-embodiment policy. Direct shielding for any commercial humanoid VLA claim on open-source-equivalent architectural elements. Together with π₀ and π₀.₅, establishes the open-academic VLA baseline against which all closed commercial VLAs (Tesla Optimus, Figure, 1X NEO) must be evaluated.

**Sources:**

1. Kim et al. arXiv:2406.09246 June 2024.
2. CoRL 2024 PMLR v270 Kim25c (proceedings.mlr.press/v270/kim25c.html).
3. OpenVLA project page (openvla.github.io).
4. GitHub: github.com/openvla/openvla.

---

### 2024-06 — RoboCasa

- **id:** `robocasa-nasiriany-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** UT Austin + NVIDIA; Soroush Nasiriany, Abhinav Maddukuri, Yuke Zhu et al.
- **disclosure citation:** Nasiriany, S., Maddukuri, A., Zhang, L., Parikh, A., Lo, A., Joshi, A., Mandlekar, A., Zhu, Y. 'RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots'. arXiv:2406.02523, June 2024. RSS 2024. UT Austin + NVIDIA. RoboCasa365 follow-up (OpenReview tQJYKwc3n4) extends to 365 tasks across 2,500 kitchen environments.
- **disclosed subsystems:** `control-physics-simulation`, `control-imitation-learning`, `control-foundation-model-policy`, `control-loco-manipulation`

**Prior art notes:**

> RoboCasa is the canonical generative-AI-augmented household-task simulation framework (UT Austin + NVIDIA, RSS 2024). ~1-year-deep open-permissive prior art for: generative-AI-authored simulation environments at scale, large-scale (>1k hours) demonstration datasets for VLA training, kitchen-scene household-task benchmark suite. Direct shielding for any commercial humanoid claim on 'training data at scale for household manipulation' — RoboCasa365's 1,600 synthetic + 600 human hours establishes the open-academic baseline.

**Sources:**

1. Nasiriany et al. arXiv:2406.02523 June 2024.
2. Project page (robocasa.ai).
3. GitHub: github.com/robocasa/robocasa.
4. RSS 2024 proceedings (robocasa.ai/assets/robocasa_rss24.pdf).

---

### 2024-06 — HumanPlus humanoid

- **id:** `humanplus-stanford-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Stanford University; Zipeng Fu, Qingqing Zhao, Qi Wu, Gordon Wetzstein, Chelsea Finn
- **disclosure citation:** Fu, Z., Zhao, Q., Wu, Q., Wetzstein, G., Finn, C. 'HumanPlus: Humanoid Shadowing and Imitation from Humans'. CoRL 2024. arXiv:2406.10454. Stanford University.
- **disclosed subsystems:** `control-rl-policy`, `control-imitation-learning`, `control-motion-capture-imitation`, `control-humanoid-shadowing`

**Prior art notes:**

> HumanPlus (Fu et al. CoRL 2024) is the canonical Stanford humanoid-imitation-from-humans paper. 1-year-deep open-permissive prior art for: two-stage RL-shadowing + IL fine-tuning, real-hardware humanoid full-body imitation from human motion. Direct architectural application of AMP/ASE lineage (rounds 21+27) to actual humanoid hardware. Direct shielding for any commercial humanoid claim on 'humanoid imitates humans' or 'mocap-trained humanoid policy on real hardware'.

**Sources:**

1. Fu et al. arXiv:2406.10454 CoRL 2024.
2. Project page (humanoid-shadowing.github.io).
3. GitHub: github.com/MarkFzp/humanplus.

---

### 2024-09 — MaskedMimic

- **id:** `maskedmimic-tessler-stanford-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** NVIDIA Research + Stanford; Chen Tessler, Yunrong Guo, Ofir Nabati, Gal Chechik, Xue Bin Peng
- **disclosure citation:** Tessler, C., Guo, Y., Nabati, O., Chechik, G., Peng, X. B. 'MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting'. SIGGRAPH Asia 2024. arXiv:2409.14393. NVIDIA Research + Stanford.
- **disclosed subsystems:** `control-rl-policy`, `control-imitation-learning`, `control-motion-capture-imitation`, `control-masked-motion-inpainting`

**Prior art notes:**

> MaskedMimic (Tessler + Peng SIGGRAPH Asia 2024) is the architectural successor to AMP + ASE for physics-based character control. 1-year-deep open-permissive prior art. Continues the DeepMimic 2018 → AMP 2021 → ASE 2022 → MaskedMimic 2024 chain. Direct shielding for any commercial humanoid claim on masked-token motion-inpainting or unified-conditioning character control.

**Sources:**

1. Tessler et al. arXiv:2409.14393 SIGGRAPH Asia 2024.
2. GitHub: github.com/NVIDIA-Omniverse/IsaacGymEnvs (MaskedMimic implementation).

---

### 2024-10 — π₀ (Pi-Zero)

- **id:** `physical-intelligence-pi0-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Physical Intelligence; Black, Brown, Driess, Finn et al.
- **disclosure citation:** Black, K., Brown, N., Driess, D., Esmail, A., Equi, M., Finn, C., et al. 'π₀: A Vision-Language-Action Flow Model for General Robot Control'. arXiv:2410.24164, October 2024. Physical Intelligence (physicalintelligence.company).
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-flow-matching`, `control-foundation-model-policy`, `control-imitation-learning`

**Prior art notes:**

> π₀ is Physical Intelligence's canonical first VLA foundation policy (Oct 2024). 1.5-year-deep open-academic publication. Establishes architectural prior art for: flow-matching action distribution in VLA, cross-embodiment policy pretraining, single foundation model controlling multiple robot platforms. Direct successor lineage from RT-1 (2022), RT-2 (2023), OpenVLA (2024). Direct shielding for any commercial humanoid claim on VLA-based control (Tesla Optimus, Figure, 1X NEO, Apptronik all face this); particularly for any claim on flow-matching action heads or cross-embodiment pretraining.

**Sources:**

1. Black et al. arXiv:2410.24164 October 2024.
2. Physical Intelligence pi0 paper (physicalintelligence.company/download/pi0.pdf).
3. Physical Intelligence company page (physicalintelligence.company).

---

### 2024-10 — RDT-1B (Robotics Diffusion Transformer)

- **id:** `rdt-1b-thu-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Tsinghua TSAIL (THU-ML); Songming Liu et al.
- **disclosure citation:** Liu, S., et al. 'RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation'. arXiv:2410.07864, October 2024. ICLR 2025. Tsinghua TSAIL (THU-ML) lab.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-foundation-model-policy`, `control-diffusion-policy`, `control-imitation-learning`, `control-bimanual-manipulation`

**Prior art notes:**

> RDT-1B is THU-ML's canonical diffusion-based VLA foundation model for bimanual manipulation (ICLR 2025). 7-month-deep open-permissive prior art for: diffusion-formulation VLA at billion-parameter scale, bimanual manipulation foundation policy, multi-robot pre-training corpus. The canonical Chinese-academy entry in the open-weight VLA race alongside Stanford OpenVLA and Physical Intelligence π₀. Directly cited as a comparison baseline in OpenVLA-OFT (round-12); now resolves correctly. Direct shielding for any commercial humanoid claim on diffusion-based bimanual VLA.

**Sources:**

1. Liu et al. arXiv:2410.07864 October 2024.
2. Project page (rdt-robotics.github.io/rdt-robotics).
3. GitHub: github.com/thu-ml/RoboticsDiffusionTransformer.
4. HuggingFace: huggingface.co/robotics-diffusion-transformer/rdt-1b.

---

### 2025-02 — ToddlerBot

- **id:** `stanford-toddlerbot-2025`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Stanford Robotics Lab; Haochen Shi, Weizhuo Wang, Shuran Song, C. Karen Liu
- **disclosure citation:** Shi, H., Wang, W., Song, S., Liu, C. K. 'ToddlerBot: Open-Source ML-Compatible Humanoid Platform for Loco-Manipulation'. arXiv:2502.00893, February 2025. Conference on Robot Learning (CoRL) 2025 oral. Stanford Robotics Lab.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-arm`, `mechanism-3d-printed-platform`, `control-rl-policy`, `control-imitation-learning`, `control-sim-to-real`, `control-loco-manipulation`

**Prior art notes:**

> ToddlerBot is Stanford's canonical sub-$6k open-hardware ML-compatible humanoid (CoRL 2025 oral). Establishes 1-year-deep open-academic prior art for: integrated loco-manipulation policy training on an open humanoid platform, transferable motor system-ID for sim-to-real without hand-tuning, 30-DoF anthropomorphic full-body at sub-$6k. Direct shielding for any commercial claim on integrated full-body humanoid policy training, particularly any 'one policy controls the whole body' claim. Together with Berkeley Humanoid Lite, establishes the open-academic baseline for sub-$10k humanoid robotics.

**Sources:**

1. Shi, Wang, Song, Liu. arXiv:2502.00893 February 2025.
2. CoRL 2025 proceedings (proceedings.mlr.press/v305/shi25a.html).
3. Project page (toddlerbot.github.io).
4. GitHub: github.com/hshi74/toddlerbot.

---

### 2025-02 — OpenVLA-OFT

- **id:** `openvla-oft-stanford-2025`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Stanford; Moo Jin Kim, Chelsea Finn, Percy Liang
- **disclosure citation:** Kim, M. J., Finn, C., Liang, P. 'Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success'. arXiv:2502.19645, February 2025. Stanford.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-foundation-model-policy`, `control-action-chunking`, `control-parallel-decoding`, `control-imitation-learning`

**Prior art notes:**

> OpenVLA-OFT is the canonical Optimized Fine-Tuning recipe for VLA models (Stanford, Feb 2025). 15-month-deep prior art on: parallel action decoding for VLA, action chunking + continuous action representation + L1 regression objective combination. Direct shielding for any commercial humanoid VLA fine-tuning claim, particularly any claim on 'fast inference at high success' for humanoid VLAs. Outperforms π₀ on bimanual ALOHA — the canonical academic benchmark for bimanual humanoid manipulation.

**Sources:**

1. Kim, Finn, Liang. arXiv:2502.19645 February 2025.
2. Project page (openvla-oft.github.io).
3. GitHub: github.com/moojink/openvla-oft.

---

### 2025-11 — LeFlexiTac (Columbia RoboPIL tactile-LeRobot)

- **id:** `leflexitac-columbia-2025`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** Columbia University RoboPIL lab; Naian Tao, Yifan He, Wesley Maa, Binghao Huang, Yunzhu Li
- **disclosure citation:** Tao, N., He, Y., Maa, W., Huang, B., Li, Y. 'LeFlexiTac: Giving Robots a Sense of Touch'. Columbia University RoboPIL Blog, May 2026. Public GitHub fork of HuggingFace LeRobot at github.com/TNA001-AI/lerobot_tactile, repo created 2025-11-14, Apache License 2.0. Project page: tna001-ai.github.io/LeFlexiTac/.
- **disclosed subsystems:** `sensing-tactile-fingertip`, `sensing-vision-tactile`, `control-vla-tactile-augmented`, `control-imitation-learning`, `mechanism-parallel-jaw-gripper`

**Prior art notes:**

> LeFlexiTac (Columbia RoboPIL November 2025+; blog disclosure May 2026) is the canonical open-source tactile-augmented LeRobot extension demonstrating tactile sensing as an additive modality across four distinct policy architectures (ACT, Diffusion Policy, Pi0.5, SmolVLA). Apache 2.0 open-permissive prior art. Direct shielding for any commercial humanoid claim deriving from: (1) tactile observation channels in VLA / imitation-learning policy frameworks; (2) tactile-augmented LeRobot / SO-ARM platforms; (3) the architectural pattern of feeding a single tactile stream into multiple policy backbones. Lineage descends from GelSight (corpus gelsight, MIT 2009) for vision-tactile sensing and from HuggingFace LeRobot (corpus huggingface-lerobot-2024) for the framework substrate.

**Sources:**

1. github.com/TNA001-AI/lerobot_tactile (Apache 2.0; created 2025-11-14).
2. tna001-ai.github.io/LeFlexiTac/ (project page).
3. Tao, N., He, Y., Maa, W., Huang, B., Li, Y. 'LeFlexiTac: Giving Robots a Sense of Touch'. Columbia University RoboPIL Blog, 2026.
4. Parent repo: github.com/huggingface/lerobot.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `0f95e9a`.*
