---
title: "control-feature-matching"
parent: "Invalidity Contentions"
nav_order: 59
layout: default
---

# Invalidity Contention Packet — `control-feature-matching`

**Generated:** 2026-05-10  
**Cross-cut tag:** `control-feature-matching`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2024-05  
**Most recent disclosure:** 2024-06

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-feature-matching`.

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

### 2024-05 — RoMa (Robust Dense Feature Matching)

- **id:** `roma-edstedt-cvpr-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Linköping University; Johan Edstedt, Qiyu Sun, Georg Bökman, Mårten Wadenbäck, Michael Felsberg
- **disclosure citation:** Edstedt, J., Sun, Q., Bökman, G., Wadenbäck, M., Felsberg, M. 'RoMa: Robust Dense Feature Matching'. CVPR 2024. arXiv:2305.15404. Linköping University.
- **disclosed subsystems:** `control-foundation-model-perception`, `control-feature-matching`

**Prior art notes:**

> RoMa (Edstedt et al. CVPR 2024) is the canonical state-of-the-art dense feature matching method. 1-year-deep open-permissive prior art. Used in 3D-vision pipelines including the MASt3R lineage.

**Sources:**

1. Edstedt et al. arXiv:2305.15404 CVPR 2024.

---

### 2024-06 — MASt3R (Matching And Stereo 3D Reconstruction)

- **id:** `mast3r-naver-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** NAVER LABS Europe; Vincent Leroy, Yohann Cabon, Jerome Revaud
- **disclosure citation:** Leroy, V., Cabon, Y., Revaud, J. 'Grounding Image Matching in 3D with MASt3R'. ECCV 2024. arXiv:2406.09756. NAVER LABS Europe.
- **disclosed subsystems:** `control-foundation-model-perception`, `control-3d-reconstruction`, `control-feature-matching`, `control-visual-localization`

**Prior art notes:**

> MASt3R (Leroy et al. ECCV 2024) is DUSt3R's direct successor adding image-matching. 1-year-deep open-permissive prior art. Together with DUSt3R (round-28), MegaSaM (round-13), ViPE (round-11), RADIO-ViPE (round-10), establishes the calibration-free reconstruction chain that any commercial humanoid camera-perception claim must contend with.

**Sources:**

1. Leroy et al. arXiv:2406.09756 ECCV 2024.
2. GitHub: github.com/naver/mast3r.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `7ee2634`.*
