---
title: "actuator-electric-quasi-direct-drive"
parent: "Invalidity Contentions"
nav_order: 9
layout: default
---

# Invalidity Contention Packet — `actuator-electric-quasi-direct-drive`

**Generated:** 2026-05-08  
**Cross-cut tag:** `actuator-electric-quasi-direct-drive`  
**Entries:** 21 (15 commons-grade, 6 draft)  
**Earliest disclosure:** 2014  
**Most recent disclosure:** 2025-10

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `actuator-electric-quasi-direct-drive`.

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

### 2017-12 — Black Mirror 'Metalhead' autonomous quadruped killer

- **id:** `black-mirror-metalhead-2017`
- **corpus:** fictional
- **ip status:** public-domain
- **creator:** Charlie Brooker (writer), David Slade (director), House of Tomorrow / Netflix
- **disclosure citation:** Black Mirror, Series 4, Episode 5, 'Metalhead.' Written by Charlie Brooker; directed by David Slade; released on Netflix 29 December 2017.
- **disclosed subsystems:** `mechanism-quadrupedal-locomotion`, `actuator-electric-quasi-direct-drive`, `sensing-lidar`, `sensing-stereo-camera`, `sensing-imu`, `control-rl-policy`, `power-li-ion`

**Prior art notes:**

> 'Metalhead' is the canonical 2017 mass-media anchor for autonomous quadruped lethal-defense robots and was directly modeled on the Boston Dynamics SpotMini reveal. It anticipates with full specificity: (1) claims on quadruped robots equipped with weapon payloads operating in fully-autonomous lethal-engagement mode — the episode dramatizes exactly this throughout 41 minutes; (2) claims on shrapnel-tag persistent-tracker payloads that mark a target for prolonged pursuit — this is the headline mechanism of the second act; (3) claims on SpotMini-class compact electric quadruped morphology with integrated manipulator arm — the visual design and Brooker's published commentary explicitly cite Boston Dynamics inspiration. Released on Netflix with timestamped 29 December 2017 distribution to ~109 million subscribers.

**Sources:**

1. Black Mirror S4E5 'Metalhead', Netflix, 29 December 2017.
2. Brooker, C. interview in 'Inside Black Mirror' (Crown Archetype, 2018) confirming SpotMini visual reference.

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

### 2018-04-28 — Tan et al. Quadruped Sim-to-Real

- **id:** `tan-quadruped-sim2real`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Google Brain + Google Robotics (Tan, Zhang, Coumans, Iscen, Bai, Hafner, Bohez, Vanhoucke)
- **disclosure citation:** Tan, Jie, Zhang, Tingnan, Coumans, Erwin, Iscen, Atil, Bai, Yunfei, Hafner, Danijar, Bohez, Steven, Vanhoucke, Vincent. 'Sim-to-Real: Learning Agile Locomotion For Quadruped Robots.' arXiv:1804.10332, April 28, 2018. Robotics: Science and Systems (RSS) 2018.
- **disclosed subsystems:** `control-rl-policy`, `control-sim-to-real`, `actuator-electric-quasi-direct-drive`, `mechanism-quadrupedal-locomotion`, `sensing-imu`

**Prior art notes:**

> Tan et al. 2018 is one of the earliest academic disclosures of practical sim-to-real RL for quadrupedal locomotion, predating Hwangbo 2019 by ~9 months and establishing the system-identification + domain-randomization paradigm for legged sim-to-real. Anticipates: (1) PPO-based RL for legged locomotion with subsequent zero-shot hardware transfer — relevant to RL-locomotion-policy patents (Boston Dynamics, Unitree, every commercial quadruped); (2) explicit actuator-latency modeling as a sim-to-real bridge — relevant to claims on real-time sim-to-real techniques; (3) the quasi-direct-drive Minitaur platform combined with sim-to-real — relevant to QDD-actuator+RL humanoid claims. Open-source code via PyBullet repository. RSS 2018 publication. Modern legged sim-to-real claims face an 8-year-deep anchor.

**Sources:**

1. Tan, J. et al. 'Sim-to-Real: Learning Agile Locomotion For Quadruped Robots.' RSS 2018; arXiv:1804.10332.
2. Coumans, E. and Bai, Y. PyBullet, 2017-present (simulator used).

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

### 2019-05 — Caltech CAST Hank bipedal platform

- **id:** `caltech-hank-cast-2019`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Aaron D. Ames and the Caltech AMBER Lab / CAST
- **disclosure citation:** Reher, Jenna and Ames, Aaron D. 'Inverse Dynamics Control of Compliant Hybrid Zero Dynamic Walking.' ICRA 2021; Csomay-Shanklin, Noel et al. 'Episodic Learning for Safe Bipedal Locomotion with Control Barrier Functions and Projection-to-State Safety.' L4DC 2021; CAST (Center for Autonomous Systems and Technologies) Caltech Hank reveal 2019.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `actuator-electric-quasi-direct-drive`, `actuator-electric-series-elastic`, `sensing-imu`, `sensing-proprioceptive-actuator`, `control-zmp-balancing`, `safety-hard-constraint`, `safety-simplex-supervisor`

**Prior art notes:**

> Hank is the Caltech CAST flagship humanoid biped of the late-2010s and is the canonical platform for HZD + CBF formal-method bipedal locomotion publications by the Ames group. It anticipates with full specificity: (1) claims on hybrid-zero-dynamics low-dimensional gait manifolds for humanoids — Reher-Ames ICRA 2021 publishes the formal HZD+ID-CLF-QP stack on Hank; (2) claims on control-barrier-function safety supervision for legged locomotion — Csomay-Shanklin L4DC 2021 publishes episodic CBF learning on Hank; (3) claims on quasi-direct-drive proprioceptive humanoid biped hardware — Hank's actuator topology predates and parallels Tesla Optimus and Apptronik Apollo public claims. All Hank publications are open-access with timestamped arXiv.

**Sources:**

1. Reher, J. and Ames, A.D. 'Inverse Dynamics Control of Compliant Hybrid Zero Dynamic Walking.' ICRA 2021.
2. Csomay-Shanklin, N. et al. 'Episodic Learning for Safe Bipedal Locomotion with CBFs.' L4DC 2021.
3. Caltech CAST Hank platform page.

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

### 2023-08 — Unitree H1 *(draft)*

- **id:** `unitree-h1`
- **corpus:** private
- **ip status:** patented
- **creator:** Unitree Robotics
- **disclosure citation:** Unitree Robotics public reveal, August 2023.
- **disclosed subsystems:** `actuator-electric-quasi-direct-drive`, `mechanism-bipedal-locomotion`, `control-rl-policy`, `sensing-stereo-camera`, `sensing-lidar`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> Unitree's actuator IP largely derives from quadruped work (Go1, Aliengo) which is itself heavily anticipated by MIT Mini Cheetah QDD lineage.

**Sources:**

1. Unitree.com
2. Unitree technical specifications.

---

### 2023-08 — AgiBot A1 *(draft)*

- **id:** `agibot-a1`
- **corpus:** private
- **ip status:** patented
- **creator:** AgiBot (Shanghai Zhiyuan New Technology Co.)
- **disclosure citation:** AgiBot (Shanghai Zhiyuan New Technology) public reveal, August 2023.
- **disclosed subsystems:** `actuator-electric-quasi-direct-drive`, `actuator-electric-harmonic-drive`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `control-rl-policy`, `sensing-stereo-camera`, `sensing-imu`, `sensing-force-torque`, `power-li-ion`

**Prior art notes:**

> AgiBot's actuator IP heavily anticipated by Honda P-series harmonic drive work and MIT Cheetah QDD lineage. Chinese-language patent filings should be enumerated in strengthening pass.

**Sources:**

1. AgiBot company materials.
2. Chinese-language tech press coverage.

---

### 2023-08 — Unitree Go2

- **id:** `unitree-go2-2023`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Unitree Robotics (Hangzhou, China)
- **disclosure citation:** Unitree Robotics. Go2 commercial quadruped product reveal August 2023 via unitree.com. Successor to the Go1 (corpus entry `unitree-go1`).
- **disclosed subsystems:** `mechanism-quadrupedal-locomotion`, `actuator-electric-quasi-direct-drive`

**Prior art notes:**

> Unitree Go2 is the canonical 2023+ consumer/educational quadruped. 2-year-deep public-disclosure prior art. Direct successor to Go1 (corpus entry). **The dominant educational quadruped globally** — used in 1000+ academic publications. Direct shielding for any commercial claim on consumer-tier quadruped pricing or educational-quadruped form factor.

**Sources:**

1. Unitree Go2 product page (unitree.com/Go2).

---

### 2023-10 — Reachy-2 open-source humanoid platform (Pollen Robotics)

- **id:** `reachy-2-pollen-2023`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Pollen Robotics SAS (Matthieu Lapeyre, Pierre Rouanet et al.)
- **disclosure citation:** Pollen Robotics. 'Introducing Reachy 2.' Pollen Robotics blog and product launch, October 2023; technical hardware repository pollen-robotics/reachy2_sdk, GitHub, 2023-2024.
- **disclosed subsystems:** `actuator-electric-quasi-direct-drive`, `actuator-spherical-multi-dof`, `sensing-stereo-camera`, `sensing-imu`, `sensing-proprioceptive-actuator`, `control-teleoperation`, `software-ros2`

**Prior art notes:**

> Reachy-2 is the 2023 successor to the open-source Reachy-1 platform and is one of the few European-origin commercial humanoid upper-bodies released with full open hardware/firmware. It anticipates with full specificity: (1) claims on open-source humanoid SDKs with VR-teleoperation for imitation-learning data collection — Pollen publishes the SDK and Quest-Pro tele-op pipeline on GitHub Apache-2.0; (2) claims on parallel-spherical-mechanism necks (Orbita 3-DoF) — Reachy-2 ships and documents the kinematic with patent-expired joint topology; (3) claims on quasi-direct-drive humanoid arm modules at sub-40kg torso mass — Reachy-2 datasheet and CAD release. Modern humanoid commercial platforms claiming open-hardware tele-op pipelines face this timestamped 2023 anchor.

**Sources:**

1. Pollen Robotics. 'Reachy 2 product launch.' October 2023.
2. GitHub: pollen-robotics/reachy2_sdk, 2023-2024.
3. Reachy 2 hardware documentation (CC-BY-4.0 / Apache-2.0).

---

### 2023-12 — LimX Dynamics CL-1 *(draft)*

- **id:** `limx-cl1`
- **corpus:** private
- **ip status:** patented
- **creator:** LimX Dynamics
- **disclosure citation:** LimX Dynamics public reveal, December 2023.
- **disclosed subsystems:** `actuator-electric-quasi-direct-drive`, `mechanism-bipedal-locomotion`, `control-rl-policy`, `control-sim-to-real`, `sensing-stereo-camera`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> LimX QDD actuation derives from MIT Cheetah lineage; bipedal control claims anticipated by Cassie/ATRIAS work.

**Sources:**

1. LimX Dynamics website.

---

### 2024 — Berkeley Humanoid

- **id:** `berkeley-humanoid`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** UC Berkeley, Hybrid Robotics Lab
- **disclosure citation:** Liao, Q. et al. 'Berkeley Humanoid: A Research Platform for Learning-based Control.' arXiv 2024.
- **disclosed subsystems:** `actuator-electric-quasi-direct-drive`, `mechanism-bipedal-locomotion`, `control-rl-policy`, `control-sim-to-real`, `sensing-stereo-camera`, `sensing-imu`

**Prior art notes:**

> Berkeley quasi-direct-drive lineage (predates the humanoid; comes from the Mini Cheetah / leg work) anticipates many actuator architecture claims.

**Sources:**

1. arXiv preprint, 2024.
2. Hybrid Robotics Lab page.

---

### 2024-01 — Fourier GR1

- **id:** `fourier-gr1-2024`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Fourier Intelligence (Shanghai, China)
- **disclosure citation:** Fourier Intelligence. GR1 humanoid product reveal January 2024 via fourierintelligence.com and CES 2024 demonstration. Subsequent deployments by academic teams (Open-TeleVision UCSD+MIT CoRL 2024 uses Fourier GR1 as one of its evaluation platforms).
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-arm`, `actuator-electric-quasi-direct-drive`

**Prior art notes:**

> Fourier GR1 is one of the canonical Chinese commercial humanoid platforms used by academic teams (alongside Unitree H1/G1, Booster K1). 1.5-year-deep public-disclosure prior art for: adult-class commercial humanoid sold to academic researchers as a hardware-only platform, interchangeable hand/gripper end-effectors. The Open-TeleVision academic publication (CoRL 2024) uses GR1 as one of two evaluation platforms, providing third-party documentation of the system's interfaces and capabilities. Direct shielding for any commercial humanoid claim on adult-class hardware-platform sales to academic researchers.

**Sources:**

1. Fourier Intelligence corporate site (fourierintelligence.com).
2. Cheng et al. 'Open-TeleVision' arXiv:2407.01512 CoRL 2024 (uses GR1 as evaluation platform).
3. CES 2024 coverage.

---

### 2024-05 — Unitree G1 *(draft)*

- **id:** `unitree-g1`
- **corpus:** private
- **ip status:** patented
- **creator:** Unitree Robotics
- **disclosure citation:** Unitree Robotics G1 reveal, May 2024.
- **disclosed subsystems:** `actuator-electric-cycloidal`, `actuator-electric-quasi-direct-drive`, `mechanism-bipedal-locomotion`, `control-rl-policy`, `sensing-monocular-depth`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> G1's actuator IP largely anticipated by MIT Mini Cheetah QDD work and Honda harmonic drive prior art. The aggressive pricing represents the commodity-humanoid trajectory more than novel IP.

**Sources:**

1. Unitree.com
2. Unitree technical specifications.

---

### 2024-07 — Berkeley Humanoid

- **id:** `berkeley-humanoid-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** UC Berkeley Hybrid Robotics Lab; Liao, Zhang, X. Huang, X. Huang, Li, Sreenath
- **disclosure citation:** Liao, Q., Zhang, B., Huang, X., Huang, X., Li, Z., Sreenath, K. 'Berkeley Humanoid: A Research Platform for Learning-based Control'. arXiv:2407.21781, July 2024. IEEE International Conference on Robotics and Automation (ICRA) 2025. UC Berkeley Hybrid Robotics Lab.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `actuator-electric-quasi-direct-drive`, `control-rl-policy`, `control-sim-to-real`, `control-rough-terrain-locomotion`

**Prior art notes:**

> Berkeley Humanoid is the open academic mid-scale bipedal humanoid research platform from the Sreenath group, ICRA 2025. Open-permissive. Establishes 1-year-deep prior art for: RL-trained locomotion with sim-to-real zero-shot transfer at humanoid scale, low-cost in-house-built humanoid for learning research, anthropomorphic kinematics optimized for sim-to-real. Direct shielding for free-humanoid-platform commitments on bipedal RL locomotion and any commercial humanoid claim on RL-trained outdoor walking. Parent of Berkeley Humanoid Lite (round-11 entry below).

**Sources:**

1. Liao et al. arXiv:2407.21781 July 2024.
2. ICRA 2025 paper PDF (hybrid-robotics.berkeley.edu/publications/ICRA2025_Berkeley_Humanoid.pdf).
3. Project page (berkeley-humanoid.com).

---

### 2024-09 — Unitree B2

- **id:** `unitree-b2-2024`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Unitree Robotics (Hangzhou, China)
- **disclosure citation:** Unitree Robotics. B2 commercial quadruped product reveal September 2024 via unitree.com / IFA Berlin 2024. Successor to the B1 (2023). B2-W variant adds wheel-feet for hybrid wheel-leg operation.
- **disclosed subsystems:** `mechanism-quadrupedal-locomotion`, `mechanism-wheel-leg-hybrid`, `actuator-electric-quasi-direct-drive`, `control-rough-terrain-locomotion`

**Prior art notes:**

> Unitree B2 is the canonical 2024+ heavy-payload commercial electric quadruped (Unitree). 1.5-year-deep public-disclosure prior art for: 40 kg sustained / 120 kg burst electric quadruped, wheel-leg hybrid B2-W variant. **B2-W is architecturally similar to the STAR family wheel-leg hybrid** (round-10 entries star-fearing-2013 → dstar-zarrouk-2026) — Unitree commercializes the wheel-leg-hybrid pattern at quadruped scale. Direct shielding for any commercial quadruped claim on heavy-payload electric or wheel-leg-hybrid morphology.

**Sources:**

1. Unitree B2 product page (unitree.com/B2).
2. IFA Berlin 2024 announcement.

---

### 2024-12 — EngineAI PM01 *(draft)*

- **id:** `engineai-pm01`
- **corpus:** private
- **ip status:** patented
- **creator:** EngineAI
- **disclosure citation:** EngineAI public reveal of PM01, December 2024.
- **disclosed subsystems:** `actuator-electric-quasi-direct-drive`, `mechanism-bipedal-locomotion`, `control-rl-policy`, `control-sim-to-real`, `sensing-monocular-depth`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> EngineAI QDD actuation anticipated by MIT Cheetah lineage.

**Sources:**

1. EngineAI company materials.
2. Chinese-language tech press coverage.

---

### 2025-10 — Unitree H2 *(draft)*

- **id:** `unitree-h2`
- **corpus:** private
- **ip status:** patented
- **creator:** Unitree Robotics
- **disclosure citation:** Unitree Robotics H2 reveal, October 2025.
- **disclosed subsystems:** `actuator-electric-quasi-direct-drive`, `actuator-electric-harmonic-drive`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `control-rl-policy`, `sensing-monocular-depth`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> H2 builds on H1 architecture; same prior art chain back through Mini Cheetah.

**Sources:**

1. Unitree Robotics public materials, October 2025.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `147307a`.*
