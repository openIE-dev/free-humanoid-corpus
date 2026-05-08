---
title: "control-foundation-model"
parent: "Invalidity Contentions"
nav_order: 34
layout: default
---

# Invalidity Contention Packet — `control-foundation-model`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-foundation-model`  
**Entries:** 3 (3 commons-grade, 0 draft)  
**Earliest disclosure:** 2017-06  
**Most recent disclosure:** 2023-07

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `46e9af2`.*
