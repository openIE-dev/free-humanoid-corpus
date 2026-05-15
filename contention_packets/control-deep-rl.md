---
title: "control-deep-rl"
parent: "Invalidity Contentions"
nav_order: 55
layout: default
---

# Invalidity Contention Packet — `control-deep-rl`

**Generated:** 2026-05-15  
**Cross-cut tag:** `control-deep-rl`  
**Entries:** 3 (3 commons-grade, 0 draft)  
**Earliest disclosure:** 2013-12  
**Most recent disclosure:** 2018-01

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-deep-rl`.

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

### 2013-12 — Deep Q-Network (DQN)

- **id:** `dqn-mnih-deepmind-2013`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** DeepMind; Volodymyr Mnih, Koray Kavukcuoglu, David Silver et al.
- **disclosure citation:** Mnih, V., Kavukcuoglu, K., Silver, D., Graves, A., Antonoglou, I., Wierstra, D., Riedmiller, M. 'Playing Atari with Deep Reinforcement Learning'. NeurIPS 2013 workshop; arXiv:1312.5602. Subsequent: 'Human-level control through deep reinforcement learning' Nature 518 2015. DeepMind.
- **disclosed subsystems:** `control-rl-policy`, `control-q-learning`, `control-deep-rl`

**Prior art notes:**

> DQN (Mnih et al. DeepMind Nature 2015) is the foundational deep reinforcement learning paper. 12-year-deep public-domain prior art. The architectural ancestor of every modern deep RL system including TRPO + PPO + SAC + every RL humanoid training. Direct shielding for any commercial humanoid claim that trains policies via deep RL.

**Sources:**

1. Mnih et al. arXiv:1312.5602 NeurIPS 2013.
2. Mnih et al. Nature 518 2015 ('Human-level control through deep reinforcement learning').

---

### 2015-09 — DDPG (Deep Deterministic Policy Gradient; Lillicrap et al. 2015)

- **id:** `lillicrap-ddpg-2015`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** DeepMind; Lillicrap + Hunt + Pritzel + Heess + Erez + Tassa + Silver + Wierstra
- **disclosure citation:** Lillicrap, T.P., Hunt, J.J., Pritzel, A., Heess, N., Erez, T., Tassa, Y., Silver, D., Wierstra, D. 'Continuous control with deep reinforcement learning'. arXiv:1509.02971, ICLR 2016. DeepMind.
- **disclosed subsystems:** `control-policy-gradient`, `control-deep-rl`

**Prior art notes:**

> DDPG (Lillicrap et al. DeepMind 2015) is the foundational deep-network continuous-control RL algorithm. 10-year-deep public-domain prior art.

**Sources:**

1. arxiv.org/abs/1509.02971

---

### 2018-01 — Soft Actor-Critic (SAC; Haarnoja et al. 2018)

- **id:** `haarnoja-soft-actor-critic-2018`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** UC Berkeley; Tuomas Haarnoja + Aurick Zhou + Pieter Abbeel + Sergey Levine
- **disclosure citation:** Haarnoja, T., Zhou, A., Abbeel, P., Levine, S. 'Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor'. ICML 2018, arXiv:1801.01290. UC Berkeley.
- **disclosed subsystems:** `control-policy-gradient`, `control-deep-rl`

**Prior art notes:**

> SAC (Haarnoja et al. UC Berkeley ICML 2018) is the canonical maximum-entropy off-policy actor-critic. 7-year-deep public-domain prior art.

**Sources:**

1. arxiv.org/abs/1801.01290

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `cd2f551`.*
