---
title: "control-diffusion-policy"
parent: "Invalidity Contentions"
nav_order: 53
layout: default
---

# Invalidity Contention Packet — `control-diffusion-policy`

**Generated:** 2026-05-10  
**Cross-cut tag:** `control-diffusion-policy`  
**Entries:** 4 (4 commons-grade, 0 draft)  
**Earliest disclosure:** 2020-06  
**Most recent disclosure:** 2024-10

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-diffusion-policy`.

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

### 2020-06 — Denoising Diffusion Probabilistic Models (DDPM)

- **id:** `ddpm-ho-neurips-2020`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** UC Berkeley; Jonathan Ho, Ajay Jain, Pieter Abbeel; antecedent: Stanford Sohl-Dickstein 2015
- **disclosure citation:** Ho, J., Jain, A., Abbeel, P. 'Denoising Diffusion Probabilistic Models'. NeurIPS 2020. arXiv:2006.11239. UC Berkeley. The antecedent: Sohl-Dickstein, J., Weiss, E., Maheswaranathan, N., Ganguli, S. 'Deep Unsupervised Learning using Nonequilibrium Thermodynamics'. ICML 2015 (the original diffusion model paper).
- **disclosed subsystems:** `control-foundation-model`, `control-diffusion-policy`, `control-generative-model`

**Prior art notes:**

> DDPM (Ho et al. NeurIPS 2020) is the foundational modern diffusion-models paper. 5-year-deep public-domain prior art. **Direct architectural ancestor of Diffusion Policy (corpus), DP3 (round-17), RDT-1B (round-13), π₀ (round-12)** — every diffusion-based VLA + manipulation policy. Direct shielding for any commercial humanoid claim on diffusion-based action generation. Closes a major foundational citation chain.

**Sources:**

1. Ho, Jain, Abbeel. arXiv:2006.11239 NeurIPS 2020.
2. Sohl-Dickstein et al. ICML 2015 (diffusion antecedent).

---

### 2024-03 — 3D Diffusion Policy (DP3)

- **id:** `dp3-ze-rss-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Stanford + Tsinghua + CMU; Yanjie Ze, Hao Xu, et al.
- **disclosure citation:** Ze, Y., Zhang, G., Zhang, K., Hu, C., Wang, M., Xu, H. '3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations'. RSS 2024. arXiv:2403.03954. Stanford + Tsinghua + CMU.
- **disclosed subsystems:** `control-imitation-learning`, `control-diffusion-policy`, `control-3d-perception`, `control-cross-embodiment`

**Prior art notes:**

> 3D Diffusion Policy (Ze et al. RSS 2024) is the canonical 3D extension of Chi/Song's Diffusion Policy (corpus entry). 1-year-deep open-permissive prior art for: 3D-input diffusion-policy for manipulation, point-cloud-conditioned action generation. Direct shielding for any commercial humanoid claim on 3D-perception-conditioned manipulation policies. Together with Diffusion Policy, RDT-1B (diffusion VLA), and Octo (transformer + diffusion-head), establishes the diffusion-policy family that shields commercial diffusion-VLA claims.

**Sources:**

1. Ze et al. arXiv:2403.03954 RSS 2024.
2. Project page (3d-diffusion-policy.github.io).
3. GitHub: github.com/YanjieZe/3D-Diffusion-Policy.

---

### 2024-05 — Octo (Open-Source Generalist Robot Policy)

- **id:** `octo-rss-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Octo Model Team (UC Berkeley + Stanford + CMU + Google DeepMind); Levine + Finn + Sadigh group lineage
- **disclosure citation:** Octo Model Team: Ghosh, D., Walke, H., Pertsch, K., Black, K., Mees, O., Dasari, S., Hejna, J., Kreiman, T., Xu, C., Luo, J., Tan, Y. L., Sanketi, P., Vuong, Q., Xiao, T., Sadigh, D., Finn, C., Levine, S. 'Octo: An Open-Source Generalist Robot Policy'. arXiv:2405.12213, May 2024. Robotics: Science and Systems (RSS) 2024. UC Berkeley + Stanford + Carnegie Mellon + Google DeepMind.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-foundation-model-policy`, `control-diffusion-policy`, `control-cross-embodiment`, `control-imitation-learning`

**Prior art notes:**

> Octo is the canonical first open-source generalist robot policy. 1-year-deep open-permissive academic prior art predating OpenVLA by ~1 month (RSS May 2024 vs OpenVLA arXiv June 2024). Establishes the architectural pattern for: transformer + diffusion-policy action head, Open-X-Embodiment-trained cross-embodiment policy at 27M-93M parameter scale, language-OR-goal-image conditioning. Direct shielding for any commercial humanoid VLA claim on diffusion-policy action heads (RDT-1B, π₀ both build on this) and on Open-X-Embodiment-trained cross-embodiment foundation. Together with OpenVLA, π₀, π₀.₅, OpenVLA-OFT, and RDT-1B, establishes the open academic VLA baseline against which Figure Helix, NVIDIA GR00T N1, Microsoft Magma, and any closed commercial VLA must be evaluated.

**Sources:**

1. Octo Model Team. arXiv:2405.12213 May 2024.
2. RSS 2024 proceedings (roboticsproceedings.org/rss20/p090.pdf).
3. Project page (octo-models.github.io).
4. GitHub: github.com/octo-models/octo.

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
