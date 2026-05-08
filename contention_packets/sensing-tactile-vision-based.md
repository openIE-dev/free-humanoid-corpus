---
title: "sensing-tactile-vision-based"
parent: "Invalidity Contentions"
nav_order: 155
layout: default
---

# Invalidity Contention Packet — `sensing-tactile-vision-based`

**Generated:** 2026-05-08  
**Cross-cut tag:** `sensing-tactile-vision-based`  
**Entries:** 5 (4 commons-grade, 1 draft)  
**Earliest disclosure:** 2017-04  
**Most recent disclosure:** 2024-11

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `sensing-tactile-vision-based`.

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

### 2020-05 — DIGIT (Meta tactile sensor)

- **id:** `meta-digit-tactile-2020`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Meta AI Research (formerly Facebook AI); Roberto Calandra group
- **disclosure citation:** Lambeta, M., Chou, P.-W., Tian, S., Yang, B., Maloon, B., Most, V. R., Stroud, D., Santos, R., Byagowi, A., Kammerer, G., Jayaraman, D., Calandra, R. 'DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation'. IEEE RA-L 5(3) 2020. arXiv:2005.14679. Facebook AI Research (now Meta AI).
- **disclosed subsystems:** `sensing-tactile-vision-based`, `sensing-fingertip-tactile`

**Prior art notes:**

> DIGIT is the canonical open-source academic vision-based tactile sensor (Lambeta + Calandra Meta AI, RA-L 2020). 5-year-deep open-permissive prior art for: compact vision-based tactile fingertip, open-hardware tactile-sensor design, image-based deformation tactile signal. Tesla Optimus Gen 3's 'tactile fingertip sensors' claim (round-15 entry, see prior_art_notes) faces this prior art directly. Direct shielding for any commercial humanoid claim on fingertip tactile sensing — DIGIT's open-hardware design has been widely replicated by academic groups, plus its commercial cousin GelSight (corpus entry `gelsight`) covers the broader vision-based-tactile chain.

**Sources:**

1. Lambeta et al. IEEE RA-L 5(3) 2020; arXiv:2005.14679.
2. Project page (digit.ml).
3. GitHub: github.com/facebookresearch/digit-design.
4. Meta AI / FAIR DIGIT documentation (meta.ai/research).

---

### 2022-05 — GelSight Mini

- **id:** `gelsight-mini-2022`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** GelSight Inc. (MIT spinout from Adelson Perceptual Science Group)
- **disclosure citation:** GelSight, Inc. (Waltham, MA; founded 2011 as MIT spinout from Edward Adelson's Perceptual Science Group). GelSight Mini commercial product reveal 2022. gelsight.com. The compact 30 mm × 30 mm × 25 mm version of the original GelSight (Johnson + Adelson 2009).
- **disclosed subsystems:** `sensing-tactile-vision-based`, `sensing-fingertip-tactile`

**Prior art notes:**

> GelSight Mini is the canonical compact commercial vision-based tactile sensor (2022+). 3-year-deep public-disclosure prior art with descent from the foundational Johnson-Adelson 2009 academic GelSight paper (corpus entry `gelsight`). **Commercialization complement to the open-hardware DIGIT (round-16) and academic TacTip (round-18)** — three vision-based-tactile architectures from three different labs (MIT/Adelson, Meta/Calandra, Bristol/Lepora). Tesla Optimus Gen 3's 'tactile fingertip sensors' claim (round-15) faces all four (GelSight + DIGIT + TacTip + ReSkin) as modality-distinct prior-art chains.

**Sources:**

1. GelSight Inc. corporate site (gelsight.com).
2. GelSight Mini product page (gelsight.com/gelsight-mini).

---

### 2024-06 — Tactile SoftHand-A

- **id:** `tactile-softhand-a-2025`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Bristol Robotics Laboratory (Lepora group) + Pisa-IIT (Bianchi, Catalano)
- **disclosure citation:** Li, H., Ford, C. J., Lu, C., Lin, Y., Bianchi, M., Catalano, M. G., Psomopoulou, E., Lepora, N. F. 'Tactile SoftHand-A: 3D-Printed, Tactile, Highly-underactuated, Anthropomorphic Robot Hand with an Antagonistic Tendon Mechanism'. arXiv:2406.12731, June 2024. International Journal of Robotics Research, October 2025. Bristol Robotics Laboratory + Pisa-IIT collaboration.
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `mechanism-antagonistic-tendon`, `mechanism-3d-printed-hand`, `sensing-tactile-vision-based`, `sensing-fingertip-tactile`

**Prior art notes:**

> Tactile SoftHand-A is the 2024-2025 direct successor to the Pisa-IIT SoftHand 2 (round-8 entry pisa-iit-softhand-2). Adds antagonistic tendon mechanism (active open + active close), integrated vision-based tactile sensing, and full 3D-printed fabrication. IJRR October 2025. Direct shielding for free-humanoid-platform's hand v0.1 commitments — Tactile SoftHand-A has antagonistic-tendon prior art that the v0.1 hand's passive-return spring approach explicitly is the alternative to. Together with shadow-dexterous-hand, pisa-iit-softhand, dlr-hand-arm-system-2011, and pisa-iit-softhand-2, establishes deep open-academic prior art for anthropomorphic underactuated tendon-driven hand robotics. **Particularly relevant for hand v0.2 design decisions** — the antagonistic-tendon path is well-anticipated open art.

**Sources:**

1. Li et al. arXiv:2406.12731 June 2024.
2. Li et al. International Journal of Robotics Research October 2025 (DOI: 10.1177/02783649251379516).
3. GitHub: github.com/HaoranLi-Data/Tactile_SoftHand_A.
4. Lepora group publications (lepora.com/papers/).

---

### 2024-11 — DIGIT 360 (Meta) *(draft)*

- **id:** `meta-digit-360-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Meta AI Research / Reality Labs; Calandra group successor team
- **disclosure citation:** Meta AI / Meta Reality Labs. DIGIT 360 reveal November 2024 via ai.meta.com / digit.ml. Successor to DIGIT (Lambeta + Calandra RA-L 2020, corpus entry `meta-digit-tactile-2020`). Adds omnidirectional 360° finger-shaped tactile sensing surface.
- **disclosed subsystems:** `sensing-tactile-vision-based`, `sensing-fingertip-tactile`, `sensing-omnidirectional-tactile`

**Prior art notes:**

> DIGIT 360 (Meta, November 2024) is the canonical first omnidirectional vision-based tactile finger. ~6-month-deep open-permissive prior art for: 360° tactile sensing in anthropomorphic finger form factor, multi-camera (18-cam) internal imaging architecture. Direct successor to DIGIT (round-16) closing the flat-surface limitation. Direct shielding for any commercial humanoid claim on omnidirectional fingertip tactile sensing — particularly relevant for Tesla Optimus Gen 3 and Figure Helix tactile-claim shielding.

**Sources:**

1. Meta AI Research blog (ai.meta.com/blog/digit-360).
2. Project page (digit.ml/digit360).
3. GitHub: github.com/facebookresearch/digit360.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `35dc1dd`.*
