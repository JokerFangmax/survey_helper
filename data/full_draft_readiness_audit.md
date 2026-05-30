# Full Draft Readiness Audit

Generated for Stage 8 after reading `AGENTS.md`, `SURVEY_RULES.md`, `manuscript/main.tex`, all `manuscript/sections/*.tex`, `bib/references.bib`, `taxonomy.md`, `outline.md`, `data/papers.csv`, `data/claim_bank.md`, `data/claim_evidence_map.md`, and the existing `data/global_integration_check.md`.

## Executive Status

The manuscript has a coherent full-paper skeleton and a readable conceptual arc: abstract -> introduction -> background/scope -> taxonomy -> video prediction -> object-centric dynamics -> latent world models -> diffusion/interactive models -> evaluation/open challenges -> conclusion. It is stronger than the previous integration state because the abstract, introduction, and conclusion are now prose rather than scaffolds.

The draft is not submission-ready yet. The main blockers are unresolved evidence markers in manuscript prose, missing author/date metadata, incomplete figure/table assets promised by the outline, and several claims that are intentionally parked behind missing notes. No citation-key typo or obvious LaTeX reference break was found, so no manuscript fixes were made.

## 1. Required Parts Check

| Required part | Status | Evidence |
|---|---|---|
| Abstract | Present | `manuscript/main.tex` has a 193-word abstract. |
| Introduction | Present | `manuscript/sections/01_introduction.tex`. |
| Background | Present | `manuscript/sections/02_background.tex`. |
| Taxonomy | Present | `manuscript/sections/03_taxonomy.tex`. |
| Main body sections | Present | Sections 04--07 cover video prediction, object-centric dynamics, latent world models, and diffusion/interactive world models. |
| Evaluation/open challenges | Present | `manuscript/sections/08_evaluation_open_challenges.tex`. |
| Conclusion | Present | `manuscript/sections/09_conclusion.tex`. |
| Bibliography | Present | `\bibliography{../bib/references}` in `manuscript/main.tex`; `bib/references.bib` exists. |

Remaining structural issue: `\author{TODO}` and `\date{TODO}` are still present in `manuscript/main.tex`.

## 2. Unresolved Marker Check

Marker inventory in manuscript files:

| Marker | Count | Notes |
|---|---:|---|
| `[NEEDS SOURCE]` | 18 | 13 in manuscript prose, 5 in comment audit blocks. |
| `[VERIFY]` | 0 | None found. |
| `[TODO]` | 0 | None found as bracketed marker. |
| `[NEEDS MORE EVIDENCE]` | 0 | None found in manuscript files. |
| Raw `TODO` | 7 | `author`, `date`, and `% - Revision TODOs:` comment headings. |

Important prose-level `[NEEDS SOURCE]` locations:

- `01_introduction.tex`: broad modern diffusion/benchmark/latent-control coverage remains evidence-limited.
- `04_video_prediction.tex`: P020 and P023--P028 are not evidence-ready for detailed video-prediction claims.
- `05_object_centric_physical_dynamics.tex`: P017--P019 and P029--P031 need notes before stronger object-centric claims.
- `06_latent_world_models.tex`: P010, P014--P016, and P032 need notes before modern latent-control claims.
- `07_diffusion_interactive_world_models.tex`: P011, P020--P022, and diffusion physical-law claims remain weakly supported.
- `08_evaluation_open_challenges.tex`: detailed benchmark claims for P033--P036 and P038--P040 remain incomplete; long-horizon physical evaluation, exact metric-suite design, and broad sim-to-real reliability remain unsupported.

## 3. Citation-Key Validity

All citation keys used in `manuscript/main.tex` and `manuscript/sections/*.tex` are present in `bib/references.bib`.

All cited keys are also present in `data/papers.csv`.

Unique citation keys used in the manuscript: 23.

No obvious citation-key typos or citation syntax problems were found. No citation fixes were made.

## 4. Paper-List-Driven Risk

Overall risk: medium.

The manuscript is mostly synthesis-driven. Sections generally ask what role a model family plays, what representation or dynamics it uses, and how it is evaluated. This fits the project rules.

More paper-list-driven areas:

- Section 03 taxonomy has several family paragraphs that list representative papers, but this is mostly acceptable because the taxonomy table and axes provide synthesis.
- Section 07 has inventory-style paragraphs for Video Diffusion Models, MCVD, VideoWorld, and Vid2World. This is acceptable as an evidence-gap placeholder, but it should become more synthetic after notes are completed.
- Section 08 has benchmark inventory paragraphs for FVD, PHYRE, CLEVRER, Physion, PhyGenBench, Physical Law Perspective, and Physics-IQ. This is necessary for now, but a final version should compare benchmark purposes, inputs, metrics, and limitations rather than mainly naming them.

Recommendation: after completing missing notes, convert candidate-paper inventory paragraphs into comparison tables or axis-based synthesis paragraphs.

## 5. Taxonomy Consistency

Mostly consistent taxonomy axes:

- Modeling goal
- Representation
- Dynamics
- Conditioning / interaction
- Evaluation

The axes are introduced in the abstract, introduction, background, and taxonomy section, then reused throughout Sections 04--08.

Main inconsistency:

- `02_background.tex` says "This survey distinguishes six conceptual families," while `03_taxonomy.tex` defines seven families: action-conditioned pixel/motion prediction, stochastic future modeling, object-centric dynamics, latent planning/control, diffusion world models, interactive environments, and evaluation/benchmarks. This is a small but concrete consistency issue.

Structural mismatch with `outline.md`:

- `outline.md` separates diffusion-based/image-space world models, interactive/embodied environments, evaluation, open challenges, and conclusion into distinct later sections.
- The current manuscript combines diffusion and interactive world models in Section 07, and combines evaluation and open challenges in Section 08.
- This is workable, but the outline should be synchronized or the manuscript should be expanded to match the outline.

## 6. Section Transitions

Overall transition quality: good.

Strong transitions:

- Section 02 -> 03: background introduces the organizing axes, then taxonomy formalizes them.
- Section 03 -> 04: taxonomy prepares video prediction as the first modeling family.
- Section 04 -> 05: pixel-level limits motivate object/entity structure.
- Section 05 -> 06: explicit physical decomposition motivates compact latent state.
- Section 06 -> 07: abstraction-fidelity trade-off motivates image-space diffusion and interaction.
- Section 07 -> 08: diffusion/interactive limitations motivate multi-axis evaluation.
- Section 08 -> 09: conclusion synthesizes the evaluation problem and conceptual arc.

Minor transition issue:

- The introduction refers to "The background section" rather than a numbered `Section~\ref{...}` because Section 02 has no label. This avoids a broken reference, but adding `\label{sec:background}` later would improve consistency.

## 7. Repetition Check

Repeated themes are intentional but currently somewhat heavy:

- "Visual realism is not world-model correctness" appears in the abstract, introduction, background, taxonomy, diffusion/interactive section, evaluation section, and conclusion.
- "Frame metrics do not establish control utility or physical correctness" appears in background, taxonomy, video prediction, evaluation, and introduction.
- "Abstraction-fidelity trade-off" appears in introduction, latent section, diffusion section, evaluation section, and conclusion.

This repetition is not fatal because these are core survey messages. However, the final manuscript would benefit from pruning repeated full explanations after the taxonomy section. Later sections can refer back to the established distinction instead of restating it in full.

## 8. Introduction Preview Accuracy

The introduction accurately previews the current manuscript:

- It motivates predictive world models from video.
- It distinguishes world modeling from generic video generation.
- It states the realism/usefulness/physics/interaction tension.
- It defines scope and taxonomy axes.
- It previews the current section order, including combined diffusion/interactive Section 07 and evaluation/open-challenges Section 08.

Potential issue:

- The introduction marks broad modern diffusion-video, benchmark, and latent-control claims as `[NEEDS SOURCE]`. This is evidence-honest but not submission-ready.

## 9. Conclusion Claim Check

The conclusion does not introduce major new papers or citations.

The conclusion does not appear to introduce unsupported new claims beyond the manuscript's established synthesis. Its final statement that future work should jointly test prediction, interaction, long-horizon consistency, and physical validity is consistent with Section 08.

Minor caution:

- The phrase "Current evidence suggests that progress along one axis does not guarantee progress along the others" is supported by the manuscript's evaluation argument, but it is broad. It is acceptable in a conclusion, but could be softened further if the paper remains evidence-limited.

## 10. Missing Figures and Tables

Current manuscript assets:

- One table only: `tab:taxonomy_branches` in Section 03.
- No figures found.

High-value missing figures/tables:

1. Figure 1: survey landscape from pixel video prediction to structured dynamics, latent control, diffusion/interactive simulation, and evaluation.
2. Table 2 or expanded taxonomy table: branch-by-branch comparison with goal, representation, dynamics, conditioning, evaluation, evidence-ready papers, and evidence gaps.
3. Figure/Table for action-conditioned versus passive video prediction.
4. Table for video prediction evaluation signals: frame metrics, sampled futures, planning/control utility.
5. Figure for object-centric dynamics pipeline: pixels -> objects/relations -> rollout/planning/rendering.
6. Figure for latent world-model control loop: encoder, recurrent dynamics, reward/value, planner/actor.
7. Table for latent world-model variants: online planning, latent imagination, hallucinated policy training, evidence gaps.
8. Table for diffusion versus latent world-model trade-offs: fidelity, compute, controllability, physical evaluation.
9. Figure or table for known actions versus latent actions in interactive world models.
10. Evaluation matrix crossing visual fidelity, control utility, physical consistency, causal/counterfactual validity, and long-horizon robustness.
11. Table of open challenges mapped to taxonomy axes and missing notes.

Minimum recommended before submission: Figure 1, expanded taxonomy table, diffusion/latent trade-off table, and evaluation matrix.

## Additional LaTeX / Readiness Notes

- No missing `\ref{...}` targets were found.
- Label count: 8. Reference count: 6. Missing references: none.
- `\toprule`, `\midrule`, and `\bottomrule` are supported because `booktabs` is loaded.
- `main.tex` loads `hyperref`, but no package for graphics is loaded. Add `graphicx` later if figures are introduced.
- The manuscript contains in-file claim-evidence audits as LaTeX comments. These are useful during drafting but should probably be removed or moved to `data/` before submission.

## Blocking Issues

1. Unresolved prose-level `[NEEDS SOURCE]` markers remain across Sections 01, 04, 05, 06, 07, and 08.
2. `\author{TODO}` and `\date{TODO}` remain in `manuscript/main.tex`.
3. Several major coverage areas are still evidence-limited: diffusion-video lineage, modern latent/control variants, interactive diffusion/world models, object-centric extensions, and physical/counterfactual benchmark comparisons.
4. No figures exist, and only one table exists, despite the survey relying heavily on taxonomy and comparison.

## Important But Non-Blocking Issues

1. `02_background.tex` says six conceptual families, while the taxonomy section uses seven.
2. `outline.md` no longer matches the current manuscript organization after Section 07.
3. Repetition of the visual-realism-versus-world-model-validity message is useful but currently heavy.
4. Section 07 and Section 08 contain candidate-paper and benchmark inventory paragraphs that should become more synthetic after notes are complete.
5. Core terms such as `visual realism`, `visual plausibility`, `physical consistency`, `physical commonsense`, and `physical-law validity` are mostly clear but could be defined more explicitly.
6. Claim-evidence audit comments remain embedded in manuscript `.tex` files.

## Recommended Next Revision Order

1. Resolve metadata: replace `\author{TODO}` and `\date{TODO}`.
2. Complete or explicitly defer the notes behind prose-level `[NEEDS SOURCE]` markers, prioritizing P033--P040, P011/P020--P022, P010/P014--P016/P032, then P017--P019/P029--P031.
3. Fix taxonomy consistency: change the six-family statement or align Section 03 with it; synchronize `outline.md` with the actual manuscript structure.
4. Convert inventory paragraphs in Sections 07 and 08 into axis-based synthesis once missing notes are ready.
5. Add minimum visual assets: Figure 1, expanded taxonomy table, diffusion/latent trade-off table, and evaluation matrix.
6. Reduce repeated explanations of the same evaluation principle after the taxonomy section.
7. Move or remove manuscript-internal claim-evidence audit comments before submission.
8. Run a LaTeX build after figures/tables are added.

