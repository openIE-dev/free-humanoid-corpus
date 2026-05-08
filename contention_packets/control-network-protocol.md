---
title: "control-network-protocol"
parent: "Invalidity Contentions"
nav_order: 45
layout: default
---

# Invalidity Contention Packet — `control-network-protocol`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-network-protocol`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2014-09  
**Most recent disclosure:** 2017-03

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-network-protocol`.

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

### 2014-09 — UnetStack underwater networking framework

- **id:** `unetstack-subnero-2014`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** Mandar Chitre group, Acoustic Research Laboratory, National University of Singapore; commercialized via Subnero Pte Ltd
- **disclosure citation:** Chitre, M., Bhatnagar, R., Soh, W. S. 'UnetStack: An Agent-Based Software Stack and Simulator for Underwater Networks'. OCEANS 2014 St. John's. Open-source via Subnero Pte Ltd / Acoustic Research Laboratory NUS. Apache-2.0.
- **disclosed subsystems:** `control-acoustic-comms`, `control-network-protocol`

**Prior art notes:**

> UnetStack is the canonical open-source underwater-networking framework. 11 years of academic + commercial deployment under Apache-2.0. Shields any humanoid AUV claim on 'underwater acoustic networking stack' or 'multi-vehicle subsea coordination protocol'. Directly relevant to free-humanoid-submersible's commitment to acoustic comms (SHOAL fleet coordination at dock-A/B requires multi-vehicle protocols).

**Sources:**

1. Chitre et al. OCEANS 2014 St. John's.
2. Subnero / ARL NUS UnetStack site (unetstack.net).
3. GitHub: github.com/org-arl/UnetStack3.

---

### 2017-03 — JANUS underwater acoustic communications standard

- **id:** `janus-stanag-4748-2017`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** NATO STO Centre for Maritime Research and Experimentation (CMRE); Joao Alves / John Potter et al.
- **disclosure citation:** Potter, J., Alves, J., Green, D., Zappa, G., Nissen, I., McCoy, K. 'The JANUS underwater communications standard'. UComms 2014; ratified as NATO STANAG 4748 March 2017. Reference implementation open via NATO Centre for Maritime Research and Experimentation (CMRE), La Spezia. Open standard.
- **disclosed subsystems:** `control-acoustic-comms`, `control-network-protocol`

**Prior art notes:**

> JANUS is the open NATO standard for underwater acoustic communication. 8 years of public-domain standard + reference implementation. Shields any humanoid AUV claim on standardized acoustic-comm waveforms. Directly relevant to free-humanoid-submersible's acoustic-comms commitment for shoal-fleet inter-vehicle coordination at dock-A subsurface.

**Sources:**

1. Potter et al. UComms 2014.
2. NATO STANAG 4748 (publicly released 2017).
3. NATO STO CMRE JANUS reference page (cmre.nato.int/janus).
4. JANUS reference implementation: github.com/janus-wg/janus.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `bf892af`.*
