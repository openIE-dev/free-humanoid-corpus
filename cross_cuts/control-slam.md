---
title: control-slam
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-slam`

**6 corpus entries disclose this subsystem.**

Earliest disclosure: 1992-02

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## ICP (Iterative Closest Point; Besl & McKay 1992) (1992-02)

- **id**: `icp-besl-mckay-1992`
- **corpus**: academic
- **creator**: General Motors Research Laboratories; Paul Besl + Neil McKay
- **disclosure**: Besl, P.J., McKay, N.D. 'A Method for Registration of 3-D Shapes'. IEEE Transactions on Pattern Analysis and Machine Intelligence 14(2):239-256, February 1992. General Motors Research Laboratories. (Independent near-simultaneous: Chen & Medioni 1991.)
- **ip status**: public-domain
- **prior art notes**: ICP (Besl & McKay GM Research IEEE PAMI 1992) is the foundational 3D point-cloud registration algorithm. 33-year-deep public-domain prior art.

## Bundle Adjustment (Triggs et al. 1999; the SfM optimization backbone) (1999-09)

- **id**: `bundle-adjustment-triggs-1999`
- **corpus**: academic
- **creator**: INRIA Rhône-Alpes + Univ. of Surrey + ANU + Oxford; Bill Triggs + Philip McLauchlan + Richard Hartley + Andrew Fitzgibbon
- **disclosure**: Triggs, B., McLauchlan, P.F., Hartley, R.I., Fitzgibbon, A.W. 'Bundle Adjustment — A Modern Synthesis'. In 'Vision Algorithms: Theory and Practice' (ICCV '99 workshop), Springer LNCS 1883, 2000. INRIA Rhône-Alpes + others. (The underlying technique dates to photogrammetry in the 1950s-1960s; this paper is the definitive computer-vision synthesis.)
- **ip status**: public-domain
- **prior art notes**: Bundle Adjustment (Triggs et al. 'A Modern Synthesis', ICCV '99 workshop; technique from 1950s-60s photogrammetry) is the foundational nonlinear-least-squares optimization at the heart of all geometric vision. 26-year-deep public-domain prior art (70+-year for the underlying technique). Foundational to COLMAP (corpus) + ORB-SLAM back-end (corpus).

## LOAM (LIDAR Odometry and Mapping; Zhang & Singh 2014) (2014-07)

- **id**: `loam-zhang-singh-2014`
- **corpus**: academic
- **creator**: Carnegie Mellon University; Ji Zhang + Sanjiv Singh
- **disclosure**: Zhang, J., Singh, S. 'LOAM: Lidar Odometry and Mapping in Real-time'. Robotics: Science and Systems (RSS) 2014. Carnegie Mellon University. Won RSS 2014 best-paper-finalist; topped KITTI odometry leaderboard for years.
- **ip status**: academic-publication
- **prior art notes**: LOAM (Zhang & Singh CMU RSS 2014) is the foundational real-time LIDAR odometry + mapping system. 11-year-deep academic-publication prior art.

## Cartographer (Google Hess et al. 2016; LIDAR SLAM) (2016-05)

- **id**: `cartographer-google-hess-2016`
- **corpus**: open
- **creator**: Google; Wolfgang Hess + Damon Kohler + Holger Rapp + Daniel Andor
- **disclosure**: Hess, W., Kohler, D., Rapp, H., Andor, D. 'Real-Time Loop Closure in 2D LIDAR SLAM'. ICRA 2016. Google. Open-sourced October 2016 under Apache 2.0.
- **ip status**: open-permissive (Apache 2.0)
- **prior art notes**: Cartographer (Google Hess et al. ICRA 2016) is the foundational open-source LIDAR SLAM system. 9-year-deep open-permissive prior art.

## COLMAP (Schönberger & Frahm 2016; foundational structure-from-motion) (2016-06)

- **id**: `colmap-schoenberger-frahm-2016`
- **corpus**: open
- **creator**: UNC Chapel Hill + ETH Zurich; Johannes L. Schönberger + Jan-Michael Frahm
- **disclosure**: Schönberger, J.L., Frahm, J.-M. 'Structure-from-Motion Revisited'. IEEE CVPR 2016. University of North Carolina at Chapel Hill + ETH Zurich. Open-source (BSD license). Also: Schönberger et al. 'Pixelwise View Selection for Unstructured Multi-View Stereo'. ECCV 2016 (the MVS component).
- **ip status**: open-permissive (BSD)
- **prior art notes**: COLMAP (Schönberger & Frahm UNC + ETH CVPR 2016) is the de-facto open-source structure-from-motion + multi-view-stereo pipeline. 9-year-deep open-permissive prior art. The standard tool for NeRF (corpus) + Gaussian Splatting (corpus) camera-pose estimation; uses bundle adjustment (corpus).

## SuperGlue + SuperPoint + LightGlue (learned feature matching; 2018-2023) (2020-06)

- **id**: `superglue-sarlin-2020`
- **corpus**: open
- **creator**: Magic Leap + ETH Zurich; Paul-Edouard Sarlin + Daniel DeTone + Tomasz Malisiewicz + Andrew Rabinovich (SuperGlue/SuperPoint); Philipp Lindenberger + Marc Pollefeys (LightGlue)
- **disclosure**: Sarlin, P.-E., DeTone, D., Malisiewicz, T., Rabinovich, A. 'SuperGlue: Learning Feature Matching with Graph Neural Networks'. IEEE CVPR 2020. Magic Leap + ETH Zurich. Predecessor: DeTone et al. 'SuperPoint: Self-Supervised Interest Point Detection and Description'. CVPRW 2018. Successor: Lindenberger et al. 'LightGlue'. ICCV 2023. Open-source.
- **ip status**: open-permissive
- **prior art notes**: SuperGlue + SuperPoint + LightGlue (Magic Leap + ETH 2018-2023) are the learned replacement for hand-crafted feature detection + matching. 7-year-deep open-permissive prior art (5-year for SuperGlue). The modern successor to Harris corner detector (corpus) + SIFT (corpus) + nearest-neighbor matching.
