---
title: control-motion-capture-imitation
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-motion-capture-imitation`

**2 corpus entries disclose this subsystem.**

Earliest disclosure: 2018-04

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## DeepMimic (2018-04)

- **id**: `deepmimic-peng-siggraph-2018`
- **corpus**: academic
- **creator**: UC Berkeley + UBC; Xue Bin (Jason) Peng, Pieter Abbeel, Sergey Levine, Michiel van de Panne
- **disclosure**: Peng, X. B., Abbeel, P., Levine, S., van de Panne, M. 'DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills'. ACM Transactions on Graphics 37(4) 2018 (SIGGRAPH 2018). arXiv:1804.02717. UC Berkeley + UBC.
- **ip status**: open-permissive
- **prior art notes**: DeepMimic (Peng et al. SIGGRAPH 2018) is the canonical foundational motion-capture-imitation deep-RL framework. 7-year-deep open-permissive prior art for: deep-RL imitation of motion-capture references, physics-based character animation via RL, complex acrobatic skill (backflip, spin) RL training. **The architectural ancestor of**: Adversarial Motion Priors (round-21 entry below), ASE (Peng et al. 2022), the entire humanoid-from-mocap-data line. Direct shielding for any commercial humanoid claim on motion-capture-trained policies (Tesla Optimus, Figure Helix demos all use mocap-style imitation; this is 7-year-deep prior art).

## Adversarial Motion Priors (AMP) (2021-04)

- **id**: `amp-peng-siggraph-2021`
- **corpus**: academic
- **creator**: UC Berkeley; Xue Bin (Jason) Peng, Ze Ma, Pieter Abbeel, Sergey Levine, Angjoo Kanazawa
- **disclosure**: Peng, X. B., Ma, Z., Abbeel, P., Levine, S., Kanazawa, A. 'AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control'. ACM Transactions on Graphics 40(4) 2021 (SIGGRAPH 2021). arXiv:2104.02180. UC Berkeley.
- **ip status**: open-permissive
- **prior art notes**: Adversarial Motion Priors (Peng et al. SIGGRAPH 2021) is the canonical extension of DeepMimic to GAN-style latent-space motion imitation. 4-year-deep open-permissive prior art for: GAN-distilled motion priors, latent-space mocap style imitation, task-conditioned style-aware humanoid RL. **The architectural ancestor of contemporary humanoid-from-mocap RL** including ASE (Peng et al. 2022), HumanPlus (Stanford 2024), ExBody (Stanford 2024), H1 / G1 humanoid policies (Unitree). Direct shielding for any commercial humanoid claim on 'humanoid moves like a human' style-aware locomotion.
