---
title: "mechanism-tendon-routing"
parent: "Invalidity Contentions"
nav_order: 75
layout: default
---

# Invalidity Contention Packet — `mechanism-tendon-routing`

**Generated:** 2026-05-07  
**Cross-cut tag:** `mechanism-tendon-routing`  
**Entries:** 15 (12 commons-grade, 3 draft)  
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

### 2011-05 — DLR Hand-Arm System

- **id:** `dlr-hand-arm-system-2011`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Markus Grebenstein, Alin Albu-Schäffer, Antonio Bicchi (collaboration), Gerd Hirzinger; DLR Institute of Robotics and Mechatronics, Oberpfaffenhofen
- **disclosure citation:** Grebenstein, Markus; Albu-Schäffer, Alin; Bahls, Thomas; Chalon, Maxime; Eiberger, Oliver; Friedl, Werner; Gruber, Robin; Haddadin, Sami; Hagn, Ulrich; Haslinger, Robert; Höppner, Hannes; Jörg, Stefan; Nickl, Mathias; Nothhelfer, Alexander; Petit, Florian; Reill, Josef; Seitz, Norbert; Wimböck, Thomas; Wolf, Sebastian; Wüsthoff, Tilo; Hirzinger, Gerd. 'The DLR Hand Arm System.' IEEE International Conference on Robotics and Automation (ICRA), Shanghai, May 2011, pp. 3175-3182. DOI: 10.1109/ICRA.2011.5980371. Companion thesis: Grebenstein, M. 'Approaching Human Performance: The Functionality-Driven Awiwi Robot Hand.' PhD thesis, ETH Zurich, 2012; published Springer Tracts in Advanced Robotics 98, 2014. ISBN 978-3-319-03592-9.
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `mechanism-tendon-routing`, `mechanism-underactuated-grasping`, `actuator-electric-tendon-driven`, `sensing-tactile-fingertip`, `sensing-force-torque`, `sensing-proprioceptive-actuator`

**Prior art notes:**

> The DLR Hand-Arm System (Grebenstein et al. ICRA 2011, Grebenstein PhD/STAR 2014) is the canonical academic disclosure of variable-impedance antagonistically-tendon-driven anthropomorphic hand-arm hardware. Anticipates with element-by-element mechanism-level specificity: (1) mechanically programmable variable joint stiffness via antagonistic tendons with nonlinear elastic elements — directly relevant to commercial claims on variable-stiffness humanoid hand IP; (2) the 19-DoF, 38-tendon, 38-motor architecture with motors in the forearm — relevant to claims on tendon-driven hand-with-forearm-actuation humanoid IP (Tesla Optimus Gen-3, Figure-02, Apptronik Apollo, Sanctuary Phoenix all show variations of this topology); (3) impact-survival via mechanical compliance absorption — anticipates claims on collision-tolerant humanoid hand IP; (4) the biomimetic muscle-tendon co-contraction analogue — relevant to claims on biomimetic humanoid manipulation. Grebenstein's PhD thesis (200+ pages) provides the deepest single-source mechanism disclosure in dexterous robotic hand history. Modern variable-impedance anthropomorphic hand IP filings face this 15-year-deep academic anchor with mechanical-drawing-level specificity.

**Sources:**

1. Grebenstein, M. et al. 'The DLR Hand Arm System.' IEEE ICRA 2011: 3175-3182. DOI: 10.1109/ICRA.2011.5980371.
2. Grebenstein, M. 'Approaching Human Performance: The Functionality-Driven Awiwi Robot Hand.' Springer Tracts in Advanced Robotics 98, 2014. ISBN 978-3-319-03592-9.
3. Wolf, S. et al. 'The DLR FSJ: Energy based design of a variable stiffness joint.' IEEE ICRA 2011 (companion paper on the variable-stiffness joint mechanism).

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

### 2014-05 — Yale OpenHand / ReFlex Hand

- **id:** `yale-reflex-openhand-2014`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Lael Odhner, Aaron Dollar, Robert Howe; Yale GRAB Lab and Harvard BioRobotics; with RightHand Robotics, Inc. as the commercial spinout (ReFlex SF/TakkTile)
- **disclosure citation:** Odhner, Lael U.; Jentoft, Leif P.; Claffee, Mark R.; Corson, Nicholas; Tenzer, Yaroslav; Ma, Raymond R.; Buehler, Martin; Kohout, Robert; Howe, Robert D.; Dollar, Aaron M. 'A compliant, underactuated hand for robust manipulation.' International Journal of Robotics Research, Volume 33, Issue 5, April 2014, pp. 736-752. DOI: 10.1177/0278364913514466. Yale OpenHand Project release: Ma, R. R. and Dollar, A. M. 'Yale OpenHand Project: Optimizing Open-Source Hand Designs for Ease of Fabrication and Adoption.' IEEE Robotics & Automation Magazine, Volume 24, Issue 1, March 2017, pp. 32-40. DOI: 10.1109/MRA.2016.2639034. Open-hardware repository at https://www.eng.yale.edu/grablab/openhand/.
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `mechanism-tendon-routing`, `mechanism-underactuated-grasping`, `actuator-electric-tendon-driven`, `sensing-tactile-fingertip`

**Prior art notes:**

> Yale OpenHand / ReFlex SF (Odhner-Dollar et al. IJRR 2014; Yale OpenHand Project IEEE RAM 2017) is the canonical open-hardware academic disclosure of underactuated tendon-driven robust grasping hands. Anticipates with full open-hardware specificity: (1) the three-finger underactuated tendon-driven gripper with passive compliance — directly relevant to claims on simple-grasp humanoid end-effectors; (2) the open-hardware design release pattern (CAD files, BOMs, fabrication instructions) for robotic hands — relevant to claims on 3D-printable robotic hand IP (predates and anticipates many late-2010s and 2020s open-hardware hand patents); (3) the compliant-grasp-without-perception paradigm as an alternative to dexterous-perception-driven manipulation — relevant to claims on perception-light humanoid grasping; (4) integration of barometric tactile sensors (TakkTile) into a robot hand — relevant to claims on humanoid tactile fingertip IP. Yale GRAB Lab has continuous publication record on underactuated hands since the early 2000s; the 2014 IJRR consolidates the design canon. Modern open-hardware humanoid hand IP filings face this 12-year-deep open-source academic anchor.

**Sources:**

1. Odhner, L.U. et al. 'A compliant, underactuated hand for robust manipulation.' IJRR 33(5): 736-752, April 2014. DOI: 10.1177/0278364913514466.
2. Ma, R.R. and Dollar, A.M. 'Yale OpenHand Project: Optimizing Open-Source Hand Designs for Ease of Fabrication and Adoption.' IEEE RAM 24(1), March 2017. DOI: 10.1109/MRA.2016.2639034.
3. Yale OpenHand Project repository: https://www.eng.yale.edu/grablab/openhand/
4. Tenzer, Y.; Jentoft, L.P.; Howe, R.D. 'The Feel of MEMS Barometers: Inexpensive and Easily Customized Tactile Array Sensors.' IEEE RAM 21(3): 89-95, 2014.

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

### 2018-09 — Pisa-IIT SoftHand 2

- **id:** `pisa-iit-softhand-2`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Cosimo Della Santina, Cristina Piazza, Giorgio Grioli, Manuel G. Catalano, Antonio Bicchi; Centro 'E. Piaggio', Università di Pisa, and Italian Institute of Technology (IIT)
- **disclosure citation:** Della Santina, Cosimo; Piazza, Cristina; Grioli, Giorgio; Catalano, Manuel G.; Bicchi, Antonio. 'Toward Dexterous Manipulation With Augmented Adaptive Synergies: The Pisa/IIT SoftHand 2.' IEEE Transactions on Robotics, Volume 34, Issue 5, October 2018, pp. 1141-1156. DOI: 10.1109/TRO.2018.2830407. First public disclosure as a conference work in earlier 2017 venues; the consolidated T-RO paper is the canonical reference.
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `mechanism-tendon-routing`, `mechanism-underactuated-grasping`, `actuator-electric-tendon-driven`

**Prior art notes:**

> Pisa-IIT SoftHand 2 (Della Santina et al. T-RO 2018) is the canonical academic disclosure of multi-synergy augmented underactuated anthropomorphic hands, extending the 2014 SoftHand from one synergy to two. Anticipates with element-by-element specificity: (1) the augmented multi-synergy actuation pattern that enables 19-DoF hand operation with 2 motors and provides in-hand manipulation capability — directly relevant to claims on low-motor-count dexterous humanoid hand IP (Tesla Optimus claimed motor-counts in the 11-22 range, Figure-02 hand counts similar; the SoftHand 2 paradigm anticipates the underactuation-with-manipulation-capability angle of those claims); (2) the formal extension of synergy theory from grasping (one synergy) to grasping-plus-manipulation (two synergies) — relevant to claims on synergy-based humanoid manipulation IP; (3) compliant passive shape adaptation eliminating perception-driven grasp planning — relevant to claims on perception-light humanoid grasping IP. Heavily cited (>200); consolidates Bicchi-group underactuation lineage from the 1990s. Modern multi-synergy underactuated humanoid hand IP filings face this 8-year-deep academic anchor.

**Sources:**

1. Della Santina, C. et al. 'Toward Dexterous Manipulation With Augmented Adaptive Synergies: The Pisa/IIT SoftHand 2.' IEEE T-RO 34(5): 1141-1156, October 2018. DOI: 10.1109/TRO.2018.2830407.
2. Catalano, M.G. et al. 'Adaptive synergies for the design and control of the Pisa/IIT SoftHand'. IJRR 33(5), 2014 (predecessor entry pisa-iit-softhand).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `e4bb790`.*
