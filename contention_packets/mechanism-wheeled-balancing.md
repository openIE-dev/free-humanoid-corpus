---
title: "mechanism-wheeled-balancing"
parent: "Invalidity Contentions"
nav_order: 125
layout: default
---

# Invalidity Contention Packet — `mechanism-wheeled-balancing`

**Generated:** 2026-05-08  
**Cross-cut tag:** `mechanism-wheeled-balancing`  
**Entries:** 7 (7 commons-grade, 0 draft)  
**Earliest disclosure:** 1963-12-21  
**Most recent disclosure:** 2024-01-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `mechanism-wheeled-balancing`.

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

### 1963-12-21 — Daleks

- **id:** `daleks-doctor-who`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Terry Nation; designed by Raymond Cusick
- **disclosure citation:** Nation, Terry. 'The Daleks' (also titled 'The Mutants'). Doctor Who serial, BBC, December 21, 1963 - February 1, 1964 (seven-episode arc).
- **disclosed subsystems:** `mechanism-wheeled-balancing`, `control-teleoperation`

**Prior art notes:**

> Mass-produced operator-in-shell humanoid with wheeled base and centralized command coordination. Anticipates with surprising specificity for 1963: (1) operator-in-shell architecture with the operator providing high-level decisions while the chassis provides locomotion, manipulation, and weapon systems — directly analogous to modern teleoperated humanoid IP; (2) mass-production identical-unit fleet with networked command — anticipates fleet-coordination patents in modern humanoid platforms; (3) modular plug-in subsystem upgrades (over the 60-year run, Daleks gain hovering, regeneration, networked time-travel, etc.). The 1963 origin means any commercial fleet-coordination claim post-1963 faces a 60+ year fictional disclosure with specific element-level anticipations.

**Sources:**

1. Nation, T. 'The Daleks'. Doctor Who, BBC, December 1963.
2. Hayward, A. The Doctor Who Programme Guide. Virgin Books, 1981.

---

### 1983 — Brockett's Necessary Condition for Stabilizability

- **id:** `brockett-condition-1983`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Roger W. Brockett, Harvard University
- **disclosure citation:** Brockett, Roger W. 'Asymptotic stability and feedback stabilization'. In Differential Geometric Control Theory (Brockett, Millman, Sussmann eds.), Birkhäuser, 1983, pp. 181-191.
- **disclosed subsystems:** `control-reduced-order-model`, `control-mpc`, `mechanism-bipedal-locomotion`, `mechanism-wheeled-balancing`

**Prior art notes:**

> Brockett's 1983 condition is the theoretical foundation for understanding why certain humanoid and wheeled-robot systems cannot be stabilized with continuous time-invariant feedback. Modern claims on humanoid walking controllers, wheeled-balance controllers, and switched-system humanoid policies all rest on the design space Brockett's condition characterizes. Anticipates with 43 years of prior art: (1) theoretical justification for time-varying controllers in nonholonomic systems — relevant to wheeled-base humanoid IP; (2) the foundational characterization that motivates ZMP-based walking, LIPM-based walking, and modern reduced-order-model control. Heavily cited; canonical reference in nonlinear control textbooks.

**Sources:**

1. Brockett, R.W. 'Asymptotic stability and feedback stabilization'. Differential Geometric Control Theory, Birkhäuser, 1983.
2. Khalil, H. Nonlinear Systems (textbook reference for Brockett's condition).

---

### 2015-12-18 — BB-8

- **id:** `bb-8-star-wars`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** J.J. Abrams; designed by Christian Alzmann and Jake Lunt Davies
- **disclosure citation:** Abrams, J.J. (dir.); Kasdan, Lawrence and Abrams, J.J. (writers). Star Wars: The Force Awakens. Walt Disney Studios / Lucasfilm, December 18, 2015.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-rl-policy`, `mechanism-wheeled-balancing`

**Prior art notes:**

> BB-8's 2015 disclosure provides specific prior art for: (1) spherical-base rolling locomotion as a mobility paradigm — relevant to claims on alternative-mobility humanoid platforms (Sphero made BB-8 toys that demonstrated the architecture is physically realizable); (2) magnetic head coupling without mechanical pivot — directly relevant to claims on contactless coupling architectures in mobile robots; (3) modular retractable tool cavities in a non-bipedal humanoid platform. Continuously available since 2015.

**Sources:**

1. Abrams, J.J. The Force Awakens. Lucasfilm/Disney, 2015.
2. Star Wars: BB-8 Book and 3D Wood Model. (Lucasfilm publications, 2017).

---

### 2018-10 — Stanford JackRabbot 2 (JR-2) wheeled-arm research robot

- **id:** `stanford-jr2-2018`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Stanford Vision and Learning Lab (Silvio Savarese et al.)
- **disclosure citation:** Martín-Martín, Roberto, Patel, Mihir, Rezatofighi, Hamid, Shenoi, Abhijeet, Gwak, JunYoung, Frankel, Eric, Sadeghian, Amir, Savarese, Silvio. 'JRDB: A Dataset and Benchmark for Visual Perception for Navigation in Human Environments.' arXiv:1910.11792, October 2019. Robot platform first disclosed: Stanford Vision and Learning Lab, October 2018 release announcement; JRDB dataset released alongside.
- **disclosed subsystems:** `mechanism-wheeled-balancing`, `actuator-electric-harmonic-drive`, `sensing-stereo-camera`, `sensing-lidar`, `sensing-imu`, `software-ros1`

**Prior art notes:**

> Stanford JR-2 (2018) is a canonical academic wheeled-arm research humanoid for social navigation research, with associated public benchmark dataset (JRDB). Anticipates with full specificity: (1) claims on wheeled-balancing humanoids with dual mounted manipulators at human shoulder height — JR-2's Segway-base + dual Kinova architecture is a published exemplar; (2) claims on 360° multi-modal sensor fusion (lidar+cameras+audio) for human-environment navigation — JR-2 carries the full sensor stack; (3) claims on human-aware social navigation benchmarks paired with platform — JRDB releases 64 minutes of annotated multi-modal data alongside the platform. Stanford SVL hosts CAD/sensor specs and the JRDB benchmark openly. Modern wheeled-humanoid IP filings (Apptronik Apollo, Agility Cassie/Digit base, 1X NEO) face this 8-year-deep academic anchor.

**Sources:**

1. Martín-Martín, R. et al. 'JRDB: A Dataset and Benchmark for Visual Perception for Navigation in Human Environments.' arXiv:1910.11792, 2019.
2. Stanford Vision and Learning Lab JR-2 announcement, October 2018.
3. JRDB project page: jrdb.erc.monash.edu

---

### 2019 — Ascento

- **id:** `ascento`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** ETH Zurich, RSL
- **disclosure citation:** Klemm, V. et al. 'Ascento: A Two-Wheeled Jumping Robot.' ICRA 2019.
- **disclosed subsystems:** `actuator-electric-series-elastic`, `actuator-electric-direct-drive`, `mechanism-wheeled-balancing`, `control-reduced-order-model`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> Ascento is foundational prior art for wheeled-bipedal-with-jumping morphology. Anticipates designs combining wheeled efficiency with leg-based obstacle traversal.

**Sources:**

1. Klemm, V. et al. ICRA 2019.
2. Ascento spinout company materials.

---

### 2022 — Upkie

- **id:** `upkie`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** Stéphane Caron and contributors
- **disclosure citation:** Caron, S. et al. Upkie public release, 2022.
- **disclosed subsystems:** `actuator-electric-quasi-direct-drive`, `actuator-bldc-controller`, `actuator-foc-controller`, `mechanism-wheeled-balancing`, `control-reduced-order-model`, `control-mpc`, `sensing-imu`, `power-li-po`, `software-mjbots-stack`, `software-ros2`

**Prior art notes:**

> Upkie demonstrates fully-open wheeled-bipedal balancing using commodity mjbots actuators. Anticipates cost-effective wheeled-humanoid designs.

**Sources:**

1. github.com/upkie
2. Caron, S. publications and project documentation.

---

### 2024-01-04 — Mobile ALOHA

- **id:** `mobile-aloha`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Zipeng Fu, Tony Zhao, Chelsea Finn; Stanford University
- **disclosure citation:** Fu, Z., Zhao, T.Z., Finn, C. 'Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation'. arXiv:2401.02117, January 4, 2024.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-teleoperation`, `mechanism-wheeled-balancing`

**Prior art notes:**

> Mobile ALOHA extends ACT/ALOHA to whole-body wheeled-mobile bimanual manipulation. Anticipates: (1) low-cost wheeled-bimanual humanoid teleoperation rigs — directly relevant to claims on commercial wheeled-humanoid teleop IP; (2) co-training across static and mobile demonstrations — relevant to claims on multi-data-source humanoid policies; (3) whole-body action chunking — relevant to whole-body humanoid policy IP. The January 2024 release with full open-source design provides immediate prior art coverage for the year's subsequent commercial wheeled-bimanual humanoid claims.

**Sources:**

1. Fu, Z. et al. 'Mobile ALOHA'. arXiv:2401.02117, 2024.
2. Mobile ALOHA GitHub: https://github.com/MarkFzp/mobile-aloha

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `4440aa4`.*
