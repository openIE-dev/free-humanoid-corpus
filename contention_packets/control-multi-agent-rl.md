---
title: "control-multi-agent-rl"
parent: "Invalidity Contentions"
nav_order: 98
layout: default
---

# Invalidity Contention Packet — `control-multi-agent-rl`

**Generated:** 2026-05-14  
**Cross-cut tag:** `control-multi-agent-rl`  
**Entries:** 3 (3 commons-grade, 0 draft)  
**Earliest disclosure:** 2018-06  
**Most recent disclosure:** 2024-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-multi-agent-rl`.

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

### 2018-06 — OpenAI Five (2018-2019; Dota 2 world-champion-defeating RL agent)

- **id:** `openai-five-dota2-2018`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** OpenAI; OpenAI Five team (Greg Brockman + Christopher Berner + Szymon Sidor + Ilya Sutskever et al.)
- **disclosure citation:** OpenAI. OpenAI Five — a team of 5 RL agents playing Dota 2. First public demo June 2018; lost to pro teams at The International 2018; defeated the world-champion team OG in April 2019 (best-of-three). Technical report: Berner et al. 'Dota 2 with Large Scale Deep Reinforcement Learning'. arXiv:1912.06680, December 2019.
- **disclosed subsystems:** `ai-foundation-model`, `control-multi-agent-rl`

**Prior art notes:**

> OpenAI Five (OpenAI 2018-2019; arXiv 1912.06680) is the deep-RL agent team that mastered Dota 2 — long-horizon, partial-information, real-time team play. 7-year-deep academic-publication prior art. Partner result to DeepMind AlphaStar (corpus); uses LSTM (corpus) + PPO (corpus).

**Sources:**

1. arxiv.org/abs/1912.06680

---

### 2019-01 — AlphaStar (DeepMind 2019; StarCraft II grandmaster)

- **id:** `alphastar-deepmind-2019`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** DeepMind (London); Oriol Vinyals + Igor Babuschkin + David Silver team
- **disclosure citation:** Vinyals, O., Babuschkin, I., Czarnecki, W.M., et al. 'Grandmaster level in StarCraft II using multi-agent reinforcement learning'. Nature 575:350-354, October 2019. DeepMind. Public demonstration January 2019.
- **disclosed subsystems:** `ai-foundation-model`, `control-multi-agent-rl`

**Prior art notes:**

> AlphaStar (DeepMind Vinyals et al. Nature 2019) is the foundational grandmaster-level real-time-strategy RL agent. 6-year-deep academic-publication prior art.

**Sources:**

1. Nature 575:350-354, October 2019.

---

### 2024-04 — DeepMind humanoid soccer (Haarnoja et al.)

- **id:** `deepmind-humanoid-soccer-haarnoja-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Google DeepMind; Tuomas Haarnoja, Yuval Tassa, Nicolas Heess + ~25 co-authors
- **disclosure citation:** Haarnoja, T., Moran, B., Lever, G., Huang, S. H., Tirumala, D., Humplik, J., Wulfmeier, M., Tunyasuvunakool, S., Siegel, N. Y., Hafner, R., Bloesch, M., Hartikainen, K., Byravan, A., Hasenclever, L., Tassa, Y., Sadeghi, F., Batchelor, N., Casarini, F., Saliceti, S., Game, C., Sreendra, N., Patel, K., Gwira, M., Huber, A., Hurley, N., Nori, F., Hadsell, R., Heess, N. 'Learning agile soccer skills for a bipedal robot with deep reinforcement learning'. Science Robotics 9(89) April 2024.
- **disclosed subsystems:** `control-rl-policy`, `control-sim-to-real`, `control-multi-agent-rl`, `control-self-play`, `mechanism-bipedal-locomotion`

**Prior art notes:**

> DeepMind humanoid soccer (Haarnoja et al. Science Robotics April 2024) is the canonical end-to-end deep-RL humanoid agility paper. 1-year-deep open-academic prior art for: zero-shot sim-to-real agile humanoid skills (kicking, defending, getting up), multi-agent self-play RL on humanoid hardware, teacher-student distillation for compact deployable policies. Direct shielding for any commercial humanoid claim on dynamic-skill RL training or sim-to-real agile-locomotion transfer. Together with Berkeley Humanoid (round-11), Berkeley Humanoid Lite (round-11), and ToddlerBot (round-11), establishes the open-academic agile-humanoid-RL substrate.

**Sources:**

1. Haarnoja et al. Science Robotics 9(89) 2024.
2. Project page (sites.google.com/view/op3-soccer).

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
