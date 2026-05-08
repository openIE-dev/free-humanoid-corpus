---
title: "mechanism-anthropomorphic-arm"
parent: "Invalidity Contentions"
nav_order: 64
layout: default
---

# Invalidity Contention Packet — `mechanism-anthropomorphic-arm`

**Generated:** 2026-05-07  
**Cross-cut tag:** `mechanism-anthropomorphic-arm`  
**Entries:** 6 (5 commons-grade, 1 draft)  
**Earliest disclosure:** 2016-04  
**Most recent disclosure:** 2025-02

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `mechanism-anthropomorphic-arm`.

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

### 2016-04 — OceanOne

- **id:** `oceanone-stanford-2016`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Stanford Robotics Laboratory; Oussama Khatib group; King Abdullah Univ. of Science and Technology partnership
- **disclosure citation:** Khatib, O., Yeh, X., Brantner, G., et al. 'Ocean One: A Robotic Avatar for Oceanic Discovery'. IEEE Robotics and Automation Magazine vol. 23 no. 4, 2016. First operational dive (La Lune wreck, Mediterranean, 100 m depth) April 2016.
- **disclosed subsystems:** `mechanism-thruster-vectored`, `mechanism-manipulator-arm`, `mechanism-anthropomorphic-arm`, `mechanism-anthropomorphic-hand`, `mechanism-pressure-hull`, `control-bilateral-teleop-haptic`, `control-operational-space`, `control-station-keeping`, `control-acoustic-comms`, `control-dvl-positioning`

**Prior art notes:**

> OceanOne is the canonical academic bimanual humanoid AUV. 9-year-deep open academic publication via the Khatib group at Stanford. Establishes element-by-element prior art for: 8-thruster vectored layout for humanoid AUV (exact match to free-humanoid-submersible commitment), bimanual 7-DoF anthropomorphic arms underwater, bilateral haptic teleoperation, F/T-sensor-in-the-loop manipulation, integration with Khatib's operational-space framework. Directly anticipates every architectural element of free-humanoid-submersible's design and any Aquanaut/Nauticus commercial claim on the same. The Khatib lineage extends back through Stanford operational-space papers to 1987 (38 years).

**Sources:**

1. Khatib et al. IEEE RAM 23(4) 2016.
2. G. Brantner, O. Khatib, 'Controlling Ocean One', Stanford Robotics Lab tech reports 2014-2016.
3. ICRA 2017 OceanOne workshop proceedings.

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

### 2021-03 — Memic Hominis

- **id:** `memic-hominis-2020`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Memic Innovative Surgery / Momentis Surgical (Israel)
- **disclosure citation:** Memic Innovative Surgery, Ltd. (Tel Aviv, Israel; now Momentis Surgical). FDA De Novo authorization March 1 2021 for transvaginal hysterectomy and salpingectomy/oophorectomy. memicmed.com / momentissurgical.com.
- **disclosed subsystems:** `mechanism-manipulator-arm`, `mechanism-anthropomorphic-arm`, `control-master-slave-teleoperation`

**Prior art notes:**

> Memic Hominis (FDA De Novo March 2021) is a canonical anthropomorphic-arm-kinematics surgical robotic system. 4-year-deep public-disclosure prior art for: humanoid-style (shoulder+elbow+wrist) surgical-arm kinematics, natural-orifice robotic surgery. Direct shielding for any commercial humanoid claim on anthropomorphic-arm-derivative surgical applications or natural-orifice manipulation. Together with da Vinci and Vicarious Surgical, establishes a 25-year commercial robotic-surgery prior-art chain that anticipates humanoid-form manipulator architectures from a different industrial vertical.

**Sources:**

1. Memic Innovative Surgery (memicmed.com / momentissurgical.com).
2. FDA De Novo authorization (DEN200067) March 1 2021.

---

### 2022-07 — OceanOneK

- **id:** `ocean-onek-stanford-2022`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Stanford Robotics Laboratory; Khatib group; expanded design team
- **disclosure citation:** Khatib, O., Brantner, G., Yeh, X., Salisbury, S. et al. 'OceanOneK: A 1000-meter-depth, bimanual underwater humanoid for archeology and marine exploration'. Science Robotics 2022 (announced July 2022). Subsequent IEEE RA-L publications detail control and pressure-hull innovations.
- **disclosed subsystems:** `mechanism-thruster-vectored`, `mechanism-manipulator-arm`, `mechanism-anthropomorphic-arm`, `mechanism-anthropomorphic-hand`, `mechanism-pressure-tolerant-actuator`, `mechanism-glass-sphere-buoyancy`, `control-bilateral-teleop-haptic`, `control-operational-space`, `control-station-keeping`

**Prior art notes:**

> OceanOneK extends the OceanOne lineage to 1000 m depth and adds pressure-tolerant oil-filled-actuator art. Directly shields any commercial humanoid AUV claim on: deep-depth (>500 m) bimanual humanoid manipulation, pressure-tolerant joint actuation (no rigid pressure hull on appendages), and integration of Khatib's 38-year operational-space framework with deep underwater manipulation. A 3-year-deep open-academic prior art chain with full element-by-element technical disclosure.

**Sources:**

1. Khatib et al. Science Robotics 2022.
2. Stanford Robotics Lab 'OceanOneK' project page (cs.stanford.edu/groups/manips/ocean-one-k/).
3. BBC, Le Monde, IEEE Spectrum coverage of Mediterranean shipwreck operations 2022-2023.

---

### 2024-01 — Fourier GR1

- **id:** `fourier-gr1-2024`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Fourier Intelligence (Shanghai, China)
- **disclosure citation:** Fourier Intelligence. GR1 humanoid product reveal January 2024 via fourierintelligence.com and CES 2024 demonstration. Subsequent deployments by academic teams (Open-TeleVision UCSD+MIT CoRL 2024 uses Fourier GR1 as one of its evaluation platforms).
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-arm`, `actuator-electric-quasi-direct-drive`

**Prior art notes:**

> Fourier GR1 is one of the canonical Chinese commercial humanoid platforms used by academic teams (alongside Unitree H1/G1, Booster K1). 1.5-year-deep public-disclosure prior art for: adult-class commercial humanoid sold to academic researchers as a hardware-only platform, interchangeable hand/gripper end-effectors. The Open-TeleVision academic publication (CoRL 2024) uses GR1 as one of two evaluation platforms, providing third-party documentation of the system's interfaces and capabilities. Direct shielding for any commercial humanoid claim on adult-class hardware-platform sales to academic researchers.

**Sources:**

1. Fourier Intelligence corporate site (fourierintelligence.com).
2. Cheng et al. 'Open-TeleVision' arXiv:2407.01512 CoRL 2024 (uses GR1 as evaluation platform).
3. CES 2024 coverage.

---

### 2025-02 — ToddlerBot

- **id:** `stanford-toddlerbot-2025`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Stanford Robotics Lab; Haochen Shi, Weizhuo Wang, Shuran Song, C. Karen Liu
- **disclosure citation:** Shi, H., Wang, W., Song, S., Liu, C. K. 'ToddlerBot: Open-Source ML-Compatible Humanoid Platform for Loco-Manipulation'. arXiv:2502.00893, February 2025. Conference on Robot Learning (CoRL) 2025 oral. Stanford Robotics Lab.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-arm`, `mechanism-3d-printed-platform`, `control-rl-policy`, `control-imitation-learning`, `control-sim-to-real`, `control-loco-manipulation`

**Prior art notes:**

> ToddlerBot is Stanford's canonical sub-$6k open-hardware ML-compatible humanoid (CoRL 2025 oral). Establishes 1-year-deep open-academic prior art for: integrated loco-manipulation policy training on an open humanoid platform, transferable motor system-ID for sim-to-real without hand-tuning, 30-DoF anthropomorphic full-body at sub-$6k. Direct shielding for any commercial claim on integrated full-body humanoid policy training, particularly any 'one policy controls the whole body' claim. Together with Berkeley Humanoid Lite, establishes the open-academic baseline for sub-$10k humanoid robotics.

**Sources:**

1. Shi, Wang, Song, Liu. arXiv:2502.00893 February 2025.
2. CoRL 2025 proceedings (proceedings.mlr.press/v305/shi25a.html).
3. Project page (toddlerbot.github.io).
4. GitHub: github.com/hshi74/toddlerbot.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `5228ded`.*
