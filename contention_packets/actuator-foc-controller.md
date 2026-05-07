---
title: "actuator-foc-controller"
parent: "Invalidity Contentions"
nav_order: 10
layout: default
---

# Invalidity Contention Packet — `actuator-foc-controller`

**Generated:** 2026-05-07  
**Cross-cut tag:** `actuator-foc-controller`  
**Entries:** 6 (6 commons-grade, 0 draft)  
**Earliest disclosure:** 1929-07  
**Most recent disclosure:** 2025-03

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `actuator-foc-controller`.

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

### 1929-07 — Park's Transformation (dq0 transformation)

- **id:** `park-transformation-1929`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Robert H. Park
- **disclosure citation:** Park, Robert H. 'Two-reaction theory of synchronous machines — generalized method of analysis — Part I'. AIEE Transactions 48(3): 716-727, July 1929.
- **disclosed subsystems:** `actuator-foc-controller`, `actuator-bldc-controller`, `actuator-electric-direct-drive`

**Prior art notes:**

> Park's 1929 transformation is the mathematical foundation underlying FOC (Field-Oriented Control) of every modern brushless DC and AC servo motor in humanoid platforms. Anticipates with 97 years of prior art: (1) the dq0 reference-frame transformation as the basis for vector control — every modern humanoid actuator controller (Moteus, ODrive, SimpleFOC, T-Motor, plus closed proprietary controllers) uses this transformation; (2) the decoupling of torque-producing and flux-producing current components — foundational for any motor-control humanoid IP. Modern claims on FOC implementations in humanoid actuators all face this 97-year academic prior art.

**Sources:**

1. Park, R.H. 'Two-reaction theory of synchronous machines, Part I'. AIEE Trans. 48(3): 716-727, 1929.
2. Park, R.H. 'Two-reaction theory of synchronous machines, Part II'. AIEE Trans. 52(2): 352-355, 1933.
3. Krause, P.C., Wasynczuk, O., Sudhoff, S.D. Analysis of Electric Machinery and Drive Systems (textbook lineage).

---

### 2017 — ODrive

- **id:** `odrive`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** ODrive Robotics
- **disclosure citation:** Sirkin, Oskar. ODrive open hardware release, 2017.
- **disclosed subsystems:** `actuator-bldc-controller`, `actuator-foc-controller`

**Prior art notes:**

> ODrive is significant prior art for open BLDC controller designs. Has been used in countless academic and hobbyist robotics projects since 2017.

**Sources:**

1. odriverobotics.com
2. ODrive GitHub repositories.

---

### 2019 — mjbots Moteus

- **id:** `mjbots-moteus`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** mjbots Robotic Systems (Josh Katz)
- **disclosure citation:** Katz, Josh (mjbots). Moteus controller release, 2019.
- **disclosed subsystems:** `actuator-bldc-controller`, `actuator-foc-controller`, `software-mjbots-stack`

**Prior art notes:**

> mjbots Moteus is foundational prior art for compact open BLDC controllers in legged robotics. Used in Berkeley Humanoid, Upkie, and many academic platforms.

**Sources:**

1. mjbots.com
2. Moteus GitHub repositories.

---

### 2020 — SimpleFOC

- **id:** `simplefoc`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** SimpleFOC community
- **disclosure citation:** Skuric, Antun et al. SimpleFOC library release, 2020.
- **disclosed subsystems:** `actuator-bldc-controller`, `actuator-foc-controller`

**Prior art notes:**

> SimpleFOC is significant prior art for educational/open FOC implementations. Has lowered the barrier to entry for hobbyist robotics actuator development.

**Sources:**

1. simplefoc.com
2. SimpleFOC GitHub.

---

### 2022 — Upkie

- **id:** `upkie`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** Stéphane Caron and contributors
- **disclosure citation:** Caron, S. et al. Upkie public release, 2022.
- **disclosed subsystems:** `actuator-electric-quasi-direct-drive`, `actuator-bldc-controller`, `actuator-foc-controller`, `mechanism-wheeled-balancing`, `control-reduced-order-model`, `control-mpc`, `sensing-imu`, `power-li-po`, `software-mjbots-stack`, `software-ros2`

**Prior art notes:**

> Upkie demonstrates fully-open wheeled-bipedal balancing using commodity mjbots actuators. Anticipates cost-effective wheeled-humanoid designs.

**Sources:**

1. github.com/upkie
2. Caron, S. publications and project documentation.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `864caf4`.*
