---
title: "control-motion-capture-imitation"
parent: "Invalidity Contentions"
nav_order: 43
layout: default
---

# Invalidity Contention Packet — `control-motion-capture-imitation`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-motion-capture-imitation`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2018-04  
**Most recent disclosure:** 2021-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-motion-capture-imitation`.

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

### 2018-04 — DeepMimic

- **id:** `deepmimic-peng-siggraph-2018`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** UC Berkeley + UBC; Xue Bin (Jason) Peng, Pieter Abbeel, Sergey Levine, Michiel van de Panne
- **disclosure citation:** Peng, X. B., Abbeel, P., Levine, S., van de Panne, M. 'DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills'. ACM Transactions on Graphics 37(4) 2018 (SIGGRAPH 2018). arXiv:1804.02717. UC Berkeley + UBC.
- **disclosed subsystems:** `control-rl-policy`, `control-imitation-learning`, `control-motion-capture-imitation`, `control-physics-based-animation`

**Prior art notes:**

> DeepMimic (Peng et al. SIGGRAPH 2018) is the canonical foundational motion-capture-imitation deep-RL framework. 7-year-deep open-permissive prior art for: deep-RL imitation of motion-capture references, physics-based character animation via RL, complex acrobatic skill (backflip, spin) RL training. **The architectural ancestor of**: Adversarial Motion Priors (round-21 entry below), ASE (Peng et al. 2022), the entire humanoid-from-mocap-data line. Direct shielding for any commercial humanoid claim on motion-capture-trained policies (Tesla Optimus, Figure Helix demos all use mocap-style imitation; this is 7-year-deep prior art).

**Sources:**

1. Peng, X. B. et al. ACM TOG 37(4) 2018; arXiv:1804.02717.
2. Project page (xbpeng.github.io/projects/DeepMimic).
3. BAIR open-source release (github.com/xbpeng/DeepMimic).

---

### 2021-04 — Adversarial Motion Priors (AMP)

- **id:** `amp-peng-siggraph-2021`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** UC Berkeley; Xue Bin (Jason) Peng, Ze Ma, Pieter Abbeel, Sergey Levine, Angjoo Kanazawa
- **disclosure citation:** Peng, X. B., Ma, Z., Abbeel, P., Levine, S., Kanazawa, A. 'AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control'. ACM Transactions on Graphics 40(4) 2021 (SIGGRAPH 2021). arXiv:2104.02180. UC Berkeley.
- **disclosed subsystems:** `control-rl-policy`, `control-imitation-learning`, `control-motion-capture-imitation`, `control-adversarial-style-distillation`

**Prior art notes:**

> Adversarial Motion Priors (Peng et al. SIGGRAPH 2021) is the canonical extension of DeepMimic to GAN-style latent-space motion imitation. 4-year-deep open-permissive prior art for: GAN-distilled motion priors, latent-space mocap style imitation, task-conditioned style-aware humanoid RL. **The architectural ancestor of contemporary humanoid-from-mocap RL** including ASE (Peng et al. 2022), HumanPlus (Stanford 2024), ExBody (Stanford 2024), H1 / G1 humanoid policies (Unitree). Direct shielding for any commercial humanoid claim on 'humanoid moves like a human' style-aware locomotion.

**Sources:**

1. Peng, X. B. et al. ACM TOG 40(4) 2021; arXiv:2104.02180.
2. Project page (xbpeng.github.io/projects/AMP).
3. GitHub: github.com/xbpeng/DeepMimic (AMP integrated).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `bf892af`.*
