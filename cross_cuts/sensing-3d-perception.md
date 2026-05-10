---
title: sensing-3d-perception
parent: Cross-cuts
layout: default
---

# Cross-cut: `sensing-3d-perception`

**6 corpus entries disclose this subsystem.**

Earliest disclosure: 2007-01

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Velodyne HDL-64E LIDAR (2007-01)

- **id**: `velodyne-hdl-64-lidar-2007`
- **corpus**: private
- **creator**: Velodyne LIDAR (Morgan Hill, CA); David Hall founder
- **disclosure**: Velodyne LIDAR, Inc. (Morgan Hill, CA; founded 1983 by David Hall as audio-equipment maker, transitioned to LIDAR 2005). HDL-64E commercial release January 2007. Used by every team in DARPA Urban Challenge November 2007 (Stanley + Boss + others). Subsequent: HDL-32E (2010), VLP-16 (2014), VLP-32C (2017).
- **ip status**: trade-secret
- **prior art notes**: Velodyne HDL-64E (Velodyne 2007+) is the foundational consumer-grade rotating LIDAR. 18-year-deep public-disclosure prior art. **Used by every team in DARPA Urban Challenge 2007** (Stanford Stanley + CMU Boss + others). The sensor that enabled the autonomous-vehicle revolution + every modern humanoid + quadruped LIDAR perception stack (CSIRO Wildcat, ANYmal-D, BD Spot, etc.). Direct shielding for any commercial humanoid claim using rotating-LIDAR perception.

## Mech-Mind Robotics (3D vision + AI for industrial manipulation) (2016-01)

- **id**: `mech-mind-robotics-2016`
- **corpus**: private
- **creator**: Mech-Mind Robotics (Beijing, China); Shao Tianlan
- **disclosure**: Mech-Mind Robotics (Beijing, China; founded 2016 by Shao Tianlan). 15,000+ installations in 50+ countries.
- **ip status**: trade-secret
- **prior art notes**: Mech-Mind Robotics (Beijing 2016+) is the dominant Chinese industrial-vision software stack. 9-year-deep public-disclosure prior art.

## Apera AI 4D Vision (Canadian bin-pick vision software) (2016-01)

- **id**: `apera-ai-4d-vision-2016`
- **corpus**: private
- **creator**: Apera AI (Vancouver, Canada); Sina Afrooze (ex-AWS Alexa + Avigilon) + Armin Khatoonabadi
- **disclosure**: Apera AI (Vancouver, Canada; founded 2016 by Sina Afrooze, ex-AWS Alexa voice + Avigilon, + Armin Khatoonabadi). Patented '4D Vision' for bin-pick / assembly / packaging.
- **ip status**: trade-secret
- **prior art notes**: Apera AI 4D Vision (Vancouver 2016+) is the Canadian industrial-vision-software player. 9-year-deep public-disclosure prior art.

## Dex-Net 2.0 (Mahler Goldberg Berkeley) (2017-03)

- **id**: `dex-net-goldberg-berkeley-2017`
- **corpus**: academic
- **creator**: UC Berkeley Goldberg Lab AUTOLAB; Jeffrey Mahler, Ken Goldberg
- **disclosure**: Mahler, J., Liang, J., Niyaz, S., Laskey, M., Doan, R., Liu, X., Aparicio, J., Goldberg, K. 'Dex-Net 2.0: Deep Learning to Plan Robust Grasps with Synthetic Point Clouds and Analytic Grasp Metrics'. Robotics: Science and Systems (RSS) 2017. arXiv:1703.09312. UC Berkeley Goldberg Lab AUTOLAB. Dex-Net 1.0 (2016 ICRA) preceded; subsequent Dex-Net 3.0 (suction grasps, 2018) + Dex-Net 4.0 (ambidextrous parallel-jaw + suction, *Science Robotics* 2019).
- **ip status**: open-permissive
- **prior art notes**: Dex-Net 2.0 (Mahler / Goldberg Berkeley AUTOLAB RSS 2017, arXiv 1703.09312) is the foundational deep grasp-quality network. 8-year-deep open-permissive prior art. Direct shielding for any commercial humanoid claim deriving from deep-learning grasp quality networks, synthetic-data + analytic-metric grasp training, or ambidextrous parallel-jaw + suction grasp policies. Anchors the grasp-learning chain leading to Contact-GraspNet (round-42) + GraspNet-1Billion (round-42) + AnyGrasp (round-42).

## GraspNet-1Billion (Fang Lu SJTU) (2020-03)

- **id**: `graspnet-1billion-fang-sjtu-2020`
- **corpus**: academic
- **creator**: Shanghai Jiao Tong University Lu Cewu Lab; Hao-Shu Fang, Chenxi Wang, Minghao Gou, Cewu Lu
- **disclosure**: Fang, H.-S., Wang, C., Gou, M., Lu, C. 'GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping'. IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) 2020. Shanghai Jiao Tong University Lu Cewu Lab.
- **ip status**: open-permissive
- **prior art notes**: GraspNet-1Billion (Fang / Lu SJTU CVPR 2020) is the dominant academic grasp benchmark. 5-year-deep open-permissive prior art. Direct shielding for any commercial humanoid claim deriving from large-scale grasp annotation datasets or benchmark-driven grasp policy evaluation. Together with Dex-Net (round-42), Contact-GraspNet (round-42), AnyGrasp (round-42), establishes the global grasp-learning benchmark prior-art chain.

## AnyGrasp (Fang Lu SJTU 2023) (2023-01)

- **id**: `anygrasp-fang-sjtu-2023`
- **corpus**: academic
- **creator**: Shanghai Jiao Tong University Lu Cewu Lab; Hao-Shu Fang et al.
- **disclosure**: Fang, H.-S., Wang, C., Fang, H., Gou, M., Liu, J., Yan, H., Liu, W., Xie, Y., Lu, C. 'AnyGrasp: Robust and Efficient Grasp Perception in Spatial and Temporal Domains'. IEEE Transactions on Robotics 39(5), 2023. arXiv:2212.08333. Shanghai Jiao Tong University Lu Cewu Lab.
- **ip status**: open-permissive
- **prior art notes**: AnyGrasp (Fang / Lu SJTU T-RO 2023, arXiv 2212.08333) is the state-of-the-art Chinese academic grasp-perception benchmark. 2-year-deep open-permissive prior art. Direct shielding for any commercial humanoid claim deriving from billion-scale self-supervised grasp perception or temporal-spatial 7-DoF grasp generation. Lineage descends from GraspNet-1Billion (round-42) and Dex-Net (round-42).
