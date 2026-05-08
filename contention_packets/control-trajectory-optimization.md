---
title: "control-trajectory-optimization"
parent: "Invalidity Contentions"
nav_order: 103
layout: default
---

# Invalidity Contention Packet — `control-trajectory-optimization`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-trajectory-optimization`  
**Entries:** 4 (4 commons-grade, 0 draft)  
**Earliest disclosure:** 2012-10  
**Most recent disclosure:** 2025-03

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-trajectory-optimization`.

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

### 2017-04 — OCS2 (Optimal Control for Switched Systems)

- **id:** `ocs2-eth-2017`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** ETH Zürich Robotic Systems Lab; Farbod Farshidian, Michael Neunert, Jonas Buchli
- **disclosure citation:** Farshidian, F., Neunert, M., Buchli, J. 'OCS2: An efficient C++ library for the optimal control of switched systems'. Initial release 2017+. ETH Zürich Robotic Systems Lab. Apache-2.0 open-source.
- **disclosed subsystems:** `control-mpc`, `control-optimal-control`, `control-trajectory-optimization`

**Prior art notes:**

> OCS2 (Farshidian-Neunert-Buchli ETH RSL 2017+) is the foundational C++ optimal-control library for switched + hybrid systems. 8-year-deep open-permissive prior art. Used in ETH RSL's ANYmal locomotion + humanoid research. Architectural counterpart to Crocoddyl (round-8) for SQP-based optimization. **Closes a citation-audit gap** (cited by laas-cnrs-toulouse-humanoid-2003 round-26 entry).

**Sources:**

1. Farshidian et al. OCS2 documentation.
2. GitHub: github.com/leggedrobotics/ocs2.

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

### 2025-03 — MuJoCo MPC (Howell-Tassa)

- **id:** `howell-tassa-mujoco-mpc-2025`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Google DeepMind; Howell, Lutter, Tassa et al.
- **disclosure citation:** Howell, T., Lutter, M., Acero, F., Yuan, M., Tassa, Y., et al. 'Whole-Body Model-Predictive Control of Legged Robots with MuJoCo'. arXiv:2503.04613, March 2025. Google DeepMind / Tassa group.
- **disclosed subsystems:** `control-mpc`, `control-trajectory-optimization`, `control-real-time-control`, `actuator-foc-controller`

**Prior art notes:**

> Howell-Tassa MuJoCo MPC is the direct 2025 successor to the Tassa iLQG 2012 entry already in the corpus. 14-month-deep open-permissive prior art for: real-time whole-body humanoid MPC using MuJoCo dynamics + finite-difference iLQR. Demonstrated on full-sized humanoid hardware, which closes the simulation-to-real gap that the 2012 Tassa work left open. Direct shielding for any commercial humanoid claim on real-time whole-body trajectory optimization.

**Sources:**

1. Howell et al. arXiv:2503.04613 March 2025.
2. GitHub: github.com/google-deepmind/mujoco_mpc.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `55e963d`.*
