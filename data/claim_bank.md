# Survey Claim Bank

Source basis: completed note files under `notes/` whose source is `data/first_pass_notes_report.md`.

Completed-note coverage: P001, P002, P003, P004, P005, P006, P007, P008, P009, P012, P013, P037.

Constraint: this file is a claim inventory only. It is not manuscript prose.

## Theme 1: From video prediction to world modeling

### C001

- Claim text: Action-conditioned video prediction is an early bridge from passive future-frame prediction to world modeling because it predicts future observations conditioned on candidate actions. (narrow)
- Supporting papers: P004 (`oh2015_action_conditional_video_prediction_prov`)
- Evidence summary: The P004 note states that the paper is an early action-conditioned, long-horizon video prediction study for high-dimensional RL observations and that the model uses action-conditioned feature transformations.
- Survey section: Background: video prediction as a precursor to world models.
- Confidence: high
- Missing evidence: Additional completed notes on later action-conditioned video predictors would broaden this claim.
- Suggested citation command: `\cite{oh2015_action_conditional_video_prediction_prov}`

### C002

- Claim text: Pixel-motion prediction methods reframed video prediction from reconstructing future frames from scratch to transforming observed pixels, which is useful for physical interaction settings. (narrow)
- Supporting papers: P005 (`finn2016_physical_interaction_video_prediction_prov`)
- Evidence summary: The P005 note reports that the paper explicitly models pixel motion rather than reconstructing appearance from scratch, using transformation-based mechanisms such as DNA, CDNA, and STP.
- Survey section: Background: video prediction and physical interaction.
- Confidence: high
- Missing evidence: Broader support from other motion/content or transformation-based predictors is pending completed notes.
- Suggested citation command: `\cite{finn2016_physical_interaction_video_prediction_prov}`

### C003

- Claim text: Pixel prediction quality alone is not enough to evaluate world models; downstream control or planning utility can reveal usefulness that frame metrics miss.
- Supporting papers: P004 (`oh2015_action_conditional_video_prediction_prov`), P009 (`janner2019_o2p2_prov`), P012 (`alonso2024_diamond_prov`)
- Evidence summary: The P004 note states that frame prediction quality alone underestimates usefulness for control. The P009 note states that O2P2's learned representation supports downstream planning better than an object-agnostic video predictor baseline. The P012 note evaluates a diffusion world model through Atari control performance.
- Survey section: Evaluation: from frame fidelity to control utility.
- Confidence: high
- Missing evidence: More completed notes on benchmark metrics such as FVD, PHYRE, CLEVRER, and Physion would strengthen the evaluation framing.
- Suggested citation command: `\cite{oh2015_action_conditional_video_prediction_prov,janner2019_o2p2_prov,alonso2024_diamond_prov}`

## Theme 2: Stochasticity and uncertainty in future prediction

### C004

- Claim text: Stochastic latent variables are a central response to the multi-modal nature of future video prediction, where a single deterministic rollout can average over plausible futures. (narrow)
- Supporting papers: P006 (`babaeizadeh2018_sv2p_prov`)
- Evidence summary: The P006 note says SV2P is designed to generate different plausible futures from different latent samples and motivates stochastic prediction as a remedy for deterministic blurring under uncertainty.
- Survey section: Stochastic future prediction and uncertainty.
- Confidence: high
- Missing evidence: Additional completed notes on SVG-LP and other stochastic video generation papers are needed for a broader comparison.
- Suggested citation command: `\cite{babaeizadeh2018_sv2p_prov}`

### C005

- Claim text: Stochastic video models can require special training procedures because naive end-to-end optimization may ignore latent variables. (narrow)
- Supporting papers: P006 (`babaeizadeh2018_sv2p_prov`)
- Evidence summary: The P006 note reports a variational lower bound and a three-phase training scheme introduced because naive training tends to ignore the latents.
- Survey section: Stochastic future prediction: modeling and optimization issues.
- Confidence: high
- Missing evidence: UNKNOWN
- Suggested citation command: `\cite{babaeizadeh2018_sv2p_prov}`

### C006

- Claim text: The temporal structure of stochastic latents matters: time-varying latents can improve long-horizon stability, while time-invariant latents may better capture persistent factors. (narrow)
- Supporting papers: P006 (`babaeizadeh2018_sv2p_prov`)
- Evidence summary: The P006 note states that time-varying latents help long-horizon stability on some datasets, whereas time-invariant latents can work better when the key latent factor persists over the whole video.
- Survey section: Stochastic future prediction: latent design trade-offs.
- Confidence: high
- Missing evidence: The current support is one paper, so this should be treated as a design observation rather than a general law.
- Suggested citation command: `\cite{babaeizadeh2018_sv2p_prov}`

## Theme 3: Object-centric and structured physical dynamics

### C007

- Claim text: Object-centric and relational representations provide an important inductive bias for physical dynamics by explicitly modeling entities and their interactions.
- Supporting papers: P007 (`battaglia2016_interaction_networks_prov`), P008 (`watters2017_visual_interaction_networks_prov`), P009 (`janner2019_o2p2_prov`)
- Evidence summary: The P007 note states that Interaction Networks operate on objects and relations represented as a graph. The P008 note combines a CNN visual encoder with an interaction-network dynamics predictor. The P009 note describes joint perception, physics, and rendering around object-oriented prediction and planning.
- Survey section: Object-centric and structured physical dynamics.
- Confidence: high
- Missing evidence: Completed notes for OP3, CSWM, SlotFormer, and related papers would broaden the modern object-centric comparison.
- Suggested citation command: `\cite{battaglia2016_interaction_networks_prov,watters2017_visual_interaction_networks_prov,janner2019_o2p2_prov}`

### C008

- Claim text: Visual interaction models can connect raw visual perception to structured relational dynamics rather than choosing between pixels and states. (narrow)
- Supporting papers: P008 (`watters2017_visual_interaction_networks_prov`)
- Evidence summary: The P008 note reports that VIN combines a CNN-based visual encoder with an interaction-network dynamics predictor and outperforms pixel-to-state and state-to-state baselines on long rollout position error.
- Survey section: Object-centric and structured physical dynamics.
- Confidence: high
- Missing evidence: More completed notes are needed for later visual object-centric dynamics models.
- Suggested citation command: `\cite{watters2017_visual_interaction_networks_prov}`

### C009

- Claim text: Object-oriented learned representations can support planning better than object-agnostic video predictors in structured physical tasks. (narrow)
- Supporting papers: P009 (`janner2019_o2p2_prov`)
- Evidence summary: The P009 note states that O2P2's learned representation supports downstream planning better than an object-agnostic video predictor baseline in the tower task.
- Survey section: Object-centric world models for planning.
- Confidence: high
- Missing evidence: This claim is narrow and task-specific until additional completed notes support it.
- Suggested citation command: `\cite{janner2019_o2p2_prov}`

### C010

- Claim text: Structured physical models can generalize beyond the exact training configuration and can sometimes infer hidden physical causes from visual effects.
- Supporting papers: P007 (`battaglia2016_interaction_networks_prov`), P008 (`watters2017_visual_interaction_networks_prov`)
- Evidence summary: The P007 note says Interaction Networks generalize to different numbers and configurations of objects. The P008 note says VIN can infer hidden physical causes such as invisible objects and unknown mass from visual effects.
- Survey section: Object-centric and structured physical dynamics: generalization.
- Confidence: medium
- Missing evidence: [NEEDS MORE EVIDENCE] The current evidence comes from controlled or synthetic settings; more realistic-video notes are needed.
- Suggested citation command: `\cite{battaglia2016_interaction_networks_prov,watters2017_visual_interaction_networks_prov}`

## Theme 4: Latent world models for planning and control

### C011

- Claim text: Latent world models shift world modeling from pixel-space rollout evaluation toward compact state dynamics that can be used for planning or policy learning.
- Supporting papers: P001 (`hafner2019_planet_prov`), P002 (`hafner2020_dreamer_prov`), P003 (`ha2018_world_models_prov`)
- Evidence summary: The P001 note states that PlaNet plans in latent space rather than image space. The P002 note states that Dreamer learns behavior through latent imagination. The P003 note describes a VAE, MDN-RNN, and controller pipeline for training policies inside a learned environment.
- Survey section: Latent world models for planning and control.
- Confidence: high
- Missing evidence: UNKNOWN
- Suggested citation command: `\cite{hafner2019_planet_prov,hafner2020_dreamer_prov,ha2018_world_models_prov}`

### C012

- Claim text: Recurrent latent-state models with deterministic and stochastic components are a recurring design for sample-efficient visual control.
- Supporting papers: P001 (`hafner2019_planet_prov`), P002 (`hafner2020_dreamer_prov`)
- Evidence summary: The P001 note reports that RSSM combines deterministic memory and stochastic latent variables and that both components are important for performance. The P002 note connects latent imagination to improved data efficiency and final performance on visual control tasks.
- Survey section: Latent dynamics architectures.
- Confidence: high
- Missing evidence: Completed notes on DreamerV2, IRIS, and related models would expand this claim.
- Suggested citation command: `\cite{hafner2019_planet_prov,hafner2020_dreamer_prov}`

### C013

- Claim text: Latent imagination can replace online planning with learned actor-critic behavior trained through imagined trajectories. (narrow)
- Supporting papers: P002 (`hafner2020_dreamer_prov`)
- Evidence summary: The P002 note states that Dreamer learns behavior purely through latent imagination and uses analytic gradients through imagined trajectories for policy learning.
- Survey section: Latent world models: planning versus amortized policy learning.
- Confidence: high
- Missing evidence: UNKNOWN
- Suggested citation command: `\cite{hafner2020_dreamer_prov}`

### C014

- Claim text: Policies can be optimized inside learned or hallucinated environments, but the fidelity of the learned simulator remains a central concern.
- Supporting papers: P003 (`ha2018_world_models_prov`), P001 (`hafner2019_planet_prov`), P012 (`alonso2024_diamond_prov`)
- Evidence summary: The P003 note says policies can be trained entirely inside a hallucinated environment and transferred back. The P001 note raises evaluation questions for latent simulators beyond reward curves. The P012 note raises open questions about physical correctness of diffusion world models beyond Atari return.
- Survey section: Latent world models: simulator fidelity and exploitation.
- Confidence: medium
- Missing evidence: [NEEDS MORE EVIDENCE] The simulator-fidelity risk is supported by note limitations and open questions, but needs more direct evidence from model exploitation or failure analyses.
- Suggested citation command: `\cite{ha2018_world_models_prov,hafner2019_planet_prov,alonso2024_diamond_prov}`

## Theme 5: Diffusion-based world models

### C015

- Claim text: Conditional diffusion can be used as an image-space world model for environment dynamics. (narrow)
- Supporting papers: P012 (`alonso2024_diamond_prov`)
- Evidence summary: The P012 note states that DIAMOND models environment dynamics directly with a conditional diffusion model in image space, generating next observations from observation-action history.
- Survey section: Diffusion-based world models.
- Confidence: high
- Missing evidence: Completed notes for video diffusion and MCVD are needed to connect DIAMOND to the broader diffusion-video lineage.
- Suggested citation command: `\cite{alonso2024_diamond_prov}`

### C016

- Claim text: Preserving image-space visual details can improve downstream RL performance, suggesting that aggressive perceptual compression may discard control-critical information. (narrow)
- Supporting papers: P012 (`alonso2024_diamond_prov`)
- Evidence summary: The P012 note says the paper argues that preserving visual details can improve RL performance and reports strong Atari 100k world-model results.
- Survey section: Diffusion-based world models: fidelity versus abstraction.
- Confidence: high
- Missing evidence: This claim is narrow because it is currently supported by one completed note, mainly in Atari.
- Suggested citation command: `\cite{alonso2024_diamond_prov}`

### C017

- Claim text: Diffusion world models currently leave open whether visual fidelity translates to physical correctness in realistic embodied domains. (narrow)
- Supporting papers: P012 (`alonso2024_diamond_prov`)
- Evidence summary: The P012 note lists limitations including Atari-centered evaluation, higher compute than many latent-state models, and open questions about long-horizon causal or physical correctness.
- Survey section: Diffusion-based world models: limitations and open problems.
- Confidence: medium
- Missing evidence: [NEEDS MORE EVIDENCE] Needs completed notes on physical-law benchmarks and diffusion-video papers beyond DIAMOND.
- Suggested citation command: `\cite{alonso2024_diamond_prov}`

## Theme 6: Interactive and embodied world models

### C018

- Claim text: Interactive generative environments can be learned from unlabeled video by inducing latent actions rather than relying on ground-truth action labels. (narrow)
- Supporting papers: P013 (`bruce2024_genie_prov`)
- Evidence summary: The P013 note states that Genie is trained from unlabeled video without ground-truth action labels and combines a spatiotemporal tokenizer, latent action model, and MaskGIT dynamics model.
- Survey section: Interactive and embodied world models.
- Confidence: high
- Missing evidence: Additional completed notes on video-only and interactive world models are needed for a broader claim.
- Suggested citation command: `\cite{bruce2024_genie_prov}`

### C019

- Claim text: Action-conditioned and interactive video models connect prediction to embodied use by making future video depend on interventions, policies, or latent controls.
- Supporting papers: P004 (`oh2015_action_conditional_video_prediction_prov`), P005 (`finn2016_physical_interaction_video_prediction_prov`), P013 (`bruce2024_genie_prov`)
- Evidence summary: The P004 note studies action-conditioned prediction in Atari. The P005 note studies robot pushing through action-conditioned physical-interaction video prediction. The P013 note uses latent actions to make generated environments controllable from unlabeled video.
- Survey section: Interactive and embodied world models: from actions to latent actions.
- Confidence: high
- Missing evidence: Completed notes on robot-specific world models and newer interactive diffusion models would broaden the embodied scope.
- Suggested citation command: `\cite{oh2015_action_conditional_video_prediction_prov,finn2016_physical_interaction_video_prediction_prov,bruce2024_genie_prov}`

### C020

- Claim text: Latent actions learned from video can support downstream imitation, but this evidence is currently narrow and benchmark-specific. (narrow)
- Supporting papers: P013 (`bruce2024_genie_prov`)
- Evidence summary: The P013 note states that latent actions learned from video can support downstream imitation, reaching oracle-level CoinRun performance with very few expert samples.
- Survey section: Interactive world models: controllability and downstream use.
- Confidence: high
- Missing evidence: This should be presented as narrow until supported by more domains and completed notes.
- Suggested citation command: `\cite{bruce2024_genie_prov}`

## Theme 7: Evaluation, physical consistency, and benchmarks

### C021

- Claim text: Visual realism should not be equated with world-model correctness, because generated videos can remain physically inconsistent.
- Supporting papers: P037 (`bansal2025_videophy_prov`), P012 (`alonso2024_diamond_prov`)
- Evidence summary: The P037 note reports that the best evaluated text-to-video model satisfied caption and physical-law criteria on only 39.6% of instances. The P012 note raises open questions about physical correctness beyond Atari return.
- Survey section: Evaluation: physical consistency versus visual fidelity.
- Confidence: high
- Missing evidence: More completed benchmark notes would help triangulate this point across evaluation suites.
- Suggested citation command: `\cite{bansal2025_videophy_prov,alonso2024_diamond_prov}`

### C022

- Claim text: Physical-consistency benchmarks can organize evaluation around material-interaction categories such as solid-solid, solid-fluid, and fluid-fluid interactions. (narrow)
- Supporting papers: P037 (`bansal2025_videophy_prov`)
- Evidence summary: The P037 note states that VideoPhy organizes prompts around solid-solid, solid-fluid, and fluid-fluid interactions and includes difficulty subsets.
- Survey section: Evaluation benchmarks for physical commonsense.
- Confidence: high
- Missing evidence: UNKNOWN
- Suggested citation command: `\cite{bansal2025_videophy_prov}`

### C023

- Claim text: Automatic evaluators can help scale physical-consistency evaluation, but they should be treated as approximations to human judgment rather than complete replacements. (narrow)
- Supporting papers: P037 (`bansal2025_videophy_prov`)
- Evidence summary: The P037 note states that VideoCon-Physics is a stronger automatic evaluator than compared multimodal baselines, while the limitations section says physical commonsense judgments remain partly qualitative.
- Survey section: Evaluation: automatic metrics and human verification.
- Confidence: medium
- Missing evidence: [NEEDS MORE EVIDENCE] Needs completed notes on additional automatic metrics and human-alignment studies.
- Suggested citation command: `\cite{bansal2025_videophy_prov}`

## Theme 8: Open challenges

### C024

- Claim text: A central open challenge is to evaluate world models beyond pixel fidelity and task return, including physical consistency, controllability, causal validity, and long-horizon behavior.
- Supporting papers: P004 (`oh2015_action_conditional_video_prediction_prov`), P012 (`alonso2024_diamond_prov`), P013 (`bruce2024_genie_prov`), P037 (`bansal2025_videophy_prov`)
- Evidence summary: The P004 note states that frame prediction quality alone can underestimate control usefulness. The P012 note asks how to evaluate diffusion world models for physical correctness beyond Atari return. The P013 note raises questions about controllability and open-ended interactive environments. The P037 note focuses on physical commonsense evaluation for video generation.
- Survey section: Open challenges: evaluation.
- Confidence: medium
- Missing evidence: [NEEDS MORE EVIDENCE] Needs completed notes on dedicated benchmarks such as FVD, PHYRE, CLEVRER, Physion, PhyGenBench, Physical Law Perspective, and Physics-IQ.
- Suggested citation command: `\cite{oh2015_action_conditional_video_prediction_prov,alonso2024_diamond_prov,bruce2024_genie_prov,bansal2025_videophy_prov}`

### C025

- Claim text: Another open challenge is to learn object structure, hidden variables, and interaction dynamics without direct supervision while preserving usefulness for planning or control.
- Supporting papers: P005 (`finn2016_physical_interaction_video_prediction_prov`), P007 (`battaglia2016_interaction_networks_prov`), P008 (`watters2017_visual_interaction_networks_prov`), P009 (`janner2019_o2p2_prov`), P013 (`bruce2024_genie_prov`)
- Evidence summary: The P005 note reports unsupervised object-like decompositions. The P007 and P008 notes support object-relational dynamics and hidden physical-cause inference. The P009 note reports joint object-oriented perception, physics, rendering, and planning. The P013 note learns latent actions from unlabeled video.
- Survey section: Open challenges: abstraction, structure, and controllability.
- Confidence: medium
- Missing evidence: [NEEDS MORE EVIDENCE] The current support spans related but not identical forms of unsupervised structure learning; further completed notes are needed for a tighter taxonomy.
- Suggested citation command: `\cite{finn2016_physical_interaction_video_prediction_prov,battaglia2016_interaction_networks_prov,watters2017_visual_interaction_networks_prov,janner2019_o2p2_prov,bruce2024_genie_prov}`

### C026

- Claim text: World models face a persistent abstraction-fidelity trade-off: compact latent states enable planning efficiency, while image-space generative models may preserve details that matter for control.
- Supporting papers: P001 (`hafner2019_planet_prov`), P002 (`hafner2020_dreamer_prov`), P012 (`alonso2024_diamond_prov`)
- Evidence summary: The P001 note shows latent-space planning without image rollouts. The P002 note shows latent imagination for behavior learning. The P012 note argues that preserving visual details can improve RL performance.
- Survey section: Open challenges: abstraction versus fidelity.
- Confidence: medium
- Missing evidence: [NEEDS MORE EVIDENCE] Needs more completed notes on discrete latent, transformer, and diffusion-video models before making a broad field-wide claim.
- Suggested citation command: `\cite{hafner2019_planet_prov,hafner2020_dreamer_prov,alonso2024_diamond_prov}`
