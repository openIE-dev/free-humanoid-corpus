---
title: control-trajectory-optimization
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-trajectory-optimization`

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

## MuJoCo MPC (Howell-Tassa) (2025-03)

- **id**: `howell-tassa-mujoco-mpc-2025`
- **corpus**: academic
- **creator**: Google DeepMind; Howell, Lutter, Tassa et al.
- **disclosure**: Howell, T., Lutter, M., Acero, F., Yuan, M., Tassa, Y., et al. 'Whole-Body Model-Predictive Control of Legged Robots with MuJoCo'. arXiv:2503.04613, March 2025. Google DeepMind / Tassa group.
- **ip status**: open-permissive
- **prior art notes**: Howell-Tassa MuJoCo MPC is the direct 2025 successor to the Tassa iLQG 2012 entry already in the corpus. 14-month-deep open-permissive prior art for: real-time whole-body humanoid MPC using MuJoCo dynamics + finite-difference iLQR. Demonstrated on full-sized humanoid hardware, which closes the simulation-to-real gap that the 2012 Tassa work left open. Direct shielding for any commercial humanoid claim on real-time whole-body trajectory optimization.
