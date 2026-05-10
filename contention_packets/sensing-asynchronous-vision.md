---
title: "sensing-asynchronous-vision"
parent: "Invalidity Contentions"
nav_order: 233
layout: default
---

# Invalidity Contention Packet — `sensing-asynchronous-vision`

**Generated:** 2026-05-10  
**Cross-cut tag:** `sensing-asynchronous-vision`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2008-02  
**Most recent disclosure:** 2020-09

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `sensing-asynchronous-vision`.

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

### 2008-02 — Dynamic Vision Sensor (DVS) event camera

- **id:** `lichtsteiner-dvs-event-camera-2008`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** ETH Zürich + UZH Institute of Neuroinformatics; Tobi Delbruck group
- **disclosure citation:** Lichtsteiner, P., Posch, C., Delbruck, T. 'A 128×128 120 dB 15 μs Latency Asynchronous Temporal Contrast Vision Sensor'. IEEE Journal of Solid-State Circuits 43(2) 2008. ETH Zürich + UZH Institute of Neuroinformatics. The Tobi Delbruck group; antecedent: Mahowald-Mead silicon retina (Caltech 1990s).
- **disclosed subsystems:** `sensing-event-camera`, `sensing-asynchronous-vision`, `sensing-neuromorphic-vision`

**Prior art notes:**

> The DVS event camera (Lichtsteiner-Posch-Delbruck IEEE JSSC 2008) is the canonical foundational event-camera academic publication. 17-year-deep public-domain prior art. **The architectural ancestor of every subsequent event camera** (Inivation, Prophesee, Sony IMX636). Direct shielding for any commercial humanoid claim on event-based / neuromorphic vision sensing. Closes the foundational event-camera citation chain.

**Sources:**

1. Lichtsteiner, Posch, Delbruck. IEEE JSSC 43(2) 2008.
2. Mahowald-Mead silicon retina antecedent (Caltech 1990s).
3. UZH Institute of Neuroinformatics (ini.uzh.ch).

---

### 2020-09 — Prophesee EVK4 event camera

- **id:** `prophesee-evk4-event-camera-2020`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Prophesee S.A. (Paris, France) + Sony co-developed sensor
- **disclosure citation:** Prophesee S.A. (Paris, France; founded 2014, ESIEE Paris + INSEAD Sorbonne Université spinout). EVK4 evaluation kit reveal 2020+ via prophesee.ai. Sony IMX636 sensor (Prophesee + Sony co-developed) is the EVK4's underlying chip — the first commercial event-camera sensor at megapixel resolution + industrial form factor.
- **disclosed subsystems:** `sensing-event-camera`, `sensing-asynchronous-vision`

**Prior art notes:**

> Prophesee EVK4 is the canonical commercial megapixel event camera (2020+). 5-year-deep public-disclosure prior art. Direct successor to DVS (round-29 entry above) + Inivation DAVIS. Direct shielding for any commercial humanoid claim on commercial-grade event-camera deployment.

**Sources:**

1. Prophesee corporate site (prophesee.ai).
2. Sony IMX636 sensor announcement.

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
