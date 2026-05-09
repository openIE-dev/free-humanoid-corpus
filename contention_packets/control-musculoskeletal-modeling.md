---
title: "control-musculoskeletal-modeling"
parent: "Invalidity Contentions"
nav_order: 87
layout: default
---

# Invalidity Contention Packet — `control-musculoskeletal-modeling`

**Generated:** 2026-05-09  
**Cross-cut tag:** `control-musculoskeletal-modeling`  
**Entries:** 3 (2 commons-grade, 1 draft)  
**Earliest disclosure:** 2003-01  
**Most recent disclosure:** 2016-08

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-musculoskeletal-modeling`.

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

### 2003-01 — AnyBody Modeling System *(draft)*

- **id:** `anybody-rasmussen-2003`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** AnyBody Technology A/S (Aalborg University, Denmark); John Rasmussen + Michael Damsgaard
- **disclosure citation:** AnyBody Technology A/S (Aalborg, Denmark; Aalborg University spinout 2001 by John Rasmussen + Michael Damsgaard). AnyBody Modeling System commercial reveal 2003.
- **disclosed subsystems:** `control-physics-simulation`, `control-musculoskeletal-modeling`

**Prior art notes:**

> AnyBody Modeling System (Rasmussen + Damsgaard Aalborg 2003+) is the canonical commercial biomechanics modeling system. 22-year-deep public-disclosure prior art. Together with OpenSim (round-33), establishes the biomechanics-simulation prior-art chain that informs humanoid kinematic design. Closes a Danish commercial gap and adds biomechanics depth.

**Sources:**

1. AnyBody Technology corporate site (anybodytech.com).

---

### 2007-11 — OpenSim biomechanics framework

- **id:** `opensim-delp-stanford-2007`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Stanford University; Scott Delp + colleagues
- **disclosure citation:** Delp, S. L., Anderson, F. C., Arnold, A. S., Loan, P., Habib, A., John, C. T., Guendelman, E., Thelen, D. G. 'OpenSim: Open-Source Software to Create and Analyze Dynamic Simulations of Movement'. IEEE Transactions on Biomedical Engineering 54(11) 2007. Stanford University Neuromuscular Biomechanics Laboratory.
- **disclosed subsystems:** `control-research-cluster`, `control-physics-simulation`, `control-musculoskeletal-modeling`

**Prior art notes:**

> OpenSim (Delp et al. Stanford IEEE T-BME 2007) is the dominant academic biomechanics simulation framework. 18-year-deep open-permissive prior art. **The framework underlying humanoid-robot kinematic design** — humanoid arms + legs are designed to approximate human ranges of motion documented in OpenSim models. Direct shielding for any commercial humanoid claim that derives kinematic specifications from human-anatomical models.

**Sources:**

1. Delp et al. IEEE T-BME 54(11) 2007.
2. OpenSim site (opensim.stanford.edu).
3. GitHub: github.com/opensim-org/opensim-core.

---

### 2016-08 — Rajagopal full-body OpenSim musculoskeletal model

- **id:** `rajagopal-opensim-full-body-2016`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Stanford University NMBL; Apoorva Rajagopal, Christopher Dembia, Matthew DeMers, Daniel Delp, Jennifer Hicks, Scott Delp
- **disclosure citation:** Rajagopal, A., Dembia, C. L., DeMers, M. S., Delp, D. D., Hicks, J. L., Delp, S. L. 'Full-Body Musculoskeletal Model for Muscle-Driven Simulation of Human Gait'. IEEE Transactions on Bio-medical Engineering 63(10) 2016. Stanford University Neuromuscular Biomechanics Laboratory.
- **disclosed subsystems:** `control-physics-simulation`, `control-musculoskeletal-modeling`

**Prior art notes:**

> Rajagopal full-body OpenSim model (Stanford NMBL IEEE T-BME 2016) is the canonical full-body musculoskeletal model in OpenSim. 9-year-deep open-permissive prior art. The specific paper-level anchor of the round-33 OpenSim aggregator entry for full-body humanoid kinematic-spec derivation. Direct shielding for any commercial humanoid claim deriving kinematic specifications from human anatomical models.

**Sources:**

1. Rajagopal et al. IEEE T-BME 63(10) 2016.
2. OpenSim model database (opensim.stanford.edu).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `2b483e9`.*
