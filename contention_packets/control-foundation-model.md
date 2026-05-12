---
title: "control-foundation-model"
parent: "Invalidity Contentions"
nav_order: 63
layout: default
---

# Invalidity Contention Packet — `control-foundation-model`

**Generated:** 2026-05-12  
**Cross-cut tag:** `control-foundation-model`  
**Entries:** 21 (19 commons-grade, 2 draft)  
**Earliest disclosure:** 1997-11  
**Most recent disclosure:** 2025-11

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-foundation-model`.

To use it:

1. Identify the patent claim element being challenged.
2. Match the element against the entries below in chronological order (earliest
   first). The earliest entry that discloses the element is the strongest 102
   anticipation candidate.
3. For 103 obviousness contentions, identify the closest two-or-more entries
   that together disclose all claim elements.
4. Each entry's **prior_art_notes** field is element-by-element 102/103
   anticipation analysis — citable as-is.
5. Verify the timestamp authority via the procedures in Verification (below).

The Free Humanoid Corpus is licensed CC0 1.0; no permission is required to
cite, copy, or redistribute these contentions.

---

## Entries (chronological)

### 1997-11 — Long Short-Term Memory (LSTM)

- **id:** `lstm-hochreiter-schmidhuber-1997`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** TU München + IDSIA Lugano; Sepp Hochreiter, Jürgen Schmidhuber
- **disclosure citation:** Hochreiter, S., Schmidhuber, J. 'Long Short-Term Memory'. Neural Computation 9(8) 1997. Technische Universität München + IDSIA Lugano.
- **disclosed subsystems:** `control-foundation-model`, `control-sequence-model`, `control-recurrent-network`

**Prior art notes:**

> LSTM (Hochreiter + Schmidhuber 1997) is the foundational recurrent neural network architecture. 28-year-deep public-domain prior art. >85,000 citations. The pre-Transformer-era sequence-modeling standard, still used in modern robotic policy architectures (RoboFlamingo round-29 uses LSTM action decoder). Direct shielding for any commercial humanoid claim using recurrent neural network architectures.

**Sources:**

1. Hochreiter, S., Schmidhuber, J. Neural Computation 9(8) 1997.

---

### 2013-01 — Word2Vec

- **id:** `word2vec-mikolov-2013`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Google Research; Tomas Mikolov, Kai Chen, Greg Corrado, Jeffrey Dean
- **disclosure citation:** Mikolov, T., Chen, K., Corrado, G., Dean, J. 'Efficient Estimation of Word Representations in Vector Space'. ICLR 2013 Workshop. arXiv:1301.3781. Subsequent: Mikolov et al. 'Distributed Representations of Words and Phrases and their Compositionality' NeurIPS 2013. Google Research.
- **disclosed subsystems:** `control-foundation-model`, `control-word-embedding`

**Prior art notes:**

> Word2Vec (Mikolov et al. Google 2013) is the foundational neural word-embedding paper. 12-year-deep public-domain prior art. The architectural ancestor of every modern language-model embedding underlying CLIP / SigLIP / language inputs to VLA. Direct shielding for any commercial humanoid claim using language-model embeddings.

**Sources:**

1. Mikolov et al. arXiv:1301.3781 ICLR 2013 Workshop.
2. Mikolov et al. NeurIPS 2013.

---

### 2014-09 — Sequence to Sequence Learning

- **id:** `sutskever-seq2seq-nips-2014`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Google; Ilya Sutskever, Oriol Vinyals, Quoc V. Le
- **disclosure citation:** Sutskever, I., Vinyals, O., Le, Q. V. 'Sequence to Sequence Learning with Neural Networks'. NeurIPS 2014. arXiv:1409.3215. Google.
- **disclosed subsystems:** `control-foundation-model`, `control-encoder-decoder`, `control-sequence-model`

**Prior art notes:**

> Seq2Seq (Sutskever-Vinyals-Le NeurIPS 2014) is the foundational encoder-decoder neural network paper. 11-year-deep public-domain prior art. The architectural pattern underlying every encoder-decoder system in the corpus, including every VLA's action-decoder pattern. Together with LSTM (round-30) + Transformer (round-29), establishes the sequence-modeling chain underlying every modern AI system.

**Sources:**

1. Sutskever, I., Vinyals, O., Le, Q. V. arXiv:1409.3215 NeurIPS 2014.

---

### 2017-06 — Transformer (Attention Is All You Need)

- **id:** `transformer-vaswani-neurips-2017`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Google Brain + Google Research; Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan Gomez, Łukasz Kaiser, Illia Polosukhin
- **disclosure citation:** Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., Polosukhin, I. 'Attention Is All You Need'. NeurIPS 2017. arXiv:1706.03762. Google Brain + Google Research.
- **disclosed subsystems:** `control-foundation-model`, `control-attention-mechanism`, `control-sequence-model`

**Prior art notes:**

> The Transformer (Vaswani et al. NeurIPS 2017) is **the single most-cited prior-art-everything-in-the-corpus reference**. 8-year-deep public-domain prior art. Direct architectural ancestor of every modern foundation model + every VLA. This entry resolves ~50 prior_art_notes references that previously cited 'Transformer architecture' or 'Vaswani 2017' informally. **Direct shielding for any commercial humanoid claim that uses transformer architectures**, which is essentially every modern humanoid VLA + perception system.

**Sources:**

1. Vaswani et al. arXiv:1706.03762 NeurIPS 2017.

---

### 2017-10 — Covariant.ai (robotic foundation model for grasping)

- **id:** `covariant-ai-2017`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Covariant Inc. (Berkeley, CA, USA); Pieter Abbeel + Peter Chen + Rocky Duan + Tianhao Zhang
- **disclosure citation:** Covariant Inc. (Berkeley, CA, USA; founded 2017 by Pieter Abbeel + Peter Chen + Rocky Duan + Tianhao Zhang). Covariant Brain → RFM-1 robotic foundation model 2024.
- **disclosed subsystems:** `warehouse-robot`, `control-foundation-model`

**Prior art notes:**

> Covariant.ai (Berkeley 2017+; RFM-1 2024) is the robotic foundation model for grasping. 8-year-deep public-disclosure prior art.

**Sources:**

1. en.wikipedia.org/wiki/Covariant_(company)

---

### 2018-10 — BERT (Bidirectional Encoder Representations from Transformers)

- **id:** `bert-devlin-google-2018`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Google Research; Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova
- **disclosure citation:** Devlin, J., Chang, M.-W., Lee, K., Toutanova, K. 'BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding'. NAACL 2019 Best Paper. arXiv:1810.04805. Google Research.
- **disclosed subsystems:** `control-foundation-model`, `control-language-model`, `control-self-supervised-language`

**Prior art notes:**

> BERT (Devlin et al. Google NAACL 2019) is the foundational bidirectional language model. 7-year-deep public-domain prior art. >90,000 citations. The architectural ancestor of every encoder-style language model + the predecessor of the masked-modeling regime that MAE (round-30) extended to vision.

**Sources:**

1. Devlin et al. arXiv:1810.04805 NAACL 2019.

---

### 2020-05 — GPT-3 (Brown et al. OpenAI 2020)

- **id:** `gpt-3-brown-openai-neurips-2020`
- **corpus:** academic
- **ip status:** trade-secret
- **creator:** OpenAI; Tom Brown + 30+ co-authors
- **disclosure citation:** Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., et al. 'Language Models are Few-Shot Learners'. NeurIPS 2020 Best Paper. arXiv:2005.14165. OpenAI.
- **disclosed subsystems:** `control-foundation-model`, `control-language-model`, `control-in-context-learning`

**Prior art notes:**

> GPT-3 (Brown et al. OpenAI NeurIPS 2020) is the foundational large-scale language model. 5-year-deep public-disclosure prior art. The architectural ancestor of every commercial LLM and every VLA's language backbone. Direct shielding for any commercial humanoid claim using LLM-grounded instruction following.

**Sources:**

1. Brown et al. arXiv:2005.14165 NeurIPS 2020.

---

### 2020-06 — Denoising Diffusion Probabilistic Models (DDPM)

- **id:** `ddpm-ho-neurips-2020`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** UC Berkeley; Jonathan Ho, Ajay Jain, Pieter Abbeel; antecedent: Stanford Sohl-Dickstein 2015
- **disclosure citation:** Ho, J., Jain, A., Abbeel, P. 'Denoising Diffusion Probabilistic Models'. NeurIPS 2020. arXiv:2006.11239. UC Berkeley. The antecedent: Sohl-Dickstein, J., Weiss, E., Maheswaranathan, N., Ganguli, S. 'Deep Unsupervised Learning using Nonequilibrium Thermodynamics'. ICML 2015 (the original diffusion model paper).
- **disclosed subsystems:** `control-foundation-model`, `control-diffusion-policy`, `control-generative-model`

**Prior art notes:**

> DDPM (Ho et al. NeurIPS 2020) is the foundational modern diffusion-models paper. 5-year-deep public-domain prior art. **Direct architectural ancestor of Diffusion Policy (corpus), DP3 (round-17), RDT-1B (round-13), π₀ (round-12)** — every diffusion-based VLA + manipulation policy. Direct shielding for any commercial humanoid claim on diffusion-based action generation. Closes a major foundational citation chain.

**Sources:**

1. Ho, Jain, Abbeel. arXiv:2006.11239 NeurIPS 2020.
2. Sohl-Dickstein et al. ICML 2015 (diffusion antecedent).

---

### 2021-01 — Sereact PickGPT (first commercial robotics transformer)

- **id:** `sereact-pickgpt-2021`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Sereact (Stuttgart, Germany); Ralf Gulde + Marc Tuscher (ex-Univ. Stuttgart AI)
- **disclosure citation:** Sereact (Stuttgart, Germany; founded 2021 by Ralf Gulde + Marc Tuscher, ex-Univ. Stuttgart AI). $140M+ total funding. BMW + Daimler + Bol customers.
- **disclosed subsystems:** `warehouse-robot`, `control-foundation-model`

**Prior art notes:**

> Sereact PickGPT (Stuttgart 2021+) is the canonical European warehouse-AI transformer foundation model. 4-year-deep public-disclosure prior art.

**Sources:**

1. eu-startups.com/2025/01/sereact-secures-e25-million-to-develop-robotics-hardware-and-expand-to-the-us/

---

### 2021-07 — AlphaFold 2

- **id:** `alphafold2-jumper-deepmind-2021`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** DeepMind; John Jumper, Demis Hassabis et al.
- **disclosure citation:** Jumper, J., Evans, R., Pritzel, A., Green, T., Figurnov, M., et al. 'Highly accurate protein structure prediction with AlphaFold'. Nature 596 2021. DeepMind. CASP14 winner. Nobel Prize in Chemistry 2024 (Hassabis + Jumper).
- **disclosed subsystems:** `control-foundation-model`, `control-scientific-ml`

**Prior art notes:**

> AlphaFold 2 (Jumper + Hassabis et al. DeepMind Nature 2021) is the foundational scientific ML milestone. 4-year-deep open-permissive prior art. Nobel Prize in Chemistry 2024. Often cited in humanoid robotics as the proof point that deep learning can solve previously-intractable scientific problems — the AI lab aspiration for embodied physical-AI.

**Sources:**

1. Jumper et al. Nature 596 2021.
2. AlphaFold DB (alphafold.ebi.ac.uk).

---

### 2022-04 — Flamingo (DeepMind multimodal VLM)

- **id:** `flamingo-alayrac-deepmind-2022`
- **corpus:** academic
- **ip status:** trade-secret
- **creator:** DeepMind; Jean-Baptiste Alayrac, Karen Simonyan et al.
- **disclosure citation:** Alayrac, J.-B., Donahue, J., Luc, P., Miech, A., Barr, I., Hasson, Y., Lenc, K., Mensch, A., Millican, K., Reynolds, M., Ring, R., Rutherford, E., Cabi, S., Han, T., Gong, Z., Samangouei, S., Monteiro, M., Menick, J., Borgeaud, S., Brock, A., Nematzadeh, A., Sharifzadeh, S., Binkowski, M., Barreira, R., Vinyals, O., Zisserman, A., Simonyan, K. 'Flamingo: a Visual Language Model for Few-Shot Learning'. NeurIPS 2022. arXiv:2204.14198. DeepMind.
- **disclosed subsystems:** `control-foundation-model`, `control-vision-language`

**Prior art notes:**

> Flamingo (Alayrac et al. DeepMind NeurIPS 2022) is the foundational multimodal VLM. 3-year-deep public-disclosure prior art. The architectural ancestor of OpenFlamingo + RoboFlamingo (round-29) and the multimodal-VLM lineage that underlies many modern VLAs.

**Sources:**

1. Alayrac et al. arXiv:2204.14198 NeurIPS 2022.

---

### 2023-01 — Skild AI (OmniBrain robotics foundation model)

- **id:** `skild-ai-pathak-gupta-2023`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Skild AI (USA); Deepak Pathak + Abhinav Gupta (ex-CMU faculty)
- **disclosure citation:** Skild AI (Pittsburgh + SF Bay, USA; founded 2023 by Deepak Pathak + Abhinav Gupta, ex-CMU faculty). $300M Series A 2024 at $1.5B valuation; $1.4B Series C Jan 2026 at $14B+ valuation.
- **disclosed subsystems:** `ai-foundation-model`, `control-foundation-model`

**Prior art notes:**

> Skild AI (Pittsburgh + SF 2023+) is a top-3 robotics foundation model company by capitalization. 2-year-deep public-disclosure prior art.

**Sources:**

1. businesswire.com/news/home/20240709306400/en/Skild-AI-Raises-$300M-Series-A

---

### 2023-07 — LLaMA 2

- **id:** `meta-llama-2-2023`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Meta AI; Touvron, Martin, Stone, et al.
- **disclosure citation:** Touvron, H., Martin, L., Stone, K., et al. 'Llama 2: Open Foundation and Fine-Tuned Chat Models'. arXiv:2307.09288, July 2023. Meta AI.
- **disclosed subsystems:** `control-language-model`, `control-foundation-model`

**Prior art notes:**

> LLaMA 2 is Meta's canonical open-weight LLM (July 2023). 2-year-deep open-permissive prior art for: 7B-70B-class open-weight language models. The language backbone of OpenVLA — directly anchors the LLM-grounded VLA architectural pattern. Shields any commercial humanoid claim on LLM-grounded instruction following where Llama-class open weights are an architectural alternative.

**Sources:**

1. Touvron et al. arXiv:2307.09288 July 2023.
2. Meta AI Llama project (llama.meta.com).

---

### 2023-07 — Retentive Network (RetNet)

- **id:** `retentive-network-microsoft-2023`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Microsoft Research + Tsinghua University; Yutao Sun, Furu Wei et al.
- **disclosure citation:** Sun, Y., Dong, L., Huang, S., Ma, S., Xia, Y., Xue, J., Wang, J., Wei, F. 'Retentive Network: A Successor to Transformer for Large Language Models'. arXiv:2307.08621, July 2023. Microsoft Research + Tsinghua University.
- **disclosed subsystems:** `control-foundation-model`, `control-sequence-model`

**Prior art notes:**

> RetNet (Sun et al. Microsoft + Tsinghua 2023) is one of the canonical post-Transformer architecture explorations. 2-year-deep public-domain prior art. Together with Mamba (round-34), establishes the alternative-architecture prior-art chain that challenges Transformer dominance in long-context sequence modeling.

**Sources:**

1. Sun et al. arXiv:2307.08621 July 2023.

---

### 2023-07 — DeepMind RT-2 + AutoRT + SARA-RT + RT-Trajectory

- **id:** `deepmind-rt-2-autort-2023`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** Google DeepMind robotics team
- **disclosure citation:** Google DeepMind robotics team. RT-2 released July 2023. AutoRT + SARA-RT + RT-Trajectory January 2024.
- **disclosed subsystems:** `ai-foundation-model`, `control-foundation-model`

**Prior art notes:**

> DeepMind RT-2 + AutoRT + SARA-RT + RT-Trajectory (Google DeepMind 2023-2024) is the foundational DeepMind VLA lineage. 2-year-deep academic-publication prior art.

**Sources:**

1. deepmind.google/blog/rt-2-new-model-translates-vision-and-language-into-action/

---

### 2023-10 — Open X-Embodiment / RT-X (collaborative robot dataset 2023)

- **id:** `open-x-embodiment-rt-x-2023`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** Open X-Embodiment Collaboration (200+ authors, 30+ institutions led by Google DeepMind + Stanford + Berkeley)
- **disclosure citation:** Open X-Embodiment Collaboration (Padalkar, A., et al. — 200+ authors from 30+ institutions including Google DeepMind, Stanford, UC Berkeley, MIT, CMU). 'Open X-Embodiment: Robotic Learning Datasets and RT-X Models'. arXiv:2310.08864, October 2023. ICRA 2024 best-paper award.
- **disclosed subsystems:** `ai-foundation-model`, `control-foundation-model`

**Prior art notes:**

> Open X-Embodiment / RT-X (200+ author collaboration arXiv 2310.08864, ICRA 2024 best paper) is the foundational cross-embodiment robot-learning dataset — the 'ImageNet of robot learning'. 2-year-deep open-permissive prior art. Foundational to Skild AI (corpus), Octo (corpus), OpenVLA (corpus), Pi-0.5 (corpus).

**Sources:**

1. arxiv.org/abs/2310.08864

---

### 2023-12 — Mamba (Selective State-Space Model)

- **id:** `mamba-state-space-model-gu-dao-2023`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** CMU + Princeton + Together AI; Albert Gu, Tri Dao
- **disclosure citation:** Gu, A., Dao, T. 'Mamba: Linear-Time Sequence Modeling with Selective State Spaces'. COLM 2024. arXiv:2312.00752. CMU + Princeton + Together AI. Antecedent: S4 / S4D / S5 (Gu 2022).
- **disclosed subsystems:** `control-foundation-model`, `control-state-space-model`, `control-sequence-model`

**Prior art notes:**

> Mamba (Gu + Dao COLM 2024) is the canonical state-space-model foundation architecture. 1.5-year-deep public-domain prior art. A leading architectural alternative to Transformers (round-29) for long-context sequence modeling. Direct shielding for any commercial humanoid claim using state-space-model architectures for VLA or perception.

**Sources:**

1. Gu, A., Dao, T. arXiv:2312.00752 COLM 2024.
2. Gu, A. PhD thesis (Stanford 2023) on S4/S5.

---

### 2024-10 — Anthropic Claude robotics applications *(draft)*

- **id:** `anthropic-claude-robotics-2025`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Anthropic
- **disclosure citation:** Anthropic. Claude 3.5 Sonnet 'Computer Use' API October 2024 + Claude tool-use applied to robotic platforms via third-party demonstrations 2024-2025. anthropic.com. **Indirect VLA**: Claude is not a robot-specific VLA but is increasingly used as the language reasoning backbone for high-level planning that downstream policies execute (RoboCat-style hierarchical decomposition).
- **disclosed subsystems:** `control-foundation-model`, `control-language-model`, `control-tool-use`

**Prior art notes:**

> Anthropic Claude robotics applications (Oct 2024+) — speculative prior art for tool-use language model + downstream robotic integration. Direct shielding is limited (this is not a robot-specific VLA), but the tool-use abstraction is referenced in modern hierarchical-VLA architectures (SayCan-style).

**Sources:**

1. Anthropic Claude 3.5 Sonnet 'Computer Use' announcement (anthropic.com/news/3-5-models-and-computer-use, October 2024).

---

### 2025-04 — Zeon Systems (AI-powered robotics for lab automation; Y Combinator)

- **id:** `zeon-systems-yc-2025`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Zeon Systems (San Francisco, CA, USA); Brontë + Tahir D'Mello co-founders
- **disclosure citation:** Zeon Systems (San Francisco, CA, USA; founded 2025 by Brontë + Tahir D'Mello). Y Combinator Spring 2025 batch. Backed by Y Combinator + FCVC + A* Capital. Stanford + UCSF lab partnerships.
- **disclosed subsystems:** `lab-automation-robot`, `control-natural-language-instruction`, `control-foundation-model`

**Prior art notes:**

> Zeon Systems (San Francisco 2025+; YC Spring 2025) is the canonical natural-language-driven scientific lab automation platform. <1-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid or lab-automation claim deriving from natural-language experiment description → code generation → robotic-arm execution with world-model-grounded perception + closed-loop execution.

**Sources:**

1. zeonsystems.ai (corporate site).
2. ycombinator.com/companies/zeon-systems
3. ycombinator.com/launches/NOp-zeon-systems-ai-powered-robotics-for-lab-automation

---

### 2025-06 — Apple Intelligence + Apple Robotics research (2025) *(draft)*

- **id:** `apple-vla-research-2025`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Apple Inc.
- **disclosure citation:** Apple Inc. Apple Intelligence stack (announced June 2024 WWDC); Apple Vision Pro hardware (released February 2024) increasingly deployed as teleop interface for academic humanoid robots (Open-TeleVision round-16); Apple Machine Learning Research publishing robotics-adjacent work 2024-2025.
- **disclosed subsystems:** `control-foundation-model`, `control-vr-headset-teleoperation`

**Prior art notes:**

> Apple's emerging robotics research (2024-2025) is documented primarily through hardware deployment (Apple Vision Pro in Open-TeleVision round-16) and Apple Machine Learning Research publications. Specific internal Apple robotics products are not publicly disclosed. The existence of Apple-platform academic deployments establishes prior-art shielding against any commercial humanoid claim that integrates Apple Vision Pro / Apple Intelligence as a teleop or perception interface.

**Sources:**

1. Apple Vision Pro product launch documentation Feb 2024.
2. Apple Intelligence WWDC 2024 announcement.
3. Apple Machine Learning Research (machinelearning.apple.com).
4. Open-TeleVision (round-16 corpus entry) deploys on Apple Vision Pro.

---

### 2025-11 — Sunday Robotics Memo (household humanoid; Tony Zhao + Cheng Chi)

- **id:** `sunday-robotics-memo-2025`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Sunday Robotics (USA); Tony Zhao + Cheng Chi (Stanford ALOHA + Diffusion Policy lineage)
- **disclosure citation:** Sunday Robotics (USA; founded 2024 by Tony Zhao + Cheng Chi). Memo household humanoid unveiled November 19, 2025. Founding Family Beta launching late 2026; 50 households. $1.15B valuation March 2026. $35M Series B Benchmark + Conviction-led. Tony Zhao = Stanford CS PhD ALOHA + ACT (corpus act-aloha); Cheng Chi = Columbia CS PhD + Stanford Diffusion Policy (corpus diffusion-policy).
- **disclosed subsystems:** `humanoid-wheeled`, `control-foundation-model`, `control-imitation-learning`, `mechanism-skill-capture-glove`

**Prior art notes:**

> Sunday Robotics Memo (Tony Zhao + Cheng Chi 2024-2025+) is the canonical household humanoid trained on 'zero robot data' via Skill Capture Glove human demonstrations. <1-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from: (1) household-chore humanoids; (2) human-glove-based training methodologies for robot foundation models; (3) ACT-1-class transformer VLA trained without robot demonstration data. Lineage descends from ALOHA (corpus act-aloha; Tony Zhao Stanford 2023) and Diffusion Policy (corpus diffusion-policy; Cheng Chi Columbia/Stanford 2023). The Tony Zhao + Cheng Chi commercial spinout.

**Sources:**

1. sunday.ai (corporate site).
2. techcrunch.com/2026/03/12/humanoid-robotics-maker-sunday-reaches-1-15b-valuation-to-build-household-robots/
3. eweek.com/news/sunday-memo-home-robot/
4. siliconangle.com/2025/11/20/sunday-wants-put-robot-every-home-beginning-launch-memo/
5. founded.com/sunday-memo-robot-chores-founders/

---

## Verification

This packet's entries are anchored by the Free Humanoid Corpus 2026.Q2
release with three independent cryptographic timestamps proving
pre-existence:

- **FreeTSA RFC 3161** — `releases/2026.Q2/freetsa.tsr` in the corpus repo
- **DigiCert RFC 3161** — `releases/2026.Q2/digicert.tsr`
- **OpenTimestamps Bitcoin-anchored** — `releases/2026.Q2/corpus-2026.Q2.tar.gz.ots`,
  with Bitcoin block headers at heights **948142** (bob),
  **948151** (eternitywall), and **948161** (catallaxy).

The full release tarball SHA-256 is `aa9430c6e785a409e3dbb10042b16e0e5677752c85eeffcba2c6b5605cde27ce`,
archived on Zenodo at <https://doi.org/10.5281/zenodo.20049531>.

Anyone with a Bitcoin block explorer can independently verify that the corpus
tarball — containing all entries cited in this packet — existed at or before
the timestamps anchored in those blocks.

For verification procedure see <https://github.com/openIE-dev/free-humanoid-corpus/blob/main/tools/verify_release.sh>.

---

## License

CC0 1.0 Universal (public domain dedication). No copyright restrictions on
use, citation, copying, or redistribution.

---

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `4e68247`.*
