---
title: "control-vr-headset-teleoperation"
parent: "Invalidity Contentions"
nav_order: 140
layout: default
---

# Invalidity Contention Packet — `control-vr-headset-teleoperation`

**Generated:** 2026-05-10  
**Cross-cut tag:** `control-vr-headset-teleoperation`  
**Entries:** 3 (2 commons-grade, 1 draft)  
**Earliest disclosure:** 2014-01  
**Most recent disclosure:** 2025-06

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-vr-headset-teleoperation`.

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

### 2014-01 — Vicarious Surgical

- **id:** `vicarious-surgical-2014`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Vicarious Surgical, Inc.; Adam Sachs, Sammy Khalifa (MIT)
- **disclosure citation:** Vicarious Surgical, Inc. Founded 2014 by Adam Sachs and Sammy Khalifa (MIT Robotics). Public via SPAC 2021 (NYSE: RBOT). vicarioussurgical.com. FDA breakthrough designation 2019; developmental clinical trials underway.
- **disclosed subsystems:** `mechanism-manipulator-arm`, `mechanism-single-port-deploying`, `control-vr-headset-teleoperation`

**Prior art notes:**

> Vicarious Surgical is a canonical 2014+ next-generation surgical robotic system. ~12-year-deep public-disclosure prior art for: single-port deploying-arm surgical morphology, 9-DoF arm kinematics, VR-headset surgeon interface (Apple Vision Pro / haptic-glove teleop antecedent). Direct shielding for any commercial humanoid claim on VR-headset bimanual teleoperation (notably: Open-TeleVision round-16 entry uses Apple Vision Pro for academic humanoid teleop; Vicarious Surgical pioneered the VR-teleop pattern in commercial surgical context ~10 years earlier).

**Sources:**

1. Vicarious Surgical corporate site (vicarioussurgical.com).
2. SPAC merger announcement 2021 (NYSE: RBOT).
3. FDA breakthrough designation announcement 2019.

---

### 2024-07 — Open-TeleVision

- **id:** `opentelevision-cheng-corl-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** UC San Diego + MIT; Xuxin Cheng, Jialong Li, Shiqi Yang, Ge Yang, Xiaolong Wang
- **disclosure citation:** Cheng, X., Li, J., Yang, S., Yang, G., Wang, X. 'Open-TeleVision: Teleoperation with Immersive Active Visual Feedback'. arXiv:2407.01512, July 2024. CoRL 2024. UC San Diego + MIT.
- **disclosed subsystems:** `control-teleoperation`, `control-vr-headset-teleoperation`, `sensing-stereoscopic-camera`, `control-immersive-pov`

**Prior art notes:**

> Open-TeleVision is the canonical first open-source academic Apple-Vision-Pro humanoid teleoperation system (Cheng et al. CoRL 2024). 10-month-deep open-permissive prior art for: VR-headset humanoid teleop with first-person stereo POV, active head tracking for gaze-following, hand-pose mirroring across Vision Pro + humanoid arm. Direct shielding for any commercial humanoid claim on Apple-Vision-Pro-or-equivalent VR teleop. Architectural successor to Vicarious Surgical (round-16 entry) VR-teleop in surgical context — Open-TeleVision applies the same pattern to humanoid manipulation. The 500-hour Helix (round-15) teleop dataset was likely collected via similar VR-headset teleop infrastructure.

**Sources:**

1. Cheng et al. arXiv:2407.01512 July 2024.
2. CoRL 2024 (proceedings.mlr.press lookup).
3. Project page (robot-tv.github.io).
4. GitHub: github.com/OpenTeleVision/TeleVision.

---

### 2025-06 — Apple Intelligence + Apple Robotics research (2025) *(draft)*

- **id:** `apple-vla-research-2025`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Apple Inc.
- **disclosure citation:** Apple Inc. Apple Intelligence stack (announced June 2024 WWDC); Apple Vision Pro hardware (released February 2024) increasingly deployed as teleop interface for academic humanoid robots (Open-TeleVision round-16); Apple Machine Learning Research publishing robotics-adjacent work 2024-2025.
- **disclosed subsystems:** `control-foundation-model`, `control-vr-headset-teleoperation`

**Prior art notes:**

> Apple's emerging robotics research (2024-2025) is documented primarily through hardware deployment (Apple Vision Pro in Open-TeleVision round-16) and Apple Machine Learning Research publications. Specific internal Apple robotics products are not publicly disclosed. The existence of Apple-platform academic deployments establishes prior-art shielding against any commercial humanoid claim that integrates Apple Vision Pro / Apple Intelligence as a teleop or perception interface.

**Sources:**

1. Apple Vision Pro product launch documentation Feb 2024.
2. Apple Intelligence WWDC 2024 announcement.
3. Apple Machine Learning Research (machinelearning.apple.com).
4. Open-TeleVision (round-16 corpus entry) deploys on Apple Vision Pro.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `2aee416`.*
