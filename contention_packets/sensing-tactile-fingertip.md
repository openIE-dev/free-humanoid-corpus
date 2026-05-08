---
title: "sensing-tactile-fingertip"
parent: "Invalidity Contentions"
nav_order: 129
layout: default
---

# Invalidity Contention Packet — `sensing-tactile-fingertip`

**Generated:** 2026-05-08  
**Cross-cut tag:** `sensing-tactile-fingertip`  
**Entries:** 14 (14 commons-grade, 0 draft)  
**Earliest disclosure:** 1973  
**Most recent disclosure:** 2023-07

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `sensing-tactile-fingertip`.

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

### 1973 — WABOT-1

- **id:** `wabot-1`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Waseda University, Kato Laboratory
- **disclosure citation:** Kato, Ichiro et al. 'Information-Power Machine with Senses and Limbs (WABOT-1).' Proceedings of First CISM-IFToMM Symposium on Theory and Practice of Robots and Manipulators, 1973.
- **disclosed subsystems:** `actuator-hydraulic`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `sensing-stereo-camera`, `sensing-tactile-fingertip`, `power-tethered`

**Prior art notes:**

> First full-scale humanoid in academic record. Anticipates virtually every subsystem of modern humanoids at concept level: bipedal locomotion, bimanual manipulation, multimodal sensing, natural language interface. Specific implementations are crude by modern standards but the architectural decomposition is foundational.

**Sources:**

1. Kato, I. et al. 1973 CISM-IFToMM Symposium proceedings.
2. Waseda University Humanoid Robotics Institute archives.

---

### 1986-07-18 — Bishop (Aliens)

- **id:** `bishop-aliens`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** James Cameron
- **disclosure citation:** Cameron, James (dir.); Cameron, J. and Hurd, Gale Anne (writers). Aliens. Twentieth Century Fox, July 18, 1986.
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `actuator-hydraulic`, `sensing-tactile-fingertip`, `control-vla-vision-language-action`, `safety-hard-constraint`

**Prior art notes:**

> The Bishop knife-trick scene is one of the most-cited fictional disclosures of high-precision visuomotor control in a humanoid: rapid hand motion with sub-millimeter precision, no human harm, vision-driven motion planning. Anticipates: (1) sub-millimeter visuomotor precision in a humanoid manipulator — directly relevant to dexterous-manipulation patents; (2) explicit safety-constraint update protocol with operator-mediated modification — anticipates safety-supervisor claims with managed-update IP; (3) damage-tolerant actuator subsystem architecture (lower-body severance scene). Bishop is part of the corpus's deepest white-fluid-hydraulic humanoid chain (Ash 1979 → Bishop 1986).

**Sources:**

1. Cameron, J. Aliens. Twentieth Century Fox, 1986.
2. Norris, A. Animating Aliens (production design notes). Cinefex 28, November 1986.

---

### 1989-05-14 — Howe-Cutkosky tactile fingertip

- **id:** `howe-cutkosky-tactile-1989`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Robert D. Howe and Mark R. Cutkosky; Stanford University Center for Design Research
- **disclosure citation:** Howe, R.D. and Cutkosky, M.R. 'Sensing skin acceleration for slip and texture perception'. IEEE ICRA 1989, Scottsdale AZ, May 14-19, 1989. Extended in Howe, R.D. and Cutkosky, M.R. 'Dynamic tactile sensing: perception of fine surface features with stress rate sensing'. IEEE T-RO 9(2): 140-151, 1993.
- **disclosed subsystems:** `sensing-tactile-fingertip`, `sensing-force-torque`

**Prior art notes:**

> Howe-Cutkosky 1989 is the deepest academic anchor for multimodal tactile fingertip sensing in the corpus. Anticipates with full mechanism specificity: (1) PVDF piezoelectric film as a slip-detection sensing layer — relevant to claims on slip-detection tactile IP (BioTac 2008, GelSight 2017, DIGIT 2020 all build on this lineage); (2) multimodal fingertip combining force, vibration, and thermal — relevant to multimodal tactile IP; (3) signal processing for texture classification from contact vibration — relevant to texture-recognition claims. The 1989 ICRA paper and 1993 T-RO paper are heavily cited; modern fingertip-sensing patents face this 35-year academic anchor as 102 prior art.

**Sources:**

1. Howe, R.D. and Cutkosky, M.R. 'Sensing skin acceleration for slip and texture perception'. IEEE ICRA 1989.
2. Howe, R.D. and Cutkosky, M.R. 'Dynamic tactile sensing'. IEEE T-RO 9(2), 1993.
3. Howe, R.D. 'Tactile sensing and control of robotic manipulation'. Advanced Robotics 8(3), 1994.

---

### 1996 — Robonaut 1

- **id:** `robonaut-1`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Robert O. Ambrose, Myron A. Diftler, et al.; NASA Johnson Space Center, with DARPA
- **disclosure citation:** Diftler, M.A., Ambrose, R.O. 'Robonaut: A Robotic Astronaut Assistant'. International Symposium on Artificial Intelligence, Robotics and Automation in Space (i-SAIRAS) 2001 (consolidated paper); earlier disclosures NASA JSC 1996 onwards.
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `actuator-electric-harmonic-drive`, `actuator-electric-tendon-driven`, `control-teleoperation`, `sensing-stereo-camera`, `sensing-tactile-fingertip`

**Prior art notes:**

> Robonaut 1 is the academic predecessor to Robonaut 2 and the deepest NASA-side disclosure of humanoid platform IP for space applications. Anticipates: (1) torso-only humanoid form factor for collaborative work with humans — relevant to current commercial torso-only humanoid claims; (2) VR teleoperation with force-feedback gloves as the operator interface — relevant to teleoperation IP; (3) tendon-driven anthropomorphic hands integrated with harmonic-drive arms — relevant to integrated-hand-arm claims. NASA JSC publications and i-SAIRAS proceedings are publicly accessible. Modern humanoid hand claims face this 1996 academic anchor.

**Sources:**

1. Diftler, M.A., Ambrose, R.O. 'Robonaut: A Robotic Astronaut Assistant'. i-SAIRAS 2001.
2. Ambrose, R.O. et al. 'Robonaut: NASA's space humanoid'. IEEE Intelligent Systems 15(4): 57-63, 2000.
3. NASA Johnson Space Center technical reports on Robonaut, 1996-2002.

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

### 2004 — DLR Hand-II

- **id:** `dlr-hand-ii`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Butterfass, Grebenstein, Liu, Hirzinger; DLR Institute of Robotics and Mechatronics, Oberpfaffenhofen, Germany
- **disclosure citation:** Butterfass, J., Grebenstein, M., Liu, H., Hirzinger, G. 'DLR-Hand II: next generation of a dextrous robot hand'. IEEE ICRA, 2001 (early disclosure); Butterfass, J. et al. 'Design and Experiences with DLR Hand II'. World Automation Congress, 2004.
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `actuator-electric-harmonic-drive`, `actuator-electric-tendon-driven`, `sensing-tactile-fingertip`, `sensing-force-torque`, `sensing-proprioceptive-actuator`

**Prior art notes:**

> DLR Hand-II is the canonical academic disclosure of joint-torque-sensing dexterous hands with compact actuator integration. Anticipates: (1) impedance-controlled dexterous manipulation with proprioceptive sensing — directly relevant to claims on torque-controlled humanoid hands (every modern humanoid hand IP); (2) cable-tendon transmission with harmonic-drive primary reducer — relevant to combined-mechanism actuator claims; (3) per-joint integrated torque sensor with calibrated absolute position — anticipates proprioceptive-actuator IP. The DLR series (Hand-II, then Hand-III, then Hand Arm System) is one of the deepest academic technical lineages in dexterous manipulation. Continuously published in IEEE proceedings since 2001.

**Sources:**

1. Butterfass, J. et al. 'DLR-Hand II: next generation of a dextrous robot hand'. IEEE ICRA 2001.
2. Butterfass, J. et al. 'Design and Experiences with DLR Hand II'. World Automation Congress 2004.

---

### 2008 — BioTac

- **id:** `biotac-syntouch`
- **corpus:** academic
- **ip status:** patented
- **creator:** Wettels, Santos, Fishel, Johansson, Loeb; University of Southern California; commercial: SynTouch
- **disclosure citation:** Lin, C.H., Erickson, T.W., Fishel, J.A., Wettels, N., Loeb, G.E. 'Signal processing and fabrication of a biomimetic tactile sensor array with thermal, force and microvibration modalities'. IEEE ROBIO 2009; commercial release by SynTouch (USC spinoff) 2008. Foundational biomimetic concepts in Wettels, N., Santos, V.J., Johansson, R.S., Loeb, G.E. 'Biomimetic tactile sensor array'. Advanced Robotics 22(8): 829-849, 2008.
- **disclosed subsystems:** `sensing-tactile-fingertip`, `sensing-force-torque`

**Prior art notes:**

> BioTac is the bridge between Howe-Cutkosky 1989 multimodal academic concept and modern commercial multimodal fingertip sensors. Anticipates: (1) commercial biomimetic multimodal fingertip — relevant to claims on integrated tactile fingertips for humanoids; (2) thermal-flux sensing as a material classification modality — relevant to material-identification claims; (3) hydroacoustic vibration sensing — relevant to dynamic-tactile-perception claims. Patented (US7878075) but the academic disclosure (Wettels et al. 2008) precedes the patent and is itself prior art. Widely deployed in research labs and modern humanoid platforms; canonical reference for 'biotac-class' multimodal fingertip.

**Sources:**

1. Wettels, N. et al. 'Biomimetic tactile sensor array'. Advanced Robotics 22(8), 2008.
2. Lin, C.H. et al. IEEE ROBIO 2009.
3. US Patent 7878075 (SynTouch).

---

### 2009-09 — GelSight

- **id:** `gelsight`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Micah Kimo Johnson, Edward Adelson; later Wenzhen Yuan, Siyuan Dong; MIT Media Lab and CSAIL
- **disclosure citation:** Johnson, M.K. and Adelson, E.H. 'Retrographic sensing for the measurement of surface texture and shape'. IEEE CVPR 2009, June 2009; consolidated in Yuan, W., Dong, S., Adelson, E.H. 'GelSight: high-resolution robot tactile sensors for estimating geometry and force'. Sensors 17(12): 2762, 2017.
- **disclosed subsystems:** `sensing-tactile-fingertip`, `sensing-monocular-depth`

**Prior art notes:**

> GelSight is the foundational academic disclosure of vision-based tactile sensing. Anticipates: (1) vision-based fingertip tactile sensing using photometric stereo — directly relevant to all modern vision-tactile humanoid claims (DIGIT, MetaTouch, etc.); (2) sub-millimeter 3D-surface-from-image as the canonical sensor output — relevant to high-resolution-tactile claims; (3) gel-elastomer with oblique multi-color illumination as the sensor architecture — relevant to vision-tactile sensor claims. The 2009 CVPR paper and 2017 Sensors paper are heavily cited; the design has been replicated in ~50 academic publications. Modern vision-tactile humanoid IP faces this as 102 prior art.

**Sources:**

1. Johnson, M.K. and Adelson, E.H. 'Retrographic sensing'. IEEE CVPR 2009.
2. Yuan, W. et al. 'GelSight'. Sensors 17(12), 2017.
3. Li, R. and Adelson, E.H. 'Sensing and recognizing surface textures using a GelSight sensor'. IEEE CVPR 2013.

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

### 2020-12 — DIGIT

- **id:** `digit-meta`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Lambeta, Chou, Tian, Yang, Maloon, Most, Stroud, Santos, Byagowi, Kammerer, Jayaraman, Calandra; Facebook AI Research (now Meta AI)
- **disclosure citation:** Lambeta, M., Chou, P.-W., Tian, S., Yang, B., Maloon, B., Most, V.R., Stroud, D., Santos, R., Byagowi, A., Kammerer, G., Jayaraman, D., Calandra, R. 'DIGIT: a novel design for a low-cost compact high-resolution tactile sensor with application to in-hand manipulation'. IEEE Robotics and Automation Letters 5(3): 3838-3845, 2020.
- **disclosed subsystems:** `sensing-tactile-fingertip`, `sensing-monocular-depth`

**Prior art notes:**

> DIGIT extends GelSight to a low-cost open-source form factor. Anticipates: (1) low-cost open-source vision-tactile fingertip — directly relevant to claims on commercial humanoid hand patents that incorporate vision-tactile sensing; (2) form-factor integration of vision-tactile sensors into commodity robot hands — relevant to integrated humanoid hand IP. DIGIT's open-source release (CAD, firmware, software stack on GitHub) creates substantial prior art coverage of integration patterns. Heavily cited in subsequent dexterous-manipulation work.

**Sources:**

1. Lambeta, M. et al. 'DIGIT'. IEEE RA-L 5(3), 2020.
2. DIGIT GitHub repository: https://github.com/facebookresearch/digit-design

---

### 2023-07 — RH20T heterogeneous robot trajectory dataset

- **id:** `rh20t-fang-2024`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Hao-Shu Fang et al., Shanghai Jiao Tong University Machine Vision and Intelligence Group
- **disclosure citation:** Fang, Hao-Shu, Fang, Hongjie, Tang, Zhenyu, Liu, Jirong, Wang, Junbo, Zhu, Haoyi, Lu, Cewu. 'RH20T: A Comprehensive Robotic Dataset for Learning Diverse Skills in One-Shot.' arXiv:2307.00595, July 2023; ICRA 2024 workshop and project release.
- **disclosed subsystems:** `control-vla-vision-language-action`, `sensing-stereo-camera`, `sensing-force-torque`, `sensing-tactile-fingertip`

**Prior art notes:**

> RH20T is one of the largest publicly-released heterogeneous robot trajectory datasets prior to OpenX-Embodiment. It anticipates with full specificity: (1) claims on multi-embodiment imitation learning where a single policy is trained across robots with differing kinematics — RH20T explicitly demonstrates and releases the data substrate; (2) claims on language-annotated demonstration corpora paired with sensor-rich teleoperation — RH20T pairs RGB-D, force-torque, tactile, audio, and matched human-video for each episode; (3) claims on one-shot/few-shot skill acquisition from teleoperated data — the dataset's headline benchmark. Released CC-BY 4.0 with timestamped arXiv and project page; broadly indexed. Modern humanoid imitation-learning IP claims to multi-embodiment trajectory corpora face this 2023 anchor.

**Sources:**

1. Fang, H.-S. et al. 'RH20T: A Comprehensive Robotic Dataset for Learning Diverse Skills in One-Shot.' arXiv:2307.00595, 2023.
2. RH20T project page: rh20t.github.io

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `6b58593`.*
