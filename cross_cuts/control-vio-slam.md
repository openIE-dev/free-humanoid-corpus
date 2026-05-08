---
title: control-vio-slam
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-vio-slam`

**16 corpus entries disclose this subsystem.**

Earliest disclosure: 2010-07

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## CSIRO Data61 Robotics and Autonomous Systems (2010-07)

- **id**: `csiro-data61-australia-robotics`
- **corpus**: academic
- **creator**: CSIRO Data61 (Commonwealth Scientific and Industrial Research Organisation, Australia)
- **disclosure**: CSIRO Data61 (Commonwealth Scientific and Industrial Research Organisation; Brisbane + Sydney, Australia). Robotics and Autonomous Systems group originally part of CSIRO ICT Centre, merged into Data61 in 2014. Notable projects: **Wildcat** legged robot for DARPA Subterranean Challenge (won 2nd place 2021), **Bobcat** agricultural robot, **Tilt-rotor UAV** development. Continuous robotics research output 2010+.
- **ip status**: public-domain
- **prior art notes**: CSIRO Data61 is Australia's dominant robotics research institution. 15-year-deep public-domain academic prior art spanning legged robots (DARPA SubT 2021 2nd place), agricultural automation (SwagBot, Bobcat), aerial systems. **First entry in the corpus for Australia** — closes a major regional gap. Aggregator-style entry covering CSIRO RAS broadly; specific papers should be added in future rounds.

## Savioke Relay (hotel delivery) (2014-08)

- **id**: `savioke-relay-2014`
- **corpus**: private
- **creator**: Savioke (San Jose, CA); Steve Cousins (former Willow Garage CEO)
- **disclosure**: Savioke, Inc. (San Jose, CA). Relay hotel delivery robot reveal August 2014 at Aloft Cupertino hotel. Founded by Steve Cousins (former Willow Garage CEO). Acquired by Relay Robotics 2021 (rebranding); then Aethon 2023; ST Engineering 2024.
- **ip status**: trade-secret
- **prior art notes**: Savioke Relay (Savioke San Jose 2014+) is the canonical first hotel-delivery service robot. 11-year-deep public-disclosure prior art. **The architectural predecessor of subsequent hotel + hospital + restaurant service-robot category**. Direct shielding for any commercial humanoid claim deriving from hotel-service applications. Together with Diligent Moxi (round-40) + Bear Robotics Servi (round-40), establishes the service-robot prior-art chain (hotel + hospital + restaurant).

## Bear Robotics Servi (restaurant service) (2017-08)

- **id**: `bear-robotics-servi-2017`
- **corpus**: private
- **creator**: Bear Robotics (Redwood City, CA); John Ha + colleagues
- **disclosure**: Bear Robotics, Inc. (Redwood City, CA). Servi restaurant service robot reveal 2017. Founded 2017 by John Ha (former Intel + Google) + colleagues. bearrobotics.ai. SoftBank Robotics investment partnership 2021.
- **ip status**: trade-secret
- **prior art notes**: Bear Robotics Servi (Bear Robotics Redwood City 2017+) is the canonical restaurant food-delivery service robot. 8-year-deep public-disclosure prior art with 1000+ commercial deployments. Direct shielding for any commercial humanoid claim deriving from restaurant-service applications.

## DynaSLAM (2018-06)

- **id**: `dynaslam-bescos-2018`
- **corpus**: academic
- **creator**: University of Zaragoza I3A; Bescos, Fácil, Civera, Neira
- **disclosure**: Bescos, B., Fácil, J. M., Civera, J., Neira, J. 'DynaSLAM: Tracking, Mapping and Inpainting in Dynamic Scenes'. IEEE Robotics and Automation Letters 3(4) 2018; IROS 2018. arXiv:1806.05620. Universidad de Zaragoza I3A. GPLv3 source: github.com/BertaBescos/DynaSLAM.
- **ip status**: open-copyleft
- **prior art notes**: DynaSLAM is the canonical foundational dynamic-scene visual SLAM system (Bescos et al. RA-L + IROS 2018). 7-year-deep open-copyleft prior art. Anchor of the dynamic-SLAM lineage that the entire RADIO-ViPE Table II benchmarks against (DLD-SLAM, V3D-SLAM, DGS-SLAM, RoDyn-SLAM, DynaMON are all DynaSLAM descendants). Direct shielding for any commercial humanoid claim on 'SLAM that works in dynamic environments with moving people'.

## ORB-SLAM3 (2021-04)

- **id**: `orb-slam3-2021`
- **corpus**: academic
- **creator**: University of Zaragoza I3A; Carlos Campos, Juan Tardós et al.
- **disclosure**: Campos, C., Elvira, R., Rodríguez, J. J. G., Montiel, J. M. M., Tardós, J. D. 'ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial, and Multimap SLAM'. IEEE Transactions on Robotics 37(6) December 2021, pp. 1874-1890. arXiv:2007.11898. GPLv3 source: github.com/UZ-SLAMLab/ORB_SLAM3. University of Zaragoza.
- **ip status**: open-copyleft
- **prior art notes**: ORB-SLAM3 is the canonical academic visual-inertial SLAM library and 5-year-deep open-source baseline. Heavily-cited (>3000 citations). Anticipates: (1) monocular/stereo/RGB-D + IMU fusion in a unified factor-graph framework, (2) multi-map operation across sessions for long-term autonomy, (3) bag-of-words place recognition for loop closure. Establishes the geometric-only SLAM baseline that semantic/open-vocab SLAM systems (including RADIO-ViPE, round-10 entry) extend. Any humanoid platform claim on visual-inertial SLAM faces this lineage.

## CSIRO Wildcat (DARPA Subterranean Challenge) (2021-09)

- **id**: `csiro-hudson-wildcat-darpa-subt-2021`
- **corpus**: academic
- **creator**: CSIRO Data61 + Emesent + Georgia Tech; Hudson, Talbot, et al.
- **disclosure**: Hudson, N., Talbot, F., Cox, M., Williams, J., Hines, T., Pitt, A., Wood, B., Frousheger, D., Lo Surdo, K., Molnar, T., Steindl, R., et al. 'Heterogeneous Ground and Air Platforms, Homogeneous Sensing: Team CSIRO Data61's Approach to the DARPA Subterranean Challenge'. Field Robotics 2 2022 / Journal of Field Robotics. CSIRO Data61 + Emesent + Georgia Tech. **2nd place DARPA Subterranean Challenge Finals 2021**.
- **ip status**: open-permissive
- **prior art notes**: CSIRO Data61 Wildcat (Hudson et al. Field Robotics 2022) is the specific paper-level anchor for the round-23 CSIRO Data61 aggregator. **DARPA SubT Finals 2nd place** establishes Australian academic robotics at internationally-recognizable level. Direct shielding for any commercial humanoid claim on LIDAR-only SLAM, subterranean autonomy, or multi-robot heterogeneous-platform coordination.

## DROID-SLAM (2021-12)

- **id**: `droid-slam-2021`
- **corpus**: academic
- **creator**: Princeton Vision and Learning Lab; Zachary Teed, Jia Deng
- **disclosure**: Teed, Z., Deng, J. 'DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras'. NeurIPS 2021. arXiv:2108.10869. BSD-3-Clause source: github.com/princeton-vl/DROID-SLAM. Princeton Vision and Learning Lab.
- **ip status**: open-permissive
- **prior art notes**: DROID-SLAM is the canonical dense differentiable-visual-SLAM academic system (NeurIPS 2021, BSD-3 open source). 4-year-deep prior art anticipating any humanoid claim on dense / differentiable / foundation-model-grounded visual SLAM. Immediate ancestor of ViPE (Princeton 2024-2025) and RADIO-ViPE (ITMO 2026 — round-10 entry). Together with ORB-SLAM3, establishes the academic SLAM baseline against which all modern humanoid perception claims must be evaluated.

## SemGauss-SLAM (2024-03)

- **id**: `semgauss-slam-2024`
- **corpus**: academic
- **creator**: Zhu, Siting et al. (per arXiv 2403.07494)
- **disclosure**: Zhu, S., et al. 'SemGauss-SLAM: Dense Semantic Gaussian Splatting SLAM'. arXiv:2403.07494, March 2024.
- **ip status**: open-permissive
- **prior art notes**: SemGauss-SLAM is one of the first dense-semantic Gaussian-splatting SLAM systems (March 2024). 14-month-deep prior art for combining 3D Gaussian representations with per-primitive semantic features. Predates and informs the open-vocabulary GS-SLAM lineage that WildGS-SLAM, LEG-SLAM, LEGO-SLAM, and RADIO-ViPE descend from.

## RoDyn-SLAM (2024-07)

- **id**: `rodyn-slam-jiang-2024`
- **corpus**: academic
- **creator**: Fudan University ZVG; Haochen Jiang, Yueming Xu, Kejie Li, Jianfeng Feng, Li Zhang
- **disclosure**: Jiang, H., Xu, Y., Li, K., Feng, J., Zhang, L. 'RoDyn-SLAM: Robust Dynamic Dense RGB-D SLAM with Neural Radiance Fields'. IEEE Robotics and Automation Letters 2024. arXiv:2407.01303 July 2024. Fudan University ZVG (Zhang Vision Group).
- **ip status**: open-permissive
- **prior art notes**: RoDyn-SLAM is Fudan ZVG's NeRF-based dynamic-scene SLAM (IEEE RAL 2024). 10-month-deep prior art on the NeRF branch of dynamic SLAM (distinct from the GS-based lineage of WildGS-SLAM, DGS-SLAM, DG-SLAM, etc.). Cited as a competitor in RADIO-ViPE Table II — the TUM-RGBD ATE benchmark RADIO-ViPE compares against. Together with DGS-SLAM, DG-SLAM, WildGS-SLAM, and DynaSLAM, establishes the academic dynamic-SLAM substrate that RADIO-ViPE measures itself against.

## DGS-SLAM (2024-11)

- **id**: `dgs-slam-kong-2024`
- **corpus**: academic
- **creator**: Mangyu Kong, Jaewon Lee, Seongwon Lee, Euntai Kim (per arXiv 2411.10722)
- **disclosure**: Kong, M., Lee, J., Lee, S., Kim, E. 'DGS-SLAM: Gaussian Splatting SLAM in Dynamic Environment'. arXiv:2411.10722, November 2024.
- **ip status**: open-permissive
- **prior art notes**: DGS-SLAM (Kong et al. arXiv 2411.10722, November 2024). 6-month-deep prior art on dynamic-aware Gaussian-splatting SLAM. Cited as a competitor in the RADIO-ViPE Table II TUM-RGBD ATE benchmark; the round-10 RADIO-ViPE entry's claim of SOTA is anchored by comparison against this and several sibling systems. Direct shielding for any commercial humanoid claim on dynamic-scene GS-SLAM.

## MegaSaM (2024-12)

- **id**: `megasam-google-2024`
- **corpus**: academic
- **creator**: Google DeepMind + UC Berkeley + U. Michigan (per arXiv 2412.04463)
- **disclosure**: Authors per arXiv 2412.04463. 'MegaSaM: Accurate, Fast, and Robust Structure and Motion from Casual Dynamic Videos'. arXiv:2412.04463, December 2024. Google DeepMind + UC Berkeley + University of Michigan.
- **ip status**: open-permissive
- **prior art notes**: MegaSaM (Dec 2024) is the immediate predecessor to NVIDIA ViPE in the calibration-free dynamic-monocular-video pose+depth lineage. 5-month-deep prior art for: differentiable BA with monocular depth priors + uncertainty-aware global BA on in-the-wild dynamic videos. ViPE explicitly outperforms MegaSaM in its results table; that comparison only exists if MegaSaM is the prior art baseline. Direct shielding for any commercial humanoid claim on calibration-free in-the-wild video perception.

## WildGS-SLAM (2025-04)

- **id**: `wildgs-slam-2025`
- **corpus**: academic
- **creator**: Jianhao Zheng, Zihan Zhu, Valentin Bieri, Marc Pollefeys (ETH Zürich), Songyou Peng, Iro Armeni (Stanford GradientSpaces)
- **disclosure**: Zheng, J., Zhu, Z., Bieri, V., Pollefeys, M., Peng, S., Armeni, I. 'WildGS-SLAM: Monocular Gaussian Splatting SLAM in Dynamic Environments'. CVPR 2025. arXiv:2504.03886. ETH Zürich + Stanford GradientSpaces.
- **ip status**: open-permissive
- **prior art notes**: WildGS-SLAM is the canonical CVPR 2025 monocular dynamic-scene Gaussian-splatting SLAM system from ETH + Stanford. Establishes 1-year-deep prior art for: monocular GS-SLAM with dynamic-scene robustness, photorealistic novel-view rendering of static background while filtering dynamic foreground. Among the systems RADIO-ViPE benchmarks against (TUM-RGBD dynamic). Direct shielding for any commercial humanoid claim on monocular dynamic-scene mapping with photorealistic reconstruction.

## LEG-SLAM (2025-06)

- **id**: `leg-slam-2025`
- **corpus**: academic
- **creator**: LEG-SLAM authors (per arXiv 2506.03073)
- **disclosure**: Authors per arXiv 2506.03073. 'LEG-SLAM: Real-Time Language-Enhanced Gaussian Splatting for SLAM'. arXiv:2506.03073, June 2025.
- **ip status**: open-permissive
- **prior art notes**: LEG-SLAM (June 2025) is a real-time language-enhanced GS-SLAM system. 11-month-deep prior art on: real-time fps-class language-aligned GS-SLAM, DINOv2 feature compression for compact per-Gaussian language encoding. Distinct from but contemporary with LEGO-SLAM (Nov 2025). Both feed the open-vocab GS-SLAM lineage that RADIO-ViPE compares against.

## ViPE (Video Pose Engine) (2025-08)

- **id**: `nvidia-vipe-2025`
- **corpus**: academic
- **creator**: NVIDIA Toronto AI Lab (nv-tlabs); multi-author
- **disclosure**: Huang, J., et al. (NVIDIA Toronto AI Lab + collaborators). 'ViPE: Video Pose Engine for 3D Geometric Perception'. arXiv:2508.10934, August 2025. Open-source release via nv-tlabs/vipe.
- **ip status**: open-permissive
- **prior art notes**: ViPE is NVIDIA Toronto AI Lab's canonical Video Pose Engine, August 2025 arXiv. Sits **directly between DROID-SLAM (2021) and RADIO-ViPE (2026)** in the visual-SLAM lineage: it is RADIO-ViPE's explicit foundation per the round-10 paper's text ('we build upon ViPE [5]'). 9-month-deep open-permissive academic prior art for: calibration-free metric depth from uncalibrated video, dense bundle adjustment over heterogeneous camera models, online video pose estimation at 3-5 FPS. Direct shielding for any commercial humanoid claim on uncalibrated-camera onboard 3D perception. Plus the 96M-frame released dataset is itself prior art for any humanoid-vision data-curation IP.

## LEGO-SLAM (2025-11)

- **id**: `lego-slam-2025`
- **corpus**: academic
- **creator**: Lab of AI and Robotics (per github.com/Lab-of-AI-and-Robotics/LEGO-SLAM)
- **disclosure**: Authors per arXiv 2511.16144. 'LEGO-SLAM: Language-Embedded Gaussian Optimization SLAM'. arXiv:2511.16144, November 2025. Lab of AI and Robotics.
- **ip status**: open-permissive
- **prior art notes**: LEGO-SLAM (Nov 2025) is the first claimed real-time open-vocabulary GS-SLAM system. 6-month-deep prior art for: 16-dim language-feature compression in GS, language-guided Gaussian pruning. Direct shielding for any commercial humanoid claim on real-time onboard open-vocabulary scene mapping. Together with LEG-SLAM, LEGS, and SemGauss-SLAM, the open-vocab GS-SLAM corpus is now ~6-month to 14-month deep across five contemporary systems — fully covering the architectural surface of RADIO-ViPE's competitor table.

## RADIO-ViPE (2026-04)

- **id**: `radio-vipe-itmo-2026`
- **corpus**: academic
- **creator**: ITMO University BE2R Lab; Nasser, Iumanov, Li, Popov, Mahmoud, Kolyubin
- **disclosure**: Nasser, Z., Iumanov, M., Li, T., Popov, M., Mahmoud, J., Kolyubin, S. 'RADIO-ViPE: Online Tightly Coupled Multi-Modal Fusion for Open-Vocabulary Semantic SLAM in Dynamic Environments'. arXiv:2604.26067v1, April 28, 2026. ITMO University, Biomechatronics and Energy-Efficient Robotics (BE2R) Lab, Saint Petersburg, Russia.
- **ip status**: open-permissive
- **prior art notes**: RADIO-ViPE is the most recent and architecturally complete online open-vocabulary semantic SLAM system. April 2026 arXiv preprint; 9 days before this corpus entry. Establishes very-recent (sub-1-week) open-academic prior art for: calibration-free monocular semantic SLAM, tightly-coupled multi-modal fusion (RADIO + SigLIP + geometric BA), adaptive-kernel dynamic-scene robustness, online operation at 8-10 FPS. Directly shields any commercial humanoid claim on: 'onboard semantic scene understanding from monocular video' (Tesla Optimus, Figure 02, 1X NEO, Apptronik Apollo, etc. all face this), 'language-grounded robotic perception in dynamic environments', 'calibration-free humanoid camera deployment'. The TUM-RGBD ATE comparison table in Table II of the paper enumerates the prior art — RADIO-ViPE outperforms Dyna-SLAM, DLD-SLAM, V3D-SLAM, DGS-SLAM, RoDyn-SLAM, DynaMON, ViPE — every one of which is itself open-academic prior art for humanoid perception. Lineage: ORB-SLAM3 (geometric baseline) → DROID-SLAM (dense differentiable) → ViPE (Princeton in-the-wild metric depth) → RADIO-ViPE (ITMO open-vocab + calibration-free).
