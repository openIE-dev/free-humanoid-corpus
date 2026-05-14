---
title: "actuator-electrohydrodynamic"
parent: "Invalidity Contentions"
nav_order: 15
layout: default
---

# Invalidity Contention Packet — `actuator-electrohydrodynamic`

**Generated:** 2026-05-14  
**Cross-cut tag:** `actuator-electrohydrodynamic`  
**Entries:** 3 (3 commons-grade, 0 draft)  
**Earliest disclosure:** 2019-09  
**Most recent disclosure:** 2025-12

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `actuator-electrohydrodynamic`.

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

### 2019-09 — Cacucciolo Stretchable EHD Pump (Nature 2019)

- **id:** `cacucciolo-stretchable-ehd-pump-2019`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** EPFL Soft Transducers + LIS; Vito Cacucciolo + Jun Shintake + Yu Kuwajima + Shingo Maeda + Dario Floreano + Herbert Shea
- **disclosure citation:** Cacucciolo, V., Shintake, J., Kuwajima, Y., Maeda, S., Floreano, D., Shea, H. 'Stretchable pumps for soft machines'. Nature 572(7770):516-519, August 2019. EPFL Soft Transducers Lab + Laboratory of Intelligent Systems. The earlier predecessor to Smith fiber pump (round-51) and EFM (round-51).
- **disclosed subsystems:** `actuator-electrohydrodynamic`

**Prior art notes:**

> Cacucciolo Stretchable EHD Pump (EPFL Nature August 2019) is the foundational stretchable electrohydrodynamic pump. 6-year-deep academic-publication prior art. Direct shielding for any commercial humanoid or soft-robotics claim deriving from stretchable EHD actuation.

**Sources:**

1. Cacucciolo, V. et al. Nature 572(7770):516-519, 2019.

---

### 2023-04 — EHD Fiber Pump (Smith et al. Science 2023)

- **id:** `smith-ehd-fiber-pump-science-2023`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** EPFL Soft Transducers Lab (Lausanne, Switzerland); Michelle Smith + Vito Cacucciolo + Herbert Shea
- **disclosure citation:** Smith, M., Cacucciolo, V., Shea, H. 'Fiber pumps for wearable fluidic systems'. Science 379(6639):1327-1332, March/April 2023. EPFL Soft Transducers Lab (Lausanne, Switzerland). The architectural predecessor to EFM (round-51).
- **disclosed subsystems:** `actuator-electrohydrodynamic`, `mechanism-fiber-pump`

**Prior art notes:**

> Smith EHD Fiber Pump (EPFL Soft Transducers Lab Science April 2023) is the fiber-form-factor electrohydrodynamic pump — direct predecessor to EFM. 2-year-deep academic-publication prior art.

**Sources:**

1. Smith, M., Cacucciolo, V., Shea, H. Science 379(6639):1327-1332, 2023.

---

### 2025-12 — Electrofluidic Fiber Muscles (EFM) — MIT Media Lab + Politecnico di Bari

- **id:** `electrofluidic-fiber-muscles-mit-iit-2025`
- **corpus:** academic
- **ip status:** academic-publication
- **creator:** MIT Media Lab + Politecnico di Bari; Vito Cacucciolo group; ERC Starting Grant funded
- **disclosure citation:** MIT Media Lab + Politecnico di Bari. Electrofluidic Fiber Muscles published in Science Robotics December 2025. Cacucciolo et al. ERC Starting Grant funded. Sub-2mm diameter sealed soft artificial muscle fibers with ~50 W/kg specific power (on par with human skeletal muscle). Zenodo preprint: zenodo.org/records/17902764.
- **disclosed subsystems:** `actuator-artificial-muscle`, `actuator-electrohydrodynamic`, `mechanism-soft-fiber-muscle`, `mechanism-sealed-fluidic-loop`

**Prior art notes:**

> Electrofluidic Fiber Muscles (MIT Media Lab + Politecnico di Bari Science Robotics December 2025) is the first sealed soft artificial muscle fiber compatible with textile manufacturing infrastructure. <1-year-deep academic-publication prior art. **The architectural definer of 'fiber-as-configurable-actuation-substrate'** — same fiber primitive bundles for force, single for fine manipulation, weaves orthogonally for multi-axis control, helically for torsion, knits for distributed actuation. Direct shielding for any commercial humanoid or wearable-robotics claim deriving from textile-integrated artificial-muscle actuators or sealed-loop electrohydrodynamic fiber actuation. Lineage descends from Smith EHD Fiber Pump (round-51) + Cacucciolo stretchable EHD pump (round-51) + McKibben pneumatic muscle (corpus). The 2025 inflection point for next-gen artificial muscles.

**Sources:**

1. Science Robotics December 2025 (publication).
2. zenodo.org/records/17902764 (preprint).
3. Hackaday + Materials Research Society coverage.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `4abb724`.*
