---
title: "sensing-fingertip-tactile"
parent: "Invalidity Contentions"
nav_order: 85
layout: default
---

# Invalidity Contention Packet — `sensing-fingertip-tactile`

**Generated:** 2026-05-07  
**Cross-cut tag:** `sensing-fingertip-tactile`  
**Entries:** 2 (1 commons-grade, 1 draft)  
**Earliest disclosure:** 2024-06  
**Most recent disclosure:** 2025-10

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `sensing-fingertip-tactile`.

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

### 2025-10 — Tesla Optimus Gen 3 *(draft)*

- **id:** `tesla-optimus-gen3-2025`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Tesla, Inc.
- **disclosure citation:** Tesla, Inc. Optimus Gen 3 product disclosures via Tesla AI Day-class demonstrations + product page (tesla.com/we-robot) + Optimus blog/social-media posts October 2025+. Trade-secret commercial humanoid platform.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `mechanism-tendon-driven`, `actuator-electric`, `control-vision-only-perception`, `control-foundation-model-policy`, `sensing-fingertip-tactile`

**Prior art notes:**

> Tesla Optimus Gen 3 is the dominant commercial humanoid product claim surface. Public-disclosure surface (Tesla product page + demos + social-media + investor decks) discloses dimensional specs and high-level architecture; withholds actuator architecture, specific neural-network policies, training-data composition, and on-device inference details. **The 22-DoF hand × 50-actuator claim is the most specific architectural claim** and directly engages prior-art chains in the corpus: Shadow Hand (24-DoF), DLR Hand-II (15-DoF), Pisa-IIT SoftHand (synergy reduction), Tactile SoftHand-A (antagonistic tendons + tactile fingertips, round-11 entry — directly anticipates the tactile-fingertip delicate-manipulation claim), Educational SoftHand-A (round-12 entry — clutch-gear synergy mechanism). Modern claims on tactile-fingertip dexterous manipulation face 2-year-deep tactile-softhand-a prior art and the deeper SoftHand chain back to 2014. Vision-only sensing is shielded by Tesla's own FSD patents (which Tesla cannot use offensively against an own-lineage humanoid claim) but separately by Levine's GPS PR2/BRETT (2016) for vision-driven manipulation. The full Optimus Gen 3 claim surface is therefore element-by-element anticipated by deep open academic chains plus prior commercial humanoids in the corpus.

**Sources:**

1. Tesla Optimus product page (tesla.com/we-robot).
2. Humanoid Press 'Optimus 3' database entry (humanoid.press/database/humanoid-press-database-tesla-optimus-3/).
3. Basenor explainer 'Tesla Optimus Gen 3 Hands: 22-DoF, 50 Actuators Explained'.
4. AI Robots Media coverage (airobots.media/technology/tesla-optimus-gen-3-everything-we-know-about-teslas-most-ambitious-product/).
5. Wikipedia 'Optimus (robot)' (en.wikipedia.org/wiki/Optimus_(robot)).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `171053a`.*
