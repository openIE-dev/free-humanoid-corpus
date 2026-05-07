---
title: safety-simplex-supervisor
parent: Cross-cuts
layout: default
---

# Cross-cut: `safety-simplex-supervisor`

**8 corpus entries disclose this subsystem.**

Earliest disclosure: 1940-09

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Asimov positronic robots (1940-09)

- **id**: `asimov-positronic-robots`
- **corpus**: fictional
- **creator**: Isaac Asimov
- **disclosure**: Asimov, Isaac. 'Robbie' (originally 'Strange Playfellow'). Super Science Stories, September 1940.
- **ip status**: fictional
- **prior art notes**: Establishes hard-constraint safety architecture as a hardware-level concern, not a software policy. Directly anticipates modern AI safety frameworks including Simplex supervisor architectures and constraint-based safety middleware. Specifically anticipates: hardware-level safety constraints with deterministic priority ordering.

## HAL 9000 (1968-04-02)

- **id**: `hal-9000`
- **corpus**: fictional
- **creator**: Arthur C. Clarke / Stanley Kubrick
- **disclosure**: Kubrick, Stanley (dir.). 2001: A Space Odyssey. MGM, 1968-04-02. Clarke, Arthur C. novelization, 1968.
- **ip status**: fictional
- **prior art notes**: HAL is included not as a humanoid but as the canonical depiction of safety failure due to conflicting goals — directly relevant to MathGround's framing of supervisor architectures and the need for explicit constraint hierarchies.

## Akira (Tetsuo cyborg-mutation, Akira containment) (1982-12)

- **id**: `akira-tetsuo-1988`
- **corpus**: fictional
- **creator**: Katsuhiro Otomo
- **disclosure**: Otomo, Katsuhiro. Akira. Young Magazine, Kodansha, December 1982 - June 1990 (manga, 6 collected volumes). Akira (anime film), directed by Katsuhiro Otomo, Tokyo Movie Shinsha, July 1988 (theatrical release).
- **ip status**: fictional
- **prior art notes**: Otomo's Akira (1982 manga / 1988 film) is the canonical fictional disclosure of biomechanical-cyborg uncontrolled-growth dynamics and adversarial-cyborg containment architecture. Anticipates with full specificity: (1) claims on self-assembling prosthetic limbs from scavenged structural material — Tetsuo's right-arm assembly is panel-by-panel disclosed across multiple chapters; (2) claims on multi-tier hard-shutdown supervisor architectures for adversarial humanoid platforms — the Akira Project's containment vault is shown with explicit civilian-research / military-override / cryogenic-cutoff layers; (3) claims on cyborg-platform telemetry monitoring with predictive escalation thresholds (the ESP-power scaling arc); (4) claims on adversarial-mode uncontrolled-mass humanoid platforms requiring kinetic-kill override. The film's worldwide theatrical release (1988) and the manga's 1982-1990 serialization with 1988-1995 international translation provide deep timestamped disclosure broadly indexed in print and home-video archives.

## Asimov's Zeroth Law (1985)

- **id**: `asimovs-zeroth-law`
- **corpus**: fictional
- **creator**: Isaac Asimov
- **disclosure**: Asimov, Isaac. Robots and Empire. Doubleday, 1985.
- **ip status**: fictional
- **prior art notes**: Significant for safety architecture prior art because it explicitly demonstrates priority-reordering in a hard-constraint hierarchy under conflicting goals. Anticipates modern AI safety frameworks dealing with population-scale or systemic harm tradeoffs.

## Simplex Architecture (1995)

- **id**: `sherman-simplex-architecture`
- **corpus**: academic
- **creator**: Lui Sha, Carnegie Mellon University
- **disclosure**: Sha, Lui. 'Dependable system upgrade.' Proceedings 19th IEEE Real-Time Systems Symposium, 1998. Earlier conceptual work circa 1995.
- **ip status**: public-domain
- **prior art notes**: Foundational prior art for safety supervisor architectures in robotics and physical AI. Any 'safety supervisor' or 'safety envelope' or 'fallback controller' patent claim post-1995 must contend with Sha's Simplex work as anticipating prior art. Directly relevant to MathGround's Simplex supervisor architecture.

## Runtime Assurance (RTA) (2010)

- **id**: `runtime-assurance-rta`
- **corpus**: academic
- **creator**: Air Force Research Laboratory and DARPA program
- **disclosure**: Schierman, J.D. et al. 'Runtime Assurance Framework Development for Highly Adaptive Flight Control Systems.' Air Force Research Laboratory, 2015. Earlier DARPA AACUS work circa 2010.
- **ip status**: public-domain
- **prior art notes**: Direct descendant of Simplex; the 'unverified neural net plus verified safety controller' pattern. Anticipates modern ML-safety supervisor patents in autonomous vehicles, drones, and robotics. Directly applicable as prior art to safety claims in physical AI products.

## Shielding for Safe Reinforcement Learning (2018)

- **id**: `shielding-rl`
- **corpus**: academic
- **creator**: Mohammed Alshiekh, Roderick Bloem, Rüdiger Ehlers, Bettina Könighofer, Scott Niekum, Ufuk Topcu
- **disclosure**: Alshiekh, M. et al. 'Safe Reinforcement Learning via Shielding.' AAAI 2018.
- **ip status**: public-domain
- **prior art notes**: Major prior art for any patent on RL safety filtering, shielded ML, or temporal-logic-bounded RL. Combined with Simplex and CBF prior art, makes much of the 'safe ML' patent space difficult to defend.

## Caltech CAST Hank bipedal platform (2019-05)

- **id**: `caltech-hank-cast-2019`
- **corpus**: academic
- **creator**: Aaron D. Ames and the Caltech AMBER Lab / CAST
- **disclosure**: Reher, Jenna and Ames, Aaron D. 'Inverse Dynamics Control of Compliant Hybrid Zero Dynamic Walking.' ICRA 2021; Csomay-Shanklin, Noel et al. 'Episodic Learning for Safe Bipedal Locomotion with Control Barrier Functions and Projection-to-State Safety.' L4DC 2021; CAST (Center for Autonomous Systems and Technologies) Caltech Hank reveal 2019.
- **ip status**: public-domain
- **prior art notes**: Hank is the Caltech CAST flagship humanoid biped of the late-2010s and is the canonical platform for HZD + CBF formal-method bipedal locomotion publications by the Ames group. It anticipates with full specificity: (1) claims on hybrid-zero-dynamics low-dimensional gait manifolds for humanoids — Reher-Ames ICRA 2021 publishes the formal HZD+ID-CLF-QP stack on Hank; (2) claims on control-barrier-function safety supervision for legged locomotion — Csomay-Shanklin L4DC 2021 publishes episodic CBF learning on Hank; (3) claims on quasi-direct-drive proprioceptive humanoid biped hardware — Hank's actuator topology predates and parallels Tesla Optimus and Apptronik Apollo public claims. All Hank publications are open-access with timestamped arXiv.
