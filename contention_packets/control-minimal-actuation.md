---
title: "control-minimal-actuation"
parent: "Invalidity Contentions"
nav_order: 66
layout: default
---

# Invalidity Contention Packet — `control-minimal-actuation`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-minimal-actuation`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2004-12  
**Most recent disclosure:** 2005-02

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-minimal-actuation`.

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

### 2004-12 — Wisse passive-dynamic walker thesis

- **id:** `wisse-tu-delft-passive-walker-2004`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** TU Delft Biomechanical Engineering; Martijn Wisse + Frans van der Helm
- **disclosure citation:** Wisse, M. 'Essentials of Dynamic Walking: Analysis and Design of Two-Legged Robots'. PhD thesis, Delft University of Technology, December 2004. Adviser: Frans van der Helm. Subsequent: 'Denise' planar walker (2005); 'Mike' McGeer-class walker. Foundational TU Delft passive-dynamic walking research that directly contributed to Collins-Ruina-Tedrake-Wisse Science 2005 (corpus entry round-19).
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-passive-dynamic-walking`, `control-minimal-actuation`

**Prior art notes:**

> Wisse's TU Delft passive-dynamic-walking research (PhD 2004 + Denise/Mike walkers) is the Dutch contribution to the Collins-Ruina-Tedrake-Wisse Science 2005 paper (corpus round-19). 21-year-deep public-domain prior art. Anchors the round-25 TU Delft aggregator entry with a specific paper-level disclosure. Together with McGeer 1990 + Collins 2005, establishes the passive-dynamic walking academic chain that shields any commercial humanoid efficiency claim.

**Sources:**

1. Wisse, M. PhD thesis, TU Delft, December 2004.
2. Wisse, M. + van der Helm, F. various Delft Biomechanical Engineering publications 2003-2010.

---

### 2005-02 — Collins-Ruina-Tedrake-Wisse passive-dynamic walker

- **id:** `collins-ruina-tedrake-wisse-passive-walker-2005`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Cornell + MIT + TU Delft; Steve Collins, Andy Ruina, Russ Tedrake, Martijn Wisse
- **disclosure citation:** Collins, S., Ruina, A., Tedrake, R., Wisse, M. 'Efficient Bipedal Robots Based on Passive-Dynamic Walkers'. Science 307(5712) 18 February 2005. Cornell + MIT + TU Delft. Demonstrated three minimally-actuated bipedal walkers (Cornell Ranger, MIT Toddler, Delft) walking with energetic efficiency comparable to humans, extending McGeer's purely-passive 1990 walker.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-passive-dynamic-walking`, `control-minimal-actuation`

**Prior art notes:**

> Collins-Ruina-Tedrake-Wisse passive-dynamic walking (Science 2005) is the canonical extension of McGeer's 1990 passive walker to level-ground walking with minimal actuation. 20-year-deep public-domain prior art for: minimally-actuated energetically-efficient bipedal walking, COT-driven control optimization. The architectural ancestor of: Cassie / Digit (Agility Robotics 2017+), MIT Cheetah series (Sangbae Kim 2009+), MIT Humanoid (round-8 entry mit-humanoid-2021). Direct shielding for any commercial humanoid claim on energetically-efficient bipedal walking — the 20-year-old efficient-walking academic chain shields any commercial 'we walk like humans' efficiency claim.

**Sources:**

1. Collins et al. Science 307(5712) 18 February 2005.
2. Ruina passive-dynamic walking page (ruina.tam.cornell.edu/research/topics/locomotion_and_robotics).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `46b6329`.*
