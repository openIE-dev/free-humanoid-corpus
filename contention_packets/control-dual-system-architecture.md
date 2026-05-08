---
title: "control-dual-system-architecture"
parent: "Invalidity Contentions"
nav_order: 26
layout: default
---

# Invalidity Contention Packet — `control-dual-system-architecture`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-dual-system-architecture`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2025-02  
**Most recent disclosure:** 2025-03

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-dual-system-architecture`.

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

### 2025-02 — Figure Helix

- **id:** `figure-helix-2025`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Figure AI Inc.
- **disclosure citation:** Figure AI Inc. 'Helix: A Vision-Language-Action Model for Generalist Humanoid Control'. Public reveal February 2025 via figure.ai/news/helix. Subsequent disclosures: 'Helix Accelerating Real-World Logistics' (figure.ai/news/helix-logistics) and Hacker News + Robot Report coverage. No academic publication; trade-secret commercial VLA.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-foundation-model-policy`, `control-dual-system-architecture`, `control-high-rate-continuous-control`, `control-bimanual-manipulation`, `control-multi-robot-coordination`

**Prior art notes:**

> Helix is Figure AI's canonical 2025 commercial humanoid VLA. Public-disclosure surface (corporate blog + demo videos + Hacker News + Robot Report coverage) reveals architecture (S1/S2 dual-system, 35-DoF/200Hz, ~500hr teleop training) but withholds neural-network specifics, training-data composition, fine-tuning recipe, and policy-evaluation metrics. The capability set claimed is fully covered by deep open academic prior art chains: (1) S1/S2 dual-system architecture is shared with NVIDIA GR00T N1 (round-15 entry, released within weeks; the cognitive-science S1/S2 pattern dates to Kahneman 'Thinking Fast and Slow' 2011); (2) high-rate continuous VLA control was demonstrated by π₀ (round-12, October 2024) and π₀.₅ (round-12, April 2025) in diffusion/flow-matching form; (3) onboard low-power VLA inference is anticipated by OpenVLA-OFT (round-12, parallel decoding + 26× throughput); (4) multi-robot collaboration is anticipated by ROS 2 (round-13, real-time multi-vehicle middleware) and the Mobile ALOHA / ACT bimanual lineage. Direct shielding for any Helix or Helix-derivative commercial-IP claim.

**Sources:**

1. Figure AI 'Helix' announcement (figure.ai/news/helix), February 2025.
2. Figure AI 'Helix Accelerating Real-World Logistics' (figure.ai/news/helix-logistics), 2025.
3. Robot Report coverage (therobotreport.com/figure-humanoid-robots-demonstrate-helix-model-household-chores/).
4. Hacker News discussion thread (news.ycombinator.com/item?id=43115079).

---

### 2025-03 — NVIDIA Isaac GR00T N1

- **id:** `nvidia-groot-n1-2025`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** NVIDIA; multi-author research team
- **disclosure citation:** NVIDIA. 'GR00T N1: An Open Foundation Model for Generalist Humanoid Robots'. arXiv:2503.14734, March 2025. NVIDIA GTC 2025 announcement. Open commercial license; open weights via HuggingFace nvidia/GR00T-N1-2B. Successor versions N1.6 (full-body) and N1.7 (Cosmos-Reason2 + EgoScale 20K-hour egocentric pre-training) released subsequently.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-foundation-model-policy`, `control-dual-system-architecture`, `control-egocentric-video-pretraining`, `control-cross-embodiment`

**Prior art notes:**

> NVIDIA GR00T N1 is the canonical first open commercial-licensed humanoid foundation model (GTC March 2025). 2-month-deep open prior art for: dual-system S1/S2 humanoid VLA, egocentric-human-video pre-training at scale, NVIDIA Isaac platform integration. Direct architectural sibling of Figure Helix (round-15 entry). Both adopt the dual-system pattern from cognitive science. The N1.7 EgoScale 20K-hour pre-training corpus is itself prior art for any commercial humanoid claim on egocentric-video-trained policy datasets. Direct shielding for any commercial humanoid VLA claim.

**Sources:**

1. arXiv:2503.14734 March 2025.
2. NVIDIA Newsroom announcement (nvidianews.nvidia.com/news/nvidia-isaac-gr00t-n1-open-humanoid-robot-foundation-model-simulation-frameworks).
3. HuggingFace: huggingface.co/nvidia/GR00T-N1-2B.
4. GitHub: github.com/NVIDIA/Isaac-GR00T (versions through N1.7).
5. N1.7 model card (huggingface.co/blog/nvidia/gr00t-n1-7).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `bf892af`.*
