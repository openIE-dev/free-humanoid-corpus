---
title: "mechanism-telescoping-mast"
parent: "Invalidity Contentions"
nav_order: 85
layout: default
---

# Invalidity Contention Packet — `mechanism-telescoping-mast`

**Generated:** 2026-05-07  
**Cross-cut tag:** `mechanism-telescoping-mast`  
**Entries:** 2 (1 commons-grade, 1 draft)  
**Earliest disclosure:** 2020-07  
**Most recent disclosure:** 2024-09

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `mechanism-telescoping-mast`.

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

### 2020-07 — Hello Robot Stretch

- **id:** `hello-robot-stretch-2020`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Hello Robot, Inc.; Charles Kemp + Aaron Edsinger
- **disclosure citation:** Hello Robot, Inc. 'Stretch: A Versatile Mobile Manipulator'. Public reveal July 2020 via hello-robot.com. Founded by Charles Kemp (Georgia Tech Healthcare Robotics Lab spinout) and Aaron Edsinger. Subsequent product generations: Stretch RE1 (2020), RE2 (2021), Stretch 3 (2024). Used as the deployment platform in LEGS (round-15 entry legs-berkeley-2024) and many other academic mobile-manipulation projects.
- **disclosed subsystems:** `mechanism-mobile-base`, `mechanism-manipulator-arm`, `mechanism-telescoping-mast`, `actuator-electric`

**Prior art notes:**

> Hello Robot Stretch is the canonical sub-\$25k educational mobile manipulator (2020). 5-year-deep public-disclosure prior art with 100+ academic publications using Stretch as the deployment platform. Direct shielding for any commercial mobile-manipulator claim at the educational price point or with the telescoping-mast architectural pattern. Notably **the Berkeley LEGS round-15 entry deployed on Stretch** — the round-15 entry's prior_art_notes implicitly reference Stretch as the platform; round-17 now resolves that reference. Architecturally distinct from humanoid-form mobile manipulators (Apptronik, Figure, Optimus): Stretch is single-arm + mast + wheels, not bipedal + bimanual.

**Sources:**

1. Hello Robot corporate site (hello-robot.com).
2. Kemp, C., Edsinger, A. et al. 'Stretch: A Versatile Mobile Manipulator' company technical reports 2020+.
3. Wikipedia 'Hello Robot' (en.wikipedia.org/wiki/Hello_Robot).

---

### 2024-09 — Galbot *(draft)*

- **id:** `galbot-galaxy-robotics-2024`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Galaxy Robotics (Beijing, China)
- **disclosure citation:** Galaxy Robotics (Beijing, China). Galbot platform reveal 2024 via galaxy-robotics.com / WAIC 2024 demonstration. Wheeled humanoid with telescoping torso lift + dual 7-DoF arms. ~CNY 500k initial commercial price.
- **disclosed subsystems:** `mechanism-mobile-base`, `mechanism-anthropomorphic-arm`, `mechanism-telescoping-mast`, `actuator-electric`

**Prior art notes:**

> Galbot is the canonical 2024 Chinese wheeled-humanoid commercial platform (Galaxy Robotics). 1.5-year-deep public-disclosure prior art for: telescoping-torso wheeled humanoid commercial deployment, dual-arm wheeled mobile manipulator at the educational-to-commercial price tier. Architectural sibling of Hello Robot Stretch (round-17 entry) but with humanoid-form dual-arm + telescoping-torso vs. Stretch's single-arm + mast. Direct shielding for any commercial humanoid claim on wheeled-humanoid (non-bipedal) form factor with telescoping vertical adjustment. **Directly relevant to free-humanoid-wheeled** — Galbot is the closest commercial product to that morphology.

**Sources:**

1. Galaxy Robotics corporate site (galaxy-robotics.com).
2. WAIC 2024 demonstration coverage.
3. Humanoid Press product database.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `b51f194`.*
