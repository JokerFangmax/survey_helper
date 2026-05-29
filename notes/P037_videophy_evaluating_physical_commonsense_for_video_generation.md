# VideoPhy: Evaluating Physical Commonsense for Video Generation

## Metadata

- Paper ID: P037
- Title: VideoPhy: Evaluating Physical Commonsense for Video Generation
- Authors: Hritik Bansal et al.
- Citation key: bansal2025_videophy_prov
- Year: 2025
- Venue: ICLR
- arXiv ID: 2406.03520
- DOI: UNKNOWN
- URL: https://arxiv.org/abs/2406.03520
- Category: evaluation_benchmarks
- Status: core
- Source: data/first_pass_notes_report.md

## Metadata conflicts

None.

## One-sentence summary

VideoPhy is a benchmark paper that redirects the field away from visual impressiveness alone and toward **physical commonsense evaluation** for generative video and simulation models. citeturn5view1turn35view0

## Problem setting

The paper asks whether current text-to-video models actually obey semantic prompts and physical commonsense, rather than merely producing visually plausible videos. This is directly relevant to world-model surveys because high-fidelity video generation is often mistaken for accurate world simulation. citeturn5view1

## Core idea

The paper’s main contribution is to make **physical-law evaluation explicit and measurable** for video generation, exposing a major gap between visual quality and genuine world simulation. citeturn5view1turn35view0

## Method

### Representation of the world

Representation: **evaluation benchmark / prompt space**, not a learned world representation. The benchmark is organized around physical interaction captions spanning categories of material interactions and complexity. citeturn35view2

### Training objective

For the benchmark itself: none. For the automatic evaluator, the objective is to predict human judgments of **semantic adherence** and **physical commonsense**; the paper reports ROC-AUC comparisons against other evaluators, including GPT-4-Vision and Gemini-Pro-Vision-1.5. citeturn35view0

## Input and output

[TODO]

## Dynamics modeling

This paper does not propose a predictive dynamics model. Instead, it evaluates whether externally generated videos reflect physically sensible dynamics implied by prompts. It also introduces an automatic evaluator, VideoCon-Physics, to approximate human judgments. citeturn5view1turn35view0

## Physical consistency / physical prior

[TODO]

## Interaction or controllability

The evaluated generative systems are conditioned on **text prompts**. VideoPhy’s caption set spans solid-solid, solid-fluid, and fluid-fluid interactions and includes easy/hard difficulty subsets. citeturn5view1turn35view2

## Dataset and benchmark

The benchmark contains curated physical-interaction captions across 3 material-interaction categories, evaluates a range of open and closed text-to-video models, collects human annotations, and reports semantic-adherence and physical-commonsense judgments. The abstract states that the best model in their evaluation, CogVideoX-5B, satisfies caption + physical-law criteria on only 39.6% of instances. citeturn5view1turn35view2

## Main results

[TODO]

## Strengths

[TODO]

## Limitations

Benchmark quality depends on prompt design and human annotation protocols. The benchmark is about generated video, not embodied interaction or action-conditioned control, and physical commonsense judgments remain partly qualitative even with the proposed automatic evaluator. citeturn35view0turn35view2

## Relation to this survey

### Relation to the survey taxonomy

Roles: **evaluation benchmark; physical-law evaluation**.

### Comparison with nearby papers

Unlike **P004–P013**, VideoPhy is not a world model but an evaluation instrument. It is especially valuable when read beside **P012** and **P013**, because both show impressive generative ability but do not by themselves establish strong physical commonsense or physical-law compliance. citeturn31view3turn33view1turn5view1

### Open questions raised by this paper

- How should physical evaluation benchmarks include **interaction, control, and counterfactual rollout** rather than text-only generation?
- Can automatic evaluators reliably judge **causality and conservation-style physics**, not just surface plausibility?
- What benchmark suite best unifies **video quality, controllability, and physical correctness** for world models?

## Possible citation usage

This paper can be cited when discussing:

- Use when arguing that visual realism should not be equated with world-model correctness.
- Use when describing physical-law benchmark design.
- Use when discussing scalable evaluation of physical consistency in video generation.

## Reliable claims extracted from this paper

- Claim: Existing text-to-video models remain far from accurate physical simulation.  
  - Evidence from the paper: The abstract states that the best-performing model satisfies the caption and physical laws for only 39.6% of instances. citeturn5view1
  - Source location if available: Abstract.
  - Suggested citation usage: Use when arguing that visual realism should not be equated with world-model correctness.
  - Confidence: high

- Claim: VideoPhy organizes prompts around solid-solid, solid-fluid, and fluid-fluid interactions.  
  - Evidence from the paper: Dataset construction and statistics explicitly list these three categories. citeturn5view1turn35view2
  - Source location if available: Sec. 3 / Table 1.
  - Suggested citation usage: Use when describing physical-law benchmark design.
  - Confidence: high

- Claim: VideoCon-Physics is a stronger automatic evaluator than the compared multimodal baselines for this benchmark.  
  - Evidence from the paper: Table 4 reports ROC-AUC 82/73 for VideoCon-Physics versus lower values for GPT-4-Vision, Gemini-Pro-Vision-1.5, and VideoCon. citeturn35view0
  - Source location if available: Sec. 5.2; Table 4.
  - Suggested citation usage: Use when discussing scalable evaluation of physical consistency in video generation.
  - Confidence: high

## TODO

- TODO: read abstract
- TODO: read introduction
- TODO: extract method
- TODO: extract evaluation
- TODO: extract limitations
- TODO: decide citation usage
