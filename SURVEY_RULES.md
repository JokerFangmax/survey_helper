# Survey Rules

## Scope

This survey focuses on models that learn predictive world representations from videos, especially models related to generative simulation, physical dynamics, and future state prediction.

## In scope

- Video prediction
- Latent world models learned from video
- Diffusion-based video generation with temporal or physical structure
- Generative simulation environments
- Physical dynamics learning from visual data
- Embodied or interactive world models
- Evaluation protocols for predictive world models

## Out of scope

- Pure image generation without temporal prediction
- Pure language-only world models
- Classical physics simulators without learned visual prediction
- Robotics papers without a video/world-modeling component, unless directly relevant

## Citation policy

- No citation may be added unless the paper exists in `data/papers.csv` and `bib/references.bib`.
- If a paper is mentioned in the manuscript, it must have a corresponding BibTeX key.
- If Codex is unsure, it must insert `[VERIFY]`.

## Writing policy

- Survey should synthesize methods by concepts, not list papers one by one.
- Each section should answer:
  1. What problem is this line of work solving?
  2. What assumptions does it make?
  3. What kind of world model does it learn?
  4. How does it represent dynamics?
  5. What are its strengths?
  6. What are its limitations?
  7. How does it connect to later methods?