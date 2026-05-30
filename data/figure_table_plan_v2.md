# Figure and Table Plan v2

Source basis: `data/reviewer_content_audit.md`, `manuscript/sections/*.tex`, `taxonomy.md`, `data/papers.csv`, `data/claim_bank.md`, and `data/claim_evidence_map.md`.

Scope: this is a planning artifact only. It does not rewrite manuscript prose and does not introduce new technical claims beyond the existing audit, taxonomy, paper metadata, and claim-evidence inventory.

Reviewer motivation: the content audit explicitly asks for stronger visual/table structure, especially a boundary diagram, taxonomy map, formal taxonomy matrix, evaluation protocol comparison, abstraction-fidelity trade-off figure, and benchmark/dataset landscape. The plan below turns those requests into concrete manuscript assets with data requirements and generation routes.

## Overview

| ID | Asset | Target section | Format | Priority | Generated from `papers.csv`? |
|---|---|---|---|---|---|
| F1 | Conceptual boundary diagram | Section 1 or Section 2 | TikZ | must-have | Partially |
| F2 | Taxonomy map | Section 3 | Python figure | must-have | Partially |
| T1 | Formal taxonomy matrix | Section 3 | LaTeX table | must-have | Yes, with manual grouping |
| T2 | Evaluation protocol comparison | Section 8 | LaTeX table | must-have | Partially |
| F3 | Abstraction-fidelity trade-off | Section 6 or Section 7 | Python figure | must-have | Partially |
| T3 | Benchmark / dataset landscape | Section 8 | LaTeX table | must-have | Yes, with manual curation |

## F1: Conceptual Boundary Diagram

- Purpose: Clarify the survey boundary between video prediction, video generation, predictive world models, interactive simulators, and physical simulator-like world models. This should answer the reviewer concern that the manuscript needs a crisp decision aid for what counts as a world model and what does not.
- Target section: Section 1, after the scope paragraph, or Section 2, after "World Models Beyond Future Frames".
- Exact caption draft: `Conceptual boundary between video generation, video prediction, predictive world models, interactive simulators, and physical simulator-like world models. The diagram emphasizes that visual plausibility alone is insufficient: world-model relevance increases when rollouts are conditioned on state history, actions or latent controls, planning utility, controllability, and physical or causal evaluation.`
- Required paper categories: `video_prediction`, `latent_world_models`, `object_centric_world_models`, `diffusion_world_models`, `interactive_world_models`, `generative_simulation`, `evaluation_benchmarks`.
- Required data fields: `id`, `title`, `category`, `sub_category`, `task`, `input_modality`, `output_modality`, `interaction`, `physical_prior`, `benchmark`, `metrics`, `relevance_to_survey`, `status`.
- Can be generated from `papers.csv`: Partially. The paper categories and representative examples can be pulled from `papers.csv`, but the inclusion/overlap relations are conceptual and should be manually specified to avoid pretending the CSV alone defines the boundary.
- Recommended format: TikZ. The boundary logic is conceptual and benefits from nested or overlapping regions plus small labels for criteria such as `action conditioning`, `planning utility`, `controllability`, and `physical consistency`.
- Priority: must-have.
- Notes for generation: Use method families rather than internal IDs in the figure labels. Example labels should be paper names or families, e.g., "Action-conditioned video prediction", "Dreamer/PlaNet-style latent models", "DIAMOND-style image-space world models", "Genie-style latent-action environments", and "VideoPhy-style physical evaluation".

## F2: Taxonomy Map

- Purpose: Provide a visual map of the survey taxonomy so reviewers can see how families differ by representation abstraction and interaction/control level. This addresses the audit's concern that the taxonomy currently reads like a generic organizing framework rather than a distinctive survey contribution.
- Target section: Section 3, immediately after the taxonomy axes are introduced and before the conceptual family paragraphs.
- Exact caption draft: `Taxonomy map of video-based predictive world models. The horizontal axis orders representations from image-space rollouts to tokens, features, latent states, and object or graph abstractions; the vertical axis orders conditioning from passive prediction to action-conditioned rollout, policy or planning use, latent-action interaction, and physical or counterfactual evaluation. Representative families are placed by their dominant design commitments rather than as disjoint categories.`
- Required paper categories: `video_prediction`, `object_centric_world_models`, `latent_world_models`, `diffusion_world_models`, `interactive_world_models`, `evaluation_benchmarks`.
- Required data fields: `id`, `title`, `bibtex_key`, `category`, `sub_category`, `model_family`, `dynamics_modeling`, `physical_prior`, `interaction`, `benchmark`, `metrics`, `key_contribution`, `status`.
- Can be generated from `papers.csv`: Partially. Categories, interaction labels, and representative papers can be extracted automatically. Axis coordinates should be assigned through a small manual mapping file because `papers.csv` does not currently contain numeric abstraction/control coordinates.
- Recommended format: Python figure. Use a scatter or bubble map with manual coordinates, color by family, and marker shape by evidence status (`core`, `background`, `candidate`). This will be easier to tune than TikZ as the paper pool expands.
- Priority: must-have.
- Notes for generation: Avoid clutter by plotting families first and listing 1-3 representative papers per cluster. Candidate-only papers should be visually lighter or annotated as "emerging examples" if included.

## T1: Formal Taxonomy Matrix

- Purpose: Replace or upgrade the current Section 3 taxonomy table into a formal matrix that compares families across the same dimensions. This directly responds to the audit request that Table 1 should not look like an internal work table and should use method families and formal paper names rather than local IDs.
- Target section: Section 3, replacing the current `tab:taxonomy_branches` table or appearing as the main table after F2.
- Exact caption draft: `Formal taxonomy matrix for predictive world models from video. Rows correspond to non-exclusive method families, and columns compare modeling goal, representation, transition mechanism, conditioning signal, evaluation protocol, representative papers, and main limitations.`
- Required paper categories: `video_prediction`, `object_centric_world_models`, `latent_world_models`, `diffusion_world_models`, `interactive_world_models`, `evaluation_benchmarks`, plus `physical_dynamics` and `generative_simulation` where they provide bridge examples.
- Required data fields: `category`, `sub_category`, `task`, `input_modality`, `output_modality`, `model_family`, `dynamics_modeling`, `physical_prior`, `interaction`, `benchmark`, `dataset`, `metrics`, `key_contribution`, `main_limitation`, `bibtex_key`, `status`.
- Can be generated from `papers.csv`: Yes, with manual grouping. The CSV contains most table fields, but final row labels and representative-paper selection should be curated to avoid overloading the table with every paper.
- Recommended format: LaTeX table. Use `booktabs`, compressed text, and a `tabularx` or `p{}` column layout. If the table becomes too wide, use a rotated page or move a fuller version to appendix later.
- Priority: must-have.
- Notes for generation: Candidate representative papers should only be used as examples, not as evidence for strong comparative claims unless notes are complete. Citations should use BibTeX keys from `papers.csv`, not local paper IDs.

## T2: Evaluation Protocol Comparison

- Purpose: Make evaluation mismatches explicit: frame metrics, FVD-like video quality, control return, planning success, controllability, physical consistency, causal/counterfactual reasoning, and long-horizon consistency test different properties. This responds to the audit's strongest evaluation recommendation.
- Target section: Section 8, after "Why Visual Fidelity Is Not Enough" or at the beginning of Section 8 as the organizing table for the evaluation discussion.
- Exact caption draft: `Comparison of evaluation protocols for video-based world models. Each protocol tests a different property of a learned model; visual quality, prediction fidelity, control utility, controllability, physical consistency, and causal validity should therefore be reported as complementary rather than interchangeable evidence of world-model validity.`
- Required paper categories: `evaluation_benchmarks`, `video_prediction`, `latent_world_models`, `object_centric_world_models`, `diffusion_world_models`, `interactive_world_models`.
- Required data fields: `category`, `task`, `benchmark`, `dataset`, `metrics`, `interaction`, `physical_prior`, `key_contribution`, `main_limitation`, `bibtex_key`, `status`.
- Can be generated from `papers.csv`: Partially. The table can draw metric and benchmark examples from `papers.csv`, but the "what it tests" and "what it misses" columns require manual synthesis from `claim_bank.md` and `claim_evidence_map.md`.
- Recommended format: LaTeX table.
- Priority: must-have.
- Suggested columns: `Protocol`, `Typical metrics`, `What it tests`, `What it misses`, `Representative papers/benchmarks`, `Relevant survey sections`.
- Notes for generation: This table should explicitly separate `control return` from `physical validity`, and `video quality` from `world-model correctness`. It should cite benchmark papers and representative model papers, but avoid claiming benchmark outcomes unless supported by completed notes.

## F3: Abstraction-Fidelity Trade-Off

- Purpose: Visualize the manuscript's recurring synthesis point: compact latent or object states improve planning efficiency and interpretability, while image-space generative models can preserve visual details but may be expensive and hard to validate physically. This figure should reduce repeated prose across Sections 6-8.
- Target section: Section 6 near the transition to image-space world models, or Section 7 near the opening discussion of diffusion and interaction.
- Exact caption draft: `Abstraction-fidelity trade-off in video-based world models. Compact latent and object-centric states can improve planning efficiency, compositional structure, and interpretability, whereas image-space and diffusion-based rollouts can preserve visual detail but require stronger tests for controllability, long-horizon consistency, and physical validity.`
- Required paper categories: `latent_world_models`, `object_centric_world_models`, `physical_dynamics`, `diffusion_world_models`, `interactive_world_models`, `video_prediction`.
- Required data fields: `category`, `sub_category`, `model_family`, `dynamics_modeling`, `output_modality`, `physical_prior`, `interaction`, `metrics`, `key_contribution`, `main_limitation`, `status`.
- Can be generated from `papers.csv`: Partially. Paper families and example labels can be pulled automatically, but the conceptual trade-off axes should be manually mapped from taxonomy categories and claim evidence.
- Recommended format: Python figure. Use a 2D map or radar-style family comparison. A 2D figure is preferable for readability: x-axis = representation abstraction; y-axis = visual fidelity or image detail. Overlay annotations for planning efficiency, physical interpretability, controllability, and validation burden.
- Priority: must-have.
- Notes for generation: The figure should not imply a universal ranking. It should show design pressure and evaluation trade-offs, with cautious language such as "often", "tends to", and "requires validation".

## T3: Benchmark / Dataset Landscape

- Purpose: Organize benchmark and dataset coverage by what each benchmark tests: video prediction, robotic interaction, physical reasoning, text-to-video physical consistency, driving or embodied simulation, and interactive environments. This addresses the audit's concern that physical dynamics and benchmark evidence are underdeveloped.
- Target section: Section 8, after the physical/counterfactual evaluation subsection or as a companion to T2.
- Exact caption draft: `Benchmark and dataset landscape for evaluating predictive world models from video. Benchmarks differ in whether they test frame prediction, robotic interaction, control utility, physical reasoning, text-conditioned physical commonsense, driving simulation, interactive generation, or broader world generation.`
- Required paper categories: `evaluation_benchmarks`, `video_prediction`, `interactive_world_models`, `latent_world_models`, `object_centric_world_models`, `physical_dynamics`, `diffusion_world_models`.
- Required data fields: `title`, `category`, `sub_category`, `task`, `input_modality`, `output_modality`, `benchmark`, `dataset`, `metrics`, `physical_prior`, `interaction`, `main_limitation`, `bibtex_key`, `status`.
- Can be generated from `papers.csv`: Yes, with manual curation. `benchmark`, `dataset`, and `metrics` are present in `papers.csv`, but many newer rows contain `UNKNOWN`; those cells should remain blank, marked as "not specified in current metadata", or omitted until notes are completed.
- Recommended format: LaTeX table. Use grouped rows by evaluation target. A landscape table may be needed if included in the main manuscript.
- Priority: must-have.
- Suggested row groups: `video prediction datasets`, `robot interaction datasets`, `physical reasoning benchmarks`, `video generation quality metrics`, `T2V physical consistency benchmarks`, `driving/embodied world-model datasets`, `interactive game/world environments`, `world-generation benchmarks`.
- Notes for generation: This table should distinguish datasets used to train/evaluate models from benchmark papers that define evaluation protocols. It should avoid presenting `UNKNOWN` metadata as evidence.

## Optional Nice-to-Have Assets

### T4: Claim-to-Evidence Coverage Matrix

- Purpose: Summarize which claims in `claim_bank.md` have high, medium, or incomplete evidence and which method families they support.
- Target section: Appendix or internal revision guide.
- Exact caption draft: `Claim-evidence coverage matrix for the survey's major synthesis claims. Claims are grouped by theme and linked to supporting paper families, citation keys, confidence levels, and missing-evidence notes.`
- Required paper categories: all categories with completed notes.
- Required data fields: from `data/claim_bank.md` and `data/claim_evidence_map.md`, plus `bibtex_key` and `category` from `papers.csv`.
- Can be generated from `papers.csv`: No. It requires the claim-evidence files as primary input.
- Recommended format: LaTeX table or Markdown-to-LaTeX generated table.
- Priority: nice-to-have.

### F4: Revision Coverage Heatmap

- Purpose: Show which paper families are well supported by completed notes versus currently covered mainly by metadata/candidates.
- Target section: Internal planning only, not necessarily manuscript.
- Exact caption draft: `Coverage heatmap of paper families by evidence status. Darker cells indicate families with completed notes and claim-level support; lighter cells indicate metadata-only or candidate coverage requiring further reading before strong manuscript claims.`
- Required paper categories: all categories.
- Required data fields: `category`, `sub_category`, `status`, `notes_file`.
- Can be generated from `papers.csv`: Yes.
- Recommended format: Python figure.
- Priority: nice-to-have.

## Recommended Generation Order

1. T1: Formal taxonomy matrix. This creates the stable family labels and representative-paper choices that F2 and later text can reuse.
2. F1: Conceptual boundary diagram. This should be settled early because it defines the scope and prevents overclaiming about video generation as world modeling.
3. F2: Taxonomy map. Once T1 and F1 define family labels and boundaries, the map can visualize the distinctive survey structure.
4. T2: Evaluation protocol comparison. This anchors Section 8 and prevents conflating frame metrics, control return, and physical validity.
5. T3: Benchmark / dataset landscape. This should follow T2 so benchmark rows are grouped by evaluation property, not merely by dataset name.
6. F3: Abstraction-fidelity trade-off. This can be refined last because it synthesizes Sections 4-8 and should use the final family labels from T1/F2.

## Implementation Notes

- Do not use local paper IDs such as `P004` or `P037` in manuscript-facing figure/table labels. Use method families, formal paper names, or citation commands.
- Use `papers.csv` as the source of paper metadata, but do not treat metadata-only or candidate rows as completed evidence for strong claims.
- Use `claim_bank.md` and `claim_evidence_map.md` to decide which captions and table notes can make supported synthesis claims.
- Keep captions analytical rather than promotional. Preferred wording includes "illustrates", "organizes", "compares", "tests", and "distinguishes".
- Leave unknown metadata out of manuscript tables unless the absence itself is relevant; do not display `UNKNOWN` in final camera-ready tables.
