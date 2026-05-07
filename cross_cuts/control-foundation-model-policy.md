---
title: control-foundation-model-policy
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-foundation-model-policy`

**4 corpus entries disclose this subsystem.**

Earliest disclosure: 2024-06

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## OpenVLA (2024-06)

- **id**: `openvla-stanford-2024`
- **corpus**: academic
- **creator**: Stanford + Toyota Research Institute + UC Berkeley; Kim, Pertsch, Karamcheti, Liang, Finn, Levine, Tedrake et al.
- **disclosure**: Kim, M. J., Pertsch, K., Karamcheti, S., Xiao, T., Balakrishna, A., Nair, S., Rafailov, R., Foster, E., Lam, G., Sanketi, P., Vuong, Q., Kollar, T., Burchfiel, B., Tedrake, R., Sadigh, D., Levine, S., Liang, P., Finn, C. 'OpenVLA: An Open-Source Vision-Language-Action Model'. arXiv:2406.09246, June 2024. CoRL 2024 (PMLR v270, Kim25c). Stanford + Toyota Research Institute + UC Berkeley.
- **ip status**: open-permissive
- **prior art notes**: OpenVLA is the canonical first fully-open-source VLA foundation model (CoRL 2024). 23-month-deep open-permissive academic prior art for: 7B-class open-weight VLA, Llama-2-based VLA backbone, Open-X-Embodiment-trained cross-embodiment policy. Direct shielding for any commercial humanoid VLA claim on open-source-equivalent architectural elements. Together with π₀ and π₀.₅, establishes the open-academic VLA baseline against which all closed commercial VLAs (Tesla Optimus, Figure, 1X NEO) must be evaluated.

## π₀ (Pi-Zero) (2024-10)

- **id**: `physical-intelligence-pi0-2024`
- **corpus**: academic
- **creator**: Physical Intelligence; Black, Brown, Driess, Finn et al.
- **disclosure**: Black, K., Brown, N., Driess, D., Esmail, A., Equi, M., Finn, C., et al. 'π₀: A Vision-Language-Action Flow Model for General Robot Control'. arXiv:2410.24164, October 2024. Physical Intelligence (physicalintelligence.company).
- **ip status**: open-permissive
- **prior art notes**: π₀ is Physical Intelligence's canonical first VLA foundation policy (Oct 2024). 1.5-year-deep open-academic publication. Establishes architectural prior art for: flow-matching action distribution in VLA, cross-embodiment policy pretraining, single foundation model controlling multiple robot platforms. Direct successor lineage from RT-1 (2022), RT-2 (2023), OpenVLA (2024). Direct shielding for any commercial humanoid claim on VLA-based control (Tesla Optimus, Figure, 1X NEO, Apptronik all face this); particularly for any claim on flow-matching action heads or cross-embodiment pretraining.

## OpenVLA-OFT (2025-02)

- **id**: `openvla-oft-stanford-2025`
- **corpus**: academic
- **creator**: Stanford; Moo Jin Kim, Chelsea Finn, Percy Liang
- **disclosure**: Kim, M. J., Finn, C., Liang, P. 'Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success'. arXiv:2502.19645, February 2025. Stanford.
- **ip status**: open-permissive
- **prior art notes**: OpenVLA-OFT is the canonical Optimized Fine-Tuning recipe for VLA models (Stanford, Feb 2025). 15-month-deep prior art on: parallel action decoding for VLA, action chunking + continuous action representation + L1 regression objective combination. Direct shielding for any commercial humanoid VLA fine-tuning claim, particularly any claim on 'fast inference at high success' for humanoid VLAs. Outperforms π₀ on bimanual ALOHA — the canonical academic benchmark for bimanual humanoid manipulation.

## π₀.₅ (Pi-0.5) (2025-04)

- **id**: `physical-intelligence-pi05-2025`
- **corpus**: academic
- **creator**: Physical Intelligence; Black et al.
- **disclosure**: Black, K., et al. 'π₀.₅: a Vision-Language-Action Model with Open-World Generalization'. arXiv:2504.16054, April 2025. CoRL 2025 (PMLR vol. 305 pp. 17-40, Black25a). Physical Intelligence.
- **ip status**: open-permissive
- **prior art notes**: π₀.₅ is Physical Intelligence's open-world VLA (CoRL 2025 oral). 1-year-deep prior art on: open-world (new-home) zero-shot mobile manipulation, co-training across multi-robot + web + semantic subtask data, long-horizon (10+ minute) household task autonomy. **The most direct prior art for any commercial humanoid claim on 'works in any home out-of-the-box'** — Tesla Optimus, Figure, 1X NEO, Apptronik all market this generalization claim and now face 1-year-deep open-academic anticipation. Lineage: RT-1 → RT-2 → OpenVLA → π₀ → π₀.₅.
