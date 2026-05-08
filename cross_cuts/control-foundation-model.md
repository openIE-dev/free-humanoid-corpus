---
title: control-foundation-model
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-foundation-model`

**11 corpus entries disclose this subsystem.**

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

## Word2Vec (2013-01)

- **id**: `word2vec-mikolov-2013`
- **corpus**: academic
- **creator**: Google Research; Tomas Mikolov, Kai Chen, Greg Corrado, Jeffrey Dean
- **disclosure**: Mikolov, T., Chen, K., Corrado, G., Dean, J. 'Efficient Estimation of Word Representations in Vector Space'. ICLR 2013 Workshop. arXiv:1301.3781. Subsequent: Mikolov et al. 'Distributed Representations of Words and Phrases and their Compositionality' NeurIPS 2013. Google Research.
- **ip status**: public-domain
- **prior art notes**: Word2Vec (Mikolov et al. Google 2013) is the foundational neural word-embedding paper. 12-year-deep public-domain prior art. The architectural ancestor of every modern language-model embedding underlying CLIP / SigLIP / language inputs to VLA. Direct shielding for any commercial humanoid claim using language-model embeddings.

## Transformer (Attention Is All You Need) (2017-06)

- **id**: `transformer-vaswani-neurips-2017`
- **corpus**: academic
- **creator**: Google Brain + Google Research; Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan Gomez, Łukasz Kaiser, Illia Polosukhin
- **disclosure**: Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., Polosukhin, I. 'Attention Is All You Need'. NeurIPS 2017. arXiv:1706.03762. Google Brain + Google Research.
- **ip status**: public-domain
- **prior art notes**: The Transformer (Vaswani et al. NeurIPS 2017) is **the single most-cited prior-art-everything-in-the-corpus reference**. 8-year-deep public-domain prior art. Direct architectural ancestor of every modern foundation model + every VLA. This entry resolves ~50 prior_art_notes references that previously cited 'Transformer architecture' or 'Vaswani 2017' informally. **Direct shielding for any commercial humanoid claim that uses transformer architectures**, which is essentially every modern humanoid VLA + perception system.

## BERT (Bidirectional Encoder Representations from Transformers) (2018-10)

- **id**: `bert-devlin-google-2018`
- **corpus**: academic
- **creator**: Google Research; Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova
- **disclosure**: Devlin, J., Chang, M.-W., Lee, K., Toutanova, K. 'BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding'. NAACL 2019 Best Paper. arXiv:1810.04805. Google Research.
- **ip status**: public-domain
- **prior art notes**: BERT (Devlin et al. Google NAACL 2019) is the foundational bidirectional language model. 7-year-deep public-domain prior art. >90,000 citations. The architectural ancestor of every encoder-style language model + the predecessor of the masked-modeling regime that MAE (round-30) extended to vision.

## GPT-3 (Brown et al. OpenAI 2020) (2020-05)

- **id**: `gpt-3-brown-openai-neurips-2020`
- **corpus**: academic
- **creator**: OpenAI; Tom Brown + 30+ co-authors
- **disclosure**: Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., et al. 'Language Models are Few-Shot Learners'. NeurIPS 2020 Best Paper. arXiv:2005.14165. OpenAI.
- **ip status**: trade-secret
- **prior art notes**: GPT-3 (Brown et al. OpenAI NeurIPS 2020) is the foundational large-scale language model. 5-year-deep public-disclosure prior art. The architectural ancestor of every commercial LLM and every VLA's language backbone. Direct shielding for any commercial humanoid claim using LLM-grounded instruction following.

## Denoising Diffusion Probabilistic Models (DDPM) (2020-06)

- **id**: `ddpm-ho-neurips-2020`
- **corpus**: academic
- **creator**: UC Berkeley; Jonathan Ho, Ajay Jain, Pieter Abbeel; antecedent: Stanford Sohl-Dickstein 2015
- **disclosure**: Ho, J., Jain, A., Abbeel, P. 'Denoising Diffusion Probabilistic Models'. NeurIPS 2020. arXiv:2006.11239. UC Berkeley. The antecedent: Sohl-Dickstein, J., Weiss, E., Maheswaranathan, N., Ganguli, S. 'Deep Unsupervised Learning using Nonequilibrium Thermodynamics'. ICML 2015 (the original diffusion model paper).
- **ip status**: public-domain
- **prior art notes**: DDPM (Ho et al. NeurIPS 2020) is the foundational modern diffusion-models paper. 5-year-deep public-domain prior art. **Direct architectural ancestor of Diffusion Policy (corpus), DP3 (round-17), RDT-1B (round-13), π₀ (round-12)** — every diffusion-based VLA + manipulation policy. Direct shielding for any commercial humanoid claim on diffusion-based action generation. Closes a major foundational citation chain.

## AlphaFold 2 (2021-07)

- **id**: `alphafold2-jumper-deepmind-2021`
- **corpus**: academic
- **creator**: DeepMind; John Jumper, Demis Hassabis et al.
- **disclosure**: Jumper, J., Evans, R., Pritzel, A., Green, T., Figurnov, M., et al. 'Highly accurate protein structure prediction with AlphaFold'. Nature 596 2021. DeepMind. CASP14 winner. Nobel Prize in Chemistry 2024 (Hassabis + Jumper).
- **ip status**: open-permissive
- **prior art notes**: AlphaFold 2 (Jumper + Hassabis et al. DeepMind Nature 2021) is the foundational scientific ML milestone. 4-year-deep open-permissive prior art. Nobel Prize in Chemistry 2024. Often cited in humanoid robotics as the proof point that deep learning can solve previously-intractable scientific problems — the AI lab aspiration for embodied physical-AI.

## Flamingo (DeepMind multimodal VLM) (2022-04)

- **id**: `flamingo-alayrac-deepmind-2022`
- **corpus**: academic
- **creator**: DeepMind; Jean-Baptiste Alayrac, Karen Simonyan et al.
- **disclosure**: Alayrac, J.-B., Donahue, J., Luc, P., Miech, A., Barr, I., Hasson, Y., Lenc, K., Mensch, A., Millican, K., Reynolds, M., Ring, R., Rutherford, E., Cabi, S., Han, T., Gong, Z., Samangouei, S., Monteiro, M., Menick, J., Borgeaud, S., Brock, A., Nematzadeh, A., Sharifzadeh, S., Binkowski, M., Barreira, R., Vinyals, O., Zisserman, A., Simonyan, K. 'Flamingo: a Visual Language Model for Few-Shot Learning'. NeurIPS 2022. arXiv:2204.14198. DeepMind.
- **ip status**: trade-secret
- **prior art notes**: Flamingo (Alayrac et al. DeepMind NeurIPS 2022) is the foundational multimodal VLM. 3-year-deep public-disclosure prior art. The architectural ancestor of OpenFlamingo + RoboFlamingo (round-29) and the multimodal-VLM lineage that underlies many modern VLAs.

## LLaMA 2 (2023-07)

- **id**: `meta-llama-2-2023`
- **corpus**: academic
- **creator**: Meta AI; Touvron, Martin, Stone, et al.
- **disclosure**: Touvron, H., Martin, L., Stone, K., et al. 'Llama 2: Open Foundation and Fine-Tuned Chat Models'. arXiv:2307.09288, July 2023. Meta AI.
- **ip status**: open-permissive
- **prior art notes**: LLaMA 2 is Meta's canonical open-weight LLM (July 2023). 2-year-deep open-permissive prior art for: 7B-70B-class open-weight language models. The language backbone of OpenVLA — directly anchors the LLM-grounded VLA architectural pattern. Shields any commercial humanoid claim on LLM-grounded instruction following where Llama-class open weights are an architectural alternative.

## Anthropic Claude robotics applications (2024-10)

- **id**: `anthropic-claude-robotics-2025`
- **corpus**: private
- **creator**: Anthropic
- **disclosure**: Anthropic. Claude 3.5 Sonnet 'Computer Use' API October 2024 + Claude tool-use applied to robotic platforms via third-party demonstrations 2024-2025. anthropic.com. **Indirect VLA**: Claude is not a robot-specific VLA but is increasingly used as the language reasoning backbone for high-level planning that downstream policies execute (RoboCat-style hierarchical decomposition).
- **ip status**: trade-secret
- **prior art notes**: Anthropic Claude robotics applications (Oct 2024+) — speculative prior art for tool-use language model + downstream robotic integration. Direct shielding is limited (this is not a robot-specific VLA), but the tool-use abstraction is referenced in modern hierarchical-VLA architectures (SayCan-style).

## Apple Intelligence + Apple Robotics research (2025) (2025-06)

- **id**: `apple-vla-research-2025`
- **corpus**: private
- **creator**: Apple Inc.
- **disclosure**: Apple Inc. Apple Intelligence stack (announced June 2024 WWDC); Apple Vision Pro hardware (released February 2024) increasingly deployed as teleop interface for academic humanoid robots (Open-TeleVision round-16); Apple Machine Learning Research publishing robotics-adjacent work 2024-2025.
- **ip status**: trade-secret
- **prior art notes**: Apple's emerging robotics research (2024-2025) is documented primarily through hardware deployment (Apple Vision Pro in Open-TeleVision round-16) and Apple Machine Learning Research publications. Specific internal Apple robotics products are not publicly disclosed. The existence of Apple-platform academic deployments establishes prior-art shielding against any commercial humanoid claim that integrates Apple Vision Pro / Apple Intelligence as a teleop or perception interface.
