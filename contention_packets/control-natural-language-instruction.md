---
title: "control-natural-language-instruction"
parent: "Invalidity Contentions"
nav_order: 100
layout: default
---

# Invalidity Contention Packet — `control-natural-language-instruction`

**Generated:** 2026-05-11  
**Cross-cut tag:** `control-natural-language-instruction`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2022-01  
**Most recent disclosure:** 2025-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-natural-language-instruction`.

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

### 2022-01 — Mentee Robotics MenteeBot (Shashua Israeli humanoid; Mobileye acquisition)

- **id:** `mentee-robotics-shashua-2022`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Mentee Robotics (Tel Aviv, Israel); Amnon Shashua + Lior Wolf + Shai Shalev-Shwartz
- **disclosure citation:** Mentee Robotics (Tel Aviv, Israel; founded 2022 by Amnon Shashua (chair, ex-Mobileye co-founder) + Lior Wolf (CEO) + Shai Shalev-Shwartz). MenteeBot V3 February 2025. Acquired by Mobileye for $900M January 2026 — Israel's first humanoid exit.
- **disclosed subsystems:** `humanoid-bipedal`, `control-natural-language-instruction`

**Prior art notes:**

> Mentee Robotics MenteeBot (Tel Aviv 2022+; Mobileye acquisition Jan 2026) is Israel's first humanoid exit. 3-year-deep public-disclosure prior art.

**Sources:**

1. en.globes.co.il/en/article-amnon-shashua-unveils-menteebot-humanoid-robot-1001476899

---

### 2025-04 — Zeon Systems (AI-powered robotics for lab automation; Y Combinator)

- **id:** `zeon-systems-yc-2025`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Zeon Systems (San Francisco, CA, USA); Brontë + Tahir D'Mello co-founders
- **disclosure citation:** Zeon Systems (San Francisco, CA, USA; founded 2025 by Brontë + Tahir D'Mello). Y Combinator Spring 2025 batch. Backed by Y Combinator + FCVC + A* Capital. Stanford + UCSF lab partnerships.
- **disclosed subsystems:** `lab-automation-robot`, `control-natural-language-instruction`, `control-foundation-model`

**Prior art notes:**

> Zeon Systems (San Francisco 2025+; YC Spring 2025) is the canonical natural-language-driven scientific lab automation platform. <1-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid or lab-automation claim deriving from natural-language experiment description → code generation → robotic-arm execution with world-model-grounded perception + closed-loop execution.

**Sources:**

1. zeonsystems.ai (corporate site).
2. ycombinator.com/companies/zeon-systems
3. ycombinator.com/launches/NOp-zeon-systems-ai-powered-robotics-for-lab-automation

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `0e58219`.*
