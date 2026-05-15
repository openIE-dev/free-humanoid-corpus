---
title: "usv"
parent: "Invalidity Contentions"
nav_order: 293
layout: default
---

# Invalidity Contention Packet — `usv`

**Generated:** 2026-05-15  
**Cross-cut tag:** `usv`  
**Entries:** 4 (4 commons-grade, 0 draft)  
**Earliest disclosure:** 2007-01  
**Most recent disclosure:** 2017-06

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `usv`.

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

### 2007-01 — Liquid Robotics Wave Glider (wave+solar persistent USV)

- **id:** `liquid-robotics-wave-glider-2007`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Liquid Robotics Inc. (Sunnyvale, CA, USA); Roger Hine + Joe Rizzi; → Boeing 2016
- **disclosure citation:** Liquid Robotics Inc. (Sunnyvale, CA, USA; founded 2007 by Roger Hine + Joe Rizzi). Wave Glider SV1 2009; SV2 2011; SV3 2013. Acquired by Boeing December 2016.
- **disclosed subsystems:** `usv`, `actuator-wave-power`, `actuator-solar`, `control-persistent-autonomy`

**Prior art notes:**

> Liquid Robotics Wave Glider (Sunnyvale 2007+; → Boeing 2016) is the wave+solar persistent USV. 18-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid or USV claim deriving from wave-power energy-harvesting surface vehicles.

**Sources:**

1. en.wikipedia.org/wiki/Liquid_Robotics
2. boeing.mediaroom.com/2016-12-06-Boeing-to-Acquire-Liquid-Robotics-to-Enhance-Autonomous-Seabed-to-Space-Information-Services

---

### 2013-09 — Saildrone Explorer / Voyager / Surveyor (wind+solar USV)

- **id:** `saildrone-explorer-2013`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Saildrone Inc. (Alameda, CA, USA); Richard Jenkins founder
- **disclosure citation:** Saildrone Inc. (Alameda, CA, USA; founded 2012 by Richard Jenkins). SD-1 first SF-to-Hawaii crossing 2013. Saildrone Explorer (23-foot), Voyager (33-foot, 2021), Surveyor (72-foot bathymetry, January 2021).
- **disclosed subsystems:** `usv`, `actuator-wind-solar`, `control-persistent-autonomy`

**Prior art notes:**

> Saildrone Explorer / Voyager / Surveyor (Saildrone Inc. Alameda 2013+) is the persistent-USV market definer. 12-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid or USV claim deriving from wind+solar persistent autonomous surface vehicles.

**Sources:**

1. saildrone.com/about

---

### 2016-04 — Sea Hunter ACTUV (DARPA + US Navy MDUSV)

- **id:** `sea-hunter-actuv-leidos-2016`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Leidos Inc. (Reston, VA, USA) for DARPA + ONR + US Navy
- **disclosure citation:** Leidos Inc. (Reston, VA, USA) for DARPA + ONR. Sea Hunter christened April 7, 2016; transitioned from DARPA to ONR February 2018. Anti-Submarine Warfare Continuous Trail Unmanned Vessel (ACTUV) program → Medium Displacement Unmanned Surface Vessel (MDUSV).
- **disclosed subsystems:** `usv`, `usv-mdusv`, `actuator-diesel`, `control-autonomy-stack`

**Prior art notes:**

> Sea Hunter ACTUV (Leidos for DARPA → ONR 2016+) is the first 132-foot autonomous trimaran MDUSV. 9-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid or USV claim deriving from medium-displacement autonomous ASW unmanned surface vessels.

**Sources:**

1. en.wikipedia.org/wiki/Sea_Hunter

---

### 2017-06 — iXblue / Exail DriX hydrographic USV

- **id:** `ixblue-drix-2017`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** iXblue / Exail (Saint-Germain-en-Laye, France)
- **disclosure citation:** iXblue (now Exail) (Saint-Germain-en-Laye, France). DriX demonstrated 2017 IHO centennial; formal launch October 2018. DriX O-16 (16 m, May 2024 sea trial).
- **disclosed subsystems:** `usv`, `actuator-diesel`, `control-autonomy-stack`

**Prior art notes:**

> iXblue / Exail DriX (Saint-Germain-en-Laye 2017+) is the French commercial USV market leader. 8-year-deep public-disclosure prior art. Direct shielding for any commercial humanoid or USV claim deriving from French-OEM hydrographic USVs with onboard AI.

**Sources:**

1. naval-technology.com/projects/drix-unmanned-surface-vessel-usv/

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
