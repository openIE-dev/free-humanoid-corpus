---
title: "actuator-bldc-controller"
parent: "Invalidity Contentions"
nav_order: 2
layout: default
---

# Invalidity Contention Packet — `actuator-bldc-controller`

**Generated:** 2026-05-07  
**Cross-cut tag:** `actuator-bldc-controller`  
**Entries:** 11 (11 commons-grade, 0 draft)  
**Earliest disclosure:** 1929-07  
**Most recent disclosure:** 2022

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `actuator-bldc-controller`.

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

### 2013 — MIT Cheetah

- **id:** `mit-cheetah`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** MIT Biomimetic Robotics Lab (Sangbae Kim)
- **disclosure citation:** Seok, S. et al. 'Design principles for energy-efficient legged locomotion and implementation on the MIT Cheetah robot.' IEEE/ASME Transactions on Mechatronics 20(3), 2015. Earlier ICRA 2013 disclosure.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `actuator-bldc-controller`, `mechanism-quadrupedal-locomotion`, `control-mpc`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> First-generation MIT Cheetah established the design principles for high-torque electric quadrupeds. Seok 2015 T-Mech paper provides foundational design-principles disclosure that anticipates many subsequent legged-robot actuation claims.

**Sources:**

1. Seok, S. et al. IEEE/ASME T-Mech 20(3), 2015.
2. MIT Biomimetic Robotics Lab publications.

---

### 2014 — MIT Cheetah 2

- **id:** `mit-cheetah-2`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** MIT Biomimetic Robotics Lab (Sangbae Kim)
- **disclosure citation:** Park, H.-W. et al. 'High-speed bounding with the MIT Cheetah 2: Control design and experiments.' International Journal of Robotics Research 36(2), 2017. Earlier ICRA disclosure 2014.
- **disclosed subsystems:** `actuator-electric-quasi-direct-drive`, `actuator-bldc-controller`, `sensing-proprioceptive-actuator`, `mechanism-quadrupedal-locomotion`, `control-mpc`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> MIT Cheetah 2 establishes the QDD actuator topology in a working high-speed legged robot. The Wensing 2017 T-RO paper 'Proprioceptive actuator design in the MIT Cheetah' is the foundational actuator design disclosure.

**Sources:**

1. Park, H.-W. et al. IJRR 36(2), 2017.
2. Wensing, P.M. et al. 'Proprioceptive actuator design in the MIT Cheetah.' IEEE T-RO 33(3), 2017.

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

### 2018 — MIT Cheetah 3

- **id:** `mit-cheetah-3`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** MIT Biomimetic Robotics Lab (Sangbae Kim)
- **disclosure citation:** Bledt, G. et al. 'MIT Cheetah 3: Design and Control of a Robust, Dynamic Quadruped Robot.' IROS 2018.
- **disclosed subsystems:** `actuator-electric-quasi-direct-drive`, `actuator-bldc-controller`, `sensing-proprioceptive-actuator`, `mechanism-quadrupedal-locomotion`, `control-mpc`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> Cheetah 3 establishes blind robust legged locomotion using only proprioceptive sensing — a significant prior art point against later vision-dependent legged-robot claims.

**Sources:**

1. Bledt, G. et al. IROS 2018.

---

### 2019 — MIT Mini Cheetah

- **id:** `mini-cheetah`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** MIT Biomimetic Robotics Lab (Sangbae Kim)
- **disclosure citation:** Katz, B. et al. 'Mini Cheetah: A Platform for Pushing the Limits of Dynamic Quadruped Control.' ICRA 2019.
- **disclosed subsystems:** `actuator-electric-quasi-direct-drive`, `actuator-bldc-controller`, `sensing-proprioceptive-actuator`, `mechanism-quadrupedal-locomotion`, `control-mpc`, `control-rl-policy`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> The QDD actuator topology (low gear ratio, high-torque BLDC, transparent backdrivability) is a foundational contribution. Establishes the design space for affordable dynamic legged robots.

**Sources:**

1. Katz, B. et al. ICRA 2019.
2. Wensing, P. et al. 'Proprioceptive actuator design in the MIT Cheetah.' IEEE T-RO 2017.

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

### 2021-06 — Unitree Go1

- **id:** `unitree-go1`
- **corpus:** private
- **ip status:** patented
- **creator:** Unitree Robotics
- **disclosure citation:** Unitree Robotics Go1 reveal, June 2021.
- **disclosed subsystems:** `actuator-electric-quasi-direct-drive`, `actuator-bldc-controller`, `mechanism-quadrupedal-locomotion`, `control-mpc`, `control-rl-policy`, `sensing-monocular-depth`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> Unitree Go1 actuator design is heavily anticipated by MIT Cheetah QDD prior art (Wensing 2017, Katz 2019). Pricing-driven commodification rather than novel IP.

**Sources:**

1. Unitree.com
2. Unitree technical specifications.

---

### 2021-11 — MIT Humanoid

- **id:** `mit-humanoid-2021`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Matthew Chignoli, Donghyun Kim, Elijah Stanger-Jones, Sangbae Kim; MIT Biomimetic Robotics Lab
- **disclosure citation:** Chignoli, Matthew; Kim, Donghyun; Stanger-Jones, Elijah; Kim, Sangbae. 'The MIT Humanoid Robot: Design, Motion Planning, and Control For Acrobatic Behaviors.' IEEE-RAS International Conference on Humanoid Robots (Humanoids 2020, virtual; presented November 2021), pp. 1-8. arXiv:2104.09025, April 2021.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `actuator-electric-quasi-direct-drive`, `actuator-bldc-controller`, `sensing-proprioceptive-actuator`, `sensing-imu`, `control-mpc`, `control-reduced-order-model`

**Prior art notes:**

> The MIT Humanoid (Chignoli-Kim et al. Humanoids 2020/arXiv 2021) is the canonical academic disclosure of dynamic whole-body humanoid locomotion using a quasi-direct-drive actuator topology with explicit actuator-dynamics-aware MPC, from the Sangbae Kim group (MIT Biomimetic Robotics Lab) that previously produced Mini Cheetah and Cheetah 3. Anticipates with element-by-element specificity: (1) QDD actuator topology extended from quadruped (Mini Cheetah, 2019) to humanoid biped — directly relevant to commercial claims on QDD humanoid IP (Berkeley Humanoid, Unitree H1/G1, Booster T1, much of the 2024-2026 humanoid wave employs QDD); (2) explicit actuator-dynamics-model integration into humanoid MPC (motor inertia, torque limits, current limits enter the OCP directly) — anticipates commercial claims on actuator-aware humanoid control; (3) acrobatic-capable lightweight (~24 kg) electric humanoid as a research platform — anticipates the lightweight-humanoid commercial form factor. The Sangbae Kim lineage (Cheetah 1/2/3 → Mini Cheetah → MIT Humanoid) is one of the deepest legged-robot academic chains and the MIT Humanoid arXiv preprint provides full design documentation. Modern QDD-humanoid IP filings face this 5-year-deep academic anchor.

**Sources:**

1. Chignoli, M.; Kim, D.; Stanger-Jones, E.; Kim, S. 'The MIT Humanoid Robot: Design, Motion Planning, and Control For Acrobatic Behaviors.' IEEE-RAS Humanoids 2020 (presented Nov 2021); arXiv:2104.09025.
2. Katz, B.; Di Carlo, J.; Kim, S. 'Mini Cheetah: A Platform for Pushing the Limits of Dynamic Quadruped Control.' IEEE ICRA 2019 (lineage: QDD actuator).
3. Wensing, P. et al. 'Proprioceptive actuator design in the MIT Cheetah: Impact mitigation and high-bandwidth physical interaction for dynamic legged robots.' IEEE T-RO 33(3), 2017.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `5228ded`.*
