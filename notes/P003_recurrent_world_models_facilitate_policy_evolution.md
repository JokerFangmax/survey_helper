# Recurrent World Models Facilitate Policy Evolution

## Metadata

- Paper ID: P003
- Title: Recurrent World Models Facilitate Policy Evolution
- Authors: David Ha; Jürgen Schmidhuber
- Citation key: ha2018_world_models_prov
- Year: 2018
- Venue: NeurIPS
- arXiv ID: 1803.10122
- DOI: UNKNOWN
- URL: https://arxiv.org/abs/1803.10122
- Category: latent_world_models
- Status: core
- Source: data/first_pass_notes_report.md

## Metadata conflicts

[CONFLICT: report title metadata notes arXiv title `World Models`; CSV title retained as `Recurrent World Models Facilitate Policy Evolution`.]

## One-sentence summary

This paper crystallized the “world model” paradigm in RL by decomposing perception, memory, and control into VAE, MDN-RNN, and controller modules, and by showing that policies can even be trained inside a **hallucinated environment**. citeturn7view0turn8view0turn30view1

## Problem setting

The paper addresses how to learn a compact world model from high-dimensional observations and use it to train a very small controller efficiently. It matters because it made latent predictive modeling a central lens for model-based RL and simulation-based policy learning. citeturn8view0

## Core idea

The key contribution is conceptual: it popularized the idea that compact latent predictive models can be used not only for representation learning but as **simulators for downstream policy learning**. citeturn8view0turn30view1

## Method

### Representation of the world

Representation: **latent state**. A VAE compresses pixels into a latent vector *z*, an MDN-RNN predicts future latent dynamics and maintains memory *h*, and the controller acts from `[z, h]`. citeturn8view0

### Training objective

The VAE is trained for frame reconstruction; the MDN-RNN is trained as a probabilistic next-latent predictor; the controller is optimized separately with **CMA-ES** on task return. Training is modular rather than end-to-end. citeturn8view0turn29view3

## Input and output

[TODO]

## Dynamics modeling

Temporal evolution is modeled by an **MDN-RNN** that predicts a mixture-of-Gaussians distribution over next latent vectors, conditioned on previous latent, action, and recurrent hidden state. In the Doom experiment, the world model also predicts terminal/death-related information so it can serve as a stand-in environment. citeturn8view0turn30view0

## Physical consistency / physical prior

[TODO]

## Interaction or controllability

The world model is conditioned on **actions**. Rewards are not part of the unsupervised world-model training in CarRacing, but the controller is later optimized for task reward using CMA-ES; in Doom, the world model is used as a full simulated environment for policy evolution. citeturn29view0turn30view0

## Dataset and benchmark

Tasks: CarRacing-v0 and VizDoom Take Cover. Metrics: environment return / survival time. Reported results include CarRacing average score 906 for the full world model and Doom transfer performance around 1100 average survival steps on the real environment after training inside the dream. citeturn29view0turn30view1turn30view2

## Main results

[TODO]

## Strengths

[TODO]

## Limitations

The training is decoupled, the controller is tiny and evolved rather than gradient-trained through the model, and the VAE+MDN design is relatively weak compared with later RSSM-based approaches. The paper also emphasizes proof-of-concept more than standardized large-benchmark evaluation. citeturn8view0turn29view3

## Relation to this survey

### Relation to the survey taxonomy

Roles: **latent world model for planning; historical video prediction foundation; interactive world model**.

### Comparison with nearby papers

Compared with **P001** and **P002**, this is the looser, earlier VAE+RNN formulation before RSSM and latent overshooting / imagination actor-critic. Compared with **P004–P006**, it shifts decisively from pixel-space future-frame modeling to compact latent dynamics for control. citeturn26view1turn26view0turn16view0turn15view0turn11view0

### Open questions raised by this paper

- When does modular training of perception, dynamics, and controller underperform end-to-end latent world-model learning?
- How accurate must a dream environment be for **policy transfer** to remain reliable?
- How should uncertainty in latent dynamics be regularized so the controller cannot exploit simulator flaws?

## Possible citation usage

This paper can be cited when discussing:

- Use when presenting the historical emergence of latent world models in RL.
- Use when motivating generative simulation as a training substrate.
- Use when citing early empirical success of latent world models from pixels.

## Reliable claims extracted from this paper

- Claim: The world model is factorized into VAE, MDN-RNN, and controller modules.  
  - Evidence from the paper: Sec. 2 defines the V, M, and C components and their interactions. citeturn8view0
  - Source location if available: Sec. 2.
  - Suggested citation usage: Use when presenting the historical emergence of latent world models in RL.
  - Confidence: high

- Claim: Policies can be trained entirely inside a hallucinated environment and transferred back to the real one.  
  - Evidence from the paper: The abstract states this, and the VizDoom sections describe training inside the dream and evaluating in the actual environment. citeturn7view0turn30view0turn30view1
  - Source location if available: Abstract; Sec. 4.
  - Suggested citation usage: Use when motivating generative simulation as a training substrate.
  - Confidence: high

- Claim: The full world model solves CarRacing-v0 by exceeding the benchmark score of 900.  
  - Evidence from the paper: Table 1 reports a full-world-model average score of 906 and explains that solving CarRacing requires an average reward above 900. citeturn29view0
  - Source location if available: Sec. 3.3; Table 1.
  - Suggested citation usage: Use when citing early empirical success of latent world models from pixels.
  - Confidence: high

## TODO

- TODO: read abstract
- TODO: read introduction
- TODO: extract method
- TODO: extract evaluation
- TODO: extract limitations
- TODO: decide citation usage
