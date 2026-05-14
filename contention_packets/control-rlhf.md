---
title: "control-rlhf"
parent: "Invalidity Contentions"
nav_order: 129
layout: default
---

# Invalidity Contention Packet — `control-rlhf`

**Generated:** 2026-05-14  
**Cross-cut tag:** `control-rlhf`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2022-01  
**Most recent disclosure:** 2022-12

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-rlhf`.

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

### 2022-01 — InstructGPT (Ouyang et al. OpenAI 2022; RLHF-aligned LLM)

- **id:** `instructgpt-ouyang-openai-2022`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** OpenAI; Long Ouyang + Jeff Wu + Xu Jiang + Diogo Almeida + Carroll Wainwright + Pamela Mishkin + ... + Ryan Lowe + Jan Leike + Paul Christiano lineage
- **disclosure citation:** Ouyang, L., Wu, J., Jiang, X., et al. 'Training language models to follow instructions with human feedback'. arXiv:2203.02155, March 2022. OpenAI. The technical predecessor of ChatGPT (released November 2022). Builds on Christiano et al. RLHF (corpus christiano-rlhf-2017).
- **disclosed subsystems:** `ai-foundation-model`, `control-rlhf`

**Prior art notes:**

> InstructGPT (Ouyang et al. OpenAI arXiv 2203.02155) is the RLHF recipe that made LLMs follow instructions — the technical foundation of ChatGPT + every modern chatbot's post-training. 3-year-deep public-domain prior art. Builds on Christiano et al. RLHF (corpus christiano-rlhf-2017); uses PPO (corpus ppo-schulman-openai-2017); applied to GPT-3 (corpus gpt-lineage-openai-2018-2024).

**Sources:**

1. arxiv.org/abs/2203.02155

---

### 2022-12 — Claude (Anthropic; Constitutional-AI-aligned LLM lineage 2022-2026)

- **id:** `claude-anthropic-2021`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Anthropic PBC (San Francisco, CA, USA); Dario Amodei + Daniela Amodei + ex-OpenAI safety/scaling team
- **disclosure citation:** Anthropic PBC (San Francisco, CA, USA; founded 2021 by Dario Amodei + Daniela Amodei + ex-OpenAI researchers). Claude assistant launched 2022; Claude 2 (2023); Claude 3 family Opus/Sonnet/Haiku (March 2024); Claude 3.5 (2024); Claude 4 / Opus 4 family (2025-2026). Constitutional AI: Bai et al. arXiv:2212.08073, December 2022. Also: 'Training a Helpful and Harmless Assistant with RLHF' (2022); the RSP (Responsible Scaling Policy) framework; mechanistic interpretability research.
- **disclosed subsystems:** `ai-foundation-model`, `control-rlhf`

**Prior art notes:**

> Claude (Anthropic San Francisco 2021/2022+) is the Constitutional-AI-aligned frontier LLM lineage. 3-year-deep public-disclosure prior art. Constitutional AI (CAI/RLAIF) extends Christiano RLHF (corpus) + InstructGPT (corpus). One of the three closed-frontier-LLM labs.

**Sources:**

1. anthropic.com (corporate site).
2. arxiv.org/abs/2212.08073 (Constitutional AI paper).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `4abb724`.*
