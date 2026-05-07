---
title: "mechanism-tendon-routing"
parent: "Invalidity Contentions"
nav_order: 27
layout: default
---

# Invalidity Contention Packet — `mechanism-tendon-routing`

**Generated:** 2026-05-07  
**Cross-cut tag:** `mechanism-tendon-routing`  
**Entries:** 12 (9 commons-grade, 3 draft)  
**Earliest disclosure:** 1495  
**Most recent disclosure:** 2024

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `mechanism-tendon-routing`.

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

### 1495 — Leonardo's Mechanical Knight

- **id:** `da-vinci-knight`
- **corpus:** fictional
- **ip status:** public-domain
- **creator:** Leonardo da Vinci
- **disclosure citation:** Leonardo da Vinci, Codex Atlanticus folios depicting cable-and-pulley humanoid automaton, c. 1495 (Milan, court of Ludovico Sforza). Reconstructed and analyzed in Rosheim, Mark E. Leonardo's Lost Robots. Springer, 2006.
- **disclosed subsystems:** `actuator-electric-tendon-driven`, `mechanism-anthropomorphic-hand`, `mechanism-bipedal-locomotion`, `mechanism-tendon-routing`

**Prior art notes:**

> Documented disclosure of cable-driven anthropomorphic humanoid mechanism with articulated hand, dating to c.1495 — 478 years before WABOT-1 (1973), 522 years before contemporary tendon-driven humanoid hand patents. Leonardo's drawings show explicit cable routing through joints, separation of upper-body and lower-body actuator banks, programmable behavior via cam-sequencing — all elements that recur in modern humanoid actuator IP. Modern claims on cable-driven anthropomorphic hands or tendon-routed humanoid actuators face an extraordinarily deep 102 anchor here. The Codex Atlanticus is publicly held (Biblioteca Ambrosiana, Milan) and has been continuously cited since the 19th century.

**Sources:**

1. Rosheim, Mark E. Leonardo's Lost Robots. Springer, 2006.
2. Codex Atlanticus, Biblioteca Ambrosiana, Milan (digital facsimile).

---

### 1982 — Salisbury Stanford/JPL Hand

- **id:** `salisbury-stanford-jpl-hand`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** J. Kenneth Salisbury, Stanford University and JPL
- **disclosure citation:** Salisbury, J. Kenneth. 'Kinematic and Force Analysis of Articulated Hands.' PhD Thesis, Stanford University, May 1982. Companion paper: Salisbury, J.K. and Craig, J.J. 'Articulated hands: Force control and kinematic issues.' International Journal of Robotics Research 1(1): 4-17, March 1982.
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `actuator-electric-tendon-driven`, `mechanism-tendon-routing`, `sensing-force-torque`

**Prior art notes:**

> Salisbury's 1982 thesis is the foundational academic disclosure of dexterous tendon-driven multi-finger hands with analytic grasp planning. Anticipates with mechanism-level specificity: (1) N+1 antagonistic tendon architecture for fingers — directly relevant to claims on tendon-driven humanoid hand actuators (Tesla Optimus hand, Figure hand, 1X hand); (2) the grasp matrix G and grip Jacobian formalism — anticipates virtually every modern grasp-planning patent; (3) force-closure analysis for grasp synthesis — relevant to grasp-search IP; (4) per-finger stiffness control — relevant to compliant-grasp claims. Salisbury later co-developed the PHANToM haptic device using the same kinematic framework. Thesis publicly available through Stanford Libraries; the IJRR companion paper has >2000 citations. 44-year-deep 102 anchor.

**Sources:**

1. Salisbury, J.K. PhD Thesis, Stanford University, 1982.
2. Salisbury, J.K. and Craig, J.J. 'Articulated hands.' IJRR 1(1): 4-17, 1982.
3. Mason, M.T. and Salisbury, J.K. Robot Hands and the Mechanics of Manipulation. MIT Press, 1985.

---

### 2002 — Shadow Dexterous Hand

- **id:** `shadow-dexterous-hand`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Shadow Robot Company (Richard Greenhill, Rich Walker, et al.)
- **disclosure citation:** Greenhill, Richard et al. (Shadow Robot Company). 'Shadow Dexterous Hand'. ICRA workshops 2002 onwards; mechanical disclosures in Greenhill, R., Walker, R. et al. 'The Shadow C5 Hand Prototype'. ICRA Workshop on Humanoid Manipulation, 2007.
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `actuator-pneumatic-muscle`, `actuator-electric-tendon-driven`, `mechanism-tendon-routing`, `sensing-tactile-fingertip`

**Prior art notes:**

> Shadow's hand is the longest-running academic-grade dexterous hand platform and is the standard reference for tendon-routed anthropomorphic manipulators. Anticipates and provides extensive prior art for: (1) 24-DOF anthropomorphic hand mechanism with separate-finger control — relevant to modern humanoid hand IP; (2) McKibben-style pneumatic muscle actuation in a hand — relevant to artificial-muscle hand claims; (3) tendon-tension control as a viable closed-loop mode for dexterity — relevant to tendon-controlled hand IP. Shadow has published extensively in IEEE proceedings since 2002, and the platform is licensed to academic labs worldwide. Modern Tesla, Figure, and 1X hand patents face Shadow's 22+ years of accumulated public disclosure.

**Sources:**

1. Shadow Robot Company. 'Shadow C5 Hand'. ICRA Workshop on Humanoid Manipulation, 2007.
2. Shadow Robot Company. Shadow Dexterous Hand technical specification (publicly distributed).

---

### 2003 — Shadow Dexterous Hand

- **id:** `shadow-hand`
- **corpus:** private
- **ip status:** patented
- **creator:** Shadow Robot Company
- **disclosure citation:** Shadow Robot Company. Shadow Dexterous Hand, commercial release approximately 2003.
- **disclosed subsystems:** `actuator-pneumatic-muscle`, `actuator-electric-tendon-driven`, `mechanism-anthropomorphic-hand`, `mechanism-tendon-routing`, `sensing-tactile-fingertip`

**Prior art notes:**

> Shadow Hand is among the deepest prior art references for anthropomorphic robotic hands. Most modern humanoid hand claims are anticipated by Shadow's 20+ years of disclosure.

**Sources:**

1. shadowrobot.com
2. Shadow Robot academic publications.

---

### 2008 — iCub

- **id:** `icub`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Italian Institute of Technology (IIT) and the RobotCub Consortium
- **disclosure citation:** Metta, G. et al. 'The iCub humanoid robot: an open platform for research in embodied cognition.' PerMIS 2008.
- **disclosed subsystems:** `actuator-electric-harmonic-drive`, `actuator-electric-tendon-driven`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `mechanism-tendon-routing`, `sensing-stereo-camera`, `sensing-force-torque`, `sensing-tactile-whole-body`, `software-yarp`

**Prior art notes:**

> Among the earliest fully open-source humanoid platforms with hardware design released. Anticipates: tendon-driven anthropomorphic hands, full-body artificial skin, open robotics middleware.

**Sources:**

1. Metta, G. et al. PerMIS 2008.
2. iCub.org documentation.

---

### 2008 — Willow Garage PR1

- **id:** `willow-pr1`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Willow Garage / Stanford (Ken Salisbury group)
- **disclosure citation:** Wyrobek, K.A. et al. 'Towards a Personal Robotics Development Platform: Rationale and Design of an Intrinsically Safe Personal Robot.' ICRA 2008.
- **disclosed subsystems:** `actuator-electric-tendon-driven`, `mechanism-tendon-routing`, `mechanism-anthropomorphic-hand`, `control-mpc`, `sensing-stereo-camera`, `sensing-force-torque`, `power-tethered`, `safety-hard-constraint`

**Prior art notes:**

> PR1 is significant prior art for safety-by-design humanoid robotics. Cable-driven intrinsically-safe architecture anticipates several modern compliant-actuator humanoid claims.

**Sources:**

1. Wyrobek, K.A. et al. ICRA 2008.
2. Willow Garage technical materials.

---

### 2010-02 — Robonaut 2

- **id:** `robonaut-2`
- **corpus:** academic
- **ip status:** patented
- **creator:** NASA Johnson Space Center, in partnership with General Motors
- **disclosure citation:** Diftler, M.A. et al. 'Robonaut 2 — The First Humanoid Robot in Space.' ICRA 2011.
- **disclosed subsystems:** `actuator-electric-tendon-driven`, `actuator-electric-series-elastic`, `mechanism-anthropomorphic-hand`, `mechanism-tendon-routing`, `sensing-stereo-camera`, `sensing-force-torque`, `sensing-tactile-fingertip`, `power-tethered`

**Prior art notes:**

> Robonaut 2's hand design, with 12 DoF per hand and tendon routing through the forearm, is foundational prior art for high-DoF tendon-driven humanoid hands. The NASA-GM patent portfolio has been extensively cited.

**Sources:**

1. Diftler, M.A. et al. ICRA 2011.
2. Bridgwater, L.B. et al. 'The Robonaut 2 Hand — Designed To Do Work With Tools.' ICRA 2012.

---

### 2012 — InMoov

- **id:** `inmoov`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** Gaël Langevin
- **disclosure citation:** Langevin, Gaël. InMoov project launch, 2012.
- **disclosed subsystems:** `actuator-electric-tendon-driven`, `mechanism-anthropomorphic-hand`, `mechanism-tendon-routing`, `mechanism-underactuated-grasping`

**Prior art notes:**

> InMoov has been replicated globally thousands of times since 2012; the design is among the most-built humanoid platforms in history. Anticipates: 3D-printed tendon-driven anthropomorphic hands, modular humanoid construction.

**Sources:**

1. inmoov.fr
2. Langevin, G. ongoing project documentation.

---

### 2014-11-03 — Pisa-IIT SoftHand

- **id:** `pisa-iit-softhand`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Catalano, Grioli, Farnioli, Serio, Piazza, Bicchi; Centro 'E. Piaggio', Università di Pisa, and Italian Institute of Technology
- **disclosure citation:** Catalano, M.G., Grioli, G., Farnioli, E., Serio, A., Piazza, C., Bicchi, A. 'Adaptive synergies for the design and control of the Pisa/IIT SoftHand'. International Journal of Robotics Research 33(5): 768-782, November 3, 2014.
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `actuator-electric-tendon-driven`, `mechanism-underactuated-grasping`, `mechanism-tendon-routing`

**Prior art notes:**

> The Pisa-IIT SoftHand is the canonical academic disclosure of synergistic underactuated anthropomorphic hands. Anticipates: (1) the use of human-derived postural synergies (specifically the 'first synergy' from PCA on human grasping kinematics) as the actuation pattern for an anthropomorphic robot hand — directly relevant to modern claims on synergy-driven hand IP; (2) reducing 19 DOFs to a single motor via tendon-coupling — relevant to underactuated humanoid hand patents. Bicchi's group has extensive prior art back to the 1990s on underactuated grasping; the SoftHand 2014 paper is the consolidated reference. Heavily cited; commercial extensions exist (qb robotics).

**Sources:**

1. Catalano, M.G. et al. 'Adaptive synergies for the design and control of the Pisa/IIT SoftHand'. IJRR 33(5), 2014.
2. Bicchi, A. and Asada, H. 'On the closure properties of robotic grasping'. IEEE T-RO 1995 (foundational underactuation work).

---

### 2022 — Sanctuary Phoenix Gen 6 *(draft)*

- **id:** `sanctuary-phoenix-gen6`
- **corpus:** private
- **ip status:** patented
- **creator:** Sanctuary AI
- **disclosure citation:** Sanctuary AI public reveals of Phoenix predecessors, 2020-2022.
- **disclosed subsystems:** `actuator-hydraulic`, `actuator-electric-direct-drive`, `mechanism-anthropomorphic-hand`, `mechanism-tendon-routing`, `control-teleoperation`, `sensing-stereo-camera`, `sensing-force-torque`

**Prior art notes:**

> Sanctuary's hybrid hydraulic-electric actuation faces extensive prior art from Boston Dynamics Atlas (hydraulic), Honda (electric), and academic hybrid actuation literature.

**Sources:**

1. Sanctuary AI public materials, 2020-2022.

---

### 2023-05 — Sanctuary AI Phoenix *(draft)*

- **id:** `sanctuary-phoenix`
- **corpus:** private
- **ip status:** patented
- **creator:** Sanctuary AI
- **disclosure citation:** Sanctuary AI public reveal, May 2023.
- **disclosed subsystems:** `actuator-electric-cycloidal`, `actuator-electric-direct-drive`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `mechanism-tendon-routing`, `control-teleoperation`, `control-rl-policy`, `sensing-stereo-camera`, `sensing-force-torque`, `power-li-ion`

**Prior art notes:**

> Sanctuary's high-DoF hand claims face Shadow Hand (2003) and iCub (2008) as deep prior art for tendon-driven anthropomorphic hands with high finger DoF.

**Sources:**

1. sanctuary.ai
2. Sanctuary AI press materials and demonstration videos.

---

### 2024 — 1X NEO *(draft)*

- **id:** `1x-neo`
- **corpus:** private
- **ip status:** patented
- **creator:** 1X Technologies (formerly Halodi Robotics)
- **disclosure citation:** 1X Technologies public reveal, 2024.
- **disclosed subsystems:** `actuator-electric-tendon-driven`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `mechanism-tendon-routing`, `control-rl-policy`, `control-teleoperation`, `sensing-stereo-camera`, `power-li-ion`

**Prior art notes:**

> Tendon-driven compliant actuation is heavily anticipated by iCub, by Shadow Robot Hand work, and by decades of academic compliant-actuation literature.

**Sources:**

1. 1X Technologies website.
2. Halodi Robotics historical materials.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `559a8b5`.*
