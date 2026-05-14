---
title: "rl-infrastructure"
parent: "Invalidity Contentions"
nav_order: 248
layout: default
---

# Invalidity Contention Packet — `rl-infrastructure`

**Generated:** 2026-05-14  
**Cross-cut tag:** `rl-infrastructure`  
**Entries:** 8 (8 commons-grade, 0 draft)  
**Earliest disclosure:** 2004-01  
**Most recent disclosure:** 2023-10

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `rl-infrastructure`.

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

### 2004-01 — Gazebo (foundational ROS-integrated robotics simulator)

- **id:** `gazebo-koenig-howard-2004`
- **corpus:** open
- **ip status:** open-permissive (Apache 2.0)
- **creator:** USC + Open Source Robotics Foundation; Nathan Koenig + Andrew Howard
- **disclosure citation:** Koenig, N., Howard, A. 'Design and use paradigms for Gazebo, an open-source multi-robot simulator'. IROS 2004. USC. Subsequent: Open Source Robotics Foundation maintainership; Ignition Gazebo (now Gazebo Sim) rewrite 2019+.
- **disclosed subsystems:** `rl-infrastructure`, `simulator`

**Prior art notes:**

> Gazebo (Koenig + Howard USC 2004+) is the foundational ROS-integrated robotics simulator. 21-year-deep open-permissive prior art.

**Sources:**

1. gazebosim.org
2. Koenig + Howard IROS 2004.

---

### 2013-11 — CoppeliaSim (formerly V-REP; Rohmer Coppelia 2013)

- **id:** `coppeliasim-vrep-rohmer-2013`
- **corpus:** private
- **ip status:** trade-secret (commercial; free educational)
- **creator:** Coppelia Robotics AG (Zurich, Switzerland); Eric Rohmer + Surya Singh + Marc Freese
- **disclosure citation:** Rohmer, E., Singh, S.P.N., Freese, M. 'V-REP: A Versatile and Scalable Robot Simulation Framework'. IROS 2013. Coppelia Robotics AG (Zurich, Switzerland). Renamed CoppeliaSim 2019.
- **disclosed subsystems:** `rl-infrastructure`, `simulator`

**Prior art notes:**

> CoppeliaSim / V-REP (Coppelia Robotics Zurich 2013+) is the alternative-to-Gazebo robotics simulator. 12-year-deep public-disclosure prior art.

**Sources:**

1. coppeliarobotics.com
2. Rohmer + Singh + Freese IROS 2013.

---

### 2016-04 — OpenAI Gym (foundational RL benchmark library)

- **id:** `openai-gym-brockman-2016`
- **corpus:** open
- **ip status:** open-permissive (MIT)
- **creator:** OpenAI; Greg Brockman + John Schulman + Wojciech Zaremba + team
- **disclosure citation:** Brockman, G., Cheung, V., Pettersson, L., Schneider, J., Schulman, J., Tang, J., Zaremba, W. 'OpenAI Gym'. arXiv:1606.01540, April 2016. OpenAI. Subsequent: Gymnasium (Farama Foundation 2022 maintained fork).
- **disclosed subsystems:** `rl-infrastructure`

**Prior art notes:**

> OpenAI Gym (OpenAI 2016+; Gymnasium 2022 fork) is the foundational RL benchmark library. 9-year-deep open-permissive prior art.

**Sources:**

1. arxiv.org/abs/1606.01540
2. github.com/openai/gym

---

### 2017-01 — Wandelbots Tracepen ('Windows for Robots')

- **id:** `wandelbots-2017`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Wandelbots (Dresden, Germany); TU Dresden 7-co-founder team
- **disclosure citation:** Wandelbots (Dresden, Germany; founded 2017 by Christian Piacht + Maria Piacht + Georg Püschel + Sebastian Werner + Jan Falkenberg + Giang Nguyen + Christoph Biering, TU Dresden). ~$123M raised from Insight + Microsoft + Next47.
- **disclosed subsystems:** `rl-infrastructure`, `control-no-code-programming`

**Prior art notes:**

> Wandelbots (Dresden 2017+) is the Tracepen no-code robot programming category-definer. 8-year-deep public-disclosure prior art.

**Sources:**

1. xpert.digital/en/robotics-start-up/

---

### 2017-05 — OpenAI Baselines (reference RL algorithm implementations)

- **id:** `openai-baselines-2017`
- **corpus:** open
- **ip status:** open-permissive (MIT)
- **creator:** OpenAI; subsequent Stable Baselines3 by Antonin Raffin
- **disclosure citation:** OpenAI. Baselines repository launched May 2017. Reference implementations of DQN + PPO + TRPO + DDPG + A2C + ACKTR + GAIL by experts. Subsequent: Stable Baselines (Antonin Raffin 2018+) and Stable Baselines3 (2020+).
- **disclosed subsystems:** `rl-infrastructure`

**Prior art notes:**

> OpenAI Baselines + Stable Baselines3 (OpenAI 2017+; Raffin 2018+) are the canonical RL reference implementations. 8-year-deep open-permissive prior art.

**Sources:**

1. github.com/openai/baselines
2. github.com/DLR-RM/stable-baselines3

---

### 2017-12 — NVIDIA Isaac Platform (2017+; the GPU-robotics ecosystem)

- **id:** `nvidia-isaac-platform-2017`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** NVIDIA Corporation (Santa Clara, CA, USA); Jensen Huang + Deepu Talla (Robotics + Edge AI VP)
- **disclosure citation:** NVIDIA Corporation. Isaac SDK first announced December 2017 (CES 2018). Isaac Sim (PhysX-based + Omniverse-integrated, ~2019). Isaac Gym (massively-parallel GPU RL, 2021). Isaac Lab (open-source RL framework, 2023, successor to Isaac Gym). Isaac ROS (ROS 2 GPU packages). Jetson edge-AI compute modules (TX1 2015 → TX2 → Xavier → Orin → Thor).
- **disclosed subsystems:** `rl-infrastructure`, `ai-foundation-model`

**Prior art notes:**

> NVIDIA Isaac Platform (NVIDIA Corporation, 2015 Jetson / 2017 Isaac SDK / 2019 Isaac Sim / 2021 Isaac Gym / 2023 Isaac Lab / 2025 GR00T + Cosmos) is the GPU-robotics ecosystem — the dominant robotics-infrastructure stack. 10-year-deep public-disclosure prior art.

**Sources:**

1. NVIDIA Isaac + Jetson product documentation.

---

### 2021-06 — Waabi (Urtasun generative-AI neural simulator AV)

- **id:** `waabi-urtasun-2021`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Waabi Innovation Inc. (Toronto, Canada); Raquel Urtasun (ex-Uber ATG; U-Toronto faculty)
- **disclosure citation:** Waabi Innovation Inc. (Toronto, Canada; founded 2021 by Raquel Urtasun, ex-Uber ATG Toronto head + University of Toronto faculty). $750M+$250M milestone funding (combined ~$1B by 2025).
- **disclosed subsystems:** `autonomous-vehicle`, `rl-infrastructure`

**Prior art notes:**

> Waabi (Toronto 2021+; ~$1B raised) is the most architecturally-distinct AV company (generative-AI simulation-first). 4-year-deep public-disclosure prior art.

**Sources:**

1. utoronto.ca/news/self-driving-startup-waabi-makes-global-headlines

---

### 2023-10 — Meta FAIR robotics (Habitat 3.0 + Spot studies)

- **id:** `meta-fair-robotics-2023`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Meta FAIR (Menlo Park, CA, USA); Dhruv Batra + Yann LeCun advisor
- **disclosure citation:** Meta FAIR (Menlo Park, CA, USA; Dhruv Batra + Yann LeCun advisor). Habitat 3.0 simulator (humans + humanoids + robots together) 2023. Spot-based real-world retrieval studies 2024-2025. Open-source tools release 2025.
- **disclosed subsystems:** `ai-foundation-model`, `rl-infrastructure`

**Prior art notes:**

> Meta FAIR robotics (Menlo Park 2023+) is the Meta robotics research + open-source tooling push. 2-year-deep open-permissive prior art.

**Sources:**

1. therobotreport.com/metas-fair-team-releases-3-tools-for-robotics-researchers/

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
