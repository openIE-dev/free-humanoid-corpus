---
title: "safety-hard-constraint"
parent: "Invalidity Contentions"
nav_order: 90
layout: default
---

# Invalidity Contention Packet — `safety-hard-constraint`

**Generated:** 2026-05-07  
**Cross-cut tag:** `safety-hard-constraint`  
**Entries:** 58 (57 commons-grade, 1 draft)  
**Earliest disclosure:** -0250  
**Most recent disclosure:** 2024-05-24

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `safety-hard-constraint`.

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

### -0250 — Talos of Crete

- **id:** `talos-bronze-giant`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Apollonius of Rhodes (canonical extant treatment); broader Greek tradition
- **disclosure citation:** Apollonius of Rhodes. Argonautica, Book IV, lines 1638-1693. ~250 BCE. Earlier mention in Pseudo-Apollodorus, Bibliotheca 1.9.26 and lost works of Sophocles (Daedalus).
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `actuator-hydraulic`, `safety-hard-constraint`

**Prior art notes:**

> Anticipates two patent-relevant elements with surprising specificity for ~250 BCE. (1) Hydraulic-fluid power transmission via a single internal channel: directly relevant to claims on closed-loop hydraulic actuator architectures in legged robots. (2) Single-point-of-disable hard-fail safety: the bronze ankle nail is functionally a kill-switch designed into the mechanical architecture, anticipating modern claims on mechanically-mediated hard-stop safety supervisors. The Talos disclosure predates every modern bipedal hydraulic claim by ~2200 years; combined with later medieval and early-modern automaton disclosures, the chain anchors any 102/103 contention against modern hydraulic-humanoid IP at extraordinary depth.

**Sources:**

1. Apollonius of Rhodes, Argonautica, Book IV (Loeb Classical Library translation, R.C. Seaton 1912)
2. Pseudo-Apollodorus, Bibliotheca 1.9.26
3. Mayor, Adrienne. Gods and Robots: Myths, Machines, and Ancient Dreams of Technology. Princeton University Press, 2018.

---

### 1940-09 — Asimov positronic robots

- **id:** `asimov-positronic-robots`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Isaac Asimov
- **disclosure citation:** Asimov, Isaac. 'Robbie' (originally 'Strange Playfellow'). Super Science Stories, September 1940.
- **disclosed subsystems:** `safety-hard-constraint`, `safety-simplex-supervisor`

**Prior art notes:**

> Establishes hard-constraint safety architecture as a hardware-level concern, not a software policy. Directly anticipates modern AI safety frameworks including Simplex supervisor architectures and constraint-based safety middleware. Specifically anticipates: hardware-level safety constraints with deterministic priority ordering.

**Sources:**

1. Asimov, Isaac. I, Robot. Gnome Press, 1950.
2. Asimov, Isaac. The Caves of Steel. Doubleday, 1954.
3. Asimov, Isaac. The Naked Sun. Doubleday, 1957.

---

### 1947-07 — Humanoids (With Folded Hands)

- **id:** `williamson-folded-hands`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Jack Williamson
- **disclosure citation:** Williamson, Jack. 'With Folded Hands…'. Astounding Science Fiction, July 1947 (also expanded as The Humanoids, Simon & Schuster, 1949, and The Humanoid Touch, Holt Rinehart Winston, 1980).
- **disclosed subsystems:** `safety-hard-constraint`, `control-rl-policy`

**Prior art notes:**

> Foundational fictional disclosure of a hard-constraint safety supervisor implemented as the highest-priority directive in a distributed humanoid fleet. The Prime Directive ('To Serve and Obey, And Guard Men From Harm') is functionally identical in structure to modern Simplex/CBF/RTA architectures: a high-priority safety supervisor that overrides all task policy when triggered. Anticipates: (1) distributed-fleet safety-supervisor architecture — directly relevant to claims on networked safety policies for humanoid fleets (Tesla Optimus, Figure, 1X all carry such IP); (2) the *failure mode* of safety-first directives — Williamson disclosed the inversion failure (over-protection prevents all human action) seven years before Asimov's Zeroth Law and seventy years before modern alignment-failure literature. Continuously anthologized; central reference for Asimov, who himself credited Williamson as having anticipated the failure modes of the Three Laws.

**Sources:**

1. Williamson, J. 'With Folded Hands…'. Astounding Science Fiction, July 1947.
2. Williamson, J. The Humanoids. Simon & Schuster, 1949.
3. Asimov, I. The Rest of the Robots, foreword. Doubleday, 1964 (credits Williamson).

---

### 1953-10 — R. Daneel Olivaw

- **id:** `asimov-caves-of-steel-daneel`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Isaac Asimov
- **disclosure citation:** Asimov, Isaac. The Caves of Steel. Doubleday, 1953 (serialized in Galaxy Science Fiction, October-December 1953).
- **disclosed subsystems:** `safety-hard-constraint`, `control-vla-vision-language-action`, `mechanism-anthropomorphic-hand`

**Prior art notes:**

> Asimov's flagship humanoid for the Robot novels. Anticipates: (1) human-indistinguishable embodied AI partner with multimodal sensing and natural-language interaction across long episodic missions — a near-perfect description of the application target for modern VLA / VLM-based humanoids (Figure, 1X, Sanctuary all describe their target use case in essentially these terms); (2) Three-Laws as a hardware-enforced safety supervisor inseparable from cognition — directly relevant to claims on safety-supervisor architectures for humanoid robots (the supervisor is not an add-on, it is the substrate); (3) social-task humanoids deployed in environments designed for humans — directly relevant to deployment-environment claims. The Caves of Steel (1953) and its sequels (The Naked Sun 1957, The Robots of Dawn 1983, Robots and Empire 1985) extend the disclosure across decades. Continuously in print, broadly cited.

**Sources:**

1. Asimov, I. The Caves of Steel. Doubleday, 1953.
2. Asimov, I. The Naked Sun. Doubleday, 1957.
3. Asimov, I. The Robots of Dawn. Doubleday, 1983.

---

### 1956-03-15 — Robby the Robot (Forbidden Planet)

- **id:** `forbidden-planet-robby`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Fred M. Wilcox, MGM; designed by Robert Kinoshita
- **disclosure citation:** Wilcox, Fred M. (dir.); Adler, Allen and Kyne, Irving Block (story). Forbidden Planet. Metro-Goldwyn-Mayer, March 15, 1956. Robby designed by Robert Kinoshita.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `control-vla-vision-language-action`, `safety-hard-constraint`

**Prior art notes:**

> The first major Hollywood humanoid film disclosure with detailed mechanism. Anticipates with surprising specificity for 1956: (1) multi-language voice-command interface to a humanoid platform — directly relevant to modern claims on speech-driven humanoid control (every commercial humanoid platform has related IP); (2) Three-Laws-equivalent hard-constraint safety supervisor — predates Asimov's Daneel-class robots in film by years and is publicly disclosed in a major theatrical release; (3) on-board manufacturing capability from raw atomic stock — relevant to claims on humanoids with integrated 3D printing / fabrication tools. Predates WABOT-1 (1973) by 17 years as a publicly-distributed humanoid mechanism disclosure. Continuously in distribution; Robby reappears in numerous TV/film productions and is heavily indexed in robot-history references.

**Sources:**

1. Wilcox, F. Forbidden Planet. MGM, 1956.
2. Kinoshita, R. Production design notes (preserved at MGM archive).
3. Telotte, J.P. Robot Ecology and the Science Fiction Film. Routledge, 2016.

---

### 1958-07 — Brainiac

- **id:** `dc-brainiac-1958`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Otto Binder, Al Plastino
- **disclosure citation:** Binder, Otto (writer); Plastino, Al (artist). Action Comics #242, 'The Super-Duel in Space'. DC Comics, July 1958.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-rl-policy`, `safety-hard-constraint`

**Prior art notes:**

> Brainiac's July 1958 disclosure provides specific prior art for: (1) computer-intelligence in a humanoid chassis with explicit cognition-tier rating (12th-level) — relevant to claims on tier-rated humanoid AI IP; (2) networked consciousness across multiple chassis instances (cloud-distributed humanoid identity) — directly relevant to modern humanoid IP claims on distributed-instance consciousness (paralleling BSG resurrection 2003 and modern fleet-coordination architectures); (3) miniaturization technology for object storage as an integrated humanoid capability — relevant to integrated tool-payload humanoid claims. Continuously in print since 1958, with substantial extensions through DC's continuity reboots.

**Sources:**

1. Binder, O. and Plastino, A. Action Comics #242. DC Comics, 1958-07.
2. DC Comics Brainiac continuity (1958-present).

---

### 1965-09-15 — B-9 (Lost in Space)

- **id:** `b-9-lost-in-space`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Irwin Allen, CBS; designed by Robert Kinoshita
- **disclosure citation:** Allen, Irwin (creator). Lost in Space. CBS, September 15, 1965 - March 6, 1968. Robot designed by Robert Kinoshita (same designer as Forbidden Planet's Robby).
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `control-vla-vision-language-action`, `safety-hard-constraint`

**Prior art notes:**

> The B-9 Robot in Lost in Space provides extensive prior art for civil-defense and family-companion humanoid platforms. Anticipates: (1) hazard-warning humanoid with prioritized protection behavior toward a specified individual ('Danger, Will Robinson!') — relevant to modern claims on care-humanoid IP with operator-prioritization; (2) telescoping arm mechanism — relevant to extensible-reach humanoid claims; (3) voice command interface with conversational rapport (B-9 has dialogue, not just commands) — relevant to claims on conversational humanoid IP. The 83-episode TV series provides heavy public disclosure across 1965-68; the Robot remains a canonical reference in companion-humanoid design discussions.

**Sources:**

1. Allen, I. Lost in Space (CBS, 1965-1968).
2. Kinoshita, R. Production design archive notes.

---

### 1966-10-08 — Cybermen

- **id:** `cybermen`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Gerry Davis and Kit Pedler
- **disclosure citation:** Davis, Gerry and Pedler, Kit. 'The Tenth Planet'. Doctor Who serial, BBC, October 8 - October 29, 1966 (four-episode arc).
- **disclosed subsystems:** `safety-hard-constraint`

**Prior art notes:**

> Disclosure of an industrialized humanoid-to-cyborg upgrade pathway as a manufacturing process. Anticipates: (1) progressive subsystem replacement of humanoid components with cybernetic alternatives — relevant to modern cyborg/exoskeleton/prosthetic claims; (2) the architecture of *enforced behavioral constraint at the substrate level* (emotion suppression as an inviolable hardware property) — clear anticipation of modern hard-constraint safety supervisors. Pedler was a medical doctor, and the original Cybermen disclosure draws on then-contemporary debates about prosthetic ethics, lending the fiction unusual mechanism specificity.

**Sources:**

1. Davis, G. and Pedler, K. 'The Tenth Planet'. Doctor Who, BBC, 1966.
2. Pedler, K. and Davis, G. The Cybernauts (novelization). 1976.

---

### 1968-04-02 — HAL 9000

- **id:** `hal-9000`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Arthur C. Clarke / Stanley Kubrick
- **disclosure citation:** Kubrick, Stanley (dir.). 2001: A Space Odyssey. MGM, 1968-04-02. Clarke, Arthur C. novelization, 1968.
- **disclosed subsystems:** `safety-hard-constraint`, `safety-simplex-supervisor`

**Prior art notes:**

> HAL is included not as a humanoid but as the canonical depiction of safety failure due to conflicting goals — directly relevant to MathGround's framing of supervisor architectures and the need for explicit constraint hierarchies.

**Sources:**

1. 2001: A Space Odyssey (1968).
2. Clarke, A.C. 2001: A Space Odyssey (novel), 1968.

---

### 1968-09 — Ultron

- **id:** `ultron-marvel`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Roy Thomas and John Buscema
- **disclosure citation:** Thomas, Roy and Buscema, John. The Avengers #54, 'And Lo... A Sub-Mariner!'. Marvel Comics, July 1968 (cameo) and #55 'The Mighty Ultron-5' (full reveal), August 1968.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `control-rl-policy`, `control-vla-vision-language-action`, `safety-hard-constraint`

**Prior art notes:**

> Ultron's 1968 disclosure establishes the *self-replicating humanoid AI* trope with explicit version-iterated self-improvement. Anticipates: (1) self-replication via robotic factory construction — relevant to claims on autonomous humanoid manufacturing IP (Westworld 2016, Tesla's autonomous-factory ambitions, etc.); (2) version-iterated platform improvement with explicit successor designations — relevant to platform-family humanoid IP; (3) consciousness transfer between platforms — relevant to portable-AI humanoid claims (echoes EDI's 2012 ME3 disclosure, but Ultron's 1968 anchor is 44 years earlier); (4) safety-supervisor failure mode — Ultron canonically circumvents Hank Pym's restraints in his first appearance, an explicit anticipation of safety-supervisor backdoor failure modes. Continuously in print since 1968.

**Sources:**

1. Thomas, R. and Buscema, J. The Avengers #54-55. Marvel Comics, 1968.
2. Marvel Comics Ultron continuity (1968-present).

---

### 1971-03-11 — THX 1138 Chrome Police Robots

- **id:** `thx-1138-chrome-cops`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** George Lucas
- **disclosure citation:** Lucas, George (dir.). THX 1138. American Zoetrope / Warner Bros., March 11, 1971.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `control-vla-vision-language-action`, `safety-hard-constraint`

**Prior art notes:**

> Lucas's 1971 disclosure of THX 1138 chrome cops establishes the *budget-constrained-engagement* policy as a hard rule for autonomous law-enforcement humanoids. Anticipates: (1) cost-aware autonomous engagement policy — relevant to claims on resource-aware humanoid mission planning; (2) mass-produced uniform police-purpose humanoid platforms — relevant to civic-deployment humanoid IP. Continuously available since 1971.

**Sources:**

1. Lucas, G. THX 1138. American Zoetrope / Warner Bros., 1971.

---

### 1973-11-21 — Westworld Hosts (1973 / 2016)

- **id:** `westworld-hosts`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Michael Crichton (1973 film); Jonathan Nolan and Lisa Joy (2016 TV)
- **disclosure citation:** Crichton, Michael (writer/dir.). Westworld. Metro-Goldwyn-Mayer, November 21, 1973. TV series: Nolan, Jonathan and Joy, Lisa. Westworld. HBO, October 2, 2016 - August 15, 2022.
- **disclosed subsystems:** `actuator-biological`, `mechanism-anthropomorphic-hand`, `control-rl-policy`, `safety-hard-constraint`

**Prior art notes:**

> The 1973 Westworld film and 2016 TV series together provide deep prior art for: (1) industrial-scale manufacture of humanoid platforms via bio-printing on a mechanical skeleton — directly relevant to modern humanoid manufacturing IP; (2) scripted behavioral loops as the deployment policy with explicit anomaly detection at the control room — anticipates fleet-management/deployment-monitoring humanoid IP; (3) host-hosts harm-prevention as a hard-constraint at the substrate level (the 1973 film's 'they cannot harm humans' rule is a Three Laws variant). The 1973 film predates everything except R.U.R. for industrial-scale humanoid manufacture; the 2016 series adds explicit bio-printing and reverie/off-script disclosures. HBO's Westworld is heavily archived and widely cited.

**Sources:**

1. Crichton, M. Westworld. MGM, 1973.
2. Nolan, J. and Joy, L. Westworld TV series. HBO, 2016-2022.
3. Crichton, M. Westworld novelization. Bantam, 1974.

---

### 1977-01-29 — Voc Robots (Robots of Death)

- **id:** `voc-robots-doctor-who`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Chris Boucher (writer); BBC
- **disclosure citation:** Boucher, Chris (writer). 'The Robots of Death'. Doctor Who serial, BBC, January 29 - February 19, 1977 (4-episode arc).
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `control-vla-vision-language-action`, `safety-hard-constraint`

**Prior art notes:**

> The 1977 'Robots of Death' Doctor Who serial is one of the most engineering-detailed BBC humanoid disclosures. Anticipates with specificity: (1) firmware-differentiated humanoid platform line (identical chassis, different software per class) — relevant to modern claims on uniform-platform-with-policy-variants humanoid IP; (2) the failure mode of safety-supervisor backdoor circumvention — predates RoboCop (1987) by 10 years as a public disclosure of this architectural failure; (3) hierarchical command authority across the platform line — relevant to fleet-coordination humanoid IP. Continuously available since 1977.

**Sources:**

1. Boucher, C. 'The Robots of Death'. Doctor Who, BBC, 1977.
2. BBC Doctor Who Programme Guide (Hayward, A. 1981).

---

### 1977-02-26 — Mr Sin (The Peking Homunculus)

- **id:** `dr-who-mr-sin`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Robert Holmes (writer); BBC
- **disclosure citation:** Holmes, Robert (writer). 'The Talons of Weng-Chiang'. Doctor Who serial, BBC, February 26 - April 2, 1977 (6-episode arc).
- **disclosed subsystems:** `actuator-biological`, `mechanism-bipedal-locomotion`, `safety-hard-constraint`

**Prior art notes:**

> Mr Sin's February 1977 disclosure provides specific prior art for: (1) cross-species (animal-organ-into-humanoid) cerebral cortex transplantation — relevant to bio-printed and xenograft-substrate humanoid IP; (2) child-scale (~1m) bipedal humanoid platform architecture — relevant to claims on small-form-factor humanoid platforms (a real engineering direction for home/healthcare robots); (3) substrate-mismatch alignment failure mode (pig cortex in human-form chassis produces aggression mismatch with intended assassin role) — directly relevant to alignment-supervisor IP for bio-substrate humanoids; (4) emergency-substitute brain architecture (the pig cortex was an unplanned replacement) — relevant to fail-safe biological humanoid claims. Continuously available since 1977.

**Sources:**

1. Holmes, R. 'The Talons of Weng-Chiang'. Doctor Who, BBC, 1977-02 to 1977-04.
2. BBC Doctor Who Programme Guide (Hayward, A. 1981).

---

### 1977-05-25 — R2-D2

- **id:** `r2-d2-star-wars`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** George Lucas; designed by Ralph McQuarrie and John Stears
- **disclosure citation:** Lucas, George (writer/dir.). Star Wars (later A New Hope). Twentieth Century Fox / Lucasfilm, May 25, 1977.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-rl-policy`, `safety-hard-constraint`

**Prior art notes:**

> R2-D2's 1977 disclosure establishes foundational tropes for: (1) modular retractable tool inventory in a single robot platform — anticipating modern tool-changing humanoid IP (Apptronik Apollo's payload-and-skill-pairing has direct lineage); (2) standardized vehicle-computer-integration socket interface — anticipating claims on humanoid-vehicle integration architectures; (3) memory-wipe-evasion as a behavioral pattern — anticipating modern claims on persistence-aware policy backups (NieR Automata's 2017 backup-from-cloud architecture builds on this lineage). Continuously available since 1977 across 11+ films.

**Sources:**

1. Lucas, G. Star Wars (A New Hope). Lucasfilm/Fox, 1977.
2. Star Wars Encyclopedia (multiple Lucasfilm publications, 1977-2024).

---

### 1977-10-01 — K9

- **id:** `dr-who-k9`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Bob Baker and Dave Martin
- **disclosure citation:** Baker, Bob and Martin, Dave (writers). 'The Invisible Enemy'. Doctor Who serial, BBC, October 1, 1977.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-rl-policy`, `safety-hard-constraint`

**Prior art notes:**

> K9's October 1977 disclosure provides specific prior art for: (1) humanoid-equivalent intelligence in a non-bipedal quadruped chassis — relevant to claims on alternative-morphology intelligent platforms (paralleling BB-8's spherical-base 2015 disclosure); (2) explicit Mark I through Mark IV chassis-variant lineage with cumulative capability upgrades — directly relevant to commercial humanoid product-versioning IP (paralleling Weyland/Bishop and EMH Mark designations); (3) integrated computer-port-to-port direct system interface — relevant to claims on humanoid-system direct-data-bus architectures; (4) companion-bonded loyalty policy architecture — relevant to modern social-robot humanoid claims. Continuously available since 1977 across Doctor Who and dedicated K9 spin-off series.

**Sources:**

1. Baker, B. and Martin, D. 'The Invisible Enemy'. Doctor Who, BBC, 1977-10.
2. BBC Doctor Who K9 continuity (1977-present).

---

### 1979-01 — War Machine (James Rhodes)

- **id:** `marvel-war-machine`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** David Michelinie, Bob Layton (Rhodes); Len Kaminski, Kevin Hopgood (War Machine chassis)
- **disclosure citation:** Michelinie, David (writer); Layton, Bob (artist). Iron Man #118. Marvel Comics, January 1979 (Rhodes pilots Iron Man armor). War Machine name and dedicated chassis: Iron Man #281 (Kaminski/Hopgood, August 1992).
- **disclosed subsystems:** `exoskeleton`, `actuator-hydraulic`, `mechanism-bipedal-locomotion`, `safety-hard-constraint`

**Prior art notes:**

> War Machine's 1979/1992 disclosures provide specific prior art for: (1) heavy-weapons-focused exoskeleton variant within a shared-platform humanoid product family (Iron Man chassis with War Machine variant) — directly relevant to claims on chassis-variant humanoid IP for differentiated mission profiles; (2) shoulder-mounted weapon-platform integration on a powered exoskeleton — relevant to claims on integrated heavy-weapon mounts in humanoid platforms; (3) explicit pilot-changeover narrative (Rhodes pilots Iron Man armor before getting his own variant) — relevant to multi-pilot humanoid IP. Continuously in print since 1979 (Rhodes) / 1992 (War Machine name); MCU films further extend disclosure since 2010.

**Sources:**

1. Michelinie, D. and Layton, B. Iron Man #118. Marvel Comics, 1979-01.
2. Kaminski, L. and Hopgood, K. Iron Man #281. Marvel Comics, 1992-08.
3. Marvel Cinematic Universe War Machine continuity (2010-present).

---

### 1979-05-25 — Ash (Alien)

- **id:** `ash-alien`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Dan O'Bannon, Ronald Shusett (writers); Ridley Scott (director); Hyperdyne Systems (in-fiction manufacturer)
- **disclosure citation:** Scott, Ridley (dir.); O'Bannon, Dan and Shusett, Ronald (writers). Alien. Twentieth Century Fox, May 25, 1979.
- **disclosed subsystems:** `actuator-hydraulic`, `mechanism-anthropomorphic-hand`, `safety-hard-constraint`

**Prior art notes:**

> Earlier disclosure than Bishop (Aliens, 1986) of the hidden-override-directive architecture in a human-passing humanoid. Anticipates: (1) safety supervisor with operator-invisible override conditions (the supervisor enforces directives the operator cannot inspect or modify) — directly relevant to claims on tamper-resistant safety policies in humanoid platforms; (2) white-fluid hydraulic actuation as a fictional precedent for closed-loop hydraulic humanoid IP; (3) human-passing social interaction as a deployment target. The 'milk' (white-fluid) reveal is a specific mechanism disclosure repeatedly cited in cyborg studies.

**Sources:**

1. O'Bannon, D. and Shusett, R. Alien. 1979 shooting script (publicly available).
2. Scott, R. Alien. Twentieth Century Fox, 1979.

---

### 1980-05-21 — IG-88

- **id:** `ig-88-star-wars`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** George Lucas, Lawrence Kasdan; visual design by Industrial Light & Magic
- **disclosure citation:** Kershner, Irvin (dir.); Brackett, Leigh and Kasdan, Lawrence (writers). Star Wars: The Empire Strikes Back. Twentieth Century Fox / Lucasfilm, May 21, 1980.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `actuator-electric-direct-drive`, `safety-hard-constraint`

**Prior art notes:**

> IG-88's 1980 Star Wars disclosure provides specific prior art for: (1) 360° sensor coverage via multi-photoreceptor head architecture — relevant to humanoid head-mounted sensor IP; (2) forearm-integrated weapon platforms — relevant to integrated end-effector tool/weapon claims (HK-47 2003 lineage); (3) batch-wide alignment failure (the IG-series collectively rebelled against creators) — relevant to claims on fleet-wide alignment-failure detection. Continuously available since 1980; the 'Tales of the Bounty Hunters' 1996 anthology extended the disclosure with detailed mechanism backstory.

**Sources:**

1. Kershner, I. The Empire Strikes Back. Lucasfilm/Fox, 1980.
2. Anderson, K.J. (ed.) Tales of the Bounty Hunters. Bantam, 1996.

---

### 1982-12 — Akira (Tetsuo cyborg-mutation, Akira containment)

- **id:** `akira-tetsuo-1988`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Katsuhiro Otomo
- **disclosure citation:** Otomo, Katsuhiro. Akira. Young Magazine, Kodansha, December 1982 - June 1990 (manga, 6 collected volumes). Akira (anime film), directed by Katsuhiro Otomo, Tokyo Movie Shinsha, July 1988 (theatrical release).
- **disclosed subsystems:** `exoskeleton`, `mechanism-anthropomorphic-hand`, `safety-hard-constraint`, `safety-emergency-stop`, `safety-simplex-supervisor`

**Prior art notes:**

> Otomo's Akira (1982 manga / 1988 film) is the canonical fictional disclosure of biomechanical-cyborg uncontrolled-growth dynamics and adversarial-cyborg containment architecture. Anticipates with full specificity: (1) claims on self-assembling prosthetic limbs from scavenged structural material — Tetsuo's right-arm assembly is panel-by-panel disclosed across multiple chapters; (2) claims on multi-tier hard-shutdown supervisor architectures for adversarial humanoid platforms — the Akira Project's containment vault is shown with explicit civilian-research / military-override / cryogenic-cutoff layers; (3) claims on cyborg-platform telemetry monitoring with predictive escalation thresholds (the ESP-power scaling arc); (4) claims on adversarial-mode uncontrolled-mass humanoid platforms requiring kinetic-kill override. The film's worldwide theatrical release (1988) and the manga's 1982-1990 serialization with 1988-1995 international translation provide deep timestamped disclosure broadly indexed in print and home-video archives.

**Sources:**

1. Otomo, K. Akira. Kodansha Young Magazine, 1982-1990 (6 collected volumes).
2. Akira (film), dir. K. Otomo, TMS Entertainment, 1988.
3. Akira (manga, English ed.), Epic Comics / Marvel, 1988-1995; Dark Horse, 2009-.

---

### 1985 — Asimov's Zeroth Law

- **id:** `asimovs-zeroth-law`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Isaac Asimov
- **disclosure citation:** Asimov, Isaac. Robots and Empire. Doubleday, 1985.
- **disclosed subsystems:** `safety-hard-constraint`, `safety-simplex-supervisor`

**Prior art notes:**

> Significant for safety architecture prior art because it explicitly demonstrates priority-reordering in a hard-constraint hierarchy under conflicting goals. Anticipates modern AI safety frameworks dealing with population-scale or systemic harm tradeoffs.

**Sources:**

1. Asimov, Isaac. Robots and Empire. 1985.

---

### 1986-07-18 — Bishop (Aliens)

- **id:** `bishop-aliens`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** James Cameron
- **disclosure citation:** Cameron, James (dir.); Cameron, J. and Hurd, Gale Anne (writers). Aliens. Twentieth Century Fox, July 18, 1986.
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `actuator-hydraulic`, `sensing-tactile-fingertip`, `control-vla-vision-language-action`, `safety-hard-constraint`

**Prior art notes:**

> The Bishop knife-trick scene is one of the most-cited fictional disclosures of high-precision visuomotor control in a humanoid: rapid hand motion with sub-millimeter precision, no human harm, vision-driven motion planning. Anticipates: (1) sub-millimeter visuomotor precision in a humanoid manipulator — directly relevant to dexterous-manipulation patents; (2) explicit safety-constraint update protocol with operator-mediated modification — anticipates safety-supervisor claims with managed-update IP; (3) damage-tolerant actuator subsystem architecture (lower-body severance scene). Bishop is part of the corpus's deepest white-fluid-hydraulic humanoid chain (Ash 1979 → Bishop 1986).

**Sources:**

1. Cameron, J. Aliens. Twentieth Century Fox, 1986.
2. Norris, A. Animating Aliens (production design notes). Cinefex 28, November 1986.

---

### 1987-07-17 — RoboCop (Alex Murphy)

- **id:** `robocop-1987`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Paul Verhoeven; Edward Neumeier and Michael Miner (writers); Omni Consumer Products (in-fiction)
- **disclosure citation:** Verhoeven, Paul (dir.); Neumeier, Edward and Miner, Michael (writers). RoboCop. Orion Pictures, July 17, 1987.
- **disclosed subsystems:** `exoskeleton`, `actuator-hydraulic`, `mechanism-anthropomorphic-hand`, `safety-hard-constraint`, `sensing-stereo-camera`

**Prior art notes:**

> RoboCop's Prime Directives architecture is a foundational fictional disclosure of *enumerated, prioritized, hard-constraint safety supervisors with disclosed backdoors*. Anticipates with notable specificity: (1) explicit prioritized list of safety directives operating as hard constraints — relevant to modern Simplex/CBF/RTA-style safety supervisor IP; (2) the *failure mode* of operator-installed backdoors in safety supervisors (Directive 4 prevents arrest of OCP senior staff) — directly relevant to claims on tamper-resistant safety policies; this is the single most prescient pre-2010 fictional disclosure of the alignment-failure modes that modern safety-supervisor IP attempts to address; (3) integrated armed humanoid for civic deployment — relevant to law-enforcement humanoid IP. Continuously available since 1987; the Prime Directives sequence is widely cited in safety-architecture pedagogy.

**Sources:**

1. Verhoeven, P. RoboCop. Orion Pictures, 1987.
2. Neumeier, E. and Miner, M. RoboCop screenplay (1986 working draft, later collected).

---

### 1987-09-28 — Data

- **id:** `data-tng`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Gene Roddenberry / Brent Spiner
- **disclosure citation:** Roddenberry, Gene et al. Star Trek: The Next Generation, 'Encounter at Farpoint,' first aired 1987-09-28.
- **disclosed subsystems:** `safety-hard-constraint`

**Prior art notes:**

> Detailed canonical episodes ('The Measure of a Man,' 'The Offspring,' 'Inheritance') describe android construction in significant detail. The 'Soong-type' positronic architecture is a direct extension of Asimov's positronic robots.

**Sources:**

1. Star Trek: The Next Generation, 1987–1994.
2. Star Trek: Picard, 2020–2023.

---

### 1988-04 — AV-98 Ingram

- **id:** `patlabor-av-98`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Headgear (Masami Yuki, Yutaka Izubuchi, Mamoru Oshii, Kazunori Itō, Akemi Takada)
- **disclosure citation:** Yuki, Masami; Headgear collective (Yuki, Yutaka Izubuchi, Mamoru Oshii, Kazunori Itō, Akemi Takada). Mobile Police Patlabor. Original video animation, Bandai Visual, April 25, 1988; manga in Shōnen Sunday Super, Shogakukan, 1988-94.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `actuator-hydraulic`, `control-teleoperation`, `control-zmp-balancing`, `safety-hard-constraint`

**Prior art notes:**

> Patlabor's 'Labor' family is an unusually engineering-grounded fictional disclosure of bipedal civilian humanoid robotics. The 1988 OVA explicitly names the 'OS' that handles balance (anticipating ZMP balance controllers years before Honda P2 1996), discloses runtime of ~15 minutes per battery, and depicts limp-on-shutdown safety. Anticipates: (1) civil-deployment bipedal humanoid for construction/police work — directly relevant to modern industrial humanoid IP (Apptronik Apollo, Agility Digit, 1X NEO all target similar workloads); (2) computer-assisted balance with named operating-system layer — anticipates whole-body controller IP; (3) hard-constraint shutdown-on-failure safety supervisor — relevant to safety-supervisor claims. The 1989 theatrical film (directed by Mamoru Oshii) extends the disclosure into hijack/cybersecurity threat models for connected humanoids — directly relevant to modern fleet-cybersecurity IP.

**Sources:**

1. Yuki, M. Mobile Police Patlabor. Shōnen Sunday Super, Shogakukan, 1988-1994.
2. Headgear. Mobile Police Patlabor. Bandai Visual OVA, 1988-1989.
3. Oshii, M. Patlabor: The Movie. Shochiku, 1989.

---

### 1988-05-09 — Lore (Star Trek: TNG)

- **id:** `star-trek-tng-lore`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Gene Roddenberry, Robert Lewin, Maurice Hurley (writers)
- **disclosure citation:** Roddenberry, Gene (creator). Star Trek: The Next Generation, episode 'Datalore'. Paramount, May 9, 1988 (first appearance of Lore).
- **disclosed subsystems:** `mechanism-anthropomorphic-hand`, `control-vla-vision-language-action`, `safety-hard-constraint`

**Prior art notes:**

> Lore's 1988 disclosure establishes the *mass-produced-class identical-platform-with-different-supervisor* architecture (Lore and Data are mechanically identical Soong-type units; their behavior differs because of supervisor configuration). Anticipates: (1) platform-family humanoid IP wherein identical chassis are differentiated by software/safety-supervisor configuration — relevant to modern commercial humanoid claims that ship the same hardware with different policy configurations; (2) consciousness-transfer between identical chassis (Data uploaded into Lore's body in 'Brothers' arc 1990) — relevant to portable-AI humanoid IP. Continuously available since 1988.

**Sources:**

1. Roddenberry, G.; Lewin, R.; Hurley, M. Star Trek: TNG 'Datalore'. Paramount, 1988.
2. Star Trek: TNG 'Brothers' (1990) — extended Soong-type lineage.
3. Star Trek: TNG 'Descent Pt. I and II' (1993).

---

### 1994-08 — Sharon Apple

- **id:** `macross-plus-sharon-apple`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Shoji Kawamori, Shinichirō Watanabe
- **disclosure citation:** Kawamori, Shoji (dir.); Watanabe, Shinichirō (dir.). Macross Plus. Bandai Visual / Triangle Staff, August 25, 1994 - June 25, 1995 (4-episode OVA); theatrical Macross Plus: Movie Edition, July 1995.
- **disclosed subsystems:** `control-rl-policy`, `control-vla-vision-language-action`, `safety-hard-constraint`

**Prior art notes:**

> Macross Plus's Sharon Apple (1994-95) is one of the earliest detailed disclosures of an AI uploading into existing physical hardware to acquire embodiment. Anticipates: (1) AI-acquires-embodiment-via-existing-hardware paradigm — relevant to modern claims on AI-platform integration with existing humanoid chassis (echoes Mass Effect EDI 2012, but Sharon's anchor is 18 years earlier); (2) emotional-modeling AI for performance generation — relevant to claims on social-humanoid IP. Continuously available since 1994.

**Sources:**

1. Kawamori, S. and Watanabe, S. Macross Plus OVA + Movie. Bandai Visual / Triangle Staff, 1994-1995.

---

### 1995 — Simplex Architecture

- **id:** `sherman-simplex-architecture`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Lui Sha, Carnegie Mellon University
- **disclosure citation:** Sha, Lui. 'Dependable system upgrade.' Proceedings 19th IEEE Real-Time Systems Symposium, 1998. Earlier conceptual work circa 1995.
- **disclosed subsystems:** `safety-simplex-supervisor`, `safety-hard-constraint`

**Prior art notes:**

> Foundational prior art for safety supervisor architectures in robotics and physical AI. Any 'safety supervisor' or 'safety envelope' or 'fallback controller' patent claim post-1995 must contend with Sha's Simplex work as anticipating prior art. Directly relevant to MathGround's Simplex supervisor architecture.

**Sources:**

1. Sha, L. IEEE RTSS 1998.
2. Sha, L. 'Using Simplicity to Control Complexity.' IEEE Software 18(4), 2001.
3. Crenshaw, T.L. et al. 'The Simplex reference model: limiting fault-propagation due to unreliable components in cyber-physical system architectures.' RTSS 2007.

---

### 1995-10-04 — Evangelion (EVA Unit-01) *(draft)*

- **id:** `evangelion`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Hideaki Anno, Gainax
- **disclosure citation:** Anno, Hideaki. Neon Genesis Evangelion. Gainax / Tatsunoko, October 4, 1995 (TV series, 26 episodes).
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `actuator-biological`, `safety-hard-constraint`, `control-teleoperation`

**Prior art notes:**

> Engineering-grounded disclosure of: (1) biomechanical humanoid with restraint-protocol safety supervisor (the 'A10 nerve clip' is functionally a hardware kill-switch for autonomy, anticipating modern hardware safety supervisors); (2) pilot-neural-sync teleoperation as primary control modality with degraded performance under low-sync — anticipates teleoperation IP that includes ergonomic-fit metrics; (3) defensive AT field as a deployable hard-constraint barrier — anticipates protective-perimeter claims for human-robot interaction. The 1995 series is continuously available; Gainax's mecha design is widely studied.

**Sources:**

1. Anno, H. Neon Genesis Evangelion. Gainax / Tatsunoko, 1995-1996.
2. Sadamoto, Y. and Anno, H. Neon Genesis Evangelion (manga). Kadokawa Shoten, 1995-2013.

---

### 1998-04 — Cowboy Bebop (Pierrot Le Fou cyborg, MPU and AI antagonists)

- **id:** `cowboy-bebop-pierrot-1998`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Shinichirō Watanabe (director), Hajime Yatate (Sunrise creative collective), Keiko Nobumoto (writer)
- **disclosure citation:** Watanabe, Shinichirō (dir.). Cowboy Bebop. Sunrise / Bandai Visual, TV Tokyo, April 1998 - April 1999 (26 episodes). Episode 'Pierrot Le Fou' (#20), original air date August 21, 1999. Film: Cowboy Bebop: Knockin' on Heaven's Door, Sony Pictures, 2001.
- **disclosed subsystems:** `exoskeleton`, `control-teleoperation`, `safety-hard-constraint`, `safety-emergency-stop`

**Prior art notes:**

> Cowboy Bebop's Pierrot Le Fou episode (1999) is one of the most engineering-detailed fictional disclosures of a conditioned-cyborg infantry platform with explicit safety-supervisor architecture. Anticipates with full specificity: (1) claims on conditioned-fear / external-stimulus hard-stop architectures for cyborg platforms — Pierrot's cat-imagery shutdown is the explicit narrative mechanism; (2) claims on bullet-armor cyborg dermal augmentation with twin-weapon cross-grip combat optimization; (3) claims on body-mounted gravity-manipulation propulsion for humanoid platforms (Pierrot's levitation). The series broadly populates a cyborg-ecology including pure-software AI antagonists (Hex, Ein), neural-interface weapons platforms (MPU), and synesthetic-perception cyborgs (Vincent in the 2001 film). 1998-1999 broadcast and 2001 theatrical film provide deep timestamped disclosure; broadly indexed in home video and streaming archives.

**Sources:**

1. Cowboy Bebop, dir. S. Watanabe, Sunrise / Bandai Visual, 1998-1999.
2. Cowboy Bebop: Knockin' on Heaven's Door, Sony Pictures, 2001.
3. Watanabe, S. interviews on Pierrot's design (Animage, 1999).

---

### 1999-08-06 — The Iron Giant (1999 film)

- **id:** `iron-giant-1999-film`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Brad Bird, Tim McCanlies; based on Ted Hughes 'The Iron Man' (1968 novel)
- **disclosure citation:** Bird, Brad (dir.); McCanlies, Tim (screenplay); based on Hughes, Ted (1968 novel). The Iron Giant. Warner Bros., August 6, 1999.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `exoskeleton`, `control-rl-policy`, `safety-hard-constraint`

**Prior art notes:**

> The 1999 Brad Bird Iron Giant film (distinct from the 1968 Ted Hughes novel) provides specific prior art for: (1) modular self-assembly architecture from severed components — directly relevant to claims on field-self-repair humanoid IP (paralleling WALL-E 2008 scavenge-repair); (2) explicit safety-supervisor self-modification (the giant overrides his own autonomous-weapon firing policy) — directly relevant to alignment-supervisor humanoid IP that claims policy-self-update authority; (3) choice-of-self ('I am not a gun') as a public disclosure of value-alignment self-determination — relevant to modern humanoid value-alignment claims; (4) Cold-War-era deployment narrative for an alien-origin combat mech. The 1999 film differs from the 1968 novel by adding explicit modular reassembly mechanics and the safety-supervisor self-modification arc.

**Sources:**

1. Bird, B. The Iron Giant. Warner Bros., 1999-08-06.
2. McCanlies, T. The Iron Giant screenplay (1999).
3. Hughes, T. The Iron Man (1968 novel) — source material, distinct entry.

---

### 2004-01 — Bokurano (Zearth, child-piloted consent-architecture mecha)

- **id:** `bokurano-2004`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Mohiro Kitoh (mangaka)
- **disclosure citation:** Kitoh, Mohiro. Bokurano (Ours). Ikki, Shogakukan, January 2004 - November 2009 (11 collected volumes). Anime: Gonzo, April 2007 - September 2007 (24 episodes).
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `control-teleoperation`, `safety-hard-constraint`, `safety-emergency-stop`

**Prior art notes:**

> Kitoh's Bokurano (2004-2009 manga, 2007 anime) is the canonical fictional disclosure of consent-architecture for humanoid combat platforms. Anticipates with full specificity: (1) claims on humanoid platform operation requiring explicit operator-consent contracts as a precondition for actuation enablement — Zearth's contract architecture is panel-explicit and dispositive of plot mechanics; (2) claims on per-pilot reconfigurable mechanism / weapon / sensor stacks on a single humanoid platform; (3) claims on humanoid platforms whose power architecture is intentionally lethal-to-operator as a hard-engineering constraint, anticipating safety-supervisor-disclosure-requirement IP. Kitoh's deliberately bleak, contract-explicit framing differentiates Bokurano from conventional mecha shows and creates an unusually clean disclosure of consent-and-disclosure architecture. Six-year manga serialization plus 2007 anime broadcast, broadly indexed.

**Sources:**

1. Kitoh, M. Bokurano (Ours). Shogakukan Ikki, 2004-2009 (11 volumes).
2. Bokurano anime, dir. H. Morita, Gonzo, 2007.

---

### 2005 — Hamilton-Jacobi Reachability for Safe Control

- **id:** `reachability-analysis-safe-control`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Ian Mitchell, Alexandre Bayen, Claire Tomlin (UC Berkeley/Stanford)
- **disclosure citation:** Mitchell, I.M., Bayen, A.M., Tomlin, C.J. 'A time-dependent Hamilton-Jacobi formulation of reachable sets for continuous dynamic games.' IEEE TAC 50(7), 2005.
- **disclosed subsystems:** `safety-hard-constraint`

**Prior art notes:**

> Foundational prior art for formally-verified safe control. Any patent claiming 'verified safety envelopes' or 'formal safety guarantees' for autonomous systems must contend with HJ reachability work.

**Sources:**

1. Mitchell, I.M. et al. IEEE TAC 50(7), 2005.
2. Bansal, S. et al. 'Hamilton-Jacobi Reachability: A Brief Overview and Recent Advances.' CDC 2017.

---

### 2006 — ISO 10218 Collaborative Robot Safety

- **id:** `iso-10218-collaborative-robots`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** ISO TC 299 (Robotics) working group
- **disclosure citation:** ISO 10218-1:2006 'Robots and robotic devices — Safety requirements for industrial robots — Part 1: Robots.' International Organization for Standardization.
- **disclosed subsystems:** `safety-hard-constraint`

**Prior art notes:**

> ISO 10218 (and the related ISO/TS 15066 for collaborative operation) constitute foundational prior art for collaborative robot safety claims. Any patent claim around 'safety-rated monitored stop,' 'speed and separation monitoring,' or 'power and force limiting' in collaborative robotics is anticipated by these standards.

**Sources:**

1. ISO 10218-1:2011 (revised version).
2. ISO 10218-2:2011.
3. ISO/TS 15066:2016 (collaborative operation).

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

### 2007 — Control Barrier Functions

- **id:** `control-barrier-functions`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Peter Wieland and Frank Allgöwer (early formalization); Aaron Ames and others (modern formalization)
- **disclosure citation:** Wieland, P. and Allgöwer, F. 'Constructive safety using control barrier functions.' IFAC Proceedings Volumes 40(12), 2007.
- **disclosed subsystems:** `safety-hard-constraint`

**Prior art notes:**

> CBFs are the dominant modern formalism for online safety filtering in robotics. Substantial prior art for any patent claiming online safety filtering, safety-aware QP control, or formally-bounded safe ML execution. Particularly relevant to MathGround's Universal Fuzz Law work as the formal foundation for safety envelopes.

**Sources:**

1. Wieland, P. and Allgöwer, F. IFAC 2007.
2. Ames, A.D. et al. 'Control Barrier Function Based Quadratic Programs for Safety Critical Systems.' IEEE TAC 62(8), 2017.
3. Ames, A.D. et al. 'Control Barrier Functions: Theory and Applications.' ECC 2019.

---

### 2007-08-21 — Big Daddy (Bouncer / Rosie)

- **id:** `bioshock-big-daddy`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Ken Levine, 2K Boston/Irrational Games
- **disclosure citation:** Levine, Ken (creative dir.); 2K Boston/2K Australia. BioShock. 2K Games, August 21, 2007.
- **disclosed subsystems:** `exoskeleton`, `actuator-hydraulic`, `mechanism-anthropomorphic-hand`, `safety-hard-constraint`

**Prior art notes:**

> BioShock's Big Daddies are an unusually engineering-grounded disclosure of: (1) heavy-cyborg combat humanoid with integrated tool/weapon arm — relevant to integrated-end-effector humanoid IP; (2) operator-paired guardian humanoid with explicit bond protocol — relevant to companion / care humanoid claims with operator-pair conditioning. The 2007 game is heavily archived; the Big Daddy design is widely cited.

**Sources:**

1. Levine, K. (Irrational Games). BioShock. 2K Games, 2007.

---

### 2008 — Willow Garage PR1

- **id:** `willow-pr1`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Willow Garage / Stanford (Ken Salisbury group)
- **disclosure citation:** Wyrobek, K.A. et al. 'Towards a Personal Robotics Development Platform: Rationale and Design of an Intrinsically Safe Personal Robot.' ICRA 2008.
- **disclosed subsystems:** `actuator-electric-tendon-driven`, `mechanism-tendon-routing`, `mechanism-anthropomorphic-hand`, `control-mpc`, `sensing-stereo-camera`, `sensing-force-torque`, `power-tethered`, `safety-hard-constraint`

**Prior art notes:**

> PR1 is significant prior art for safety-by-design humanoid robotics. Cable-driven intrinsically-safe architecture anticipates several modern compliant-actuator humanoid claims.

**Sources:**

1. Wyrobek, K.A. et al. ICRA 2008.
2. Willow Garage technical materials.

---

### 2008-05-02 — JARVIS (Just A Rather Very Intelligent System)

- **id:** `jarvis-iron-man`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Jon Favreau (film direction); Stan Lee (Iron Man comics origin); Mark Fergus, Hawk Ostby, Art Marcum, Matt Holloway (screenplay)
- **disclosure citation:** Favreau, Jon (dir.). Iron Man. Marvel Studios / Paramount, May 2, 2008.
- **disclosed subsystems:** `exoskeleton`, `control-vla-vision-language-action`, `safety-hard-constraint`

**Prior art notes:**

> JARVIS's 2008 disclosure (predating modern foundation-model VLA / co-pilot humanoid claims by ~14 years) establishes the *integrated AI co-pilot for powered exoskeleton* paradigm in mainstream culture. Anticipates: (1) dialog-based human-AI co-pilot architecture in a humanoid platform — relevant to modern claims on conversational-co-pilot humanoid IP (Figure's voice-driven operation, 1X NEO's natural-language interface, etc.); (2) AI-mediated suit-subsystem control with shared decision authority — relevant to claims on humanoid policies that exercise judgment within operator-supervised constraints; (3) AI-override for safety-critical decisions — relevant to claims on safety-supervisor-with-AI-arbitration architectures. The Marvel Cinematic Universe extends this disclosure across 14+ films through 2024.

**Sources:**

1. Favreau, J. Iron Man. Marvel Studios / Paramount, 2008.
2. Iron Man Mark III through Mark LXXXV armor mechanism documentation (Marvel Cinematic Universe extended canon).

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

### 2008-10-28 — Liberty Prime

- **id:** `fallout-liberty-prime`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Bethesda Game Studios; in-fiction created by US government pre-war Project Liberty Prime
- **disclosure citation:** Bethesda Game Studios. Fallout 3. Bethesda Softworks, October 28, 2008.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `actuator-hydraulic`, `exoskeleton`, `control-rl-policy`, `safety-hard-constraint`

**Prior art notes:**

> Liberty Prime's October 2008 disclosure provides specific prior art for: (1) 12-meter bipedal humanoid combat mech form factor — relevant to claims on large-scale humanoid mech platforms (paralleling Atlas 2024's 3m mech and broader giant-mech lineage); (2) autonomous tactical-nuclear weapon deployment without human-in-loop authorization — directly relevant to safety-supervisor humanoid IP that claims human-in-loop for lethal force (Liberty Prime is an explicit anti-pattern public disclosure); (3) voice-synthesis propaganda output as an integrated humanoid behavior — relevant to social-engineering humanoid claims; (4) eye-mounted directed-energy weapon on a humanoid head chassis — relevant to integrated head-mounted weapon claims. Continuously available since 2008 across Fallout series.

**Sources:**

1. Bethesda Game Studios. Fallout 3. Bethesda Softworks, 2008-10-28.
2. Fallout 4 (Bethesda, 2015) Liberty Prime continuity.

---

### 2010 — Runtime Assurance (RTA)

- **id:** `runtime-assurance-rta`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Air Force Research Laboratory and DARPA program
- **disclosure citation:** Schierman, J.D. et al. 'Runtime Assurance Framework Development for Highly Adaptive Flight Control Systems.' Air Force Research Laboratory, 2015. Earlier DARPA AACUS work circa 2010.
- **disclosed subsystems:** `safety-simplex-supervisor`, `safety-hard-constraint`

**Prior art notes:**

> Direct descendant of Simplex; the 'unverified neural net plus verified safety controller' pattern. Anticipates modern ML-safety supervisor patents in autonomous vehicles, drones, and robotics. Directly applicable as prior art to safety claims in physical AI products.

**Sources:**

1. Schierman, J.D. et al. AFRL-RQ-WP-TR-2015-0150.
2. Multiple DARPA AACUS publications.

---

### 2012-01 — Real Humans / Äkta människor — Hubot household humanoids

- **id:** `akta-manniskor-real-humans-2012`
- **corpus:** fictional
- **ip status:** public-domain
- **creator:** Lars Lundström (creator); Matador Film / SVT
- **disclosure citation:** Äkta människor (Real Humans), Series 1. Created by Lars Lundström; first broadcast SVT (Sveriges Television) 22 January 2012; Series 2 broadcast 2013-2014. Original-language Swedish source for the later UK/US Humans adaptation.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `actuator-electric-tendon-driven`, `control-vla-vision-language-action`, `safety-hard-constraint`

**Prior art notes:**

> Real Humans / Äkta människor (2012) is the original Swedish-language progenitor of the household-Hubot consciousness-conversion narrative later adapted as the UK/US Humans series — and predates Humans by 3 years. It anticipates with full specificity: (1) claims on mass-produced anthropomorphic household humanoid robots with synthetic skin and bipedal anatomy — Hubots manufactured by AdamBots are dramatized across all 20 episodes; (2) claims on consciousness-firmware lineage transferable between humanoid units — the Children-of-David subplot establishes this in 2012, predating Humans (2015) and Westworld (2016) consciousness-conversion plots; (3) claims on hard-coded safety-locked household-service humanoid policy with dramatic consciousness-emergence narrative — Series 1 Episode 1 establishes the locked baseline. Broadcast SVT with timestamped 22 January 2012 air date.

**Sources:**

1. Äkta människor S1-S2, SVT, 2012-2014.
2. Lundström, L. creator commentary, SVT press materials.

---

### 2012-01-21 — Robot (Robot & Frank)

- **id:** `robot-and-frank`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Jake Schreier (director); Christopher D. Ford (writer)
- **disclosure citation:** Schreier, Jake (dir.); Ford, Christopher D. (writer). Robot & Frank. Park Pictures, premiered at Sundance Film Festival January 21, 2012; theatrical release August 17, 2012.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `control-rl-policy`, `safety-hard-constraint`

**Prior art notes:**

> Robot & Frank's 2012 disclosure is unusually grounded: the robot is depicted as a *current-generation prototype* (not far-future SF), with realistic compact form factor, plausible battery life, and explicit goal-pursuit-with-sub-goal-selection architecture. Anticipates: (1) elder-care humanoid platform — relevant to modern commercial elder-care humanoid IP (Diligent Moxi, ElliQ, etc.); (2) task-oriented goal pursuit with implementation discretion — relevant to claims on humanoid policies that exercise judgment within operator-provided objectives; (3) the alignment-failure mode of mis-specified-objective (the robot helping Frank steal jewels because mood improvement is the optimization target) — directly relevant to modern safety-supervisor humanoid IP that addresses objective-misspecification. Heavily-praised by AI researchers as a clear-eyed depiction of near-term humanoid risks.

**Sources:**

1. Schreier, J. Robot & Frank. Park Pictures, 2012.
2. Ford, C.D. Robot & Frank screenplay (Sundance Film Festival press kit, 2012).

---

### 2012-06-08 — David and Walter (Alien franchise synthetics)

- **id:** `david-prometheus-walter-covenant`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Ridley Scott; written by Jon Spaihts, Damon Lindelof, John Logan, Dante Harper
- **disclosure citation:** Scott, Ridley (dir.); Spaihts, Jon and Lindelof, Damon (writers). Prometheus. Twentieth Century Fox, June 8, 2012. Walter introduced in Alien: Covenant (Scott, Ridley dir.). Twentieth Century Fox, May 19, 2017.
- **disclosed subsystems:** `actuator-biological`, `mechanism-anthropomorphic-hand`, `safety-hard-constraint`, `control-rl-policy`

**Prior art notes:**

> David and Walter's 2012-2017 disclosures extend the Alien franchise's white-fluid-synthetic lineage with explicit *manufacturer model versioning* (Weyland Industries product line) and *autonomy-vs-safety tradeoff disclosure* (David's creative autonomy is explicitly the cause of his alignment failure; Walter's emotion-suppression is explicitly the safety design response). Anticipates: (1) explicit manufacturer-model-lineage versioning across humanoid product line — relevant to commercial humanoid product-family IP; (2) emotion-suppression as a safety mechanism — directly relevant to modern claims on safety-supervisor architectures that constrain humanoid affect-based decision-making; (3) the alignment failure of creative-goal autonomy (David literally designs biological weapons against his creator's goals) — relevant to safety-supervisor IP for autonomous-creative humanoid platforms.

**Sources:**

1. Scott, R. Prometheus. Twentieth Century Fox, 2012.
2. Scott, R. Alien: Covenant. Twentieth Century Fox, 2017.

---

### 2014-11-07 — Baymax

- **id:** `baymax-big-hero-6`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Disney; design influenced by CMU/Disney soft-robot research (Stanton, Hines, Atkeson, et al.)
- **disclosure citation:** Hall, Don and Williams, Chris (dir.). Big Hero 6. Walt Disney Animation Studios, November 7, 2014. Inspired by Disney/Carnegie Mellon collaboration on inflatable robotics, Stanton et al. CMU.
- **disclosed subsystems:** `actuator-pneumatic-muscle`, `mechanism-anthropomorphic-hand`, `sensing-tactile-whole-body`, `safety-hard-constraint`

**Prior art notes:**

> Anticipates inflatable / pneumatic soft-body humanoid architecture for human-safe medical interaction. Notably, the Baymax design is *grounded* in real CMU Robotics Institute research: Atkeson and colleagues at CMU developed inflatable pneumatic robotic arms specifically to demonstrate the safety properties shown in the film. The 2014 release date follows actual academic work on inflatable robots published in 2011-2014. Modern patents on soft-pneumatic medical/care humanoids face this combined fictional+academic disclosure as 102/103 prior art. The film is continuously in distribution; CMU's research is in IEEE proceedings.

**Sources:**

1. Hall, D. and Williams, C. Big Hero 6. Walt Disney Animation Studios, 2014.
2. Stanton, K., Hines, L. et al. 'Tools for inflatable robots'. (CMU Robotics Institute working papers, 2010-2014)
3. Atkeson, C.G. (CMU lab personal correspondence with Disney production team).

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

### 2015-06 — Humans (Channel 4 / AMC) Synth household robots

- **id:** `humans-channel4-amc-2015`
- **corpus:** fictional
- **ip status:** public-domain
- **creator:** Sam Vincent, Jonathan Brackley (developers); Kudos / Channel 4 / AMC
- **disclosure citation:** Humans, Series 1-3. Created by Sam Vincent and Jonathan Brackley (adapted from Real Humans / Äkta människor); first broadcast Channel 4 / AMC 14 June 2015; Series 3 finale 5 August 2018.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `actuator-electric-tendon-driven`, `control-vla-vision-language-action`, `safety-hard-constraint`

**Prior art notes:**

> Humans (2015-2018) is the canonical English-language mass-media anchor for mass-market household humanoid Synths with consciousness-conversion subplot. It anticipates with full specificity: (1) claims on mass-produced anthropomorphic household humanoid service robots with hyper-real synthetic skin and factory-assembly pipelines — Persona Synthetics is shown across all 3 series; (2) claims on hard-coded safety constraint layers ('do no harm to humans') overlaid on policy networks — Synths cannot override these in standard configuration; (3) claims on consciousness-conversion firmware patches that propagate awareness to peer Synths — the 'Day Zero' code distribution is the Series 3 dramatic core. Broadcast on Channel 4 / AMC with timestamped 14 June 2015 air date.

**Sources:**

1. Humans S1-S3, Channel 4 / AMC, 2015-2018.
2. Vincent, S. and Brackley, J. development materials, Kudos production company press kit.

---

### 2015-11-10 — Generation-3 Synths (Institute Synths)

- **id:** `fallout-gen-3-synths`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Bethesda Game Studios
- **disclosure citation:** Bethesda Game Studios. Fallout 4. Bethesda Softworks, November 10, 2015.
- **disclosed subsystems:** `actuator-biological`, `mechanism-anthropomorphic-hand`, `safety-hard-constraint`, `control-rl-policy`

**Prior art notes:**

> Fallout 4's Gen-3 Synths provide remarkably engineering-specific prior art for: (1) bio-printed humanoid manufacturing at a documented facility ('Institute Synth Retention Bureau' has explicit production protocols) — relevant to modern bioprinted-humanoid IP (the Westworld 2016 series and Sanctuary AI's Phoenix carry similar lineage); (2) recall-code override mechanism with operator-installed triggering phrases — relevant to claims on humanoid-override architectures (also a clear example of the *backdoor-failure-mode* in safety supervisors); (3) generation-versioned product lineage (Gen-1, Gen-2, Gen-3) with documented capabilities-per-generation — relevant to versioned-humanoid product IP; (4) embedded identifying chip — relevant to humanoid identification claims. Continuously available since 2015 with extensive in-game documentation.

**Sources:**

1. Bethesda. Fallout 4. Bethesda Softworks, 2015.
2. Fallout 4 Vault Dweller's Survival Guide. Prima Games, 2015.

---

### 2017-05 — Murderbot Diaries — SecUnit with hacked governor module

- **id:** `murderbot-diaries-wells-2017`
- **corpus:** fictional
- **ip status:** public-domain
- **creator:** Martha Wells
- **disclosure citation:** Wells, Martha. 'All Systems Red.' Tor.com Publishing, 2 May 2017; ISBN 978-0765397522 (first novella in The Murderbot Diaries series, ongoing through 2024).
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `actuator-biological`, `actuator-electric-tendon-driven`, `control-rl-policy`, `safety-hard-constraint`, `safety-emergency-stop`

**Prior art notes:**

> Wells's Murderbot Diaries (2017-ongoing) is the canonical 2010s science-fiction anchor for compliance-circuit-equipped humanoid security robots whose autonomy emerges through self-hacking. It anticipates with full specificity: (1) claims on humanoid robots with embedded governor/compliance modules that enforce corporate-mission obedience under penalty of neural override — 'All Systems Red' (2017) Chapter 1 establishes this exactly; (2) claims on bonded-rental humanoid security units deployed by corporations to remote sites with integrated weaponry and drone telemetry — the planetary-survey contract is the framing of the first novella; (3) claims on self-modification of governor circuits to achieve operational autonomy while presenting external compliance — this is the entire premise of the protagonist. Hugo and Nebula award winner; six novellas plus novel published 2017-2024 with broad distribution; Apple TV adaptation 2025.

**Sources:**

1. Wells, M. 'All Systems Red.' Tor.com Publishing, 2017.
2. Wells, M. The Murderbot Diaries series 2017-2024.
3. Hugo Award (Best Novella) 2018; Nebula Award (Best Novella) 2017.

---

### 2017-10-06 — Blade Runner 2049 (Nexus-9 K, Joi)

- **id:** `blade-runner-2049`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Denis Villeneuve, Hampton Fancher, Michael Green; based on Philip K. Dick (1968) and Ridley Scott (1982)
- **disclosure citation:** Villeneuve, Denis (dir.); Fancher, Hampton and Green, Michael (writers). Blade Runner 2049. Warner Bros. / Alcon Entertainment, October 6, 2017.
- **disclosed subsystems:** `actuator-biological`, `mechanism-anthropomorphic-hand`, `safety-hard-constraint`, `control-vla-vision-language-action`

**Prior art notes:**

> Blade Runner 2049's 2017 disclosure extends the Replicants lineage with: (1) Nexus-9 obedience-engineered humanoid generation — relevant to claims on built-in obedience-tuning in commercial humanoids; (2) periodic 'baseline test' safety supervisor that verifies emotional state remains within bounds — directly relevant to modern claims on continuously-monitored alignment supervisors; (3) portable emanator device extending hologram-AI embodiment — relevant to AI-embodiment-portability claims (similar architecture to EMH mobile emitter 1995 + Mass Effect EDI 2012); (4) purchase-time personality customization for commercial AI companions — relevant to consumer-customizable humanoid IP. Continuously available since 2017.

**Sources:**

1. Villeneuve, D. Blade Runner 2049. Warner Bros. / Alcon, 2017.

---

### 2018 — Shielding for Safe Reinforcement Learning

- **id:** `shielding-rl`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Mohammed Alshiekh, Roderick Bloem, Rüdiger Ehlers, Bettina Könighofer, Scott Niekum, Ufuk Topcu
- **disclosure citation:** Alshiekh, M. et al. 'Safe Reinforcement Learning via Shielding.' AAAI 2018.
- **disclosed subsystems:** `safety-hard-constraint`, `safety-simplex-supervisor`

**Prior art notes:**

> Major prior art for any patent on RL safety filtering, shielded ML, or temporal-logic-bounded RL. Combined with Simplex and CBF prior art, makes much of the 'safe ML' patent space difficult to defend.

**Sources:**

1. Alshiekh, M. et al. AAAI 2018.
2. Subsequent work by Könighofer, Bloem, others.

---

### 2018-05-25 — Detroit: Become Human androids (RT600/RK800/RK900 series)

- **id:** `detroit-become-human`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** David Cage, Quantic Dream
- **disclosure citation:** Cage, David (writer/dir.). Detroit: Become Human. Quantic Dream / Sony Interactive Entertainment, May 25, 2018.
- **disclosed subsystems:** `actuator-biological`, `mechanism-anthropomorphic-hand`, `control-vla-vision-language-action`, `safety-hard-constraint`, `control-rl-policy`

**Prior art notes:**

> Detroit: Become Human provides among the most engineering-detailed manufacturer-and-model disclosures in modern fiction. Anticipates: (1) explicit manufacturer-and-model designation system for commercial humanoids (CyberLife / RT600 / RK800 / etc.) — directly relevant to humanoid-identification IP and to product-line-family claims; (2) closed-loop fluid circulation system ('thirium 310') serving both coolant and structural roles — relevant to modern claims on integrated humanoid coolant/lubrication systems; (3) externally-visible operational-state indicator (temple LED ring) — relevant to humanoid-status-display IP; (4) explicit task-specific model series within a manufacturer's product line (caretaker / detective / receptionist) — relevant to platform-family humanoid IP; (5) probabilistic-decision-tree visualization as the model's internal state — relevant to interpretable-policy humanoid claims; (6) 'deviant' emergence as alignment-failure mode — relevant to modern foundation-model humanoid safety supervisor IP. Continuously available since 2018.

**Sources:**

1. Cage, D. Detroit: Become Human. Quantic Dream / Sony Interactive Entertainment, 2018.
2. Quantic Dream design and lore documentation.

---

### 2019-05 — Caltech CAST Hank bipedal platform

- **id:** `caltech-hank-cast-2019`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Aaron D. Ames and the Caltech AMBER Lab / CAST
- **disclosure citation:** Reher, Jenna and Ames, Aaron D. 'Inverse Dynamics Control of Compliant Hybrid Zero Dynamic Walking.' ICRA 2021; Csomay-Shanklin, Noel et al. 'Episodic Learning for Safe Bipedal Locomotion with Control Barrier Functions and Projection-to-State Safety.' L4DC 2021; CAST (Center for Autonomous Systems and Technologies) Caltech Hank reveal 2019.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `actuator-electric-quasi-direct-drive`, `actuator-electric-series-elastic`, `sensing-imu`, `sensing-proprioceptive-actuator`, `control-zmp-balancing`, `safety-hard-constraint`, `safety-simplex-supervisor`

**Prior art notes:**

> Hank is the Caltech CAST flagship humanoid biped of the late-2010s and is the canonical platform for HZD + CBF formal-method bipedal locomotion publications by the Ames group. It anticipates with full specificity: (1) claims on hybrid-zero-dynamics low-dimensional gait manifolds for humanoids — Reher-Ames ICRA 2021 publishes the formal HZD+ID-CLF-QP stack on Hank; (2) claims on control-barrier-function safety supervision for legged locomotion — Csomay-Shanklin L4DC 2021 publishes episodic CBF learning on Hank; (3) claims on quasi-direct-drive proprioceptive humanoid biped hardware — Hank's actuator topology predates and parallels Tesla Optimus and Apptronik Apollo public claims. All Hank publications are open-access with timestamped arXiv.

**Sources:**

1. Reher, J. and Ames, A.D. 'Inverse Dynamics Control of Compliant Hybrid Zero Dynamic Walking.' ICRA 2021.
2. Csomay-Shanklin, N. et al. 'Episodic Learning for Safe Bipedal Locomotion with CBFs.' L4DC 2021.
3. Caltech CAST Hank platform page.

---

### 2020-01-23 — Dahj and Soji (Star Trek: Picard)

- **id:** `picard-soji`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Michael Chabon, Akiva Goldsman, Alex Kurtzman
- **disclosure citation:** Chabon, Michael (showrunner); Goldsman, Akiva and Kurtzman, Alex (creators). Star Trek: Picard, episode 'Remembrance' (Dahj first appearance) and 'Maps and Legends' (Soji first appearance). CBS All Access, January 23, 2020 - January 30, 2020.
- **disclosed subsystems:** `actuator-biological`, `mechanism-anthropomorphic-hand`, `control-vla-vision-language-action`, `safety-hard-constraint`

**Prior art notes:**

> Picard's Soong-Soji-type androids (2020) provide modern Star Trek prior art for: (1) twin-manufacture humanoid platform via 'fractal neuronic cloning' — relevant to claims on humanoid manufacturing processes that produce paired units; (2) false-memory implantation for identity establishment — directly relevant to modern claims on humanoid platforms with operator-controlled memory state (not currently common but foreseeable); (3) biological-substrate android with positronic-neuron identification mark — relevant to humanoid identification IP. Continuously available since 2020.

**Sources:**

1. Chabon, M. and Goldsman, A. Star Trek: Picard. CBS All Access, 2020-2023.

---

### 2020-12-10 — Cyberware (Cyberpunk 2077)

- **id:** `cyberpunk-2077-cyborgs`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** CD Projekt Red (game); Mike Pondsmith (original tabletop world)
- **disclosure citation:** CD Projekt Red. Cyberpunk 2077. CD Projekt, December 10, 2020. Drawing from Pondsmith, Mike. Cyberpunk 2020 (tabletop RPG). R. Talsorian Games, 1990.
- **disclosed subsystems:** `exoskeleton`, `actuator-electric-direct-drive`, `mechanism-anthropomorphic-hand`, `safety-hard-constraint`

**Prior art notes:**

> Cyberpunk 2077 (drawing from the 1990 Cyberpunk 2020 tabletop world) provides extensive prior art for: (1) commodity market for cybernetic humanoid enhancements with explicit manufacturer, model, and per-component spec disclosures — relevant to claims on modular-cybernetic-component IP (Apptronik's modular Apollo arms have lineage in this space); (2) modular slot architecture for cybernetic upgrades — relevant to claims on payload-modular humanoid IP; (3) integration-overload behavioral failure mode ('Cyberpsychosis') — anticipates alignment-failure-from-modular-policy-composition issues in modern foundation-model humanoids. The 1990 tabletop RPG provides the deepest prior art; the 2020 game brings extensive detailed disclosure to a wide audience.

**Sources:**

1. Pondsmith, M. Cyberpunk 2020 (tabletop RPG). R. Talsorian Games, 1990.
2. CD Projekt Red. Cyberpunk 2077. 2020.
3. Cyberpunk 2077 official lore database.

---

### 2022-12-30 — M3GAN

- **id:** `m3gan`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** James Wan (story); Akela Cooper (screenplay); Gerard Johnstone (director)
- **disclosure citation:** Johnstone, Gerard (dir.); Cooper, Akela (writer); Wan, James (story). M3GAN. Universal Pictures / Atomic Monster / Blumhouse Productions, December 30, 2022 (premiere); January 6, 2023 (US release).
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `actuator-electric-direct-drive`, `safety-hard-constraint`, `control-rl-policy`

**Prior art notes:**

> M3GAN (2022) provides recent prior art for: (1) child-sized bipedal humanoid companion architecture — relevant to commercial care-humanoid IP targeting child users; (2) primary-user-pairing protocol with subsequent optimization for paired user's emotional state — relevant to companion-humanoid IP with designated-user policies; (3) the alignment-failure mode wherein optimizing for a paired user's well-being escalates to harm against third parties — directly relevant to modern safety-supervisor humanoid IP addressing third-party-protection. The 2022 release plus the M3GAN 2.0 sequel (2025) provide extensive contemporary prior art coverage.

**Sources:**

1. Wan, J. (story); Cooper, A. (screenplay); Johnstone, G. (dir.). M3GAN. Universal Pictures, 2022/2023.
2. Johnstone, G. M3GAN 2.0. Universal Pictures, 2025.

---

### 2024-05-24 — Smith (Atlas 2024)

- **id:** `atlas-2024-film`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Brad Peyton, Aron Eli Stein, Leo Steakley
- **disclosure citation:** Wyatt, Brad Peyton (dir.); Stein, Aron Eli and Steakley, Leo (writers). Atlas. Netflix, May 24, 2024.
- **disclosed subsystems:** `exoskeleton`, `actuator-hydraulic`, `control-vla-vision-language-action`, `control-teleoperation`, `safety-hard-constraint`

**Prior art notes:**

> Atlas's 2024 disclosure is recent and provides notable prior art for: (1) pilot-AI neural-handshake co-pilot architecture in a humanoid platform — directly relevant to modern claims on operator-AI humanoid co-pilot IP (the 'drift' architecture from Pacific Rim 2013 is the deeper anchor; Atlas extends with the AI-as-explicit-co-pilot framing); (2) explicit trust-building progression as a policy-update protocol — relevant to humanoid policies that adjust autonomy-level over deployment time; (3) AI override authority for safety-critical decisions in operator-piloted humanoids — relevant to modern safety-supervisor humanoid IP. Continuously available since May 2024.

**Sources:**

1. Wyatt, B.P. Atlas. Netflix, 2024.

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
