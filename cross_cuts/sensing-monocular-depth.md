---
title: sensing-monocular-depth
parent: Cross-cuts
layout: default
---

# Cross-cut: `sensing-monocular-depth`

**11 corpus entries disclose this subsystem.**

Earliest disclosure: 1981-08

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Lucas-Kanade Optical Flow (1981-08)

- **id**: `lucas-kanade-1981`
- **corpus**: academic
- **creator**: Bruce D. Lucas and Takeo Kanade, Carnegie Mellon University
- **disclosure**: Lucas, Bruce D. and Kanade, Takeo. 'An iterative image registration technique with an application to stereo vision'. Proceedings of the 7th International Joint Conference on Artificial Intelligence (IJCAI), Vancouver, August 1981, pp. 674-679.
- **ip status**: public-domain
- **prior art notes**: Lucas-Kanade 1981 is the foundational academic disclosure of dense optical flow estimation for robotic vision. Anticipates with 45 years of prior art: (1) optical-flow-based visual servoing for humanoid manipulation and locomotion — relevant to claims on visual-tracking-based humanoid policies; (2) iterative least-squares formulation that extends to modern KLT and PWC-style optical flow networks; (3) image-pyramid for multi-scale flow estimation. The KLT tracker is essentially the universal default for visual feature tracking and underlies SLAM, visual odometry, and many manipulation control loops. Modern visual humanoid IP all face this 1981 academic anchor.

## SIFT (Scale-Invariant Feature Transform) (1999-09)

- **id**: `lowe-sift-1999`
- **corpus**: academic
- **creator**: David G. Lowe, University of British Columbia
- **disclosure**: Lowe, David G. 'Object recognition from local scale-invariant features'. Proceedings of the IEEE International Conference on Computer Vision (ICCV), Corfu, September 1999, pp. 1150-1157. Extended in Lowe, D.G. 'Distinctive image features from scale-invariant keypoints'. IJCV 60(2): 91-110, 2004.
- **ip status**: patented
- **prior art notes**: SIFT 1999 (and the canonical 2004 IJCV paper) is one of the most-cited algorithms in computer vision and a foundational visual-feature anchor for humanoid perception. Anticipates: (1) scale-invariant feature detection and matching — relevant to claims on visual humanoid perception that use feature-based localization (every visual SLAM system pre-deep-learning, and many modern hybrid systems, use SIFT or its descendants ORB / SURF); (2) the 128-D local-gradient histogram descriptor architecture. Patented (US6711293, expired 2020); the 2004 IJCV paper is the standard citation. Modern visual humanoid IP that uses local-feature matching faces this 27-year academic anchor.

## GelSight (2009-09)

- **id**: `gelsight`
- **corpus**: academic
- **creator**: Micah Kimo Johnson, Edward Adelson; later Wenzhen Yuan, Siyuan Dong; MIT Media Lab and CSAIL
- **disclosure**: Johnson, M.K. and Adelson, E.H. 'Retrographic sensing for the measurement of surface texture and shape'. IEEE CVPR 2009, June 2009; consolidated in Yuan, W., Dong, S., Adelson, E.H. 'GelSight: high-resolution robot tactile sensors for estimating geometry and force'. Sensors 17(12): 2762, 2017.
- **ip status**: open-permissive
- **prior art notes**: GelSight is the foundational academic disclosure of vision-based tactile sensing. Anticipates: (1) vision-based fingertip tactile sensing using photometric stereo — directly relevant to all modern vision-tactile humanoid claims (DIGIT, MetaTouch, etc.); (2) sub-millimeter 3D-surface-from-image as the canonical sensor output — relevant to high-resolution-tactile claims; (3) gel-elastomer with oblique multi-color illumination as the sensor architecture — relevant to vision-tactile sensor claims. The 2009 CVPR paper and 2017 Sensors paper are heavily cited; the design has been replicated in ~50 academic publications. Modern vision-tactile humanoid IP faces this as 102 prior art.

## Crazyflie (2013)

- **id**: `crazyflie`
- **corpus**: open
- **creator**: Bitcraze AB
- **disclosure**: Bitcraze AB. Crazyflie 1.0 release, 2013.
- **ip status**: open-permissive
- **prior art notes**: Open hardware aerial platform with extensive academic citation. Anticipates: open nano-UAV designs broadly.

## ORB-SLAM (2015-04)

- **id**: `orb-slam-mur-artal-2015`
- **corpus**: academic
- **creator**: Raul Mur-Artal, J.M.M. Montiel, Juan D. Tardós; University of Zaragoza
- **disclosure**: Mur-Artal, Raul; Montiel, J.M.M.; Tardós, Juan D. 'ORB-SLAM: a versatile and accurate monocular SLAM system'. IEEE Transactions on Robotics 31(5): 1147-1163, October 2015. Extended: ORB-SLAM2 (RGB-D + stereo, 2017); ORB-SLAM3 (visual-inertial + multi-map, 2021).
- **ip status**: open-permissive
- **prior art notes**: ORB-SLAM is one of the standard reference visual SLAM systems for humanoid platforms. Anticipates: (1) real-time monocular SLAM as a deployable architecture — relevant to claims on humanoid visual localization; (2) the three-thread tracking + mapping + loop-closing architecture — relevant to multi-thread perception humanoid IP; (3) ORB-feature-based place recognition for loop closure — relevant to scene-recognition humanoid claims. The 2015 T-RO paper plus subsequent ORB-SLAM2 (2017) and ORB-SLAM3 (2021) extensions provide deep prior art coverage; the GitHub release (GPL-v3) makes the architecture defensively-published.

## DIGIT (2020-12)

- **id**: `digit-meta`
- **corpus**: academic
- **creator**: Lambeta, Chou, Tian, Yang, Maloon, Most, Stroud, Santos, Byagowi, Kammerer, Jayaraman, Calandra; Facebook AI Research (now Meta AI)
- **disclosure**: Lambeta, M., Chou, P.-W., Tian, S., Yang, B., Maloon, B., Most, V.R., Stroud, D., Santos, R., Byagowi, A., Kammerer, G., Jayaraman, D., Calandra, R. 'DIGIT: a novel design for a low-cost compact high-resolution tactile sensor with application to in-hand manipulation'. IEEE Robotics and Automation Letters 5(3): 3838-3845, 2020.
- **ip status**: open-permissive
- **prior art notes**: DIGIT extends GelSight to a low-cost open-source form factor. Anticipates: (1) low-cost open-source vision-tactile fingertip — directly relevant to claims on commercial humanoid hand patents that incorporate vision-tactile sensing; (2) form-factor integration of vision-tactile sensors into commodity robot hands — relevant to integrated humanoid hand IP. DIGIT's open-source release (CAD, firmware, software stack on GitHub) creates substantial prior art coverage of integration patterns. Heavily cited in subsequent dexterous-manipulation work.

## CLIP (Contrastive Language-Image Pretraining) (2021-02-26)

- **id**: `radford-clip-2021`
- **corpus**: academic
- **creator**: Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, et al.; OpenAI
- **disclosure**: Radford, Alec; Kim, Jong Wook; Hallacy, Chris; Ramesh, Aditya; Goh, Gabriel; Agarwal, Sandhini; Sastry, Girish; Askell, Amanda; Mishkin, Pamela; Clark, Jack; Krueger, Gretchen; Sutskever, Ilya. 'Learning transferable visual models from natural language supervision'. arXiv:2103.00020, February 26, 2021. Published ICML 2021.
- **ip status**: open-permissive
- **prior art notes**: CLIP 2021 is the foundational academic disclosure of contrastive vision-language pretraining at internet scale. Anticipates: (1) the use of contrastive image-text pretraining as a frozen perception backbone for humanoid VLA policies — directly relevant to modern VLA humanoid claims (RT-2, Open X-Embodiment, OpenVLA, PaLM-E, π-zero all build on CLIP-class architectures); (2) zero-shot perception via natural-language descriptions of target objects — relevant to claims on language-conditioned humanoid manipulation; (3) the architecture of training visual encoders on uncurated web data — relevant to data-scaling claims. Modern VLA humanoid IP all face this 5-year academic anchor.

## Unitree Go1 (2021-06)

- **id**: `unitree-go1`
- **corpus**: private
- **creator**: Unitree Robotics
- **disclosure**: Unitree Robotics Go1 reveal, June 2021.
- **ip status**: patented
- **prior art notes**: Unitree Go1 actuator design is heavily anticipated by MIT Cheetah QDD prior art (Wensing 2017, Katz 2019). Pricing-driven commodification rather than novel IP.

## Unitree G1 (2024-05)

- **id**: `unitree-g1`
- **corpus**: private
- **creator**: Unitree Robotics
- **disclosure**: Unitree Robotics G1 reveal, May 2024.
- **ip status**: patented
- **prior art notes**: G1's actuator IP largely anticipated by MIT Mini Cheetah QDD work and Honda harmonic drive prior art. The aggressive pricing represents the commodity-humanoid trajectory more than novel IP.

## EngineAI PM01 (2024-12)

- **id**: `engineai-pm01`
- **corpus**: private
- **creator**: EngineAI
- **disclosure**: EngineAI public reveal of PM01, December 2024.
- **ip status**: patented
- **prior art notes**: EngineAI QDD actuation anticipated by MIT Cheetah lineage.

## Unitree H2 (2025-10)

- **id**: `unitree-h2`
- **corpus**: private
- **creator**: Unitree Robotics
- **disclosure**: Unitree Robotics H2 reveal, October 2025.
- **ip status**: patented
- **prior art notes**: H2 builds on H1 architecture; same prior art chain back through Mini Cheetah.
