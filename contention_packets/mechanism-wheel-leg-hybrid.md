---
title: "mechanism-wheel-leg-hybrid"
parent: "Invalidity Contentions"
nav_order: 29
layout: default
---

# Invalidity Contention Packet — `mechanism-wheel-leg-hybrid`

**Generated:** 2026-05-07  
**Cross-cut tag:** `mechanism-wheel-leg-hybrid`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2002-10-01  
**Most recent disclosure:** 2004

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `mechanism-wheel-leg-hybrid`.

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

### 2002-10-01 — Tachikoma

- **id:** `ghost-in-the-shell-tachikoma`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Kenji Kamiyama (TV series), Masamune Shirow (precursor design)
- **disclosure citation:** Kamiyama, Kenji. Ghost in the Shell: Stand Alone Complex. Production I.G, October 1, 2002 (TV series); precursor 'Fuchikoma' design in Shirow, M. Ghost in the Shell, 1989.
- **disclosed subsystems:** `mechanism-wheel-leg-hybrid`, `control-rl-policy`

**Prior art notes:**

> The most engineering-specific disclosure in the GitS franchise. Anticipates: (1) wheel-leg hybrid locomotion in a quadruped — directly relevant to claims on hybrid-mobility morphologies (BD Spot's hybrid variants, OpenLoco quadrupeds); (2) decentralized swarm AI with periodic policy synchronization — anticipates federated-learning humanoid fleet IP, the specific architecture used by Tesla Optimus's fleet learning; (3) individual experience accumulation followed by aggregation — directly relevant to fleet-policy-update IP. The 2002 broadcast is well-archived; Production I.G's mecha designs are widely cited in robotics venues.

**Sources:**

1. Kamiyama, K. Ghost in the Shell: Stand Alone Complex. Production I.G, 2002-2005.
2. Shirow, M. The Ghost in the Shell, Chapter 5 (Fuchikoma precursor). Kodansha, 1991.

---

### 2004 — HUBO

- **id:** `hubo`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** KAIST, Hubo Lab (Jun-Ho Oh)
- **disclosure citation:** Park, Ill-Woo et al. 'Mechanical Design of Humanoid Robot Platform KHR-3 (HUBO).' IEEE-RAS Humanoids 2005.
- **disclosed subsystems:** `actuator-electric-harmonic-drive`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `mechanism-wheel-leg-hybrid`, `control-zmp-balancing`, `sensing-stereo-camera`, `sensing-lidar`, `sensing-force-torque`

**Prior art notes:**

> DRC-Hubo's 2015 win demonstrated transformer-style transitioning between bipedal and wheeled-knee modes for navigating both stairs and flat ground. Anticipates: hybrid locomotion modes in humanoids.

**Sources:**

1. Park, I.-W. et al. IEEE-RAS Humanoids 2005.
2. DARPA Robotics Challenge final report, 2015.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `32bba80`.*
