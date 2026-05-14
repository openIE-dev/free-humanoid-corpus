---
title: "control-world-model"
parent: "Invalidity Contentions"
nav_order: 157
layout: default
---

# Invalidity Contention Packet — `control-world-model`

**Generated:** 2026-05-14  
**Cross-cut tag:** `control-world-model`  
**Entries:** 3 (3 commons-grade, 0 draft)  
**Earliest disclosure:** 2023-01  
**Most recent disclosure:** 2025-01

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-world-model`.

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

### 2023-01 — DreamerV3 (Danijar Hafner et al. 2023; world-model RL)

- **id:** `dreamer-v3-hafner-2023`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Google DeepMind + University of Toronto; Danijar Hafner + Jurgis Pasukonis + Jimmy Ba + Timothy Lillicrap
- **disclosure citation:** Hafner, D., Pasukonis, J., Ba, J., Lillicrap, T. 'Mastering Diverse Domains through World Models'. arXiv:2301.04104, January 2023. Google DeepMind + University of Toronto. Predecessors: PlaNet (2018), Dreamer (2019), DreamerV2 (2020).
- **disclosed subsystems:** `ai-foundation-model`, `control-world-model`

**Prior art notes:**

> DreamerV3 (Danijar Hafner et al. Google DeepMind + Toronto, arXiv 2301.04104) is the most-effective general-purpose world-model RL algorithm. 2-year-deep public-domain prior art (5-year for the broader Dreamer lineage).

**Sources:**

1. arxiv.org/abs/2301.04104

---

### 2024-02 — Genie (Google DeepMind 2024; foundation world model from video)

- **id:** `genie-deepmind-2024`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** Google DeepMind; Jake Bruce + Michael Dennis + Ashley Edwards + team
- **disclosure citation:** Bruce, J., Dennis, M., Edwards, A., et al. 'Genie: Generative Interactive Environments'. arXiv:2402.15391, February 2024 (ICML 2024 best paper). Google DeepMind. Genie 2 (December 2024, 3D worlds); Genie 3 (2025, real-time interactive).
- **disclosed subsystems:** `ai-foundation-model`, `control-world-model`

**Prior art notes:**

> Genie (Google DeepMind arXiv 2402.15391, ICML 2024 best paper) is the foundational world model trained from unlabeled video. 1-year-deep academic-publication prior art. Directly relevant to robot world models (NVIDIA Cosmos corpus, RoboCat corpus, Sora corpus as 'world simulator').

**Sources:**

1. arxiv.org/abs/2402.15391

---

### 2025-01 — NVIDIA Cosmos

- **id:** `nvidia-cosmos-2025`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** NVIDIA; multi-author research team
- **disclosure citation:** NVIDIA. 'Cosmos World Foundation Model Platform for Physical AI'. arXiv:2501.03575, January 2025. NVIDIA CES 2025 announcement. Open weights via HuggingFace nvidia/Cosmos-* family. Cosmos-Reason2-2B variant subsequently used as the System 2 backbone in GR00T N1.7.
- **disclosed subsystems:** `control-foundation-model-perception`, `control-world-model`, `control-video-generation`, `control-sim-to-real`

**Prior art notes:**

> NVIDIA Cosmos is the canonical world-foundation-model platform for physical AI (NVIDIA CES January 2025). 4-month-deep open-permissive prior art for: video generation + understanding + sim-to-real-transfer foundation models, world-modeling for physical-AI policy training. **Cosmos-Reason2-2B is the System-2 backbone of GR00T N1.7** (round-15 entry); round-17 now resolves that lineage citation. Direct shielding for any commercial humanoid claim on world-model-based policy training or on video-generation-based simulation augmentation.

**Sources:**

1. NVIDIA arXiv:2501.03575 January 2025.
2. NVIDIA CES 2025 announcement (nvidianews.nvidia.com).
3. HuggingFace: huggingface.co/nvidia/Cosmos.
4. GitHub: github.com/NVIDIA/Cosmos.

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
