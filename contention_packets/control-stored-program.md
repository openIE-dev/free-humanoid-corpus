---
title: "control-stored-program"
parent: "Invalidity Contentions"
nav_order: 142
layout: default
---

# Invalidity Contention Packet — `control-stored-program`

**Generated:** 2026-05-15  
**Cross-cut tag:** `control-stored-program`  
**Entries:** 5 (5 commons-grade, 0 draft)  
**Earliest disclosure:** 1804-01  
**Most recent disclosure:** 1968-01

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-stored-program`.

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

### 1804-01 — Jacquard Loom (Joseph Marie Jacquard 1804; punch-card programmable machine)

- **id:** `jacquard-loom-1804`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Joseph Marie Jacquard (Lyon, France, 1804); building on Bouchon (1725) + Falcon (1728) + Vaucanson (1745)
- **disclosure citation:** Joseph Marie Jacquard. The Jacquard machine (an attachment for the drawloom), patented 1804 in Lyon, France. Built on earlier punch-card / perforated-cylinder loom mechanisms by Basile Bouchon (1725), Jean-Baptiste Falcon (1728), and Jacques de Vaucanson (1745, corpus).
- **disclosed subsystems:** `automaton-historical`, `control-stored-program`

**Prior art notes:**

> The Jacquard Loom (Joseph Marie Jacquard Lyon 1804) is the first practical large-scale programmable machine. 221-year-deep public-domain prior art. The conceptual ancestor of all programmable automation + stored-program computation.

**Sources:**

1. Jacquard, J.M. French Patent (1804).

---

### 1952-03 — MIT Numerical Control (NC machine tool; 1952)

- **id:** `mit-numerical-control-1952`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** MIT Servomechanisms Laboratory + John T. Parsons + US Air Force
- **disclosure citation:** MIT Servomechanisms Laboratory (with John T. Parsons + US Air Force). First numerically-controlled milling machine demonstrated March 1952 (a modified Cincinnati Hydrotel). Parsons conceived the idea ~1948-1949; MIT built the prototype 1949-1952; the APT (Automatically Programmed Tool) language followed (Douglas T. Ross, 1956-1959).
- **disclosed subsystems:** `manipulator-arm`, `control-numerical`, `control-stored-program`

**Prior art notes:**

> MIT Numerical Control (MIT Servomechanisms Lab + Parsons + USAF 1952; APT language 1956-1959) is the first numerically-controlled machine tool. 73-year-deep public-domain prior art. The bridge from Jacquard punch cards to modern CNC + industrial robots.

**Sources:**

1. MIT Servomechanisms Laboratory NC machine documentation, 1952.

---

### 1954-12 — Devol Programmed Article Transfer (foundational arm patent)

- **id:** `devol-programmed-article-transfer-1954`
- **corpus:** academic
- **ip status:** public-domain (expired)
- **creator:** George C. Devol Jr.; later Unimation co-founder with Joseph Engelberger
- **disclosure citation:** Devol, G.C. 'Programmed Article Transfer'. US Patent 2,988,237; filed December 10, 1954; granted June 13, 1961. The originating patent for programmable manipulator arms. George Devol subsequently co-founded Unimation with Joseph Engelberger 1956.
- **disclosed subsystems:** `manipulator-arm`, `control-stored-program`

**Prior art notes:**

> Devol's 1954 'Programmed Article Transfer' patent (US 2,988,237) is the originating patent for programmable manipulator arms. 71-year-deep public-domain prior art. The foundational predicate for every commercial robot arm. Direct shielding for any commercial humanoid claim deriving from programmable position-controlled manipulator arms.

**Sources:**

1. US Patent 2,988,237 'Programmed Article Transfer'.
2. automate.org/robotics/engelberger/joseph-engelberger-unimate

---

### 1961-01 — Unimate (the first industrial robot arm)

- **id:** `unimate-unimation-1961`
- **corpus:** private
- **ip status:** public-domain
- **creator:** Unimation Inc. (Danbury, CT, USA); George Devol + Joseph Engelberger
- **disclosure citation:** Devol, G.C. + Engelberger, J.F. / Unimation Inc. (Danbury, CT, USA; founded 1956). Unimate first deployed at GM Inland Fisher Guide plant, Ewing Township NJ, 1961. The first industrial robot arm. Robot Hall of Fame inductee 2003.
- **disclosed subsystems:** `manipulator-arm`, `actuator-hydraulic`, `control-stored-program`

**Prior art notes:**

> Unimate (Unimation Danbury CT 1961) is the first industrial robot arm. 64-year-deep public-domain prior art. Direct shielding for any commercial humanoid claim deriving from industrial articulated robot arms. The Kawasaki 1968 license seeded the entire Japanese arm-OEM industry; the Stäubli 1989 acquisition transferred the lineage to Europe.

**Sources:**

1. en.wikipedia.org/wiki/Unimate
2. automate.org/robotics/engelberger/joseph-engelberger-unimate

---

### 1968-01 — Modicon 084 PLC (Dick Morley 1968; the first Programmable Logic Controller)

- **id:** `modicon-plc-morley-1968`
- **corpus:** private
- **ip status:** public-domain (foundational concept; Modicon now Schneider Electric)
- **creator:** Bedford Associates → Modicon (Bedford, MA, USA); Richard 'Dick' Morley
- **disclosure citation:** Bedford Associates (Bedford, MA, USA; Richard 'Dick' Morley + team). Modicon 084 — the first commercial Programmable Logic Controller — developed 1968-1969 in response to a 1968 GM Hydramatic Division request for a solid-state replacement for hard-wired relay logic. Modicon = MOdular DIgital CONtroller.
- **disclosed subsystems:** `control-industrial`, `control-stored-program`

**Prior art notes:**

> The Modicon 084 PLC (Dick Morley / Bedford Associates 1968-1969) is the first Programmable Logic Controller. 57-year-deep public-disclosure prior art. The universal industrial controller — ancestor of every robot controller + automated factory.

**Sources:**

1. Modicon 084 Smithsonian documentation.
2. Morley, R. 'The Technology Machine' interviews.

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
