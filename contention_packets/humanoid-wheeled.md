---
title: "humanoid-wheeled"
parent: "Invalidity Contentions"
nav_order: 159
layout: default
---

# Invalidity Contention Packet — `humanoid-wheeled`

**Generated:** 2026-05-10  
**Cross-cut tag:** `humanoid-wheeled`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2022-01  
**Most recent disclosure:** 2025-11

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `humanoid-wheeled`.

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

### 2022-01 — Reflex Robotics (NYC wheeled humanoid)

- **id:** `reflex-robotics-mentese-2022`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Reflex Robotics (Brooklyn, NY, USA); Enes Mentese (ex-MIT/Boston Dynamics/Tesla)
- **disclosure citation:** Reflex Robotics (Brooklyn, NY, USA; founded 2022 by Enes Mentese, ex-MIT/Boston Dynamics/Tesla).
- **disclosed subsystems:** `humanoid-wheeled`

**Prior art notes:**

> Reflex Robotics (Brooklyn 2022+) is the NYC-native low-cost wheeled humanoid. 3-year-deep public-disclosure prior art.

**Sources:**

1. techcrunch.com/2024/03/13/reflex-robotics-wheeled-humanoid-is-here-to-grab-you-a-snack/

---

### 2025-11 — Sunday Robotics Memo (household humanoid; Tony Zhao + Cheng Chi)

- **id:** `sunday-robotics-memo-2025`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Sunday Robotics (USA); Tony Zhao + Cheng Chi (Stanford ALOHA + Diffusion Policy lineage)
- **disclosure citation:** Sunday Robotics (USA; founded 2024 by Tony Zhao + Cheng Chi). Memo household humanoid unveiled November 19, 2025. Founding Family Beta launching late 2026; 50 households. $1.15B valuation March 2026. $35M Series B Benchmark + Conviction-led. Tony Zhao = Stanford CS PhD ALOHA + ACT (corpus act-aloha); Cheng Chi = Columbia CS PhD + Stanford Diffusion Policy (corpus diffusion-policy).
- **disclosed subsystems:** `humanoid-wheeled`, `control-foundation-model`, `control-imitation-learning`, `mechanism-skill-capture-glove`

**Prior art notes:**

> Sunday Robotics Memo (Tony Zhao + Cheng Chi 2024-2025+) is the canonical household humanoid trained on 'zero robot data' via Skill Capture Glove human demonstrations. <1-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from: (1) household-chore humanoids; (2) human-glove-based training methodologies for robot foundation models; (3) ACT-1-class transformer VLA trained without robot demonstration data. Lineage descends from ALOHA (corpus act-aloha; Tony Zhao Stanford 2023) and Diffusion Policy (corpus diffusion-policy; Cheng Chi Columbia/Stanford 2023). The Tony Zhao + Cheng Chi commercial spinout.

**Sources:**

1. sunday.ai (corporate site).
2. techcrunch.com/2026/03/12/humanoid-robotics-maker-sunday-reaches-1-15b-valuation-to-build-household-robots/
3. eweek.com/news/sunday-memo-home-robot/
4. siliconangle.com/2025/11/20/sunday-wants-put-robot-every-home-beginning-launch-memo/
5. founded.com/sunday-memo-robot-chores-founders/

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `b980619`.*
