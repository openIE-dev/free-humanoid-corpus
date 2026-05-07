---
title: "control-foundation-model-policy"
parent: "Invalidity Contentions"
nav_order: 21
layout: default
---

# Invalidity Contention Packet — `control-foundation-model-policy`

**Generated:** 2026-05-07  
**Cross-cut tag:** `control-foundation-model-policy`  
**Entries:** 5 (5 commons-grade, 0 draft)  
**Earliest disclosure:** 2024-06  
**Most recent disclosure:** 2025-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-foundation-model-policy`.

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

### 2024-06 — OpenVLA

- **id:** `openvla-stanford-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Stanford + Toyota Research Institute + UC Berkeley; Kim, Pertsch, Karamcheti, Liang, Finn, Levine, Tedrake et al.
- **disclosure citation:** Kim, M. J., Pertsch, K., Karamcheti, S., Xiao, T., Balakrishna, A., Nair, S., Rafailov, R., Foster, E., Lam, G., Sanketi, P., Vuong, Q., Kollar, T., Burchfiel, B., Tedrake, R., Sadigh, D., Levine, S., Liang, P., Finn, C. 'OpenVLA: An Open-Source Vision-Language-Action Model'. arXiv:2406.09246, June 2024. CoRL 2024 (PMLR v270, Kim25c). Stanford + Toyota Research Institute + UC Berkeley.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-foundation-model-policy`, `control-imitation-learning`, `control-cross-embodiment`

**Prior art notes:**

> OpenVLA is the canonical first fully-open-source VLA foundation model (CoRL 2024). 23-month-deep open-permissive academic prior art for: 7B-class open-weight VLA, Llama-2-based VLA backbone, Open-X-Embodiment-trained cross-embodiment policy. Direct shielding for any commercial humanoid VLA claim on open-source-equivalent architectural elements. Together with π₀ and π₀.₅, establishes the open-academic VLA baseline against which all closed commercial VLAs (Tesla Optimus, Figure, 1X NEO) must be evaluated.

**Sources:**

1. Kim et al. arXiv:2406.09246 June 2024.
2. CoRL 2024 PMLR v270 Kim25c (proceedings.mlr.press/v270/kim25c.html).
3. OpenVLA project page (openvla.github.io).
4. GitHub: github.com/openvla/openvla.

---

### 2024-10 — π₀ (Pi-Zero)

- **id:** `physical-intelligence-pi0-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Physical Intelligence; Black, Brown, Driess, Finn et al.
- **disclosure citation:** Black, K., Brown, N., Driess, D., Esmail, A., Equi, M., Finn, C., et al. 'π₀: A Vision-Language-Action Flow Model for General Robot Control'. arXiv:2410.24164, October 2024. Physical Intelligence (physicalintelligence.company).
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-flow-matching`, `control-foundation-model-policy`, `control-imitation-learning`

**Prior art notes:**

> π₀ is Physical Intelligence's canonical first VLA foundation policy (Oct 2024). 1.5-year-deep open-academic publication. Establishes architectural prior art for: flow-matching action distribution in VLA, cross-embodiment policy pretraining, single foundation model controlling multiple robot platforms. Direct successor lineage from RT-1 (2022), RT-2 (2023), OpenVLA (2024). Direct shielding for any commercial humanoid claim on VLA-based control (Tesla Optimus, Figure, 1X NEO, Apptronik all face this); particularly for any claim on flow-matching action heads or cross-embodiment pretraining.

**Sources:**

1. Black et al. arXiv:2410.24164 October 2024.
2. Physical Intelligence pi0 paper (physicalintelligence.company/download/pi0.pdf).
3. Physical Intelligence company page (physicalintelligence.company).

---

### 2024-10 — RDT-1B (Robotics Diffusion Transformer)

- **id:** `rdt-1b-thu-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Tsinghua TSAIL (THU-ML); Songming Liu et al.
- **disclosure citation:** Liu, S., et al. 'RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation'. arXiv:2410.07864, October 2024. ICLR 2025. Tsinghua TSAIL (THU-ML) lab.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-foundation-model-policy`, `control-diffusion-policy`, `control-imitation-learning`, `control-bimanual-manipulation`

**Prior art notes:**

> RDT-1B is THU-ML's canonical diffusion-based VLA foundation model for bimanual manipulation (ICLR 2025). 7-month-deep open-permissive prior art for: diffusion-formulation VLA at billion-parameter scale, bimanual manipulation foundation policy, multi-robot pre-training corpus. The canonical Chinese-academy entry in the open-weight VLA race alongside Stanford OpenVLA and Physical Intelligence π₀. Directly cited as a comparison baseline in OpenVLA-OFT (round-12); now resolves correctly. Direct shielding for any commercial humanoid claim on diffusion-based bimanual VLA.

**Sources:**

1. Liu et al. arXiv:2410.07864 October 2024.
2. Project page (rdt-robotics.github.io/rdt-robotics).
3. GitHub: github.com/thu-ml/RoboticsDiffusionTransformer.
4. HuggingFace: huggingface.co/robotics-diffusion-transformer/rdt-1b.

---

### 2025-02 — OpenVLA-OFT

- **id:** `openvla-oft-stanford-2025`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Stanford; Moo Jin Kim, Chelsea Finn, Percy Liang
- **disclosure citation:** Kim, M. J., Finn, C., Liang, P. 'Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success'. arXiv:2502.19645, February 2025. Stanford.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-foundation-model-policy`, `control-action-chunking`, `control-parallel-decoding`, `control-imitation-learning`

**Prior art notes:**

> OpenVLA-OFT is the canonical Optimized Fine-Tuning recipe for VLA models (Stanford, Feb 2025). 15-month-deep prior art on: parallel action decoding for VLA, action chunking + continuous action representation + L1 regression objective combination. Direct shielding for any commercial humanoid VLA fine-tuning claim, particularly any claim on 'fast inference at high success' for humanoid VLAs. Outperforms π₀ on bimanual ALOHA — the canonical academic benchmark for bimanual humanoid manipulation.

**Sources:**

1. Kim, Finn, Liang. arXiv:2502.19645 February 2025.
2. Project page (openvla-oft.github.io).
3. GitHub: github.com/moojink/openvla-oft.

---

### 2025-04 — π₀.₅ (Pi-0.5)

- **id:** `physical-intelligence-pi05-2025`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Physical Intelligence; Black et al.
- **disclosure citation:** Black, K., et al. 'π₀.₅: a Vision-Language-Action Model with Open-World Generalization'. arXiv:2504.16054, April 2025. CoRL 2025 (PMLR vol. 305 pp. 17-40, Black25a). Physical Intelligence.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-foundation-model-policy`, `control-co-training`, `control-loco-manipulation`, `control-semantic-subtask-prediction`

**Prior art notes:**

> π₀.₅ is Physical Intelligence's open-world VLA (CoRL 2025 oral). 1-year-deep prior art on: open-world (new-home) zero-shot mobile manipulation, co-training across multi-robot + web + semantic subtask data, long-horizon (10+ minute) household task autonomy. **The most direct prior art for any commercial humanoid claim on 'works in any home out-of-the-box'** — Tesla Optimus, Figure, 1X NEO, Apptronik all market this generalization claim and now face 1-year-deep open-academic anticipation. Lineage: RT-1 → RT-2 → OpenVLA → π₀ → π₀.₅.

**Sources:**

1. Black et al. arXiv:2504.16054 April 2025.
2. CoRL 2025 PMLR v305 Black25a (proceedings.mlr.press/v305/black25a.html).
3. Physical Intelligence pi0.5 paper (pi.website/download/pi05.pdf).
4. Knowledge Insulating VLA follow-up (physicalintelligence.company/download/pi05_KI.pdf).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `864caf4`.*
