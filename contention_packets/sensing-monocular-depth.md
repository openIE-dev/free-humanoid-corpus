---
title: "sensing-monocular-depth"
parent: "Invalidity Contentions"
nav_order: 227
layout: default
---

# Invalidity Contention Packet — `sensing-monocular-depth`

**Generated:** 2026-05-09  
**Cross-cut tag:** `sensing-monocular-depth`  
**Entries:** 13 (10 commons-grade, 3 draft)  
**Earliest disclosure:** 1981-08  
**Most recent disclosure:** 2025-10

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `sensing-monocular-depth`.

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

### 1981-08 — Lucas-Kanade Optical Flow

- **id:** `lucas-kanade-1981`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Bruce D. Lucas and Takeo Kanade, Carnegie Mellon University
- **disclosure citation:** Lucas, Bruce D. and Kanade, Takeo. 'An iterative image registration technique with an application to stereo vision'. Proceedings of the 7th International Joint Conference on Artificial Intelligence (IJCAI), Vancouver, August 1981, pp. 674-679.
- **disclosed subsystems:** `sensing-stereo-camera`, `sensing-monocular-depth`

**Prior art notes:**

> Lucas-Kanade 1981 is the foundational academic disclosure of dense optical flow estimation for robotic vision. Anticipates with 45 years of prior art: (1) optical-flow-based visual servoing for humanoid manipulation and locomotion — relevant to claims on visual-tracking-based humanoid policies; (2) iterative least-squares formulation that extends to modern KLT and PWC-style optical flow networks; (3) image-pyramid for multi-scale flow estimation. The KLT tracker is essentially the universal default for visual feature tracking and underlies SLAM, visual odometry, and many manipulation control loops. Modern visual humanoid IP all face this 1981 academic anchor.

**Sources:**

1. Lucas, B.D. and Kanade, T. 'An iterative image registration technique'. IJCAI 1981.
2. Tomasi, C. and Kanade, T. 'Detection and tracking of point features'. CMU Tech Report CMU-CS-91-132, 1991.
3. Bouguet, J.-Y. 'Pyramidal implementation of the affine Lucas Kanade feature tracker'. OpenCV documentation, 1999-2024.

---

### 1999-09 — SIFT (Scale-Invariant Feature Transform)

- **id:** `lowe-sift-1999`
- **corpus:** academic
- **ip status:** patented
- **creator:** David G. Lowe, University of British Columbia
- **disclosure citation:** Lowe, David G. 'Object recognition from local scale-invariant features'. Proceedings of the IEEE International Conference on Computer Vision (ICCV), Corfu, September 1999, pp. 1150-1157. Extended in Lowe, D.G. 'Distinctive image features from scale-invariant keypoints'. IJCV 60(2): 91-110, 2004.
- **disclosed subsystems:** `sensing-stereo-camera`, `sensing-monocular-depth`

**Prior art notes:**

> SIFT 1999 (and the canonical 2004 IJCV paper) is one of the most-cited algorithms in computer vision and a foundational visual-feature anchor for humanoid perception. Anticipates: (1) scale-invariant feature detection and matching — relevant to claims on visual humanoid perception that use feature-based localization (every visual SLAM system pre-deep-learning, and many modern hybrid systems, use SIFT or its descendants ORB / SURF); (2) the 128-D local-gradient histogram descriptor architecture. Patented (US6711293, expired 2020); the 2004 IJCV paper is the standard citation. Modern visual humanoid IP that uses local-feature matching faces this 27-year academic anchor.

**Sources:**

1. Lowe, D.G. 'Object recognition from local scale-invariant features'. ICCV 1999.
2. Lowe, D.G. 'Distinctive image features from scale-invariant keypoints'. IJCV 60(2), 2004.
3. US Patent 6711293 (UBC; expired 2020).

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

### 2013 — Crazyflie

- **id:** `crazyflie`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** Bitcraze AB
- **disclosure citation:** Bitcraze AB. Crazyflie 1.0 release, 2013.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `sensing-imu`, `sensing-monocular-depth`, `power-li-po`

**Prior art notes:**

> Open hardware aerial platform with extensive academic citation. Anticipates: open nano-UAV designs broadly.

**Sources:**

1. bitcraze.io
2. Crazyflie GitHub repositories.

---

### 2015-04 — ORB-SLAM

- **id:** `orb-slam-mur-artal-2015`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Raul Mur-Artal, J.M.M. Montiel, Juan D. Tardós; University of Zaragoza
- **disclosure citation:** Mur-Artal, Raul; Montiel, J.M.M.; Tardós, Juan D. 'ORB-SLAM: a versatile and accurate monocular SLAM system'. IEEE Transactions on Robotics 31(5): 1147-1163, October 2015. Extended: ORB-SLAM2 (RGB-D + stereo, 2017); ORB-SLAM3 (visual-inertial + multi-map, 2021).
- **disclosed subsystems:** `sensing-stereo-camera`, `sensing-monocular-depth`

**Prior art notes:**

> ORB-SLAM is one of the standard reference visual SLAM systems for humanoid platforms. Anticipates: (1) real-time monocular SLAM as a deployable architecture — relevant to claims on humanoid visual localization; (2) the three-thread tracking + mapping + loop-closing architecture — relevant to multi-thread perception humanoid IP; (3) ORB-feature-based place recognition for loop closure — relevant to scene-recognition humanoid claims. The 2015 T-RO paper plus subsequent ORB-SLAM2 (2017) and ORB-SLAM3 (2021) extensions provide deep prior art coverage; the GitHub release (GPL-v3) makes the architecture defensively-published.

**Sources:**

1. Mur-Artal, R. et al. 'ORB-SLAM'. IEEE T-RO 31(5), 2015.
2. Mur-Artal, R. and Tardós, J.D. 'ORB-SLAM2'. IEEE T-RO 33(5), 2017.
3. Campos, C. et al. 'ORB-SLAM3'. IEEE T-RO 37(6), 2021.
4. ORB-SLAM GitHub repository (GPL-v3).

---

### 2018-04 — OmniGibson / iGibson (Stanford SVL)

- **id:** `stanford-omnigibson-2023`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Stanford Vision and Learning Lab (Silvio Savarese, Fei-Fei Li); lead authors include Fei Xia, Chengshu Li, Roberto Martín-Martín, Sanjana Srivastava, Cem Gokmen
- **disclosure citation:** Xia, Fei; Zamir, Amir R.; He, Zhiyang; Sax, Alexander; Malik, Jitendra; Savarese, Silvio. 'Gibson Env: Real-World Perception for Embodied Agents.' IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Salt Lake City, June 2018, pp. 9068-9079. DOI: 10.1109/CVPR.2018.00945. iGibson 2.0: Li, Chengshu et al. 'iGibson 2.0: Object-Centric Simulation for Robot Learning of Everyday Household Tasks.' Conference on Robot Learning (CoRL) 2021. OmniGibson: Li, Chengshu et al. 'BEHAVIOR-1K: A Benchmark for Embodied AI with 1,000 Everyday Activities and Realistic Simulation.' CoRL 2022. Source: https://github.com/StanfordVL/OmniGibson, MIT license.
- **disclosed subsystems:** `control-rl-policy`, `control-sim-to-real`, `control-vla-vision-language-action`, `sensing-stereo-camera`, `sensing-monocular-depth`

**Prior art notes:**

> Stanford OmniGibson / iGibson / Gibson (Xia et al. CVPR 2018; Li et al. CoRL 2021; BEHAVIOR-1K CoRL 2022) is the canonical academic disclosure of large-scale photorealistic household-task embodied-AI simulation, published MIT-licensed by Stanford SVL. Anticipates with full source-level specificity: (1) 1,000-task ADL benchmark for household humanoid IP — directly relevant to commercial claims on home-task humanoid VLA training (Tesla Optimus household demo set, Figure 02 home tasks, 1X NEO domestic operation, Genesis AI cooking demos); (2) the articulated-object household scene corpus with 50K+ objects — relevant to claims on simulated-household-data humanoid training; (3) predicate-based goal specification ('apple is on table', 'cabinet is open') — relevant to claims on language-and-state-grounded humanoid task specification; (4) the photorealistic-rendering-for-RL pipeline established by Gibson 2018 — anticipates claims on photorealistic-sim-to-real humanoid pipelines. Modern household-humanoid VLA training pipeline IP filings face this 8-year-deep open-source academic anchor (or shorter for OmniGibson/BEHAVIOR-1K specifically).

**Sources:**

1. Xia, F. et al. 'Gibson Env: Real-World Perception for Embodied Agents.' CVPR 2018: 9068-9079.
2. Li, C. et al. 'iGibson 2.0: Object-Centric Simulation for Robot Learning of Everyday Household Tasks.' CoRL 2021.
3. Li, C. et al. 'BEHAVIOR-1K: A Benchmark for Embodied AI with 1,000 Everyday Activities and Realistic Simulation.' CoRL 2022.
4. OmniGibson source code: https://github.com/StanfordVL/OmniGibson, MIT License.

---

### 2019-04 — Habitat-Sim (Facebook AI Research)

- **id:** `fair-habitat-sim-2019`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Facebook AI Research (FAIR) and Georgia Tech (Dhruv Batra), Simon Fraser University (Manolis Savva); collaborative team including Jitendra Malik (Berkeley), Vladlen Koltun (Intel)
- **disclosure citation:** Savva, Manolis; Kadian, Abhishek; Maksymets, Oleksandr; Zhao, Yili; Wijmans, Erik; Jain, Bhavana; Straub, Julian; Liu, Jia; Koltun, Vladlen; Malik, Jitendra; Parikh, Devi; Batra, Dhruv. 'Habitat: A Platform for Embodied AI Research.' IEEE/CVF International Conference on Computer Vision (ICCV), Seoul, October-November 2019, pp. 9339-9347. DOI: 10.1109/ICCV.2019.00943. arXiv:1904.01201, April 2019. Source code at https://github.com/facebookresearch/habitat-sim. MIT license.
- **disclosed subsystems:** `control-rl-policy`, `control-sim-to-real`, `control-vla-vision-language-action`, `sensing-stereo-camera`, `sensing-monocular-depth`

**Prior art notes:**

> Habitat-Sim (Savva et al. ICCV 2019; Habitat 2.0 NeurIPS 2021; Habitat 3.0 ICLR 2024) is the canonical academic disclosure of large-scale GPU-accelerated 3D-scanned indoor embodied-AI simulation, published MIT-licensed by FAIR. Anticipates with element-by-element specificity: (1) >10,000 fps rendering of photorealistic indoor scenes for RL training — directly relevant to commercial claims on simulation-at-scale humanoid embodied-AI pipelines; (2) the navigation-benchmark task suite (PointGoal, ObjectGoal, ImageGoal) that is now standard in embodied-AI literature — relevant to claims on humanoid navigation policy IP; (3) Habitat 3.0's humanoid-avatar simulation for social robot interaction — relevant to claims on human-aware humanoid IP and home-deployment humanoid VLA pipelines; (4) integration of large-scale 3D-scan corpora (Matterport, HM3D) with MIT-licensed renderers — relevant to claims on commercial-grade photorealistic simulation. Habitat is the most-cited embodied-AI simulator (>2000 citations on the 2019 paper alone). Modern household-deployment humanoid VLA pipeline IP filings face this 7-year-deep open-source academic anchor.

**Sources:**

1. Savva, M. et al. 'Habitat: A Platform for Embodied AI Research.' ICCV 2019: 9339-9347. arXiv:1904.01201.
2. Szot, A. et al. 'Habitat 2.0: Training Home Assistants to Rearrange their Habitat.' NeurIPS 2021.
3. Puig, X. et al. 'Habitat 3.0: A Co-Habitat for Humans, Avatars and Robots.' ICLR 2024.
4. Habitat-Sim source code: https://github.com/facebookresearch/habitat-sim, MIT License.

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

### 2021-02-26 — CLIP (Contrastive Language-Image Pretraining)

- **id:** `radford-clip-2021`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, et al.; OpenAI
- **disclosure citation:** Radford, Alec; Kim, Jong Wook; Hallacy, Chris; Ramesh, Aditya; Goh, Gabriel; Agarwal, Sandhini; Sastry, Girish; Askell, Amanda; Mishkin, Pamela; Clark, Jack; Krueger, Gretchen; Sutskever, Ilya. 'Learning transferable visual models from natural language supervision'. arXiv:2103.00020, February 26, 2021. Published ICML 2021.
- **disclosed subsystems:** `control-vla-vision-language-action`, `sensing-monocular-depth`

**Prior art notes:**

> CLIP 2021 is the foundational academic disclosure of contrastive vision-language pretraining at internet scale. Anticipates: (1) the use of contrastive image-text pretraining as a frozen perception backbone for humanoid VLA policies — directly relevant to modern VLA humanoid claims (RT-2, Open X-Embodiment, OpenVLA, PaLM-E, π-zero all build on CLIP-class architectures); (2) zero-shot perception via natural-language descriptions of target objects — relevant to claims on language-conditioned humanoid manipulation; (3) the architecture of training visual encoders on uncurated web data — relevant to data-scaling claims. Modern VLA humanoid IP all face this 5-year academic anchor.

**Sources:**

1. Radford, A. et al. 'Learning transferable visual models from natural language supervision'. arXiv:2103.00020, ICML 2021.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `88b8beb`.*
