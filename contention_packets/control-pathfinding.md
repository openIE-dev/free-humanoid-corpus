---
title: "control-pathfinding"
parent: "Invalidity Contentions"
nav_order: 85
layout: default
---

# Invalidity Contention Packet — `control-pathfinding`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-pathfinding`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 1968-07  
**Most recent disclosure:** 1995-05

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-pathfinding`.

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

### 1968-07 — A* search algorithm

- **id:** `a-star-hart-nilsson-raphael-1968`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** SRI International; Peter Hart, Nils Nilsson, Bertram Raphael
- **disclosure citation:** Hart, P. E., Nilsson, N. J., Raphael, B. 'A Formal Basis for the Heuristic Determination of Minimum Cost Paths'. IEEE Transactions on Systems Science and Cybernetics 4(2) 1968. Stanford Research Institute (now SRI International).
- **disclosed subsystems:** `control-graph-search`, `control-pathfinding`, `control-heuristic-search`

**Prior art notes:**

> A* (Hart-Nilsson-Raphael IEEE T-SSC 1968) is the foundational heuristic graph-search algorithm. 57-year-deep public-domain prior art. Originally developed for SRI Shakey (the world's first general-purpose mobile robot). The substrate of every navigation + planning + autorouting + path-finding system.

**Sources:**

1. Hart, P. E., Nilsson, N. J., Raphael, B. IEEE T-SSC 4(2) 1968.

---

### 1995-05 — D* dynamic replanning algorithm (Stentz)

- **id:** `stentz-cmu-d-star-1995`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Carnegie Mellon University Robotics Institute; Anthony Stentz
- **disclosure citation:** Stentz, A. 'The Focussed D* Algorithm for Real-Time Replanning'. IJCAI 1995. Carnegie Mellon University Robotics Institute. Subsequent: 'Optimal and Efficient Path Planning for Partially-Known Environments'. ICRA 1994 (the foundational D* paper). Subsequent extension: D* Lite (Koenig + Likhachev 2002).
- **disclosed subsystems:** `control-graph-search`, `control-dynamic-replanning`, `control-pathfinding`

**Prior art notes:**

> D* (Stentz CMU 1994/1995) is the foundational dynamic-replanning algorithm. 30-year-deep public-domain prior art. Direct extension of A* (round-33) for changing environments. Deployed in CMU Boss (DARPA Urban Challenge winner 2007), Mars rovers, every autonomous-vehicle stack. Direct shielding for any commercial humanoid claim using dynamic-replanning navigation.

**Sources:**

1. Stentz, A. ICRA 1994.
2. Stentz, A. IJCAI 1995 (Focussed D*).
3. Koenig, S., Likhachev, M. 'D* Lite' AAAI 2002.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `69278e1`.*
