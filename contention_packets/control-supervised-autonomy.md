---
title: "control-supervised-autonomy"
parent: "Invalidity Contentions"
nav_order: 110
layout: default
---

# Invalidity Contention Packet — `control-supervised-autonomy`

**Generated:** 2026-05-09  
**Cross-cut tag:** `control-supervised-autonomy`  
**Entries:** 3 (2 commons-grade, 1 draft)  
**Earliest disclosure:** 2015-06  
**Most recent disclosure:** 2020-01

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-supervised-autonomy`.

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

### 2015-06 — DRC-HUBO+ (DARPA Robotics Challenge winner)

- **id:** `kaist-drc-hubo-2015`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** KAIST Humanoid Robot Research Center; Jun-Ho Oh group + Rainbow Robotics
- **disclosure citation:** KAIST + Rainbow Robotics. 'DRC-HUBO+: A robotic platform for the DARPA Robotics Challenge'. Lim, J., Lee, I., Shim, I., et al. International Journal of Robotics Research / Journal of Field Robotics 2017. Won 1st place at DARPA Robotics Challenge Finals Pomona June 2015 — completing all 8 disaster-response tasks in 44m28s. The follow-on commercial version was Rainbow Robotics' first product (corpus has rainbow-robotics-rb-y1 as the modern commercial successor).
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-wheel-leg-hybrid`, `actuator-electric`, `control-whole-body-qp`, `control-supervised-autonomy`

**Prior art notes:**

> DRC-HUBO+ (KAIST + Rainbow Robotics, DRC 2015) is the canonical Korean academic humanoid milestone — 1st place winner of the DARPA Robotics Challenge Finals June 2015. 10-year-deep public-domain prior art for: wheel-leg hybrid transformable bipedal humanoid (knee-rolling for stability + bipedal for stairs), operator-supervised whole-body autonomy under intermittent comm. Direct shielding for any commercial humanoid claim on transformable lower-body morphology or DRC-class disaster-response capability set. Established Rainbow Robotics' commercial humanoid lineage (corpus entry rainbow-robotics-rb-y1).

**Sources:**

1. Lim, J. et al. JFR / IJRR 2017.
2. DARPA Robotics Challenge Finals 2015 Pomona results.
3. KAIST Humanoid Robot Research Center publications.
4. IEEE Spectrum coverage 'Korean Team Wins DARPA Robotics Challenge' 2015.

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

### 2020-01 — ISRO Vyommitra (Gaganyaan humanoid)

- **id:** `isro-vyommitra-2020`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Indian Space Research Organisation (ISRO); Vikram Sarabhai Space Centre, Thiruvananthapuram
- **disclosure citation:** Indian Space Research Organisation (ISRO). Vyommitra reveal January 22 2020 at Symposium on Human Spaceflight, Bengaluru. Vikram Sarabhai Space Centre (Thiruvananthapuram, Kerala) led design + fabrication. Planned first space flight: Gaganyaan-1 Q4 2025; subsequent Gaganyaan-2 2026. The first Indian humanoid robot for space.
- **disclosed subsystems:** `mechanism-anthropomorphic-arm`, `mechanism-half-humanoid`, `control-supervised-autonomy`, `control-bilingual-speech`, `sensing-cabin-environment`

**Prior art notes:**

> ISRO Vyommitra is the canonical Indian humanoid space-robot (2020+, Gaganyaan-1 launch Q4 2025). 5-year-deep public-domain prior art for: half-humanoid (no-legs) anthropomorphic upper-body for spacecraft cabin operation, bilingual (Hindi + English) speech-interfaced robot, female-form humanoid for crew-substitute missions. Direct architectural successor to NASA Robonaut 1+2 (corpus entries) for ISS deployment. **The first humanoid-robot entry from India in the corpus** — closes a major regional gap.

**Sources:**

1. ISRO Vyommitra announcement (pib.gov.in/PressReleasePage.aspx?PRID=2002418).
2. Wikipedia 'Vyommitra' (en.wikipedia.org/wiki/Vyommitra).
3. The Print, GKToday, MakerSmuse coverage 2020-2025.
4. Symposium on Human Spaceflight, Bengaluru, January 2020.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `bd98079`.*
