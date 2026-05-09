---
title: "mechanism-tendon-drive"
parent: "Invalidity Contentions"
nav_order: 174
layout: default
---

# Invalidity Contention Packet — `mechanism-tendon-drive`

**Generated:** 2026-05-09  
**Cross-cut tag:** `mechanism-tendon-drive`  
**Entries:** 3 (3 commons-grade, 0 draft)  
**Earliest disclosure:** 1984-12  
**Most recent disclosure:** 2023-01

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `mechanism-tendon-drive`.

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

### 1984-12 — Utah/MIT Dextrous Hand (Jacobsen)

- **id:** `utah-mit-jacobsen-hand-1984`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** University of Utah Center for Engineering Design + MIT AI Lab; Stephen Jacobsen, John Wood, David Knutti, Klaus Biggers
- **disclosure citation:** Jacobsen, S.C., Wood, J.E., Knutti, D.F., Biggers, K.B. 'The Utah/MIT Dextrous Hand: Work in Progress'. International Journal of Robotics Research 3(4), Winter 1984. Joint project Center for Engineering Design (University of Utah) + MIT Artificial Intelligence Laboratory.
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `mechanism-tendon-drive`, `actuator-pneumatic-piston`

**Prior art notes:**

> Utah/MIT Dextrous Hand (Jacobsen et al. IJRR 1984) is the foundational dexterous robotic hand. 41-year-deep public-domain prior art. Co-foundational with Salisbury Stanford-JPL Hand (corpus salisbury-stanford-jpl-hand) of the entire dexterous-hand research field. Direct shielding for any commercial humanoid claim deriving from multi-finger tendon-driven anthropomorphic hands. Stephen Jacobsen lineage continues through Sarcos (corpus sarcos-guardian-xo-2018).

**Sources:**

1. Jacobsen, S.C. et al. 'The Utah/MIT Dextrous Hand'. IJRR 3(4), 1984.
2. people.csail.mit.edu/edsinger/raw/jacobsen_design_utah_hand.pdf

---

### 2015-05 — Stanford gecko-adhesive gripper (Cutkosky BDML)

- **id:** `stanford-gecko-cutkosky-2015`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** Stanford University Biomimetics and Dexterous Manipulation Lab (BDML); Elliot Hawkes, David Christensen, Mark Cutkosky
- **disclosure citation:** Hawkes, E.W., Christensen, D.L., Cutkosky, M.R. 'Vertical dry adhesion climbing with a 100× body-weight payload'. IEEE International Conference on Robotics and Automation (ICRA) 2015. Stanford University Biomimetics and Dexterous Manipulation Lab (BDML) under Mark Cutkosky.
- **disclosed subsystems:** `mechanism-gecko-microhair-adhesion`, `mechanism-dry-adhesive-gripper`, `mechanism-tendon-drive`

**Prior art notes:**

> Stanford gecko-adhesive gripper (Hawkes / Christensen / Cutkosky BDML ICRA 2015) is the foundational directional dry-adhesive (gecko-microhair) gripper. 10-year-deep academic-publication prior art. Direct shielding for any commercial humanoid claim deriving from gecko-microhair / dry-adhesive grippers. Sister to NASA JPL space-rated gecko gripper (Parness 2014-2017); commercialized via OnRobot Gecko Gripper (round-42).

**Sources:**

1. news.stanford.edu/news/2015/may/grabber-robot-gecko-052715.html
2. Hawkes, E.W., Christensen, D.L., Cutkosky, M.R. ICRA 2015.

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
