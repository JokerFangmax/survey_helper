# Internal Trace Cleanup Report

## Scope

Cleaned internal workflow traces from:

- `manuscript/sections/01_introduction.tex`
- `manuscript/sections/02_background.tex`
- `manuscript/sections/03_taxonomy.tex`
- `manuscript/sections/04_video_prediction.tex`
- `manuscript/sections/05_object_centric_physical_dynamics.tex`
- `manuscript/sections/06_latent_world_models.tex`
- `manuscript/sections/07_diffusion_interactive_world_models.tex`
- `manuscript/sections/08_evaluation_open_challenges.tex`

No changes were made to `data/papers.csv`, `notes/`, or `bib/references.bib`.

## Cleanup Actions

| Category | Action taken | Files affected |
|---|---|---|
| Local evidence workflow phrases | Removed or replaced phrases such as "completed notes", "evidence-ready", "coverage targets", "UNKNOWN evidence fields", "metadata-only", "repository indexes", "note base", and "current evidence base". | Sections 01, 02, 03, 04, 05, 06, 07, 08 |
| Paper IDs in manuscript prose/tables | Replaced paper identifiers such as P001, P002, P003, P004, P005, P006, P007, P008, P009, P012, P013, and P037 with formal method or paper-family names. | Sections 03, 04 |
| Local claim-audit comments | Removed embedded `Claim-Evidence Audit` / `Concise Claim-Evidence Audit` comment blocks from manuscript section files. | Sections 01, 02, 04, 05, 06, 07, 08 |
| Unsupported or workflow-dependent sentences | Deleted sentences that exposed local note status. Where useful for caution, replaced them with formal limitations such as "this section does not make detailed claims" or "the survey treats this as an open challenge." | Sections 01, 04, 05, 06, 07, 08 |
| Claim weakening | Weakened claims about diffusion-video lineage, modern latent extensions, newer interactive diffusion papers, and benchmark families so they indicate relevance or evaluation direction without asserting unsupported detailed results. | Sections 06, 07, 08 |

## Notable Edits

- Introduction: removed the sentence stating that some papers were "indexed but not yet supported by completed notes" and treated as "coverage targets".
- Background: removed note-status language and kept only the conceptual taxonomy setup.
- Taxonomy: changed the table column from "Evidence-ready examples" to "Representative examples" and replaced internal paper IDs with method names.
- Video prediction: replaced P004/P005/P006 prose references with method names and removed the local evidence-gap framing.
- Object-centric dynamics: replaced "completed notes" / "evidence-ready" wording with formal discussion of reviewed papers and comparison dimensions.
- Latent world models: removed `UNKNOWN` evidence-field language and reframed modern extensions as comparison axes rather than supported detailed claims.
- Diffusion and interactive world models: removed repository/note-status descriptions and weakened detailed claims about Video Diffusion Models, MCVD, VideoWorld, and Vid2World.
- Evaluation: removed local note-status descriptions for FVD, PHYRE, CLEVRER, Physion, PhyGenBench, How Far Is Video Generation from World Model, and Physics-IQ; retained them only as benchmark-context citations where appropriate.

## Verification

Ran a manuscript-wide search for:

`completed notes`, `completed-note`, `evidence-ready`, `coverage targets`, `UNKNOWN`, `claim bank`, `TODO`, `VERIFY`, `NEEDS SOURCE`, `NEEDS MORE EVIDENCE`, `P[0-9]{3}`, `metadata-only`, `repository indexes`, `note base`, `current evidence base`, `local note`, `this draft`, `Claim-Evidence Audit`, and `Concise Claim`.

Result: no matches in `manuscript/main.tex` or `manuscript/sections`.

## Remaining Caution

This cleanup intentionally did not broaden literature coverage or add new claims. Several sections now use conservative phrasing for newer or less-developed areas; those areas should be strengthened only after the corresponding literature notes and claim-evidence mappings are completed.
