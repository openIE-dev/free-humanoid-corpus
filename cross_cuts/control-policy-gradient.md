---
title: control-policy-gradient
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-policy-gradient`

**2 corpus entries disclose this subsystem.**

Earliest disclosure: 2015-02

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Trust Region Policy Optimization (TRPO) (2015-02)

- **id**: `trpo-schulman-icml-2015`
- **corpus**: academic
- **creator**: UC Berkeley; John Schulman, Sergey Levine, Philipp Moritz, Michael Jordan, Pieter Abbeel
- **disclosure**: Schulman, J., Levine, S., Moritz, P., Jordan, M. I., Abbeel, P. 'Trust Region Policy Optimization'. ICML 2015. arXiv:1502.05477. UC Berkeley.
- **ip status**: public-domain
- **prior art notes**: TRPO (Schulman et al. ICML 2015) is the direct predecessor of PPO. 10-year-deep public-domain prior art for: trust-region constrained policy gradient. Together with PPO (round-30), establishes the policy-gradient lineage that all modern RL humanoid/quadruped training builds on.

## Proximal Policy Optimization (PPO) (2017-07)

- **id**: `ppo-schulman-openai-2017`
- **corpus**: academic
- **creator**: OpenAI; John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, Oleg Klimov
- **disclosure**: Schulman, J., Wolski, F., Dhariwal, P., Radford, A., Klimov, O. 'Proximal Policy Optimization Algorithms'. arXiv:1707.06347, July 2017. OpenAI.
- **ip status**: public-domain
- **prior art notes**: PPO (Schulman et al. OpenAI 2017) is the dominant RL algorithm in robotics. 8-year-deep public-domain prior art. **Cited 55 times in this corpus alone — the most-cited missing-entry before round-30**. The actual training algorithm of: ANYmal sim-to-real (corpus entry hwangbo-anymal-sim2real), Berkeley Humanoid (round-11), ToddlerBot (round-11), DeepMind humanoid soccer (round-18), MIT Cheetah series (corpus), OpenAI Dactyl (corpus), Hwangbo ANYmal, Tan quadruped sim2real (corpus), every Isaac Gym RL paper. Direct shielding for any commercial humanoid claim on RL-trained policies — PPO is the algorithm the policies are actually trained with.
