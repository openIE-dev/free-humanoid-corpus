---
title: "mechanism-antagonistic-tendon"
parent: "Invalidity Contentions"
nav_order: 191
layout: default
---

# Invalidity Contention Packet — `mechanism-antagonistic-tendon`

**Generated:** 2026-05-14  
**Cross-cut tag:** `mechanism-antagonistic-tendon`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2024-06  
**Most recent disclosure:** 2025-10

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `mechanism-antagonistic-tendon`.

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

### 2025-10 — Educational SoftHand-A

- **id:** `educational-softhand-a-2025`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Bristol Robotics Laboratory + Bristol Grammar School; Jared Lepora (16-yr student), Haoran Li, Efi Psomopoulou, Nathan F. Lepora
- **disclosure citation:** Lepora, J., Li, H., Psomopoulou, E., Lepora, N. F. 'Educational SoftHand-A: Building an Anthropomorphic Hand with Soft Synergies using LEGO® MINDSTORMS®'. arXiv:2510.15638, October 2025. Bristol Robotics Laboratory + Bristol Grammar School.
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `mechanism-antagonistic-tendon`, `mechanism-differential-synergy`, `mechanism-soft-synergy`, `mechanism-educational-platform`

**Prior art notes:**

> Educational SoftHand-A is the LEGO MINDSTORMS instantiation of the Pisa-IIT SoftHand / Tactile SoftHand-A lineage (Oct 2025). 7-month-deep prior art for: differential clutch-gear synergy mechanism in LEGO bricks, agonist-antagonist tendon pair from a single dual-motor module, accessible educational reproduction of professional SoftHand-class designs. **Direct relevance for free-humanoid-platform hand v0.2** — the differential-synergy clutch-gear approach is documented open art that the v0.2 hand could adopt or explicitly diverge from. Together with pisa-iit-softhand, pisa-iit-softhand-2, and tactile-softhand-a-2025, the SoftHand synergy-mechanism lineage is now 11-year-deep continuous open academic publication (2014-2025) across four design generations.

**Sources:**

1. Lepora, Li, Psomopoulou, Lepora. arXiv:2510.15638 October 2025.
2. Project page (lepora.com/EduSoftHand-A).
3. Press: TechXplore, Interesting Engineering, Popular Science (October 2025).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `c61fc91`.*
