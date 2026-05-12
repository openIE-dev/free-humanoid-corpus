---
title: "control-slam"
parent: "Invalidity Contentions"
nav_order: 133
layout: default
---

# Invalidity Contention Packet — `control-slam`

**Generated:** 2026-05-12  
**Cross-cut tag:** `control-slam`  
**Entries:** 3 (3 commons-grade, 0 draft)  
**Earliest disclosure:** 1992-02  
**Most recent disclosure:** 2016-05

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-slam`.

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

### 1992-02 — ICP (Iterative Closest Point; Besl & McKay 1992)

- **id:** `icp-besl-mckay-1992`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** General Motors Research Laboratories; Paul Besl + Neil McKay
- **disclosure citation:** Besl, P.J., McKay, N.D. 'A Method for Registration of 3-D Shapes'. IEEE Transactions on Pattern Analysis and Machine Intelligence 14(2):239-256, February 1992. General Motors Research Laboratories. (Independent near-simultaneous: Chen & Medioni 1991.)
- **disclosed subsystems:** `ai-foundation-model`, `control-slam`

**Prior art notes:**

> ICP (Besl & McKay GM Research IEEE PAMI 1992) is the foundational 3D point-cloud registration algorithm. 33-year-deep public-domain prior art.

**Sources:**

1. IEEE PAMI 14(2):239-256, 1992.

---

### 2014-07 — LOAM (LIDAR Odometry and Mapping; Zhang & Singh 2014)

- **id:** `loam-zhang-singh-2014`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** Carnegie Mellon University; Ji Zhang + Sanjiv Singh
- **disclosure citation:** Zhang, J., Singh, S. 'LOAM: Lidar Odometry and Mapping in Real-time'. Robotics: Science and Systems (RSS) 2014. Carnegie Mellon University. Won RSS 2014 best-paper-finalist; topped KITTI odometry leaderboard for years.
- **disclosed subsystems:** `ai-foundation-model`, `control-slam`

**Prior art notes:**

> LOAM (Zhang & Singh CMU RSS 2014) is the foundational real-time LIDAR odometry + mapping system. 11-year-deep academic-publication prior art.

**Sources:**

1. Zhang, J., Singh, S. RSS 2014.

---

### 2016-05 — Cartographer (Google Hess et al. 2016; LIDAR SLAM)

- **id:** `cartographer-google-hess-2016`
- **corpus:** open
- **ip status:** open-permissive (Apache 2.0)
- **creator:** Google; Wolfgang Hess + Damon Kohler + Holger Rapp + Daniel Andor
- **disclosure citation:** Hess, W., Kohler, D., Rapp, H., Andor, D. 'Real-Time Loop Closure in 2D LIDAR SLAM'. ICRA 2016. Google. Open-sourced October 2016 under Apache 2.0.
- **disclosed subsystems:** `ai-foundation-model`, `control-slam`

**Prior art notes:**

> Cartographer (Google Hess et al. ICRA 2016) is the foundational open-source LIDAR SLAM system. 9-year-deep open-permissive prior art.

**Sources:**

1. ICRA 2016 paper.
2. github.com/cartographer-project/cartographer

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `4e68247`.*
