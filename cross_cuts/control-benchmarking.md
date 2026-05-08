---
title: control-benchmarking
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-benchmarking`

**6 corpus entries disclose this subsystem.**

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

## CALVIN (2021-12)

- **id**: `calvin-mees-2022`
- **corpus**: academic
- **creator**: University of Freiburg AIS Lab; Oier Mees, Lukas Hermann, Wolfram Burgard
- **disclosure**: Mees, O., Hermann, L., Rosete-Beas, E., Burgard, W. 'CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks'. IEEE Robotics and Automation Letters 7(3) 2022. arXiv:2112.03227. University of Freiburg.
- **ip status**: open-permissive
- **prior art notes**: CALVIN is the canonical long-horizon language-conditioned manipulation benchmark (Mees + Burgard Freiburg, RA-L 2022). 4-year-deep open-permissive prior art for: language-conditioned robot manipulation benchmark, teleoperated 'play data' as training distribution, hour-scale unstructured play datasets for language grounding. Direct shielding for any commercial humanoid claim on language-conditioned manipulation training data + benchmarks. Together with LIBERO (round-17), RoboCasa (round-16), robomimic (round-16), establishes the language-conditioned-VLA evaluation substrate.

## FurnitureBench (2023-05)

- **id**: `furniturebench-heo-rss-2023`
- **corpus**: academic
- **creator**: KAIST + USC; Minho Heo, Youngwoon Lee, Doohyun Lee, Joseph J. Lim
- **disclosure**: Heo, M., Lee, Y., Lee, D., Lim, J. J. 'FurnitureBench: Reproducible Real-World Benchmark for Long-Horizon Complex Manipulation'. RSS 2023. arXiv:2305.12821. KAIST + USC.
- **ip status**: open-permissive
- **prior art notes**: FurnitureBench is the canonical real-world long-horizon manipulation benchmark (Heo et al. RSS 2023). 2-year-deep open-permissive prior art for: furniture-assembly real-robot benchmark, fiducial-based standardization for cross-lab reproducibility. Distinct architectural branch from sim-only benchmarks: FurnitureBench is real-robot, while RLBench/robomimic/LIBERO/RoboCasa are simulated. Direct shielding for any commercial humanoid claim on furniture-assembly or long-horizon real-world benchmark performance.

## LIBERO (Lifelong Robot Learning Benchmark) (2023-06)

- **id**: `libero-liu-neurips-2023`
- **corpus**: academic
- **creator**: UT Austin + Bytedance Research; Bo Liu, Yifeng Zhu, Yuke Zhu, Peter Stone et al.
- **disclosure**: Liu, B., Zhu, Y., Gao, C., Feng, Y., Liu, Q., Zhu, Y., Stone, P. 'LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning'. NeurIPS 2023 Track on Datasets and Benchmarks. arXiv:2306.03310. UT Austin + Bytedance Research.
- **ip status**: open-permissive
- **prior art notes**: LIBERO is the canonical lifelong-robot-learning benchmark (Liu et al. NeurIPS 2023). 2-year-deep prior art on the benchmark surface that **OpenVLA-OFT (round-12), π₀ (round-12), RDT-1B (round-13), and most contemporary VLA papers report results against**. Any commercial humanoid VLA claim of 'we outperform X% on LIBERO' implies the LIBERO benchmark itself is reproducible academic art — that benchmark's 130 tasks plus extendible generation pipeline are 100% open-permissive prior art. Together with robomimic (round-16) and SimplerEnv (round-17 entry), establishes the open-academic VLA evaluation substrate.

## SimplerEnv (2024-05)

- **id**: `simpler-env-li-corl-2024`
- **corpus**: academic
- **creator**: UCSD + Stanford + UC Berkeley + Google DeepMind; Xuanlin Li, Kyle Hsu, Sergey Levine, Chelsea Finn, Hao Su et al.
- **disclosure**: Li, X., Hsu, K., Gu, J., Pertsch, K., Mees, O., Walke, H. R., Fu, C., Lunawat, I., Sieh, I., Kirmani, S., Levine, S., Wu, J., Finn, C., Su, H., Vuong, Q., Xiao, T. 'Evaluating Real-World Robot Manipulation Policies in Simulation'. CoRL 2024. arXiv:2405.05941. UCSD + Stanford + UC Berkeley + Google DeepMind.
- **ip status**: open-permissive
- **prior art notes**: SimplerEnv is the canonical sim-eval framework matched to real-world manipulation evaluations (Li et al. CoRL 2024). 1-year-deep open-permissive prior art for: simulation-based VLA policy evaluation that correlates with real-world performance, sim-real matched setup design (Google Robot, WidowX+Bridge). Direct shielding for any commercial humanoid claim on 'our sim eval predicts real performance' or on specific simulated benchmark infrastructure.
