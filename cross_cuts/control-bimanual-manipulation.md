---
title: control-bimanual-manipulation
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-bimanual-manipulation`

**2 corpus entries disclose this subsystem.**

Earliest disclosure: 2024-10

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## RDT-1B (Robotics Diffusion Transformer) (2024-10)

- **id**: `rdt-1b-thu-2024`
- **corpus**: academic
- **creator**: Tsinghua TSAIL (THU-ML); Songming Liu et al.
- **disclosure**: Liu, S., et al. 'RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation'. arXiv:2410.07864, October 2024. ICLR 2025. Tsinghua TSAIL (THU-ML) lab.
- **ip status**: open-permissive
- **prior art notes**: RDT-1B is THU-ML's canonical diffusion-based VLA foundation model for bimanual manipulation (ICLR 2025). 7-month-deep open-permissive prior art for: diffusion-formulation VLA at billion-parameter scale, bimanual manipulation foundation policy, multi-robot pre-training corpus. The canonical Chinese-academy entry in the open-weight VLA race alongside Stanford OpenVLA and Physical Intelligence π₀. Directly cited as a comparison baseline in OpenVLA-OFT (round-12); now resolves correctly. Direct shielding for any commercial humanoid claim on diffusion-based bimanual VLA.

## Figure Helix (2025-02)

- **id**: `figure-helix-2025`
- **corpus**: private
- **creator**: Figure AI Inc.
- **disclosure**: Figure AI Inc. 'Helix: A Vision-Language-Action Model for Generalist Humanoid Control'. Public reveal February 2025 via figure.ai/news/helix. Subsequent disclosures: 'Helix Accelerating Real-World Logistics' (figure.ai/news/helix-logistics) and Hacker News + Robot Report coverage. No academic publication; trade-secret commercial VLA.
- **ip status**: trade-secret
- **prior art notes**: Helix is Figure AI's canonical 2025 commercial humanoid VLA. Public-disclosure surface (corporate blog + demo videos + Hacker News + Robot Report coverage) reveals architecture (S1/S2 dual-system, 35-DoF/200Hz, ~500hr teleop training) but withholds neural-network specifics, training-data composition, fine-tuning recipe, and policy-evaluation metrics. The capability set claimed is fully covered by deep open academic prior art chains: (1) S1/S2 dual-system architecture is shared with NVIDIA GR00T N1 (round-15 entry, released within weeks; the cognitive-science S1/S2 pattern dates to Kahneman 'Thinking Fast and Slow' 2011); (2) high-rate continuous VLA control was demonstrated by π₀ (round-12, October 2024) and π₀.₅ (round-12, April 2025) in diffusion/flow-matching form; (3) onboard low-power VLA inference is anticipated by OpenVLA-OFT (round-12, parallel decoding + 26× throughput); (4) multi-robot collaboration is anticipated by ROS 2 (round-13, real-time multi-vehicle middleware) and the Mobile ALOHA / ACT bimanual lineage. Direct shielding for any Helix or Helix-derivative commercial-IP claim.
