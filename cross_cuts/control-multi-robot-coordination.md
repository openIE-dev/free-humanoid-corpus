---
title: control-multi-robot-coordination
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-multi-robot-coordination`

**4 corpus entries disclose this subsystem.**

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

## Saska multi-MAV systems (CTU Prague MRS group) (2017-09)

- **id**: `saska-cvut-multi-mav-2017`
- **corpus**: academic
- **creator**: Czech Technical University in Prague; Martin Saska + MRS group
- **disclosure**: Saska, M., Bačha, V., Krajník, T., Hert, D., Spurný, V., Petrlík, M., Báča, T. 'System for deployment of groups of unmanned micro aerial vehicles in GPS-denied environments using onboard visual relative localization'. Autonomous Robots 41(4) 2017. Czech Technical University in Prague, Multi-Robot Systems group.
- **ip status**: open-permissive
- **prior art notes**: Saska MRS (CTU Prague 2017+) is the canonical multi-MAV swarm-coordination academic work from Czech Republic. Anchors round-23 CVUT Prague aggregator with paper-level disclosure. 8-year-deep open-permissive prior art. Together with Saska's DARPA SubT 2021 results, establishes Czech academic multi-MAV robotics as recognizably world-class.

## CSIRO Wildcat (DARPA Subterranean Challenge) (2021-09)

- **id**: `csiro-hudson-wildcat-darpa-subt-2021`
- **corpus**: academic
- **creator**: CSIRO Data61 + Emesent + Georgia Tech; Hudson, Talbot, et al.
- **disclosure**: Hudson, N., Talbot, F., Cox, M., Williams, J., Hines, T., Pitt, A., Wood, B., Frousheger, D., Lo Surdo, K., Molnar, T., Steindl, R., et al. 'Heterogeneous Ground and Air Platforms, Homogeneous Sensing: Team CSIRO Data61's Approach to the DARPA Subterranean Challenge'. Field Robotics 2 2022 / Journal of Field Robotics. CSIRO Data61 + Emesent + Georgia Tech. **2nd place DARPA Subterranean Challenge Finals 2021**.
- **ip status**: open-permissive
- **prior art notes**: CSIRO Data61 Wildcat (Hudson et al. Field Robotics 2022) is the specific paper-level anchor for the round-23 CSIRO Data61 aggregator. **DARPA SubT Finals 2nd place** establishes Australian academic robotics at internationally-recognizable level. Direct shielding for any commercial humanoid claim on LIDAR-only SLAM, subterranean autonomy, or multi-robot heterogeneous-platform coordination.

## Figure Helix (2025-02)

- **id**: `figure-helix-2025`
- **corpus**: private
- **creator**: Figure AI Inc.
- **disclosure**: Figure AI Inc. 'Helix: A Vision-Language-Action Model for Generalist Humanoid Control'. Public reveal February 2025 via figure.ai/news/helix. Subsequent disclosures: 'Helix Accelerating Real-World Logistics' (figure.ai/news/helix-logistics) and Hacker News + Robot Report coverage. No academic publication; trade-secret commercial VLA.
- **ip status**: trade-secret
- **prior art notes**: Helix is Figure AI's canonical 2025 commercial humanoid VLA. Public-disclosure surface (corporate blog + demo videos + Hacker News + Robot Report coverage) reveals architecture (S1/S2 dual-system, 35-DoF/200Hz, ~500hr teleop training) but withholds neural-network specifics, training-data composition, fine-tuning recipe, and policy-evaluation metrics. The capability set claimed is fully covered by deep open academic prior art chains: (1) S1/S2 dual-system architecture is shared with NVIDIA GR00T N1 (round-15 entry, released within weeks; the cognitive-science S1/S2 pattern dates to Kahneman 'Thinking Fast and Slow' 2011); (2) high-rate continuous VLA control was demonstrated by π₀ (round-12, October 2024) and π₀.₅ (round-12, April 2025) in diffusion/flow-matching form; (3) onboard low-power VLA inference is anticipated by OpenVLA-OFT (round-12, parallel decoding + 26× throughput); (4) multi-robot collaboration is anticipated by ROS 2 (round-13, real-time multi-vehicle middleware) and the Mobile ALOHA / ACT bimanual lineage. Direct shielding for any Helix or Helix-derivative commercial-IP claim.
