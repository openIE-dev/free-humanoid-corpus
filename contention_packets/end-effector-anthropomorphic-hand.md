---
title: "end-effector-anthropomorphic-hand"
parent: "Invalidity Contentions"
nav_order: 123
layout: default
---

# Invalidity Contention Packet — `end-effector-anthropomorphic-hand`

**Generated:** 2026-05-09  
**Cross-cut tag:** `end-effector-anthropomorphic-hand`  
**Entries:** 3 (3 commons-grade, 0 draft)  
**Earliest disclosure:** 2014-05  
**Most recent disclosure:** 2023-01

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `end-effector-anthropomorphic-hand`.

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

### 2014-05 — DEKA / Mobius Bionics LUKE Arm

- **id:** `deka-mobius-luke-arm-2014`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** DEKA Research and Development Corporation (Manchester, NH, USA); Dean Kamen; DARPA Revolutionizing Prosthetics; commercialized as Mobius Bionics
- **disclosure citation:** DEKA Research and Development Corporation (Manchester, NH, USA; Dean Kamen). DARPA Revolutionizing Prosthetics program 2006-2014. FDA clearance May 2014. Mobius Bionics commercial launch July 2016. Named 'LUKE' after Star Wars (Luke Skywalker's prosthetic arm).
- **disclosed subsystems:** `end-effector-anthropomorphic-hand`, `exoskeleton-upper-limb`, `actuator-electric`, `control-multi-modal-user-input`

**Prior art notes:**

> DEKA / Mobius Bionics LUKE Arm (DEKA Manchester NH 2014; Mobius Bionics 2016) is the first FDA-cleared integrated multi-joint upper-extremity prosthesis. 11-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from integrated multi-joint upper-extremity prostheses. DARPA RP outcome; sister to APL MPL (corpus apl-mpl-revolutionizing-prosthetics-2009).

**Sources:**

1. darpa.mil/news/2016/mobius-bionics-luke-arms-walter-reed
2. darpa.mil/about/innovation-timeline/revolutionizing-prosthetics

---

### 2018-01 — Inspire-Robots RH56 5-finger 6-DoF dexterous hand

- **id:** `inspire-robots-rh56-2018`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Inspire-Robots Co., Ltd. (Beijing, China)
- **disclosure citation:** Inspire-Robots Co., Ltd. (Beijing, China). RH56 series 5-finger 6-DoF dexterous hand commercial reveal ~2018. Used by Unitree G1 / H2, Fourier GR-1, and many other Chinese commercial humanoids.
- **disclosed subsystems:** `end-effector-anthropomorphic-hand`, `actuator-electric`, `sensing-tactile-distributed`

**Prior art notes:**

> Inspire-Robots RH56 (Beijing 2018+) is the widely-deployed Chinese 5-finger 6-DoF anthropomorphic hand used by Unitree, Fourier, and many other Chinese commercial humanoids. 7-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from 5-finger 6-DoF Chinese commercial dexterous hands. Together with Linkerbot Linker Hand (round-44), establishes the Chinese hand-supplier prior-art chain.

**Sources:**

1. en.inspire-robots.com/wp-content/uploads/2024/02/INSPIRE-ROBOTS-THE-DEXTEROUS-HAND-RH56-SERIES-USER-MANUAL.pdf

---

### 2023-01 — Linkerbot Linker Hand (Beijing)

- **id:** `linkerbot-linker-hand-beijing-2023`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Linkerbot Co., Ltd. (Beijing, China); Alex Zhou Yong (周永) founder
- **disclosure citation:** Linkerbot Co., Ltd. (Beijing, China). Founded 2023 by Alex Zhou Yong (周永). Linker Hand product family ranges 6-42 DoF across all three mainstream dexterous-hand actuation technologies (linkage transmission, tendon drive, direct drive). Series B+ closed early May 2026 at USD 3B valuation; next round targeting USD 6B (May 2026). Early backers: Ant Group, HongShan Group. Latest investors: Zhongguancun Science Park Fund, Bank of China Asset Management, Fosun Capital.
- **disclosed subsystems:** `end-effector-anthropomorphic-hand`, `mechanism-tendon-drive`, `mechanism-linkage-drive`, `mechanism-direct-drive`, `actuator-electric`

**Prior art notes:**

> Linkerbot Linker Hand (Beijing 2023+) is the global volume-leader in high-DoF dexterous hands per Reuters (>80% market share by volume). 2-3-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from high-DoF anthropomorphic hand product families spanning linkage / tendon / direct-drive actuation, or from dedicated-hand supplier business models. The Chinese hand-specialist complement to corpus humanoid-platform entries (Unitree, Fourier, AgiBot, Astribot, Galbot, etc.). Lineage descends from foundational anthropomorphic-hand prior art: Belgrade-USC Hand (round-42 belgrade-usc-tomovic-bekey-hand-1963), Shadow Dexterous Hand (corpus shadow-dexterous-hand), Allegro Hand (corpus allegro-hand-wonik-simlab-2014), DLR Hand II (corpus dlr-hand-ii).

**Sources:**

1. linkerbot.cn/index (corporate site).
2. thenextweb.com/news/linkerbot-china-robot-hand-6-billion-valuation
3. scmp.com/tech/tech-trends/article/3344242 (South China Morning Post).
4. interestingengineering.com/ai-robotics/china-linkerbot-robotic-hands-human-skills
5. Reuters market-share reporting (cited in TNW and SCMP).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `bd98079`.*
