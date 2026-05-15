---
title: "control-dynamics"
parent: "Invalidity Contentions"
nav_order: 60
layout: default
---

# Invalidity Contention Packet — `control-dynamics`

**Generated:** 2026-05-15  
**Cross-cut tag:** `control-dynamics`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 1788-01  
**Most recent disclosure:** 1987-01

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-dynamics`.

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

### 1788-01 — Lagrangian Mechanics (Joseph-Louis Lagrange 1788; foundation of robot dynamics)

- **id:** `lagrangian-mechanics-1788`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Joseph-Louis Lagrange (Italian-French mathematician); Académie des Sciences
- **disclosure citation:** Lagrange, J.-L. 'Mécanique Analytique'. Paris, 1788. Reformulated Newtonian mechanics in terms of generalized coordinates + the Lagrangian L = T - V (kinetic minus potential energy) + the principle of least action.
- **disclosed subsystems:** `control-dynamics`

**Prior art notes:**

> Lagrangian Mechanics (Joseph-Louis Lagrange, 'Mécanique Analytique' 1788) is the foundational formulation used in every robot's equations of motion. 237-year-deep public-domain prior art.

**Sources:**

1. Lagrange, J.-L. 'Mécanique Analytique'. Paris, 1788.

---

### 1987-01 — Featherstone Rigid Body Dynamics Algorithms (1987)

- **id:** `featherstone-rigid-body-dynamics-1987`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** University of Edinburgh / Australian National University; Roy Featherstone
- **disclosure citation:** Featherstone, R. 'Robot Dynamics Algorithms'. Kluwer Academic, 1987. Extended: 'Rigid Body Dynamics Algorithms'. Springer, 2008. University of Edinburgh / Australian National University. The foundational O(n) articulated-body dynamics algorithm.
- **disclosed subsystems:** `control-dynamics`

**Prior art notes:**

> Featherstone Rigid Body Dynamics Algorithms (Edinburgh / ANU 1987, 2008) is the foundational O(n) articulated-body dynamics algorithm. 38-year-deep public-domain prior art.

**Sources:**

1. Featherstone, R. 'Rigid Body Dynamics Algorithms'. Springer 2008.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `cd2f551`.*
