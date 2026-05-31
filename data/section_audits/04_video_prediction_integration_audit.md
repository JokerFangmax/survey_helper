# Section 04 Integration Audit

Section: `manuscript/sections/04_video_prediction.tex`

## Changes Applied

- Added Diffusion Forcing as a brief bridge between architecture-oriented video prediction and diffusion-based world models.
- Added a forward pointer from Section 04 to Sections 06 and 07 for token-based world models and causal-diffusion sequence models.
- Kept the section centered on action-conditioned Atari prediction, robot pixel-motion prediction, and SV2P-style stochastic prediction.

## Citation Keys Used

- `chen2024diffusion_forcing_prov`
- `wu2024ivideogpt`

## Integration Plan Items Skipped

- Did not make Diffusion Forcing a central Section 04 paper.
- Did not add the full proposed sentence claiming independent per-token noise levels, diffusion guidance, and autoregressive video rollout behavior in detail.
- Did not update figures or tables inside Section 04 because no local Section 04 table exists.

## Unsupported Claims Removed or Weakened

- Weakened "Diffusion Forcing is the most prominent example" to "a useful bridge" because the placeholder note does not support a prominence claim.
- Avoided claims about rollout beyond training horizon, planning gains, and follow-up influence because detailed notes are not available.

## Remaining TODOs

- Complete a detailed note for P081 before expanding the technical description of Diffusion Forcing.
- If Section 04 later gains a video-prediction comparison table, add Diffusion Forcing only as a bridge/cross-reference, not as a core video-prediction baseline.
