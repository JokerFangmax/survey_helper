# Section Audit: 02 Background

File: `manuscript/sections/02_background.tex`

## Major Claims

1. Video prediction estimates future visual observations from past visual evidence, and action-conditioned variants predict under interventions.
   - Supporting papers: P004, P005, P006
   - Citation keys: `oh2015_action_conditional_video_prediction_prov`, `finn2016_physical_interaction_video_prediction_prov`, `babaeizadeh2018_sv2p_prov`
   - Evidence source: C001, C002, C004; completed notes P004, P005, P006
   - Confidence: high

2. Predictive world models from videos are broader than future-frame prediction because they may support controlled prediction, planning, policy learning, imagined interaction, or simulator-style analysis beyond pixel reconstruction.
   - Supporting papers: P001, P002, P003, P004, P009, P012
   - Citation keys: `hafner2019_planet_prov`, `hafner2020_dreamer_prov`, `ha2018_world_models_prov`, `oh2015_action_conditional_video_prediction_prov`, `janner2019_o2p2_prov`, `alonso2024_diamond_prov`
   - Evidence source: C003, C011, C013, C014, C015; completed notes P001, P002, P003, P004, P009, P012
   - Confidence: high

3. Representation is a central taxonomy axis because the completed notes cover models operating over pixels, latent states, object/graph states, diffusion image space, or latent action/token spaces.
   - Supporting papers: P001, P002, P003, P004, P005, P007, P008, P009, P012, P013
   - Citation keys: `hafner2019_planet_prov`, `hafner2020_dreamer_prov`, `ha2018_world_models_prov`, `oh2015_action_conditional_video_prediction_prov`, `finn2016_physical_interaction_video_prediction_prov`, `battaglia2016_interaction_networks_prov`, `watters2017_visual_interaction_networks_prov`, `janner2019_o2p2_prov`, `alonso2024_diamond_prov`, `bruce2024_genie_prov`
   - Evidence source: C007, C011, C015, C018; taxonomy.md; completed notes
   - Confidence: medium

4. Dynamics and conditioning are central axes because different model families use pixel-space recurrence, stochastic latent variables, recurrent latent states, graph interactions, conditional diffusion, explicit actions, or learned latent actions.
   - Supporting papers: P001, P002, P004, P005, P006, P007, P008, P012, P013
   - Citation keys: `hafner2019_planet_prov`, `hafner2020_dreamer_prov`, `oh2015_action_conditional_video_prediction_prov`, `finn2016_physical_interaction_video_prediction_prov`, `babaeizadeh2018_sv2p_prov`, `battaglia2016_interaction_networks_prov`, `watters2017_visual_interaction_networks_prov`, `alonso2024_diamond_prov`, `bruce2024_genie_prov`
   - Evidence source: C004, C005, C006, C012, C015, C018, C019; completed notes
   - Confidence: high

5. Evaluation must distinguish frame fidelity, planning/control utility, controllability, physical consistency, and human or automatic judgments.
   - Supporting papers: P004, P009, P012, P037
   - Citation keys: `oh2015_action_conditional_video_prediction_prov`, `janner2019_o2p2_prov`, `alonso2024_diamond_prov`, `bansal2025_videophy_prov`
   - Evidence source: C003, C021, C022, C023, C024; completed notes P004, P009, P012, P037
   - Confidence: high

6. The survey distinguishes pixel-level video prediction, latent world models, object-centric physical dynamics, diffusion-based world models, interactive and embodied world models, and evaluation benchmarks for physical consistency, while treating some branches as provisional until more notes are complete.
   - Supporting papers: P001, P002, P003, P004, P005, P006, P007, P008, P009, P012, P013, P037
   - Citation keys: `hafner2019_planet_prov`, `hafner2020_dreamer_prov`, `ha2018_world_models_prov`, `oh2015_action_conditional_video_prediction_prov`, `finn2016_physical_interaction_video_prediction_prov`, `babaeizadeh2018_sv2p_prov`, `battaglia2016_interaction_networks_prov`, `watters2017_visual_interaction_networks_prov`, `janner2019_o2p2_prov`, `alonso2024_diamond_prov`, `bruce2024_genie_prov`, `bansal2025_videophy_prov`
   - Evidence source: taxonomy.md; claim bank themes C001--C026; completed notes
   - Confidence: medium

## Unsupported or Weak Claims

- The phrase "world model" is defined operationally for this survey, and the revised section narrows it to controlled prediction, planning, policy learning, or simulator-style analysis.
- The claim that representation, dynamics, conditioning, interaction, and evaluation are useful axes remains a taxonomy-level synthesis. It is supported by the completed notes but should be revisited after completing notes for P010--P040.
- Claims about diffusion-based world models are now explicitly narrow because the completed-note evidence mainly covers P012/DIAMOND.
- Claims about physical-consistency evaluation are strong for P037 but incomplete as benchmark coverage until P033--P040 notes are completed.

## Possible Missing References

- P010, P014--P016, P032 for broader latent world-model coverage.
- P011, P020, P022 for diffusion-video and interactive diffusion coverage.
- P017--P019 and P029--P031 for broader object-centric physical dynamics.
- P024--P028 for video prediction baselines and stochastic/video factorization coverage.
- P033--P036 and P038--P040 for evaluation benchmarks and physical-law testing.

## Suggestions for Improvement

- Complete notes for benchmark papers before expanding the evaluation-heavy parts of the background and later evaluation section.
- Add a small definitions table after the section is stable, mapping "video prediction", "world model", "generative simulator", "interactive world model", and "physical-consistency benchmark" to evidence-backed criteria.
- Revisit the taxonomy paragraph after notes for P010--P040 are ingested, because several currently narrow branches may need rebalancing.
- When drafting the introduction, keep this background section as a definitions-and-axes section rather than duplicating the survey's full motivation.

## Revision Notes

- Revised after `data/section_audits/02_background_review.md`.
- Split the dense world-model paragraph into a definition paragraph and an evaluation-beyond-frames paragraph.
- Replaced broad claims such as "visually strong generative models" and "complete evaluation protocol" with narrower survey-scoped wording.
- Kept the original valid citation set and did not add new citations from papers whose notes are incomplete.
