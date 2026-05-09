---
title: "control-autonomous-driving"
parent: "Invalidity Contentions"
nav_order: 24
layout: default
---

# Invalidity Contention Packet — `control-autonomous-driving`

**Generated:** 2026-05-09  
**Cross-cut tag:** `control-autonomous-driving`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2009-01  
**Most recent disclosure:** 2017-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-autonomous-driving`.

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

### 2009-01 — Waymo / Google Self-Driving Car

- **id:** `waymo-google-self-driving-car-2009`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Google X / Waymo (Alphabet subsidiary); Sebastian Thrun + DARPA Grand Challenge alumni
- **disclosure citation:** Google X / Project Chauffeur self-driving car project initiated January 2009 (publicly disclosed October 2010). Spun out as Waymo (subsidiary of Alphabet) December 2016. waymo.com. First public driverless service Phoenix Arizona December 2018; expanded San Francisco + LA + Austin 2023-2025.
- **disclosed subsystems:** `control-autonomous-driving`, `control-multimodal-sensor-fusion`, `control-predictive-planning`

**Prior art notes:**

> Waymo / Google Self-Driving Car (Project Chauffeur 2009-2016 → Waymo 2016+) is the canonical foundational autonomous-vehicle commercial deployment. 16-year-deep public-disclosure prior art. **Architecturally adjacent to humanoid robotics** via Tesla FSD chip → Optimus shared perception architecture chain (Tesla Optimus Gen 3 corpus entry explicitly cites FSD chip). Direct shielding for any commercial humanoid claim on multi-modal perception derivative applications from autonomous-vehicle stacks.

**Sources:**

1. Waymo corporate site (waymo.com).
2. Project Chauffeur public disclosure October 2010.
3. Wikipedia 'Waymo'.

---

### 2017-04 — Baidu Apollo (autonomous driving — distinct from Apptronik humanoid)

- **id:** `baidu-apollo-self-driving-2017`
- **corpus:** private
- **ip status:** open-permissive
- **creator:** Baidu Inc. (Beijing, China)
- **disclosure citation:** Baidu Inc. (Beijing, China). Apollo open-source autonomous driving platform announced April 2017. apollo.baidu.com. **Note: this is the Baidu Apollo autonomous-vehicle platform, distinct from Apptronik Apollo humanoid robot (corpus entry apptronik-apollo)** — both confusingly share the name 'Apollo'.
- **disclosed subsystems:** `control-autonomous-driving`, `control-multimodal-sensor-fusion`, `control-research-cluster`

**Prior art notes:**

> Baidu Apollo (Baidu Beijing 2017+) is the Chinese open-source autonomous-vehicle platform. 8-year-deep open-permissive prior art. **Distinct from Apptronik Apollo humanoid (corpus entry apptronik-apollo) by application + architecture** — both share the 'Apollo' name only by coincidence. Direct shielding for any commercial humanoid claim that derives perception or planning from autonomous-vehicle stacks (which the Tesla Optimus FSD lineage explicitly does).

**Sources:**

1. Baidu Apollo platform site (apollo.baidu.com).
2. GitHub: github.com/ApolloAuto/apollo.

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
