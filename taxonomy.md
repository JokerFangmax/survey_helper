# Concept-Driven Taxonomy

Survey title: *Learning Predictive World Models from Videos: A Survey on Generative Simulation and Physical Dynamics*

Evidence policy: this taxonomy is grounded in `data/papers.csv`, completed notes, `data/claim_bank.md`, and `data/claim_evidence_map.md`. Claims are supported only where completed notes exist. Indexed papers without completed notes are listed as coverage targets, not as claim evidence.

Completed-note evidence currently covers: P001, P002, P003, P004, P005, P006, P007, P008, P009, P012, P013, P037.

## Taxonomy Axes

- Modeling goal: what the model is intended to predict, simulate, control, or evaluate.
- Representation type: pixel/video, latent state, object/graph state, token sequence, diffusion/noise space, benchmark/prompt space.
- Dynamics model: autoregressive CNN/RNN, transformation-based pixel motion, variational stochastic predictor, recurrent state-space model, graph interaction model, object-oriented renderer/dynamics, conditional diffusion, token dynamics, evaluator/benchmark.
- Conditioning signal: past video, actions, latent actions, text prompts, rewards, object states, benchmark captions.
- Evaluation protocol: reconstruction metrics, rollout error, control return, planning success, human evaluation, physical-consistency or commonsense judgment.

## Branch A: Action-Conditioned Pixel and Motion Prediction

- Modeling goal: predict future frames from past frames and interventions, making visual prediction responsive to actions rather than only extrapolating passive video.
- Representation type: pixel/video representation, sometimes with learned feature-space transformations or pixel-motion transformations.
- Dynamics model: action-conditioned autoregressive CNNs; transformation-based motion predictors such as DNA/CDNA/STP in the completed notes.
- Conditioning signal: past frames plus known actions or robot commands.
- Evaluation protocol: frame metrics such as MSE, PSNR, and SSIM; downstream control utility or task success where available.
- Core papers with completed notes: P004 (`oh2015_action_conditional_video_prediction_prov`), P005 (`finn2016_physical_interaction_video_prediction_prov`).
- Indexed papers needing notes for fuller coverage: P024 (`gupta2023_maskvit_prov`), P025 (`wang2019_e3dlstm_prov`), P026 (`gao2022_simvp_prov`), P027 (`villegas2017_motion_content_prov`).
- Supported claims: C001, C002, C003, C019.
- Limitations: pixel-space predictors can be brittle over long horizons; frame quality may not track control usefulness; transformation-based decompositions may remain short-horizon and domain-specific.
- Open questions: how to evaluate action-conditioned predictors beyond pixel fidelity; how to connect motion prediction to causal physical state; how to preserve useful details without requiring exact pixel reconstruction.

## Branch B: Stochastic Future Modeling

- Modeling goal: represent distributions over possible futures instead of committing to one deterministic rollout.
- Representation type: pixel/video representation augmented with latent stochastic variables.
- Dynamics model: variational recurrent video predictor with sampled time-varying or time-invariant latents.
- Conditioning signal: past frames, optional actions, and sampled latent variables.
- Evaluation protocol: PSNR/SSIM, best-of-sample evaluation, qualitative diversity and consistency checks.
- Core papers with completed notes: P006 (`babaeizadeh2018_sv2p_prov`).
- Indexed papers needing notes for fuller coverage: P028 (`denton2018_svg_lp_prov`).
- Supported claims: C004, C005, C006.
- Limitations: current completed evidence is narrow; stochastic video metrics can reward best samples without fully testing calibrated uncertainty; latent variables may be ignored without careful training.
- Open questions: how to evaluate stochastic forecasts without best-of-many heuristics; how to bind stochasticity to objects, hidden variables, or physical causes; how to keep diverse long-horizon futures physically consistent. [NEEDS MORE EVIDENCE]

## Branch C: Object-Centric and Relational Physical Dynamics

- Modeling goal: model physical systems as entities and interactions, often to improve generalization, hidden-state inference, and planning.
- Representation type: object states, relation graphs, object-centric latent variables, or visual features mapped into structured dynamics.
- Dynamics model: graph interaction networks; visual encoder plus interaction dynamics; object-oriented perception, physics, and rendering modules.
- Conditioning signal: object states, visual observations, relational structure, and sometimes task/planning objectives.
- Evaluation protocol: state or rollout error, planning success, generalization across object configurations, qualitative physical plausibility.
- Core papers with completed notes: P007 (`battaglia2016_interaction_networks_prov`), P008 (`watters2017_visual_interaction_networks_prov`), P009 (`janner2019_o2p2_prov`).
- Indexed papers needing notes for fuller coverage: P017 (`kipf2020_cswm_prov`), P018 (`wu2023_slotformer_prov`), P019 (`veerapaneni2019_op3_prov`), P029 (`fragkiadaki2016_billiards_prov`), P030 (`chang2016_compositional_object_physics_prov`), P031 (`minderer2019_object_structure_dynamics_prov`).
- Supported claims: C007, C008, C009, C010, C025.
- Limitations: much of the completed evidence is from synthetic or controlled settings; object abstractions may require strong priors or fail under clutter; not all object-centric models are video-first.
- Open questions: how to learn object structure without direct supervision; how to infer hidden physical variables from raw video; how to combine object-level dynamics with rich generative rendering; how to transfer structured dynamics to realistic embodied environments. [NEEDS MORE EVIDENCE]

## Branch D: Latent World Models for Planning and Control

- Modeling goal: learn compact predictive states that support planning, policy learning, or policy evolution from visual observations.
- Representation type: continuous latent states, recurrent state-space models, VAE latents, reward/value-related latent features.
- Dynamics model: VAE plus MDN-RNN controller pipelines; RSSM latent transition models; latent imagination with actor-critic behavior learning.
- Conditioning signal: past observations, actions, rewards, candidate action sequences, learned policies.
- Evaluation protocol: episodic return, control return, sample efficiency, task success, comparison to model-free or simulator baselines.
- Core papers with completed notes: P001 (`hafner2019_planet_prov`), P002 (`hafner2020_dreamer_prov`), P003 (`ha2018_world_models_prov`).
- Indexed papers needing notes for fuller coverage: P010 (`zhou2025_dino_wm_prov`), P014 (`micheli2023_iris_prov`), P015 (`hafner2021_dreamerv2_prov`), P016 (`wu2022_daydreamer_prov`), P032 (`wu2023_contextwm_prov`).
- Supported claims: C011, C012, C013, C014, C026.
- Limitations: reward-driven evaluation may miss physical correctness; learned simulators can be exploitable; online planning can be slow; compact latents may discard visual details useful for control.
- Open questions: when should a world model use online planning versus amortized policy learning; how should latent simulators be evaluated beyond return; how can compact state abstractions retain control-critical visual detail; how well do latent models transfer across domains. [NEEDS MORE EVIDENCE]

## Branch E: Image-Space and Diffusion-Based World Models

- Modeling goal: use strong generative video models, especially diffusion models, as predictive simulators or world models.
- Representation type: image space, video frames, diffusion/noise space, and sometimes action-conditioned visual histories.
- Dynamics model: conditional diffusion for next-observation prediction; autoregressive rollout by feeding generated frames back into context.
- Conditioning signal: observation history, action history, optional text/video conditioning depending on the indexed paper.
- Evaluation protocol: control performance in a learned world model, video quality metrics, qualitative trajectory analysis, physical-consistency checks where available.
- Core papers with completed notes: P012 (`alonso2024_diamond_prov`).
- Indexed papers needing notes for fuller coverage: P011 (`ho2022_video_diffusion_models_prov`), P020 (`voleti2022_mcvd_prov`), P022 (`huang2026_vid2world_prov`).
- Supported claims: C015, C016, C017, C021, C026.
- Limitations: completed evidence is currently Atari-centered; diffusion can be computationally heavier than latent-state models; visual fidelity does not establish physical correctness.
- Open questions: when does image-space generation justify its compute cost; how should diffusion simulators be evaluated for physical consistency; how can diffusion models support interactive control rather than passive generation. [NEEDS MORE EVIDENCE]

## Branch F: Interactive and Embodied Generative Environments

- Modeling goal: create controllable predictive environments from video, including settings where the action space is known, latent, or inferred.
- Representation type: video tokens, latent action tokens, interactive video states, action-conditioned latent or pixel representations.
- Dynamics model: action-conditioned predictors, latent-action dynamics models, token autoregressive dynamics, and learned simulators for control.
- Conditioning signal: real actions, robot commands, latent actions, prompts or initial frames, policies.
- Evaluation protocol: controllability, imitation performance, task success, human evaluation, control return.
- Core papers with completed notes: P004 (`oh2015_action_conditional_video_prediction_prov`), P005 (`finn2016_physical_interaction_video_prediction_prov`), P013 (`bruce2024_genie_prov`).
- Indexed papers needing notes for fuller coverage: P016 (`wu2022_daydreamer_prov`), P021 (`ren2025_videoworld_prov`), P022 (`huang2026_vid2world_prov`), P024 (`gupta2023_maskvit_prov`).
- Supported claims: C018, C019, C020, C025.
- Limitations: current completed evidence mixes Atari, robot pushing, and CoinRun-style settings; latent-action controllability is still narrow; video-only learning can leave action semantics ambiguous.
- Open questions: how to evaluate controllability in open-ended video worlds; how to align latent actions with real interventions; how to move from playable videos to physically reliable embodied simulators. [NEEDS MORE EVIDENCE]

## Branch G: Evaluation, Physical Consistency, and Benchmarks

- Modeling goal: measure whether predictive or generative video models are useful as world models, not merely visually plausible generators.
- Representation type: benchmark prompts, generated videos, human judgments, automatic evaluator scores, task returns, planning outcomes.
- Dynamics model: not always a model branch; includes metrics, benchmark designs, and evaluators for physical commonsense, control utility, and video quality.
- Conditioning signal: text prompts, video inputs, actions, benchmark tasks, human labels.
- Evaluation protocol: human evaluation, automatic physical-consistency scores, semantic adherence, task return, rollout error, planning success.
- Core papers with completed notes: P037 (`bansal2025_videophy_prov`), plus evaluation-relevant evidence from P004, P009, P012, and P013.
- Indexed papers needing notes for fuller coverage: P033 (`bakhtin2019_phyre_prov`), P034 (`yi2020_clevrer_prov`), P035 (`bear2021_physion_prov`), P036 (`unterthiner2018_fvd_prov`), P038 (`meng2025_phygenbench_prov`), P039 (`kang2025_physical_law_perspective_prov`), P040 (`motamed2025_physics_iq_prov`).
- Supported claims: C003, C021, C022, C023, C024.
- Limitations: benchmark results can depend on prompt design, annotation protocol, domain abstraction, and automatic-evaluator reliability; many current metrics do not jointly test visual quality, controllability, causal validity, and physical law compliance.
- Open questions: how to combine video quality, physical consistency, controllability, and causal/counterfactual testing; how to validate automatic evaluators; how to compare action-conditioned world models with text-conditioned video generators. [NEEDS MORE EVIDENCE]

## Cross-Cutting Comparison Table Draft

| Branch | Goal | Representation | Dynamics | Conditioning | Evaluation | Completed-note papers |
|---|---|---|---|---|---|---|
| Action-conditioned pixel/motion prediction | Predict future video under interventions | Pixels, motion transforms | CNN/RNN, DNA/CDNA/STP | Frames plus actions | Frame metrics, task utility | P004, P005 |
| Stochastic future modeling | Model multiple plausible futures | Pixels plus stochastic latents | Variational recurrent predictor | Frames, actions, latent samples | PSNR/SSIM, best-of-samples | P006 |
| Object-centric dynamics | Model entities and interactions | Objects, graphs, visual object states | Interaction networks, object physics/rendering | Objects, relations, visuals | Rollout error, planning success | P007, P008, P009 |
| Latent world models | Plan or learn behavior in compact state | Latent states, RSSM, VAE latents | Recurrent latent dynamics | Observations, actions, rewards | Return, sample efficiency | P001, P002, P003 |
| Diffusion world models | Use generative image-space dynamics | Images, diffusion/noise space | Conditional diffusion rollout | Observation/action history | Control return, visual analysis | P012 |
| Interactive environments | Generate controllable video worlds | Tokens, latent actions, video states | Token or action-conditioned dynamics | Actions, latent actions, prompts | Controllability, imitation, human eval | P004, P005, P013 |
| Evaluation and benchmarks | Test world-model correctness | Prompts, videos, scores | Metrics/evaluators | Text, video, actions, labels | Human and automatic judgment | P037, plus P004/P009/P012/P013 |
