---
title: control-foundation-model-policy
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-foundation-model-policy`

**16 corpus entries disclose this subsystem.**

Earliest disclosure: 2021-08

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## robomimic (2021-08)

- **id**: `robomimic-mandlekar-2021`
- **corpus**: academic
- **creator**: Stanford + UT Austin; Ajay Mandlekar, Yuke Zhu, Roberto Martín-Martín, Fei-Fei Li, Silvio Savarese et al.
- **disclosure**: Mandlekar, A., Xu, D., Wong, J., Nasiriany, S., Wang, C., Kulkarni, R., Fei-Fei, L., Savarese, S., Zhu, Y., Martín-Martín, R. 'What Matters in Learning from Offline Human Demonstrations for Robot Manipulation'. CoRL 2021; arXiv:2108.03298. Stanford + UT Austin. MIT-licensed framework.
- **ip status**: open-permissive
- **prior art notes**: robomimic is the canonical IL benchmark + framework (Mandlekar et al. CoRL 2021). 4-year-deep open-permissive prior art for: standardized imitation-learning datasets + reference algorithms for robotic manipulation. Direct shielding for any commercial humanoid claim on IL training infrastructure. Together with RoboCasa (round-16 entry), Octo (round-15), OpenVLA (round-12), establishes the open-academic IL substrate against which all commercial VLA performance must be measured.

## RT-X / Open X-Embodiment collaboration paper (2023-10)

- **id**: `rt-x-collaboration-2023`
- **corpus**: academic
- **creator**: Open X-Embodiment Collaboration (21 institutions, 100+ co-authors)
- **disclosure**: Open X-Embodiment Collaboration et al. 'Open X-Embodiment: Robotic Learning Datasets and RT-X Models'. ICRA 2024. arXiv:2310.08864. Cross-institutional collaboration spanning 21 institutions (Google DeepMind, Stanford, UC Berkeley, MIT, CMU, Columbia, NYU, Toyota Research Institute, Imperial College, ETH Zürich, Tokyo Tech, et al.). The paper introducing the dataset now in the corpus as `open-x-embodiment`.
- **ip status**: open-permissive
- **prior art notes**: RT-X / Open X-Embodiment collaboration (ICRA 2024) is the canonical 21-institution cross-embodiment VLA collaboration. 1.5-year-deep open-permissive prior art for: publicly-coordinated cross-institutional robot dataset pool, cross-embodiment VLA training methodology, RT-1-X / RT-2-X cross-embodiment models. Direct shielding for any commercial humanoid claim on cross-embodiment VLA training. **The collaboration model itself is novel art** — establishes that open multi-institution dataset pooling for robot learning is well-anticipated public-domain academic practice. Distinct from the dataset entry (`open-x-embodiment` already in corpus) by emphasis on the model-training + collaboration-pattern artifacts.

## Astribot S1 (2024-04)

- **id**: `astribot-s1-stardust-2025`
- **corpus**: private
- **creator**: Stardust Intelligence (Shenzhen, China)
- **disclosure**: Stardust Intelligence (Shenzhen, China; founded December 2022). Astribot S1 reveal April 2024 via stardust-tech.com / astribot.com demo videos showing 10 m/s arm motion. Stardust Intelligence Astribot Suite paper July 2025 (peer-reviewed; teleop + DuoCore-WB imitation learning achieving 80% task success). Commercial availability late 2025+ in China.
- **ip status**: trade-secret
- **prior art notes**: Astribot S1 is one of the canonical 2024-2025 Chinese commercial humanoid platforms (Stardust Intelligence). 1.5-year-deep public-disclosure prior art for: ≥10 m/s anthropomorphic arm motion (claimed industry-leading), 36-DoF whole-body humanoid, DuoCore-WB whole-body IL framework. Direct shielding for any commercial humanoid claim on extreme arm-speed performance — Astribot's April 2024 viral demo set the public benchmark. Claim surface is peer-reviewed (Astribot Suite paper July 2025), unlike most Chinese commercial humanoid platforms.

## Octo (Open-Source Generalist Robot Policy) (2024-05)

- **id**: `octo-rss-2024`
- **corpus**: academic
- **creator**: Octo Model Team (UC Berkeley + Stanford + CMU + Google DeepMind); Levine + Finn + Sadigh group lineage
- **disclosure**: Octo Model Team: Ghosh, D., Walke, H., Pertsch, K., Black, K., Mees, O., Dasari, S., Hejna, J., Kreiman, T., Xu, C., Luo, J., Tan, Y. L., Sanketi, P., Vuong, Q., Xiao, T., Sadigh, D., Finn, C., Levine, S. 'Octo: An Open-Source Generalist Robot Policy'. arXiv:2405.12213, May 2024. Robotics: Science and Systems (RSS) 2024. UC Berkeley + Stanford + Carnegie Mellon + Google DeepMind.
- **ip status**: open-permissive
- **prior art notes**: Octo is the canonical first open-source generalist robot policy. 1-year-deep open-permissive academic prior art predating OpenVLA by ~1 month (RSS May 2024 vs OpenVLA arXiv June 2024). Establishes the architectural pattern for: transformer + diffusion-policy action head, Open-X-Embodiment-trained cross-embodiment policy at 27M-93M parameter scale, language-OR-goal-image conditioning. Direct shielding for any commercial humanoid VLA claim on diffusion-policy action heads (RDT-1B, π₀ both build on this) and on Open-X-Embodiment-trained cross-embodiment foundation. Together with OpenVLA, π₀, π₀.₅, OpenVLA-OFT, and RDT-1B, establishes the open academic VLA baseline against which Figure Helix, NVIDIA GR00T N1, Microsoft Magma, and any closed commercial VLA must be evaluated.

## OpenVLA (2024-06)

- **id**: `openvla-stanford-2024`
- **corpus**: academic
- **creator**: Stanford + Toyota Research Institute + UC Berkeley; Kim, Pertsch, Karamcheti, Liang, Finn, Levine, Tedrake et al.
- **disclosure**: Kim, M. J., Pertsch, K., Karamcheti, S., Xiao, T., Balakrishna, A., Nair, S., Rafailov, R., Foster, E., Lam, G., Sanketi, P., Vuong, Q., Kollar, T., Burchfiel, B., Tedrake, R., Sadigh, D., Levine, S., Liang, P., Finn, C. 'OpenVLA: An Open-Source Vision-Language-Action Model'. arXiv:2406.09246, June 2024. CoRL 2024 (PMLR v270, Kim25c). Stanford + Toyota Research Institute + UC Berkeley.
- **ip status**: open-permissive
- **prior art notes**: OpenVLA is the canonical first fully-open-source VLA foundation model (CoRL 2024). 23-month-deep open-permissive academic prior art for: 7B-class open-weight VLA, Llama-2-based VLA backbone, Open-X-Embodiment-trained cross-embodiment policy. Direct shielding for any commercial humanoid VLA claim on open-source-equivalent architectural elements. Together with π₀ and π₀.₅, establishes the open-academic VLA baseline against which all closed commercial VLAs (Tesla Optimus, Figure, 1X NEO) must be evaluated.

## RoboCasa (2024-06)

- **id**: `robocasa-nasiriany-2024`
- **corpus**: academic
- **creator**: UT Austin + NVIDIA; Soroush Nasiriany, Abhinav Maddukuri, Yuke Zhu et al.
- **disclosure**: Nasiriany, S., Maddukuri, A., Zhang, L., Parikh, A., Lo, A., Joshi, A., Mandlekar, A., Zhu, Y. 'RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots'. arXiv:2406.02523, June 2024. RSS 2024. UT Austin + NVIDIA. RoboCasa365 follow-up (OpenReview tQJYKwc3n4) extends to 365 tasks across 2,500 kitchen environments.
- **ip status**: open-permissive
- **prior art notes**: RoboCasa is the canonical generative-AI-augmented household-task simulation framework (UT Austin + NVIDIA, RSS 2024). ~1-year-deep open-permissive prior art for: generative-AI-authored simulation environments at scale, large-scale (>1k hours) demonstration datasets for VLA training, kitchen-scene household-task benchmark suite. Direct shielding for any commercial humanoid claim on 'training data at scale for household manipulation' — RoboCasa365's 1,600 synthetic + 600 human hours establishes the open-academic baseline.

## π₀ (Pi-Zero) (2024-10)

- **id**: `physical-intelligence-pi0-2024`
- **corpus**: academic
- **creator**: Physical Intelligence; Black, Brown, Driess, Finn et al.
- **disclosure**: Black, K., Brown, N., Driess, D., Esmail, A., Equi, M., Finn, C., et al. 'π₀: A Vision-Language-Action Flow Model for General Robot Control'. arXiv:2410.24164, October 2024. Physical Intelligence (physicalintelligence.company).
- **ip status**: open-permissive
- **prior art notes**: π₀ is Physical Intelligence's canonical first VLA foundation policy (Oct 2024). 1.5-year-deep open-academic publication. Establishes architectural prior art for: flow-matching action distribution in VLA, cross-embodiment policy pretraining, single foundation model controlling multiple robot platforms. Direct successor lineage from RT-1 (2022), RT-2 (2023), OpenVLA (2024). Direct shielding for any commercial humanoid claim on VLA-based control (Tesla Optimus, Figure, 1X NEO, Apptronik all face this); particularly for any claim on flow-matching action heads or cross-embodiment pretraining.

## RDT-1B (Robotics Diffusion Transformer) (2024-10)

- **id**: `rdt-1b-thu-2024`
- **corpus**: academic
- **creator**: Tsinghua TSAIL (THU-ML); Songming Liu et al.
- **disclosure**: Liu, S., et al. 'RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation'. arXiv:2410.07864, October 2024. ICLR 2025. Tsinghua TSAIL (THU-ML) lab.
- **ip status**: open-permissive
- **prior art notes**: RDT-1B is THU-ML's canonical diffusion-based VLA foundation model for bimanual manipulation (ICLR 2025). 7-month-deep open-permissive prior art for: diffusion-formulation VLA at billion-parameter scale, bimanual manipulation foundation policy, multi-robot pre-training corpus. The canonical Chinese-academy entry in the open-weight VLA race alongside Stanford OpenVLA and Physical Intelligence π₀. Directly cited as a comparison baseline in OpenVLA-OFT (round-12); now resolves correctly. Direct shielding for any commercial humanoid claim on diffusion-based bimanual VLA.

## OpenVLA-OFT (2025-02)

- **id**: `openvla-oft-stanford-2025`
- **corpus**: academic
- **creator**: Stanford; Moo Jin Kim, Chelsea Finn, Percy Liang
- **disclosure**: Kim, M. J., Finn, C., Liang, P. 'Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success'. arXiv:2502.19645, February 2025. Stanford.
- **ip status**: open-permissive
- **prior art notes**: OpenVLA-OFT is the canonical Optimized Fine-Tuning recipe for VLA models (Stanford, Feb 2025). 15-month-deep prior art on: parallel action decoding for VLA, action chunking + continuous action representation + L1 regression objective combination. Direct shielding for any commercial humanoid VLA fine-tuning claim, particularly any claim on 'fast inference at high success' for humanoid VLAs. Outperforms π₀ on bimanual ALOHA — the canonical academic benchmark for bimanual humanoid manipulation.

## Magma (Microsoft Multimodal Agent) (2025-02)

- **id**: `microsoft-magma-cvpr-2025`
- **corpus**: academic
- **creator**: Microsoft Research; Jianwei Yang et al.
- **disclosure**: Yang, J., et al. 'Magma: A Foundation Model for Multimodal AI Agents'. arXiv:2502.13130, February 2025. CVPR 2025. Microsoft Research.
- **ip status**: open-permissive
- **prior art notes**: Magma is Microsoft's canonical multimodal agent foundation model (CVPR 2025). 3-month-deep prior art for: unified digital + physical task foundation policy, Set-of-Mark + Trace-of-Mark visual grounding annotations. Direct shielding for any commercial humanoid claim on 'one model controls both robot manipulation AND computer/phone interaction' (a notable claim cluster from 1X NEO marketing and Sanctuary Phoenix demos). Magma-8B's open weights make it a re-implementable baseline that any commercial claim must outperform on UI + robot benchmarks to differentiate.

## Figure Helix (2025-02)

- **id**: `figure-helix-2025`
- **corpus**: private
- **creator**: Figure AI Inc.
- **disclosure**: Figure AI Inc. 'Helix: A Vision-Language-Action Model for Generalist Humanoid Control'. Public reveal February 2025 via figure.ai/news/helix. Subsequent disclosures: 'Helix Accelerating Real-World Logistics' (figure.ai/news/helix-logistics) and Hacker News + Robot Report coverage. No academic publication; trade-secret commercial VLA.
- **ip status**: trade-secret
- **prior art notes**: Helix is Figure AI's canonical 2025 commercial humanoid VLA. Public-disclosure surface (corporate blog + demo videos + Hacker News + Robot Report coverage) reveals architecture (S1/S2 dual-system, 35-DoF/200Hz, ~500hr teleop training) but withholds neural-network specifics, training-data composition, fine-tuning recipe, and policy-evaluation metrics. The capability set claimed is fully covered by deep open academic prior art chains: (1) S1/S2 dual-system architecture is shared with NVIDIA GR00T N1 (round-15 entry, released within weeks; the cognitive-science S1/S2 pattern dates to Kahneman 'Thinking Fast and Slow' 2011); (2) high-rate continuous VLA control was demonstrated by π₀ (round-12, October 2024) and π₀.₅ (round-12, April 2025) in diffusion/flow-matching form; (3) onboard low-power VLA inference is anticipated by OpenVLA-OFT (round-12, parallel decoding + 26× throughput); (4) multi-robot collaboration is anticipated by ROS 2 (round-13, real-time multi-vehicle middleware) and the Mobile ALOHA / ACT bimanual lineage. Direct shielding for any Helix or Helix-derivative commercial-IP claim.

## NVIDIA Isaac GR00T N1 (2025-03)

- **id**: `nvidia-groot-n1-2025`
- **corpus**: academic
- **creator**: NVIDIA; multi-author research team
- **disclosure**: NVIDIA. 'GR00T N1: An Open Foundation Model for Generalist Humanoid Robots'. arXiv:2503.14734, March 2025. NVIDIA GTC 2025 announcement. Open commercial license; open weights via HuggingFace nvidia/GR00T-N1-2B. Successor versions N1.6 (full-body) and N1.7 (Cosmos-Reason2 + EgoScale 20K-hour egocentric pre-training) released subsequently.
- **ip status**: open-permissive
- **prior art notes**: NVIDIA GR00T N1 is the canonical first open commercial-licensed humanoid foundation model (GTC March 2025). 2-month-deep open prior art for: dual-system S1/S2 humanoid VLA, egocentric-human-video pre-training at scale, NVIDIA Isaac platform integration. Direct architectural sibling of Figure Helix (round-15 entry). Both adopt the dual-system pattern from cognitive science. The N1.7 EgoScale 20K-hour pre-training corpus is itself prior art for any commercial humanoid claim on egocentric-video-trained policy datasets. Direct shielding for any commercial humanoid VLA claim.

## Google DeepMind Gemini Robotics 1.5 (2025-03)

- **id**: `google-gemini-robotics-1-5-2025`
- **corpus**: private
- **creator**: Google DeepMind
- **disclosure**: Google DeepMind. Gemini Robotics + Gemini Robotics-ER (Embodied Reasoning) reveal March 12 2025 via deepmind.google. Gemini Robotics 1.5 announced June 2025. The first VLA built atop Gemini 2.0 Flash foundation model.
- **ip status**: trade-secret
- **prior art notes**: Gemini Robotics 1.5 is Google DeepMind's canonical 2025 commercial VLA built atop Gemini 2.0 Flash. ~6-month-deep public-disclosure prior art at corpus-entry time. The successor to RT-1 (corpus) + RT-2 (corpus) in the Google DeepMind VLA lineage. Direct shielding for any commercial humanoid VLA claim on 'foundation-model-backbone-conditioned policy'.

## π₀.₅ (Pi-0.5) (2025-04)

- **id**: `physical-intelligence-pi05-2025`
- **corpus**: academic
- **creator**: Physical Intelligence; Black et al.
- **disclosure**: Black, K., et al. 'π₀.₅: a Vision-Language-Action Model with Open-World Generalization'. arXiv:2504.16054, April 2025. CoRL 2025 (PMLR vol. 305 pp. 17-40, Black25a). Physical Intelligence.
- **ip status**: open-permissive
- **prior art notes**: π₀.₅ is Physical Intelligence's open-world VLA (CoRL 2025 oral). 1-year-deep prior art on: open-world (new-home) zero-shot mobile manipulation, co-training across multi-robot + web + semantic subtask data, long-horizon (10+ minute) household task autonomy. **The most direct prior art for any commercial humanoid claim on 'works in any home out-of-the-box'** — Tesla Optimus, Figure, 1X NEO, Apptronik all market this generalization claim and now face 1-year-deep open-academic anticipation. Lineage: RT-1 → RT-2 → OpenVLA → π₀ → π₀.₅.

## π₀.₅ Knowledge Insulating (Pi-0.5 KI) (2025-09)

- **id**: `physical-intelligence-pi05-ki-2025`
- **corpus**: academic
- **creator**: Physical Intelligence
- **disclosure**: Physical Intelligence. 'π₀.₅: Knowledge Insulating' technical report Sept 2025 via physicalintelligence.company/download/pi05_KI.pdf. Successor variant to π₀.₅ (round-12 entry) addressing catastrophic forgetting + multi-task interference.
- **ip status**: open-permissive
- **prior art notes**: π₀.₅ KI is Physical Intelligence's Sept 2025 architectural extension of π₀.₅ (round-12). 8-month-deep prior art for: knowledge-insulation in VLA, catastrophic-forgetting mitigation in foundation-policy training. Direct shielding for any commercial humanoid claim on multi-task VLA training without interference.

## Tesla Optimus Gen 3 (2025-10)

- **id**: `tesla-optimus-gen3-2025`
- **corpus**: private
- **creator**: Tesla, Inc.
- **disclosure**: Tesla, Inc. Optimus Gen 3 product disclosures via Tesla AI Day-class demonstrations + product page (tesla.com/we-robot) + Optimus blog/social-media posts October 2025+. Trade-secret commercial humanoid platform.
- **ip status**: trade-secret
- **prior art notes**: Tesla Optimus Gen 3 is the dominant commercial humanoid product claim surface. Public-disclosure surface (Tesla product page + demos + social-media + investor decks) discloses dimensional specs and high-level architecture; withholds actuator architecture, specific neural-network policies, training-data composition, and on-device inference details. **The 22-DoF hand × 50-actuator claim is the most specific architectural claim** and directly engages prior-art chains in the corpus: Shadow Hand (24-DoF), DLR Hand-II (15-DoF), Pisa-IIT SoftHand (synergy reduction), Tactile SoftHand-A (antagonistic tendons + tactile fingertips, round-11 entry — directly anticipates the tactile-fingertip delicate-manipulation claim), Educational SoftHand-A (round-12 entry — clutch-gear synergy mechanism). Modern claims on tactile-fingertip dexterous manipulation face 2-year-deep tactile-softhand-a prior art and the deeper SoftHand chain back to 2014. Vision-only sensing is shielded by Tesla's own FSD patents (which Tesla cannot use offensively against an own-lineage humanoid claim) but separately by Levine's GPS PR2/BRETT (2016) for vision-driven manipulation. The full Optimus Gen 3 claim surface is therefore element-by-element anticipated by deep open academic chains plus prior commercial humanoids in the corpus.
