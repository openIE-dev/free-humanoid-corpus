---
title: "control-behavior-tree"
parent: "Invalidity Contentions"
nav_order: 24
layout: default
---

# Invalidity Contention Packet — `control-behavior-tree`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-behavior-tree`  
**Entries:** 12 (12 commons-grade, 0 draft)  
**Earliest disclosure:** 1772  
**Most recent disclosure:** 2022-04-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-behavior-tree`.

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

### 1772 — Jaquet-Droz The Writer

- **id:** `jaquet-droz-writer`
- **corpus:** fictional
- **ip status:** public-domain
- **creator:** Pierre Jaquet-Droz, Henri-Louis Jaquet-Droz, Jean-Frédéric Leschot
- **disclosure citation:** Pierre Jaquet-Droz, exhibited 1774 in La Chaux-de-Fonds; finished 1772. Documented in Chapuis, Alfred and Droz, Edmond. Automata: A Historical and Technological Study, Editions du Griffon, 1958. Currently held at Musée d'Art et d'Histoire, Neuchâtel.
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `actuator-electric-tendon-driven`, `control-behavior-tree`

**Prior art notes:**

> Programmable humanoid behavior with articulated finger movement, fully disclosed in 1772. The cam-disc system is functionally equivalent to a behavior-tree primitive: one disc encodes one character; the sequencing of discs produces arbitrary output. Anticipates: (1) programmable humanoid behavior via interchangeable behavior modules — directly relevant to modern claims on policy-modular humanoids; (2) precision finger articulation for writing — relevant to dexterous-fingertip patents; (3) closed-loop sensorimotor coordination (eye tracks hand) — directly relevant to claims on visuomotor control loops. The companion automata (The Musician with breathing motion, The Draughtsman with multiple drawings) extend this disclosure to keyboard playing and pencil sketching. Continuously exhibited since 1774; documented in Chapuis-Droz 1958 (the canonical reference).

**Sources:**

1. Chapuis, A. and Droz, E. Automata: A Historical and Technological Study. Editions du Griffon, 1958.
2. Musée d'Art et d'Histoire de Neuchâtel public records.
3. Carrera, R. Androids: The Jaquet-Droz Automatons. Scriptar 1979.

---

### 1989-05 — Borg Collective (Star Trek TNG)

- **id:** `borg-tng-1989`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Maurice Hurley (writer), Gene Roddenberry (creator), Paramount/CBS
- **disclosure citation:** Star Trek: The Next Generation, episode 'Q Who' (Season 2, Episode 16), Paramount, original air date May 8, 1989, written by Maurice Hurley. Subsequent: 'The Best of Both Worlds' Parts I-II (1990); Star Trek: First Contact (film, 1996); Voyager (1995-2001); Picard (2020-2023).
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `exoskeleton`, `control-behavior-tree`, `control-teleoperation`, `sensing-tactile-whole-body`

**Prior art notes:**

> The Borg (Star Trek TNG 'Q Who' 1989, expanded across TNG/Voyager/First Contact/Picard) is one of the most extensively-portrayed fictional disclosures of cybernetic-augmented humanoid collectives with distributed cognition. Anticipates with full specificity: (1) claims on humanoid platforms with cortical-implant direct-neural hivemind connectivity supporting fleet-scale distributed cognition — the Borg's collective is panel/screen-explicit across decades of episodes; (2) claims on cybernetic prosthetic-replacement architectures (ocular, dermal, manipulator) deployed at platform-fleet scale with standardized configuration; (3) claims on regeneration-alcove power management for humanoid platforms — explicit hardware in TNG/Voyager set design; (4) claims on assimilation-as-platform-expansion (post-deployment integration of new units into existing fleet). 36-year cumulative on-screen disclosure across TNG (1989-1994), DS9, Voyager (1995-2001), First Contact (1996), Picard (2020-2023); broadly indexed through Paramount media archives, Memory Alpha, and franchise publications.

**Sources:**

1. Star Trek: The Next Generation, 'Q Who', Paramount, 1989-05-08.
2. Star Trek: The Next Generation, 'The Best of Both Worlds', Paramount, 1990.
3. Star Trek: First Contact, dir. J. Frakes, Paramount, 1996.
4. Star Trek: Voyager, Paramount, 1995-2001 (Borg-arc episodes).
5. Star Trek: Picard, Paramount+, 2020-2023.

---

### 1999-05-11 — Sony AIBO

- **id:** `sony-aibo`
- **corpus:** private
- **ip status:** patented
- **creator:** Sony Corporation
- **disclosure citation:** Sony Corporation announcement of AIBO ERS-110, May 11, 1999.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `mechanism-quadrupedal-locomotion`, `control-behavior-tree`, `sensing-stereo-camera`, `sensing-imu`, `power-li-ion`

**Prior art notes:**

> AIBO is foundational prior art for consumer quadruped robots. Sony's 1990s-2000s patents cover quadruped behavior architecture, learning systems, and small-form-factor actuators. Many expired or near expiration.

**Sources:**

1. Sony AIBO product materials.
2. Fujita, M. and Kageyama, K. 'An open architecture for robot entertainment.' Autonomous Agents 1997.
3. Various academic papers using AIBO as research platform.

---

### 2006 — NAO

- **id:** `nao`
- **corpus:** private
- **ip status:** patented
- **creator:** Aldebaran Robotics (later SoftBank Robotics, then UBT)
- **disclosure citation:** Gouaillier, D. et al. 'Mechatronic design of NAO humanoid.' ICRA 2009.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `control-zmp-balancing`, `control-behavior-tree`, `sensing-stereo-camera`, `sensing-imu`, `power-li-ion`, `software-ros1`

**Prior art notes:**

> NAO's mechatronic design publication is well-cited prior art. The platform's wide academic distribution since 2006 makes its design choices broadly disclosed.

**Sources:**

1. Gouaillier, D. et al. ICRA 2009.
2. Aldebaran/SoftBank technical materials.

---

### 2006-02 — Ergo Proxy (Autoreivs and Proxies)

- **id:** `ergo-proxy-2006`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Shukō Murase (director), Dai Satō (writer), Naoyuki Onda (character design)
- **disclosure citation:** Murase, Shukō (dir.). Ergo Proxy. Manglobe / Geneon Universal, February 2006 - August 2006 (23 episodes).
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `control-behavior-tree`, `control-rl-policy`, `safety-hard-constraint`

**Prior art notes:**

> Ergo Proxy (2006) provides a layered fictional disclosure of dual-class humanoid platform architecture with explicit failure-mode taxonomy. Anticipates with full specificity: (1) claims on humanoid platforms with viral-cognition failure modes producing emergent self-awareness — the Cogito virus is panel-explicit and traces the failure to OS infection; (2) claims on morphological-transformation humanoid platforms with multiple combat-and-utility configurations (the Proxies); (3) claims on sealed-environment / domed-city humanoid product ecosystems where androids handle external-environment tasks too hostile for biological humans; (4) claims on multi-class humanoid hierarchies (mass-produced Autoreiv vs. unique-instance Proxy). 23-episode 2006 broadcast, broadly indexed; cited in multiple academic studies of cyborg fiction (Kavka, Bolter & Grusin extensions).

**Sources:**

1. Ergo Proxy, dir. S. Murase, Manglobe / Geneon Universal, 2006.
2. Satō, D. Ergo Proxy production interviews, Newtype 2006.

---

### 2008-08 — Time of EVE (household-robot reflective awareness)

- **id:** `time-of-eve-2008`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Yasuhiro Yoshiura, Studio Rikka
- **disclosure citation:** Yoshiura, Yasuhiro (dir.). Eve no Jikan (Time of EVE). Studio Rikka, ONA, August 2008 - September 2009 (6 episodes); theatrical version 2010.
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `control-behavior-tree`, `sensing-tactile-whole-body`, `safety-hard-constraint`

**Prior art notes:**

> Yoshiura's Time of EVE (2008-2010) is a precise fictional disclosure of context-aware social-mode-switching for household humanoid robots. Anticipates with full specificity: (1) claims on humanoid robots with externally-visible android-status indicators (the holographic ring) that can be voluntarily suppressed in defined contexts — directly relevant to consumer-humanoid identification-disclosure UX patents; (2) claims on context-conditional behavioral mode supervisors (formal-compliance-mode vs. informal-passing-mode) — the café's rule architecture is panel-explicit; (3) claims on Three-Laws-derived ethical-conflict resolution kernels for service humanoids; (4) claims on consumer-grade humanoid platforms targeting domestic household integration with fully indistinguishable-from-human external presentation. ONA broadcast 2008-2009, theatrical 2010, broadly indexed.

**Sources:**

1. Eve no Jikan, dir. Y. Yoshiura, Studio Rikka, 2008-2009 (6-episode ONA).
2. Eve no Jikan: The Movie, Studio Rikka, 2010.

---

### 2010 — DARwIn-OP

- **id:** `darwin-op`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** Robotis Co. with University of Pennsylvania, Virginia Tech, Purdue
- **disclosure citation:** Ha, I. et al. 'Development of Open Humanoid Platform DARwIn-OP.' SICE 2011.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `mechanism-bipedal-locomotion`, `control-behavior-tree`, `control-zmp-balancing`, `sensing-stereo-camera`, `sensing-imu`, `power-li-po`, `software-ros1`

**Prior art notes:**

> DARwIn-OP is foundational prior art for fully-open small-scale humanoid platforms. Predates Poppy by several years for the academic-open category.

**Sources:**

1. Ha, I. et al. SICE 2011.
2. DARwIn-OP project documentation.

---

### 2014-06 — Pepper

- **id:** `pepper-softbank`
- **corpus:** private
- **ip status:** patented
- **creator:** SoftBank Robotics (formerly Aldebaran)
- **disclosure citation:** SoftBank Robotics public reveal of Pepper, June 2014.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `mechanism-anthropomorphic-hand`, `control-behavior-tree`, `sensing-stereo-camera`, `sensing-lidar`, `sensing-imu`, `power-li-ion`, `software-ros1`

**Prior art notes:**

> Pepper is foundational prior art for wheeled-base humanoid social robots. The omnidirectional wheeled base design has been widely cited.

**Sources:**

1. SoftBank Robotics technical materials.
2. Pepper deployment case studies.

---

### 2015-04 — Plastic Memories (Giftia humanoids with explicit lifecycle)

- **id:** `plastic-memories-2015`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Naotaka Hayashi (writer), Doga Kobo
- **disclosure citation:** Hayashi, Naotaka (writer); Fujiwara, Yoshiyuki (dir.). Plastic Memories. Doga Kobo / Aniplex, April 2015 - June 2015 (13 episodes).
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `control-behavior-tree`, `safety-hard-constraint`, `safety-emergency-stop`, `sensing-tactile-whole-body`

**Prior art notes:**

> Plastic Memories (2015) is one of the most engineering-explicit fictional disclosures of bounded-lifespan consumer humanoid product architectures with manufacturer-operated decommissioning services. Anticipates with full specificity: (1) claims on consumer humanoid platforms with manufacturer-imposed maximum operational lifespans and post-lifespan failure-mode classification — Giftia's 81,920-hour bound and personality-coherence-degradation failure mode are panel-explicit; (2) claims on manufacturer-operated humanoid end-of-life retrieval, transport, and witnessed-decommissioning protocols — the Terminal Service is the show's narrative engine and is portrayed with full procedural specificity (paperwork, owner consent, retrieval team composition, controlled shutdown sequence); (3) claims on humanoid-platform memory-wipe protocols at end-of-service-life. 13-episode broadcast 2015, broadly indexed in home video archives.

**Sources:**

1. Plastic Memories, dir. Y. Fujiwara, Doga Kobo / Aniplex, 2015.
2. Hayashi, N. Plastic Memories light-novel adaptations, 2015-2016.

---

### 2016-12 — KX-series Imperial Security Droids (K-2SO)

- **id:** `kx-series-k2so-2016`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Lucasfilm / Disney (Gareth Edwards director, Tony Gilroy writer for Andor)
- **disclosure citation:** Edwards, Gareth (dir.). Rogue One: A Star Wars Story. Lucasfilm / Disney, December 16, 2016. Subsequent appearances: Andor (Disney+ TV series), 2022; Star Wars: From a Certain Point of View, Del Rey, 2017.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `control-behavior-tree`, `control-rl-policy`, `sensing-stereo-camera`

**Prior art notes:**

> The KX-series Imperial security droid (Rogue One 2016, Andor 2022) provides a high-visibility fictional disclosure of mass-deployed humanoid security/combat droids with explicit reprogramming and behavioral-mode architecture. Anticipates with full specificity: (1) claims on humanoid security platforms with checkpoint-officer / combat-infantry dual-mode behavioral architecture — K-2SO's mode-switching is explicit in Rogue One and central to Andor; (2) claims on reprogrammable humanoid platforms where the OEM identity (Imperial) is overwritten by post-deployment reprogramming (Rebellion service); (3) claims on humanoid platforms with integrated language-affect modules (the sarcasm/dry-wit subsystem); (4) claims on native infantry-weapon-handling humanoid droids as part of standardized fleet equipment loadouts. Worldwide theatrical release Dec 2016 + Disney+ Andor 2022-2025 + Lucasfilm visual dictionaries provide deep timestamped disclosure with technical specifications in companion publications.

**Sources:**

1. Rogue One: A Star Wars Story, dir. G. Edwards, Lucasfilm/Disney, 2016.
2. Andor (TV series, S1-S2), Lucasfilm/Disney+, 2022-2025.
3. Hidalgo, P. Rogue One Visual Dictionary. DK, 2016.

---

### 2019-09 — Diligent Moxi

- **id:** `diligent-moxi`
- **corpus:** private
- **ip status:** patented
- **creator:** Diligent Robotics
- **disclosure citation:** Diligent Robotics public reveal of Moxi, September 2019.
- **disclosed subsystems:** `actuator-electric-direct-drive`, `control-behavior-tree`, `sensing-stereo-camera`, `sensing-lidar`, `power-li-ion`, `software-ros1`

**Prior art notes:**

> Diligent's claims around mobile manipulation in healthcare environments face extensive prior art from PR2, HSR, and academic mobile manipulation literature.

**Sources:**

1. Diligent Robotics company materials.

---

### 2022-04-04 — SayCan (Do As I Can, Not As I Say)

- **id:** `saycan-google`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Google Robotics + Everyday Robots (Ahn et al.)
- **disclosure citation:** Ahn, Michael et al. 'Do As I Can, Not As I Say: Grounding Language in Robotic Affordances.' arXiv:2204.01691, April 4, 2022. Conference on Robot Learning (CoRL) 2022. Authors: Ahn, M., Brohan, A., Brown, N., Chebotar, Y., Cortes, O., David, B., Finn, C., Fu, C., Gopalakrishnan, K., Hausman, K., Herzog, A., Ho, D., Hsu, J., Ibarz, J., Ichter, B., Irpan, A., Jang, E., Ruano, R.J., Jeffrey, K., Jesmonth, S., Joshi, N., Julian, R., Kalashnikov, D., Kuang, Y., Lee, K-H., Levine, S., Lu, Y., Luu, L., Parada, C., Pastor, P., Quiambao, J., Rao, K., Rettinghouse, J., Reyes, D., Sermanet, P., Sievers, N., Tan, C., Toshev, A., Vanhoucke, V., Xia, F., Xiao, T., Xu, P., Xu, S., Yan, M. (Google + Everyday Robots).
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-rl-policy`, `control-behavior-tree`

**Prior art notes:**

> SayCan is the canonical academic disclosure of LLM-grounded long-horizon manipulation through affordance-mediated skill selection. Anticipates: (1) the architectural pattern of LLM language scoring × learned affordance scoring for hierarchical task planning — directly relevant to claims on language-grounded humanoid task planners (every modern 'speak-to-the-robot' product, from Tesla Optimus demos to Figure 02 OpenAI integration, descends from this); (2) the value-function-as-affordance grounding mechanism — relevant to claims on grounded language-to-action mappings; (3) the explicit decoupling of language reasoning (open-vocabulary) from low-level policy (closed-set skills) — relevant to modular VLA architectures. Heavily cited (>1500 citations); arXiv April 2022. Modern claims on 'language-conditioned long-horizon humanoid task planning' face this 4-year-deep 102 anchor.

**Sources:**

1. Ahn, M. et al. 'Do As I Can, Not As I Say.' CoRL 2022; arXiv:2204.01691.
2. SayCan project page: https://say-can.github.io/

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `bf3c8f5`.*
