# Search Queries and Search Protocol

## Survey Title

Learning Predictive World Models from Videos: A Survey on Generative Simulation and Physical Dynamics

## Purpose

This file records the search process used to build and expand the literature pool. It is not the final paper list. The final structured paper database is stored in `data/papers.csv`, and citation entries are stored in `bib/references.bib`.

## Round 1: Initial Deep Research Search

- Date: 2026-05-29
- Tool: ChatGPT Deep Research
- Output file: `data/deep-research-report.md`
- Resulting files:
  - `data/papers.csv`
  - `bib/references.bib`

### Main search goal

Build an initial verified paper pool for a survey on predictive world models from videos, with emphasis on video prediction, latent world models, diffusion-based video generation, generative simulation, physical dynamics learning, embodied world models, and evaluation benchmarks.

### Keyword groups

#### Predictive world models from video

- predictive world model video
- learning world models from videos
- video world model
- visual world model
- latent world model video
- future prediction from video

#### Video prediction and dynamics

- video prediction physical dynamics
- future frame prediction dynamics
- long-horizon video prediction
- stochastic video prediction
- object-centric video prediction
- visual dynamics model

#### Generative simulation

- generative simulation world model
- neural simulator video
- learned simulator from video
- generative simulator physical dynamics
- simulation from video

#### Diffusion and generative video world models

- diffusion video prediction
- diffusion world model
- video diffusion physical consistency
- generative video model dynamics
- diffusion models for physical dynamics

#### Embodied and interactive world models

- embodied world model
- action-conditioned video prediction
- interactive world model
- robotics world model from video
- policy learning with video world models

#### Evaluation and benchmarks

- benchmark video world model
- physical reasoning benchmark video generation
- evaluation of video prediction models
- physical consistency video generation

### Inclusion criteria

Include a paper if it satisfies at least one of the following:

- It learns predictive dynamics from videos or visual observations.
- It models future states, future frames, or latent future trajectories.
- It proposes a world model with visual, physical, or interactive dynamics.
- It uses generative models to simulate dynamic environments.
- It evaluates physical consistency, temporal consistency, or controllability in generated videos.
- It is a foundational paper needed to explain the development of this area.

### Exclusion criteria

Exclude or mark as low priority if:

- The paper is only about static image generation.
- The paper is only about language models with no visual/video world modeling component.
- The paper is a classical physics simulator without a learned visual model.
- The paper is a pure robotics control paper without video prediction, visual dynamics, or world modeling.
- The paper is only about generic text-to-video generation and has no clear connection to prediction, dynamics, simulation, or physical consistency.

### Round 1 notes

- Initial pool size: 40 papers.
- Main categories discovered:
  - video prediction
  - latent world models
  - object-centric world models
  - physical dynamics
  - diffusion world models
  - interactive world models
  - evaluation benchmarks
- Next search should focus on:
  - recent embodied video world models
  - controllable video generation as simulation
  - physical consistency metrics
  - survey papers on video prediction and world models
  - missing SIGGRAPH / CoRL / RSS papers

## Round 2: Targeted Literature Expansion

- Date: 2026-05-30
- Tool: ChatGPT Deep Research / targeted literature expansion
- Output file: `data/targeted_literature_expansion_report.md`
- Ingestion action:
  - Append verified non-duplicate papers to `data/papers.csv`.
  - Append matching BibTeX entries to `bib/references.bib`.
  - Create placeholder notes from `templates/paper_note_template.md`.
  - Skip duplicates already represented in the existing database.

### Main search goal

Patch literature-coverage gaps identified by the reviewer-style audit and the major-revision backlog. The targeted search focused on under-covered families in Sections 04-08: recurrent and architecture-oriented video prediction, object-centric video representation and dynamics, modern latent/token/feature-space world models, interactive/generative world simulators, driving world models, and physical/world-generation evaluation benchmarks.

### Keyword groups

#### Video prediction / visual dynamics baselines

- ConvLSTM video prediction
- PredRNN spatiotemporal predictive learning
- PredRNN++ deep-in-time dilemma
- Memory In Memory spatiotemporal dynamics
- VideoGPT VQ-VAE Transformers

#### Object-centric / structured world models

- Slot Attention object-centric learning
- SAVi conditional object-centric learning from video
- SAVi++ real-world videos object-centric learning
- real-world object-centric video temporal feature similarities
- slot-based visual dynamics simulation

#### Latent / token / feature-space world models

- DreamerV3 mastering diverse domains world models
- interactive VideoGPT scalable world models
- token world models video interaction
- feature-space world models planning

#### Generative simulation / interactive world models

- Sora video generation models as world simulators
- UniSim learning interactive real-world simulators
- GAIA-1 generative world model autonomous driving
- DriveDreamer world models autonomous driving
- Cosmos world foundation model physical AI

#### Physical and world-generation evaluation

- WorldScore unified evaluation benchmark world generation
- physical-law evaluation video generation
- physical commonsense benchmark video generation
- world generation evaluation benchmark

### Inclusion criteria

Include a paper if it satisfies at least one of the following:

- It was explicitly requested by the reviewer audit as missing coverage.
- It fills a gap in architecture-oriented video prediction baselines.
- It extends object-centric learning from static or synthetic settings toward video or real-world video.
- It extends latent world models through diverse-domain training, tokenization, interactivity, robot learning, feature-space planning, or video pretraining.
- It proposes interactive or controllable video/world simulation.
- It provides evaluation protocols for physical consistency, causal reasoning, controllability, or broader world generation.

### Duplicate detection protocol

Before appending, compare each candidate against existing `data/papers.csv` and `bib/references.bib` by:

- normalized title,
- arXiv ID,
- URL,
- `bibtex_key`,
- and clear title/author equivalence when report titles differ slightly from existing rows.

### Round 2 ingestion notes

- Candidate report IDs considered: P041-P078.
- New papers appended: P041, P042, P043, P044, P049, P050, P051, P052, P054, P057, P062, P063, P064, P065, P066, P067, P068, P078.
- Duplicate candidates skipped because they already existed in the database:
  - P045 duplicates existing P025 (Eidetic 3D LSTM).
  - P046 duplicates existing P026 (SimVP).
  - P047 duplicates existing P023 (PhyDNet / Disentangling Physical Dynamics).
  - P048 duplicates existing P020 (MCVD).
  - P053 duplicates existing P017 (C-SWM).
  - P055 duplicates existing P018 (SlotFormer).
  - P056 duplicates existing P015 (DreamerV2).
  - P058 duplicates existing P014 (IRIS).
  - P059 duplicates existing P016 (DayDreamer).
  - P060 duplicates existing P010 (DINO-WM).
  - P061 duplicates existing P032 (Contextualized World Models).
  - P069 duplicates existing P021 (VideoWorld).
  - P070 duplicates existing P022 (Vid2World).
  - P071 duplicates existing P033 (PHYRE).
  - P072 duplicates existing P034 (CLEVRER).
  - P073 duplicates existing P035 (Physion).
  - P074 duplicates existing P037 (VideoPhy).
  - P075 duplicates existing P038 (PhyGenBench).
  - P076 duplicates existing P039 (How Far Is Video Generation from World Model).
  - P077 duplicates existing P040 (Physics-IQ).

### Round 2 caution

Placeholder notes created in this round are not evidence-ready reading notes. They should not be used to support technical manuscript claims until their `UNKNOWN` fields are replaced by verified evidence extracted from the corresponding paper.
