---
title: "control-optimal-control"
parent: "Invalidity Contentions"
nav_order: 88
layout: default
---

# Invalidity Contention Packet — `control-optimal-control`

**Generated:** 2026-05-09  
**Cross-cut tag:** `control-optimal-control`  
**Entries:** 3 (3 commons-grade, 0 draft)  
**Earliest disclosure:** 1960-03  
**Most recent disclosure:** 2017-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-optimal-control`.

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

### 1960-03 — Kalman filter + LQR (Linear-Quadratic Regulator)

- **id:** `kalman-filter-lqr-1960`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Stanford University + RIAS; Rudolf E. Kálmán
- **disclosure citation:** Kalman, R. E. 'A New Approach to Linear Filtering and Prediction Problems'. Journal of Basic Engineering 82(1) 1960. Kalman, R. E. 'Contributions to the Theory of Optimal Control'. Bol. Soc. Mat. Mexicana 5(2) 1960. Stanford University + RIAS.
- **disclosed subsystems:** `control-state-estimation`, `control-kalman-filter`, `control-lqr`, `control-optimal-control`

**Prior art notes:**

> The Kalman filter + LQR (Kalman 1960) is the foundational state estimation + optimal control framework. 65-year-deep public-domain prior art. Used in essentially every robotic system. Direct shielding for any commercial humanoid claim involving state estimation, sensor fusion, or feedback control. **The underlying mathematics of every IMU-based attitude estimator** + every GPS-INS-DVL fusion stack in the corpus's submersible / wheeled / centaur entries.

**Sources:**

1. Kalman, R. E. Journal of Basic Engineering 82(1) 1960.
2. Kalman, R. E. Bol. Soc. Mat. Mexicana 5(2) 1960.

---

### 1989-08 — Model Predictive Control (MPC)

- **id:** `mpc-garcia-prett-morari-1989`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Caltech (Morari) + Shell (Prett) + IBM (Garcia)
- **disclosure citation:** Garcia, C. E., Prett, D. M., Morari, M. 'Model Predictive Control: Theory and Practice—a Survey'. Automatica 25(3) 1989. Antecedents: Richalet 1976, Cutler-Ramaker 1980 DMC.
- **disclosed subsystems:** `control-mpc`, `control-receding-horizon`, `control-optimal-control`

**Prior art notes:**

> MPC (Garcia-Prett-Morari Automatica 1989) is the foundational Model Predictive Control academic survey. 36-year-deep public-domain prior art. The substrate of: Tassa iLQG (corpus), Crocoddyl (corpus), Howell-Tassa MuJoCo MPC (corpus round-11), OCS2 (round-33 entry below), Capture Point (corpus round-21), every humanoid + quadruped MPC controller in the corpus.

**Sources:**

1. Garcia, C. E., Prett, D. M., Morari, M. Automatica 25(3) 1989.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `bd98079`.*
