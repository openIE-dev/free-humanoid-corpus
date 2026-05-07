---
title: control-physics-simulation
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-physics-simulation`

**3 corpus entries disclose this subsystem.**

Earliest disclosure: 2012-10

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## MuJoCo (original) (2012-10)

- **id**: `mujoco-todorov-2012`
- **corpus**: academic
- **creator**: Emo Todorov, Tom Erez, Yuval Tassa (originally University of Washington / Roboti LLC; now Google DeepMind)
- **disclosure**: Todorov, E., Erez, T., Tassa, Y. 'MuJoCo: A physics engine for model-based control'. IROS 2012. Originally proprietary (Roboti LLC); acquired by Google DeepMind October 2021 and released under Apache-2.0.
- **ip status**: open-permissive
- **prior art notes**: MuJoCo is the canonical academic physics engine for model-based robotic control (Todorov-Erez-Tassa 2012). 13-year-deep prior art spanning the proprietary Roboti era (2012-2021) and the open-source DeepMind era (2021+). The substrate that the Tassa iLQG entry, Howell-Tassa MuJoCo MPC entry, MJX entry, and Genesis simulator entry all build on or interop with. Direct shielding for any commercial humanoid claim on contact-rich policy training simulation. MJCF is the format OpenLoco compiles to, so MuJoCo is the reference simulator for the entire free-humanoid-family.

## Drake (2019-01)

- **id**: `drake-tedrake-2019`
- **corpus**: academic
- **creator**: MIT CSAIL Robot Locomotion Group + Toyota Research Institute; Russ Tedrake et al.
- **disclosure**: Tedrake, R., the Drake Development Team. 'Drake: Model-Based Design and Verification for Robotics'. drake.mit.edu, project active since ~2010 with formal v1.0 in January 2019. BSD-3-Clause source: github.com/RobotLocomotion/drake. MIT CSAIL + Toyota Research Institute.
- **ip status**: open-permissive
- **prior art notes**: Drake is the canonical MIT/TRI model-based design + verification toolkit for robotics (Tedrake et al., active since ~2010, v1.0 Jan 2019). 6-year-deep formal-release prior art, 15-year-deep project. Distinct from MuJoCo by emphasis on deterministic verifiable semantics (relevant for safety-critical / certification use cases). Direct shielding for any commercial humanoid claim on verifiable model-based control or whole-body QP/MPC architectures. Free-humanoid-platform/wheeled/centaur/submersible all reference Drake as a tertiary simulator option for whole-body MPC validation.

## NVIDIA Isaac Gym (2021-08)

- **id**: `nvidia-isaac-gym-2021`
- **corpus**: academic
- **creator**: NVIDIA + ETH Zürich Robotic Systems Lab; Makoviychuk et al.
- **disclosure**: Makoviychuk, V., Wawrzyniak, L., Guo, Y., Lu, M., Storey, K., Macklin, M., Hoeller, D., Rudin, N., Allshire, A., Handa, A., State, G. 'Isaac Gym: High-Performance GPU-Based Physics Simulation For Robot Learning'. NeurIPS 2021 Track on Datasets and Benchmarks. arXiv:2108.10470.
- **ip status**: open-permissive
- **prior art notes**: Isaac Gym is the canonical first-generation NVIDIA GPU-parallelized robotic RL simulator (NeurIPS 2021). 4-year-deep open-permissive prior art. Direct ancestor of Isaac Lab (round-8 entry nvidia-isaac-lab-2024) and the substrate for the canonical sim-to-real ANYmal perceptive-locomotion papers. Direct shielding for any commercial humanoid claim on GPU-parallelized RL training; particularly the thousands-of-parallel-envs scaling that commercial humanoid vendors cite as proprietary.
