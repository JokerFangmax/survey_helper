# Section 08 Integration Audit

Section: `manuscript/sections/08_evaluation_open_challenges.tex`

## Changes Applied

- Strengthened the evaluation framework around:
  - visual/reconstruction metrics,
  - control and planning utility,
  - human-judgment physical commonsense evaluation,
  - automated physics-adherence detection,
  - measurement-based physical evaluation,
  - causal/counterfactual evaluation.
- Integrated WorldModelBench, VideoPhy-2, Morpheus, WorldScore, and What-If World as benchmark coverage points.
- Preserved VideoPhy as the completed-note anchor for physical commonsense evaluation.
- Added explicit caveats that newer benchmark citations establish coverage, not detailed model rankings or solved evaluation.

## Citation Keys Used

- `oh2015_action_conditional_video_prediction_prov`
- `finn2016_physical_interaction_video_prediction_prov`
- `unterthiner2018_fvd_prov`
- `janner2019_o2p2_prov`
- `hafner2019_planet_prov`
- `hafner2020_dreamer_prov`
- `alonso2024_diamond_prov`
- `bruce2024_genie_prov`
- `bansal2025_videophy_prov`
- `bansal2025videophy2_prov`
- `li2025worldmodelbench_prov`
- `zhang2025morpheus_prov`
- `cai2026whatifworld_prov`
- `duan2025worldscore`
- `battaglia2016_interaction_networks_prov`
- `watters2017_visual_interaction_networks_prov`
- `bakhtin2019_phyre_prov`
- `yi2020_clevrer_prov`
- `bear2021_physion_prov`
- `meng2025_phygenbench_prov`
- `kang2025_physical_law_perspective_prov`
- `motamed2025_physics_iq_prov`

## Integration Plan Items Skipped

- Did not include exact WorldModelBench claims about 67K labels, 14 frontier models, a 2B judger, or GPT-4o comparison.
- Did not include VideoPhy-2's proposed 22% hard-subset joint-performance claim.
- Did not include Morpheus claims about exact experiment classes, evaluated model list, or systematic failures across all models.
- Did not include WorldScore claims about specific axes, scene layouts, or model-family dominance.
- Did not claim What-If World is the first benchmark of its kind.

## Unsupported Claims Removed or Weakened

- Reframed automated evaluation as promising but not solved.
- Reframed newer benchmarks as extending the evaluation map, not superseding older benchmarks.
- Reframed What-If World as an emerging direction.
- Reframed WorldModelBench, Morpheus, VideoPhy-2, WorldScore, and What-If World citations as benchmark coverage until detailed notes are completed.

## Remaining TODOs

- Complete detailed notes for P082, P083, P084, P078, and P085 before adding quantitative findings.
- Complete or expand notes for P033-P040 and P078-P085 before building a consolidated benchmark comparison table.
- Revisit `data/claim_bank.md` and `data/claim_evidence_map.md` after notes are completed so new evaluation claims become traceable claim IDs.
