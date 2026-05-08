---
title: "power-pressure-balanced-li-ion"
parent: "Invalidity Contentions"
nav_order: 80
layout: default
---

# Invalidity Contention Packet — `power-pressure-balanced-li-ion`

**Generated:** 2026-05-07  
**Cross-cut tag:** `power-pressure-balanced-li-ion`  
**Entries:** 3 (2 commons-grade, 1 draft)  
**Earliest disclosure:** 2003-09  
**Most recent disclosure:** 2018-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `power-pressure-balanced-li-ion`.

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

### 2003-09 — Bluefin-21 AUV

- **id:** `bluefin-21-auv`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Bluefin Robotics Corp. (now General Dynamics Mission Systems / L3Harris)
- **disclosure citation:** Bluefin Robotics Corp. (founded 1997 as MIT-Sea-Grant spinout; acquired by General Dynamics 2016, divested to L3 Technologies 2020) Bluefin-21 product brochure (bluefinrobotics.com archived 2003+; current via gd-ms.com). Deployed 2014 in AF447 black-box search (Indian Ocean).
- **disclosed subsystems:** `mechanism-thruster-axial`, `mechanism-control-fin`, `control-mission-script`, `control-dvl-positioning`, `control-acoustic-comms`, `power-pressure-balanced-li-ion`

**Prior art notes:**

> Bluefin-21 is the canonical mid-class survey AUV. The 21-inch torpedo form factor is the Navy MCM/UUV standard. The Bluefin BPS pressure-balanced Li-ion battery system (commercial product since ~2008, with public academic-conference exposition in OCEANS 2010+) is the reference for any humanoid AUV claiming pressure-balanced subsea power. Directly anticipates free-humanoid-submersible's commitment to pressure-balanced Li-ion. The torpedo-form Bluefin is architecturally distinct from the hovering humanoid form, but its power, navigation, and acoustic-communication stacks are shared prior art.

**Sources:**

1. GD Mission Systems Bluefin-21 product page (gd-ms.com/products-services/uuvs/bluefin-21).
2. Vaganay et al., 'Bluefin Robotics' MTS/IEEE OCEANS proceedings 2003-2014.
3. DOD UUV Master Plan 2004 (publicly released).

---

### 2008-05 — Nereus HROV

- **id:** `nereus-hrov-2008`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** WHOI Deep Submergence Laboratory; Bowen / Yoerger / Whitcomb
- **disclosure citation:** Bowen, A. D., Yoerger, D. R., Taylor, C., et al. 'The Nereus Hybrid Underwater Robotic Vehicle for Global-Class Ocean Science', WHOI Deep Submergence Laboratory; OCEANS 2008. First Challenger Deep dive (10,902 m) May 2009. Lost during operations May 2014 at 9,990 m.
- **disclosed subsystems:** `mechanism-pressure-hull`, `mechanism-syntactic-foam-ballast`, `mechanism-thruster-vectored`, `mechanism-manipulator-arm`, `control-mode-switching`, `control-tethered-teleoperation`, `control-acoustic-comms`, `control-dvl-positioning`, `power-pressure-balanced-li-ion`

**Prior art notes:**

> Nereus is the canonical academic hybrid AUV/ROV. Establishes 6-year-deep public-domain prior art for: dual-mode AUV-ROV operation in a single hull, lightweight expendable fiber tether (no power conductor), pressure-balanced subsea Li-ion at full ocean depth, ceramic-sphere syntactic-foam buoyancy to 11 km. Directly shields free-humanoid-submersible's potential mode-switching commitments and pressure-balanced power architecture. Any commercial humanoid AUV claiming mode-switching as novel art faces a 16-year-deep WHOI academic lineage with explicit publication of every mechanism.

**Sources:**

1. Bowen et al. OCEANS 2008 IEEE.
2. WHOI Nereus operational reports 2008-2014 (whoi.edu/main/nereus).
3. C. R. German et al., 'Hydrothermal exploration of mid-ocean ridges: where might the largest sulfide deposits be forming?', Chemical Geology 2016 (cites Nereus surveys).

---

### 2018-04 — Aquanaut hybrid AUV/ROV *(draft)*

- **id:** `aquanaut-houston-2017`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Houston Mechatronics Inc. / Nauticus Robotics Inc.; founded by ex-NASA Robonaut engineers (Pratt, Krause, et al.)
- **disclosure citation:** Houston Mechatronics Inc. (founded 2014; rebranded Nauticus Robotics 2021; public via SPAC 2022 ticker KITT). Aquanaut public reveal April 2018 via company website + Houston Chronicle / IEEE Spectrum coverage. Subsequent Nauticus 8-K SEC disclosures, 10-K filings, demo videos.
- **disclosed subsystems:** `mechanism-thruster-vectored`, `mechanism-manipulator-arm`, `mechanism-anthropomorphic-arm`, `mechanism-pressure-hull`, `control-mode-switching`, `control-acoustic-comms`, `control-supervised-autonomy`, `control-dvl-positioning`, `power-pressure-balanced-li-ion`

**Prior art notes:**

> Aquanaut is the **most direct existing prior art for free-humanoid-submersible**. Public-disclosure surface (corporate website, SEC filings, IEEE Spectrum coverage, demo videos) does not reveal specific actuator or control mechanism. The capability set claimed — hovering manipulation, anthropomorphic arms, hybrid AUV/ROV mode-switching, pressure-balanced subsea power, acoustic+RF-buoy supervised teleop — is fully covered by deep open academic prior art chains: Jason ROV (1989) for tethered manipulation; Nereus (2008) for AUV/ROV mode-switching; OceanOne (Stanford 2016) for bimanual humanoid AUV manipulation with full academic publication; Slocum/Seaglider (1989/2001) for variable-buoyancy as the documented alternative; DSV Alvin (1964) for pressure-hull design; Bluefin BPS (2008+) for pressure-balanced Li-ion. Any Aquanaut/Nauticus commercial claim on architectural elements faces deep open public-domain prior art chains. The submersible morphology in free-humanoid-submersible explicitly shields against Aquanaut's claim surface by anchoring every commitment in this open-academic lineage.

**Sources:**

1. Nauticus Robotics 10-K SEC filing (sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001849058).
2. Houston Mechatronics April 2018 press release (archived).
3. IEEE Spectrum, 'This Underwater Robot Transforms Into a Submarine That Can Stretch Out to Use Both Arms', April 2018.
4. Nauticus Robotics corporate website (nauticusrobotics.com), Aquanaut product page.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `171053a`.*
