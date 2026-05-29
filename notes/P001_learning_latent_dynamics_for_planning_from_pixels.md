# Learning Latent Dynamics for Planning from Pixels

## Metadata

- Paper ID: P001
- Title: Learning Latent Dynamics for Planning from Pixels
- Authors: Danijar Hafner et al.
- Citation key: hafner2019_planet_prov
- Year: 2019
- Venue: ICML
- arXiv ID: 1811.04551
- DOI: UNKNOWN
- URL: https://arxiv.org/abs/1811.04551
- Category: latent_world_models
- Status: core
- Source: data/first_pass_notes_report.md

## Metadata conflicts

None.

## One-sentence summary

PlaNet is a landmark latent world model because it shows that planning can be done directly in a compact learned latent state, avoiding image-space rollouts while still solving challenging visual control tasks. citeturn25view1turn1view0turn27view2

## Problem setting

PlaNet targets model-based control from pixels in partially observed, continuous-action environments where image-level planning is too expensive and brittle. This is important because it reframes world modeling around **latent transition learning plus online planning**, which becomes a major branch of later work. citeturn25view1turn1view0

## Core idea

The key contribution is the combination of **RSSM latent dynamics + latent-space MPC**, which made world-model planning from pixels substantially more sample efficient and computationally practical. citeturn25view1turn1view0turn27view3

## Method

### Representation of the world

Representation: **latent state** via RSSM. The state has deterministic and stochastic components, with an encoder / representation model, transition model, observation model, and reward model. The planner uses only latent states and predicted rewards, not decoded images. citeturn1view0

### Training objective

Training uses a variational objective with observation and reward reconstruction/prediction terms plus KL regularization, and introduces **latent overshooting** as a multi-step latent-space consistency objective. The appendix/result discussion notes that RSSM itself did not require latent overshooting in the final agent. citeturn1view0turn27view0

## Input and output

[TODO]

## Dynamics modeling

Temporal evolution is modeled by a **recurrent state-space model (RSSM)** that combines deterministic memory and stochastic latent variables. Rollouts in latent space are used inside a CEM planner with online replanning (MPC). citeturn1view0turn27view2

## Physical consistency / physical prior

[TODO]

## Interaction or controllability

The world model is conditioned on **actions** and trained also to predict **rewards** from latent states. Planning is action-sequence search rather than a learned policy. citeturn1view0

## Dataset and benchmark

Tasks: six visual DeepMind Control Suite tasks including Cartpole Swing Up, Reacher Easy, Cheetah Run, Finger Spin, Cup Catch, and Walker Walk. Metrics: episodic return versus number of collected episodes; comparisons to A3C, D4PG, and planning with the true simulator. citeturn27view1turn27view3

## Main results

[TODO]

## Strengths

[TODO]

## Limitations

PlaNet depends on online planning, which is slower at action time than policy amortization. Long-horizon behavior still depends on finite-horizon CEM search, and the method is specialized to continuous-control settings with hand-designed reward signals rather than open-ended video simulation. citeturn27view2turn27view3

## Relation to this survey

### Relation to the survey taxonomy

Roles: **latent world model for planning; embodied world model**.

### Comparison with nearby papers

Compared with **P003**, PlaNet replaces VAE+MDN modularity with a more principled RSSM and explicit latent-space MPC. Compared with **P002**, PlaNet still plans online instead of learning a latent-space actor-critic policy. Compared with **P004–P006**, it moves decisively away from pixel-space rollout evaluation. citeturn8view0turn26view0turn16view0turn15view0turn11view0

### Open questions raised by this paper

- When should world models prefer **online planning** versus **amortized policy learning**?
- How can latent models preserve control-critical visual detail without decoding every step?
- What is the right evaluation for latent simulators beyond reward curves?

## Possible citation usage

This paper can be cited when discussing:

- Use when motivating world models that separate planning from pixel generation.
- Use when discussing latent-state design for world models.
- Use when surveying data efficiency gains from latent model-based control.

## Reliable claims extracted from this paper

- Claim: PlaNet plans in latent space rather than image space.  
  - Evidence from the paper: The abstract and Sec. 2 state that PlaNet chooses actions via fast online planning in latent space, with rewards predicted from latent states. citeturn25view1turn1view0
  - Source location if available: Abstract; Sec. 2.
  - Suggested citation usage: Use when motivating world models that separate planning from pixel generation.
  - Confidence: high

- Claim: The RSSM’s combination of deterministic and stochastic transitions is important for performance.  
  - Evidence from the paper: Sec. 3 and experimental analysis report that both components are crucial; the stochastic component is especially important. citeturn1view0turn27view3
  - Source location if available: Sec. 3; Sec. 5.
  - Suggested citation usage: Use when discussing latent-state design for world models.
  - Confidence: high

- Claim: PlaNet is markedly more data-efficient than pixel-based D4PG on the tested control tasks.  
  - Evidence from the paper: Table 1 reports PlaNet on 1,000 episodes versus D4PG on 100,000, along with large estimated data-efficiency gains. citeturn27view3
  - Source location if available: Sec. 5; Table 1.
  - Suggested citation usage: Use when surveying data efficiency gains from latent model-based control.
  - Confidence: high

## TODO

- TODO: read abstract
- TODO: read introduction
- TODO: extract method
- TODO: extract evaluation
- TODO: extract limitations
- TODO: decide citation usage
