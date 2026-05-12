---
title: "control-llm-reasoning"
parent: "Invalidity Contentions"
nav_order: 81
layout: default
---

# Invalidity Contention Packet — `control-llm-reasoning`

**Generated:** 2026-05-12  
**Cross-cut tag:** `control-llm-reasoning`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2022-01  
**Most recent disclosure:** 2024-01

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-llm-reasoning`.

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

### 2022-01 — Chain-of-Thought Prompting (Wei et al. Google 2022)

- **id:** `chain-of-thought-wei-google-2022`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Google Research / Google Brain; Jason Wei + Xuezhi Wang + Dale Schuurmans + Maarten Bosma + Brian Ichter + Fei Xia + Ed Chi + Quoc Le + Denny Zhou
- **disclosure citation:** Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q., Zhou, D. 'Chain-of-Thought Prompting Elicits Reasoning in Large Language Models'. arXiv:2201.11903, NeurIPS 2022. Google Research / Google Brain. Related: Kojima et al. 'Large Language Models are Zero-Shot Reasoners' ('Let's think step by step', 2022).
- **disclosed subsystems:** `ai-foundation-model`, `control-llm-reasoning`

**Prior art notes:**

> Chain-of-Thought Prompting (Wei et al. Google arXiv 2201.11903) is the discovery that prompting an LLM to 'show its work' dramatically improves reasoning — the foundation of LLM reasoning + agentic workflows + inference-time-compute reasoning models. 3-year-deep public-domain prior art. Foundational to LLM-driven robot task planning (SayCan/PaLM-E/Eureka corpus).

**Sources:**

1. arxiv.org/abs/2201.11903

---

### 2024-01 — AlphaProof + AlphaGeometry (DeepMind 2024; AI at IMO silver-medal level)

- **id:** `alphaproof-alphageometry-deepmind-2024`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** Google DeepMind; Trieu H. Trinh + Yuhuai Wu + Quoc Le (AlphaGeometry); + AlphaProof team
- **disclosure citation:** Trinh, T.H., Wu, Y., Le, Q.V., He, H., Luong, T. 'Solving olympiad geometry without human demonstrations'. Nature 625:476-482, January 2024 (AlphaGeometry). AlphaProof + AlphaGeometry 2 announced July 2024 — together solved 4 of 6 problems at the 2024 International Mathematical Olympiad, equivalent to a silver medal. Google DeepMind.
- **disclosed subsystems:** `ai-foundation-model`, `control-llm-reasoning`

**Prior art notes:**

> AlphaProof + AlphaGeometry (DeepMind 2024; Nature 2024) are AI systems solving olympiad-level mathematics at IMO silver-medal level. 1-2-year-deep academic-publication prior art. AlphaZero (corpus) + Gemini (corpus) applied to formal mathematics; part of DeepMind's AlphaX-for-science lineage.

**Sources:**

1. Nature 625:476-482, January 2024 (AlphaGeometry).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `dd66352`.*
