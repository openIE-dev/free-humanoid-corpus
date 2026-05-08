---
title: "control-foundation-model-policy"
parent: "Invalidity Contentions"
nav_order: 31
layout: default
---

# Invalidity Contention Packet — `control-foundation-model-policy`

**Generated:** 2026-05-08  
**Cross-cut tag:** `control-foundation-model-policy`  
**Entries:** 14 (13 commons-grade, 1 draft)  
**Earliest disclosure:** 2021-08  
**Most recent disclosure:** 2025-10

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free Humanoid Corpus that
bears on the subsystem `control-foundation-model-policy`.

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

### 2021-08 — robomimic

- **id:** `robomimic-mandlekar-2021`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Stanford + UT Austin; Ajay Mandlekar, Yuke Zhu, Roberto Martín-Martín, Fei-Fei Li, Silvio Savarese et al.
- **disclosure citation:** Mandlekar, A., Xu, D., Wong, J., Nasiriany, S., Wang, C., Kulkarni, R., Fei-Fei, L., Savarese, S., Zhu, Y., Martín-Martín, R. 'What Matters in Learning from Offline Human Demonstrations for Robot Manipulation'. CoRL 2021; arXiv:2108.03298. Stanford + UT Austin. MIT-licensed framework.
- **disclosed subsystems:** `control-imitation-learning`, `control-foundation-model-policy`, `control-benchmarking`

**Prior art notes:**

> robomimic is the canonical IL benchmark + framework (Mandlekar et al. CoRL 2021). 4-year-deep open-permissive prior art for: standardized imitation-learning datasets + reference algorithms for robotic manipulation. Direct shielding for any commercial humanoid claim on IL training infrastructure. Together with RoboCasa (round-16 entry), Octo (round-15), OpenVLA (round-12), establishes the open-academic IL substrate against which all commercial VLA performance must be measured.

**Sources:**

1. Mandlekar et al. CoRL 2021; arXiv:2108.03298.
2. Project page (robomimic.github.io).
3. GitHub: github.com/ARISE-Initiative/robomimic.

---

### 2023-10 — RT-X / Open X-Embodiment collaboration paper

- **id:** `rt-x-collaboration-2023`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Open X-Embodiment Collaboration (21 institutions, 100+ co-authors)
- **disclosure citation:** Open X-Embodiment Collaboration et al. 'Open X-Embodiment: Robotic Learning Datasets and RT-X Models'. ICRA 2024. arXiv:2310.08864. Cross-institutional collaboration spanning 21 institutions (Google DeepMind, Stanford, UC Berkeley, MIT, CMU, Columbia, NYU, Toyota Research Institute, Imperial College, ETH Zürich, Tokyo Tech, et al.). The paper introducing the dataset now in the corpus as `open-x-embodiment`.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-cross-embodiment`, `control-foundation-model-policy`, `control-imitation-learning`

**Prior art notes:**

> RT-X / Open X-Embodiment collaboration (ICRA 2024) is the canonical 21-institution cross-embodiment VLA collaboration. 1.5-year-deep open-permissive prior art for: publicly-coordinated cross-institutional robot dataset pool, cross-embodiment VLA training methodology, RT-1-X / RT-2-X cross-embodiment models. Direct shielding for any commercial humanoid claim on cross-embodiment VLA training. **The collaboration model itself is novel art** — establishes that open multi-institution dataset pooling for robot learning is well-anticipated public-domain academic practice. Distinct from the dataset entry (`open-x-embodiment` already in corpus) by emphasis on the model-training + collaboration-pattern artifacts.

**Sources:**

1. Open X-Embodiment Collaboration arXiv:2310.08864 ICRA 2024.
2. Project page (robotics-transformer-x.github.io).
3. Open X-Embodiment dataset (robotics-transformer-x.github.io/data).

---

### 2024-04 — Astribot S1

- **id:** `astribot-s1-stardust-2025`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Stardust Intelligence (Shenzhen, China)
- **disclosure citation:** Stardust Intelligence (Shenzhen, China; founded December 2022). Astribot S1 reveal April 2024 via stardust-tech.com / astribot.com demo videos showing 10 m/s arm motion. Stardust Intelligence Astribot Suite paper July 2025 (peer-reviewed; teleop + DuoCore-WB imitation learning achieving 80% task success). Commercial availability late 2025+ in China.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-arm`, `actuator-electric`, `control-imitation-learning`, `control-foundation-model-policy`

**Prior art notes:**

> Astribot S1 is one of the canonical 2024-2025 Chinese commercial humanoid platforms (Stardust Intelligence). 1.5-year-deep public-disclosure prior art for: ≥10 m/s anthropomorphic arm motion (claimed industry-leading), 36-DoF whole-body humanoid, DuoCore-WB whole-body IL framework. Direct shielding for any commercial humanoid claim on extreme arm-speed performance — Astribot's April 2024 viral demo set the public benchmark. Claim surface is peer-reviewed (Astribot Suite paper July 2025), unlike most Chinese commercial humanoid platforms.

**Sources:**

1. Stardust Intelligence corporate site (stardust-tech.com / astribot.com).
2. Astribot Suite paper July 2025 (peer-reviewed; venue TBV).
3. Humanoid Press product database (humanoid.press/database/database-astribot-s1).
4. Origin of Bots, RobotsLATAM, Mike Kalil coverage 2024-2026.

---

### 2024-05 — Octo (Open-Source Generalist Robot Policy)

- **id:** `octo-rss-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Octo Model Team (UC Berkeley + Stanford + CMU + Google DeepMind); Levine + Finn + Sadigh group lineage
- **disclosure citation:** Octo Model Team: Ghosh, D., Walke, H., Pertsch, K., Black, K., Mees, O., Dasari, S., Hejna, J., Kreiman, T., Xu, C., Luo, J., Tan, Y. L., Sanketi, P., Vuong, Q., Xiao, T., Sadigh, D., Finn, C., Levine, S. 'Octo: An Open-Source Generalist Robot Policy'. arXiv:2405.12213, May 2024. Robotics: Science and Systems (RSS) 2024. UC Berkeley + Stanford + Carnegie Mellon + Google DeepMind.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-foundation-model-policy`, `control-diffusion-policy`, `control-cross-embodiment`, `control-imitation-learning`

**Prior art notes:**

> Octo is the canonical first open-source generalist robot policy. 1-year-deep open-permissive academic prior art predating OpenVLA by ~1 month (RSS May 2024 vs OpenVLA arXiv June 2024). Establishes the architectural pattern for: transformer + diffusion-policy action head, Open-X-Embodiment-trained cross-embodiment policy at 27M-93M parameter scale, language-OR-goal-image conditioning. Direct shielding for any commercial humanoid VLA claim on diffusion-policy action heads (RDT-1B, π₀ both build on this) and on Open-X-Embodiment-trained cross-embodiment foundation. Together with OpenVLA, π₀, π₀.₅, OpenVLA-OFT, and RDT-1B, establishes the open academic VLA baseline against which Figure Helix, NVIDIA GR00T N1, Microsoft Magma, and any closed commercial VLA must be evaluated.

**Sources:**

1. Octo Model Team. arXiv:2405.12213 May 2024.
2. RSS 2024 proceedings (roboticsproceedings.org/rss20/p090.pdf).
3. Project page (octo-models.github.io).
4. GitHub: github.com/octo-models/octo.

---

### 2024-06 — OpenVLA

- **id:** `openvla-stanford-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Stanford + Toyota Research Institute + UC Berkeley; Kim, Pertsch, Karamcheti, Liang, Finn, Levine, Tedrake et al.
- **disclosure citation:** Kim, M. J., Pertsch, K., Karamcheti, S., Xiao, T., Balakrishna, A., Nair, S., Rafailov, R., Foster, E., Lam, G., Sanketi, P., Vuong, Q., Kollar, T., Burchfiel, B., Tedrake, R., Sadigh, D., Levine, S., Liang, P., Finn, C. 'OpenVLA: An Open-Source Vision-Language-Action Model'. arXiv:2406.09246, June 2024. CoRL 2024 (PMLR v270, Kim25c). Stanford + Toyota Research Institute + UC Berkeley.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-foundation-model-policy`, `control-imitation-learning`, `control-cross-embodiment`

**Prior art notes:**

> OpenVLA is the canonical first fully-open-source VLA foundation model (CoRL 2024). 23-month-deep open-permissive academic prior art for: 7B-class open-weight VLA, Llama-2-based VLA backbone, Open-X-Embodiment-trained cross-embodiment policy. Direct shielding for any commercial humanoid VLA claim on open-source-equivalent architectural elements. Together with π₀ and π₀.₅, establishes the open-academic VLA baseline against which all closed commercial VLAs (Tesla Optimus, Figure, 1X NEO) must be evaluated.

**Sources:**

1. Kim et al. arXiv:2406.09246 June 2024.
2. CoRL 2024 PMLR v270 Kim25c (proceedings.mlr.press/v270/kim25c.html).
3. OpenVLA project page (openvla.github.io).
4. GitHub: github.com/openvla/openvla.

---

### 2024-06 — RoboCasa

- **id:** `robocasa-nasiriany-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** UT Austin + NVIDIA; Soroush Nasiriany, Abhinav Maddukuri, Yuke Zhu et al.
- **disclosure citation:** Nasiriany, S., Maddukuri, A., Zhang, L., Parikh, A., Lo, A., Joshi, A., Mandlekar, A., Zhu, Y. 'RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots'. arXiv:2406.02523, June 2024. RSS 2024. UT Austin + NVIDIA. RoboCasa365 follow-up (OpenReview tQJYKwc3n4) extends to 365 tasks across 2,500 kitchen environments.
- **disclosed subsystems:** `control-physics-simulation`, `control-imitation-learning`, `control-foundation-model-policy`, `control-loco-manipulation`

**Prior art notes:**

> RoboCasa is the canonical generative-AI-augmented household-task simulation framework (UT Austin + NVIDIA, RSS 2024). ~1-year-deep open-permissive prior art for: generative-AI-authored simulation environments at scale, large-scale (>1k hours) demonstration datasets for VLA training, kitchen-scene household-task benchmark suite. Direct shielding for any commercial humanoid claim on 'training data at scale for household manipulation' — RoboCasa365's 1,600 synthetic + 600 human hours establishes the open-academic baseline.

**Sources:**

1. Nasiriany et al. arXiv:2406.02523 June 2024.
2. Project page (robocasa.ai).
3. GitHub: github.com/robocasa/robocasa.
4. RSS 2024 proceedings (robocasa.ai/assets/robocasa_rss24.pdf).

---

### 2024-10 — π₀ (Pi-Zero)

- **id:** `physical-intelligence-pi0-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Physical Intelligence; Black, Brown, Driess, Finn et al.
- **disclosure citation:** Black, K., Brown, N., Driess, D., Esmail, A., Equi, M., Finn, C., et al. 'π₀: A Vision-Language-Action Flow Model for General Robot Control'. arXiv:2410.24164, October 2024. Physical Intelligence (physicalintelligence.company).
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-flow-matching`, `control-foundation-model-policy`, `control-imitation-learning`

**Prior art notes:**

> π₀ is Physical Intelligence's canonical first VLA foundation policy (Oct 2024). 1.5-year-deep open-academic publication. Establishes architectural prior art for: flow-matching action distribution in VLA, cross-embodiment policy pretraining, single foundation model controlling multiple robot platforms. Direct successor lineage from RT-1 (2022), RT-2 (2023), OpenVLA (2024). Direct shielding for any commercial humanoid claim on VLA-based control (Tesla Optimus, Figure, 1X NEO, Apptronik all face this); particularly for any claim on flow-matching action heads or cross-embodiment pretraining.

**Sources:**

1. Black et al. arXiv:2410.24164 October 2024.
2. Physical Intelligence pi0 paper (physicalintelligence.company/download/pi0.pdf).
3. Physical Intelligence company page (physicalintelligence.company).

---

### 2024-10 — RDT-1B (Robotics Diffusion Transformer)

- **id:** `rdt-1b-thu-2024`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Tsinghua TSAIL (THU-ML); Songming Liu et al.
- **disclosure citation:** Liu, S., et al. 'RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation'. arXiv:2410.07864, October 2024. ICLR 2025. Tsinghua TSAIL (THU-ML) lab.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-foundation-model-policy`, `control-diffusion-policy`, `control-imitation-learning`, `control-bimanual-manipulation`

**Prior art notes:**

> RDT-1B is THU-ML's canonical diffusion-based VLA foundation model for bimanual manipulation (ICLR 2025). 7-month-deep open-permissive prior art for: diffusion-formulation VLA at billion-parameter scale, bimanual manipulation foundation policy, multi-robot pre-training corpus. The canonical Chinese-academy entry in the open-weight VLA race alongside Stanford OpenVLA and Physical Intelligence π₀. Directly cited as a comparison baseline in OpenVLA-OFT (round-12); now resolves correctly. Direct shielding for any commercial humanoid claim on diffusion-based bimanual VLA.

**Sources:**

1. Liu et al. arXiv:2410.07864 October 2024.
2. Project page (rdt-robotics.github.io/rdt-robotics).
3. GitHub: github.com/thu-ml/RoboticsDiffusionTransformer.
4. HuggingFace: huggingface.co/robotics-diffusion-transformer/rdt-1b.

---

### 2025-02 — OpenVLA-OFT

- **id:** `openvla-oft-stanford-2025`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Stanford; Moo Jin Kim, Chelsea Finn, Percy Liang
- **disclosure citation:** Kim, M. J., Finn, C., Liang, P. 'Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success'. arXiv:2502.19645, February 2025. Stanford.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-foundation-model-policy`, `control-action-chunking`, `control-parallel-decoding`, `control-imitation-learning`

**Prior art notes:**

> OpenVLA-OFT is the canonical Optimized Fine-Tuning recipe for VLA models (Stanford, Feb 2025). 15-month-deep prior art on: parallel action decoding for VLA, action chunking + continuous action representation + L1 regression objective combination. Direct shielding for any commercial humanoid VLA fine-tuning claim, particularly any claim on 'fast inference at high success' for humanoid VLAs. Outperforms π₀ on bimanual ALOHA — the canonical academic benchmark for bimanual humanoid manipulation.

**Sources:**

1. Kim, Finn, Liang. arXiv:2502.19645 February 2025.
2. Project page (openvla-oft.github.io).
3. GitHub: github.com/moojink/openvla-oft.

---

### 2025-02 — Magma (Microsoft Multimodal Agent)

- **id:** `microsoft-magma-cvpr-2025`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Microsoft Research; Jianwei Yang et al.
- **disclosure citation:** Yang, J., et al. 'Magma: A Foundation Model for Multimodal AI Agents'. arXiv:2502.13130, February 2025. CVPR 2025. Microsoft Research.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-foundation-model-policy`, `control-multimodal-agent`, `control-set-of-mark-grounding`

**Prior art notes:**

> Magma is Microsoft's canonical multimodal agent foundation model (CVPR 2025). 3-month-deep prior art for: unified digital + physical task foundation policy, Set-of-Mark + Trace-of-Mark visual grounding annotations. Direct shielding for any commercial humanoid claim on 'one model controls both robot manipulation AND computer/phone interaction' (a notable claim cluster from 1X NEO marketing and Sanctuary Phoenix demos). Magma-8B's open weights make it a re-implementable baseline that any commercial claim must outperform on UI + robot benchmarks to differentiate.

**Sources:**

1. Yang et al. arXiv:2502.13130 February 2025.
2. CVPR 2025 paper (openaccess.thecvf.com/content/CVPR2025/html/Yang_Magma_A_Foundation_Model_for_Multimodal_AI_Agents_CVPR_2025_paper.html).
3. Microsoft Research blog (microsoft.com/en-us/research/blog/magma-a-foundation-model-for-multimodal-ai-agents-across-digital-and-physical-worlds/).
4. GitHub: github.com/microsoft/Magma.
5. HuggingFace: huggingface.co/microsoft/Magma-8B.

---

### 2025-02 — Figure Helix

- **id:** `figure-helix-2025`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Figure AI Inc.
- **disclosure citation:** Figure AI Inc. 'Helix: A Vision-Language-Action Model for Generalist Humanoid Control'. Public reveal February 2025 via figure.ai/news/helix. Subsequent disclosures: 'Helix Accelerating Real-World Logistics' (figure.ai/news/helix-logistics) and Hacker News + Robot Report coverage. No academic publication; trade-secret commercial VLA.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-foundation-model-policy`, `control-dual-system-architecture`, `control-high-rate-continuous-control`, `control-bimanual-manipulation`, `control-multi-robot-coordination`

**Prior art notes:**

> Helix is Figure AI's canonical 2025 commercial humanoid VLA. Public-disclosure surface (corporate blog + demo videos + Hacker News + Robot Report coverage) reveals architecture (S1/S2 dual-system, 35-DoF/200Hz, ~500hr teleop training) but withholds neural-network specifics, training-data composition, fine-tuning recipe, and policy-evaluation metrics. The capability set claimed is fully covered by deep open academic prior art chains: (1) S1/S2 dual-system architecture is shared with NVIDIA GR00T N1 (round-15 entry, released within weeks; the cognitive-science S1/S2 pattern dates to Kahneman 'Thinking Fast and Slow' 2011); (2) high-rate continuous VLA control was demonstrated by π₀ (round-12, October 2024) and π₀.₅ (round-12, April 2025) in diffusion/flow-matching form; (3) onboard low-power VLA inference is anticipated by OpenVLA-OFT (round-12, parallel decoding + 26× throughput); (4) multi-robot collaboration is anticipated by ROS 2 (round-13, real-time multi-vehicle middleware) and the Mobile ALOHA / ACT bimanual lineage. Direct shielding for any Helix or Helix-derivative commercial-IP claim.

**Sources:**

1. Figure AI 'Helix' announcement (figure.ai/news/helix), February 2025.
2. Figure AI 'Helix Accelerating Real-World Logistics' (figure.ai/news/helix-logistics), 2025.
3. Robot Report coverage (therobotreport.com/figure-humanoid-robots-demonstrate-helix-model-household-chores/).
4. Hacker News discussion thread (news.ycombinator.com/item?id=43115079).

---

### 2025-03 — NVIDIA Isaac GR00T N1

- **id:** `nvidia-groot-n1-2025`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** NVIDIA; multi-author research team
- **disclosure citation:** NVIDIA. 'GR00T N1: An Open Foundation Model for Generalist Humanoid Robots'. arXiv:2503.14734, March 2025. NVIDIA GTC 2025 announcement. Open commercial license; open weights via HuggingFace nvidia/GR00T-N1-2B. Successor versions N1.6 (full-body) and N1.7 (Cosmos-Reason2 + EgoScale 20K-hour egocentric pre-training) released subsequently.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-foundation-model-policy`, `control-dual-system-architecture`, `control-egocentric-video-pretraining`, `control-cross-embodiment`

**Prior art notes:**

> NVIDIA GR00T N1 is the canonical first open commercial-licensed humanoid foundation model (GTC March 2025). 2-month-deep open prior art for: dual-system S1/S2 humanoid VLA, egocentric-human-video pre-training at scale, NVIDIA Isaac platform integration. Direct architectural sibling of Figure Helix (round-15 entry). Both adopt the dual-system pattern from cognitive science. The N1.7 EgoScale 20K-hour pre-training corpus is itself prior art for any commercial humanoid claim on egocentric-video-trained policy datasets. Direct shielding for any commercial humanoid VLA claim.

**Sources:**

1. arXiv:2503.14734 March 2025.
2. NVIDIA Newsroom announcement (nvidianews.nvidia.com/news/nvidia-isaac-gr00t-n1-open-humanoid-robot-foundation-model-simulation-frameworks).
3. HuggingFace: huggingface.co/nvidia/GR00T-N1-2B.
4. GitHub: github.com/NVIDIA/Isaac-GR00T (versions through N1.7).
5. N1.7 model card (huggingface.co/blog/nvidia/gr00t-n1-7).

---

### 2025-04 — π₀.₅ (Pi-0.5)

- **id:** `physical-intelligence-pi05-2025`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Physical Intelligence; Black et al.
- **disclosure citation:** Black, K., et al. 'π₀.₅: a Vision-Language-Action Model with Open-World Generalization'. arXiv:2504.16054, April 2025. CoRL 2025 (PMLR vol. 305 pp. 17-40, Black25a). Physical Intelligence.
- **disclosed subsystems:** `control-vla-vision-language-action`, `control-foundation-model-policy`, `control-co-training`, `control-loco-manipulation`, `control-semantic-subtask-prediction`

**Prior art notes:**

> π₀.₅ is Physical Intelligence's open-world VLA (CoRL 2025 oral). 1-year-deep prior art on: open-world (new-home) zero-shot mobile manipulation, co-training across multi-robot + web + semantic subtask data, long-horizon (10+ minute) household task autonomy. **The most direct prior art for any commercial humanoid claim on 'works in any home out-of-the-box'** — Tesla Optimus, Figure, 1X NEO, Apptronik all market this generalization claim and now face 1-year-deep open-academic anticipation. Lineage: RT-1 → RT-2 → OpenVLA → π₀ → π₀.₅.

**Sources:**

1. Black et al. arXiv:2504.16054 April 2025.
2. CoRL 2025 PMLR v305 Black25a (proceedings.mlr.press/v305/black25a.html).
3. Physical Intelligence pi0.5 paper (pi.website/download/pi05.pdf).
4. Knowledge Insulating VLA follow-up (physicalintelligence.company/download/pi05_KI.pdf).

---

### 2025-10 — Tesla Optimus Gen 3 *(draft)*

- **id:** `tesla-optimus-gen3-2025`
- **corpus:** private
- **ip status:** trade-secret
- **creator:** Tesla, Inc.
- **disclosure citation:** Tesla, Inc. Optimus Gen 3 product disclosures via Tesla AI Day-class demonstrations + product page (tesla.com/we-robot) + Optimus blog/social-media posts October 2025+. Trade-secret commercial humanoid platform.
- **disclosed subsystems:** `mechanism-bipedal-locomotion`, `mechanism-anthropomorphic-hand`, `mechanism-tendon-driven`, `actuator-electric`, `control-vision-only-perception`, `control-foundation-model-policy`, `sensing-fingertip-tactile`

**Prior art notes:**

> Tesla Optimus Gen 3 is the dominant commercial humanoid product claim surface. Public-disclosure surface (Tesla product page + demos + social-media + investor decks) discloses dimensional specs and high-level architecture; withholds actuator architecture, specific neural-network policies, training-data composition, and on-device inference details. **The 22-DoF hand × 50-actuator claim is the most specific architectural claim** and directly engages prior-art chains in the corpus: Shadow Hand (24-DoF), DLR Hand-II (15-DoF), Pisa-IIT SoftHand (synergy reduction), Tactile SoftHand-A (antagonistic tendons + tactile fingertips, round-11 entry — directly anticipates the tactile-fingertip delicate-manipulation claim), Educational SoftHand-A (round-12 entry — clutch-gear synergy mechanism). Modern claims on tactile-fingertip dexterous manipulation face 2-year-deep tactile-softhand-a prior art and the deeper SoftHand chain back to 2014. Vision-only sensing is shielded by Tesla's own FSD patents (which Tesla cannot use offensively against an own-lineage humanoid claim) but separately by Levine's GPS PR2/BRETT (2016) for vision-driven manipulation. The full Optimus Gen 3 claim surface is therefore element-by-element anticipated by deep open academic chains plus prior commercial humanoids in the corpus.

**Sources:**

1. Tesla Optimus product page (tesla.com/we-robot).
2. Humanoid Press 'Optimus 3' database entry (humanoid.press/database/humanoid-press-database-tesla-optimus-3/).
3. Basenor explainer 'Tesla Optimus Gen 3 Hands: 22-DoF, 50 Actuators Explained'.
4. AI Robots Media coverage (airobots.media/technology/tesla-optimus-gen-3-everything-we-know-about-teslas-most-ambitious-product/).
5. Wikipedia 'Optimus (robot)' (en.wikipedia.org/wiki/Optimus_(robot)).

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

*Generated from <https://github.com/openIE-dev/free-humanoid-corpus> at corpus revision `bf892af`.*
