---
title: "control-policy-gradient"
parent: "Invalidity Contentions"
nav_order: 119
layout: default
---

# Invalidity Contention Packet — `control-policy-gradient`

**Generated:** 2026-05-12  
**Cross-cut tag:** `control-policy-gradient`  
**Entries:** 7 (7 commons-grade, 0 draft)  
**Earliest disclosure:** 1992-05  
**Most recent disclosure:** 2018-01

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-policy-gradient`.

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

### 1992-05 — REINFORCE (Williams 1992; foundational policy-gradient)

- **id:** `williams-reinforce-1992`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Northeastern University; Ronald J. Williams
- **disclosure citation:** Williams, R.J. 'Simple statistical gradient-following algorithms for connectionist reinforcement learning'. Machine Learning 8(3-4):229-256, May 1992. Northeastern University. The foundational policy-gradient algorithm.
- **disclosed subsystems:** `control-policy-gradient`

**Prior art notes:**

> REINFORCE (Williams Northeastern 1992) is the foundational policy-gradient algorithm. 33-year-deep public-domain prior art. Direct shielding for any commercial humanoid claim deriving from policy-gradient RL.

**Sources:**

1. Williams, R.J. Machine Learning 8(3-4):229-256, 1992.

---

### 1999-12 — Policy Gradient Theorem (Sutton et al. 1999)

- **id:** `sutton-policy-gradient-theorem-1999`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** AT&T Labs Research + UMass; Richard Sutton + David McAllester + Satinder Singh + Yishay Mansour
- **disclosure citation:** Sutton, R.S., McAllester, D., Singh, S., Mansour, Y. 'Policy Gradient Methods for Reinforcement Learning with Function Approximation'. NIPS 1999. AT&T Labs Research + University of Massachusetts.
- **disclosed subsystems:** `control-policy-gradient`

**Prior art notes:**

> Policy Gradient Theorem (Sutton et al. NIPS 1999) is the foundational theoretical result for policy-gradient + function approximation. 26-year-deep public-domain prior art.

**Sources:**

1. Sutton, R.S. et al. NIPS 1999.

---

### 2014-06 — Deterministic Policy Gradient (Silver et al. 2014)

- **id:** `silver-deterministic-policy-gradient-2014`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** DeepMind + INRIA; David Silver + Guy Lever + Nicolas Heess + Thomas Degris + Daan Wierstra + Martin Riedmiller
- **disclosure citation:** Silver, D., Lever, G., Heess, N., Degris, T., Wierstra, D., Riedmiller, M. 'Deterministic Policy Gradient Algorithms'. ICML 2014. DeepMind + INRIA.
- **disclosed subsystems:** `control-policy-gradient`

**Prior art notes:**

> Deterministic Policy Gradient (Silver et al. DeepMind ICML 2014) is the direct ancestor of DDPG. 11-year-deep public-domain prior art.

**Sources:**

1. Silver, D. et al. ICML 2014.

---

### 2015-02 — Trust Region Policy Optimization (TRPO)

- **id:** `trpo-schulman-icml-2015`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** UC Berkeley; John Schulman, Sergey Levine, Philipp Moritz, Michael Jordan, Pieter Abbeel
- **disclosure citation:** Schulman, J., Levine, S., Moritz, P., Jordan, M. I., Abbeel, P. 'Trust Region Policy Optimization'. ICML 2015. arXiv:1502.05477. UC Berkeley.
- **disclosed subsystems:** `control-rl-policy`, `control-policy-gradient`

**Prior art notes:**

> TRPO (Schulman et al. ICML 2015) is the direct predecessor of PPO. 10-year-deep public-domain prior art for: trust-region constrained policy gradient. Together with PPO (round-30), establishes the policy-gradient lineage that all modern RL humanoid/quadruped training builds on.

**Sources:**

1. Schulman et al. arXiv:1502.05477 ICML 2015.

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

### 2017-07 — Proximal Policy Optimization (PPO)

- **id:** `ppo-schulman-openai-2017`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** OpenAI; John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, Oleg Klimov
- **disclosure citation:** Schulman, J., Wolski, F., Dhariwal, P., Radford, A., Klimov, O. 'Proximal Policy Optimization Algorithms'. arXiv:1707.06347, July 2017. OpenAI.
- **disclosed subsystems:** `control-rl-policy`, `control-policy-gradient`

**Prior art notes:**

> PPO (Schulman et al. OpenAI 2017) is the dominant RL algorithm in robotics. 8-year-deep public-domain prior art. **Cited 55 times in this corpus alone — the most-cited missing-entry before round-30**. The actual training algorithm of: ANYmal sim-to-real (corpus entry hwangbo-anymal-sim2real), Berkeley Humanoid (round-11), ToddlerBot (round-11), DeepMind humanoid soccer (round-18), MIT Cheetah series (corpus), OpenAI Dactyl (corpus), Hwangbo ANYmal, Tan quadruped sim2real (corpus), every Isaac Gym RL paper. Direct shielding for any commercial humanoid claim on RL-trained policies — PPO is the algorithm the policies are actually trained with.

**Sources:**

1. Schulman et al. arXiv:1707.06347 July 2017.
2. OpenAI Spinning Up implementation (spinningup.openai.com).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `dd66352`.*
