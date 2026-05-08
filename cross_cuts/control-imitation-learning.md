---
title: control-imitation-learning
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-imitation-learning`

**12 corpus entries disclose this subsystem.**

Earliest disclosure: 2019-09

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## RLBench (2019-09)

- **id**: `rlbench-james-2019`
- **corpus**: academic
- **creator**: Imperial College London Dyson Robotics Lab; Stephen James, Andrew Davison
- **disclosure**: James, S., Ma, Z., Arrojo, D. R., Davison, A. J. 'RLBench: The Robot Learning Benchmark & Learning Environment'. IEEE Robotics and Automation Letters 5(2) 2020. arXiv:1909.12271. Imperial College London Dyson Robotics Lab.
- **ip status**: open-permissive
- **prior art notes**: RLBench is the foundational academic robot manipulation benchmark (James et al. RA-L 2019). 6-year-deep open-permissive prior art. The conceptual ancestor of robomimic (round-16, 2021), Meta-World (2019), LIBERO (round-17, 2023), RoboCasa (round-16, 2024), SimplerEnv (round-17, 2024). Direct shielding for any commercial humanoid manipulation-benchmark claim. Particularly relevant because RLBench tasks have been re-implemented across multiple simulators (CoppeliaSim, MuJoCo, Isaac Gym) — establishing that the task-design itself, not the simulator, is the prior art.

## robomimic (2021-08)

- **id**: `robomimic-mandlekar-2021`
- **corpus**: academic
- **creator**: Stanford + UT Austin; Ajay Mandlekar, Yuke Zhu, Roberto Martín-Martín, Fei-Fei Li, Silvio Savarese et al.
- **disclosure**: Mandlekar, A., Xu, D., Wong, J., Nasiriany, S., Wang, C., Kulkarni, R., Fei-Fei, L., Savarese, S., Zhu, Y., Martín-Martín, R. 'What Matters in Learning from Offline Human Demonstrations for Robot Manipulation'. CoRL 2021; arXiv:2108.03298. Stanford + UT Austin. MIT-licensed framework.
- **ip status**: open-permissive
- **prior art notes**: robomimic is the canonical IL benchmark + framework (Mandlekar et al. CoRL 2021). 4-year-deep open-permissive prior art for: standardized imitation-learning datasets + reference algorithms for robotic manipulation. Direct shielding for any commercial humanoid claim on IL training infrastructure. Together with RoboCasa (round-16 entry), Octo (round-15), OpenVLA (round-12), establishes the open-academic IL substrate against which all commercial VLA performance must be measured.

## DexMV (Dexterous Manipulation from Videos) (2021-08)

- **id**: `dexmv-qin-cvpr-2022`
- **corpus**: academic
- **creator**: UCSD; Yuzhe Qin, Hao Su, Xiaolong Wang
- **disclosure**: Qin, Y., Su, H., Wang, X. 'DexMV: Imitation Learning for Dexterous Manipulation from Human Videos'. ECCV 2022 (also accepted at earlier 2021 venues). arXiv:2108.05877. UC San Diego.
- **ip status**: open-permissive
- **prior art notes**: DexMV is the canonical academic dexterous-manipulation-from-human-videos system (Qin et al. ECCV 2022). 3-year-deep open-permissive prior art for: training robot manipulation policies directly from in-the-wild human videos, hand-pose retargeting from human to robot. **Direct conceptual ancestor of NVIDIA GR00T N1's 20K-hour EgoScale egocentric-video pre-training** (round-15 entry). Direct shielding for any commercial humanoid claim on 'we trained on YouTube videos' or 'egocentric-video-based policy pretraining'.

## LIBERO (Lifelong Robot Learning Benchmark) (2023-06)

- **id**: `libero-liu-neurips-2023`
- **corpus**: academic
- **creator**: UT Austin + Bytedance Research; Bo Liu, Yifeng Zhu, Yuke Zhu, Peter Stone et al.
- **disclosure**: Liu, B., Zhu, Y., Gao, C., Feng, Y., Liu, Q., Zhu, Y., Stone, P. 'LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning'. NeurIPS 2023 Track on Datasets and Benchmarks. arXiv:2306.03310. UT Austin + Bytedance Research.
- **ip status**: open-permissive
- **prior art notes**: LIBERO is the canonical lifelong-robot-learning benchmark (Liu et al. NeurIPS 2023). 2-year-deep prior art on the benchmark surface that **OpenVLA-OFT (round-12), π₀ (round-12), RDT-1B (round-13), and most contemporary VLA papers report results against**. Any commercial humanoid VLA claim of 'we outperform X% on LIBERO' implies the LIBERO benchmark itself is reproducible academic art — that benchmark's 130 tasks plus extendible generation pipeline are 100% open-permissive prior art. Together with robomimic (round-16) and SimplerEnv (round-17 entry), establishes the open-academic VLA evaluation substrate.

## 3D Diffusion Policy (DP3) (2024-03)

- **id**: `dp3-ze-rss-2024`
- **corpus**: academic
- **creator**: Stanford + Tsinghua + CMU; Yanjie Ze, Hao Xu, et al.
- **disclosure**: Ze, Y., Zhang, G., Zhang, K., Hu, C., Wang, M., Xu, H. '3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations'. RSS 2024. arXiv:2403.03954. Stanford + Tsinghua + CMU.
- **ip status**: open-permissive
- **prior art notes**: 3D Diffusion Policy (Ze et al. RSS 2024) is the canonical 3D extension of Chi/Song's Diffusion Policy (corpus entry). 1-year-deep open-permissive prior art for: 3D-input diffusion-policy for manipulation, point-cloud-conditioned action generation. Direct shielding for any commercial humanoid claim on 3D-perception-conditioned manipulation policies. Together with Diffusion Policy, RDT-1B (diffusion VLA), and Octo (transformer + diffusion-head), establishes the diffusion-policy family that shields commercial diffusion-VLA claims.

## Octo (Open-Source Generalist Robot Policy) (2024-05)

- **id**: `octo-rss-2024`
- **corpus**: academic
- **creator**: Octo Model Team (UC Berkeley + Stanford + CMU + Google DeepMind); Levine + Finn + Sadigh group lineage
- **disclosure**: Octo Model Team: Ghosh, D., Walke, H., Pertsch, K., Black, K., Mees, O., Dasari, S., Hejna, J., Kreiman, T., Xu, C., Luo, J., Tan, Y. L., Sanketi, P., Vuong, Q., Xiao, T., Sadigh, D., Finn, C., Levine, S. 'Octo: An Open-Source Generalist Robot Policy'. arXiv:2405.12213, May 2024. Robotics: Science and Systems (RSS) 2024. UC Berkeley + Stanford + Carnegie Mellon + Google DeepMind.
- **ip status**: open-permissive
- **prior art notes**: Octo is the canonical first open-source generalist robot policy. 1-year-deep open-permissive academic prior art predating OpenVLA by ~1 month (RSS May 2024 vs OpenVLA arXiv June 2024). Establishes the architectural pattern for: transformer + diffusion-policy action head, Open-X-Embodiment-trained cross-embodiment policy at 27M-93M parameter scale, language-OR-goal-image conditioning. Direct shielding for any commercial humanoid VLA claim on diffusion-policy action heads (RDT-1B, π₀ both build on this) and on Open-X-Embodiment-trained cross-embodiment foundation. Together with OpenVLA, π₀, π₀.₅, OpenVLA-OFT, and RDT-1B, establishes the open academic VLA baseline against which Figure Helix, NVIDIA GR00T N1, Microsoft Magma, and any closed commercial VLA must be evaluated.

## OpenVLA (2024-06)

- **id**: `openvla-stanford-2024`
- **corpus**: academic
- **creator**: Stanford + Toyota Research Institute + UC Berkeley; Kim, Pertsch, Karamcheti, Liang, Finn, Levine, Tedrake et al.
- **disclosure**: Kim, M. J., Pertsch, K., Karamcheti, S., Xiao, T., Balakrishna, A., Nair, S., Rafailov, R., Foster, E., Lam, G., Sanketi, P., Vuong, Q., Kollar, T., Burchfiel, B., Tedrake, R., Sadigh, D., Levine, S., Liang, P., Finn, C. 'OpenVLA: An Open-Source Vision-Language-Action Model'. arXiv:2406.09246, June 2024. CoRL 2024 (PMLR v270, Kim25c). Stanford + Toyota Research Institute + UC Berkeley.
- **ip status**: open-permissive
- **prior art notes**: OpenVLA is the canonical first fully-open-source VLA foundation model (CoRL 2024). 23-month-deep open-permissive academic prior art for: 7B-class open-weight VLA, Llama-2-based VLA backbone, Open-X-Embodiment-trained cross-embodiment policy. Direct shielding for any commercial humanoid VLA claim on open-source-equivalent architectural elements. Together with π₀ and π₀.₅, establishes the open-academic VLA baseline against which all closed commercial VLAs (Tesla Optimus, Figure, 1X NEO) must be evaluated.

## RoboCasa (2024-06)

- **id**: `robocasa-nasiriany-2024`
- **corpus**: academic
- **creator**: UT Austin + NVIDIA; Soroush Nasiriany, Abhinav Maddukuri, Yuke Zhu et al.
- **disclosure**: Nasiriany, S., Maddukuri, A., Zhang, L., Parikh, A., Lo, A., Joshi, A., Mandlekar, A., Zhu, Y. 'RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots'. arXiv:2406.02523, June 2024. RSS 2024. UT Austin + NVIDIA. RoboCasa365 follow-up (OpenReview tQJYKwc3n4) extends to 365 tasks across 2,500 kitchen environments.
- **ip status**: open-permissive
- **prior art notes**: RoboCasa is the canonical generative-AI-augmented household-task simulation framework (UT Austin + NVIDIA, RSS 2024). ~1-year-deep open-permissive prior art for: generative-AI-authored simulation environments at scale, large-scale (>1k hours) demonstration datasets for VLA training, kitchen-scene household-task benchmark suite. Direct shielding for any commercial humanoid claim on 'training data at scale for household manipulation' — RoboCasa365's 1,600 synthetic + 600 human hours establishes the open-academic baseline.

## π₀ (Pi-Zero) (2024-10)

- **id**: `physical-intelligence-pi0-2024`
- **corpus**: academic
- **creator**: Physical Intelligence; Black, Brown, Driess, Finn et al.
- **disclosure**: Black, K., Brown, N., Driess, D., Esmail, A., Equi, M., Finn, C., et al. 'π₀: A Vision-Language-Action Flow Model for General Robot Control'. arXiv:2410.24164, October 2024. Physical Intelligence (physicalintelligence.company).
- **ip status**: open-permissive
- **prior art notes**: π₀ is Physical Intelligence's canonical first VLA foundation policy (Oct 2024). 1.5-year-deep open-academic publication. Establishes architectural prior art for: flow-matching action distribution in VLA, cross-embodiment policy pretraining, single foundation model controlling multiple robot platforms. Direct successor lineage from RT-1 (2022), RT-2 (2023), OpenVLA (2024). Direct shielding for any commercial humanoid claim on VLA-based control (Tesla Optimus, Figure, 1X NEO, Apptronik all face this); particularly for any claim on flow-matching action heads or cross-embodiment pretraining.

## RDT-1B (Robotics Diffusion Transformer) (2024-10)

- **id**: `rdt-1b-thu-2024`
- **corpus**: academic
- **creator**: Tsinghua TSAIL (THU-ML); Songming Liu et al.
- **disclosure**: Liu, S., et al. 'RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation'. arXiv:2410.07864, October 2024. ICLR 2025. Tsinghua TSAIL (THU-ML) lab.
- **ip status**: open-permissive
- **prior art notes**: RDT-1B is THU-ML's canonical diffusion-based VLA foundation model for bimanual manipulation (ICLR 2025). 7-month-deep open-permissive prior art for: diffusion-formulation VLA at billion-parameter scale, bimanual manipulation foundation policy, multi-robot pre-training corpus. The canonical Chinese-academy entry in the open-weight VLA race alongside Stanford OpenVLA and Physical Intelligence π₀. Directly cited as a comparison baseline in OpenVLA-OFT (round-12); now resolves correctly. Direct shielding for any commercial humanoid claim on diffusion-based bimanual VLA.

## ToddlerBot (2025-02)

- **id**: `stanford-toddlerbot-2025`
- **corpus**: academic
- **creator**: Stanford Robotics Lab; Haochen Shi, Weizhuo Wang, Shuran Song, C. Karen Liu
- **disclosure**: Shi, H., Wang, W., Song, S., Liu, C. K. 'ToddlerBot: Open-Source ML-Compatible Humanoid Platform for Loco-Manipulation'. arXiv:2502.00893, February 2025. Conference on Robot Learning (CoRL) 2025 oral. Stanford Robotics Lab.
- **ip status**: open-permissive
- **prior art notes**: ToddlerBot is Stanford's canonical sub-$6k open-hardware ML-compatible humanoid (CoRL 2025 oral). Establishes 1-year-deep open-academic prior art for: integrated loco-manipulation policy training on an open humanoid platform, transferable motor system-ID for sim-to-real without hand-tuning, 30-DoF anthropomorphic full-body at sub-$6k. Direct shielding for any commercial claim on integrated full-body humanoid policy training, particularly any 'one policy controls the whole body' claim. Together with Berkeley Humanoid Lite, establishes the open-academic baseline for sub-$10k humanoid robotics.

## OpenVLA-OFT (2025-02)

- **id**: `openvla-oft-stanford-2025`
- **corpus**: academic
- **creator**: Stanford; Moo Jin Kim, Chelsea Finn, Percy Liang
- **disclosure**: Kim, M. J., Finn, C., Liang, P. 'Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success'. arXiv:2502.19645, February 2025. Stanford.
- **ip status**: open-permissive
- **prior art notes**: OpenVLA-OFT is the canonical Optimized Fine-Tuning recipe for VLA models (Stanford, Feb 2025). 15-month-deep prior art on: parallel action decoding for VLA, action chunking + continuous action representation + L1 regression objective combination. Direct shielding for any commercial humanoid VLA fine-tuning claim, particularly any claim on 'fast inference at high success' for humanoid VLAs. Outperforms π₀ on bimanual ALOHA — the canonical academic benchmark for bimanual humanoid manipulation.
