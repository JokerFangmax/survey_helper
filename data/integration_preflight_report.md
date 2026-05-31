# Integration Preflight Report

Target plan: `data/integration_plan.md`

Status: manuscript sections were inspected but not modified.

## Executive Summary

The integration plan is not ready to apply as written. Only three of the ten proposed papers are currently present in `data/papers.csv` with valid BibTeX keys and corresponding note files:

- iVideoGPT
- Cosmos
- WorldScore

However, all three note files are placeholder notes with `UNKNOWN` fields and no extracted reliable claims. They are metadata-ready but not claim-ready for the detailed manuscript revisions proposed in the plan.

Seven proposed papers are missing from `data/papers.csv`, and therefore also lack valid BibTeX keys, BibTeX entries, and notes in the current workspace:

- V-JEPA 2
- LAPA
- Diffusion Forcing
- WorldModelBench
- VideoPhy-2
- Morpheus
- What-If World

No manuscript placeholder citations of the form `[cite ...]`, `[NEEDS SOURCE]`, or `[VERIFY]` were found in `manuscript/sections/*.tex`.

## Paper Readiness Matrix

| Proposed paper | In `data/papers.csv` | `bibtex_key` | Key in `bib/references.bib` | Note file | Integration status |
|---|---:|---|---:|---|---|
| iVideoGPT | yes, P062 | `wu2024ivideogpt` | yes | `notes/P062_wu2024ivideogpt.md` | Metadata-ready only; note is placeholder |
| V-JEPA 2 | no | missing | no | missing | Blocked |
| LAPA | no | missing | no | missing | Blocked |
| Cosmos | yes, P068 | `nvidia2025cosmos` | yes | `notes/P068_nvidia2025cosmos.md` | Metadata-ready only; note is placeholder |
| Diffusion Forcing | no | missing | no | missing | Blocked |
| WorldModelBench | no | missing | no | missing | Blocked |
| VideoPhy-2 | no | missing | no | missing | Blocked |
| Morpheus | no | missing | no | missing | Blocked |
| WorldScore | yes, P078 | `duan2025worldscore` | yes | `notes/P078_duan2025worldscore.md` | Metadata-ready only; note is placeholder |
| What-If World | no | missing | no | missing | Blocked |

## Ready-to-Integrate Papers

No proposed paper is fully ready for detailed manuscript integration.

The following papers can only be used for very limited, metadata-level mentions because they exist in `data/papers.csv`, have BibTeX entries, and have note files:

- iVideoGPT: safe only as an indexed candidate bridge paper for interactive token world models, based on P062 metadata. Detailed claims about architecture, pretraining scale, datasets, transfer, or model-based RL are not supported by the current note.
- Cosmos: safe only as an indexed candidate Section 07 reference for world foundation model framing, based on P068 metadata. Detailed claims about model scales, open-weight release, robotics/autonomous-driving toolkits, or physical failures are not supported by the current note.
- WorldScore: safe only as an indexed candidate Section 08 addition for broader world-generation evaluation taxonomy, based on P078 metadata. Detailed claims about evaluation axes, tasks, findings, or model comparisons are not supported by the current note.

## Missing Papers

These proposed papers are absent from `data/papers.csv`:

- V-JEPA 2
- LAPA
- Diffusion Forcing
- WorldModelBench
- VideoPhy-2
- Morpheus
- What-If World

Because `data/papers.csv` is the single source of truth, no manuscript citation or substantive claim should be added for these papers until their metadata rows are added and verified.

## Missing BibTeX Keys

The following proposed papers have no valid `bibtex_key` in `data/papers.csv`:

- V-JEPA 2
- LAPA
- Diffusion Forcing
- WorldModelBench
- VideoPhy-2
- Morpheus
- What-If World

The three indexed papers have valid keys that are present in `bib/references.bib`:

- `wu2024ivideogpt`
- `nvidia2025cosmos`
- `duan2025worldscore`

## Missing Notes

The following proposed papers lack note files because they are not indexed:

- V-JEPA 2
- LAPA
- Diffusion Forcing
- WorldModelBench
- VideoPhy-2
- Morpheus
- What-If World

The following note files exist but are placeholders and do not currently support detailed manuscript claims:

- `notes/P062_wu2024ivideogpt.md`
- `notes/P068_nvidia2025cosmos.md`
- `notes/P078_duan2025worldscore.md`

Each contains a placeholder summary, many `UNKNOWN` fields, and an empty "Reliable claims extracted from this paper" section.

## Manuscript Placeholder Citation Check

Search scope: `manuscript/sections/*.tex`

No placeholder citations were found matching:

- `[cite ...]`
- `[CITE ...]`
- `[NEEDS SOURCE]`
- `[VERIFY]`

The integration plan itself contains many placeholder citations such as `[cite Diffusion Forcing]`, `[cite V-JEPA 2]`, `[cite both]`, and `[cite all]`. These are not present in the manuscript and should not be copied into manuscript sections.

## Unsafe Claims Requiring Verification

The following factual claims in `data/integration_plan.md` are not currently supported by completed notes or sufficiently detailed `data/papers.csv` entries.

### iVideoGPT

Unsafe until the P062 note is completed:

- iVideoGPT was published at NeurIPS 2024.
- It pre-trains on millions of human and robotic manipulation trajectories.
- It uses a novel compressive tokenization technique.
- It performs next-token prediction over observation-action-reward or multimodal sequences.
- It transfers to action-conditioned video prediction, visual planning, and model-based RL.
- Its transfer is strongest within visually similar domains.
- Discrete token dynamics achieve scalability and task generality beyond earlier recurrent formulations.

Current support: P062 metadata only says the paper connects tokenized video generation to interactive world modeling and is a candidate bridge paper for Sections 06 and 07.

### V-JEPA 2

All plan claims are unsafe because the paper is missing from `data/papers.csv`, BibTeX, and `notes/`.

Examples requiring verification:

- Trained on over one million hours of internet video.
- Uses a joint-embedding predictive architecture without pixel generation.
- V-JEPA 2-AC supports zero-shot pick-and-place planning on physical robot arms.
- Requires action-conditioned post-training to function as a planner.
- Provides the strongest recent evidence for non-generative latent prediction in control.
- Learns dense features that may implicitly capture object-like structure.

### LAPA

All plan claims are unsafe because the paper is missing from `data/papers.csv`, BibTeX, and `notes/`.

Examples requiring verification:

- Published at ICLR 2025.
- Learns discrete latent actions via VQ-VAE between image frames from internet-scale video.
- Pretrains a vision-language-action model without ground-truth action labels.
- Fine-tunes on small-scale robot data to map latent actions to physical actions.
- Outperforms action-labeled VLA models.
- Extends Genie to real robot manipulation.

### Cosmos

Unsafe until the P068 note is completed:

- Cosmos provides pre-trained diffusion and autoregressive video models at multiple scales.
- It includes fine-tuning toolkits for robotics and autonomous driving.
- It is released as an open-weight platform.
- It is the largest-scale industrial effort in the diffusion-video lineage.
- It provides evidence that visual realism, controllability, temporal consistency, and physical validity do not improve together.
- It exhibits systematic physical failures or poor physical benchmark performance.

Current support: P068 metadata only supports a cautious high-level mention as an industrial-scale world foundation model platform for physical AI.

### Diffusion Forcing

All plan claims are unsafe because the paper is missing from `data/papers.csv`, BibTeX, and `notes/`.

Examples requiring verification:

- Published at NeurIPS 2024.
- Trains diffusion models causally for next-token prediction.
- Uses independent per-token noise levels.
- Enables autoregressive video rollouts combining next-token flexibility with diffusion guidance.
- Rolls out beyond the training horizon without divergence.
- Improves decision-making or planning tasks.
- Serves as a technical foundation for follow-up interactive diffusion papers.

### WorldModelBench

All plan claims are unsafe because the paper is missing from `data/papers.csv`, BibTeX, and `notes/`.

Examples requiring verification:

- Published at NeurIPS 2025.
- Evaluates robotics and autonomous-driving video generation with instruction-following and physics-adherence criteria.
- Includes 67K crowd-sourced human labels for 14 frontier models.
- Fine-tunes a 2B-parameter judger.
- The judger outperforms GPT-4o by 8.6% on violation detection.
- Detects violations such as size changes breaching mass conservation.

### VideoPhy-2

All plan claims are unsafe because the paper is missing from `data/papers.csv`, BibTeX, and `notes/`.

Examples requiring verification:

- Extends VideoPhy to action-centric real-world activities.
- Reports 22% joint performance on a hard subset for the best model.
- Identifies conservation-law weaknesses such as mass and momentum.
- Introduces VideoPhy-AutoEval.

Note: the existing workspace contains VideoPhy, P037, with key `bansal2025_videophy_prov`; this is not VideoPhy-2.

### Morpheus

All plan claims are unsafe because the paper is missing from `data/papers.csv`, BibTeX, and `notes/`.

Examples requiring verification:

- Uses controlled laboratory recordings of falling balls, projectile motion, pendulums, and collisions.
- Uses zero-shot object segmentation, trajectory tracking, and PINN fitting.
- Tests conservation of energy, momentum, and acceleration.
- Evaluates six state-of-the-art models including Cosmos, CogVideoX, and Veo3.
- Shows systematic physical failures across all models.

### WorldScore

Unsafe until the P078 note is completed:

- Published at ICCV 2025.
- Unifies evaluation across 3D, 4D, and video generation.
- Decomposes world generation into next-scene generation tasks with camera-trajectory layout specifications.
- Evaluates controllability, quality, and dynamics.
- Shows that no single model family dominates across all axes.

Current support: P078 metadata only supports a cautious high-level mention as a candidate broader world-generation evaluation benchmark.

### What-If World

All plan claims are unsafe because the paper is missing from `data/papers.csv`, BibTeX, and `notes/`.

Examples requiring verification:

- It is a 2026 arXiv preprint.
- It is the first benchmark focused on counterfactual reasoning for general world models in embodied scenarios.
- It tests counterfactual action selection, physical outcome prediction under intervention, and causal structure discovery from video.

## Proposed Revisions Safe to Apply Now

Safe now, if manuscript edits are later requested:

- Do not apply the detailed sentence-level or paragraph-level revisions in the current integration plan.
- Optionally add a non-technical planning note outside the manuscript that iVideoGPT, Cosmos, and WorldScore are indexed candidates requiring completed notes before integration.
- Optionally update an internal to-do list to prioritize completing notes for the seven missing papers and expanding the three placeholder notes.

For manuscript sections, the only defensible content now would be very cautious, metadata-level citation-list additions for iVideoGPT, Cosmos, and WorldScore. Even those are not recommended yet because their notes explicitly say detailed reading is still required.

## Revisions Blocked by Missing Metadata, BibTeX, or Notes

Blocked completely:

- All V-JEPA 2 revisions.
- All LAPA revisions.
- All Diffusion Forcing revisions.
- All WorldModelBench revisions.
- All VideoPhy-2 revisions.
- All Morpheus revisions.
- All What-If World revisions.

Blocked pending completed notes:

- Detailed iVideoGPT Section 06/07 integration.
- Detailed Cosmos Section 07 integration.
- Detailed WorldScore Section 08 integration.

## Recommended Integration Order

1. Add and verify metadata for missing papers in `data/papers.csv`: V-JEPA 2, LAPA, Diffusion Forcing, WorldModelBench, VideoPhy-2, Morpheus, and What-If World.
2. Add verified BibTeX entries for those papers to `bib/references.bib`.
3. Create complete note files for all seven missing papers.
4. Replace placeholder notes for iVideoGPT, Cosmos, and WorldScore with detailed reading notes, including reliable extracted claims with section/page evidence.
5. Re-run `python scripts\validate_papers.py` and `python scripts\check_bibtex_keys.py`.
6. Integrate evaluation papers first only after notes are complete: WorldModelBench, VideoPhy-2, Morpheus, then WorldScore and What-If World. This order matches the survey's stated high-priority evidence gap around evaluation.
7. Integrate mechanism papers next: Diffusion Forcing, LAPA, Cosmos, then iVideoGPT and V-JEPA 2. This order avoids adding detailed method claims before the evaluation backbone and metadata are reliable.
8. Only after the above, revise manuscript Sections 06, 07, and 08 using verified citation keys from `bib/references.bib`.

## Bottom Line

The integration plan is useful as a roadmap, but it currently contains many unsupported factual claims. Applying it directly would violate the repository rules against unsupported citations and unverified technical claims. The next safe action is metadata and note completion, not manuscript revision.
