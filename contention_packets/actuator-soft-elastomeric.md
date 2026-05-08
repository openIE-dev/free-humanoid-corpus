---
title: "actuator-soft-elastomeric"
parent: "Invalidity Contentions"
nav_order: 15
layout: default
---

# Invalidity Contention Packet — `actuator-soft-elastomeric`

**Generated:** 2026-05-08  
**Cross-cut tag:** `actuator-soft-elastomeric`  
**Entries:** 3 (3 commons-grade, 0 draft)  
**Earliest disclosure:** 2014-09  
**Most recent disclosure:** 2021-11

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `actuator-soft-elastomeric`.

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

### 2014-09 — Harvard Soft Robotics Toolkit

- **id:** `harvard-soft-robotics-toolkit-2017`
- **corpus:** academic
- **ip status:** open-copyleft
- **creator:** Harvard Biodesign Lab + Harvard Microrobotics Lab; Conor Walsh, Robert Wood, Dónal Holland et al.
- **disclosure citation:** Holland, D. P., Park, E. J., Polygerinos, P., Bennett, G. J., Walsh, C. J. 'The Soft Robotics Toolkit: Shared Resources for Research and Design'. Soft Robotics Vol. 1 No. 3 2014. Wood + Walsh groups, Harvard Biodesign Lab + Harvard Microrobotics Lab.
- **disclosed subsystems:** `actuator-soft-elastomeric`, `actuator-pneumatic`, `sensing-tactile`, `mechanism-soft-robotics`

**Prior art notes:**

> The Harvard Soft Robotics Toolkit is the canonical open-academic soft-robotics fabrication library (Holland et al. Soft Robotics 1(3) 2014; Wood + Walsh group lineage). 11-year-deep open prior art for: elastomeric soft actuators (PneuNets, fiber-reinforced bending), soft sensors, complete fabrication recipes. Direct shielding for any commercial humanoid claim on soft-actuator fabrication or soft-sensor design. Particularly relevant for any future free-humanoid-soft variant.

**Sources:**

1. Holland et al. Soft Robotics 1(3) 2014.
2. Soft Robotics Toolkit site (softroboticstoolkit.com).
3. Wood + Walsh group publications (biodesign.seas.harvard.edu).

---

### 2017-04 — TacTip (vision-based tactile sensor)

- **id:** `bristol-tactip-2017`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Bristol Robotics Laboratory; Nathan Lepora group
- **disclosure citation:** Ward-Cherrier, B., Pestell, N., Cramphorn, L., Winstone, B., Giannaccini, M. E., Rossiter, J., Lepora, N. F. 'The TacTip Family: Soft Optical Tactile Sensors with 3D-Printed Biomimetic Morphologies'. Soft Robotics 5(2) 2018; arXiv:1803.04922. Bristol Robotics Laboratory (Lepora group).
- **disclosed subsystems:** `sensing-tactile-vision-based`, `sensing-fingertip-tactile`, `actuator-soft-elastomeric`

**Prior art notes:**

> TacTip is the canonical academic vision-based tactile sensor with 3D-printed biomimetic skin (Lepora group Bristol, 2017+). 8-year-deep open-permissive prior art predating Meta DIGIT (round-16, 2020) by 3 years; predates GelSight commercialization by ~6 years. **The architectural ancestor of Tactile SoftHand-A (round-11, 2024) and Educational SoftHand-A (round-12, 2025)** — both Lepora-group successors integrating TacTip at fingertips. Direct shielding for any commercial humanoid claim on biomimetic-papillae tactile fingertips. Tesla Optimus Gen 3's 'tactile fingertip sensors' claim faces TacTip + DIGIT + GelSight + ReSkin as three modality-distinct prior-art chains.

**Sources:**

1. Ward-Cherrier et al. Soft Robotics 5(2) 2018; arXiv:1803.04922.
2. Lepora group publications (lepora.com).
3. TacTip GitHub + open-hardware build instructions.

---

### 2021-11 — ReSkin (magnetic tactile skin)

- **id:** `cmu-reskin-tactile-2021`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Carnegie Mellon University + Meta AI Research; Bhirangi, Hellebrekers, Majidi, Gupta
- **disclosure citation:** Bhirangi, R., Hellebrekers, T., Majidi, C., Gupta, A. 'ReSkin: versatile, replaceable, lasting tactile skins'. CoRL 2021. arXiv:2111.00071, November 2021. Carnegie Mellon University + Meta AI Research.
- **disclosed subsystems:** `sensing-tactile-magnetic`, `sensing-tactile-skin`, `actuator-soft-elastomeric`

**Prior art notes:**

> ReSkin is the canonical magnetic-based tactile-skin academic anchor (Bhirangi et al. CoRL 2021). 4-year-deep open-permissive prior art for: magnetic-particle-embedded elastomeric tactile skin, replaceable-skin (peel-and-replace) tactile-sensor architecture, low-cost (<$10/skin) tactile-sensor designs. Distinct from DIGIT/GelSight (vision-based) by sensing modality — complementary prior art. Direct shielding for any commercial humanoid claim on magnetic-based tactile skin or replaceable-tactile-skin architecture.

**Sources:**

1. Bhirangi et al. CoRL 2021; arXiv:2111.00071.
2. Project page (reskin.dev).
3. GitHub: github.com/raunaqbhirangi/reskin_sensor.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `bb592c0`.*
