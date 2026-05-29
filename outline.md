# Survey Outline

Working title: *Learning Predictive World Models from Videos: A Survey on Generative Simulation and Physical Dynamics*

Purpose: submission-oriented outline only. This file is not manuscript prose. Claims below refer to `data/claim_bank.md` and should be expanded only after the relevant notes are complete.

## 1. Introduction

- Section thesis: predictive world models from video have moved from frame prediction toward controllable, structured, generative, and physically evaluated simulators.
- Key claims: C001, C003, C011, C021, C024.
- Supporting papers: P004 (`oh2015_action_conditional_video_prediction_prov`), P001 (`hafner2019_planet_prov`), P002 (`hafner2020_dreamer_prov`), P003 (`ha2018_world_models_prov`), P012 (`alonso2024_diamond_prov`), P037 (`bansal2025_videophy_prov`).
- Expected figures/tables: Figure 1, survey landscape showing the transition from pixel video prediction to latent control, structured dynamics, diffusion simulators, interactive environments, and physical evaluation.
- Missing evidence: broader benchmark support from P033-P040; diffusion-video lineage notes P011/P020; modern latent/interactive notes P010/P014-P016/P021/P022. [NEEDS MORE EVIDENCE]

## 2. Scope, Definitions, and Taxonomy

- Section thesis: the survey should classify work by modeling goal, representation, dynamics, conditioning, and evaluation rather than by chronological paper families.
- Key claims: C003, C007, C011, C015, C019, C021.
- Supporting papers: P004, P005, P007, P008, P009, P001, P002, P003, P012, P013, P037.
- Expected figures/tables: Table 1, taxonomy axes; Table 2, branch-by-branch comparison from `taxonomy.md`.
- Missing evidence: complete notes for indexed papers outside the current completed-note set; definitions for "world model", "generative simulator", and "physical consistency" should be checked against notes before manuscript drafting. [NEEDS MORE EVIDENCE]

## 3. From Video Prediction to World Modeling

- Section thesis: early video prediction becomes relevant to world modeling when predictions are conditioned on actions, evaluated for control utility, or designed around physical interactions.
- Key claims: C001, C002, C003, C019.
- Supporting papers: P004 (`oh2015_action_conditional_video_prediction_prov`), P005 (`finn2016_physical_interaction_video_prediction_prov`), P009 (`janner2019_o2p2_prov`), P012 (`alonso2024_diamond_prov`).
- Expected figures/tables: Figure 2, passive frame prediction versus action-conditioned prediction; Table 3, evaluation signals from frame metrics to planning/control utility.
- Missing evidence: notes for recurrent and transformer-style video predictors P024-P027; additional evidence on whether frame metrics correlate with downstream usefulness. [NEEDS MORE EVIDENCE]

## 4. Stochasticity and Uncertainty in Future Prediction

- Section thesis: stochastic future modeling is necessary when video futures are multi-modal, but uncertainty design and evaluation remain under-supported by the current note set.
- Key claims: C004, C005, C006.
- Supporting papers: P006 (`babaeizadeh2018_sv2p_prov`).
- Expected figures/tables: Figure 3, deterministic single rollout versus sampled future distribution; Table 4, latent design choices such as time-varying versus time-invariant latents.
- Missing evidence: completed notes for P028 (`denton2018_svg_lp_prov`) and any additional stochastic-video papers; stronger evidence on calibrated uncertainty and physical consistency of stochastic rollouts. [NEEDS MORE EVIDENCE]

## 5. Object-Centric and Structured Physical Dynamics

- Section thesis: object and relation structure is a key inductive bias for physical dynamics, especially when models must generalize across configurations, infer hidden causes, or support planning.
- Key claims: C007, C008, C009, C010, C025.
- Supporting papers: P007 (`battaglia2016_interaction_networks_prov`), P008 (`watters2017_visual_interaction_networks_prov`), P009 (`janner2019_o2p2_prov`), P005 (`finn2016_physical_interaction_video_prediction_prov`), P013 (`bruce2024_genie_prov`).
- Expected figures/tables: Figure 4, mapping from pixels to objects/relations to rollouts/planning; Table 5, structured-dynamics assumptions and evaluation settings.
- Missing evidence: notes for P017-P019 and P029-P031; more realistic-video evidence for object-centric generalization beyond controlled or synthetic settings. [NEEDS MORE EVIDENCE]

## 6. Latent World Models for Planning and Control

- Section thesis: latent world models make predictive modeling useful for control by replacing expensive image rollouts with compact dynamics for planning, policy learning, or policy evolution.
- Key claims: C011, C012, C013, C014, C026.
- Supporting papers: P001 (`hafner2019_planet_prov`), P002 (`hafner2020_dreamer_prov`), P003 (`ha2018_world_models_prov`), P012 (`alonso2024_diamond_prov`).
- Expected figures/tables: Figure 5, latent world-model loop with encoder, dynamics, reward/value, planner or actor; Table 6, online planning versus latent imagination versus hallucinated policy training.
- Missing evidence: notes for P010, P014, P015, P016, P032; direct evidence on simulator exploitation or physical failures in learned latent simulators. [NEEDS MORE EVIDENCE]

## 7. Diffusion-Based and Image-Space World Models

- Section thesis: diffusion-based world models revisit image-space simulation with stronger generative machinery, creating a new abstraction-fidelity trade-off for control and physical evaluation.
- Key claims: C015, C016, C017, C021, C026.
- Supporting papers: P012 (`alonso2024_diamond_prov`), P001 (`hafner2019_planet_prov`), P002 (`hafner2020_dreamer_prov`), P037 (`bansal2025_videophy_prov`).
- Expected figures/tables: Figure 6, latent-state rollout versus image-space diffusion rollout; Table 7, fidelity, compute, controllability, and evaluation trade-offs.
- Missing evidence: completed notes for P011, P020, P022; more evidence outside Atari; physical-law evaluation of diffusion rollouts. [NEEDS MORE EVIDENCE]

## 8. Interactive and Embodied Generative Environments

- Section thesis: interactive world models extend prediction from watching video to controlling video worlds, using known actions, robot commands, or learned latent actions.
- Key claims: C018, C019, C020, C025.
- Supporting papers: P004 (`oh2015_action_conditional_video_prediction_prov`), P005 (`finn2016_physical_interaction_video_prediction_prov`), P013 (`bruce2024_genie_prov`).
- Expected figures/tables: Figure 7, action-conditioned versus latent-action-controlled video generation; Table 8, conditioning signals and controllability evaluations.
- Missing evidence: completed notes for P016, P021, P022, P024; stronger evidence linking controllability to physically reliable simulation. [NEEDS MORE EVIDENCE]

## 9. Evaluation: Physical Consistency, Control Utility, and Benchmarks

- Section thesis: evaluating video world models requires combining visual fidelity, control utility, physical commonsense, causal validity, and human/automatic judgments.
- Key claims: C003, C021, C022, C023, C024.
- Supporting papers: P004 (`oh2015_action_conditional_video_prediction_prov`), P009 (`janner2019_o2p2_prov`), P012 (`alonso2024_diamond_prov`), P013 (`bruce2024_genie_prov`), P037 (`bansal2025_videophy_prov`).
- Expected figures/tables: Table 9, evaluation protocols and what they test; Figure 8, evaluation matrix crossing visual fidelity, control, physical consistency, and generalization.
- Missing evidence: completed notes for P033-P036 and P038-P040; direct comparison among FVD, physical-reasoning benchmarks, prompt-based video commonsense benchmarks, and control returns. [NEEDS MORE EVIDENCE]

## 10. Open Challenges

- Section thesis: the central unresolved issues are evaluation beyond surface realism, unsupervised structure learning, controllability, long-horizon physical consistency, and the abstraction-fidelity trade-off.
- Key claims: C014, C017, C023, C024, C025, C026.
- Supporting papers: P001, P002, P003, P004, P005, P007, P008, P009, P012, P013, P037.
- Expected figures/tables: Table 10, open challenges mapped to evidence gaps and candidate papers needing notes.
- Missing evidence: most challenge claims are medium confidence in the claim bank; the section should remain explicitly cautious until the missing notes are completed. [NEEDS MORE EVIDENCE]

## 11. Conclusion

- Section thesis: the conclusion should synthesize the survey's conceptual arc and evidence gaps without introducing new claims.
- Key claims: reuse only claims already established in Sections 3-10.
- Supporting papers: no new supporting papers beyond prior sections.
- Expected figures/tables: none required; optional final roadmap figure if the introduction figure is not overloaded.
- Missing evidence: all unresolved `[NEEDS MORE EVIDENCE]` items from earlier sections should be summarized, not hidden.

## Planned Figures and Tables

- Figure 1: survey landscape from video prediction to physical world models.
- Figure 2: passive prediction versus action-conditioned prediction.
- Figure 3: deterministic rollout versus stochastic future distribution.
- Figure 4: object-centric dynamics pipeline.
- Figure 5: latent world-model control loop.
- Figure 6: latent rollout versus image-space diffusion rollout.
- Figure 7: known actions versus latent actions for interactive generation.
- Figure 8: evaluation matrix for fidelity, control, physics, and generalization.
- Table 1: taxonomy axes.
- Table 2: concept-driven taxonomy branches.
- Table 3: video prediction evaluation signals.
- Table 4: stochastic latent design choices.
- Table 5: structured dynamics assumptions.
- Table 6: planning/control variants in latent world models.
- Table 7: diffusion versus latent world-model trade-offs.
- Table 8: interactive conditioning signals and controllability.
- Table 9: evaluation protocols.
- Table 10: open challenges and missing evidence.

## Evidence-Gap Priority List

- High priority: complete notes for evaluation papers P033-P040, because several outline sections depend on evaluation claims.
- High priority: complete notes for diffusion-video papers P011, P020, and P022 before drafting the diffusion section.
- High priority: complete notes for latent-control extensions P010, P014-P016, and P032 before broadening claims about modern latent world models.
- Medium priority: complete notes for object-centric papers P017-P019 and P029-P031 before drafting the structured-dynamics section.
- Medium priority: complete notes for video prediction baselines P024-P028 before drafting the historical video-prediction section.
