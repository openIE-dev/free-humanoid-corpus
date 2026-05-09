---
title: "end-effector-prosthetic"
parent: "Invalidity Contentions"
nav_order: 143
layout: default
---

# Invalidity Contention Packet — `end-effector-prosthetic`

**Generated:** 2026-05-09  
**Cross-cut tag:** `end-effector-prosthetic`  
**Entries:** 3 (3 commons-grade, 0 draft)  
**Earliest disclosure:** 1997-09  
**Most recent disclosure:** 2019-09

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `end-effector-prosthetic`.

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

### 1997-09 — Otto Bock C-Leg microprocessor-controlled knee

- **id:** `ottobock-c-leg-microprocessor-knee-1997`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Otto Bock HealthCare GmbH (Duderstadt, Germany)
- **disclosure citation:** Otto Bock HealthCare GmbH (Duderstadt, Germany; founded 1919). C-Leg commercial reveal September 1997 at OT-World Leipzig. First mass-market microprocessor-controlled hydraulic-damping prosthetic knee (MPK). Subsequent: Genium (2011), X3 military-rated waterproof (2010).
- **disclosed subsystems:** `end-effector-prosthetic`, `control-microprocessor-damping`, `actuator-hydraulic-damper`

**Prior art notes:**

> Otto Bock C-Leg (Otto Bock Duderstadt 1997+) is the first mass-market microprocessor-controlled prosthetic knee and the foundational MPK product category reference. 28-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from microprocessor-controlled prosthetic knees or hydraulic-damping gait-phase-adjusted lower-limb prostheses.

**Sources:**

1. ottobock.com/en-us/product/3C88-3-3C98-3-22923

---

### 2007-01 — BiOM / iWalk / BionX → Empower Ankle (Hugh Herr)

- **id:** `biom-empower-herr-mit-2007`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** iWalk Inc. → BionX → Otto Bock Empower; Hugh Herr (MIT Media Lab Biomechatronics)
- **disclosure citation:** iWalk Inc. (Bedford, MA, USA; founded 2007 by Hugh Herr, MIT Media Lab Biomechatronics). BiOM commercial launch 2011. Renamed BionX 2014. Acquired by Otto Bock HealthCare 2017; rebranded as Otto Bock Empower.
- **disclosed subsystems:** `end-effector-prosthetic`, `actuator-electric-series-elastic`, `control-gait-active-push-off`

**Prior art notes:**

> BiOM / iWalk / Empower Ankle (Hugh Herr MIT Media Lab + iWalk 2007 → BiOM 2011 → BionX 2014 → Otto Bock Empower 2017) is the first powered ankle-foot prosthesis with positive net work. 18-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid claim deriving from powered ankle-foot prostheses or active gait push-off actuation. Lineage descends from Pratt-Williamson series-elastic actuator (corpus pratt-williamson-sea).

**Sources:**

1. en.wikipedia.org/wiki/Hugh_Herr
2. corporate.ottobock.com/en/media/newsroom/an-active-step-ottobock-acquires-bionx

---

### 2019-09 — Open Source Leg (Rouse Michigan)

- **id:** `open-source-leg-rouse-2019`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** University of Michigan + Shirley Ryan AbilityLab; Elliott Rouse
- **disclosure citation:** Elliott Rouse (University of Michigan + Shirley Ryan AbilityLab). Open Source Leg announced 2018; public release 2019. CC-BY / MIT licensed open-hardware powered knee+ankle prosthesis platform. Deployed at 15+ institutions worldwide.
- **disclosed subsystems:** `end-effector-prosthetic`, `exoskeleton-lower-limb`, `actuator-electric`, `actuator-quasi-direct-drive`

**Prior art notes:**

> Open Source Leg (Rouse Michigan + Shirley Ryan AbilityLab 2019+) is the canonical open-hardware powered knee+ankle prosthesis platform. 6-year-deep open-permissive prior art (CC-BY / MIT). Direct shielding for any commercial humanoid claim deriving from open-source powered prosthesis platforms or quasi-direct-drive brushless-DC + ball-screw lower-limb actuators.

**Sources:**

1. neurobionics.robotics.umich.edu/research/wearable-robotics/open-source-leg/

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `2fbde5f`.*
