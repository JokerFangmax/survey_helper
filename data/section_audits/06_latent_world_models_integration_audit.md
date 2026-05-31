# Section 06 Integration Audit

Section: `manuscript/sections/06_latent_world_models.tex`

## Changes Applied

- Added iVideoGPT as a token-based interactive world-model bridge.
- Added V-JEPA 2 as a feature-space predictive model contrast to generative latent-state models.
- Added the requested comparison axes:
  - discrete tokens vs. continuous latent states,
  - generative latent prediction vs. non-generative feature prediction,
  - small-domain world models vs. large-scale video-pretrained models.
- Preserved Recurrent World Models, PlaNet, and Dreamer as the foundational lineage.
- Added a closing paragraph emphasizing that modern token and feature-space models are complementary pressure tests, not replacements for RSSM/Dreamer-style models.

## Citation Keys Used

- `ha2018_world_models_prov`
- `hafner2019_planet_prov`
- `hafner2020_dreamer_prov`
- `alonso2024_diamond_prov`
- `hafner2021_dreamerv2_prov`
- `micheli2023_iris_prov`
- `wu2022_daydreamer_prov`
- `zhou2025_dino_wm_prov`
- `wu2023_contextwm_prov`
- `wu2024ivideogpt`
- `assran2025vjepa2_prov`

## Integration Plan Items Skipped

- Did not claim iVideoGPT was published at NeurIPS 2024; the local CSV/BibTeX currently list it as arXiv.
- Did not claim iVideoGPT pretrains on millions of trajectories or achieves specific transfer results.
- Did not claim V-JEPA 2 trains on over one million hours of video, achieves zero-shot pick-and-place, or requires a specific AC post-training stage.
- Did not claim iVideoGPT or V-JEPA 2 provide stronger evidence than PlaNet/Dreamer.

## Unsupported Claims Removed or Weakened

- Replaced detailed empirical claims with design-space language.
- Weakened "core evidence" language to "recent bridge," "methodological contrast," and "useful additions to the survey map."
- Added explicit caution that stronger empirical claims require completed notes.

## Remaining TODOs

- Complete detailed notes for P062 and P079 before expanding their method/results descriptions.
- Complete notes for DreamerV2, IRIS, DayDreamer, DINO-WM, and ContextWM before making detailed modern latent-model comparisons.
