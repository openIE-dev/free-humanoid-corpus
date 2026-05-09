---
title: "control-middleware"
parent: "Invalidity Contentions"
nav_order: 66
layout: default
---

# Invalidity Contention Packet — `control-middleware`

**Generated:** 2026-05-09  
**Cross-cut tag:** `control-middleware`  
**Entries:** 4 (4 commons-grade, 0 draft)  
**Earliest disclosure:** 2009-05  
**Most recent disclosure:** 2017-12

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-middleware`.

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

### 2009-05 — ROS (Robot Operating System)

- **id:** `ros-quigley-2009`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Stanford AI Lab + Willow Garage; Quigley, Conley, Gerkey, Faust, Foote, Leibs, Wheeler, Ng
- **disclosure citation:** Quigley, M., Conley, K., Gerkey, B., Faust, J., Foote, T., Leibs, J., Wheeler, R., Ng, A. Y. 'ROS: an open-source Robot Operating System'. ICRA 2009 Workshop on Open Source Software. Stanford / Willow Garage. First public release 2007. BSD-3-Clause / Apache-2.0. Stewardship transferred to Open Robotics.
- **disclosed subsystems:** `control-middleware`, `control-publish-subscribe`

**Prior art notes:**

> ROS is the canonical open-source robotics middleware (2007 internal, 2009 ICRA workshop publication). 17-year-deep BSD-3 / Apache-2.0 open-permissive prior art. Effectively every academic robotic system of the 2010s and 2020s integrates via ROS or ROS 2 — including all of the open humanoid platforms (Berkeley Humanoid, ToddlerBot, Pollen Reachy) in the corpus. Direct shielding for any commercial humanoid claim on 'modular driver-publishing-subscribing robotics middleware', message-passing inter-process communication for robots, or the standard tool-stack patterns it established (rosbag, rviz, tf, MoveIt).

**Sources:**

1. Quigley et al. ICRA 2009 Workshop on Open Source Software.
2. ROS official site (ros.org).
3. Open Robotics (openrobotics.org).

---

### 2010-12 — TurtleBot

- **id:** `turtlebot-willow-garage-2010`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Willow Garage (initial); subsequent Robotis (TB3) + Clearpath Robotics (TB4)
- **disclosure citation:** Willow Garage. TurtleBot reveal December 2010 as a low-cost ROS-integrated educational mobile robot. Subsequent versions: TurtleBot 2 (2012), TurtleBot 3 (2017, Robotis-manufactured), TurtleBot 4 (2022, Clearpath Robotics-manufactured). turtlebot.com.
- **disclosed subsystems:** `mechanism-mobile-base`, `control-rl-policy`, `control-middleware`

**Prior art notes:**

> TurtleBot (Willow Garage 2010+) is the canonical foundational ROS educational mobile robot. 15-year-deep open-permissive prior art. The hardware platform underlying every ROS tutorial globally + 1000+ academic publications. Direct shielding for any commercial humanoid claim derived from low-cost mobile-robot educational platforms.

**Sources:**

1. TurtleBot site (turtlebot.com).
2. Willow Garage product history.

---

### 2013-01 — MoveIt! motion-planning framework

- **id:** `moveit-sucan-icra-2014`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Willow Garage / Open Robotics; Ioan Sucan, Sachin Chitta + community
- **disclosure citation:** Sucan, I. A., Chitta, S. 'MoveIt!'. Open-source ROS motion-planning framework. Initial release 2013. moveit.ros.org. Willow Garage / SRI / PickNik Robotics maintenance lineage.
- **disclosed subsystems:** `control-motion-planning`, `control-middleware`

**Prior art notes:**

> MoveIt! (Sucan + Chitta Willow Garage 2013+) is the foundational ROS motion-planning framework. 12-year-deep open-permissive prior art. The de facto library for academic + industrial robots integrating with ROS. Direct shielding for any commercial humanoid claim using ROS-integrated motion-planning libraries.

**Sources:**

1. MoveIt! site (moveit.ros.org).
2. GitHub: github.com/ros-planning/moveit.

---

### 2017-12 — ROS 2

- **id:** `ros-2-2017`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Open Robotics; multi-author community
- **disclosure citation:** Open Robotics. ROS 2 'Ardent Apalone' first stable release December 8, 2017. Architectural redesign of ROS atop DDS (Data Distribution Service) for real-time, multi-vehicle, and embedded use. Apache-2.0.
- **disclosed subsystems:** `control-middleware`, `control-real-time-communication`, `control-publish-subscribe`

**Prior art notes:**

> ROS 2 is the modern academic + commercial robotics middleware (2017+). 8-year-deep open-permissive prior art for: real-time DDS-based robotics middleware, lifecycle-managed component architectures for multi-robot systems, QoS-aware inter-vehicle messaging. All four free-humanoid-family morphologies (platform/wheeled/centaur/submersible) commit to ROS 2 as the integration substrate, shielded by this entry.

**Sources:**

1. ROS 2 documentation (docs.ros.org).
2. Macenski, S., Foote, T., Gerkey, B., Lalancette, C., Woodall, W. 'Robot Operating System 2: Design, architecture, and uses in the wild'. Science Robotics 7(66) 2022.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `d6a964d`.*
