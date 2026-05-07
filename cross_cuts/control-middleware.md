---
title: control-middleware
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-middleware`

**2 corpus entries disclose this subsystem.**

Earliest disclosure: 2009-05

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## ROS (Robot Operating System) (2009-05)

- **id**: `ros-quigley-2009`
- **corpus**: academic
- **creator**: Stanford AI Lab + Willow Garage; Quigley, Conley, Gerkey, Faust, Foote, Leibs, Wheeler, Ng
- **disclosure**: Quigley, M., Conley, K., Gerkey, B., Faust, J., Foote, T., Leibs, J., Wheeler, R., Ng, A. Y. 'ROS: an open-source Robot Operating System'. ICRA 2009 Workshop on Open Source Software. Stanford / Willow Garage. First public release 2007. BSD-3-Clause / Apache-2.0. Stewardship transferred to Open Robotics.
- **ip status**: open-permissive
- **prior art notes**: ROS is the canonical open-source robotics middleware (2007 internal, 2009 ICRA workshop publication). 17-year-deep BSD-3 / Apache-2.0 open-permissive prior art. Effectively every academic robotic system of the 2010s and 2020s integrates via ROS or ROS 2 — including all of the open humanoid platforms (Berkeley Humanoid, ToddlerBot, Pollen Reachy) in the corpus. Direct shielding for any commercial humanoid claim on 'modular driver-publishing-subscribing robotics middleware', message-passing inter-process communication for robots, or the standard tool-stack patterns it established (rosbag, rviz, tf, MoveIt).

## ROS 2 (2017-12)

- **id**: `ros-2-2017`
- **corpus**: academic
- **creator**: Open Robotics; multi-author community
- **disclosure**: Open Robotics. ROS 2 'Ardent Apalone' first stable release December 8, 2017. Architectural redesign of ROS atop DDS (Data Distribution Service) for real-time, multi-vehicle, and embedded use. Apache-2.0.
- **ip status**: open-permissive
- **prior art notes**: ROS 2 is the modern academic + commercial robotics middleware (2017+). 8-year-deep open-permissive prior art for: real-time DDS-based robotics middleware, lifecycle-managed component architectures for multi-robot systems, QoS-aware inter-vehicle messaging. All four free-humanoid-family morphologies (platform/wheeled/centaur/submersible) commit to ROS 2 as the integration substrate, shielded by this entry.
