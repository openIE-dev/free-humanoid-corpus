---
title: "safety-simplex-supervisor"
parent: "Invalidity Contentions"
nav_order: 56
layout: default
---

# Invalidity Contention Packet — `safety-simplex-supervisor`

**Generated:** 2026-05-07  
**Cross-cut tag:** `safety-simplex-supervisor`  
**Entries:** 8 (8 commons-grade, 0 draft)  
**Earliest disclosure:** 1940-09  
**Most recent disclosure:** 2019-05

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `safety-simplex-supervisor`.

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `0ab4327`.*
