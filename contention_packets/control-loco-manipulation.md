---
title: "control-loco-manipulation"
parent: "Invalidity Contentions"
nav_order: 38
layout: default
---

# Invalidity Contention Packet — `control-loco-manipulation`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-loco-manipulation`  
**Entries:** 4 (4 commons-grade, 0 draft)  
**Earliest disclosure:** 2023-10  
**Most recent disclosure:** 2025-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-loco-manipulation`.

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

### 2023-10 — Habitat 3.0

- **id:** `fair-habitat-3-puig-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** FAIR + Georgia Tech + UIUC; Puig, Mottaghi, Batra, Malik et al.
- **disclosure citation:** Puig, X., Undersander, E., Szot, A., Cote, M. D., Yang, T.-Y., Partsey, R., Desai, R., Clegg, A. W., Hlavac, M., Min, S. Y., Vondruš, T., Gervet, T., Berges, V.-P., Turner, J. M., Maksymets, O., Kira, Z., Kalakrishnan, M., Malik, J., Chaplot, D. S., Jain, U., Batra, D., Rai, A., Mottaghi, R. 'Habitat 3.0: A Co-Habitat for Humans, Avatars and Robots'. ICLR 2024. arXiv:2310.13724. FAIR + Georgia Tech + UIUC.
- **disclosed subsystems:** `control-physics-simulation`, `control-multi-agent-simulation`, `control-human-robot-collaboration`, `control-loco-manipulation`

**Prior art notes:**

> Habitat 3.0 is the canonical academic multi-agent embodied simulator with humanoid avatars (Puig et al. ICLR 2024). 1.5-year-deep open-permissive prior art for: humanoid-and-robot co-simulation, social-navigation tasks where robots interact with human avatars, large-scale (211-house) furnished scene library for embodied AI. Direct shielding for any commercial humanoid claim on training-with-humans-in-simulation or social-navigation policies.

**Sources:**

1. Puig et al. arXiv:2310.13724 ICLR 2024.
2. Project page (aihabitat.org/habitat3).
3. GitHub: github.com/facebookresearch/habitat-lab.

---

### 2024-06 — RoboCasa

- **id:** `robocasa-nasiriany-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** UT Austin + NVIDIA; Soroush Nasiriany, Abhinav Maddukuri, Yuke Zhu et al.
- **disclosure citation:** Nasiriany, S., Maddukuri, A., Zhang, L., Parikh, A., Lo, A., Joshi, A., Mandlekar, A., Zhu, Y. 'RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots'. arXiv:2406.02523, June 2024. RSS 2024. UT Austin + NVIDIA. RoboCasa365 follow-up (OpenReview tQJYKwc3n4) extends to 365 tasks across 2,500 kitchen environments.
- **disclosed subsystems:** `control-physics-simulation`, `control-imitation-learning`, `control-foundation-model-policy`, `control-loco-manipulation`

**Prior art notes:**

> RoboCasa is the canonical generative-AI-augmented household-task simulation framework (UT Austin + NVIDIA, RSS 2024). ~1-year-deep open-permissive prior art for: generative-AI-authored simulation environments at scale, large-scale (>1k hours) demonstration datasets for VLA training, kitchen-scene household-task benchmark suite. Direct shielding for any commercial humanoid claim on 'training data at scale for household manipulation' — RoboCasa365's 1,600 synthetic + 600 human hours establishes the open-academic baseline.

**Sources:**

1. Nasiriany et al. arXiv:2406.02523 June 2024.
2. Project page (robocasa.ai).
3. GitHub: github.com/robocasa/robocasa.
4. RSS 2024 proceedings (robocasa.ai/assets/robocasa_rss24.pdf).

---

### 2025-02 — ToddlerBot

- **id:** `stanford-toddlerbot-2025`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Stanford Robotics Lab; Haochen Shi, Weizhuo Wang, Shuran Song, C. Karen Liu
- **disclosure citation:** Shi, H., Wang, W., Song, S., Liu, C. K. 'ToddlerBot: Open-Source ML-Compatible Humanoid Platform for Loco-Manipulation'. arXiv:2502.00893, February 2025. Conference on Robot Learning (CoRL) 2025 oral. Stanford Robotics Lab.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-arm`, `mechanism-3d-printed-platform`, `control-rl-policy`, `control-imitation-learning`, `control-sim-to-real`, `control-loco-manipulation`

**Prior art notes:**

> ToddlerBot is Stanford's canonical sub-$6k open-hardware ML-compatible humanoid (CoRL 2025 oral). Establishes 1-year-deep open-academic prior art for: integrated loco-manipulation policy training on an open humanoid platform, transferable motor system-ID for sim-to-real without hand-tuning, 30-DoF anthropomorphic full-body at sub-$6k. Direct shielding for any commercial claim on integrated full-body humanoid policy training, particularly any 'one policy controls the whole body' claim. Together with Berkeley Humanoid Lite, establishes the open-academic baseline for sub-$10k humanoid robotics.

**Sources:**

1. Shi, Wang, Song, Liu. arXiv:2502.00893 February 2025.
2. CoRL 2025 proceedings (proceedings.mlr.press/v305/shi25a.html).
3. Project page (toddlerbot.github.io).
4. GitHub: github.com/hshi74/toddlerbot.

---

### 2025-04 — π₀.₅ (Pi-0.5)

- **id:** `physical-intelligence-pi05-2025`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Physical Intelligence; Black et al.
- **disclosure citation:** Black, K., et al. 'π₀.₅: a Vision-Language-Action Model with Open-World Generalization'. arXiv:2504.16054, April 2025. CoRL 2025 (PMLR vol. 305 pp. 17-40, Black25a). Physical Intelligence.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-foundation-model-policy`, `control-co-training`, `control-loco-manipulation`, `control-semantic-subtask-prediction`

**Prior art notes:**

> π₀.₅ is Physical Intelligence's open-world VLA (CoRL 2025 oral). 1-year-deep prior art on: open-world (new-home) zero-shot mobile manipulation, co-training across multi-robot + web + semantic subtask data, long-horizon (10+ minute) household task autonomy. **The most direct prior art for any commercial humanoid claim on 'works in any home out-of-the-box'** — Tesla Optimus, Figure, 1X NEO, Apptronik all market this generalization claim and now face 1-year-deep open-academic anticipation. Lineage: RT-1 → RT-2 → OpenVLA → π₀ → π₀.₅.

**Sources:**

1. Black et al. arXiv:2504.16054 April 2025.
2. CoRL 2025 PMLR v305 Black25a (proceedings.mlr.press/v305/black25a.html).
3. Physical Intelligence pi0.5 paper (pi.website/download/pi05.pdf).
4. Knowledge Insulating VLA follow-up (physicalintelligence.company/download/pi05_KI.pdf).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `6b58593`.*
