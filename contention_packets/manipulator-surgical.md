---
title: "manipulator-surgical"
parent: "Invalidity Contentions"
nav_order: 178
layout: default
---

# Invalidity Contention Packet — `manipulator-surgical`

**Generated:** 2026-05-11  
**Cross-cut tag:** `manipulator-surgical`  
**Entries:** 4 (4 commons-grade, 0 draft)  
**Earliest disclosure:** 2006-09  
**Most recent disclosure:** 2021-09

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `manipulator-surgical`.

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

### 2006-09 — MAKO RIO orthopedic robot-arm-assisted surgery

- **id:** `mako-rio-stryker-2006`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** MAKO Surgical Corp. (Fort Lauderdale, FL, USA) → Stryker Corporation 2013
- **disclosure citation:** MAKO Surgical Corp. (Fort Lauderdale, FL, USA; founded 2004). RIO (Robotic-Arm Interactive Orthopedic) system FDA-cleared 2006 for partial knee. Acquired by Stryker Corporation December 2013 for USD 1.65B. Subsequent MAKO Total Knee 2017; MAKO 4 2025.
- **disclosed subsystems:** `manipulator-arm`, `manipulator-surgical`, `manipulator-haptic-boundary`, `actuator-electric`

**Prior art notes:**

> MAKO RIO (MAKO Surgical Fort Lauderdale 2006 → Stryker 2013) is the canonical robotic-arm-assisted orthopedic surgery system. 19-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from haptic-boundary-constrained surgical arms. Lineage descends from Barrett WAM Arm (round-45).

**Sources:**

1. en.wikipedia.org/wiki/MAKO_Surgical_Corp.

---

### 2011-01 — Mazor Renaissance / Stealth Spine guidance

- **id:** `mazor-renaissance-medtronic-2011`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Mazor Robotics Ltd. (Caesarea, Israel; Moshe Shoham Technion); → Medtronic 2018
- **disclosure citation:** Mazor Robotics Ltd. (Caesarea, Israel; founded 2000 by Moshe Shoham, Technion). SpineAssist FDA-cleared 2004; Renaissance FDA-cleared 2011 (1.5 mm accuracy bone-mounted spine guidance). Mazor X 2017. Acquired by Medtronic 2018 for USD 1.6B.
- **disclosed subsystems:** `manipulator-arm`, `manipulator-surgical`, `manipulator-parallel`, `actuator-electric`

**Prior art notes:**

> Mazor Robotics SpineAssist + Renaissance + Mazor X (Caesarea Israel 2004-2017+; Medtronic 2018) is the bone-mounted spine surgical guidance system. 21-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from bone-mounted parallel-mechanism surgical guidance arms.

**Sources:**

1. en.wikipedia.org/wiki/Mazor_Robotics

---

### 2019-09 — CMR Surgical Versius modular soft-tissue surgical robot

- **id:** `cmr-versius-2019`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** CMR Surgical Ltd. (Cambridge, UK)
- **disclosure citation:** Cambridge Medical Robotics Surgical Ltd. (Cambridge, UK; founded 2014). Versius commercial reveal September 2019. CE-mark 2019. FDA Versius Plus 510(k) clearance 2025. Modular small-footprint per-arm soft-tissue surgical robot.
- **disclosed subsystems:** `manipulator-arm`, `manipulator-surgical`, `manipulator-modular`, `actuator-electric`

**Prior art notes:**

> CMR Surgical Versius (Cambridge UK 2019+) is the canonical modular small-footprint soft-tissue surgical robot. 6-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from modular per-arm surgical robotics.

**Sources:**

1. en.wikipedia.org/wiki/CMR_Surgical

---

### 2021-09 — Medtronic Hugo RAS modular surgical platform

- **id:** `medtronic-hugo-ras-2021`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Medtronic plc (Dublin, Ireland; HQ Galway / Minneapolis)
- **disclosure citation:** Medtronic plc (Dublin, Ireland; HQ Galway / Minneapolis). Hugo RAS (Robotic-Assisted Surgery) commercial reveal September 2021. CE-mark 2021. FDA urology 510(k) clearance December 2025. Modular multi-arm soft-tissue surgical platform — Medtronic's answer to da Vinci.
- **disclosed subsystems:** `manipulator-arm`, `manipulator-surgical`, `manipulator-modular`, `actuator-electric`

**Prior art notes:**

> Medtronic Hugo RAS (Medtronic Dublin 2021+) is Medtronic's modular multi-arm soft-tissue surgical platform — the answer to da Vinci. 4-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from modular multi-arm surgical robotics.

**Sources:**

1. medtronic.com/en-us/healthcare-professionals/specialties/surgical-robotics/hugo-robotic-assisted-surgery.html

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `0e58219`.*
