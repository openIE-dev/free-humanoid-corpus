---
title: sensing-fingertip-tactile
parent: Cross-cuts
layout: default
---

# Cross-cut: `sensing-fingertip-tactile`

**3 corpus entries disclose this subsystem.**

Earliest disclosure: 2020-05

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## DIGIT (Meta tactile sensor) (2020-05)

- **id**: `meta-digit-tactile-2020`
- **corpus**: academic
- **creator**: Meta AI Research (formerly Facebook AI); Roberto Calandra group
- **disclosure**: Lambeta, M., Chou, P.-W., Tian, S., Yang, B., Maloon, B., Most, V. R., Stroud, D., Santos, R., Byagowi, A., Kammerer, G., Jayaraman, D., Calandra, R. 'DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation'. IEEE RA-L 5(3) 2020. arXiv:2005.14679. Facebook AI Research (now Meta AI).
- **ip status**: open-permissive
- **prior art notes**: DIGIT is the canonical open-source academic vision-based tactile sensor (Lambeta + Calandra Meta AI, RA-L 2020). 5-year-deep open-permissive prior art for: compact vision-based tactile fingertip, open-hardware tactile-sensor design, image-based deformation tactile signal. Tesla Optimus Gen 3's 'tactile fingertip sensors' claim (round-15 entry, see prior_art_notes) faces this prior art directly. Direct shielding for any commercial humanoid claim on fingertip tactile sensing — DIGIT's open-hardware design has been widely replicated by academic groups, plus its commercial cousin GelSight (corpus entry `gelsight`) covers the broader vision-based-tactile chain.

## Tactile SoftHand-A (2024-06)

- **id**: `tactile-softhand-a-2025`
- **corpus**: academic
- **creator**: Bristol Robotics Laboratory (Lepora group) + Pisa-IIT (Bianchi, Catalano)
- **disclosure**: Li, H., Ford, C. J., Lu, C., Lin, Y., Bianchi, M., Catalano, M. G., Psomopoulou, E., Lepora, N. F. 'Tactile SoftHand-A: 3D-Printed, Tactile, Highly-underactuated, Anthropomorphic Robot Hand with an Antagonistic Tendon Mechanism'. arXiv:2406.12731, June 2024. International Journal of Robotics Research, October 2025. Bristol Robotics Laboratory + Pisa-IIT collaboration.
- **ip status**: open-permissive
- **prior art notes**: Tactile SoftHand-A is the 2024-2025 direct successor to the Pisa-IIT SoftHand 2 (round-8 entry pisa-iit-softhand-2). Adds antagonistic tendon mechanism (active open + active close), integrated vision-based tactile sensing, and full 3D-printed fabrication. IJRR October 2025. Direct shielding for free-humanoid-platform's hand v0.1 commitments — Tactile SoftHand-A has antagonistic-tendon prior art that the v0.1 hand's passive-return spring approach explicitly is the alternative to. Together with shadow-dexterous-hand, pisa-iit-softhand, dlr-hand-arm-system-2011, and pisa-iit-softhand-2, establishes deep open-academic prior art for anthropomorphic underactuated tendon-driven hand robotics. **Particularly relevant for hand v0.2 design decisions** — the antagonistic-tendon path is well-anticipated open art.

## Tesla Optimus Gen 3 (2025-10)

- **id**: `tesla-optimus-gen3-2025`
- **corpus**: private
- **creator**: Tesla, Inc.
- **disclosure**: Tesla, Inc. Optimus Gen 3 product disclosures via Tesla AI Day-class demonstrations + product page (tesla.com/we-robot) + Optimus blog/social-media posts October 2025+. Trade-secret commercial humanoid platform.
- **ip status**: trade-secret
- **prior art notes**: Tesla Optimus Gen 3 is the dominant commercial humanoid product claim surface. Public-disclosure surface (Tesla product page + demos + social-media + investor decks) discloses dimensional specs and high-level architecture; withholds actuator architecture, specific neural-network policies, training-data composition, and on-device inference details. **The 22-DoF hand × 50-actuator claim is the most specific architectural claim** and directly engages prior-art chains in the corpus: Shadow Hand (24-DoF), DLR Hand-II (15-DoF), Pisa-IIT SoftHand (synergy reduction), Tactile SoftHand-A (antagonistic tendons + tactile fingertips, round-11 entry — directly anticipates the tactile-fingertip delicate-manipulation claim), Educational SoftHand-A (round-12 entry — clutch-gear synergy mechanism). Modern claims on tactile-fingertip dexterous manipulation face 2-year-deep tactile-softhand-a prior art and the deeper SoftHand chain back to 2014. Vision-only sensing is shielded by Tesla's own FSD patents (which Tesla cannot use offensively against an own-lineage humanoid claim) but separately by Levine's GPS PR2/BRETT (2016) for vision-driven manipulation. The full Optimus Gen 3 claim surface is therefore element-by-element anticipated by deep open academic chains plus prior commercial humanoids in the corpus.
