---
title: "mechanism-quadcopter"
parent: "Invalidity Contentions"
nav_order: 215
layout: default
---

# Invalidity Contention Packet — `mechanism-quadcopter`

**Generated:** 2026-05-14  
**Cross-cut tag:** `mechanism-quadcopter`  
**Entries:** 3 (3 commons-grade, 0 draft)  
**Earliest disclosure:** 2010-01  
**Most recent disclosure:** 2018-02

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `mechanism-quadcopter`.

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

### 2010-01 — Parrot AR.Drone

- **id:** `parrot-ar-drone-2010`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Parrot SA (Paris, France)
- **disclosure citation:** Parrot SA (Paris, France). AR.Drone reveal CES 2010 + commercial release August 2010. AR.Drone 2.0 (2012); Bebop (2014). The first commercial WiFi-controllable consumer quadcopter with open developer SDK.
- **disclosed subsystems:** `mechanism-quadcopter`, `mechanism-aerial-thruster`

**Prior art notes:**

> Parrot AR.Drone (Parrot Paris 2010+) is the foundational commercial WiFi-controllable consumer quadcopter. 15-year-deep public-disclosure prior art. **Predates DJI Phantom (2013, round-35 entry) by 3 years**. Open developer SDK drove early academic robotics research. Together with Crazyflie (corpus) + DJI Phantom (round-35) + Skydio R1 (round-35), establishes the consumer-drone prior-art chain.

**Sources:**

1. Parrot AR.Drone CES 2010 announcement.
2. Wikipedia 'Parrot AR.Drone'.

---

### 2013-01 — DJI Phantom + Mavic consumer drone lineage

- **id:** `dji-phantom-2013`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** DJI (Da-Jiang Innovations, Shenzhen, China)
- **disclosure citation:** DJI (Da-Jiang Innovations Science and Technology Co., Shenzhen, China; founded 2006). Phantom 1 reveal January 2013. Subsequent Phantom 2/3/4, Mavic Pro/Air/Mini lineage. dji.com. **The dominant commercial consumer drone manufacturer worldwide** (~70%+ market share).
- **disclosed subsystems:** `mechanism-aerial-thruster`, `mechanism-quadcopter`, `control-flight-controller`

**Prior art notes:**

> DJI Phantom + Mavic (DJI Shenzhen 2013+) is the canonical dominant consumer drone lineage. 12-year-deep public-disclosure prior art with ~70%+ market share. **Architecturally adjacent to humanoid robotics** via the LEONARDO (corpus caltech-leonardo-2021) bipedal-aerial hybrid + FSTAR/FCSTAR (corpus round-14) wheel-leg-aerial hybrid lineage — both inherit propeller + IMU + flight-controller stacks from the consumer-drone industry.

**Sources:**

1. DJI corporate site (dji.com).
2. Wikipedia 'DJI'.

---

### 2018-02 — Skydio R1 / Skydio 2 autonomous drone

- **id:** `skydio-r1-2018`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Skydio, Inc. (Redwood City, CA); MIT alumni Adam Bry, Abe Bachrach, Matt Donahoe
- **disclosure citation:** Skydio, Inc. (Redwood City, CA; founded 2014 by MIT alumni Adam Bry, Abe Bachrach, Matt Donahoe). R1 reveal February 2018; Skydio 2 (2019); X10 (2024). skydio.com. **First commercial consumer drone with full computer-vision-based autonomy** (navigation + obstacle avoidance + tracking without GPS or manual control).
- **disclosed subsystems:** `mechanism-quadcopter`, `control-cv-autonomous-flight`, `control-obstacle-avoidance`, `control-subject-tracking`

**Prior art notes:**

> Skydio R1 (Skydio Redwood City 2018+) is the canonical computer-vision-based autonomous consumer drone. 7-year-deep public-disclosure prior art for: pure-CV autonomous flight + 360° obstacle avoidance + autonomous subject tracking. Direct shielding for any commercial humanoid claim on CV-based autonomous navigation through unstructured environments.

**Sources:**

1. Skydio corporate site (skydio.com).
2. Skydio R1 launch coverage February 2018.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `c61fc91`.*
