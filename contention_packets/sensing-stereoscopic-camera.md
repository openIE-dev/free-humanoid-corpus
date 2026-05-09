---
title: "sensing-stereoscopic-camera"
parent: "Invalidity Contentions"
nav_order: 224
layout: default
---

# Invalidity Contention Packet — `sensing-stereoscopic-camera`

**Generated:** 2026-05-09  
**Cross-cut tag:** `sensing-stereoscopic-camera`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2000-07  
**Most recent disclosure:** 2024-07

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `sensing-stereoscopic-camera`.

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

### 2000-07 — Intuitive Surgical da Vinci

- **id:** `intuitive-surgical-da-vinci-2000`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Intuitive Surgical, Inc.; SRI International + Stanford JPL Salisbury lineage roots
- **disclosure citation:** Intuitive Surgical, Inc. (Sunnyvale, CA). da Vinci Surgical System FDA approval July 11, 2000. SRI International / Stanford telesurgical lineage; Salisbury Stanford-JPL hand era roots. Subsequent product generations: da Vinci S (2006), Si (2009), Xi (2014), X (2017), SP single-port (2018), Ion bronchoscopy (2019), da Vinci 5 (2024).
- **disclosed subsystems:** `mechanism-manipulator-arm`, `mechanism-tendon-driven`, `mechanism-wristed-instrument`, `control-master-slave-teleoperation`, `control-tremor-filtering`, `sensing-stereoscopic-camera`

**Prior art notes:**

> The Intuitive Surgical da Vinci system is the canonical commercial surgical-robot platform (FDA approval July 2000). 25-year-deep public-disclosure prior art for: master-slave teleoperated manipulator + console architecture, EndoWrist tendon-driven wristed-instrument design (architecturally descended from Salisbury's Stanford-JPL hand 1982 — corpus entry `salisbury-stanford-jpl-hand-1982`), tremor filtering + motion scaling for telerobotic precision. Direct shielding for any commercial humanoid claim on bimanual fine-manipulation with wristed end-effectors and tremor-filtered teleoperation. The 25-year commercial deployment + 7,500+ systems + 10M+ procedures establishes a deeply-anticipated prior-art cushion for any humanoid manipulation claim.

**Sources:**

1. Intuitive Surgical corporate site (intuitive.com).
2. FDA premarket approval (PMA) database, da Vinci System (P000004).
3. Wikipedia 'Da Vinci Surgical System'.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `2b483e9`.*
