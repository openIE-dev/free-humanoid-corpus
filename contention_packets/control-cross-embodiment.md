---
title: "control-cross-embodiment"
parent: "Invalidity Contentions"
nav_order: 49
layout: default
---

# Invalidity Contention Packet — `control-cross-embodiment`

**Generated:** 2026-05-10  
**Cross-cut tag:** `control-cross-embodiment`  
**Entries:** 6 (5 commons-grade, 1 draft)  
**Earliest disclosure:** 2023-10  
**Most recent disclosure:** 2025-03

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-cross-embodiment`.

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

### 2023-10 — RT-X / Open X-Embodiment collaboration paper

- **id:** `rt-x-collaboration-2023`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Open X-Embodiment Collaboration (21 institutions, 100+ co-authors)
- **disclosure citation:** Open X-Embodiment Collaboration et al. 'Open X-Embodiment: Robotic Learning Datasets and RT-X Models'. ICRA 2024. arXiv:2310.08864. Cross-institutional collaboration spanning 21 institutions (Google DeepMind, Stanford, UC Berkeley, MIT, CMU, Columbia, NYU, Toyota Research Institute, Imperial College, ETH Zürich, Tokyo Tech, et al.). The paper introducing the dataset now in the corpus as `open-x-embodiment`.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-cross-embodiment`, `control-foundation-model-policy`, `control-imitation-learning`

**Prior art notes:**

> RT-X / Open X-Embodiment collaboration (ICRA 2024) is the canonical 21-institution cross-embodiment VLA collaboration. 1.5-year-deep open-permissive prior art for: publicly-coordinated cross-institutional robot dataset pool, cross-embodiment VLA training methodology, RT-1-X / RT-2-X cross-embodiment models. Direct shielding for any commercial humanoid claim on cross-embodiment VLA training. **The collaboration model itself is novel art** — establishes that open multi-institution dataset pooling for robot learning is well-anticipated public-domain academic practice. Distinct from the dataset entry (`open-x-embodiment` already in corpus) by emphasis on the model-training + collaboration-pattern artifacts.

**Sources:**

1. Open X-Embodiment Collaboration arXiv:2310.08864 ICRA 2024.
2. Project page (robotics-transformer-x.github.io).
3. Open X-Embodiment dataset (robotics-transformer-x.github.io/data).

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

### 2025-03 — NVIDIA Isaac GR00T N1

- **id:** `nvidia-groot-n1-2025`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** NVIDIA; multi-author research team
- **disclosure citation:** NVIDIA. 'GR00T N1: An Open Foundation Model for Generalist Humanoid Robots'. arXiv:2503.14734, March 2025. NVIDIA GTC 2025 announcement. Open commercial license; open weights via HuggingFace nvidia/GR00T-N1-2B. Successor versions N1.6 (full-body) and N1.7 (Cosmos-Reason2 + EgoScale 20K-hour egocentric pre-training) released subsequently.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-foundation-model-policy`, `control-dual-system-architecture`, `control-egocentric-video-pretraining`, `control-cross-embodiment`

**Prior art notes:**

> NVIDIA GR00T N1 is the canonical first open commercial-licensed humanoid foundation model (GTC March 2025). 2-month-deep open prior art for: dual-system S1/S2 humanoid VLA, egocentric-human-video pre-training at scale, NVIDIA Isaac platform integration. Direct architectural sibling of Figure Helix (round-15 entry). Both adopt the dual-system pattern from cognitive science. The N1.7 EgoScale 20K-hour pre-training corpus is itself prior art for any commercial humanoid claim on egocentric-video-trained policy datasets. Direct shielding for any commercial humanoid VLA claim.

**Sources:**

1. arXiv:2503.14734 March 2025.
2. NVIDIA Newsroom announcement (nvidianews.nvidia.com/news/nvidia-isaac-gr00t-n1-open-humanoid-robot-foundation-model-simulation-frameworks).
3. HuggingFace: huggingface.co/nvidia/GR00T-N1-2B.
4. GitHub: github.com/NVIDIA/Isaac-GR00T (versions through N1.7).
5. N1.7 model card (huggingface.co/blog/nvidia/gr00t-n1-7).

---

### 2025-03 — Google DeepMind Gemini Robotics 1.5 *(draft)*

- **id:** `google-gemini-robotics-1-5-2025`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Google DeepMind
- **disclosure citation:** Google DeepMind. Gemini Robotics + Gemini Robotics-ER (Embodied Reasoning) reveal March 12 2025 via deepmind.google. Gemini Robotics 1.5 announced June 2025. The first VLA built atop Gemini 2.0 Flash foundation model.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-foundation-model-policy`, `control-cross-embodiment`

**Prior art notes:**

> Gemini Robotics 1.5 is Google DeepMind's canonical 2025 commercial VLA built atop Gemini 2.0 Flash. ~6-month-deep public-disclosure prior art at corpus-entry time. The successor to RT-1 (corpus) + RT-2 (corpus) in the Google DeepMind VLA lineage. Direct shielding for any commercial humanoid VLA claim on 'foundation-model-backbone-conditioned policy'.

**Sources:**

1. Google DeepMind announcement (deepmind.google/discover/blog/gemini-robotics-brings-ai-into-the-physical-world/).
2. DeepMind Gemini Robotics paper (when published).

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
