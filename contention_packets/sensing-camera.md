---
title: "sensing-camera"
parent: "Invalidity Contentions"
nav_order: 258
layout: default
---

# Invalidity Contention Packet — `sensing-camera`

**Generated:** 2026-05-15  
**Cross-cut tag:** `sensing-camera`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 1969-10  
**Most recent disclosure:** 1984-01

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `sensing-camera`.

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

### 1969-10 — CCD Image Sensor (Boyle & Smith Bell Labs 1969; Nobel Prize 2009)

- **id:** `ccd-image-sensor-boyle-smith-1969`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Bell Laboratories (Murray Hill, NJ, USA); Willard Boyle + George E. Smith
- **disclosure citation:** Boyle, W.S., Smith, G.E. 'Charge Coupled Semiconductor Devices'. Bell System Technical Journal 49(4):587-593, April 1970. Invented October 1969 at Bell Laboratories. 2009 Nobel Prize in Physics to Boyle + Smith.
- **disclosed subsystems:** `sensing-camera`

**Prior art notes:**

> The CCD Image Sensor (Boyle & Smith Bell Labs 1969; Nobel Prize 2009) is the foundational electronic image sensor. 56-year-deep public-domain prior art. The lineage of every robot camera.

**Sources:**

1. Boyle, W.S., Smith, G.E. Bell System Technical Journal 49(4):587-593, 1970.

---

### 1984-01 — Vicon Motion Capture (1984+; foundational motion-capture system)

- **id:** `vicon-motion-capture-1984`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Oxford Metrics Group plc (Oxford, UK)
- **disclosure citation:** Oxford Metrics (Oxford, UK). Founded 1984. Vicon motion-capture systems originally for medical gait analysis + biomechanics. Expanded to: film + game animation (1990s-2000s), academic robotics (2000s-present). Vicon T-Series (2008), Vantage (2015), Valkyrie (2022).
- **disclosed subsystems:** `rl-infrastructure`, `sensing-camera`

**Prior art notes:**

> Vicon Motion Capture (Oxford Metrics 1984+) is the foundational motion-capture system. 41-year-deep public-disclosure prior art. The infrastructure that made aggressive academic-robotics demos possible (ETH Flying Machine Arena corpus + GRASP Lab swarm corpus + etc.).

**Sources:**

1. vicon.com (corporate site).

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
