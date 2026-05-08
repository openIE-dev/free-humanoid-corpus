---
title: control-optimal-control
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-optimal-control`

**3 corpus entries disclose this subsystem.**

Earliest disclosure: 1960-03

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Kalman filter + LQR (Linear-Quadratic Regulator) (1960-03)

- **id**: `kalman-filter-lqr-1960`
- **corpus**: academic
- **creator**: Stanford University + RIAS; Rudolf E. Kálmán
- **disclosure**: Kalman, R. E. 'A New Approach to Linear Filtering and Prediction Problems'. Journal of Basic Engineering 82(1) 1960. Kalman, R. E. 'Contributions to the Theory of Optimal Control'. Bol. Soc. Mat. Mexicana 5(2) 1960. Stanford University + RIAS.
- **ip status**: public-domain
- **prior art notes**: The Kalman filter + LQR (Kalman 1960) is the foundational state estimation + optimal control framework. 65-year-deep public-domain prior art. Used in essentially every robotic system. Direct shielding for any commercial humanoid claim involving state estimation, sensor fusion, or feedback control. **The underlying mathematics of every IMU-based attitude estimator** + every GPS-INS-DVL fusion stack in the corpus's submersible / wheeled / centaur entries.

## Model Predictive Control (MPC) (1989-08)

- **id**: `mpc-garcia-prett-morari-1989`
- **corpus**: academic
- **creator**: Caltech (Morari) + Shell (Prett) + IBM (Garcia)
- **disclosure**: Garcia, C. E., Prett, D. M., Morari, M. 'Model Predictive Control: Theory and Practice—a Survey'. Automatica 25(3) 1989. Antecedents: Richalet 1976, Cutler-Ramaker 1980 DMC.
- **ip status**: public-domain
- **prior art notes**: MPC (Garcia-Prett-Morari Automatica 1989) is the foundational Model Predictive Control academic survey. 36-year-deep public-domain prior art. The substrate of: Tassa iLQG (corpus), Crocoddyl (corpus), Howell-Tassa MuJoCo MPC (corpus round-11), OCS2 (round-33 entry below), Capture Point (corpus round-21), every humanoid + quadruped MPC controller in the corpus.

## OCS2 (Optimal Control for Switched Systems) (2017-04)

- **id**: `ocs2-eth-2017`
- **corpus**: academic
- **creator**: ETH Zürich Robotic Systems Lab; Farbod Farshidian, Michael Neunert, Jonas Buchli
- **disclosure**: Farshidian, F., Neunert, M., Buchli, J. 'OCS2: An efficient C++ library for the optimal control of switched systems'. Initial release 2017+. ETH Zürich Robotic Systems Lab. Apache-2.0 open-source.
- **ip status**: open-permissive
- **prior art notes**: OCS2 (Farshidian-Neunert-Buchli ETH RSL 2017+) is the foundational C++ optimal-control library for switched + hybrid systems. 8-year-deep open-permissive prior art. Used in ETH RSL's ANYmal locomotion + humanoid research. Architectural counterpart to Crocoddyl (round-8) for SQP-based optimization. **Closes a citation-audit gap** (cited by laas-cnrs-toulouse-humanoid-2003 round-26 entry).
