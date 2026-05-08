---
title: control-foundation-model
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-foundation-model`

**4 corpus entries disclose this subsystem.**

Earliest disclosure: 1997-11

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Long Short-Term Memory (LSTM) (1997-11)

- **id**: `lstm-hochreiter-schmidhuber-1997`
- **corpus**: academic
- **creator**: TU München + IDSIA Lugano; Sepp Hochreiter, Jürgen Schmidhuber
- **disclosure**: Hochreiter, S., Schmidhuber, J. 'Long Short-Term Memory'. Neural Computation 9(8) 1997. Technische Universität München + IDSIA Lugano.
- **ip status**: public-domain
- **prior art notes**: LSTM (Hochreiter + Schmidhuber 1997) is the foundational recurrent neural network architecture. 28-year-deep public-domain prior art. >85,000 citations. The pre-Transformer-era sequence-modeling standard, still used in modern robotic policy architectures (RoboFlamingo round-29 uses LSTM action decoder). Direct shielding for any commercial humanoid claim using recurrent neural network architectures.

## Transformer (Attention Is All You Need) (2017-06)

- **id**: `transformer-vaswani-neurips-2017`
- **corpus**: academic
- **creator**: Google Brain + Google Research; Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan Gomez, Łukasz Kaiser, Illia Polosukhin
- **disclosure**: Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., Polosukhin, I. 'Attention Is All You Need'. NeurIPS 2017. arXiv:1706.03762. Google Brain + Google Research.
- **ip status**: public-domain
- **prior art notes**: The Transformer (Vaswani et al. NeurIPS 2017) is **the single most-cited prior-art-everything-in-the-corpus reference**. 8-year-deep public-domain prior art. Direct architectural ancestor of every modern foundation model + every VLA. This entry resolves ~50 prior_art_notes references that previously cited 'Transformer architecture' or 'Vaswani 2017' informally. **Direct shielding for any commercial humanoid claim that uses transformer architectures**, which is essentially every modern humanoid VLA + perception system.

## Denoising Diffusion Probabilistic Models (DDPM) (2020-06)

- **id**: `ddpm-ho-neurips-2020`
- **corpus**: academic
- **creator**: UC Berkeley; Jonathan Ho, Ajay Jain, Pieter Abbeel; antecedent: Stanford Sohl-Dickstein 2015
- **disclosure**: Ho, J., Jain, A., Abbeel, P. 'Denoising Diffusion Probabilistic Models'. NeurIPS 2020. arXiv:2006.11239. UC Berkeley. The antecedent: Sohl-Dickstein, J., Weiss, E., Maheswaranathan, N., Ganguli, S. 'Deep Unsupervised Learning using Nonequilibrium Thermodynamics'. ICML 2015 (the original diffusion model paper).
- **ip status**: public-domain
- **prior art notes**: DDPM (Ho et al. NeurIPS 2020) is the foundational modern diffusion-models paper. 5-year-deep public-domain prior art. **Direct architectural ancestor of Diffusion Policy (corpus), DP3 (round-17), RDT-1B (round-13), π₀ (round-12)** — every diffusion-based VLA + manipulation policy. Direct shielding for any commercial humanoid claim on diffusion-based action generation. Closes a major foundational citation chain.

## LLaMA 2 (2023-07)

- **id**: `meta-llama-2-2023`
- **corpus**: academic
- **creator**: Meta AI; Touvron, Martin, Stone, et al.
- **disclosure**: Touvron, H., Martin, L., Stone, K., et al. 'Llama 2: Open Foundation and Fine-Tuned Chat Models'. arXiv:2307.09288, July 2023. Meta AI.
- **ip status**: open-permissive
- **prior art notes**: LLaMA 2 is Meta's canonical open-weight LLM (July 2023). 2-year-deep open-permissive prior art for: 7B-70B-class open-weight language models. The language backbone of OpenVLA — directly anchors the LLM-grounded VLA architectural pattern. Shields any commercial humanoid claim on LLM-grounded instruction following where Llama-class open weights are an architectural alternative.
