---
title: control-cross-embodiment
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-cross-embodiment`

**4 corpus entries disclose this subsystem.**

Earliest disclosure: 2024-03

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## 3D Diffusion Policy (DP3) (2024-03)

- **id**: `dp3-ze-rss-2024`
- **corpus**: academic
- **creator**: Stanford + Tsinghua + CMU; Yanjie Ze, Hao Xu, et al.
- **disclosure**: Ze, Y., Zhang, G., Zhang, K., Hu, C., Wang, M., Xu, H. '3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations'. RSS 2024. arXiv:2403.03954. Stanford + Tsinghua + CMU.
- **ip status**: open-permissive
- **prior art notes**: 3D Diffusion Policy (Ze et al. RSS 2024) is the canonical 3D extension of Chi/Song's Diffusion Policy (corpus entry). 1-year-deep open-permissive prior art for: 3D-input diffusion-policy for manipulation, point-cloud-conditioned action generation. Direct shielding for any commercial humanoid claim on 3D-perception-conditioned manipulation policies. Together with Diffusion Policy, RDT-1B (diffusion VLA), and Octo (transformer + diffusion-head), establishes the diffusion-policy family that shields commercial diffusion-VLA claims.

## Octo (Open-Source Generalist Robot Policy) (2024-05)

- **id**: `octo-rss-2024`
- **corpus**: academic
- **creator**: Octo Model Team (UC Berkeley + Stanford + CMU + Google DeepMind); Levine + Finn + Sadigh group lineage
- **disclosure**: Octo Model Team: Ghosh, D., Walke, H., Pertsch, K., Black, K., Mees, O., Dasari, S., Hejna, J., Kreiman, T., Xu, C., Luo, J., Tan, Y. L., Sanketi, P., Vuong, Q., Xiao, T., Sadigh, D., Finn, C., Levine, S. 'Octo: An Open-Source Generalist Robot Policy'. arXiv:2405.12213, May 2024. Robotics: Science and Systems (RSS) 2024. UC Berkeley + Stanford + Carnegie Mellon + Google DeepMind.
- **ip status**: open-permissive
- **prior art notes**: Octo is the canonical first open-source generalist robot policy. 1-year-deep open-permissive academic prior art predating OpenVLA by ~1 month (RSS May 2024 vs OpenVLA arXiv June 2024). Establishes the architectural pattern for: transformer + diffusion-policy action head, Open-X-Embodiment-trained cross-embodiment policy at 27M-93M parameter scale, language-OR-goal-image conditioning. Direct shielding for any commercial humanoid VLA claim on diffusion-policy action heads (RDT-1B, π₀ both build on this) and on Open-X-Embodiment-trained cross-embodiment foundation. Together with OpenVLA, π₀, π₀.₅, OpenVLA-OFT, and RDT-1B, establishes the open academic VLA baseline against which Figure Helix, NVIDIA GR00T N1, Microsoft Magma, and any closed commercial VLA must be evaluated.

## OpenVLA (2024-06)

- **id**: `openvla-stanford-2024`
- **corpus**: academic
- **creator**: Stanford + Toyota Research Institute + UC Berkeley; Kim, Pertsch, Karamcheti, Liang, Finn, Levine, Tedrake et al.
- **disclosure**: Kim, M. J., Pertsch, K., Karamcheti, S., Xiao, T., Balakrishna, A., Nair, S., Rafailov, R., Foster, E., Lam, G., Sanketi, P., Vuong, Q., Kollar, T., Burchfiel, B., Tedrake, R., Sadigh, D., Levine, S., Liang, P., Finn, C. 'OpenVLA: An Open-Source Vision-Language-Action Model'. arXiv:2406.09246, June 2024. CoRL 2024 (PMLR v270, Kim25c). Stanford + Toyota Research Institute + UC Berkeley.
- **ip status**: open-permissive
- **prior art notes**: OpenVLA is the canonical first fully-open-source VLA foundation model (CoRL 2024). 23-month-deep open-permissive academic prior art for: 7B-class open-weight VLA, Llama-2-based VLA backbone, Open-X-Embodiment-trained cross-embodiment policy. Direct shielding for any commercial humanoid VLA claim on open-source-equivalent architectural elements. Together with π₀ and π₀.₅, establishes the open-academic VLA baseline against which all closed commercial VLAs (Tesla Optimus, Figure, 1X NEO) must be evaluated.

## NVIDIA Isaac GR00T N1 (2025-03)

- **id**: `nvidia-groot-n1-2025`
- **corpus**: academic
- **creator**: NVIDIA; multi-author research team
- **disclosure**: NVIDIA. 'GR00T N1: An Open Foundation Model for Generalist Humanoid Robots'. arXiv:2503.14734, March 2025. NVIDIA GTC 2025 announcement. Open commercial license; open weights via HuggingFace nvidia/GR00T-N1-2B. Successor versions N1.6 (full-body) and N1.7 (Cosmos-Reason2 + EgoScale 20K-hour egocentric pre-training) released subsequently.
- **ip status**: open-permissive
- **prior art notes**: NVIDIA GR00T N1 is the canonical first open commercial-licensed humanoid foundation model (GTC March 2025). 2-month-deep open prior art for: dual-system S1/S2 humanoid VLA, egocentric-human-video pre-training at scale, NVIDIA Isaac platform integration. Direct architectural sibling of Figure Helix (round-15 entry). Both adopt the dual-system pattern from cognitive science. The N1.7 EgoScale 20K-hour pre-training corpus is itself prior art for any commercial humanoid claim on egocentric-video-trained policy datasets. Direct shielding for any commercial humanoid VLA claim.
