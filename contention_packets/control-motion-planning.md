---
title: "control-motion-planning"
parent: "Invalidity Contentions"
nav_order: 69
layout: default
---

# Invalidity Contention Packet — `control-motion-planning`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-motion-planning`  
**Entries:** 3 (3 commons-grade, 0 draft)  
**Earliest disclosure:** 1998-10  
**Most recent disclosure:** 2013-01

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-motion-planning`.

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

### 1998-10 — Rapidly-exploring Random Tree (RRT)

- **id:** `rrt-lavalle-1998`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Iowa State University; Steven M. LaValle
- **disclosure citation:** LaValle, S. M. 'Rapidly-Exploring Random Trees: A New Tool for Path Planning'. Computer Science Department, Iowa State University, TR 98-11, October 1998. Subsequent: LaValle + Kuffner ICRA 2000. Karaman + Frazzoli IJRR 2011 (RRT*).
- **disclosed subsystems:** `control-motion-planning`, `control-sampling-based-planning`

**Prior art notes:**

> RRT (LaValle Iowa State 1998) is the foundational sampling-based motion-planning algorithm. 27-year-deep public-domain prior art. >18,000 citations on the original. The dominant motion planner in every humanoid + manipulator academic + commercial motion-planning library (MoveIt!, OMPL, etc.).

**Sources:**

1. LaValle, S. M. Iowa State TR 98-11 1998.
2. LaValle, S. M., Kuffner, J. ICRA 2000.
3. Karaman, S., Frazzoli, E. IJRR 2011 (RRT*).
4. LaValle, S. M. 'Planning Algorithms' Cambridge UP 2006 (canonical textbook).

---

### 2003-09 — LAAS-CNRS Toulouse humanoid robotics

- **id:** `laas-cnrs-toulouse-humanoid-2003`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** LAAS-CNRS Toulouse; Jean-Paul Laumond, Olivier Stasse, Florent Lamiraux et al.
- **disclosure citation:** Laboratoire d'Analyse et d'Architecture des Systèmes (LAAS-CNRS), Toulouse, France. Founded 1968; one of CNRS's largest joint research units. **HRP-2 humanoid deployed at LAAS 2003** as the first European HRP-2 unit (under joint Japanese-French research agreement). Subsequent: HRP-2 then HRP-4 deployments. Notable researchers: Jean-Paul Laumond (motion planning), Olivier Stasse (humanoid manipulation), Florent Lamiraux.
- **disclosed subsystems:** `control-research-cluster`, `control-whole-body-qp`, `control-motion-planning`, `mechanism-bipedal-locomotion`

**Prior art notes:**

> LAAS-CNRS Toulouse is the foundational European humanoid research lab (HRP-2 deployment 2003+). 22-year-deep public-domain academic prior art. **The origin of the Pinocchio rigid-body dynamics library** that underlies OCS2 and Crocoddyl (corpus entry mastalli-crocoddyl-2020). Direct shielding for any commercial humanoid claim on whole-body dynamics computation or motion-planning theory. Brings French-academic robotics depth in the corpus from 13 to 14 entries.

**Sources:**

1. LAAS-CNRS corporate site (laas.fr).
2. Pinocchio library (github.com/stack-of-tasks/pinocchio).
3. Laumond + Stasse + Lamiraux publications.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `69278e1`.*
