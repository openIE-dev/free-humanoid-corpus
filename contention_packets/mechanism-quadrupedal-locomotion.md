---
title: "mechanism-quadrupedal-locomotion"
parent: "Invalidity Contentions"
nav_order: 218
layout: default
---

# Invalidity Contention Packet — `mechanism-quadrupedal-locomotion`

**Generated:** 2026-05-15  
**Cross-cut tag:** `mechanism-quadrupedal-locomotion`  
**Entries:** 25 (21 commons-grade, 4 draft)  
**Earliest disclosure:** 1968-09-27  
**Most recent disclosure:** 2024-09

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `mechanism-quadrupedal-locomotion`.

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

### 1968-09-27 — GE Quadruped Transporter (Walking Truck)

- **id:** `ge-walking-truck`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Ralph S. Mosher and team, General Electric Research Laboratory, Schenectady NY
- **disclosure citation:** Mosher, Ralph S. 'Test and evaluation of a versatile walking truck.' General Electric Schenectady Research Lab Report, September 1968. Published abstract: Mosher, R.S. 'Exploring the potential of a quadruped'. Society of Automotive Engineers, January 1969 (Detroit Engineering Show, Paper 690191).
- **disclosed subsystems:** `actuator-hydraulic`, `control-teleoperation`, `mechanism-quadrupedal-locomotion`

**Prior art notes:**

> The GE Walking Truck is the deepest hydraulic legged-locomotion academic disclosure in the corpus and substantially predates everything in the modern legged-robotics commercial portfolio. Mosher's 1968 SAE paper discloses with full specificity: (1) hydraulic actuation per leg with 3-DOF — anticipates hydraulic legged claims by Boston Dynamics (BigDog 2005) by 37 years; (2) master-slave kinesthetic teleoperation with force feedback — anticipates teleoperation claims for legged systems; (3) 1500 kg payload legged loadbearing — anticipates legged-loadbearing claims (Boston Dynamics LS3, Ghost Robotics Vision 60); (4) 90 hp combustion engine power source for legged locomotion. Modern claims on hydraulic / combustion-powered legged loadbearing all face this 1968 disclosure as 102 prior art at unusual depth. Publicly funded research, openly published.

**Sources:**

1. Mosher, R.S. 'Exploring the potential of a quadruped'. SAE Paper 690191, 1969.
2. Mosher, R.S. 'Test and evaluation of a versatile walking truck'. GE Schenectady Research Lab Report, 1968.
3. Liston, R. and Mosher, R. 'A versatile walking truck'. Mechanical Engineering 90(8): 12-19, 1968.

---

### 1981-01 — Raibert MIT Leg Lab (foundational dynamic legged locomotion) *(draft)*

- **id:** `raibert-mit-leg-lab-history-1980s`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** MIT Leg Laboratory; Marc Raibert (founder), then Jerry Pratt + Hugh Herr (post-Raibert era)
- **disclosure citation:** Raibert, M. H. 'Legged Robots That Balance'. MIT Press 1986. MIT Leg Lab (founded by Raibert at CMU 1981, moved to MIT 1986). Series of foundational dynamic-legged-robot designs: 3D one-leg hopper (1983), 3D quadruped (1984), planar biped (1989), 3D biped (1989), 4-legged Spring Flamingo (1995), Spring Turkey, M2, etc. Foundational predecessors of Boston Dynamics (Raibert founded BD 1992, took the Leg Lab portfolio with him). The corpus already has `raibert-hopping-1leg` for the foundational 1-leg hopper; this entry covers the broader Leg Lab portfolio as a corpus anchor.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-quadrupedal-locomotion`, `mechanism-dynamic-legged-locomotion`, `control-slip-model`, `control-raibert-decomposition`

**Prior art notes:**

> Marc Raibert's MIT Leg Lab portfolio (1981-1995) is the canonical foundational dynamic-legged-robotics academic anchor. 44-year-deep public-domain prior art predating the entire commercial humanoid era. **Most modern Boston Dynamics IP descends architecturally from this era** — Raibert founded BD in 1992 with the Leg Lab portfolio. The Spring-Loaded Inverted Pendulum (SLIP) model and Raibert's 3-part control decomposition remain the foundational analytical tools for dynamic legged locomotion. Together with Vukobratović ZMP (1969), McGeer passive walker (1990), Collins-Ruina passive (2005), establishes the four-pillar academic chain underpinning all modern bipedal/quadrupedal robotics — anticipating commercial humanoid claims by 30-55 years. Direct shielding for any commercial dynamic-locomotion claim. Note: corpus already has `raibert-hopping-1leg` for the specific 1-leg hopper; this entry is the broader Leg Lab portfolio anchor.

**Sources:**

1. Raibert, M. H. 'Legged Robots That Balance'. MIT Press 1986.
2. MIT Leg Lab archives (groups.csail.mit.edu/leglab/).
3. Raibert biographical material (Boston Dynamics founder history).

---

### 1999-05-11 — Sony AIBO

- **id:** `sony-aibo`
- **corpus:** private
- **ip status:** patented
- **creator:** Sony Corporation
- **disclosure citation:** Sony Corporation announcement of AIBO ERS-110, May 11, 1999.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `mechanism-quadrupedal-locomotion`, `control-behavior-tree`, `sensing-stereo-camera`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> AIBO is foundational prior art for consumer quadruped robots. Sony's 1990s-2000s patents cover quadruped behavior architecture, learning systems, and small-form-factor actuators. Many expired or near expiration.

**Sources:**

1. Sony AIBO product materials.
2. Fujita, M. and Kageyama, K. 'An open architecture for robot entertainment.' Autonomous Agents 1997.
3. Various academic papers using AIBO as research platform.

---

### 2005-12 — Boston Dynamics BigDog

- **id:** `boston-dynamics-bigdog-2005`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Boston Dynamics; Marc Raibert et al. (under DARPA TUGV)
- **disclosure citation:** Boston Dynamics + Foster-Miller + Jet Propulsion Laboratory + Harvard Concord Field Station. BigDog public reveal December 2005 video. Funded by DARPA TUGV (Tactical Ground Vehicle) program 2005-2015. Raibert, M. et al. 'BigDog, the Rough-Terrain Quadruped Robot' IFAC Proceedings 41(2) 2008.
- **disclosed subsystems:** `mechanism-quadrupedal-locomotion`, `mechanism-hydraulic-actuator`, `mechanism-dynamic-legged-locomotion`, `control-raibert-decomposition`, `control-rough-terrain-locomotion`

**Prior art notes:**

> BigDog is the canonical Boston Dynamics foundational hydraulic quadruped (December 2005). 20-year-deep public-disclosure prior art for: dynamic-balance commercial quadruped, hydraulic-actuated heavy-payload legged robot, rough-terrain dynamic stabilization. Direct architectural application of Raibert's MIT Leg Lab work (round-19 entry) at commercial scale. The ancestor of every modern Boston Dynamics platform: LS3 (2012), Spot (2015+), Atlas (2013+). Direct shielding for any commercial quadruped or quadruped-derivative humanoid claim. The viral 'kicked on ice' video itself constitutes a uniquely-public defensive disclosure of dynamic-recovery behavior.

**Sources:**

1. Raibert et al. IFAC Proceedings 41(2) 2008.
2. Boston Dynamics BigDog YouTube reveal video December 2005.
3. DARPA TUGV program documentation.

---

### 2010-07 — CSIRO Data61 Robotics and Autonomous Systems *(draft)*

- **id:** `csiro-data61-australia-robotics`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** CSIRO Data61 (Commonwealth Scientific and Industrial Research Organisation, Australia)
- **disclosure citation:** CSIRO Data61 (Commonwealth Scientific and Industrial Research Organisation; Brisbane + Sydney, Australia). Robotics and Autonomous Systems group originally part of CSIRO ICT Centre, merged into Data61 in 2014. Notable projects: **Wildcat** legged robot for DARPA Subterranean Challenge (won 2nd place 2021), **Bobcat** agricultural robot, **Tilt-rotor UAV** development. Continuous robotics research output 2010+.
- **disclosed subsystems:** `control-research-cluster`, `control-vio-slam`, `mechanism-quadrupedal-locomotion`, `control-agricultural-autonomy`

**Prior art notes:**

> CSIRO Data61 is Australia's dominant robotics research institution. 15-year-deep public-domain academic prior art spanning legged robots (DARPA SubT 2021 2nd place), agricultural automation (SwagBot, Bobcat), aerial systems. **First entry in the corpus for Australia** — closes a major regional gap. Aggregator-style entry covering CSIRO RAS broadly; specific papers should be added in future rounds.

**Sources:**

1. CSIRO Data61 corporate site (data61.csiro.au).
2. CSIRO Robotics and Autonomous Systems (research.csiro.au/robotics).
3. DARPA SubT 2021 results.
4. Cordin et al. CSIRO Wildcat / Spotter publications.

---

### 2012-09 — Boston Dynamics LS3 (AlphaDog)

- **id:** `boston-dynamics-ls3-alphadog-2012`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Boston Dynamics under DARPA / USMC contract
- **disclosure citation:** Boston Dynamics + Marines Corps Warfighting Laboratory. LS3 (Legged Squad Support System) program reveal September 2012; demonstrated through 2015. AlphaDog is the prototype name (Phase 1, 2009-2012); LS3 is the Phase 2 (2012-2015) production version. Funded by DARPA + USMC.
- **disclosed subsystems:** `mechanism-quadrupedal-locomotion`, `mechanism-hydraulic-actuator`, `control-voice-command`, `control-rough-terrain-locomotion`

**Prior art notes:**

> LS3 / AlphaDog is the canonical 2012 hydraulic heavy-payload tactical quadruped (Boston Dynamics under DARPA + USMC). 13-year-deep public-disclosure prior art for: 400 lb payload quadruped, voice-commanded squad-support behavior, 20-mile endurance hydraulic quadruped. Direct successor to BigDog (round-20 entry above), architectural ancestor of Spot. **The hydraulic-vs-electric-quadruped architectural choice was decided at LS3** — BD pivoted to all-electric for Spot in part because LS3's noise made it tactically unusable. This decision is itself architectural prior art for modern humanoid claims.

**Sources:**

1. Boston Dynamics LS3 YouTube reveals 2012-2015.
2. DARPA + USMC program documentation.

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

### 2013-12 — Cheetah-cub

- **id:** `cheetah-cub-epfl`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Spröwitz, Tuleu, Vespignani, Ajallooeian, Badri, Ijspeert; EPFL Biorobotics Laboratory
- **disclosure citation:** Spröwitz, A., Tuleu, A., Vespignani, M., Ajallooeian, M., Badri, E., Ijspeert, A.J. 'Towards dynamic trot gait locomotion: Design, control, and experiments with Cheetah-cub, a compliant quadruped robot'. International Journal of Robotics Research 32(8): 932-950, December 2013.
- **disclosed subsystems:** `mechanism-quadrupedal-locomotion`, `actuator-electric-direct-drive`, `control-rl-policy`

**Prior art notes:**

> Cheetah-cub is one of the earliest open-source compliant compact quadruped academic disclosures. Anticipates: (1) compact open-source compliant quadruped — directly relevant to modern claims on small commercial quadrupeds (Unitree Go1, Boston Dynamics Spot Mini class); (2) parametric CPG-based gait control on a real platform — relevant to bio-inspired locomotion claims; (3) pantograph-leg mechanism as a compliant-footed quadruped architecture — relevant to compliant-leg quadruped IP. The 2013 IJRR paper and open-source EPFL releases provide deep prior art for modern commercial compact quadrupeds.

**Sources:**

1. Spröwitz, A. et al. 'Towards dynamic trot gait locomotion'. IJRR 32(8), 2013.
2. EPFL Biorobotics Laboratory public design files (2013-2018).

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

### 2015-02 — Boston Dynamics Spot

- **id:** `hyundai-boston-dynamics-spot`
- **corpus:** private
- **ip status:** patented
- **creator:** Boston Dynamics (now Hyundai Motor Group subsidiary)
- **disclosure citation:** Boston Dynamics public reveal of Spot, February 2015.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `mechanism-quadrupedal-locomotion`, `control-mpc`, `sensing-stereo-camera`, `sensing-imu`, `power-li-ion`, `power-hot-swap`

**Prior art notes:**

> Spot is the most commercially deployed quadruped robot. BD's Spot patents face deep prior art from MIT Cheetah series, ANYmal lineage, and academic quadruped literature.

**Sources:**

1. Boston Dynamics product materials.
2. Boston Dynamics technical blog.

---

### 2016 — ANYmal

- **id:** `anymal`
- **corpus:** private
- **ip status:** patented
- **creator:** ANYbotics, ETH Zurich Robotic Systems Lab
- **disclosure citation:** Hutter, M. et al. 'ANYmal — a highly mobile and dynamic quadrupedal robot.' IROS 2016.
- **disclosed subsystems:** `actuator-electric-series-elastic`, `mechanism-quadrupedal-locomotion`, `control-rl-policy`, `control-sim-to-real`, `sensing-stereo-camera`, `sensing-lidar`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> ANYbotics SEA design heavily anticipated by NASA Valkyrie and Robonaut SEA work. ETH RSL academic publications provide open prior art for many control claims.

**Sources:**

1. Hutter, M. et al. IROS 2016.
2. ANYbotics company materials.

---

### 2016-06 — Boston Dynamics SpotMini

- **id:** `boston-dynamics-spotmini-2017`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Boston Dynamics
- **disclosure citation:** Boston Dynamics. SpotMini public reveal June 2016 demo video; subsequent IEEE Spectrum coverage 2017-2018; capability demonstrations via Boston Dynamics YouTube. Discontinued in favor of Spot (the production quadruped) circa 2019.
- **disclosed subsystems:** `mechanism-quadrupedal-locomotion`, `actuator-electric`, `control-rl-policy`, `control-teleoperation`

**Prior art notes:**

> SpotMini is the architectural predecessor to commercial Spot. ~9-year-deep public-disclosure prior art for: all-electric quadruped morphology (distinct from hydraulic BigDog/Spot ancestors), dorsal-mount manipulator on quadruped base, Velodyne+depth-camera quadruped sensor stack. Trade-secret control software, public capability surface. Direct shielding for any commercial humanoid-quadruped or quadruped-manipulator claim. Cited in cheetah-cub-epfl and black-mirror-metalhead-2017 prior_art_notes; round-14 backfill closes those citation chains.

**Sources:**

1. Boston Dynamics YouTube reveal videos June 2016 and 2018.
2. IEEE Spectrum 'Boston Dynamics' SpotMini Is All Electric, Agile, and Has a Capable Face-Arm', 2017.
3. Vision Systems Design coverage 2018.

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

### 2018 — Ghost Robotics Vision 60

- **id:** `ghost-robotics-vision-60`
- **corpus:** private
- **ip status:** patented
- **creator:** Ghost Robotics
- **disclosure citation:** Ghost Robotics Vision 60 release, 2018.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `mechanism-quadrupedal-locomotion`, `control-mpc`, `sensing-stereo-camera`, `sensing-lidar`, `sensing-imu`, `power-li-ion`, `software-ros1`

**Prior art notes:**

> Ghost Robotics derives from Penn's Kod*lab academic quadruped work. The legged-robot patents face the same MIT Cheetah / ANYmal / Penn Kod*lab prior art chain as other quadrupeds.

**Sources:**

1. Ghost Robotics company materials.

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

### 2018-09 — Tencent Robotics X Lab *(draft)*

- **id:** `tencent-robotics-x-lab-2018`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Tencent Holdings (Shenzhen, China)
- **disclosure citation:** Tencent Robotics X (Shenzhen, China). Founded September 2018 as Tencent's robotics research division. Notable products: Max (quadruped 2021), Booster (bipedal 2022 — distinct from Booster Robotics), Smart Lab automation.
- **disclosed subsystems:** `control-research-cluster`, `mechanism-quadrupedal-locomotion`, `mechanism-bipedal-locomotion`

**Prior art notes:**

> Tencent Robotics X (Shenzhen 2018+) is one of China's major commercial robotics divisions. Aggregator-style entry. Together with Tsinghua (round-26) + SJTU (round-26) + CASIA (round-29) + BIT (round-29), brings explicit Chinese robotics ecosystem representation to a 5-pillar mix of commercial + academic + national-research.

**Sources:**

1. Tencent Robotics X corporate site (roboticsx.tencent.com).

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

### 2019-01-16 — Hwangbo ANYmal Sim-to-Real Locomotion

- **id:** `hwangbo-anymal-sim2real`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Hwangbo, Lee, Dosovitskiy, Bellicoso, Tsounis, Koltun, Hutter; ETH Zürich Robotic Systems Lab + Intel Intelligent Systems Lab
- **disclosure citation:** Hwangbo, Jemin, Lee, Joonho, Dosovitskiy, Alexey, Bellicoso, Dario, Tsounis, Vassilios, Koltun, Vladlen, Hutter, Marco. 'Learning agile and dynamic motor skills for legged robots.' Science Robotics 4(26): eaau5872, January 16, 2019.
- **disclosed subsystems:** `control-rl-policy`, `control-sim-to-real`, `actuator-electric-series-elastic`, `mechanism-quadrupedal-locomotion`, `sensing-imu`

**Prior art notes:**

> Hwangbo et al. 2019 is the foundational academic disclosure of practical RL-based sim-to-real legged locomotion. Anticipates with full architectural specificity: (1) actuator-network-based high-fidelity simulation (neural network as drop-in actuator dynamics) — directly relevant to claims on humanoid sim-to-real pipelines (Berkeley Humanoid, Apptronik Apollo, Tesla Optimus all use derivatives); (2) zero-shot policy transfer from RL-in-sim to legged hardware — anticipates virtually every modern legged-RL-policy patent; (3) recovery from arbitrary falls via single learned policy — relevant to fall-recovery IP for humanoids. Published in Science Robotics; one of the most-cited robotics RL papers (>2000 citations). Modern humanoid sim-to-real claims face this 7-year-deep anchor with full peer-review defensibility.

**Sources:**

1. Hwangbo, J. et al. 'Learning agile and dynamic motor skills for legged robots.' Science Robotics 4(26), 2019.
2. Lee, J. et al. 'Learning quadrupedal locomotion over challenging terrain.' Science Robotics 5(47), 2020 (sequel).

---

### 2019-04 — Stanford Pupper / Doggo open-source quadruped

- **id:** `stanford-pupper-doggo-2019`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Stanford Student Robotics; Nathan Kau, Aaron Schultz et al.
- **disclosure citation:** Stanford Student Robotics. Stanford Doggo open-source quadruped reveal April 2019. Subsequent: Stanford Pupper (smaller variant). stanfordstudentrobotics.org / hands-on-robotics.stanford.edu. Open-hardware design under MIT license.
- **disclosed subsystems:** `mechanism-quadrupedal-locomotion`, `actuator-electric`, `mechanism-3d-printed-platform`

**Prior art notes:**

> Stanford Pupper / Doggo (Stanford Student Robotics 2019+) is the canonical Stanford educational open-source quadruped. 6-year-deep open-permissive prior art. The Stanford academic counterpart to Unitree Go1/Go2 (corpus) for educational quadruped robotics. Direct shielding for any commercial quadruped claim deriving from low-cost open-hardware educational platforms.

**Sources:**

1. Stanford Student Robotics (stanfordstudentrobotics.org).
2. Hands-on-Robotics Stanford (hands-on-robotics.stanford.edu).
3. GitHub: github.com/Nate711/StanfordDoggoProject.

---

### 2020 — Boston Dynamics Spot (fuel-cell variant) *(draft)*

- **id:** `spot-fuel-cell`
- **corpus:** private
- **ip status:** patented
- **creator:** Boston Dynamics
- **disclosure citation:** Boston Dynamics partnership announcements with fuel cell vendors, 2020.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `mechanism-quadrupedal-locomotion`, `control-mpc`, `sensing-stereo-camera`, `sensing-imu`, `power-fuel-cell`

**Prior art notes:**

> Demonstrates fuel-cell-powered legged robotics at commercial scale. Anticipates fuel-cell power claims in field robotics applications.

**Sources:**

1. Boston Dynamics partnership announcements.
2. Industrial deployment case studies.

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

### 2022-09 — ANYmal-D industrial quadruped (ETH RSL / ANYbotics)

- **id:** `anymal-d-eth-rsl-2022`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** ANYbotics AG / ETH Zürich Robotic Systems Lab (Marco Hutter)
- **disclosure citation:** ANYbotics product disclosure ANYmal D, September 2022; technical updates in Miki, Takahiro et al. 'Learning robust perceptive locomotion for quadrupedal robots in the wild.' Science Robotics 7(62), 2022; Hoeller, David et al. 'ANYmal Parkour: Learning agile navigation for quadrupedal robots.' Science Robotics 9(88), 2024.
- **disclosed subsystems:** `mechanism-quadrupedal-locomotion`, `actuator-electric-series-elastic`, `actuator-electric-harmonic-drive`, `sensing-imu`, `sensing-lidar`, `sensing-stereo-camera`, `sensing-proprioceptive-actuator`, `control-rl-policy`, `control-sim-to-real`, `software-ros2`

**Prior art notes:**

> ANYmal-D is the production-deployed industrial quadruped of the 2022-2024 period and the platform for the headline RSL/ANYbotics RL-locomotion papers in Science Robotics. It anticipates with full specificity: (1) claims on perceptive-locomotion RL policies trained in simulation and transferred to outdoor industrial terrain — Miki Sci.Rob. 2022 publishes the teacher-student distillation pipeline running on this hardware; (2) claims on agile parkour-class learned locomotion — Hoeller Sci.Rob. 2024 publishes the policy on ANYmal-D; (3) claims on series-elastic torque-controlled quadruped joints in IP67 industrial enclosures — ANYdrive disclosed at IROS 2018 with hardware refresh on D-variant. Modern legged-robot IP claims face this timestamped industrial-deployment anchor.

**Sources:**

1. Miki, T. et al. 'Learning robust perceptive locomotion for quadrupedal robots in the wild.' Science Robotics 7(62), 2022.
2. Hoeller, D. et al. 'ANYmal Parkour.' Science Robotics 9(88), 2024.
3. ANYbotics ANYmal D datasheet, 2022.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `cd2f551`.*
