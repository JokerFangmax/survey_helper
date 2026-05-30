# Full Draft Blocking Fixes

Generated after applying blocking fixes requested from `data/full_draft_readiness_audit.md`.

## Scope

Only blocking or marker-level fixes were applied. No sections were rewritten wholesale, no new papers were added, and no unsupported citations were introduced.

## Fixes Applied

### Metadata TODOs

- Replaced `\author{TODO}` with `\author{Anonymous}` in `manuscript/main.tex`.
- Replaced `\date{TODO}` with `\date{}` in `manuscript/main.tex`.

### Citation-Key Check

- Rechecked manuscript citation keys against `bib/references.bib`.
- Result: no invalid citation keys were found.
- No citation-key edits were necessary.

### Unsupported Marker Cleanup

Removed all manuscript occurrences of `[NEEDS SOURCE]`, `[VERIFY]`, bracketed `[TODO]`, and raw `TODO`.

The changes did not convert unsupported claims into supported claims. Instead, unsupported material was weakened or reframed as deferred coverage:

- `manuscript/sections/01_introduction.tex`
  - Reframed modern diffusion-video, benchmark, and latent-control papers as coverage targets rather than established evidence.
  - Updated comment wording from marker-style TODO/source language to neutral revision notes.

- `manuscript/sections/04_video_prediction.tex`
  - Replaced unsupported claims about P020 and P023--P028 with a statement that these papers are coverage targets until notes support detailed comparison.

- `manuscript/sections/05_object_centric_physical_dynamics.tex`
  - Reframed C-SWM, SlotFormer, OP3, billiards-style visual physics, compositional dynamics, and unsupervised object-structure papers as coverage targets rather than evidence for stronger claims.

- `manuscript/sections/06_latent_world_models.tex`
  - Reframed DreamerV2, IRIS, DayDreamer, DINO-WM, and Contextualized World Models claims as deferred coverage because their local notes remain incomplete or contain `UNKNOWN` fields.

- `manuscript/sections/07_diffusion_interactive_world_models.tex`
  - Weakened the diffusion-video lineage paragraph so Video Diffusion Models and MCVD are treated as indexed coverage targets rather than evidence for architecture or empirical claims.
  - Weakened VideoWorld and Vid2World discussion so they are not used to support mechanism, benchmark, action-space, or result claims.
  - Replaced an unsupported claim about denoising objectives with an open evaluation question about causal structure, conservation-like behavior, object permanence, and counterfactual validity.
  - Updated comment audit wording to remove marker-style TODO/source language.

- `manuscript/sections/08_evaluation_open_challenges.tex`
  - Reframed FVD details as not claimed in this draft because the local note is metadata-only.
  - Reframed PHYRE, CLEVRER, and Physion details as not claimed because corresponding notes contain `UNKNOWN` fields.
  - Replaced unsupported long-horizon physical-evaluation claims with open coverage-target language.
  - Reframed PhyGenBench, Physical Law Perspective, and Physics-IQ details as deferred until notes are completed.
  - Replaced an unsupported "exact metrics remain unsettled" marker with "not established in the current evidence base."
  - Weakened broad sim-to-real reliability language into an open challenge rather than an established result.
  - Updated comment audit wording to remove marker-style TODO/source language.

### Conclusion Check

- `manuscript/sections/09_conclusion.tex`
  - Softened "Current evidence suggests..." to "The preceding sections suggest..." so the conclusion clearly synthesizes prior sections rather than introducing a new independent claim.

## Post-Fix Marker Check

After edits, manuscript search found:

- `[NEEDS SOURCE]`: 0
- `[VERIFY]`: 0
- `[TODO]`: 0
- raw `TODO`: 0

## Validation Commands

Ran:

```powershell
python scripts\validate_papers.py
python scripts\check_bibtex_keys.py
```

Results:

- `validate_papers.py`: passed and wrote `data/validation_report.md`.
- `check_bibtex_keys.py`: passed.
- CSV rows with BibTeX keys: 40.
- Unique CSV BibTeX keys: 40.
- BibTeX entries: 40.
- Unique BibTeX keys: 40.
- Missing BibTeX entries for CSV keys: none.
- Unused BibTeX entries: none.

## Remaining Non-Blocking Issues

- The manuscript still has only one table and no figures.
- `02_background.tex` says six conceptual families, while the taxonomy section uses seven.
- `outline.md` still differs from the current manuscript organization after Section 07.
- Some candidate-paper paragraphs remain inventory-like, but they no longer make unsupported claims.
- In-file claim-evidence audit comments remain in the `.tex` files for drafting traceability.

