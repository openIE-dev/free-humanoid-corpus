---
title: control-world-model
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-world-model`

**3 corpus entries disclose this subsystem.**

Earliest disclosure: 2023-01

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## DreamerV3 (Danijar Hafner et al. 2023; world-model RL) (2023-01)

- **id**: `dreamer-v3-hafner-2023`
- **corpus**: academic
- **creator**: Google DeepMind + University of Toronto; Danijar Hafner + Jurgis Pasukonis + Jimmy Ba + Timothy Lillicrap
- **disclosure**: Hafner, D., Pasukonis, J., Ba, J., Lillicrap, T. 'Mastering Diverse Domains through World Models'. arXiv:2301.04104, January 2023. Google DeepMind + University of Toronto. Predecessors: PlaNet (2018), Dreamer (2019), DreamerV2 (2020).
- **ip status**: public-domain
- **prior art notes**: DreamerV3 (Danijar Hafner et al. Google DeepMind + Toronto, arXiv 2301.04104) is the most-effective general-purpose world-model RL algorithm. 2-year-deep public-domain prior art (5-year for the broader Dreamer lineage).

## Genie (Google DeepMind 2024; foundation world model from video) (2024-02)

- **id**: `genie-deepmind-2024`
- **corpus**: academic
- **creator**: Google DeepMind; Jake Bruce + Michael Dennis + Ashley Edwards + team
- **disclosure**: Bruce, J., Dennis, M., Edwards, A., et al. 'Genie: Generative Interactive Environments'. arXiv:2402.15391, February 2024 (ICML 2024 best paper). Google DeepMind. Genie 2 (December 2024, 3D worlds); Genie 3 (2025, real-time interactive).
- **ip status**: academic-publication
- **prior art notes**: Genie (Google DeepMind arXiv 2402.15391, ICML 2024 best paper) is the foundational world model trained from unlabeled video. 1-year-deep academic-publication prior art. Directly relevant to robot world models (NVIDIA Cosmos corpus, RoboCat corpus, Sora corpus as 'world simulator').

## NVIDIA Cosmos (2025-01)

- **id**: `nvidia-cosmos-2025`
- **corpus**: academic
- **creator**: NVIDIA; multi-author research team
- **disclosure**: NVIDIA. 'Cosmos World Foundation Model Platform for Physical AI'. arXiv:2501.03575, January 2025. NVIDIA CES 2025 announcement. Open weights via HuggingFace nvidia/Cosmos-* family. Cosmos-Reason2-2B variant subsequently used as the System 2 backbone in GR00T N1.7.
- **ip status**: open-permissive
- **prior art notes**: NVIDIA Cosmos is the canonical world-foundation-model platform for physical AI (NVIDIA CES January 2025). 4-month-deep open-permissive prior art for: video generation + understanding + sim-to-real-transfer foundation models, world-modeling for physical-AI policy training. **Cosmos-Reason2-2B is the System-2 backbone of GR00T N1.7** (round-15 entry); round-17 now resolves that lineage citation. Direct shielding for any commercial humanoid claim on world-model-based policy training or on video-generation-based simulation augmentation.
