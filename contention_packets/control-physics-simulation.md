---
title: "control-physics-simulation"
parent: "Invalidity Contentions"
nav_order: 54
layout: default
---

# Invalidity Contention Packet — `control-physics-simulation`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-physics-simulation`  
**Entries:** 6 (6 commons-grade, 0 draft)  
**Earliest disclosure:** 2012-10  
**Most recent disclosure:** 2024-06

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-physics-simulation`.

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

### 2012-10 — MuJoCo (original)

- **id:** `mujoco-todorov-2012`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Emo Todorov, Tom Erez, Yuval Tassa (originally University of Washington / Roboti LLC; now Google DeepMind)
- **disclosure citation:** Todorov, E., Erez, T., Tassa, Y. 'MuJoCo: A physics engine for model-based control'. IROS 2012. Originally proprietary (Roboti LLC); acquired by Google DeepMind October 2021 and released under Apache-2.0.
- **disclosed subsystems:** `control-physics-simulation`, `control-mpc`, `control-trajectory-optimization`

**Prior art notes:**

> MuJoCo is the canonical academic physics engine for model-based robotic control (Todorov-Erez-Tassa 2012). 13-year-deep prior art spanning the proprietary Roboti era (2012-2021) and the open-source DeepMind era (2021+). The substrate that the Tassa iLQG entry, Howell-Tassa MuJoCo MPC entry, MJX entry, and Genesis simulator entry all build on or interop with. Direct shielding for any commercial humanoid claim on contact-rich policy training simulation. MJCF is the format OpenLoco compiles to, so MuJoCo is the reference simulator for the entire free-humanoid-family.

**Sources:**

1. Todorov, Erez, Tassa. IROS 2012.
2. MuJoCo official site (mujoco.org).
3. GitHub: github.com/google-deepmind/mujoco.
4. DeepMind acquisition + open-sourcing announcement, October 2021.

---

### 2019-01 — Drake

- **id:** `drake-tedrake-2019`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** MIT CSAIL Robot Locomotion Group + Toyota Research Institute; Russ Tedrake et al.
- **disclosure citation:** Tedrake, R., the Drake Development Team. 'Drake: Model-Based Design and Verification for Robotics'. drake.mit.edu, project active since ~2010 with formal v1.0 in January 2019. BSD-3-Clause source: github.com/RobotLocomotion/drake. MIT CSAIL + Toyota Research Institute.
- **disclosed subsystems:** `control-physics-simulation`, `control-mpc`, `control-formal-verification`, `control-trajectory-optimization`

**Prior art notes:**

> Drake is the canonical MIT/TRI model-based design + verification toolkit for robotics (Tedrake et al., active since ~2010, v1.0 Jan 2019). 6-year-deep formal-release prior art, 15-year-deep project. Distinct from MuJoCo by emphasis on deterministic verifiable semantics (relevant for safety-critical / certification use cases). Direct shielding for any commercial humanoid claim on verifiable model-based control or whole-body QP/MPC architectures. Free-humanoid-platform/wheeled/centaur/submersible all reference Drake as a tertiary simulator option for whole-body MPC validation.

**Sources:**

1. Tedrake, R. 'Underactuated Robotics' textbook (underactuated.mit.edu).
2. Drake official site (drake.mit.edu).
3. GitHub: github.com/RobotLocomotion/drake.

---

### 2020-03 — SAPIEN simulator

- **id:** `sapien-xiang-cvpr-2020`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** UC San Diego + Stanford; Hao Su, Leonidas Guibas, Angel Chang group
- **disclosure citation:** Xiang, F., Qin, Y., Mo, K., Xia, Y., Zhu, H., Liu, F., Liu, M., Jiang, H., Yuan, Y., Wang, H., Yi, L., Chang, A. X., Guibas, L. J., Su, H. 'SAPIEN: A SimulAted Part-based Interactive ENvironment'. arXiv:2003.08515, March 2020. CVPR 2020. UC San Diego + Stanford. ManiSkill follow-up framework via haosulab/ManiSkill (Hillbot Inc.).
- **disclosed subsystems:** `control-physics-simulation`, `control-articulated-object-manipulation`, `control-sim-to-real`

**Prior art notes:**

> SAPIEN is the canonical PartNet-Mobility-based articulated-object simulator (Xiang et al. CVPR 2020). 5-year-deep open-permissive prior art for: part-level mobility annotation in robotic simulation, depth-noise modeling for sim-to-real, ManiSkill manipulation benchmark suite. Distinct from MuJoCo (rigid-body baseline), Isaac Gym (GPU-parallelized), and Genesis (multi-physics) by emphasis on articulated-object interaction. Direct shielding for any commercial humanoid claim on articulated-object manipulation training simulation.

**Sources:**

1. Xiang et al. arXiv:2003.08515 March 2020; CVPR 2020.
2. ManiSkill GitHub (github.com/haosulab/ManiSkill).
3. PartNet-Mobility dataset (partnet.org/MobilityProject/).

---

### 2021-08 — NVIDIA Isaac Gym

- **id:** `nvidia-isaac-gym-2021`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** NVIDIA + ETH Zürich Robotic Systems Lab; Makoviychuk et al.
- **disclosure citation:** Makoviychuk, V., Wawrzyniak, L., Guo, Y., Lu, M., Storey, K., Macklin, M., Hoeller, D., Rudin, N., Allshire, A., Handa, A., State, G. 'Isaac Gym: High-Performance GPU-Based Physics Simulation For Robot Learning'. NeurIPS 2021 Track on Datasets and Benchmarks. arXiv:2108.10470.
- **disclosed subsystems:** `control-physics-simulation`, `control-rl-policy`, `control-sim-to-real`, `control-gpu-parallelized-rl`

**Prior art notes:**

> Isaac Gym is the canonical first-generation NVIDIA GPU-parallelized robotic RL simulator (NeurIPS 2021). 4-year-deep open-permissive prior art. Direct ancestor of Isaac Lab (round-8 entry nvidia-isaac-lab-2024) and the substrate for the canonical sim-to-real ANYmal perceptive-locomotion papers. Direct shielding for any commercial humanoid claim on GPU-parallelized RL training; particularly the thousands-of-parallel-envs scaling that commercial humanoid vendors cite as proprietary.

**Sources:**

1. Makoviychuk et al. arXiv:2108.10470 NeurIPS 2021.
2. GitHub: github.com/NVIDIA-Omniverse/IsaacGymEnvs (research preview, archived).

---

### 2023-10 — Habitat 3.0

- **id:** `fair-habitat-3-puig-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** FAIR + Georgia Tech + UIUC; Puig, Mottaghi, Batra, Malik et al.
- **disclosure citation:** Puig, X., Undersander, E., Szot, A., Cote, M. D., Yang, T.-Y., Partsey, R., Desai, R., Clegg, A. W., Hlavac, M., Min, S. Y., Vondruš, T., Gervet, T., Berges, V.-P., Turner, J. M., Maksymets, O., Kira, Z., Kalakrishnan, M., Malik, J., Chaplot, D. S., Jain, U., Batra, D., Rai, A., Mottaghi, R. 'Habitat 3.0: A Co-Habitat for Humans, Avatars and Robots'. ICLR 2024. arXiv:2310.13724. FAIR + Georgia Tech + UIUC.
- **disclosed subsystems:** `control-physics-simulation`, `control-multi-agent-simulation`, `control-human-robot-collaboration`, `control-loco-manipulation`

**Prior art notes:**

> Habitat 3.0 is the canonical academic multi-agent embodied simulator with humanoid avatars (Puig et al. ICLR 2024). 1.5-year-deep open-permissive prior art for: humanoid-and-robot co-simulation, social-navigation tasks where robots interact with human avatars, large-scale (211-house) furnished scene library for embodied AI. Direct shielding for any commercial humanoid claim on training-with-humans-in-simulation or social-navigation policies.

**Sources:**

1. Puig et al. arXiv:2310.13724 ICLR 2024.
2. Project page (aihabitat.org/habitat3).
3. GitHub: github.com/facebookresearch/habitat-lab.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `b80ce5d`.*
