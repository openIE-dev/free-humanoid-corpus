---
title: sensing-tactile-vision-based
parent: Cross-cuts
layout: default
---

# Cross-cut: `sensing-tactile-vision-based`

**5 corpus entries disclose this subsystem.**

Earliest disclosure: 2017-04

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## TacTip (vision-based tactile sensor) (2017-04)

- **id**: `bristol-tactip-2017`
- **corpus**: academic
- **creator**: Bristol Robotics Laboratory; Nathan Lepora group
- **disclosure**: Ward-Cherrier, B., Pestell, N., Cramphorn, L., Winstone, B., Giannaccini, M. E., Rossiter, J., Lepora, N. F. 'The TacTip Family: Soft Optical Tactile Sensors with 3D-Printed Biomimetic Morphologies'. Soft Robotics 5(2) 2018; arXiv:1803.04922. Bristol Robotics Laboratory (Lepora group).
- **ip status**: open-permissive
- **prior art notes**: TacTip is the canonical academic vision-based tactile sensor with 3D-printed biomimetic skin (Lepora group Bristol, 2017+). 8-year-deep open-permissive prior art predating Meta DIGIT (round-16, 2020) by 3 years; predates GelSight commercialization by ~6 years. **The architectural ancestor of Tactile SoftHand-A (round-11, 2024) and Educational SoftHand-A (round-12, 2025)** — both Lepora-group successors integrating TacTip at fingertips. Direct shielding for any commercial humanoid claim on biomimetic-papillae tactile fingertips. Tesla Optimus Gen 3's 'tactile fingertip sensors' claim faces TacTip + DIGIT + GelSight + ReSkin as three modality-distinct prior-art chains.

## DIGIT (Meta tactile sensor) (2020-05)

- **id**: `meta-digit-tactile-2020`
- **corpus**: academic
- **creator**: Meta AI Research (formerly Facebook AI); Roberto Calandra group
- **disclosure**: Lambeta, M., Chou, P.-W., Tian, S., Yang, B., Maloon, B., Most, V. R., Stroud, D., Santos, R., Byagowi, A., Kammerer, G., Jayaraman, D., Calandra, R. 'DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation'. IEEE RA-L 5(3) 2020. arXiv:2005.14679. Facebook AI Research (now Meta AI).
- **ip status**: open-permissive
- **prior art notes**: DIGIT is the canonical open-source academic vision-based tactile sensor (Lambeta + Calandra Meta AI, RA-L 2020). 5-year-deep open-permissive prior art for: compact vision-based tactile fingertip, open-hardware tactile-sensor design, image-based deformation tactile signal. Tesla Optimus Gen 3's 'tactile fingertip sensors' claim (round-15 entry, see prior_art_notes) faces this prior art directly. Direct shielding for any commercial humanoid claim on fingertip tactile sensing — DIGIT's open-hardware design has been widely replicated by academic groups, plus its commercial cousin GelSight (corpus entry `gelsight`) covers the broader vision-based-tactile chain.

## GelSight Mini (2022-05)

- **id**: `gelsight-mini-2022`
- **corpus**: private
- **creator**: GelSight Inc. (MIT spinout from Adelson Perceptual Science Group)
- **disclosure**: GelSight, Inc. (Waltham, MA; founded 2011 as MIT spinout from Edward Adelson's Perceptual Science Group). GelSight Mini commercial product reveal 2022. gelsight.com. The compact 30 mm × 30 mm × 25 mm version of the original GelSight (Johnson + Adelson 2009).
- **ip status**: trade-secret
- **prior art notes**: GelSight Mini is the canonical compact commercial vision-based tactile sensor (2022+). 3-year-deep public-disclosure prior art with descent from the foundational Johnson-Adelson 2009 academic GelSight paper (corpus entry `gelsight`). **Commercialization complement to the open-hardware DIGIT (round-16) and academic TacTip (round-18)** — three vision-based-tactile architectures from three different labs (MIT/Adelson, Meta/Calandra, Bristol/Lepora). Tesla Optimus Gen 3's 'tactile fingertip sensors' claim (round-15) faces all four (GelSight + DIGIT + TacTip + ReSkin) as modality-distinct prior-art chains.

## Tactile SoftHand-A (2024-06)

- **id**: `tactile-softhand-a-2025`
- **corpus**: academic
- **creator**: Bristol Robotics Laboratory (Lepora group) + Pisa-IIT (Bianchi, Catalano)
- **disclosure**: Li, H., Ford, C. J., Lu, C., Lin, Y., Bianchi, M., Catalano, M. G., Psomopoulou, E., Lepora, N. F. 'Tactile SoftHand-A: 3D-Printed, Tactile, Highly-underactuated, Anthropomorphic Robot Hand with an Antagonistic Tendon Mechanism'. arXiv:2406.12731, June 2024. International Journal of Robotics Research, October 2025. Bristol Robotics Laboratory + Pisa-IIT collaboration.
- **ip status**: open-permissive
- **prior art notes**: Tactile SoftHand-A is the 2024-2025 direct successor to the Pisa-IIT SoftHand 2 (round-8 entry pisa-iit-softhand-2). Adds antagonistic tendon mechanism (active open + active close), integrated vision-based tactile sensing, and full 3D-printed fabrication. IJRR October 2025. Direct shielding for free-humanoid-platform's hand v0.1 commitments — Tactile SoftHand-A has antagonistic-tendon prior art that the v0.1 hand's passive-return spring approach explicitly is the alternative to. Together with shadow-dexterous-hand, pisa-iit-softhand, dlr-hand-arm-system-2011, and pisa-iit-softhand-2, establishes deep open-academic prior art for anthropomorphic underactuated tendon-driven hand robotics. **Particularly relevant for hand v0.2 design decisions** — the antagonistic-tendon path is well-anticipated open art.

## DIGIT 360 (Meta) (2024-11)

- **id**: `meta-digit-360-2024`
- **corpus**: academic
- **creator**: Meta AI Research / Reality Labs; Calandra group successor team
- **disclosure**: Meta AI / Meta Reality Labs. DIGIT 360 reveal November 2024 via ai.meta.com / digit.ml. Successor to DIGIT (Lambeta + Calandra RA-L 2020, corpus entry `meta-digit-tactile-2020`). Adds omnidirectional 360° finger-shaped tactile sensing surface.
- **ip status**: open-permissive
- **prior art notes**: DIGIT 360 (Meta, November 2024) is the canonical first omnidirectional vision-based tactile finger. ~6-month-deep open-permissive prior art for: 360° tactile sensing in anthropomorphic finger form factor, multi-camera (18-cam) internal imaging architecture. Direct successor to DIGIT (round-16) closing the flat-surface limitation. Direct shielding for any commercial humanoid claim on omnidirectional fingertip tactile sensing — particularly relevant for Tesla Optimus Gen 3 and Figure Helix tactile-claim shielding.
