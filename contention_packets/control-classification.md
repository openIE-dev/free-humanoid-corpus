---
title: "control-classification"
parent: "Invalidity Contentions"
nav_order: 46
layout: default
---

# Invalidity Contention Packet — `control-classification`

**Generated:** 2026-05-09  
**Cross-cut tag:** `control-classification`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 1995-09  
**Most recent disclosure:** 2001-10

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-classification`.

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

### 1995-09 — Support Vector Machines (SVM)

- **id:** `svm-cortes-vapnik-1995`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** AT&T Bell Laboratories; Corinna Cortes, Vladimir Vapnik
- **disclosure citation:** Cortes, C., Vapnik, V. 'Support-Vector Networks'. Machine Learning 20(3) 1995. AT&T Bell Laboratories.
- **disclosed subsystems:** `control-machine-learning`, `control-classification`

**Prior art notes:**

> SVM (Cortes-Vapnik Machine Learning 1995) is the foundational margin-maximizing classifier. 30-year-deep public-domain prior art. The dominant ML algorithm pre-2012. Used in many pre-deep-learning robotic-perception systems.

**Sources:**

1. Cortes, C., Vapnik, V. Machine Learning 20(3) 1995.

---

### 2001-10 — Random Forests

- **id:** `random-forest-breiman-2001`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** UC Berkeley; Leo Breiman
- **disclosure citation:** Breiman, L. 'Random Forests'. Machine Learning 45(1) 2001. UC Berkeley.
- **disclosed subsystems:** `control-machine-learning`, `control-classification`, `control-ensemble-method`

**Prior art notes:**

> Random Forests (Breiman Machine Learning 2001) is the foundational ensemble decision-tree algorithm. 24-year-deep public-domain prior art. Used in Microsoft Kinect (round-33) skeletal-tracking 2011 and many pre-deep-learning robotic-perception systems.

**Sources:**

1. Breiman, L. Machine Learning 45(1) 2001.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `073503d`.*
