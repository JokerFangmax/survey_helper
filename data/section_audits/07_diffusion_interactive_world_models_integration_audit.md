# Section 07 Integration Audit

Section: `manuscript/sections/07_diffusion_interactive_world_models.tex`

## Changes Applied

- Reorganized the section around:
  - video diffusion as predictive generation,
  - conditional and causal diffusion dynamics,
  - latent actions and interactive control,
  - large-scale world foundation model efforts,
  - newer interactive diffusion directions,
  - why these are not automatically physical simulators.
- Integrated Diffusion Forcing as a causal-diffusion sequence-modeling design point.
- Integrated LAPA cautiously as a latent-action/video-pretraining candidate for embodied control.
- Integrated Cosmos cautiously as an industrial-scale world foundation model platform for physical AI.
- Added iVideoGPT as a token-based interactive world-model bridge.
- Preserved DIAMOND and Genie as the strongest locally supported anchors.

## Citation Keys Used

- `hafner2019_planet_prov`
- `hafner2020_dreamer_prov`
- `alonso2024_diamond_prov`
- `ho2022_video_diffusion_models_prov`
- `voleti2022_mcvd_prov`
- `oh2015_action_conditional_video_prediction_prov`
- `finn2016_physical_interaction_video_prediction_prov`
- `bruce2024_genie_prov`
- `chen2024diffusion_forcing_prov`
- `ye2025lapa_prov`
- `wu2024ivideogpt`
- `nvidia2025cosmos`
- `ren2025_videoworld_prov`
- `huang2026_vid2world_prov`
- `bansal2025_videophy_prov`

## Integration Plan Items Skipped

- Did not claim Cosmos is the largest-scale industrial effort, open-weight, or has specific physical-benchmark failures.
- Did not claim LAPA outperforms action-labeled VLA models or eliminates action labels.
- Did not claim Diffusion Forcing improves decision-making/planning tasks or is the technical foundation for follow-up papers.
- Did not give detailed model-scale, data-scale, or benchmark numbers for Cosmos, LAPA, Diffusion Forcing, iVideoGPT, VideoWorld, or Vid2World.

## Unsupported Claims Removed or Weakened

- Reframed Cosmos as a platform-scale effort rather than a solved simulator.
- Reframed LAPA as reducing or reframing action-supervision questions, not eliminating robot action labels.
- Reframed Diffusion Forcing as complementary to DIAMOND-style conditional diffusion rather than a replacement.
- Reframed newer interactive diffusion papers as emerging boundary examples rather than established evidence.

## Remaining TODOs

- Complete detailed notes for P068, P080, P081, P062, P021, and P022 before making stronger claims.
- Add a comparison table only after notes support specific mechanisms, datasets, and evaluation protocols.
