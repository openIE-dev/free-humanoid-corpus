---
title: control-motion-capture-imitation
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-motion-capture-imitation`

**5 corpus entries disclose this subsystem.**

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

## Adversarial Skill Embeddings (ASE) (2022-04)

- **id**: `ase-peng-stanford-2022`
- **corpus**: academic
- **creator**: NVIDIA + Stanford + UC Berkeley + University of Toronto; Xue Bin Peng et al.
- **disclosure**: Peng, X. B., Guo, Y., Halper, L., Levine, S., Fidler, S. 'ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters'. ACM Transactions on Graphics 41(4) 2022 (SIGGRAPH 2022). arXiv:2205.01906. NVIDIA + Stanford + UC Berkeley + University of Toronto.
- **ip status**: open-permissive
- **prior art notes**: ASE (Peng et al. SIGGRAPH 2022) is the canonical successor to AMP (round-21). 3-year-deep open-permissive prior art for: latent-skill-space adversarial-training for character animation, task-conditioned skill reuse. **Direct ancestor of HumanPlus + ExBody humanoid imitation policies** (round-27 entries below). Together with DeepMimic (round-21) + AMP (round-21), establishes the 7-year mocap-imitation-RL chain DeepMimic 2018 → AMP 2021 → ASE 2022 → HumanPlus 2024 → ExBody 2024.

## ExBody whole-body humanoid policy (2024-02)

- **id**: `exbody-stanford-2024`
- **corpus**: academic
- **creator**: UC San Diego + MIT + CMU; Xuxin Cheng, Yandong Ji, Junming Chen, Ruihan Yang, Ge Yang, Xiaolong Wang
- **disclosure**: Cheng, X., Ji, Y., Chen, J., Yang, R., Yang, G., Wang, X. 'Expressive Whole-Body Control for Humanoid Robots'. RSS 2024. arXiv:2402.16796. UC San Diego + MIT + CMU.
- **ip status**: open-permissive
- **prior art notes**: ExBody (Cheng et al. RSS 2024) is the canonical expressive whole-body humanoid policy paper. 1.5-year-deep open-permissive prior art. Companion to HumanPlus (round-27); both apply mocap-imitation RL to actual humanoid hardware (Unitree H1). Direct shielding for any commercial humanoid claim on expressive whole-body motion (dance, gestures).

## HumanPlus humanoid (2024-06)

- **id**: `humanplus-stanford-2024`
- **corpus**: academic
- **creator**: Stanford University; Zipeng Fu, Qingqing Zhao, Qi Wu, Gordon Wetzstein, Chelsea Finn
- **disclosure**: Fu, Z., Zhao, Q., Wu, Q., Wetzstein, G., Finn, C. 'HumanPlus: Humanoid Shadowing and Imitation from Humans'. CoRL 2024. arXiv:2406.10454. Stanford University.
- **ip status**: open-permissive
- **prior art notes**: HumanPlus (Fu et al. CoRL 2024) is the canonical Stanford humanoid-imitation-from-humans paper. 1-year-deep open-permissive prior art for: two-stage RL-shadowing + IL fine-tuning, real-hardware humanoid full-body imitation from human motion. Direct architectural application of AMP/ASE lineage (rounds 21+27) to actual humanoid hardware. Direct shielding for any commercial humanoid claim on 'humanoid imitates humans' or 'mocap-trained humanoid policy on real hardware'.
