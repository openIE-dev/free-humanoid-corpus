---
title: control-multi-robot-coordination
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-multi-robot-coordination`

**2 corpus entries disclose this subsystem.**

Earliest disclosure: 2000-01

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Czech Technical University Prague (CVUT/CTU) robotics (2000-01)

- **id**: `cvut-prague-czech-robotics`
- **corpus**: academic
- **creator**: Czech Technical University in Prague (CVUT/CTU); Multi-Robot Systems group + Faculty of Electrical Engineering
- **disclosure**: České Vysoké Učení Technické v Praze / Czech Technical University in Prague (CVUT/CTU). Faculty of Electrical Engineering robotics group; Multi-Robot Systems (MRS) group led by Martin Saska — major contributor to multi-MAV (multi-Micro-Aerial-Vehicle) research and DARPA Subterranean Challenge (2nd place 2021 alongside CSIRO). cvut.cz.
- **ip status**: open-permissive
- **prior art notes**: CVUT Prague is Czech Republic's leading robotics academic institution and a Central European robotics anchor. **First real (non-fictional) entry in the corpus from Czech Republic** — closes a regional gap (corpus had only the fictional R.U.R. entry from CZ). Notable for multi-MAV + DARPA SubT work. Aggregator-style; specific CVUT MRS papers should be added in future rounds.

## Figure Helix (2025-02)

- **id**: `figure-helix-2025`
- **corpus**: private
- **creator**: Figure AI Inc.
- **disclosure**: Figure AI Inc. 'Helix: A Vision-Language-Action Model for Generalist Humanoid Control'. Public reveal February 2025 via figure.ai/news/helix. Subsequent disclosures: 'Helix Accelerating Real-World Logistics' (figure.ai/news/helix-logistics) and Hacker News + Robot Report coverage. No academic publication; trade-secret commercial VLA.
- **ip status**: trade-secret
- **prior art notes**: Helix is Figure AI's canonical 2025 commercial humanoid VLA. Public-disclosure surface (corporate blog + demo videos + Hacker News + Robot Report coverage) reveals architecture (S1/S2 dual-system, 35-DoF/200Hz, ~500hr teleop training) but withholds neural-network specifics, training-data composition, fine-tuning recipe, and policy-evaluation metrics. The capability set claimed is fully covered by deep open academic prior art chains: (1) S1/S2 dual-system architecture is shared with NVIDIA GR00T N1 (round-15 entry, released within weeks; the cognitive-science S1/S2 pattern dates to Kahneman 'Thinking Fast and Slow' 2011); (2) high-rate continuous VLA control was demonstrated by π₀ (round-12, October 2024) and π₀.₅ (round-12, April 2025) in diffusion/flow-matching form; (3) onboard low-power VLA inference is anticipated by OpenVLA-OFT (round-12, parallel decoding + 26× throughput); (4) multi-robot collaboration is anticipated by ROS 2 (round-13, real-time multi-vehicle middleware) and the Mobile ALOHA / ACT bimanual lineage. Direct shielding for any Helix or Helix-derivative commercial-IP claim.
