---
title: "control-language-model"
parent: "Invalidity Contentions"
nav_order: 49
layout: default
---

# Invalidity Contention Packet — `control-language-model`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-language-model`  
**Entries:** 4 (3 commons-grade, 1 draft)  
**Earliest disclosure:** 2018-10  
**Most recent disclosure:** 2024-10

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-language-model`.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `94b7a2a`.*
