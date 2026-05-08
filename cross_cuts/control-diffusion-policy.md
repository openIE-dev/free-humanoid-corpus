---
title: control-diffusion-policy
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-diffusion-policy`

**3 corpus entries disclose this subsystem.**

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

## RDT-1B (Robotics Diffusion Transformer) (2024-10)

- **id**: `rdt-1b-thu-2024`
- **corpus**: academic
- **creator**: Tsinghua TSAIL (THU-ML); Songming Liu et al.
- **disclosure**: Liu, S., et al. 'RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation'. arXiv:2410.07864, October 2024. ICLR 2025. Tsinghua TSAIL (THU-ML) lab.
- **ip status**: open-permissive
- **prior art notes**: RDT-1B is THU-ML's canonical diffusion-based VLA foundation model for bimanual manipulation (ICLR 2025). 7-month-deep open-permissive prior art for: diffusion-formulation VLA at billion-parameter scale, bimanual manipulation foundation policy, multi-robot pre-training corpus. The canonical Chinese-academy entry in the open-weight VLA race alongside Stanford OpenVLA and Physical Intelligence π₀. Directly cited as a comparison baseline in OpenVLA-OFT (round-12); now resolves correctly. Direct shielding for any commercial humanoid claim on diffusion-based bimanual VLA.
