---
title: control-physics-simulation
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-physics-simulation`

**10 corpus entries disclose this subsystem.**

Earliest disclosure: 2003-01

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## AnyBody Modeling System (2003-01)

- **id**: `anybody-rasmussen-2003`
- **corpus**: private
- **creator**: AnyBody Technology A/S (Aalborg University, Denmark); John Rasmussen + Michael Damsgaard
- **disclosure**: AnyBody Technology A/S (Aalborg, Denmark; Aalborg University spinout 2001 by John Rasmussen + Michael Damsgaard). AnyBody Modeling System commercial reveal 2003.
- **ip status**: trade-secret
- **prior art notes**: AnyBody Modeling System (Rasmussen + Damsgaard Aalborg 2003+) is the canonical commercial biomechanics modeling system. 22-year-deep public-disclosure prior art. Together with OpenSim (round-33), establishes the biomechanics-simulation prior-art chain that informs humanoid kinematic design. Closes a Danish commercial gap and adds biomechanics depth.

## OpenSim biomechanics framework (2007-11)

- **id**: `opensim-delp-stanford-2007`
- **corpus**: academic
- **creator**: Stanford University; Scott Delp + colleagues
- **disclosure**: Delp, S. L., Anderson, F. C., Arnold, A. S., Loan, P., Habib, A., John, C. T., Guendelman, E., Thelen, D. G. 'OpenSim: Open-Source Software to Create and Analyze Dynamic Simulations of Movement'. IEEE Transactions on Biomedical Engineering 54(11) 2007. Stanford University Neuromuscular Biomechanics Laboratory.
- **ip status**: open-permissive
- **prior art notes**: OpenSim (Delp et al. Stanford IEEE T-BME 2007) is the dominant academic biomechanics simulation framework. 18-year-deep open-permissive prior art. **The framework underlying humanoid-robot kinematic design** — humanoid arms + legs are designed to approximate human ranges of motion documented in OpenSim models. Direct shielding for any commercial humanoid claim that derives kinematic specifications from human-anatomical models.

## MuJoCo (original) (2012-10)

- **id**: `mujoco-todorov-2012`
- **corpus**: academic
- **creator**: Emo Todorov, Tom Erez, Yuval Tassa (originally University of Washington / Roboti LLC; now Google DeepMind)
- **disclosure**: Todorov, E., Erez, T., Tassa, Y. 'MuJoCo: A physics engine for model-based control'. IROS 2012. Originally proprietary (Roboti LLC); acquired by Google DeepMind October 2021 and released under Apache-2.0.
- **ip status**: open-permissive
- **prior art notes**: MuJoCo is the canonical academic physics engine for model-based robotic control (Todorov-Erez-Tassa 2012). 13-year-deep prior art spanning the proprietary Roboti era (2012-2021) and the open-source DeepMind era (2021+). The substrate that the Tassa iLQG entry, Howell-Tassa MuJoCo MPC entry, MJX entry, and Genesis simulator entry all build on or interop with. Direct shielding for any commercial humanoid claim on contact-rich policy training simulation. MJCF is the format OpenLoco compiles to, so MuJoCo is the reference simulator for the entire free-humanoid-family.

## PyBullet (2016-01)

- **id**: `pybullet-coumans-2017`
- **corpus**: academic
- **creator**: Erwin Coumans (Google Brain), Yunfei Bai
- **disclosure**: Coumans, E., Bai, Y. 'PyBullet: A Python module for physics simulation for games, robotics and machine learning'. 2016-2025. pybullet.org. Bullet physics engine antecedent (Coumans 2003+). Open-source ZLIB license.
- **ip status**: open-permissive
- **prior art notes**: PyBullet (Coumans Google 2017+) is the foundational open-source physics engine for academic robotics + RL. 9-year-deep open-permissive prior art. The dominant academic simulator before MuJoCo open-sourcing 2021. Direct shielding for any commercial humanoid claim using physics-simulation training infrastructure.

## DeepMind Control Suite (2018-01)

- **id**: `dm-control-suite-tassa-2018`
- **corpus**: academic
- **creator**: DeepMind; Yuval Tassa et al.
- **disclosure**: Tassa, Y., Doron, Y., Muldal, A., Erez, T., Li, Y., Casas, D. d. L., Budden, D., Abdolmaleki, A., Merel, J., Lefrancq, A., Lillicrap, T., Riedmiller, M. 'DeepMind Control Suite'. arXiv:1801.00690, January 2018. DeepMind.
- **ip status**: open-permissive
- **prior art notes**: DeepMind Control Suite (Tassa et al. DeepMind 2018) is the foundational continuous-control RL benchmark suite. 7-year-deep open-permissive prior art. Used in countless RL papers 2018-2024. Direct shielding for any commercial humanoid claim using MuJoCo-based continuous-control benchmark evaluation.

## Drake (2019-01)

- **id**: `drake-tedrake-2019`
- **corpus**: academic
- **creator**: MIT CSAIL Robot Locomotion Group + Toyota Research Institute; Russ Tedrake et al.
- **disclosure**: Tedrake, R., the Drake Development Team. 'Drake: Model-Based Design and Verification for Robotics'. drake.mit.edu, project active since ~2010 with formal v1.0 in January 2019. BSD-3-Clause source: github.com/RobotLocomotion/drake. MIT CSAIL + Toyota Research Institute.
- **ip status**: open-permissive
- **prior art notes**: Drake is the canonical MIT/TRI model-based design + verification toolkit for robotics (Tedrake et al., active since ~2010, v1.0 Jan 2019). 6-year-deep formal-release prior art, 15-year-deep project. Distinct from MuJoCo by emphasis on deterministic verifiable semantics (relevant for safety-critical / certification use cases). Direct shielding for any commercial humanoid claim on verifiable model-based control or whole-body QP/MPC architectures. Free-humanoid-platform/wheeled/centaur/submersible all reference Drake as a tertiary simulator option for whole-body MPC validation.

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

## Habitat 3.0 (2023-10)

- **id**: `fair-habitat-3-puig-2024`
- **corpus**: academic
- **creator**: FAIR + Georgia Tech + UIUC; Puig, Mottaghi, Batra, Malik et al.
- **disclosure**: Puig, X., Undersander, E., Szot, A., Cote, M. D., Yang, T.-Y., Partsey, R., Desai, R., Clegg, A. W., Hlavac, M., Min, S. Y., Vondruš, T., Gervet, T., Berges, V.-P., Turner, J. M., Maksymets, O., Kira, Z., Kalakrishnan, M., Malik, J., Chaplot, D. S., Jain, U., Batra, D., Rai, A., Mottaghi, R. 'Habitat 3.0: A Co-Habitat for Humans, Avatars and Robots'. ICLR 2024. arXiv:2310.13724. FAIR + Georgia Tech + UIUC.
- **ip status**: open-permissive
- **prior art notes**: Habitat 3.0 is the canonical academic multi-agent embodied simulator with humanoid avatars (Puig et al. ICLR 2024). 1.5-year-deep open-permissive prior art for: humanoid-and-robot co-simulation, social-navigation tasks where robots interact with human avatars, large-scale (211-house) furnished scene library for embodied AI. Direct shielding for any commercial humanoid claim on training-with-humans-in-simulation or social-navigation policies.

## RoboCasa (2024-06)

- **id**: `robocasa-nasiriany-2024`
- **corpus**: academic
- **creator**: UT Austin + NVIDIA; Soroush Nasiriany, Abhinav Maddukuri, Yuke Zhu et al.
- **disclosure**: Nasiriany, S., Maddukuri, A., Zhang, L., Parikh, A., Lo, A., Joshi, A., Mandlekar, A., Zhu, Y. 'RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots'. arXiv:2406.02523, June 2024. RSS 2024. UT Austin + NVIDIA. RoboCasa365 follow-up (OpenReview tQJYKwc3n4) extends to 365 tasks across 2,500 kitchen environments.
- **ip status**: open-permissive
- **prior art notes**: RoboCasa is the canonical generative-AI-augmented household-task simulation framework (UT Austin + NVIDIA, RSS 2024). ~1-year-deep open-permissive prior art for: generative-AI-authored simulation environments at scale, large-scale (>1k hours) demonstration datasets for VLA training, kitchen-scene household-task benchmark suite. Direct shielding for any commercial humanoid claim on 'training data at scale for household manipulation' — RoboCasa365's 1,600 synthetic + 600 human hours establishes the open-academic baseline.
