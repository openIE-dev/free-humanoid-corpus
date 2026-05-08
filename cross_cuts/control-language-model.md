---
title: control-language-model
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-language-model`

**4 corpus entries disclose this subsystem.**

Earliest disclosure: 2018-10

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

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
