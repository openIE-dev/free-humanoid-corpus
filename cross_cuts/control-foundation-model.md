---
title: control-foundation-model
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-foundation-model`

**22 corpus entries disclose this subsystem.**

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

## Sequence to Sequence Learning (2014-09)

- **id**: `sutskever-seq2seq-nips-2014`
- **corpus**: academic
- **creator**: Google; Ilya Sutskever, Oriol Vinyals, Quoc V. Le
- **disclosure**: Sutskever, I., Vinyals, O., Le, Q. V. 'Sequence to Sequence Learning with Neural Networks'. NeurIPS 2014. arXiv:1409.3215. Google.
- **ip status**: public-domain
- **prior art notes**: Seq2Seq (Sutskever-Vinyals-Le NeurIPS 2014) is the foundational encoder-decoder neural network paper. 11-year-deep public-domain prior art. The architectural pattern underlying every encoder-decoder system in the corpus, including every VLA's action-decoder pattern. Together with LSTM (round-30) + Transformer (round-29), establishes the sequence-modeling chain underlying every modern AI system.

## Transformer (Attention Is All You Need) (2017-06)

- **id**: `transformer-vaswani-neurips-2017`
- **corpus**: academic
- **creator**: Google Brain + Google Research; Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan Gomez, Łukasz Kaiser, Illia Polosukhin
- **disclosure**: Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., Polosukhin, I. 'Attention Is All You Need'. NeurIPS 2017. arXiv:1706.03762. Google Brain + Google Research.
- **ip status**: public-domain
- **prior art notes**: The Transformer (Vaswani et al. NeurIPS 2017) is **the single most-cited prior-art-everything-in-the-corpus reference**. 8-year-deep public-domain prior art. Direct architectural ancestor of every modern foundation model + every VLA. This entry resolves ~50 prior_art_notes references that previously cited 'Transformer architecture' or 'Vaswani 2017' informally. **Direct shielding for any commercial humanoid claim that uses transformer architectures**, which is essentially every modern humanoid VLA + perception system.

## Covariant.ai (robotic foundation model for grasping) (2017-10)

- **id**: `covariant-ai-2017`
- **corpus**: private
- **creator**: Covariant Inc. (Berkeley, CA, USA); Pieter Abbeel + Peter Chen + Rocky Duan + Tianhao Zhang
- **disclosure**: Covariant Inc. (Berkeley, CA, USA; founded 2017 by Pieter Abbeel + Peter Chen + Rocky Duan + Tianhao Zhang). Covariant Brain → RFM-1 robotic foundation model 2024.
- **ip status**: trade-secret
- **prior art notes**: Covariant.ai (Berkeley 2017+; RFM-1 2024) is the robotic foundation model for grasping. 8-year-deep public-disclosure prior art.

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

## Sereact PickGPT (first commercial robotics transformer) (2021-01)

- **id**: `sereact-pickgpt-2021`
- **corpus**: private
- **creator**: Sereact (Stuttgart, Germany); Ralf Gulde + Marc Tuscher (ex-Univ. Stuttgart AI)
- **disclosure**: Sereact (Stuttgart, Germany; founded 2021 by Ralf Gulde + Marc Tuscher, ex-Univ. Stuttgart AI). $140M+ total funding. BMW + Daimler + Bol customers.
- **ip status**: trade-secret
- **prior art notes**: Sereact PickGPT (Stuttgart 2021+) is the canonical European warehouse-AI transformer foundation model. 4-year-deep public-disclosure prior art.

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

## Skild AI (OmniBrain robotics foundation model) (2023-01)

- **id**: `skild-ai-pathak-gupta-2023`
- **corpus**: private
- **creator**: Skild AI (USA); Deepak Pathak + Abhinav Gupta (ex-CMU faculty)
- **disclosure**: Skild AI (Pittsburgh + SF Bay, USA; founded 2023 by Deepak Pathak + Abhinav Gupta, ex-CMU faculty). $300M Series A 2024 at $1.5B valuation; $1.4B Series C Jan 2026 at $14B+ valuation.
- **ip status**: trade-secret
- **prior art notes**: Skild AI (Pittsburgh + SF 2023+) is a top-3 robotics foundation model company by capitalization. 2-year-deep public-disclosure prior art.

## LLaMA 2 (2023-07)

- **id**: `meta-llama-2-2023`
- **corpus**: academic
- **creator**: Meta AI; Touvron, Martin, Stone, et al.
- **disclosure**: Touvron, H., Martin, L., Stone, K., et al. 'Llama 2: Open Foundation and Fine-Tuned Chat Models'. arXiv:2307.09288, July 2023. Meta AI.
- **ip status**: open-permissive
- **prior art notes**: LLaMA 2 is Meta's canonical open-weight LLM (July 2023). 2-year-deep open-permissive prior art for: 7B-70B-class open-weight language models. The language backbone of OpenVLA — directly anchors the LLM-grounded VLA architectural pattern. Shields any commercial humanoid claim on LLM-grounded instruction following where Llama-class open weights are an architectural alternative.

## Retentive Network (RetNet) (2023-07)

- **id**: `retentive-network-microsoft-2023`
- **corpus**: academic
- **creator**: Microsoft Research + Tsinghua University; Yutao Sun, Furu Wei et al.
- **disclosure**: Sun, Y., Dong, L., Huang, S., Ma, S., Xia, Y., Xue, J., Wang, J., Wei, F. 'Retentive Network: A Successor to Transformer for Large Language Models'. arXiv:2307.08621, July 2023. Microsoft Research + Tsinghua University.
- **ip status**: public-domain
- **prior art notes**: RetNet (Sun et al. Microsoft + Tsinghua 2023) is one of the canonical post-Transformer architecture explorations. 2-year-deep public-domain prior art. Together with Mamba (round-34), establishes the alternative-architecture prior-art chain that challenges Transformer dominance in long-context sequence modeling.

## DeepMind RT-2 + AutoRT + SARA-RT + RT-Trajectory (2023-07)

- **id**: `deepmind-rt-2-autort-2023`
- **corpus**: academic
- **creator**: Google DeepMind robotics team
- **disclosure**: Google DeepMind robotics team. RT-2 released July 2023. AutoRT + SARA-RT + RT-Trajectory January 2024.
- **ip status**: academic-publication
- **prior art notes**: DeepMind RT-2 + AutoRT + SARA-RT + RT-Trajectory (Google DeepMind 2023-2024) is the foundational DeepMind VLA lineage. 2-year-deep academic-publication prior art.

## Open X-Embodiment / RT-X (collaborative robot dataset 2023) (2023-10)

- **id**: `open-x-embodiment-rt-x-2023`
- **corpus**: open
- **creator**: Open X-Embodiment Collaboration (200+ authors, 30+ institutions led by Google DeepMind + Stanford + Berkeley)
- **disclosure**: Open X-Embodiment Collaboration (Padalkar, A., et al. — 200+ authors from 30+ institutions including Google DeepMind, Stanford, UC Berkeley, MIT, CMU). 'Open X-Embodiment: Robotic Learning Datasets and RT-X Models'. arXiv:2310.08864, October 2023. ICRA 2024 best-paper award.
- **ip status**: open-permissive
- **prior art notes**: Open X-Embodiment / RT-X (200+ author collaboration arXiv 2310.08864, ICRA 2024 best paper) is the foundational cross-embodiment robot-learning dataset — the 'ImageNet of robot learning'. 2-year-deep open-permissive prior art. Foundational to Skild AI (corpus), Octo (corpus), OpenVLA (corpus), Pi-0.5 (corpus).

## Mamba (Selective State-Space Model) (2023-12)

- **id**: `mamba-state-space-model-gu-dao-2023`
- **corpus**: academic
- **creator**: CMU + Princeton + Together AI; Albert Gu, Tri Dao
- **disclosure**: Gu, A., Dao, T. 'Mamba: Linear-Time Sequence Modeling with Selective State Spaces'. COLM 2024. arXiv:2312.00752. CMU + Princeton + Together AI. Antecedent: S4 / S4D / S5 (Gu 2022).
- **ip status**: public-domain
- **prior art notes**: Mamba (Gu + Dao COLM 2024) is the canonical state-space-model foundation architecture. 1.5-year-deep public-domain prior art. A leading architectural alternative to Transformers (round-29) for long-context sequence modeling. Direct shielding for any commercial humanoid claim using state-space-model architectures for VLA or perception.

## Anthropic Claude robotics applications (2024-10)

- **id**: `anthropic-claude-robotics-2025`
- **corpus**: private
- **creator**: Anthropic
- **disclosure**: Anthropic. Claude 3.5 Sonnet 'Computer Use' API October 2024 + Claude tool-use applied to robotic platforms via third-party demonstrations 2024-2025. anthropic.com. **Indirect VLA**: Claude is not a robot-specific VLA but is increasingly used as the language reasoning backbone for high-level planning that downstream policies execute (RoboCat-style hierarchical decomposition).
- **ip status**: trade-secret
- **prior art notes**: Anthropic Claude robotics applications (Oct 2024+) — speculative prior art for tool-use language model + downstream robotic integration. Direct shielding is limited (this is not a robot-specific VLA), but the tool-use abstraction is referenced in modern hierarchical-VLA architectures (SayCan-style).

## Zeon Systems (AI-powered robotics for lab automation; Y Combinator) (2025-04)

- **id**: `zeon-systems-yc-2025`
- **corpus**: private
- **creator**: Zeon Systems (San Francisco, CA, USA); Brontë + Tahir D'Mello co-founders
- **disclosure**: Zeon Systems (San Francisco, CA, USA; founded 2025 by Brontë + Tahir D'Mello). Y Combinator Spring 2025 batch. Backed by Y Combinator + FCVC + A* Capital. Stanford + UCSF lab partnerships.
- **ip status**: trade-secret
- **prior art notes**: Zeon Systems (San Francisco 2025+; YC Spring 2025) is the canonical natural-language-driven scientific lab automation platform. <1-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid or lab-automation claim deriving from natural-language experiment description → code generation → robotic-arm execution with world-model-grounded perception + closed-loop execution.

## Apple Intelligence + Apple Robotics research (2025) (2025-06)

- **id**: `apple-vla-research-2025`
- **corpus**: private
- **creator**: Apple Inc.
- **disclosure**: Apple Inc. Apple Intelligence stack (announced June 2024 WWDC); Apple Vision Pro hardware (released February 2024) increasingly deployed as teleop interface for academic humanoid robots (Open-TeleVision round-16); Apple Machine Learning Research publishing robotics-adjacent work 2024-2025.
- **ip status**: trade-secret
- **prior art notes**: Apple's emerging robotics research (2024-2025) is documented primarily through hardware deployment (Apple Vision Pro in Open-TeleVision round-16) and Apple Machine Learning Research publications. Specific internal Apple robotics products are not publicly disclosed. The existence of Apple-platform academic deployments establishes prior-art shielding against any commercial humanoid claim that integrates Apple Vision Pro / Apple Intelligence as a teleop or perception interface.

## Apptronik Apollo (Gen 2 + Catalyst; 2025-2026) (2025-08)

- **id**: `apptronik-apollo-gen2-2025`
- **corpus**: private
- **creator**: Apptronik Inc. (Austin, TX, USA); Jeff Cardenas + Nick Paine + Luis Sentis (UT Austin Human Centered Robotics Lab / NASA Valkyrie lineage)
- **disclosure**: Apptronik Inc. (Austin, TX, USA; founded 2016, NASA Valkyrie lineage). Apollo Gen 1 revealed 2023. Apollo Gen 2 (2025) — substantially revised design with improved actuators, dexterity, and runtime. 'Catalyst' embodied-AI software platform (with Google DeepMind Gemini Robotics, 2025). Production-intent partnerships with Mercedes-Benz, GXO Logistics, and others. $350M+ Series A (Feb 2025).
- **ip status**: trade-secret
- **prior art notes**: Apptronik Apollo Gen 2 + Catalyst (Apptronik Austin 2025-2026) is the NASA-Valkyrie-lineage commercial humanoid's next-generation evolution. <1-year-deep public-disclosure prior art (Gen 1 from 2023). Lineage descends from NASA Valkyrie (corpus nasa-valkyrie) + the corpus apptronik-apollo Gen 1 entry; Catalyst uses Google DeepMind Gemini Robotics (corpus gemini-google-deepmind-2023). One of the leading US commercial-humanoid players (with Figure/Optimus/1X/Atlas corpus).

## Sunday Robotics Memo (household humanoid; Tony Zhao + Cheng Chi) (2025-11)

- **id**: `sunday-robotics-memo-2025`
- **corpus**: private
- **creator**: Sunday Robotics (USA); Tony Zhao + Cheng Chi (Stanford ALOHA + Diffusion Policy lineage)
- **disclosure**: Sunday Robotics (USA; founded 2024 by Tony Zhao + Cheng Chi). Memo household humanoid unveiled November 19, 2025. Founding Family Beta launching late 2026; 50 households. $1.15B valuation March 2026. $35M Series B Benchmark + Conviction-led. Tony Zhao = Stanford CS PhD ALOHA + ACT (corpus act-aloha); Cheng Chi = Columbia CS PhD + Stanford Diffusion Policy (corpus diffusion-policy).
- **ip status**: trade-secret
- **prior art notes**: Sunday Robotics Memo (Tony Zhao + Cheng Chi 2024-2025+) is the canonical household humanoid trained on 'zero robot data' via Skill Capture Glove human demonstrations. <1-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from: (1) household-chore humanoids; (2) human-glove-based training methodologies for robot foundation models; (3) ACT-1-class transformer VLA trained without robot demonstration data. Lineage descends from ALOHA (corpus act-aloha; Tony Zhao Stanford 2023) and Diffusion Policy (corpus diffusion-policy; Cheng Chi Columbia/Stanford 2023). The Tony Zhao + Cheng Chi commercial spinout.
