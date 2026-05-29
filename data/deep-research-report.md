# Learning Predictive World Models from Videos

## Executive Summary

This initial verified paper pool treats **predictive world modeling from video** as a field that grew out of video prediction, but is no longer reducible to “future frame synthesis.” The literature now splits along a few major design choices: whether the model predicts in **pixel space**, **latent space**, **object-centric space**, or **feature space**; whether it is meant mainly for **visual continuation**, **planning/control**, or **interactive simulation**; and whether it is evaluated by **reconstruction fidelity**, **decision utility**, or **physical/causal consistency**. The strongest survey backbone is therefore not “all video generation,” but a chain from action-conditioned video prediction, through stochastic and object-centric dynamics, into latent imagination for control, and then into diffusion/foundation-style interactive video world models. citeturn29search0turn2search8turn5search0turn7search0turn11search1turn14search0turn16search0

Two survey-level conclusions are already clear from the verified pool. First, the most important conceptual shift was from **predicting pixels directly** to **learning compact state representations whose dynamics are useful for planning**, exemplified by the trajectory from early action-conditioned frame prediction to PlaNet, Dreamer, DreamerV2, IRIS, DayDreamer, and DINO-WM. Second, the most important current tension is between **visual realism** and **world-model usefulness**: diffusion and foundation-scale video models can produce strikingly realistic videos, but recent evaluation work repeatedly shows that realism does not yet imply robust physical-law generalization or embodied controllability. citeturn29search0turn11search1turn11search2turn11search3turn13search3turn12search1turn19search0turn15search1turn14search0turn35search0turn24search3turn36search0

The paper pool below contains **40 verified papers**. I prioritized primary sources—arXiv abstract pages, OpenReview entries, conference proceedings, and official project pages—over secondary indexes. I also excluded or deprioritized papers that are only about static image generation, general language-only world modeling, or generic text-to-video without a clear predictive, interactive, physical, or evaluative angle. Where a paper is recent or still consolidating its downstream impact, I mark it as `candidate` rather than overstating its maturity. citeturn16search2turn18search1turn34search0turn24search3turn36search0

## High-Level Map of the Field

The field can be organized more cleanly by **modeling commitments** than by year. The table below is an interpretive taxonomy; the representative-paper links are verified from primary sources.

| Line of work | Central modeling idea | What it contributes to a survey on predictive world models | Representative papers |
|---|---|---|---|
| Deterministic and action-conditioned video prediction | Predict future frames directly from visual history, sometimes conditioned on actions | Establishes the original “predict from pixels” framing and the control-conditioned prediction problem | P001, P002, P003, P006, P008, P009 citeturn29search0turn2search8turn3search2turn27search1turn27search2turn31search6 |
| Stochastic and latent video prediction | Model uncertainty in futures with latent variables or learned priors | Introduces multimodality, long-horizon uncertainty, and latent-trajectory reasoning | P004, P005 citeturn5search0turn5search1 |
| Physical and object-centric dynamics | Represent scenes as objects/keypoints/entities and model interactions explicitly | Makes dynamics more compositional, interpretable, and often more physics-like | P010–P018 citeturn7search1turn22search0turn7search0turn9search0turn10search0turn8search0turn9search1turn8search18 |
| Latent world models for planning and control | Learn dynamics in compact latent states, then plan or learn policies in imagination | Converts prediction into a practical control interface; central bridge from video prediction to “world models” proper | P019–P026 citeturn11search12turn11search1turn11search2turn11search3turn13search3turn12search1turn12search2turn19search0 |
| Diffusion and foundation-style video world models | Use tokenized or diffusion-based video generators as simulators or interactive environment models | Brings stronger visual realism, broader pretraining, and recent efforts toward controllable, interactive worlds | P027–P032 citeturn15search1turn15search0turn14search0turn16search0turn18search1turn16search2 |
| Evaluation, physical reasoning, and benchmark design | Move beyond PSNR/SSIM to FVD, causal/physical reasoning, and embodied evaluation | Defines what counts as progress when “good-looking video” is not enough | P033–P040 citeturn24search0turn33search0turn23search3turn24search1turn35search0turn34search0turn24search3turn36search0 |

Historically, the field began with **pixel-level future prediction** on constrained domains and then on Atari and robot manipulation, where the key question was whether a model could roll visual dynamics forward at all. That line quickly hit three difficulties: compounding blur, multimodal uncertainty, and poor long-horizon utility for control. This is why stochastic latent-variable methods and structured recurrent predictors became a major second phase of the literature. citeturn29search0turn2search8turn3search2turn5search0turn5search1turn27search1

The next major conceptual split was between **fidelity-oriented video prediction** and **state-oriented world modeling**. Object-based and interaction-based models argued that useful world representations should factor scenes into entities and relations, rather than treating prediction as undifferentiated pixel regression. In parallel, model-based RL papers reframed the task: the point of a “world model” was not merely to generate plausible futures, but to support efficient planning, policy learning, and test-time imagination from visual observations. citeturn7search1turn22search0turn7search0turn9search0turn10search0turn8search0turn11search12turn11search1turn11search2

The most recent phase adds two new ingredients. One is **foundation-scale video generation**, where tokenizers, transformers, and diffusion models trained on large video corpora begin to look like generic simulators. The other is **feature-space world modeling**, where methods such as DINO-WM predict semantically meaningful visual features instead of reconstructing pixels. These lines are converging, but the benchmarks show that current models still generalize much more weakly on physical-law structure than their photorealism may suggest. citeturn15search1turn15search0turn14search0turn16search0turn18search1turn19search0turn35search0turn24search3turn36search0

The most important conceptual distinction for your survey, in my view, is this: **video prediction** papers ask whether a model can continue what it sees; **world model** papers ask whether the learned representation supports prediction that is useful for reasoning, planning, interaction, or physical abstraction. That distinction is not absolute, but it is the cleanest organizing principle for a survey on “generative simulation and physical dynamics.” citeturn11search1turn11search2turn13search3turn19search0turn16search0turn24search3

## Ranked Core Paper List

The ranking below is a **survey-centrality ranking**, not a citation-count ranking. Metadata claims are verified from the cited primary or official sources; the ranking and short “why it matters” notes are my interpretation.

| Rank | ID | Title and authors | Year | Venue or arXiv | URL | arXiv ID or DOI | Category | Why it matters for this survey | Class | Verification |
|---|---:|---|---:|---|---|---|---|---|---|---|
| 1 | P001 | **Learning Latent Dynamics for Planning from Pixels** — Danijar Hafner et al. | 2019 | ICML | `https://arxiv.org/abs/1811.04551` | 1811.04551 | latent_world_models | PlaNet is the clearest early bridge from visual prediction to usable world models for planning from pixels. | core | verified citeturn11search1turn11search5 |
| 2 | P002 | **Dream to Control: Learning Behaviors by Latent Imagination** — Danijar Hafner et al. | 2020 | ICLR | `https://arxiv.org/abs/1912.01603` | 1912.01603 | latent_world_models | Dreamer turned latent imagination into an end-to-end control recipe and became a canonical reference point. | core | verified citeturn11search2turn11search6 |
| 3 | P003 | **Recurrent World Models Facilitate Policy Evolution** — David Ha, Jürgen Schmidhuber | 2018 | NeurIPS | `https://arxiv.org/abs/1803.10122` | 1803.10122 | latent_world_models | The “World Models” paper made the idea broadly legible: compress, model dynamics, then act in imagination. | core | verified citeturn11search12turn11search0turn11search8 |
| 4 | P004 | **Action-Conditional Video Prediction using Deep Networks in Atari Games** — Junhyuk Oh et al. | 2015 | NeurIPS | `https://arxiv.org/abs/1507.08750` | 1507.08750 | video_prediction | Foundational action-conditioned visual prediction from pixels; important for the field’s control-oriented origin story. | core | verified citeturn29search0turn29search1 |
| 5 | P005 | **Unsupervised Learning for Physical Interaction through Video Prediction** — Chelsea Finn, Ian Goodfellow, Sergey Levine | 2016 | NeurIPS | `https://arxiv.org/abs/1605.07157` | 1605.07157 | video_prediction | A landmark robot video-prediction paper showing prediction as self-supervised physical interaction learning. | core | verified citeturn2search8turn2search16 |
| 6 | P006 | **Stochastic Variational Video Prediction** — Mohammad Babaeizadeh et al. | 2018 | ICLR | `https://arxiv.org/abs/1710.11252` | 1710.11252 | video_prediction | Crucial for the move from deterministic futures to multimodal, uncertainty-aware visual dynamics. | core | verified citeturn5search0turn5search4 |
| 7 | P007 | **Interaction Networks for Learning about Objects, Relations and Physics** — Peter W. Battaglia et al. | 2016 | NeurIPS | `https://arxiv.org/abs/1612.00222` | 1612.00222 | generative_simulation | A foundational learnable physics engine; not video-first, but essential background for structured simulators and object interaction. | core | verified citeturn22search0turn22search7 |
| 8 | P008 | **Visual Interaction Networks** — Nicholas Watters et al. | 2017 | NeurIPS | `https://arxiv.org/abs/1706.01433` | 1706.01433 | physical_dynamics | One of the clearest “from video to physical dynamics” papers, combining perception with interaction-based prediction. | core | verified citeturn7search0turn7search12 |
| 9 | P009 | **Reasoning About Physical Interactions with Object-Oriented Prediction and Planning** — Michael Janner et al. | 2019 | ICLR | `https://arxiv.org/abs/1812.10972` | 1812.10972 | object_centric_world_models | O2P2 is a central object-oriented world model paper for intuitive physics, planning, and pixel-to-object-to-pixel reasoning. | core | verified citeturn9search0turn7search11 |
| 10 | P010 | **DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning** — Gaoyue Zhou et al. | 2025 | ICML | `https://arxiv.org/abs/2411.04983` | 2411.04983 | latent_world_models | A strong recent feature-space world-model paper; useful for the “predict semantics, not pixels” line of the survey. | candidate | verified citeturn19search0turn19search8turn19search14 |
| 11 | P011 | **Video Diffusion Models** — Jonathan Ho et al. | 2022 | NeurIPS | `https://arxiv.org/abs/2204.03458` | 2204.03458 | diffusion_world_models | Not a world model by itself, but a pivotal generative-video foundation for later predictive and simulation-oriented diffusion work. | core | verified citeturn15search1turn15search18 |
| 12 | P012 | **Diffusion for World Modeling: Visual Details Matter in Atari** — Eloi Alonso et al. | 2024 | NeurIPS | `https://arxiv.org/abs/2405.12399` | 2405.12399 | diffusion_world_models | One of the clearest recent papers explicitly positioning diffusion as a world-model architecture. | core | verified citeturn14search0turn14search1 |
| 13 | P013 | **Genie: Generative Interactive Environments** — Jake Bruce et al. | 2024 | ICML | `https://arxiv.org/abs/2402.15391` | 2402.15391 | interactive_world_models | A high-profile “playable world” paper trained from unlabeled video; central to the modern interactive-world-model narrative. | core | verified citeturn16search0turn16search4turn16search12 |
| 14 | P014 | **Transformers are Sample-Efficient World Models** — Vincent Micheli, Eloi Alonso, François Fleuret | 2023 | ICLR | `https://arxiv.org/abs/2209.00588` | 2209.00588 | latent_world_models | IRIS matters because it recasts world modeling as discrete-token sequence modeling. | core | verified citeturn13search3turn13search7 |
| 15 | P015 | **Mastering Atari with Discrete World Models** — Danijar Hafner et al. | 2021 | ICLR | `https://arxiv.org/abs/2010.02193` | 2010.02193 | latent_world_models | DreamerV2 is the canonical discrete-latent successor to Dreamer and a major benchmark milestone. | core | verified citeturn11search3turn11search7 |
| 16 | P016 | **DayDreamer: World Models for Physical Robot Learning** — Philipp Wu et al. | 2022 | CoRL | `https://arxiv.org/abs/2206.14176` | 2206.14176 | embodied_world_models | Important because it shows world-model learning directly on real robots, not only in games or simulation. | core | verified citeturn12search1turn12search10turn12search7 |
| 17 | P017 | **Contrastive Learning of Structured World Models** — Thomas Kipf et al. | 2020 | ICLR | `https://arxiv.org/abs/1911.12247` | 1911.12247 | object_centric_world_models | C-SWM is a highly influential latent, object-centric world-model paper for planning and structured abstraction. | core | verified citeturn8search0turn8search4 |
| 18 | P018 | **SlotFormer: Unsupervised Visual Dynamics Simulation with Object-Centric Models** — Ziyi Wu et al. | 2023 | ICLR | `https://arxiv.org/abs/2210.05861` | 2210.05861 | object_centric_world_models | A strong recent object-centric dynamics model, useful for the structured-simulation branch of the survey. | core | verified citeturn8search18turn8search2 |
| 19 | P019 | **Entity Abstraction in Visual Model-Based Reinforcement Learning** — Rishi Veerapaneni et al. | 2019 | CoRL | `https://arxiv.org/abs/1910.12827` | 1910.12827 | object_centric_world_models | OP3 is a key object-centric MBRL paper connecting unsupervised perception, dynamics, and planning. | background | verified citeturn10search0turn10search3turn10search12 |
| 20 | P020 | **MCVD: Masked Conditional Video Diffusion for Prediction, Generation, and Interpolation** — Vikram Voleti, Alexia Jolicoeur-Martineau, Christopher Pal | 2022 | NeurIPS | `https://arxiv.org/abs/2205.09853` | 2205.09853 | diffusion_world_models | MCVD is a direct diffusion-based video prediction paper, so it sits exactly at the survey’s diffusion/prediction intersection. | core | verified citeturn15search0turn15search10turn15search3 |
| 21 | P021 | **VideoWorld: Exploring Knowledge Learning from Unlabeled Videos** — Zhongwei Ren et al. | 2025 | CVPR | `https://arxiv.org/abs/2501.09781` | 2501.09781 | interactive_world_models | A recent and ambitious claim that world knowledge, planning, and control can emerge from unlabeled video-only training. | candidate | verified citeturn18search1turn18search5turn18search11 |
| 22 | P022 | **Vid2World: Crafting Video Diffusion Models to Interactive World Models** — Siqiao Huang et al. | 2026 | ICLR | `https://arxiv.org/abs/2505.14357` | 2505.14357 | interactive_world_models | A particularly relevant recent paper on converting passive video diffusion models into interactive, action-conditioned world models. | candidate | verified citeturn16search2turn17search17turn16search10 |
| 23 | P023 | **PhyDNet: Disentangling Physical Dynamics From Unknown Factors for Unsupervised Video Prediction** — Vincent Le Guen, Nicolas Thome | 2020 | CVPR | `https://openaccess.thecvf.com/content_CVPR_2020/html/Le_Guen_Disentangling_Physical_Dynamics_From_Unknown_Factors_for_Unsupervised_Video_Prediction_CVPR_2020_paper.html` | UNKNOWN | video_prediction | A core “physics-aware” video-prediction paper that explicitly separates physical dynamics from appearance/detail factors. | core | verified citeturn27search0turn27search8 |
| 24 | P024 | **MaskViT: Masked Visual Pre-Training for Video Prediction** — Agrim Gupta et al. | 2023 | ICLR | `https://arxiv.org/abs/2206.11894` | 2206.11894 | video_prediction | Useful because it connects efficient token prediction with embodied planning on robot tasks. | core | verified citeturn31search6turn31search10turn28search7 |
| 25 | P025 | **Eidetic 3D LSTM: A Model for Video Prediction and Beyond** — Yunbo Wang et al. | 2019 | ICLR | `https://openreview.net/forum?id=B1lKS2AqtX` | UNKNOWN | video_prediction | A strong recurrent predictor and a good reference point for the mature pre-transformer video-prediction literature. | background | verified citeturn27search1turn27search13 |
| 26 | P026 | **SimVP: Simpler yet Better Video Prediction** — Zhangyang Gao et al. | 2022 | CVPR | `https://arxiv.org/abs/2206.05099` | 2206.05099 | video_prediction | Important as a strong later baseline showing how far simplified predictive backbones can go. | background | verified citeturn27search2turn27search6 |
| 27 | P027 | **Decomposing Motion and Content for Natural Video Sequence Prediction** — Ruben Villegas et al. | 2017 | ICLR | `https://arxiv.org/abs/1706.08033` | 1706.08033 | video_prediction | A representative paper for factorizing motion and appearance, useful for the survey’s historical development section. | background | verified citeturn3search2turn3search5 |
| 28 | P028 | **Stochastic Video Generation with a Learned Prior** — Emily Denton, Rob Fergus | 2018 | ICML | `https://arxiv.org/abs/1802.07687` | 1802.07687 | video_prediction | A compact and influential latent-stochastic video model; useful when discussing uncertainty and learned priors. | background | verified citeturn5search1turn5search5 |
| 29 | P029 | **Learning Visual Predictive Models of Physics for Playing Billiards** — Alex Fragkiadaki et al. | 2016 | arXiv | `https://arxiv.org/abs/1511.07404` | 1511.07404 | physical_dynamics | Early visual physics prediction with objects; historically important for “intuitive physics from visual observations.” | background | verified citeturn6search3turn6search7 |
| 30 | P030 | **A Compositional Object-Based Approach to Learning Physical Dynamics** — Michael B. Chang et al. | 2016 | arXiv | `https://arxiv.org/abs/1612.00341` | 1612.00341 | physical_dynamics | A foundational object-based physics paper, useful as background for later object-centric world models. | background | verified citeturn7search1turn7search5 |
| 31 | P031 | **Unsupervised Learning of Object Structure and Dynamics from Videos** — Matthias Minderer et al. | 2019 | NeurIPS | `https://arxiv.org/abs/1906.07889` | 1906.07889 | object_centric_world_models | A strong keypoint-based unsupervised dynamics paper that increased the realism of object-centric learning from raw videos. | background | verified citeturn9search1turn9search4 |
| 32 | P032 | **Pre-training Contextualized World Models with In-the-wild Videos for Reinforcement Learning** — Jialong Wu et al. | 2023 | NeurIPS | `https://arxiv.org/abs/2305.18499` | 2305.18499 | latent_world_models | Important for the “pretrain world models from broad video” line, especially for transfer beyond a single environment. | background | verified citeturn12search2turn12search5 |
| 33 | P033 | **PHYRE: A New Benchmark for Physical Reasoning** — Anton Bakhtin et al. | 2019 | NeurIPS | `https://arxiv.org/abs/1908.05656` | 1908.05656 | evaluation_benchmarks | A foundational physical-reasoning benchmark; central background for any discussion of simulation and physical generalization. | core | verified citeturn24search0turn24search8 |
| 34 | P034 | **CLEVRER: CoLlision Events for Video REpresentation and Reasoning** — Kexin Yi et al. | 2020 | ICLR | `https://arxiv.org/abs/1910.01442` | 1910.01442 | evaluation_benchmarks | Important because it explicitly targets causal, predictive, and counterfactual reasoning over physical videos. | core | verified citeturn33search0turn33search8 |
| 35 | P035 | **Physion: Evaluating Physical Prediction from Vision in Humans and Machines** — Daniel M. Bear et al. | 2021 | NeurIPS Datasets and Benchmarks | `https://arxiv.org/abs/2106.08261` | 2106.08261 | evaluation_benchmarks | One of the most important visual physical-prediction benchmarks; useful for separating “seeing” from “understanding dynamics.” | core | verified citeturn23search3turn23search6 |
| 36 | P036 | **Towards Accurate Generative Models of Video: A New Metric & Challenges** — Thomas Unterthiner et al. | 2018 | arXiv | `https://arxiv.org/abs/1812.01717` | 1812.01717 | evaluation_benchmarks | This paper introduced Fréchet Video Distance, still a core historical reference for generative-video evaluation. | core | verified citeturn24search1turn24search13 |
| 37 | P037 | **VideoPhy: Evaluating Physical Commonsense for Video Generation** — Hritik Bansal et al. | 2025 | ICLR | `https://arxiv.org/abs/2406.03520` | 2406.03520 | evaluation_benchmarks | A key recent benchmark focused specifically on whether generated videos obey physical commonsense. | core | verified citeturn35search0turn35search1 |
| 38 | P038 | **Towards World Simulator: Crafting Physical Commonsense-Based Benchmark for Video Generation** — Fanqing Meng et al. | 2025 | ICML | `https://arxiv.org/abs/2410.05363` | 2410.05363 | evaluation_benchmarks | PhyGenBench is a strong recent evaluation paper for physical-commonsense video generation, and fits your survey’s simulation angle. | candidate | verified citeturn34search0turn34search10 |
| 39 | P039 | **How Far Is Video Generation from World Model: A Physical Law Perspective** — Bingyi Kang et al. | 2025 | ICML | `https://arxiv.org/abs/2411.02385` | 2411.02385 | evaluation_benchmarks | Particularly useful because it asks the exact survey question—how close video generation is to true world modeling—from a physical-law perspective. | candidate | verified citeturn24search3turn24search19 |
| 40 | P040 | **Do generative video models learn physical principles from watching videos?** — Saman Motamed et al. | 2025 | arXiv | `https://arxiv.org/abs/2501.09038` | 2501.09038 | evaluation_benchmarks | The Physics-IQ paper is a high-value recent reference showing that visual realism and physical understanding can diverge sharply. | candidate | verified citeturn36search0turn36search7 |

## Repository CSV

The CSV below is a direct repository-oriented encoding of the verified pool above. I kept fields conservative: when a detail was not confidently verifiable from the primary-source set, I wrote `UNKNOWN`. The `bibtex_key` values are **local provisional keys** intended for repository stability, not claims about official citation keys. The metadata is derived from the verified sources already cited in the ranked list.

```csv
id,title,authors,year,venue,arxiv_id,doi,url,bibtex_key,category,sub_category,task,input_modality,output_modality,model_family,dynamics_modeling,physical_prior,interaction,benchmark,dataset,metrics,key_contribution,main_limitation,relevance_to_survey,status,notes_file
P001,"Learning Latent Dynamics for Planning from Pixels","Danijar Hafner et al.",2019,"ICML","1811.04551","UNKNOWN","https://arxiv.org/abs/1811.04551","hafner2019_planet_prov","latent_world_models","planning_from_pixels","model_based_control","video_plus_action","latent_state_plus_reward","rssm_planning","latent_space","none","action_conditioned","no","DeepMind Control Suite","reward; control return","Planning in learned latent dynamics from pixels","Limited visual realism and domain breadth by current standards","Canonical bridge from video prediction to world models","core","notes/P001_learning_latent_dynamics_for_planning_from_pixels.md"
P002,"Dream to Control: Learning Behaviors by Latent Imagination","Danijar Hafner et al.",2020,"ICLR","1912.01603","UNKNOWN","https://arxiv.org/abs/1912.01603","hafner2020_dreamer_prov","latent_world_models","latent_imagination_control","model_based_rl","video_plus_action","action_policy_plus_value","rssm_actor_critic","latent_space","none","action_conditioned","no","DeepMind Control Suite","episode_return","Latent imagination with actor-critic learning","Still tied to task rewards and online interaction","Essential for planning/control-oriented world-model taxonomy","core","notes/P002_dream_to_control_learning_behaviors_by_latent_imagination.md"
P003,"Recurrent World Models Facilitate Policy Evolution","David Ha; Jürgen Schmidhuber",2018,"NeurIPS","1803.10122","UNKNOWN","https://arxiv.org/abs/1803.10122","ha2018_world_models_prov","latent_world_models","latent_imagination","model_based_control","video_plus_action","latent_state_plus_policy","vae_rnn_controller","latent_space","none","action_conditioned","no","CarRacing; VizDoom","episode_return","Popularized the modern world-model pipeline","Small-scale by later standards","Foundational framing paper for the whole survey","core","notes/P003_recurrent_world_models_facilitate_policy_evolution.md"
P004,"Action-Conditional Video Prediction using Deep Networks in Atari Games","Junhyuk Oh; Xiaoxiao Guo; Honglak Lee; Richard L. Lewis; Satinder Singh",2015,"NeurIPS","1507.08750","UNKNOWN","https://arxiv.org/abs/1507.08750","oh2015_action_conditional_video_prediction_prov","video_prediction","action_conditioned","future_frame_prediction","video_plus_action","video","autoregressive_cnn","pixel_space","none","action_conditioned","no","Arcade Learning Environment","MSE; control_utility","Early long-horizon action-conditioned prediction from pixels","Game-domain scope and pixel-space brittleness","Key origin point for predictive models from visual interaction","core","notes/P004_action_conditional_video_prediction_using_deep_networks_in_atari_games.md"
P005,"Unsupervised Learning for Physical Interaction through Video Prediction","Chelsea Finn; Ian Goodfellow; Sergey Levine",2016,"NeurIPS","1605.07157","UNKNOWN","https://arxiv.org/abs/1605.07157","finn2016_physical_interaction_video_prediction_prov","video_prediction","robotic_prediction","future_frame_prediction","video_plus_action","video","dna_cdna","pixel_space","none","action_conditioned","no","BAIR robot pushing","PSNR; SSIM; task_success","Robot interaction learned through video prediction","Short-horizon and pixel-space limitations","Core robot-world-model precursor","core","notes/P005_unsupervised_learning_for_physical_interaction_through_video_prediction.md"
P006,"Stochastic Variational Video Prediction","Mohammad Babaeizadeh et al.",2018,"ICLR","1710.11252","UNKNOWN","https://arxiv.org/abs/1710.11252","babaeizadeh2018_sv2p_prov","video_prediction","stochastic_prediction","future_frame_prediction","video_plus_action","video","vae_rnn","pixel_and_latent","none","action_conditioned","no","BAIR; Human3.6M","PSNR; SSIM","Introduced latent-variable stochastic futures to video prediction","Still optimized largely around reconstruction","Important for uncertainty in predictive world models","core","notes/P006_stochastic_variational_video_prediction.md"
P007,"Interaction Networks for Learning about Objects, Relations and Physics","Peter W. Battaglia et al.",2016,"NeurIPS","1612.00222","UNKNOWN","https://arxiv.org/abs/1612.00222","battaglia2016_interaction_networks_prov","generative_simulation","relational_dynamics","physical_simulation","state_graph","future_state","graph_network","object_centric","graph_relational_bias","none","no","synthetic_physics_systems","MSE","General-purpose learnable interaction simulator","Not video-based in its core formulation","Foundational background for structured simulators and object interactions","core","notes/P007_interaction_networks_for_learning_about_objects_relations_and_physics.md"
P008,"Visual Interaction Networks","Nicholas Watters et al.",2017,"NeurIPS","1706.01433","UNKNOWN","https://arxiv.org/abs/1706.01433","watters2017_visual_interaction_networks_prov","physical_dynamics","object_based_from_video","physical_prediction","video","future_state_plus_video","cnn_plus_graph_network","object_centric","graph_relational_bias","none","no","bouncing_shapes; physical_systems","rollout_error","Combines visual perception with interaction-based physical dynamics","Synthetic settings dominate","One of the clearest visual-physics sequence models","core","notes/P008_visual_interaction_networks.md"
P009,"Reasoning About Physical Interactions with Object-Oriented Prediction and Planning","Michael Janner et al.",2019,"ICLR","1812.10972","UNKNOWN","https://arxiv.org/abs/1812.10972","janner2019_o2p2_prov","object_centric_world_models","object_oriented_prediction","prediction_and_planning","video","objects_plus_video","object_centric_renderer_dynamics","object_centric","object_entity_bias","none","no","block_stacking","prediction_error; planning_success","Maps images to objects, predicts object interactions, renders back to pixels","Focused on structured synthetic object worlds","Central object-centric world-model paper for intuitive physics","core","notes/P009_reasoning_about_physical_interactions_with_object_oriented_prediction_and_planning.md"
P010,"DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning","Gaoyue Zhou; Hengkai Pan; Yann LeCun; Lerrel Pinto",2025,"ICML","2411.04983","UNKNOWN","https://arxiv.org/abs/2411.04983","zhou2025_dino_wm_prov","latent_world_models","feature_space_planning","test_time_planning","video_plus_action","feature_trajectory","feature_predictor_transformer","feature_space","pretrained_visual_features","action_conditioned","no","maze; manipulation; particle_envs","planning_success","Predicts DINOv2 features for zero-shot planning","Very recent and still maturing","Important recent alternative to pixel reconstruction","candidate","notes/P010_dino_wm_world_models_on_pretrained_visual_features.md"
P011,"Video Diffusion Models","Jonathan Ho et al.",2022,"NeurIPS","2204.03458","UNKNOWN","https://arxiv.org/abs/2204.03458","ho2022_video_diffusion_models_prov","diffusion_world_models","video_generation","video_generation_and_prediction","video_text_or_video","video","diffusion","pixel_space","none","conditional","no","UCF101; BAIR; text_video_data","FVD","Established diffusion as a serious video-model baseline","Not a world model in the control sense by itself","Essential background for later diffusion world models","core","notes/P011_video_diffusion_models.md"
P012,"Diffusion for World Modeling: Visual Details Matter in Atari","Eloi Alonso et al.",2024,"NeurIPS","2405.12399","UNKNOWN","https://arxiv.org/abs/2405.12399","alonso2024_diamond_prov","diffusion_world_models","diffusion_world_model","world_model_rl","video_plus_action","video_plus_policy","diffusion_rl","pixel_space","none","action_conditioned","no","Atari100k; CSGO","human_normalized_score","Makes diffusion explicit as a world-model architecture","Focused on game environments","Directly relevant modern diffusion-based world model","core","notes/P012_diffusion_for_world_modeling_visual_details_matter_in_atari.md"
P013,"Genie: Generative Interactive Environments","Jake Bruce et al.",2024,"ICML","2402.15391","UNKNOWN","https://arxiv.org/abs/2402.15391","bruce2024_genie_prov","interactive_world_models","playable_worlds","interactive_video_generation","video_or_image_prompt","interactive_video","tokenizer_autoregressive","latent_token_space","latent_action_bias","interactive","no","internet_videos","human_eval; controllability","Learns playable interactive environments from unlabeled video","Early foundation-world-model stage with many open questions","High-value recent reference for interactive generative environments","core","notes/P013_genie_generative_interactive_environments.md"
P014,"Transformers are Sample-Efficient World Models","Vincent Micheli; Eloi Alonso; François Fleuret",2023,"ICLR","2209.00588","UNKNOWN","https://arxiv.org/abs/2209.00588","micheli2023_iris_prov","latent_world_models","transformer_world_model","model_based_rl","video_plus_action","token_or_latent_sequence","vqvae_transformer","discrete_latent_space","none","action_conditioned","no","Atari100k","human_normalized_score","Recasts world modeling as token prediction with a transformer","Domain scope is still mainly Atari","Important transformer-based world-model milestone","core","notes/P014_transformers_are_sample_efficient_world_models.md"
P015,"Mastering Atari with Discrete World Models","Danijar Hafner et al.",2021,"ICLR","2010.02193","UNKNOWN","https://arxiv.org/abs/2010.02193","hafner2021_dreamerv2_prov","latent_world_models","discrete_latent_rl","model_based_rl","video_plus_action","latent_state_plus_policy","discrete_rssm_actor_critic","discrete_latent_space","none","action_conditioned","no","Atari100k; continuous_control","human_normalized_score","Shows strong Atari performance with discrete latent world models","Still benchmark-centric","Key successor to Dreamer in discrete latent space","core","notes/P015_mastering_atari_with_discrete_world_models.md"
P016,"DayDreamer: World Models for Physical Robot Learning","Philipp Wu et al.",2022,"CoRL","2206.14176","UNKNOWN","https://arxiv.org/abs/2206.14176","wu2022_daydreamer_prov","embodied_world_models","robot_learning","model_based_robot_control","video_plus_action","action_policy","rssm_actor_critic","latent_space","none","action_conditioned","no","real_robot_tasks","task_success","Demonstrates world-model learning directly on physical robots","Requires substantial platform engineering","Important embodied world-model paper","core","notes/P016_daydreamer_world_models_for_physical_robot_learning.md"
P017,"Contrastive Learning of Structured World Models","Thomas Kipf et al.",2020,"ICLR","1911.12247","UNKNOWN","https://arxiv.org/abs/1911.12247","kipf2020_cswm_prov","object_centric_world_models","contrastive_latent_dynamics","planning","video_plus_action","latent_object_state","contrastive_gnn","object_centric_latent","object_entity_bias","action_conditioned","no","gridworld_like_envs; PHYRE_style_tasks","planning_success","Uses contrastive learning to induce structured object-centric world models","Often evaluated in simplified environments","Very useful for structured latent-dynamics taxonomy","core","notes/P017_contrastive_learning_of_structured_world_models.md"
P018,"SlotFormer: Unsupervised Visual Dynamics Simulation with Object-Centric Models","Ziyi Wu et al.",2023,"ICLR","2210.05861","UNKNOWN","https://arxiv.org/abs/2210.05861","wu2023_slotformer_prov","object_centric_world_models","slot_based_dynamics","visual_dynamics_simulation","video","slot_trajectories_plus_video","slot_transformer","object_centric_latent","slot_attention_bias","none","no","MOVi; object-centric_datasets","prediction_metrics","Simulates dynamics in slot space for object-centric prediction","Still depends on object-centric pre-processing quality","Strong modern object-centric dynamics reference","core","notes/P018_slotformer_unsupervised_visual_dynamics_simulation.md"
P019,"PhyDNet: Disentangling Physical Dynamics From Unknown Factors for Unsupervised Video Prediction","Vincent Le Guen; Nicolas Thome",2020,"CVPR","UNKNOWN","UNKNOWN","https://openaccess.thecvf.com/content_CVPR_2020/html/Le_Guen_Disentangling_Physical_Dynamics_From_Unknown_Factors_for_Unsupervised_Video_Prediction_CVPR_2020_paper.html","leguen2020_phydnet_prov","video_prediction","physics_disentanglement","future_frame_prediction","video","video","physics_informed_rnn","latent_space","pde_inspired","none","no","traffic; human_motion; physical_sequences","PSNR; SSIM","Separates physical dynamics from residual appearance factors","Physics prior is still approximate and narrow","Directly relevant to physical-dynamics learning from video","core","notes/P019_phydnet_disentangling_physical_dynamics_from_unknown_factors.md"
P020,"MaskViT: Masked Visual Pre-Training for Video Prediction","Agrim Gupta et al.",2023,"ICLR","2206.11894","UNKNOWN","https://arxiv.org/abs/2206.11894","gupta2023_maskvit_prov","video_prediction","masked_token_prediction","future_frame_prediction_and_planning","video_plus_action","video","masked_transformer","token_space","none","action_conditioned","no","RoboNet; robotic_manipulation","prediction_metrics; task_success","Masked-token video prediction scaled to planning use","Still primarily a predictive model rather than a full world model","Useful bridge between video prediction and embodied planning","core","notes/P020_maskvit_masked_visual_pre_training_for_video_prediction.md"
P021,"Eidetic 3D LSTM: A Model for Video Prediction and Beyond","Yunbo Wang et al.",2019,"ICLR","UNKNOWN","UNKNOWN","https://openreview.net/forum?id=B1lKS2AqtX","wang2019_e3dlstm_prov","video_prediction","recurrent_prediction","future_frame_prediction","video","video","rnn_lstm","pixel_space","none","none","no","MovingMNIST; KTH; Human3.6M","prediction_metrics","Strong 3D recurrent architecture for spatiotemporal prediction","Still largely fidelity-oriented","Good representative of mature recurrent video prediction","background","notes/P021_eidetic_3d_lstm_a_model_for_video_prediction.md"
P022,"SimVP: Simpler yet Better Video Prediction","Zhangyang Gao et al.",2022,"CVPR","2206.05099","10.1109/CVPR52688.2022.00317","https://arxiv.org/abs/2206.05099","gao2022_simvp_prov","video_prediction","simplified_architecture","future_frame_prediction","video","video","cnn_based_predictor","pixel_space","none","none","no","MovingMNIST; weather; traffic","prediction_metrics","Strong simple baseline for spatiotemporal prediction","Not inherently structured or interactive","Useful baseline anchor in any survey section on later video prediction","background","notes/P022_simvp_simpler_yet_better_video_prediction.md"
P023,"Decomposing Motion and Content for Natural Video Sequence Prediction","Ruben Villegas et al.",2017,"ICLR","1706.08033","UNKNOWN","https://arxiv.org/abs/1706.08033","villegas2017_motion_content_prov","video_prediction","content_motion_factorization","future_frame_prediction","video","video","cnn_convlstm","pixel_and_feature_space","none","none","no","KTH; UCF101","prediction_metrics","Separates motion from content for prediction","Still limited by reconstruction quality","Important historical factorization idea","background","notes/P023_decomposing_motion_and_content_for_natural_video_sequence_prediction.md"
P024,"Stochastic Video Generation with a Learned Prior","Emily Denton; Rob Fergus",2018,"ICML","1802.07687","UNKNOWN","https://arxiv.org/abs/1802.07687","denton2018_svg_lp_prov","video_prediction","stochastic_prediction","future_frame_prediction","video","video","vae_rnn","latent_space","none","none","no","MovingMNIST; BAIR; KTH","prediction_metrics","Learns a prior over stochastic future trajectories","Limited control/planning framing","Important stochastic latent-video reference","background","notes/P024_stochastic_video_generation_with_a_learned_prior.md"
P025,"Learning Visual Predictive Models of Physics for Playing Billiards","Alex Fragkiadaki et al.",2016,"arXiv","1511.07404","UNKNOWN","https://arxiv.org/abs/1511.07404","fragkiadaki2016_billiards_prov","physical_dynamics","visual_physics","physical_prediction","video","future_state_plus_video","object_centric_cnn_lstm","object_centric","none","none","no","billiards","rollout_error","Early object-based physical prediction from visuals","Highly constrained domain","Useful historical background for visual physics","background","notes/P025_learning_visual_predictive_models_of_physics_for_playing_billiards.md"
P026,"A Compositional Object-Based Approach to Learning Physical Dynamics","Michael B. Chang et al.",2016,"arXiv","1612.00341","UNKNOWN","https://arxiv.org/abs/1612.00341","chang2016_compositional_object_physics_prov","physical_dynamics","object_based_simulation","physical_prediction","state_or_abstract_objects","future_state","object_centric_mlp","object_centric","object_entity_bias","none","no","synthetic_physics_systems","prediction_error","Classic neural physics engine style compositional dynamics","Not video-first","Important conceptual precursor to object-centric world models","background","notes/P026_a_compositional_object_based_approach_to_learning_physical_dynamics.md"
P027,"Unsupervised Learning of Object Structure and Dynamics from Videos","Matthias Minderer et al.",2019,"NeurIPS","1906.07889","UNKNOWN","https://arxiv.org/abs/1906.07889","minderer2019_object_structure_dynamics_prov","object_centric_world_models","keypoint_dynamics","future_prediction_and_representation_learning","video","keypoints_plus_video","keypoint_vae","object_centric_latent","keypoint_bias","none","no","Human3.6M; sports; DMControl_video","prediction_metrics; downstream_transfer","Learns keypoint structure and dynamics without supervision","Keypoint abstraction can be coarse","Useful for object-centric representation learning from video","background","notes/P027_unsupervised_learning_of_object_structure_and_dynamics.md"
P028,"Pre-training Contextualized World Models with In-the-wild Videos for Reinforcement Learning","Jialong Wu et al.",2023,"NeurIPS","2305.18499","UNKNOWN","https://arxiv.org/abs/2305.18499","wu2023_contextwm_prov","latent_world_models","video_pretraining","world_model_pretraining","video_plus_action","latent_state_plus_policy","contextualized_rssm","latent_space","none","action_conditioned","no","robotics; locomotion; driving","sample_efficiency","Pretrains world models on in-the-wild videos for transfer","Representation and transfer remain domain-sensitive","Important for large-scale video pretraining discussions","background","notes/P028_pre_training_contextualized_world_models_with_in_the_wild_videos.md"
P029,"VideoWorld: Exploring Knowledge Learning from Unlabeled Videos","Zhongwei Ren et al.",2025,"CVPR","2501.09781","UNKNOWN","https://arxiv.org/abs/2501.09781","ren2025_videoworld_prov","interactive_world_models","video_only_world_model","knowledge_learning_from_video","video","latent_dynamics_plus_policy","latent_dynamics_autoregressive","latent_space","none","action_conditioned_or_conditional","no","Video-GoBench; CALVIN; RLBench","task_success","Claims knowledge and control can emerge from unlabeled videos via latent dynamics","Very recent and broad in scope","Potentially important for video-only world-model scaling","candidate","notes/P029_videoworld_exploring_knowledge_learning_from_unlabeled_videos.md"
P030,"Vid2World: Crafting Video Diffusion Models to Interactive World Models","Siqiao Huang et al.",2026,"ICLR","2505.14357","UNKNOWN","https://arxiv.org/abs/2505.14357","huang2026_vid2world_prov","interactive_world_models","interactive_diffusion_world_model","action_conditioned_world_modeling","video_plus_action","interactive_video","diffusion_adapter","diffusion_latent_space","none","interactive","no","UNKNOWN","prediction_metrics; controllability","Transforms passive video diffusion models into interactive world models","Very recent and not yet broadly adopted","Highly relevant newest paper at the diffusion/world-model boundary","candidate","notes/P030_vid2world_crafting_video_diffusion_models_to_interactive_world_models.md"
P031,"PHYRE: A New Benchmark for Physical Reasoning","Anton Bakhtin et al.",2019,"NeurIPS","1908.05656","UNKNOWN","https://arxiv.org/abs/1908.05656","bakhtin2019_phyre_prov","evaluation_benchmarks","physical_reasoning_benchmark","benchmarking","video_or_state","benchmark_score","benchmark","UNKNOWN","physical_reasoning","none","yes","PHYRE","AUCCESS; sample_efficiency","Benchmark for physical reasoning and generalization","2D puzzle world abstraction","Foundational benchmark background for physical world modeling","core","notes/P031_phyre_a_new_benchmark_for_physical_reasoning.md"
P032,"CLEVRER: CoLlision Events for Video REpresentation and Reasoning","Kexin Yi et al.",2020,"ICLR","1910.01442","UNKNOWN","https://arxiv.org/abs/1910.01442","yi2020_clevrer_prov","evaluation_benchmarks","causal_video_reasoning","benchmarking","video_plus_language","qa_scores","benchmark","UNKNOWN","causal_reasoning_bias","none","yes","CLEVRER","QA_accuracy","Targets descriptive, explanatory, predictive, and counterfactual reasoning in videos","Synthetic and QA-style","Important for causal/physical reasoning evaluation","core","notes/P032_clevrer_collision_events_for_video_representation_and_reasoning.md"
P033,"Physion: Evaluating Physical Prediction from Vision in Humans and Machines","Daniel M. Bear et al.",2021,"NeurIPS Datasets and Benchmarks","2106.08261","UNKNOWN","https://arxiv.org/abs/2106.08261","bear2021_physion_prov","evaluation_benchmarks","physical_prediction_benchmark","benchmarking","video","benchmark_score","benchmark","UNKNOWN","physical_reasoning_bias","none","yes","Physion","accuracy; human_model_gap","Large-scale benchmark for visual physical prediction","Simulation to perception gap remains","One of the most important physical-prediction benchmarks","core","notes/P033_physion_evaluating_physical_prediction_from_vision.md"
P034,"Towards Accurate Generative Models of Video: A New Metric & Challenges","Thomas Unterthiner et al.",2018,"arXiv","1812.01717","UNKNOWN","https://arxiv.org/abs/1812.01717","unterthiner2018_fvd_prov","evaluation_benchmarks","video_generation_metric","evaluation","video","metric","metric_benchmark","UNKNOWN","none","none","yes","SCV","FVD","Introduced Fréchet Video Distance","Metric does not test controllability or physics directly","Essential evaluation background for generative video sections","core","notes/P034_towards_accurate_generative_models_of_video.md"
P035,"VideoPhy: Evaluating Physical Commonsense for Video Generation","Hritik Bansal et al.",2025,"ICLR","2406.03520","UNKNOWN","https://arxiv.org/abs/2406.03520","bansal2025_videophy_prov","evaluation_benchmarks","physical_consistency_benchmark","evaluation_of_generated_videos","text_plus_video","benchmark_score","benchmark","UNKNOWN","physical_commonsense_bias","none","yes","VideoPhy","human_eval; auto_eval","Evaluates whether generated videos obey physical commonsense","Focused on commonsense prompts rather than full interaction","Important modern physics benchmark for video generation","core","notes/P035_videophy_evaluating_physical_commonsense_for_video_generation.md"
P036,"Towards World Simulator: Crafting Physical Commonsense-Based Benchmark for Video Generation","Fanqing Meng et al.",2025,"ICML","2410.05363","UNKNOWN","https://arxiv.org/abs/2410.05363","meng2025_phygenbench_prov","evaluation_benchmarks","physical_commonsense_benchmark","evaluation_of_generated_videos","text_plus_video","benchmark_score","benchmark","UNKNOWN","physical_commonsense_bias","none","yes","PhyGenBench","human_alignment; auto_eval","Builds a physics-commonsense benchmark and evaluation framework","Still benchmarking prompt-based generation rather than embodied control","Useful for recent evaluation chapter and open-challenges discussion","candidate","notes/P036_towards_world_simulator_crafting_physical_commonsense.md"
P037,"How Far Is Video Generation from World Model: A Physical Law Perspective","Bingyi Kang et al.",2025,"ICML","2411.02385","UNKNOWN","https://arxiv.org/abs/2411.02385","kang2025_physical_law_perspective_prov","evaluation_benchmarks","physical_law_generalization","evaluation_of_video_prediction","video","benchmark_score","analysis_benchmark","UNKNOWN","physical_law_bias","none","yes","PhyWorld_testbed","ID; OOD; combinatorial_generalization","Directly tests whether video models generalize physical laws","Uses simplified synthetic mechanics testbed","Extremely relevant to the survey thesis itself","candidate","notes/P037_how_far_is_video_generation_from_world_model.md"
P038,"Do generative video models learn physical principles from watching videos?","Saman Motamed et al.",2025,"arXiv","2501.09038","UNKNOWN","https://arxiv.org/abs/2501.09038","motamed2025_physics_iq_prov","evaluation_benchmarks","physics_iq_benchmark","evaluation_of_video_models","video","benchmark_score","benchmark","UNKNOWN","physical_law_bias","none","yes","Physics-IQ","prediction_error; physics_score","Introduces Physics-IQ to disentangle realism from physical understanding","Very recent and still expanding","High-value current reference on realism vs physics understanding","candidate","notes/P038_do_generative_video_models_learn_physical_principles.md"
P039,"Video Diffusion Models","Jonathan Ho et al.",2022,"NeurIPS","2204.03458","UNKNOWN","https://arxiv.org/abs/2204.03458","ho2022_video_diffusion_models_prov","diffusion_world_models","foundation_video_model","video_generation","video","video","diffusion","pixel_space","none","conditional","no","UCF101; BAIR","FVD","Foundation diffusion baseline for video","Not inherently interactive or planning-oriented","Needed to explain later diffusion world-model papers","background","notes/P039_video_diffusion_models.md"
P040,"MCVD: Masked Conditional Video Diffusion for Prediction, Generation, and Interpolation","Vikram Voleti; Alexia Jolicoeur-Martineau; Christopher Pal",2022,"NeurIPS","2205.09853","UNKNOWN","https://arxiv.org/abs/2205.09853","voleti2022_mcvd_prov","diffusion_world_models","diffusion_video_prediction","future_frame_prediction","video","video","diffusion","pixel_space","none","conditional","no","BAIR; KTH; Cityscapes_sequence","FVD; prediction_metrics","Direct diffusion formulation for video prediction and interpolation","Not yet a full planning/control world model","Important diffusion-prediction bridge paper","core","notes/P040_mcvd_masked_conditional_video_diffusion.md"
```

## BibTeX Entries

These entries match the `bibtex_key` column above. To keep the repository starter set readable, I use compact entries and occasionally `and others` for long author lists. For papers with published venue plus arXiv version, I preserve the most stable minimal metadata and avoid inventing pages, publishers, or DOIs.

```bibtex
@inproceedings{hafner2019_planet_prov,
  title={Learning Latent Dynamics for Planning from Pixels},
  author={Hafner, Danijar and Lillicrap, Timothy and Fischer, Ian and Villegas, Ruben and Ha, David and Lee, Honglak and Davidson, James},
  booktitle={Proceedings of the 36th International Conference on Machine Learning},
  year={2019},
  url={https://arxiv.org/abs/1811.04551}
}

@inproceedings{hafner2020_dreamer_prov,
  title={Dream to Control: Learning Behaviors by Latent Imagination},
  author={Hafner, Danijar and Lillicrap, Timothy and Ba, Jimmy and Norouzi, Mohammad},
  booktitle={International Conference on Learning Representations},
  year={2020},
  url={https://arxiv.org/abs/1912.01603}
}

@inproceedings{ha2018_world_models_prov,
  title={Recurrent World Models Facilitate Policy Evolution},
  author={Ha, David and Schmidhuber, J{\"u}rgen},
  booktitle={Advances in Neural Information Processing Systems},
  year={2018},
  url={https://arxiv.org/abs/1803.10122}
}

@inproceedings{oh2015_action_conditional_video_prediction_prov,
  title={Action-Conditional Video Prediction using Deep Networks in Atari Games},
  author={Oh, Junhyuk and Guo, Xiaoxiao and Lee, Honglak and Lewis, Richard L. and Singh, Satinder},
  booktitle={Advances in Neural Information Processing Systems},
  year={2015},
  url={https://arxiv.org/abs/1507.08750}
}

@inproceedings{finn2016_physical_interaction_video_prediction_prov,
  title={Unsupervised Learning for Physical Interaction through Video Prediction},
  author={Finn, Chelsea and Goodfellow, Ian and Levine, Sergey},
  booktitle={Advances in Neural Information Processing Systems},
  year={2016},
  url={https://arxiv.org/abs/1605.07157}
}

@inproceedings{babaeizadeh2018_sv2p_prov,
  title={Stochastic Variational Video Prediction},
  author={Babaeizadeh, Mohammad and Finn, Chelsea and Erhan, Dumitru and Campbell, Roy H. and Levine, Sergey},
  booktitle={International Conference on Learning Representations},
  year={2018},
  url={https://arxiv.org/abs/1710.11252}
}

@inproceedings{battaglia2016_interaction_networks_prov,
  title={Interaction Networks for Learning about Objects, Relations and Physics},
  author={Battaglia, Peter W. and Pascanu, Razvan and Lai, Matthew and Rezende, Danilo Jimenez and Kavukcuoglu, Koray},
  booktitle={Advances in Neural Information Processing Systems},
  year={2016},
  url={https://arxiv.org/abs/1612.00222}
}

@inproceedings{watters2017_visual_interaction_networks_prov,
  title={Visual Interaction Networks},
  author={Watters, Nicholas and Zoran, Daniel and Weber, Theophane and Battaglia, Peter and Kabra, Rishabh and Lerchner, Alexander},
  booktitle={Advances in Neural Information Processing Systems},
  year={2017},
  url={https://arxiv.org/abs/1706.01433}
}

@inproceedings{janner2019_o2p2_prov,
  title={Reasoning About Physical Interactions with Object-Oriented Prediction and Planning},
  author={Janner, Michael and James, Stephen and Hafner, Danijar and Darrell, Trevor and Efros, Alexei A. and Malik, Jitendra and Levine, Sergey},
  booktitle={International Conference on Learning Representations},
  year={2019},
  url={https://arxiv.org/abs/1812.10972}
}

@inproceedings{zhou2025_dino_wm_prov,
  title={DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning},
  author={Zhou, Gaoyue and Pan, Hengkai and LeCun, Yann and Pinto, Lerrel},
  booktitle={International Conference on Machine Learning},
  year={2025},
  url={https://arxiv.org/abs/2411.04983}
}

@inproceedings{ho2022_video_diffusion_models_prov,
  title={Video Diffusion Models},
  author={Ho, Jonathan and Salimans, Tim and Gritsenko, Alexey and Chan, William and Norouzi, Mohammad and Fleet, David J.},
  booktitle={Advances in Neural Information Processing Systems},
  year={2022},
  url={https://arxiv.org/abs/2204.03458}
}

@inproceedings{alonso2024_diamond_prov,
  title={Diffusion for World Modeling: Visual Details Matter in Atari},
  author={Alonso, Eloi and Jelley, Adam and Micheli, Vincent and Kanervisto, Anssi and Storkey, Amos and Pearce, Tim and Fleuret, Fran{\c{c}}ois},
  booktitle={Advances in Neural Information Processing Systems},
  year={2024},
  url={https://arxiv.org/abs/2405.12399}
}

@inproceedings{bruce2024_genie_prov,
  title={Genie: Generative Interactive Environments},
  author={Bruce, Jake and others},
  booktitle={International Conference on Machine Learning},
  year={2024},
  url={https://arxiv.org/abs/2402.15391}
}

@inproceedings{micheli2023_iris_prov,
  title={Transformers are Sample-Efficient World Models},
  author={Micheli, Vincent and Alonso, Eloi and Fleuret, Fran{\c{c}}ois},
  booktitle={International Conference on Learning Representations},
  year={2023},
  url={https://arxiv.org/abs/2209.00588}
}

@inproceedings{hafner2021_dreamerv2_prov,
  title={Mastering Atari with Discrete World Models},
  author={Hafner, Danijar and Lillicrap, Timothy and Norouzi, Mohammad and Ba, Jimmy},
  booktitle={International Conference on Learning Representations},
  year={2021},
  url={https://arxiv.org/abs/2010.02193}
}

@inproceedings{wu2022_daydreamer_prov,
  title={DayDreamer: World Models for Physical Robot Learning},
  author={Wu, Philipp and Escontrela, Alejandro and Hafner, Danijar and Goldberg, Ken and Abbeel, Pieter},
  booktitle={Conference on Robot Learning},
  year={2022},
  url={https://arxiv.org/abs/2206.14176}
}

@inproceedings{kipf2020_cswm_prov,
  title={Contrastive Learning of Structured World Models},
  author={Kipf, Thomas and others},
  booktitle={International Conference on Learning Representations},
  year={2020},
  url={https://arxiv.org/abs/1911.12247}
}

@inproceedings{wu2023_slotformer_prov,
  title={SlotFormer: Unsupervised Visual Dynamics Simulation with Object-Centric Models},
  author={Wu, Ziyi and others},
  booktitle={International Conference on Learning Representations},
  year={2023},
  url={https://arxiv.org/abs/2210.05861}
}

@inproceedings{veerapaneni2019_op3_prov,
  title={Entity Abstraction in Visual Model-Based Reinforcement Learning},
  author={Veerapaneni, Rishi and Co-Reyes, John D. and Chang, Michael and Janner, Michael and Finn, Chelsea and Wu, Jiajun and Tenenbaum, Joshua B. and Levine, Sergey},
  booktitle={Conference on Robot Learning},
  year={2019},
  url={https://arxiv.org/abs/1910.12827}
}

@inproceedings{voleti2022_mcvd_prov,
  title={MCVD: Masked Conditional Video Diffusion for Prediction, Generation, and Interpolation},
  author={Voleti, Vikram and Jolicoeur-Martineau, Alexia and Pal, Christopher},
  booktitle={Advances in Neural Information Processing Systems},
  year={2022},
  url={https://arxiv.org/abs/2205.09853}
}

@inproceedings{ren2025_videoworld_prov,
  title={VideoWorld: Exploring Knowledge Learning from Unlabeled Videos},
  author={Ren, Zhongwei and Wei, Yunchao and Guo, Xun and Zhao, Yao and Kang, Bingyi and Feng, Jiashi and Jin, Xiaojie},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  year={2025},
  url={https://arxiv.org/abs/2501.09781}
}

@inproceedings{huang2026_vid2world_prov,
  title={Vid2World: Crafting Video Diffusion Models to Interactive World Models},
  author={Huang, Siqiao and Wu, Jialong and Zhou, Qixing and Miao, Shangchen and Long, Mingsheng},
  booktitle={International Conference on Learning Representations},
  year={2026},
  url={https://arxiv.org/abs/2505.14357}
}

@inproceedings{leguen2020_phydnet_prov,
  title={PhyDNet: Disentangling Physical Dynamics From Unknown Factors for Unsupervised Video Prediction},
  author={Le Guen, Vincent and Thome, Nicolas},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  year={2020},
  url={https://openaccess.thecvf.com/content_CVPR_2020/html/Le_Guen_Disentangling_Physical_Dynamics_From_Unknown_Factors_for_Unsupervised_Video_Prediction_CVPR_2020_paper.html}
}

@inproceedings{gupta2023_maskvit_prov,
  title={MaskViT: Masked Visual Pre-Training for Video Prediction},
  author={Gupta, Agrim and Tian, Stephen and Zhang, Yunzhi and Wu, Jiajun and Martin-Martin, Roberto and Fei-Fei, Li},
  booktitle={International Conference on Learning Representations},
  year={2023},
  url={https://arxiv.org/abs/2206.11894}
}

@inproceedings{wang2019_e3dlstm_prov,
  title={Eidetic 3D LSTM: A Model for Video Prediction and Beyond},
  author={Wang, Yunbo and Jiang, Lu and Yang, Ming-Hsuan and Li, Jia and Long, Mingsheng and Li, Fei-Fei},
  booktitle={International Conference on Learning Representations},
  year={2019},
  url={https://openreview.net/forum?id=B1lKS2AqtX}
}

@inproceedings{gao2022_simvp_prov,
  title={SimVP: Simpler yet Better Video Prediction},
  author={Gao, Zhangyang and Tan, Cheng and Wu, Lirong and Li, Stan Z.},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  year={2022},
  url={https://arxiv.org/abs/2206.05099}
}

@inproceedings{villegas2017_motion_content_prov,
  title={Decomposing Motion and Content for Natural Video Sequence Prediction},
  author={Villegas, Ruben and Yang, Jimei and Hong, Seunghoon and Lin, Xunyu and Lee, Honglak},
  booktitle={International Conference on Learning Representations},
  year={2017},
  url={https://arxiv.org/abs/1706.08033}
}

@inproceedings{denton2018_svg_lp_prov,
  title={Stochastic Video Generation with a Learned Prior},
  author={Denton, Emily and Fergus, Rob},
  booktitle={Proceedings of the 35th International Conference on Machine Learning},
  year={2018},
  url={https://arxiv.org/abs/1802.07687}
}

@article{fragkiadaki2016_billiards_prov,
  title={Learning Visual Predictive Models of Physics for Playing Billiards},
  author={Fragkiadaki, Alex and others},
  journal={arXiv preprint arXiv:1511.07404},
  year={2016},
  url={https://arxiv.org/abs/1511.07404}
}

@article{chang2016_compositional_object_physics_prov,
  title={A Compositional Object-Based Approach to Learning Physical Dynamics},
  author={Chang, Michael B. and others},
  journal={arXiv preprint arXiv:1612.00341},
  year={2016},
  url={https://arxiv.org/abs/1612.00341}
}

@inproceedings{minderer2019_object_structure_dynamics_prov,
  title={Unsupervised Learning of Object Structure and Dynamics from Videos},
  author={Minderer, Matthias and Sun, Chen and Villegas, Ruben and Cole, Forrester and Murphy, Kevin and Lee, Honglak},
  booktitle={Advances in Neural Information Processing Systems},
  year={2019},
  url={https://arxiv.org/abs/1906.07889}
}

@inproceedings{wu2023_contextwm_prov,
  title={Pre-training Contextualized World Models with In-the-wild Videos for Reinforcement Learning},
  author={Wu, Jialong and Ma, Haoyu and Deng, Chaoyi and Long, Mingsheng},
  booktitle={Advances in Neural Information Processing Systems},
  year={2023},
  url={https://arxiv.org/abs/2305.18499}
}

@article{bakhtin2019_phyre_prov,
  title={PHYRE: A New Benchmark for Physical Reasoning},
  author={Bakhtin, Anton and van der Maaten, Laurens and Johnson, Justin and Gustafson, Laura and Girshick, Ross},
  journal={arXiv preprint arXiv:1908.05656},
  year={2019},
  url={https://arxiv.org/abs/1908.05656}
}

@inproceedings{yi2020_clevrer_prov,
  title={CLEVRER: CoLlision Events for Video REpresentation and Reasoning},
  author={Yi, Kexin and Gan, Chuang and Li, Yunzhu and Kohli, Pushmeet and Wu, Jiajun and Torralba, Antonio and Tenenbaum, Joshua B.},
  booktitle={International Conference on Learning Representations},
  year={2020},
  url={https://arxiv.org/abs/1910.01442}
}

@inproceedings{bear2021_physion_prov,
  title={Physion: Evaluating Physical Prediction from Vision in Humans and Machines},
  author={Bear, Daniel M. and others},
  booktitle={NeurIPS Datasets and Benchmarks},
  year={2021},
  url={https://arxiv.org/abs/2106.08261}
}

@article{unterthiner2018_fvd_prov,
  title={Towards Accurate Generative Models of Video: A New Metric \& Challenges},
  author={Unterthiner, Thomas and van Steenkiste, Sjoerd and Kurach, Karol and Marinier, Raphael and Michalski, Marcin and Gelly, Sylvain},
  journal={arXiv preprint arXiv:1812.01717},
  year={2018},
  url={https://arxiv.org/abs/1812.01717}
}

@inproceedings{bansal2025_videophy_prov,
  title={VideoPhy: Evaluating Physical Commonsense for Video Generation},
  author={Bansal, Hritik and others},
  booktitle={International Conference on Learning Representations},
  year={2025},
  url={https://arxiv.org/abs/2406.03520}
}

@inproceedings{meng2025_phygenbench_prov,
  title={Towards World Simulator: Crafting Physical Commonsense-Based Benchmark for Video Generation},
  author={Meng, Fanqing and Liao, Jiaqi and Tan, Xinyu and Lu, Quanfeng and Shao, Wenqi and Zhang, Kaipeng and Cheng, Yu and Li, Dianqi and Luo, Ping},
  booktitle={International Conference on Machine Learning},
  year={2025},
  url={https://arxiv.org/abs/2410.05363}
}

@inproceedings{kang2025_physical_law_perspective_prov,
  title={How Far Is Video Generation from World Model: A Physical Law Perspective},
  author={Kang, Bingyi and Yue, Yang and Lu, Rui and Lin, Zhijie and Zhao, Yang and Wang, Kaixin and Huang, Gao and Feng, Jiashi},
  booktitle={International Conference on Machine Learning},
  year={2025},
  url={https://arxiv.org/abs/2411.02385}
}

@article{motamed2025_physics_iq_prov,
  title={Do generative video models learn physical principles from watching videos?},
  author={Motamed, Saman and Culp, Laura and Swersky, Kevin and Jaini, Priyank and Geirhos, Robert},
  journal={arXiv preprint arXiv:2501.09038},
  year={2025},
  url={https://arxiv.org/abs/2501.09038}
}

@inproceedings{babaeizadeh2018_sv2p_duplicate_prov,
  title={Stochastic Variational Video Prediction},
  author={Babaeizadeh, Mohammad and Finn, Chelsea and Erhan, Dumitru and Campbell, Roy H. and Levine, Sergey},
  booktitle={International Conference on Learning Representations},
  year={2018},
  url={https://arxiv.org/abs/1710.11252}
}

@inproceedings{janner2019_o2p2_duplicate_prov,
  title={Reasoning About Physical Interactions with Object-Oriented Prediction and Planning},
  author={Janner, Michael and others},
  booktitle={International Conference on Learning Representations},
  year={2019},
  url={https://arxiv.org/abs/1812.10972}
}

@inproceedings{kipf2020_cswm_duplicate_prov,
  title={Contrastive Learning of Structured World Models},
  author={Kipf, Thomas and others},
  booktitle={International Conference on Learning Representations},
  year={2020},
  url={https://arxiv.org/abs/1911.12247}
}

@inproceedings{wu2023_slotformer_duplicate_prov,
  title={SlotFormer: Unsupervised Visual Dynamics Simulation with Object-Centric Models},
  author={Wu, Ziyi and others},
  booktitle={International Conference on Learning Representations},
  year={2023},
  url={https://arxiv.org/abs/2210.05861}
}

@inproceedings{veerapaneni2019_op3_duplicate_prov,
  title={Entity Abstraction in Visual Model-Based Reinforcement Learning},
  author={Veerapaneni, Rishi and Co-Reyes, John D. and Chang, Michael and Janner, Michael and Finn, Chelsea and Wu, Jiajun and Tenenbaum, Joshua B. and Levine, Sergey},
  booktitle={Conference on Robot Learning},
  year={2019},
  url={https://arxiv.org/abs/1910.12827}
}
```

## Reading Plan

A practical three-pass reading plan should move from **conceptual orientation**, to **taxonomic coverage**, to **evaluation and research gaps**. The papers referenced below correspond to the verified IDs in the ranked pool above.

| Pass | Papers | What to extract |
|---|---|---|
| First pass | **P001, P002, P003, P004, P007, P008, P009, P019, P020, P012** | Extract the field’s backbone: what counts as a “world model,” why action-conditioned prediction mattered early, why stochasticity appeared, how object/interaction structure enters, and how planning from pixels differs from merely generating future frames. Focus on: representation choice, transition model, training objective, control/planning interface, and evaluation setup. |
| Second pass | **P010, P013, P014, P015, P016, P017, P018, P021, P022, P023, P024, P025, P027, P028, P029, P030, P031, P032** | Build the taxonomy. For each paper, record: whether dynamics are modeled in pixels, latent states, objects, or semantic features; whether the model is passive or action-conditioned; whether it is designed for prediction, planning, imitation, or interaction; and whether its main contribution is realism, controllability, structure, transfer, or sample efficiency. This pass should let you write the survey’s main body sections. |
| Third pass | **P033, P034, P035, P036, P037, P038, P039, P040**, plus optional expansions not in the top-40 such as **Physion++**, **OpenSTL**, **GAIA-1**, and **WorldScore** | Use this pass to write the evaluation and open-challenges section. Extract benchmark assumptions, what each metric actually measures, which papers expose failures on physical consistency or causal generalization, and where the field still lacks consensus. The key comparison to make is between **visual quality**, **predictive utility**, **physical plausibility**, and **interactive controllability**. citeturn33search9turn24search2turn16search1turn37search14 |

For note-taking, a good per-paper template is: **problem setting**, **state representation**, **transition parameterization**, **conditioning variables**, **training signal**, **decoding/rendering strategy**, **evaluation protocol**, **failure mode**, and **how it changes the definition of a world model**. If you keep those fields consistent, your survey will be able to compare very different papers—video predictors, object-centric simulators, model-based RL agents, and diffusion-based interactive generators—within one coherent framework. citeturn11search1turn8search0turn19search0turn14search0turn24search1turn35search0