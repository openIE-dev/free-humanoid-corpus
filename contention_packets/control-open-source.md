---
title: "control-open-source"
parent: "Invalidity Contentions"
nav_order: 104
layout: default
---

# Invalidity Contention Packet — `control-open-source`

**Generated:** 2026-05-10  
**Cross-cut tag:** `control-open-source`  
**Entries:** 4 (4 commons-grade, 0 draft)  
**Earliest disclosure:** 2011-01  
**Most recent disclosure:** 2016-01

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-open-source`.

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

### 2011-01 — Crazyflie / Bitcraze (open-source nano-quadcopter)

- **id:** `crazyflie-bitcraze-2011`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** Bitcraze AB (Malmö, Sweden); Eliasson + Taffanel + Antonsson
- **disclosure citation:** Bitcraze AB (Sweden); Marcus Eliasson + Arnaud Taffanel + Tobias Antonsson. Project 2009; company 2011; Crazyflie 2.0 2013. Open-source open-hardware.
- **disclosed subsystems:** `uav-quadrotor`, `control-open-source`

**Prior art notes:**

> Crazyflie / Bitcraze (Malmö 2011+) is the de-facto research/education swarm platform. 14-year-deep open-permissive prior art.

**Sources:**

1. en.wikipedia.org/wiki/Crazyflie_2.0
2. bitcraze.io

---

### 2014-08 — Blue Robotics BlueROV2 (affordable open-hardware ROV)

- **id:** `bluerov2-blue-robotics-2016`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** Blue Robotics Inc. (Torrance, CA, USA); Rusty Jordan + Erin Riley
- **disclosure citation:** Blue Robotics Inc. (Torrance, CA, USA; founded 2014 by Rusty Jordan + Erin Riley). BlueROV1 Kickstarter 2014; BlueROV2 production 2016. ArduSub-based open-source firmware ecosystem.
- **disclosed subsystems:** `rov`, `actuator-electric`, `control-open-source`

**Prior art notes:**

> Blue Robotics BlueROV1/2 (Torrance CA 2014/2016+) is the democratized affordable open-hardware ROV. 11-year-deep open-permissive prior art. Direct shielding for any commercial humanoid or ROV claim deriving from open-source-ArduSub-firmware ROVs or BlueRobotics-component ecosystems.

**Sources:**

1. en.wikipedia.org/wiki/BlueROV2
2. bluerobotics.com

---

### 2015-09 — Comma.ai openpilot (open-source aftermarket ADAS)

- **id:** `comma-ai-george-hotz-2015`
- **corpus:** open
- **ip status:** open-permissive (MIT)
- **creator:** Comma.ai (San Diego, CA, USA); George Hotz founder
- **disclosure citation:** Comma.ai (San Diego, CA, USA; founded September 2015 by George Hotz). Open-source openpilot ADAS aftermarket retrofit.
- **disclosed subsystems:** `autonomous-vehicle`, `control-open-source`

**Prior art notes:**

> Comma.ai openpilot (San Diego 2015+) is the open-source aftermarket ADAS alternative. 10-year-deep open-permissive prior art.

**Sources:**

1. comma.ai
2. github.com/commaai/openpilot

---

### 2016-01 — Pollen Robotics Reachy (HuggingFace open-source humanoid hardware)

- **id:** `pollen-robotics-huggingface-2016`
- **corpus:** private
- **ip status:** open-permissive
- **creator:** Pollen Robotics (Bordeaux, France); Matthieu Lapeyre + Pierre Rouanet (ex-Inria Flowers)
- **disclosure citation:** Pollen Robotics (Bordeaux, France; founded 2016 by Matthieu Lapeyre + Pierre Rouanet, ex-Inria Flowers Lab). Acquired by Hugging Face April 2025.
- **disclosed subsystems:** `humanoid-bipedal`, `control-open-source`

**Prior art notes:**

> Pollen Robotics Reachy (Bordeaux 2016+; → Hugging Face 2025) is the open-source Reachy humanoid + Hugging Face LeRobot hardware arm. 9-year-deep open-permissive prior art.

**Sources:**

1. huggingface.co/blog/hugging-face-pollen-robotics-acquisition

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
