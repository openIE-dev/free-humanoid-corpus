---
title: "control-vibrotactile-feedback"
parent: "Invalidity Contentions"
nav_order: 115
layout: default
---

# Invalidity Contention Packet — `control-vibrotactile-feedback`

**Generated:** 2026-05-09  
**Cross-cut tag:** `control-vibrotactile-feedback`  
**Entries:** 2 (0 commons-grade, 2 draft)  
**Earliest disclosure:** 2023-01  
**Most recent disclosure:** 2023-09

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-vibrotactile-feedback`.

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

### 2023-01 — Manus Quantum Metagloves *(draft)*

- **id:** `manus-quantum-metagloves-2023`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Manus Meta (Eindhoven, Netherlands)
- **disclosure citation:** Manus VR / Manus Meta (Eindhoven, Netherlands; founded 2014). Quantum Metagloves reveal CES 2023. Successor to Manus Prime, Prime II, Prime X glove generations. manus-meta.com.
- **disclosed subsystems:** `control-vibrotactile-feedback`, `sensing-hand-pose-tracking`

**Prior art notes:**

> Manus Quantum Metagloves is the canonical 2023+ commercial vibrotactile-only hand-tracking glove (Manus Meta, Netherlands). 2-year-deep public-disclosure prior art for: EMF-based sub-millimeter fingertip tracking, vibrotactile-only haptic feedback in glove form factor, lightweight VR-class hand tracking. Distinct architectural branch from HaptX (full-haptic-feedback) — Manus optimizes for motion-cap-grade tracking with lightweight feedback. Direct shielding for any commercial humanoid teleop claim on EMF + IMU fingertip tracking.

**Sources:**

1. Manus Meta corporate site (manus-meta.com).
2. CES 2023 reveal coverage.

---

### 2023-09 — SenseGlove Nova 2 *(draft)*

- **id:** `senseglove-nova-2-2023`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** SenseGlove BV (Delft, Netherlands; TU Delft spinout)
- **disclosure citation:** SenseGlove BV (Delft, Netherlands; TU Delft spinout 2018). Nova 2 product reveal September 2023 via senseglove.com. Successor to Nova 1 (2021) and original SenseGlove DK1 (2018).
- **disclosed subsystems:** `control-haptic-rendering`, `actuator-active-brake`, `control-vibrotactile-feedback`, `sensing-hand-pose-tracking`

**Prior art notes:**

> SenseGlove Nova 2 is a canonical 2023+ commercial mid-fidelity haptic glove (SenseGlove, TU Delft spinout). 2-year-deep public-disclosure prior art for: active-brake force feedback in glove form factor, vibrotactile + active-brake hybrid haptic. Distinct architectural branch from HaptX (microfluidic) and Manus (vibrotactile-only). Direct shielding for any commercial humanoid teleop claim on active-brake-based glove force feedback.

**Sources:**

1. SenseGlove corporate site (senseglove.com).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `d6a964d`.*
