---
title: "control-benchmarking"
parent: "Invalidity Contentions"
nav_order: 25
layout: default
---

# Invalidity Contention Packet — `control-benchmarking`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-benchmarking`  
**Entries:** 7 (7 commons-grade, 0 draft)  
**Earliest disclosure:** 2018-01  
**Most recent disclosure:** 2024-05

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-benchmarking`.

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

### 2018-01 — DeepMind Control Suite

- **id:** `dm-control-suite-tassa-2018`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** DeepMind; Yuval Tassa et al.
- **disclosure citation:** Tassa, Y., Doron, Y., Muldal, A., Erez, T., Li, Y., Casas, D. d. L., Budden, D., Abdolmaleki, A., Merel, J., Lefrancq, A., Lillicrap, T., Riedmiller, M. 'DeepMind Control Suite'. arXiv:1801.00690, January 2018. DeepMind.
- **disclosed subsystems:** `control-rl-policy`, `control-benchmarking`, `control-physics-simulation`

**Prior art notes:**

> DeepMind Control Suite (Tassa et al. DeepMind 2018) is the foundational continuous-control RL benchmark suite. 7-year-deep open-permissive prior art. Used in countless RL papers 2018-2024. Direct shielding for any commercial humanoid claim using MuJoCo-based continuous-control benchmark evaluation.

**Sources:**

1. Tassa et al. arXiv:1801.00690 January 2018.
2. GitHub: github.com/google-deepmind/dm_control.

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

### 2024-05 — SimplerEnv

- **id:** `simpler-env-li-corl-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** UCSD + Stanford + UC Berkeley + Google DeepMind; Xuanlin Li, Kyle Hsu, Sergey Levine, Chelsea Finn, Hao Su et al.
- **disclosure citation:** Li, X., Hsu, K., Gu, J., Pertsch, K., Mees, O., Walke, H. R., Fu, C., Lunawat, I., Sieh, I., Kirmani, S., Levine, S., Wu, J., Finn, C., Su, H., Vuong, Q., Xiao, T. 'Evaluating Real-World Robot Manipulation Policies in Simulation'. CoRL 2024. arXiv:2405.05941. UCSD + Stanford + UC Berkeley + Google DeepMind.
- **disclosed subsystems:** `control-sim-to-real`, `control-benchmarking`, `control-policy-evaluation`

**Prior art notes:**

> SimplerEnv is the canonical sim-eval framework matched to real-world manipulation evaluations (Li et al. CoRL 2024). 1-year-deep open-permissive prior art for: simulation-based VLA policy evaluation that correlates with real-world performance, sim-real matched setup design (Google Robot, WidowX+Bridge). Direct shielding for any commercial humanoid claim on 'our sim eval predicts real performance' or on specific simulated benchmark infrastructure.

**Sources:**

1. Li et al. arXiv:2405.05941 May 2024; CoRL 2024.
2. Project page (simpler-env.github.io).
3. GitHub: github.com/simpler-env/SimplerEnv.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `f228137`.*
