# 目標化文獻核查與擴充建議

## 驗證說明

以下內容對應你要求的四個部分，但我先交代兩個重要原則。第一，**題名、作者、年份、URL、arXiv ID** 皆以可取得的 primary source 為準；如果我無法在本輪 primary-source 檢索中可靠確認，就保留 `UNKNOWN`，不補猜測值。第二，**「why it matters」「which section it should support」「core / background / candidate」** 屬於我的整合判讀，不是論文本身的原始 metadata。你目前稿件也已明確指出：Section 4 的 architecture-oriented baselines、Section 6 的 DreamerV2/IRIS/DayDreamer/DINO-WM/ContextWM、Section 7 的 VideoWorld/Vid2World，以及 Section 8 的 PHYRE/CLEVRER/Physion/PhyGenBench/How Far/Physics-IQ，仍屬 coverage target、incomplete notes 或 metadata-only 狀態。fileciteturn0file0

本次清單除了 reviewer 點名的主軸文獻外，我額外補入三篇我認為高價值的擴充候選：P054、P062、P078。它們分別補強 real-world object-centric video learning、interactive token world models，以及 broader world-generation evaluation，能讓你的 taxonomy 不只停在「物理一致性」單軸，而是更完整地涵蓋 representation、interaction、planning、controllability 與 evaluation。citeturn12academia0turn34academia3turn25academia3

## Missing literature table

以下對應 Part 1。

**Video prediction / visual dynamics baselines**

| ID | Title | Authors | Year | Venue or arXiv | URL | arXiv ID or DOI | Category | Why it matters for this survey | Section support | Priority | Verification |
|---|---|---|---:|---|---|---|---|---|---|---|---|
| P041 | Convolutional LSTM Network: A Machine Learning Approach for Precipitation Nowcasting | Xingjian Shi; Zhourong Chen; Hao Wang; Dit-Yan Yeung; Wai-kin Wong; Wang-chun Woo | 2015 | arXiv | `https://arxiv.org/abs/1506.04214` | 1506.04214 | recurrent_baseline | Baseline anchor for Section 04 discussion of recurrent visual dynamics. | §04 | background | citeturn0academia2 |
| P042 | PredRNN: A Recurrent Neural Network for Spatiotemporal Predictive Learning | Yunbo Wang; Haixu Wu; Jianjin Zhang; Zhifeng Gao; Jianmin Wang; Philip S. Yu; Mingsheng Long | 2021 | arXiv | `https://arxiv.org/abs/2103.09504` | 2103.09504 | recurrent_baseline | Supports Section 04 baseline lineage beyond SV2P and robot video prediction. | §04 | background | citeturn31academia1 |
| P043 | PredRNN++: Towards A Resolution of the Deep-in-Time Dilemma in Spatiotemporal Predictive Learning | Yunbo Wang; Zhifeng Gao; Mingsheng Long; Jianmin Wang; Philip S. Yu | 2018 | arXiv | `https://arxiv.org/abs/1804.06300` | 1804.06300 | recurrent_baseline | Lets Section 04 compare architectural sophistication against simpler baselines like SimVP. | §04 | background | citeturn31academia3 |
| P044 | Memory In Memory: A Predictive Neural Network for Learning Higher-Order Non-Stationarity from Spatiotemporal Dynamics | Yunbo Wang; Jianjin Zhang; Hongyu Zhu; Mingsheng Long; Jianmin Wang; Philip S. Yu | 2018 | arXiv | `https://arxiv.org/abs/1811.07490` | 1811.07490 | recurrent_baseline | Strengthens Section 04 on architecture-oriented baselines the manuscript currently flags as incomplete. | §04 | background | citeturn0academia0 |
| P045 | Eidetic 3D LSTM: A Model for Video Prediction and Beyond | UNKNOWN | UNKNOWN | UNKNOWN | `UNKNOWN` | UNKNOWN | recurrent_baseline | Useful Section 04 comparator for long-range memory designs if metadata is completed. | §04 | candidate | user-provided target only; primary-source metadata unresolved |
| P046 | SimVP: Simpler yet Better Video Prediction | Zhangyang Gao; Cheng Tan; Lirong Wu; Stan Z. Li | 2022 | arXiv | `https://arxiv.org/abs/2206.05099` | 2206.05099 | cnn_baseline | Essential for Section 04 to avoid overclaiming that more structured/complex models are always needed. | §04 | core | citeturn2academia1 |
| P047 | Disentangling Physical Dynamics from Unknown Factors for Unsupervised Video Prediction | Vincent Le Guen; Nicolas Thome | 2020 | arXiv | `https://arxiv.org/abs/2003.01460` | 2003.01460 | physics_informed_prediction | Important Section 04 bridge from generic visual forecasting to physically structured dynamics. | §04 | core | citeturn2academia0 |
| P048 | MCVD: Masked Conditional Video Diffusion for Prediction, Generation, and Interpolation | Vikram Voleti; Alexia Jolicoeur-Martineau; Christopher Pal | 2022 | arXiv | `https://arxiv.org/abs/2205.09853` | 2205.09853 | diffusion_prediction | Section 04 and Section 07 bridge for diffusion-formulated visual dynamics. | §04 | core | citeturn34academia0 |
| P049 | VideoGPT: Video Generation using VQ-VAE and Transformers | Wilson Yan; Yunzhi Zhang; Pieter Abbeel; Aravind Srinivas | 2021 | arXiv | `https://arxiv.org/abs/2104.10157` | 2104.10157 | token_video_model | Supports distinction among video generation, token modeling, and predictive world models in Sections 04 and 07. | §04/§06-07 | background | citeturn34academia1 |

**Object-centric / structured world models**

| ID | Title | Authors | Year | Venue or arXiv | URL | arXiv ID or DOI | Category | Why it matters for this survey | Section support | Priority | Verification |
|---|---|---|---:|---|---|---|---|---|---|---|---|
| P050 | Object-Centric Learning with Slot Attention | Francesco Locatello; Dirk Weissenborn; Thomas Unterthiner; Aravindh Mahendran; Georg Heigold; Jakob Uszkoreit; Alexey Dosovitskiy; Thomas Kipf | 2020 | arXiv | `https://arxiv.org/abs/2006.15055` | 2006.15055 | object_discovery | Section 05 foundation for slot-based world-model discussion. | §05 | core | citeturn7academia0 |
| P051 | Conditional Object-Centric Learning from Video | Thomas Kipf; Gamaleldin F. Elsayed; Aravindh Mahendran; Austin Stone; Sara Sabour; Georg Heigold; Rico Jonschkowski; Alexey Dosovitskiy; Klaus Greff | 2021 | arXiv | `https://arxiv.org/abs/2111.12594` | 2111.12594 | video_object_centric | Section 05 support for temporal consistency and video object-centric learning. | §05 | core | citeturn13academia0 |
| P052 | SAVi++: Towards End-to-End Object-Centric Learning from Real-World Videos | Gamaleldin F. Elsayed; Aravindh Mahendran; Sjoerd van Steenkiste; Klaus Greff; Michael C. Mozer; Thomas Kipf | 2022 | arXiv | `https://arxiv.org/abs/2206.07764` | 2206.07764 | real_world_video_ocl | Section 05 evidence that object-centric learning can move beyond toy scenes. | §05 | core | citeturn13academia1 |
| P053 | Contrastive Learning of Structured World Models | Thomas Kipf; Elise van der Pol; Max Welling | 2019 | arXiv | `https://arxiv.org/abs/1911.12247` | 1911.12247 | contrastive_world_model | Section 05 bridge from object-centric representation learning to decision-centric world models. | §05/§06 | core | citeturn16academia1 |
| P054 | Object-Centric Learning for Real-World Videos by Predicting Temporal Feature Similarities | Andrii Zadaianchuk; Maximilian Seitzer; Georg Martius | 2023 | arXiv | `https://arxiv.org/abs/2306.04829` | 2306.04829 | real_world_video_ocl | Section 05 support for the manuscript's currently underdeveloped real-world object-centric story. | §05 | candidate | citeturn12academia0 |
| P055 | SlotFormer: Unsupervised Visual Dynamics Simulation with Object-Centric Models | Ziyi Wu; Nikita Dvornik; Klaus Greff; Thomas Kipf; Animesh Garg | 2022 | arXiv | `https://arxiv.org/abs/2210.05861` | 2210.05861 | object_dynamics | One of the strongest Section 05 additions because it explicitly ties object-centric dynamics to world-model use. | §05/§08 | core | citeturn8academia0 |

**Latent / token / feature-space world models**

| ID | Title | Authors | Year | Venue or arXiv | URL | arXiv ID or DOI | Category | Why it matters for this survey | Section support | Priority | Verification |
|---|---|---|---:|---|---|---|---|---|---|---|---|
| P056 | Mastering Atari with Discrete World Models | Danijar Hafner; Timothy Lillicrap; Mohammad Norouzi; Jimmy Ba | 2020 | arXiv | `https://arxiv.org/abs/2010.02193` | 2010.02193 | discrete_latent_rl | Core Section 06 evidence beyond the manuscript's current Dreamer 2020 endpoint. | §06 | core | citeturn17academia1 |
| P057 | Mastering Diverse Domains through World Models | Danijar Hafner; Jurgis Pasukonis; Jimmy Ba; Timothy Lillicrap | 2023 | arXiv | `https://arxiv.org/abs/2301.04104` | 2301.04104 | general_world_model_rl | Section 06 needs it to avoid stopping the latent-world-model story too early. | §06 | core | citeturn17academia2 |
| P058 | Transformers are Sample-Efficient World Models | Vincent Micheli; Eloi Alonso; François Fleuret | 2022 | arXiv | `https://arxiv.org/abs/2209.00588` | 2209.00588 | token_world_model | Section 06 benefit: explicit recurrent-vs-transformer comparison within latent world models. | §06 | core | citeturn17academia3 |
| P059 | DayDreamer: World Models for Physical Robot Learning | Philipp Wu; Alejandro Escontrela; Danijar Hafner; Ken Goldberg; Pieter Abbeel | 2022 | arXiv | `https://arxiv.org/abs/2206.14176` | 2206.14176 | robot_world_model | Section 06 needs real-robot grounding, not only simulated control benchmarks. | §06 | core | citeturn17academia0 |
| P060 | DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning | Gaoyue Zhou; Hengkai Pan; Yann LeCun; Lerrel Pinto | 2024 | arXiv | `https://arxiv.org/abs/2411.04983` | 2411.04983 | feature_space_world_model | Section 06 needs this to cover the feature-space branch the reviewer explicitly requested. | §06 | core | citeturn18academia0 |
| P061 | Pre-training Contextualized World Models with In-the-wild Videos for Reinforcement Learning | Jialong Wu; Haoyu Ma; Chaoyi Deng; Mingsheng Long | 2023 | arXiv | `https://arxiv.org/abs/2305.18499` | 2305.18499 | pretrained_world_model | Section 06 support for contextualized and pretraining-based world models. | §06 | core | citeturn18academia1 |
| P062 | iVideoGPT: Interactive VideoGPTs are Scalable World Models | Jialong Wu; Shaofeng Yin; Ningya Feng; Xu He; Dong Li; Jianye Hao; Mingsheng Long | 2024 | arXiv | `https://arxiv.org/abs/2405.15223` | 2405.15223 | interactive_token_world_model | Can support either Section 06 or Section 07 as a bridge paper. | §06/§07 | candidate | citeturn34academia3 |

**Generative simulation / interactive world models**

| ID | Title | Authors | Year | Venue or arXiv | URL | arXiv ID or DOI | Category | Why it matters for this survey | Section support | Priority | Verification |
|---|---|---|---:|---|---|---|---|---|---|---|---|
| P063 | Video generation models as world simulators | Tim Brooks; Bill Peebles; Connor Holmes; Will DePue; Yufei Guo | 2024 | OpenAI technical report | `https://openai.com/index/video-generation-models-as-world-simulators/` | UNKNOWN | world_simulator_discussion | Section 07 should discuss it explicitly but cautiously, not as settled proof. | §07/§08 | core | citeturn23view0turn48view0 |
| P064 | Learning Interactive Real-World Simulators | Sherry Yang; Yilun Du; Kamyar Ghasemipour; Jonathan Tompson; Leslie Kaelbling; Dale Schuurmans; Pieter Abbeel | 2023 | arXiv | `https://arxiv.org/abs/2310.06114` | 2310.06114 | interactive_simulator | Core Section 07 evidence that real-world interactivity is a distinct goal beyond video realism. | §07 | core | citeturn19academia4 |
| P065 | GAIA-1: A Generative World Model for Autonomous Driving | Anthony Hu; Lloyd Russell; Hudson Yeo; Zak Murez; George Fedoseev; Alex Kendall; Jamie Shotton; Gianluca Corrado | 2023 | arXiv | `https://arxiv.org/abs/2309.17080` | 2309.17080 | driving_world_model | Section 07 should include at least one major driving world model beyond Atari/game examples. | §07 | core | citeturn19academia1 |
| P066 | DriveDreamer: Towards Real-world-driven World Models for Autonomous Driving | Xiaofeng Wang; Zheng Zhu; Guan Huang; Xinze Chen; Jiagang Zhu; Jiwen Lu | 2023 | arXiv | `https://arxiv.org/abs/2309.09777` | 2309.09777 | driving_world_model | Section 07 support for real-world-driven diffusion world models. | §07 | core | citeturn19academia0 |
| P067 | DriveDreamer-2: LLM-Enhanced World Models for Diverse Driving Video Generation | Guosheng Zhao; Xiaofeng Wang; Zheng Zhu; Xinze Chen; Guan Huang; Xiaoyi Bao; Xingang Wang | 2024 | arXiv | `https://arxiv.org/abs/2403.06845` | 2403.06845 | driving_world_model | Useful Section 07 contrast between controllability via explicit semantics versus latent controls. | §07 | candidate | citeturn21academia0 |
| P068 | Cosmos World Foundation Model Platform for Physical AI | NVIDIA et al. | 2025 | arXiv | `https://arxiv.org/abs/2501.03575` | 2501.03575 | world_foundation_model | Section 07 should note this as evidence of industrial consolidation around 'world foundation models'. | §07 | candidate | citeturn20academia2 |
| P069 | VideoWorld: Exploring Knowledge Learning from Unlabeled Videos | Zhongwei Ren; Yunchao Wei; Xun Guo; Yao Zhao; Bingyi Kang; Jiashi Feng; Xiaojie Jin | 2025 | arXiv | `https://arxiv.org/abs/2501.09781` | 2501.09781 | video_only_world_model | Section 07 needs it because the manuscript already points to VideoWorld as an incomplete but relevant addition. | §07 | core | citeturn20academia0 |
| P070 | Vid2World: Crafting Video Diffusion Models to Interactive World Models | Siqiao Huang; Jialong Wu; Qixing Zhou; Shangchen Miao; Mingsheng Long | 2025 | arXiv | `https://arxiv.org/abs/2505.14357` | 2505.14357 | interactive_diffusion_world_model | Core Section 07 paper because it directly refines the manuscript's video-generation/world-model boundary. | §07 | core | citeturn20academia1 |

**Physical evaluation / benchmark literature**

| ID | Title | Authors | Year | Venue or arXiv | URL | arXiv ID or DOI | Category | Why it matters for this survey | Section support | Priority | Verification |
|---|---|---|---:|---|---|---|---|---|---|---|---|
| P071 | PHYRE: A New Benchmark for Physical Reasoning | Anton Bakhtin; Laurens van der Maaten; Justin Johnson; Laura Gustafson; Ross Girshick | 2019 | arXiv | `https://arxiv.org/abs/1908.05656` | 1908.05656 | physical_reasoning_benchmark | Section 08 should cite it when discussing intervention-based physical evaluation. | §08 | core | citeturn24academia3 |
| P072 | CLEVRER: CoLlision Events for Video REpresentation and Reasoning | Kexin Yi; Chuang Gan; Yunzhu Li; Pushmeet Kohli; Jiajun Wu; Antonio Torralba; Joshua B. Tenenbaum | 2019 | arXiv | `https://arxiv.org/abs/1910.01442` | 1910.01442 | causal_video_reasoning | Section 08 can use it to strengthen causal/counterfactual evaluation discussion. | §08 | core | citeturn24academia1 |
| P073 | Physion: Evaluating Physical Prediction from Vision in Humans and Machines | Daniel M. Bear; Elias Wang; Damian Mrowca; Felix J. Binder; Hsiao-Yu Fish Tung; R. T. Pramod; Cameron Holdaway; Sirui Tao; Kevin Smith; Fan-Yun Sun; Li Fei-Fei; Nancy Kanwisher; Joshua B. Tenenbaum; Daniel L. K. Yamins; Judith E. Fan | 2021 | arXiv | `https://arxiv.org/abs/2106.08261` | 2106.08261 | physical_prediction_benchmark | Section 08 should use it to move beyond text-to-video physical eval alone. | §08 | core | citeturn24academia0 |
| P074 | VideoPhy: Evaluating Physical Commonsense for Video Generation | Hritik Bansal; Zongyu Lin; Tianyi Xie; Zeshun Zong; Michal Yarom; Yonatan Bitton; Chenfanfu Jiang; Yizhou Sun; Kai-Wei Chang; Aditya Grover | 2024 | arXiv | `https://arxiv.org/abs/2406.03520` | 2406.03520 | physical_commonsense_t2v | Section 08 core paper; already present in manuscript, but should anchor a fuller benchmark comparison. | §07/§08 | core | citeturn24academia2 |
| P075 | Towards World Simulator: Crafting Physical Commonsense-Based Benchmark for Video Generation | Fanqing Meng; Jiaqi Liao; Xinyu Tan; Wenqi Shao; Quanfeng Lu; Kaipeng Zhang; Yu Cheng; Dianqi Li; Yu Qiao; Ping Luo | 2024 | arXiv | `https://arxiv.org/abs/2410.05363` | 2410.05363 | physical_commonsense_t2v | Section 08 needs it to broaden beyond VideoPhy and to discuss law coverage more concretely. | §08 | core | citeturn25academia1 |
| P076 | How Far is Video Generation from World Model: A Physical Law Perspective | Bingyi Kang; Yang Yue; Rui Lu; Zhijie Lin; Yang Zhao; Kaixin Wang; Gao Huang; Jiashi Feng | 2024 | arXiv | `https://arxiv.org/abs/2411.02385` | 2411.02385 | physical_law_generalization | Section 08 should use it to avoid overclaiming that larger video models discover laws automatically. | §08 | core | citeturn25academia0 |
| P077 | Do generative video models learn physical principles from watching videos? | Saman Motamed; Laura Culp; Kevin Swersky; Priyank Jaini; Robert Geirhos | 2025 | arXiv | `https://arxiv.org/abs/2501.09038` | 2501.09038 | physics_benchmark | Section 08 can cite it whenever arguing that visual realism is not equivalent to physical understanding. | §08 | core | citeturn25academia2 |
| P078 | WorldScore: A Unified Evaluation Benchmark for World Generation | Haoyi Duan; Hong-Xing Yu; Sirui Chen; Li Fei-Fei; Jiajun Wu | 2025 | arXiv | `https://arxiv.org/abs/2504.00983` | 2504.00983 | world_generation_benchmark | Best treated as a candidate Section 08 addition for a broader evaluation taxonomy, not a central physics citation. | §08 | candidate | citeturn25academia3 |

## CSV rows

以下對應 Part 2。這份 CSV 直接轉寫自上表；逐筆 primary-source 驗證請對照 Part 1 的「Verification」欄。為避免捏造 metadata，我保留了 `UNKNOWN`，其中最重要的是 P045 的 E3D-LSTM 尚待手動補齊。citeturn0academia2turn31academia1turn23view0turn25academia3

```csv
id,title,authors,year,venue,arxiv_id,doi,url,bibtex_key,category,sub_category,task,input_modality,output_modality,model_family,dynamics_modeling,physical_prior,interaction,benchmark,dataset,metrics,key_contribution,main_limitation,relevance_to_survey,status,notes_file
P041,Convolutional LSTM Network: A Machine Learning Approach for Precipitation Nowcasting,Xingjian Shi; Zhourong Chen; Hao Wang; Dit-Yan Yeung; Wai-kin Wong; Wang-chun Woo,2015,arXiv,1506.04214,UNKNOWN,https://arxiv.org/abs/1506.04214,shi2015convlstm,video_prediction,recurrent_baseline,spatiotemporal prediction,video / radar frames,future frames,ConvRNN,convolutional LSTM recurrence,none,passive,nowcasting / video prediction,radar echo datasets,UNKNOWN,Introduces ConvLSTM as a canonical spatiotemporal recurrent baseline.,Not a world model; no action conditioning and limited physical abstraction.,Baseline anchor for Section 04 discussion of recurrent visual dynamics.,background,P041_shi2015convlstm.md
P042,PredRNN: A Recurrent Neural Network for Spatiotemporal Predictive Learning,Yunbo Wang; Haixu Wu; Jianjin Zhang; Zhifeng Gao; Jianmin Wang; Philip S. Yu; Mingsheng Long,2021,arXiv,2103.09504,UNKNOWN,https://arxiv.org/abs/2103.09504,wang2021predrnn,video_prediction,recurrent_baseline,spatiotemporal prediction,video,future frames,RNN,spatiotemporal recurrent memory,none,passive / action-conditioned variants,video prediction,UNKNOWN,UNKNOWN,Family anchor for PredRNN-style deep-in-time recurrent predictive learning.,Retrieved primary source is a later arXiv family anchor rather than the original 2017 conference version.,Supports Section 04 baseline lineage beyond SV2P and robot video prediction.,background,P042_wang2021predrnn.md
P043,PredRNN++: Towards A Resolution of the Deep-in-Time Dilemma in Spatiotemporal Predictive Learning,Yunbo Wang; Zhifeng Gao; Mingsheng Long; Jianmin Wang; Philip S. Yu,2018,arXiv,1804.06300,UNKNOWN,https://arxiv.org/abs/1804.06300,wang2018predrnnpp,video_prediction,recurrent_baseline,spatiotemporal prediction,video,future frames,RNN,causal LSTM + gradient highway,none,passive,video prediction,UNKNOWN,UNKNOWN,Canonical long-horizon recurrent baseline addressing gradient flow in deep temporal models.,Still primarily optimizes video prediction quality rather than controllable world modeling.,Lets Section 04 compare architectural sophistication against simpler baselines like SimVP.,background,P043_wang2018predrnnpp.md
P044,Memory In Memory: A Predictive Neural Network for Learning Higher-Order Non-Stationarity from Spatiotemporal Dynamics,Yunbo Wang; Jianjin Zhang; Hongyu Zhu; Mingsheng Long; Jianmin Wang; Philip S. Yu,2018,arXiv,1811.07490,UNKNOWN,https://arxiv.org/abs/1811.07490,wang2018mim,video_prediction,recurrent_baseline,spatiotemporal prediction,video / spatiotemporal sequences,future frames,RNN,differential recurrent memory,non-stationarity inductive bias,passive,video prediction,UNKNOWN,UNKNOWN,Important baseline for modeling higher-order non-stationarity in predicted dynamics.,"Still evaluated mainly as predictive learning, not intervention-aware world modeling.",Strengthens Section 04 on architecture-oriented baselines the manuscript currently flags as incomplete.,background,P044_wang2018mim.md
P045,Eidetic 3D LSTM: A Model for Video Prediction and Beyond,UNKNOWN,UNKNOWN,UNKNOWN,UNKNOWN,UNKNOWN,UNKNOWN,unknown_e3dlstm,video_prediction,recurrent_baseline,spatiotemporal prediction,video,future frames,RNN / 3D conv hybrid,eidetic 3D recurrent memory,none,passive,UNKNOWN,UNKNOWN,UNKNOWN,Widely cited long-range video prediction baseline combining 3D convolutional structure with recurrent memory.,Primary-source metadata could not be reliably retrieved in this search pass; manual verification is still needed.,Useful Section 04 comparator for long-range memory designs if metadata is completed.,candidate,P045_unknown_e3dlstm.md
P046,SimVP: Simpler yet Better Video Prediction,Zhangyang Gao; Cheng Tan; Lirong Wu; Stan Z. Li,2022,arXiv,2206.05099,UNKNOWN,https://arxiv.org/abs/2206.05099,gao2022simvp,video_prediction,cnn_baseline,video prediction,video,future frames,CNN,pure CNN predictive blocks,none,passive,five benchmark datasets,UNKNOWN,MSE and standard prediction metrics,Strong simple baseline that tests whether heavy recurrent/transformer machinery is necessary.,Primarily about forecasting quality; lacks explicit control or physics structure.,Essential for Section 04 to avoid overclaiming that more structured/complex models are always needed.,core,P046_gao2022simvp.md
P047,Disentangling Physical Dynamics from Unknown Factors for Unsupervised Video Prediction,Vincent Le Guen; Nicolas Thome,2020,arXiv,2003.01460,UNKNOWN,https://arxiv.org/abs/2003.01460,leguen2020phydnet,video_prediction,physics_informed_prediction,unsupervised video prediction,video,future frames,hybrid recurrent model,PhyCell + residual branch,PDE-inspired latent dynamics,passive,video prediction,four datasets,UNKNOWN,Directly strengthens the physical-dynamics angle within video prediction.,Still prediction-centric; physical prior is partial and domain-limited.,Important Section 04 bridge from generic visual forecasting to physically structured dynamics.,core,P047_leguen2020phydnet.md
P048,"MCVD: Masked Conditional Video Diffusion for Prediction, Generation, and Interpolation",Vikram Voleti; Alexia Jolicoeur-Martineau; Christopher Pal,2022,arXiv,2205.09853,UNKNOWN,https://arxiv.org/abs/2205.09853,voleti2022mcvd,video_prediction,diffusion_prediction,prediction / generation / interpolation,video,video,diffusion,conditional score-based diffusion,none,passive conditional masking,video prediction and interpolation benchmarks,UNKNOWN,UNKNOWN,Major bridge paper between video prediction and diffusion-based generation.,Not itself an interactive world model; action semantics are absent.,Section 04 and Section 07 bridge for diffusion-formulated visual dynamics.,core,P048_voleti2022mcvd.md
P049,VideoGPT: Video Generation using VQ-VAE and Transformers,Wilson Yan; Yunzhi Zhang; Pieter Abbeel; Aravind Srinivas,2021,arXiv,2104.10157,UNKNOWN,https://arxiv.org/abs/2104.10157,yan2021videogpt,video_prediction,token_video_model,video generation,video,video,token transformer,autoregressive token modeling,none,passive,video generation,BAIR Robot; UCF-101; TGIF,UNKNOWN,Tokenized video generation baseline that foreshadows token/world-model hybrids.,Generative realism does not imply controllable or physically faithful world modeling.,"Supports distinction among video generation, token modeling, and predictive world models in Sections 04 and 07.",background,P049_yan2021videogpt.md
P050,Object-Centric Learning with Slot Attention,Francesco Locatello; Dirk Weissenborn; Thomas Unterthiner; Aravindh Mahendran; Georg Heigold; Jakob Uszkoreit; Alexey Dosovitskiy; Thomas Kipf,2020,arXiv,2006.15055,UNKNOWN,https://arxiv.org/abs/2006.15055,locatello2020slotattention,object_centric,object_discovery,object-centric representation learning,image / video frames,slots / objects,slot-based,none,object decomposition,passive,object discovery and property prediction,UNKNOWN,UNKNOWN,Foundational slot-based object binding mechanism used by later video dynamics models.,No temporal dynamics by itself.,Section 05 foundation for slot-based world-model discussion.,core,P050_locatello2020slotattention.md
P051,Conditional Object-Centric Learning from Video,Thomas Kipf; Gamaleldin F. Elsayed; Aravindh Mahendran; Austin Stone; Sara Sabour; Georg Heigold; Rico Jonschkowski; Alexey Dosovitskiy; Klaus Greff,2021,arXiv,2111.12594,UNKNOWN,https://arxiv.org/abs/2111.12594,kipf2021savi,object_centric,video_object_centric,object-centric learning from video,video,slots / segmentations / tracks,slot-based recurrent model,sequential slot updates,motion / optical flow bias,conditioned on simple hints,synthetic video object segmentation / tracking,UNKNOWN,UNKNOWN,The core SAVi family anchor for sequential slot-based learning from videos.,Weak supervision and synthetic-domain assumptions limit generality.,Section 05 support for temporal consistency and video object-centric learning.,core,P051_kipf2021savi.md
P052,SAVi++: Towards End-to-End Object-Centric Learning from Real-World Videos,Gamaleldin F. Elsayed; Aravindh Mahendran; Sjoerd van Steenkiste; Klaus Greff; Michael C. Mozer; Thomas Kipf,2022,arXiv,2206.07764,UNKNOWN,https://arxiv.org/abs/2206.07764,elsayed2022savipp,object_centric,real_world_video_ocl,object-centric learning from real-world videos,video + sparse depth,slots / segmentation / tracking,slot-based video model,sequential slot video modeling,depth cues,passive,real-world object-centric video learning,Waymo Open Dataset,UNKNOWN,Shows how depth cues and scaling practices help object-centric learning transfer to real-world videos.,Depends on depth signals and remains focused on representation rather than explicit planning/control.,Section 05 evidence that object-centric learning can move beyond toy scenes.,core,P052_elsayed2022savipp.md
P053,Contrastive Learning of Structured World Models,Thomas Kipf; Elise van der Pol; Max Welling,2019,arXiv,1911.12247,UNKNOWN,https://arxiv.org/abs/1911.12247,kipf2019cswm,object_centric,contrastive_world_model,visual reinforcement learning,video / pixels,object-factored latent transitions,contrastive object-centric world model,graph neural network over object embeddings,object-factorization,action-conditioned,structured environments; Atari; physics simulation,UNKNOWN,UNKNOWN,Canonical C-SWM paper linking object-centric structure to action-conditioned world modeling.,Works best in highly structured environments; general real-video scaling remains hard.,Section 05 bridge from object-centric representation learning to decision-centric world models.,core,P053_kipf2019cswm.md
P054,Object-Centric Learning for Real-World Videos by Predicting Temporal Feature Similarities,Andrii Zadaianchuk; Maximilian Seitzer; Georg Martius,2023,arXiv,2306.04829,UNKNOWN,https://arxiv.org/abs/2306.04829,zadaianchuk2023temporalfeaturesim,object_centric,real_world_video_ocl,video object-centric learning,video,object-centric slots,slot-based model with feature losses,temporal feature similarity objective,temporal-semantic patch similarity,passive,synthetic and unconstrained videos,MOVi; YouTube-VIS,UNKNOWN,Shows a path from synthetic OCL to unconstrained real-world videos via temporally informed feature losses.,Still focuses on representation quality more than explicit predictive control.,Section 05 support for the manuscript's currently underdeveloped real-world object-centric story.,candidate,P054_zadaianchuk2023temporalfeaturesim.md
P055,SlotFormer: Unsupervised Visual Dynamics Simulation with Object-Centric Models,Ziyi Wu; Nikita Dvornik; Klaus Greff; Thomas Kipf; Animesh Garg,2022,arXiv,2210.05861,UNKNOWN,https://arxiv.org/abs/2210.05861,wu2022slotformer,object_centric,object_dynamics,visual dynamics simulation,video,future slots / generated video,object-centric transformer,autoregressive transformer over slots,object-centric decomposition,supports planning evaluation,video prediction; VQA; goal-conditioned planning,UNKNOWN,UNKNOWN,Direct object-centric dynamics simulator with downstream planning/VQA evidence.,Depends on learned slots and remains challenging in unconstrained real-world video.,One of the strongest Section 05 additions because it explicitly ties object-centric dynamics to world-model use.,core,P055_wu2022slotformer.md
P056,Mastering Atari with Discrete World Models,Danijar Hafner; Timothy Lillicrap; Mohammad Norouzi; Jimmy Ba,2020,arXiv,2010.02193,UNKNOWN,https://arxiv.org/abs/2010.02193,hafner2020dreamerv2,latent_world_model,discrete_latent_rl,model-based reinforcement learning,pixels + rewards + actions,latent rollouts / policy,RSSM,discrete latent recurrent state-space model,none,action-conditioned,Atari 55; continuous control,Atari,human-normalized score; return,DreamerV2 establishes discrete latent world models as a strong control substrate.,Task return does not directly establish physical faithfulness.,Core Section 06 evidence beyond the manuscript's current Dreamer 2020 endpoint.,core,P056_hafner2020dreamerv2.md
P057,Mastering Diverse Domains through World Models,Danijar Hafner; Jurgis Pasukonis; Jimmy Ba; Timothy Lillicrap,2023,arXiv,2301.04104,UNKNOWN,https://arxiv.org/abs/2301.04104,hafner2023dreamerv3,latent_world_model,general_world_model_rl,general model-based RL,pixels + rewards + actions,policy / imagined trajectories,RSSM,stabilized recurrent latent imagination,none,action-conditioned,150+ diverse tasks,Atari; Minecraft; locomotion and more,return / task success,DreamerV3 is the strongest general-purpose latent world-model reference in this lineage.,General control breadth still does not equal open-ended physical simulation.,Section 06 needs it to avoid stopping the latent-world-model story too early.,core,P057_hafner2023dreamerv3.md
P058,Transformers are Sample-Efficient World Models,Vincent Micheli; Eloi Alonso; François Fleuret,2022,arXiv,2209.00588,UNKNOWN,https://arxiv.org/abs/2209.00588,micheli2022iris,latent_world_model,token_world_model,sample-efficient RL,pixels + actions,discrete latent tokens / policy,VQ-VAE + Transformer,autoregressive transformer world model,discrete tokenization,action-conditioned,Atari 100k,Atari,human-normalized score,IRIS is the clearest transformer/token world-model counterpart to Dreamer-style RSSMs.,Primarily benchmarked in Atari-scale domains.,Section 06 benefit: explicit recurrent-vs-transformer comparison within latent world models.,core,P058_micheli2022iris.md
P059,DayDreamer: World Models for Physical Robot Learning,Philipp Wu; Alejandro Escontrela; Danijar Hafner; Ken Goldberg; Pieter Abbeel,2022,arXiv,2206.14176,UNKNOWN,https://arxiv.org/abs/2206.14176,wu2022daydreamer,latent_world_model,robot_world_model,physical robot learning,robot video + actions + rewards,policy / imagined trajectories,Dreamer-based,latent imagination for online robot learning,embodied interaction data,action-conditioned,robot tasks,4 physical robots,task success; adaptation speed,Critical evidence that latent world models can learn directly on physical robots.,Still task-bounded and not a general simulator benchmark.,"Section 06 needs real-robot grounding, not only simulated control benchmarks.",core,P059_wu2022daydreamer.md
P060,DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning,Gaoyue Zhou; Hengkai Pan; Yann LeCun; Lerrel Pinto,2024,arXiv,2411.04983,UNKNOWN,https://arxiv.org/abs/2411.04983,zhou2024dinowm,latent_world_model,feature_space_world_model,task-agnostic planning,offline trajectories / video + actions,future patch features / plans,feature-space world model,predictive modeling over DINOv2 patch features,pre-trained visual features,offline action-conditioned planning,six planning environments,offline behavioral trajectories,zero-shot task success,Strong exemplar of feature-space world models that avoid reconstruction entirely.,Zero-shot planning results are domain-bounded; physical law validity is not directly tested.,Section 06 needs this to cover the feature-space branch the reviewer explicitly requested.,core,P060_zhou2024dinowm.md
P061,Pre-training Contextualized World Models with In-the-wild Videos for Reinforcement Learning,Jialong Wu; Haoyu Ma; Chaoyi Deng; Mingsheng Long,2023,arXiv,2305.18499,UNKNOWN,https://arxiv.org/abs/2305.18499,wu2023contextwm,latent_world_model,pretrained_world_model,world-model pretraining for RL,in-the-wild videos,contextualized latent world model,latent dynamics model,separate context and dynamics,context-dynamics factorization,downstream action-conditioned RL,robot manipulation; locomotion; driving,in-the-wild videos + downstream RL tasks,sample efficiency,Directly addresses the in-the-wild video pretraining question missing from the manuscript.,Transfer gains do not automatically show simulator-level correctness.,Section 06 support for contextualized and pretraining-based world models.,core,P061_wu2023contextwm.md
P062,iVideoGPT: Interactive VideoGPTs are Scalable World Models,Jialong Wu; Shaofeng Yin; Ningya Feng; Xu He; Dong Li; Jianye Hao; Mingsheng Long,2024,arXiv,2405.15223,UNKNOWN,https://arxiv.org/abs/2405.15223,wu2024ivideogpt,latent_world_model,interactive_token_world_model,interactive world modeling / MBRL,visual observations + actions + rewards,token rollouts / policy,autoregressive transformer,next-token prediction with compressive tokenization,token compression,action-conditioned,video prediction; planning; MBRL,human and robotic manipulation trajectories,competitive downstream performance,Useful expansion paper linking VideoGPT-style token modeling to interactive world models.,Still combines broad claims with benchmark-specific evidence.,Can support either Section 06 or Section 07 as a bridge paper.,candidate,P062_wu2024ivideogpt.md
P063,Video generation models as world simulators,Tim Brooks; Bill Peebles; Connor Holmes; Will DePue; Yufei Guo,2024,OpenAI technical report,UNKNOWN,UNKNOWN,https://openai.com/index/video-generation-models-as-world-simulators/,brooks2024sorareport,generative_simulation,world_simulator_discussion,text-to-video generation / simulator claim,text; image; video,generated video,diffusion transformer,spacetime patch diffusion,scale-induced emergent structure,prompt-conditioned; image/video editing,qualitative capability report,internet-scale videos and images,qualitative evaluation,Most visible primary source behind the 'video generation as world simulator' narrative.,OpenAI itself notes qualitative evaluation and simulator limitations; not evidence of robust physical world modeling.,"Section 07 should discuss it explicitly but cautiously, not as settled proof.",core,P063_brooks2024sorareport.md
P064,Learning Interactive Real-World Simulators,Sherry Yang; Yilun Du; Kamyar Ghasemipour; Jonathan Tompson; Leslie Kaelbling; Dale Schuurmans; Pieter Abbeel,2023,arXiv,2310.06114,UNKNOWN,https://arxiv.org/abs/2310.06114,yang2023unisim,generative_simulation,interactive_simulator,interactive real-world simulation,images; videos; actions / instructions,simulated future observations,generative simulator,multi-dataset generative simulation,dataset orchestration,high-level instructions + low-level controls,zero-shot policy transfer,diverse image; robotics; navigation data,downstream policy performance,One of the clearest primary sources for learned interactive real-world simulators.,Simulator universality remains aspirational and dataset-composition-dependent.,Core Section 07 evidence that real-world interactivity is a distinct goal beyond video realism.,core,P064_yang2023unisim.md
P065,GAIA-1: A Generative World Model for Autonomous Driving,Anthony Hu; Lloyd Russell; Hudson Yeo; Zak Murez; George Fedoseev; Alex Kendall; Jamie Shotton; Gianluca Corrado,2023,arXiv,2309.17080,UNKNOWN,https://arxiv.org/abs/2309.17080,hu2023gaia1,generative_simulation,driving_world_model,autonomous driving world modeling,video + text + action,driving scenarios / tokens,token generative model,next-token sequence modeling,driving data and scene structure,action- and text-conditioned,autonomous driving generation,driving data,UNKNOWN,Representative generative driving world model with multimodal conditioning.,Domain-specific to driving and still far from general physical simulation.,Section 07 should include at least one major driving world model beyond Atari/game examples.,core,P065_hu2023gaia1.md
P066,DriveDreamer: Towards Real-world-driven World Models for Autonomous Driving,Xiaofeng Wang; Zheng Zhu; Guan Huang; Xinze Chen; Jiagang Zhu; Jiwen Lu,2023,arXiv,2309.09777,UNKNOWN,https://arxiv.org/abs/2309.09777,wang2023drivedreamer,generative_simulation,driving_world_model,real-world driving video generation and policy generation,driving observations,future driving videos / policies,diffusion world model,two-stage diffusion-based world modeling,traffic constraints,controllable generation,nuScenes,nuScenes,video generation quality; controllability,Diffusion-based real-world driving world model with structured traffic constraints.,Claims are domain-specific and evaluation remains largely generation-centric.,Section 07 support for real-world-driven diffusion world models.,core,P066_wang2023drivedreamer.md
P067,DriveDreamer-2: LLM-Enhanced World Models for Diverse Driving Video Generation,Guosheng Zhao; Xiaofeng Wang; Zheng Zhu; Xinze Chen; Guan Huang; Xiaoyi Bao; Xingang Wang,2024,arXiv,2403.06845,UNKNOWN,https://arxiv.org/abs/2403.06845,zhao2024drivedreamer2,generative_simulation,driving_world_model,user-defined driving video generation,language + trajectories + maps,multi-view driving video,LLM-enhanced world model,trajectory/map-guided generator,HD map and traffic rules,language-conditioned,driving video generation,UNKNOWN,FID; FVD; downstream perception utility,Adds language-level customization and uncommon events to the driving world-model story.,Still generation-heavy and domain-specific.,Useful Section 07 contrast between controllability via explicit semantics versus latent controls.,candidate,P067_zhao2024drivedreamer2.md
P068,Cosmos World Foundation Model Platform for Physical AI,NVIDIA et al.,2025,arXiv,2501.03575,UNKNOWN,https://arxiv.org/abs/2501.03575,nvidia2025cosmos,generative_simulation,world_foundation_model,world foundation model platform,video,world models / video tokens / fine-tuned models,world foundation model platform,video tokenization + pretraining + post-training,physical AI framing,downstream customization,platform / downstream examples,video curation pipeline,UNKNOWN,Industrial-scale world foundation model framing for physical AI.,Platform paper; evaluation breadth may outpace directly comparable benchmark evidence.,Section 07 should note this as evidence of industrial consolidation around 'world foundation models'.,candidate,P068_nvidia2025cosmos.md
P069,VideoWorld: Exploring Knowledge Learning from Unlabeled Videos,Zhongwei Ren; Yunchao Wei; Xun Guo; Yao Zhao; Bingyi Kang; Jiashi Feng; Xiaojie Jin,2025,arXiv,2501.09781,UNKNOWN,https://arxiv.org/abs/2501.09781,ren2025videoworld,generative_simulation,video_only_world_model,knowledge learning from unlabeled video,unlabeled video,autoregressive video / control behavior,autoregressive video model,latent dynamics model within video generator,visual-change-centered representation,video-only pretraining with downstream control,Video-GoBench; CALVIN; RLBench,unlabeled videos,Go performance; robotic control performance,Direct evidence for video-only knowledge/world-model claims beyond text supervision.,Strong claims about knowledge/rules still rely on task-specific downstream demonstrations.,Section 07 needs it because the manuscript already points to VideoWorld as an incomplete but relevant addition.,core,P069_ren2025videoworld.md
P070,Vid2World: Crafting Video Diffusion Models to Interactive World Models,Siqiao Huang; Jialong Wu; Qixing Zhou; Shangchen Miao; Mingsheng Long,2025,arXiv,2505.14357,UNKNOWN,https://arxiv.org/abs/2505.14357,huang2025vid2world,generative_simulation,interactive_diffusion_world_model,interactive world modeling,video diffusion priors + actions,interactive future video,diffusion world model,causalized autoregressive video diffusion + causal action guidance,pretrained video dynamics,action-conditioned,robot manipulation; game simulation,UNKNOWN,UNKNOWN,Perhaps the cleanest direct answer to the question 'how do pretrained video models become interactive world models?'.,Still early and benchmark-bounded; physical validity is not guaranteed by interactivity.,Core Section 07 paper because it directly refines the manuscript's video-generation/world-model boundary.,core,P070_huang2025vid2world.md
P071,PHYRE: A New Benchmark for Physical Reasoning,Anton Bakhtin; Laurens van der Maaten; Justin Johnson; Laura Gustafson; Ross Girshick,2019,arXiv,1908.05656,UNKNOWN,https://arxiv.org/abs/1908.05656,bakhtin2019phyre,evaluation,physical_reasoning_benchmark,physical reasoning,2D physical puzzles,action solutions / success,benchmark,N/A,classical mechanics puzzles,action-based puzzle solving,PHYRE,PHYRE,sample efficiency; generalization,Canonical benchmark for learning useful models of physics under intervention.,2D puzzle world; far from open-ended real video.,Section 08 should cite it when discussing intervention-based physical evaluation.,core,P071_bakhtin2019phyre.md
P072,CLEVRER: CoLlision Events for Video REpresentation and Reasoning,Kexin Yi; Chuang Gan; Yunzhu Li; Pushmeet Kohli; Jiajun Wu; Antonio Torralba; Joshua B. Tenenbaum,2019,arXiv,1910.01442,UNKNOWN,https://arxiv.org/abs/1910.01442,yi2019clevrer,evaluation,causal_video_reasoning,video reasoning,video + language questions,answers,benchmark,N/A,causal event structure,predictive / explanatory / counterfactual queries,CLEVRER,CLEVRER,question answering accuracy,Benchmark for predictive and counterfactual reasoning over physical videos.,Synthetic environment and QA format; not direct simulator evaluation.,Section 08 can use it to strengthen causal/counterfactual evaluation discussion.,core,P072_yi2019clevrer.md
P073,Physion: Evaluating Physical Prediction from Vision in Humans and Machines,Daniel M. Bear; Elias Wang; Damian Mrowca; Felix J. Binder; Hsiao-Yu Fish Tung; R. T. Pramod; Cameron Holdaway; Sirui Tao; Kevin Smith; Fan-Yun Sun; Li Fei-Fei; Nancy Kanwisher; Joshua B. Tenenbaum; Daniel L. K. Yamins; Judith E. Fan,2021,arXiv,2106.08261,UNKNOWN,https://arxiv.org/abs/2106.08261,bear2021physion,evaluation,physical_prediction_benchmark,physical prediction from vision,video,future physical outcomes / judgments,benchmark,N/A,broad physical phenomena,predictive judgment,Physion,Physion,benchmark accuracy vs human behavior,Adds a realistic physical-prediction benchmark with explicit human-machine comparison.,"Benchmark, not a world model; still simulation-based.",Section 08 should use it to move beyond text-to-video physical eval alone.,core,P073_bear2021physion.md
P074,VideoPhy: Evaluating Physical Commonsense for Video Generation,Hritik Bansal; Zongyu Lin; Tianyi Xie; Zeshun Zong; Michal Yarom; Yonatan Bitton; Chenfanfu Jiang; Yizhou Sun; Kai-Wei Chang; Aditya Grover,2024,arXiv,2406.03520,UNKNOWN,https://arxiv.org/abs/2406.03520,bansal2024videophy,evaluation,physical_commonsense_t2v,physical commonsense evaluation for video generation,text prompts + generated video,human / automatic scores,benchmark + evaluator,N/A,material interaction categories,text-conditioned generation evaluation,VideoPhy,prompts over solid-solid; solid-fluid; fluid-fluid interactions,human eval; VideoCon-Physics,Directly operationalizes the manuscript's realism-versus-physics thesis for generated videos.,Focused on T2V outputs rather than full interactive world-model rollouts.,"Section 08 core paper; already present in manuscript, but should anchor a fuller benchmark comparison.",core,P074_bansal2024videophy.md
P075,Towards World Simulator: Crafting Physical Commonsense-Based Benchmark for Video Generation,Fanqing Meng; Jiaqi Liao; Xinyu Tan; Wenqi Shao; Quanfeng Lu; Kaipeng Zhang; Yu Cheng; Dianqi Li; Yu Qiao; Ping Luo,2024,arXiv,2410.05363,UNKNOWN,https://arxiv.org/abs/2410.05363,meng2024phygenbench,evaluation,physical_commonsense_t2v,benchmarking physical commonsense in video generation,text prompts + generated video,benchmark scores,benchmark + evaluator,N/A,27 physical laws across four domains,text-conditioned evaluation,PhyGenBench / PhyGenEval,160 prompts across 27 laws,automated evaluation aligned with human feedback,The most systematic law-level physical commonsense benchmark/evaluator pair in this group.,Still centered on prompt-conditioned generation rather than interactive planning.,Section 08 needs it to broaden beyond VideoPhy and to discuss law coverage more concretely.,core,P075_meng2024phygenbench.md
P076,How Far is Video Generation from World Model: A Physical Law Perspective,Bingyi Kang; Yang Yue; Rui Lu; Zhijie Lin; Yang Zhao; Kaixin Wang; Gao Huang; Jiashi Feng,2024,arXiv,2411.02385,UNKNOWN,https://arxiv.org/abs/2411.02385,kang2024howfar,evaluation,physical_law_generalization,evaluating physical law learning in video generation,initial frames,predicted videos / law adherence,evaluation testbed,2D simulation testbed for diffusion video models,classical mechanics laws,future prediction,physical law evaluation,2D simulation testbed,in-distribution; OOD; combinatorial generalization,Directly tests whether video generation models learn abstract physics or only case-based matching.,Synthetic 2D testbed may understate capabilities in broader natural-video settings.,Section 08 should use it to avoid overclaiming that larger video models discover laws automatically.,core,P076_kang2024howfar.md
P077,Do generative video models learn physical principles from watching videos?,Saman Motamed; Laura Culp; Kevin Swersky; Priyank Jaini; Robert Geirhos,2025,arXiv,2501.09038,UNKNOWN,https://arxiv.org/abs/2501.09038,motamed2025physicsiq,evaluation,physics_benchmark,physical principle evaluation,video generation models,benchmark scores,benchmark paper,N/A,fluids; optics; mechanics; magnetism; thermodynamics,model evaluation,Physics-IQ,Physics-IQ,physics benchmark score,Broadens physical evaluation beyond simple contact events and emphasizes realism-versus-physics dissociation.,Benchmark framing centers on generative video models rather than interactive agents.,Section 08 can cite it whenever arguing that visual realism is not equivalent to physical understanding.,core,P077_motamed2025physicsiq.md
P078,WorldScore: A Unified Evaluation Benchmark for World Generation,Haoyi Duan; Hong-Xing Yu; Sirui Chen; Li Fei-Fei; Jiajun Wu,2025,arXiv,2504.00983,UNKNOWN,https://arxiv.org/abs/2504.00983,duan2025worldscore,evaluation,world_generation_benchmark,world generation evaluation,layout / camera trajectory specifications,generated worlds / next scenes,benchmark,N/A,explicit layout and camera control,controllability evaluation,WorldScore,"3,000 test examples",controllability; quality; dynamics,Broader world-generation evaluation that complements physics-only benchmarks with controllability and dynamics measures.,Not specifically a physical-law benchmark; relevance is broader than video world models alone.,"Best treated as a candidate Section 08 addition for a broader evaluation taxonomy, not a central physics citation.",candidate,P078_duan2025worldscore.md
```

## BibTeX entries

以下對應 Part 3。BibTeX key 與上面 CSV 一致；為了避免不必要的 venue/DOI 幻覺，我一律採取 **arXiv-first** 的保守寫法。對需要最終投稿版 bibliography 精修的條目，優先回頭手動補 P042 的 original conference entry 與 P045 的完整 metadata。citeturn31academia1turn0academia0

```bibtex
@article{shi2015convlstm,
  title = {Convolutional LSTM Network: A Machine Learning Approach for Precipitation Nowcasting},
  author = {Xingjian Shi and Zhourong Chen and Hao Wang and Dit-Yan Yeung and Wai-kin Wong and Wang-chun Woo},
  journal = {arXiv preprint arXiv:1506.04214},
  year = {2015},
  eprint = {1506.04214},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/1506.04214}
}

@article{wang2021predrnn,
  title = {PredRNN: A Recurrent Neural Network for Spatiotemporal Predictive Learning},
  author = {Yunbo Wang and Haixu Wu and Jianjin Zhang and Zhifeng Gao and Jianmin Wang and Philip S. Yu and Mingsheng Long},
  journal = {arXiv preprint arXiv:2103.09504},
  year = {2021},
  eprint = {2103.09504},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2103.09504}
}

@article{wang2018predrnnpp,
  title = {PredRNN++: Towards A Resolution of the Deep-in-Time Dilemma in Spatiotemporal Predictive Learning},
  author = {Yunbo Wang and Zhifeng Gao and Mingsheng Long and Jianmin Wang and Philip S. Yu},
  journal = {arXiv preprint arXiv:1804.06300},
  year = {2018},
  eprint = {1804.06300},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/1804.06300}
}

@article{wang2018mim,
  title = {Memory In Memory: A Predictive Neural Network for Learning Higher-Order Non-Stationarity from Spatiotemporal Dynamics},
  author = {Yunbo Wang and Jianjin Zhang and Hongyu Zhu and Mingsheng Long and Jianmin Wang and Philip S. Yu},
  journal = {arXiv preprint arXiv:1811.07490},
  year = {2018},
  eprint = {1811.07490},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/1811.07490}
}

@misc{unknown_e3dlstm,
  title = {Eidetic 3D LSTM: A Model for Video Prediction and Beyond},
  author = {UNKNOWN},
  year = {UNKNOWN},
  howpublished = {UNKNOWN},
  url = {UNKNOWN},
  note = {Primary-source metadata unresolved during this audit}
}

@article{gao2022simvp,
  title = {SimVP: Simpler yet Better Video Prediction},
  author = {Zhangyang Gao and Cheng Tan and Lirong Wu and Stan Z. Li},
  journal = {arXiv preprint arXiv:2206.05099},
  year = {2022},
  eprint = {2206.05099},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2206.05099}
}

@article{leguen2020phydnet,
  title = {Disentangling Physical Dynamics from Unknown Factors for Unsupervised Video Prediction},
  author = {Vincent Le Guen and Nicolas Thome},
  journal = {arXiv preprint arXiv:2003.01460},
  year = {2020},
  eprint = {2003.01460},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2003.01460}
}

@article{voleti2022mcvd,
  title = {MCVD: Masked Conditional Video Diffusion for Prediction, Generation, and Interpolation},
  author = {Vikram Voleti and Alexia Jolicoeur-Martineau and Christopher Pal},
  journal = {arXiv preprint arXiv:2205.09853},
  year = {2022},
  eprint = {2205.09853},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2205.09853}
}

@article{yan2021videogpt,
  title = {VideoGPT: Video Generation using VQ-VAE and Transformers},
  author = {Wilson Yan and Yunzhi Zhang and Pieter Abbeel and Aravind Srinivas},
  journal = {arXiv preprint arXiv:2104.10157},
  year = {2021},
  eprint = {2104.10157},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2104.10157}
}

@article{locatello2020slotattention,
  title = {Object-Centric Learning with Slot Attention},
  author = {Francesco Locatello and Dirk Weissenborn and Thomas Unterthiner and Aravindh Mahendran and Georg Heigold and Jakob Uszkoreit and Alexey Dosovitskiy and Thomas Kipf},
  journal = {arXiv preprint arXiv:2006.15055},
  year = {2020},
  eprint = {2006.15055},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2006.15055}
}

@article{kipf2021savi,
  title = {Conditional Object-Centric Learning from Video},
  author = {Thomas Kipf and Gamaleldin F. Elsayed and Aravindh Mahendran and Austin Stone and Sara Sabour and Georg Heigold and Rico Jonschkowski and Alexey Dosovitskiy and Klaus Greff},
  journal = {arXiv preprint arXiv:2111.12594},
  year = {2021},
  eprint = {2111.12594},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2111.12594}
}

@article{elsayed2022savipp,
  title = {SAVi++: Towards End-to-End Object-Centric Learning from Real-World Videos},
  author = {Gamaleldin F. Elsayed and Aravindh Mahendran and Sjoerd van Steenkiste and Klaus Greff and Michael C. Mozer and Thomas Kipf},
  journal = {arXiv preprint arXiv:2206.07764},
  year = {2022},
  eprint = {2206.07764},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2206.07764}
}

@article{kipf2019cswm,
  title = {Contrastive Learning of Structured World Models},
  author = {Thomas Kipf and Elise van der Pol and Max Welling},
  journal = {arXiv preprint arXiv:1911.12247},
  year = {2019},
  eprint = {1911.12247},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/1911.12247}
}

@article{zadaianchuk2023temporalfeaturesim,
  title = {Object-Centric Learning for Real-World Videos by Predicting Temporal Feature Similarities},
  author = {Andrii Zadaianchuk and Maximilian Seitzer and Georg Martius},
  journal = {arXiv preprint arXiv:2306.04829},
  year = {2023},
  eprint = {2306.04829},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2306.04829}
}

@article{wu2022slotformer,
  title = {SlotFormer: Unsupervised Visual Dynamics Simulation with Object-Centric Models},
  author = {Ziyi Wu and Nikita Dvornik and Klaus Greff and Thomas Kipf and Animesh Garg},
  journal = {arXiv preprint arXiv:2210.05861},
  year = {2022},
  eprint = {2210.05861},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2210.05861}
}

@article{hafner2020dreamerv2,
  title = {Mastering Atari with Discrete World Models},
  author = {Danijar Hafner and Timothy Lillicrap and Mohammad Norouzi and Jimmy Ba},
  journal = {arXiv preprint arXiv:2010.02193},
  year = {2020},
  eprint = {2010.02193},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2010.02193}
}

@article{hafner2023dreamerv3,
  title = {Mastering Diverse Domains through World Models},
  author = {Danijar Hafner and Jurgis Pasukonis and Jimmy Ba and Timothy Lillicrap},
  journal = {arXiv preprint arXiv:2301.04104},
  year = {2023},
  eprint = {2301.04104},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2301.04104}
}

@article{micheli2022iris,
  title = {Transformers are Sample-Efficient World Models},
  author = {Vincent Micheli and Eloi Alonso and François Fleuret},
  journal = {arXiv preprint arXiv:2209.00588},
  year = {2022},
  eprint = {2209.00588},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2209.00588}
}

@article{wu2022daydreamer,
  title = {DayDreamer: World Models for Physical Robot Learning},
  author = {Philipp Wu and Alejandro Escontrela and Danijar Hafner and Ken Goldberg and Pieter Abbeel},
  journal = {arXiv preprint arXiv:2206.14176},
  year = {2022},
  eprint = {2206.14176},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2206.14176}
}

@article{zhou2024dinowm,
  title = {DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning},
  author = {Gaoyue Zhou and Hengkai Pan and Yann LeCun and Lerrel Pinto},
  journal = {arXiv preprint arXiv:2411.04983},
  year = {2024},
  eprint = {2411.04983},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2411.04983}
}

@article{wu2023contextwm,
  title = {Pre-training Contextualized World Models with In-the-wild Videos for Reinforcement Learning},
  author = {Jialong Wu and Haoyu Ma and Chaoyi Deng and Mingsheng Long},
  journal = {arXiv preprint arXiv:2305.18499},
  year = {2023},
  eprint = {2305.18499},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2305.18499}
}

@article{wu2024ivideogpt,
  title = {iVideoGPT: Interactive VideoGPTs are Scalable World Models},
  author = {Jialong Wu and Shaofeng Yin and Ningya Feng and Xu He and Dong Li and Jianye Hao and Mingsheng Long},
  journal = {arXiv preprint arXiv:2405.15223},
  year = {2024},
  eprint = {2405.15223},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2405.15223}
}

@misc{brooks2024sorareport,
  title = {Video generation models as world simulators},
  author = {Tim Brooks and Bill Peebles and Connor Holmes and Will DePue and Yufei Guo},
  year = {2024},
  howpublished = {OpenAI technical report},
  url = {https://openai.com/index/video-generation-models-as-world-simulators/},
  note = {Accessed 2026-05-30}
}

@article{yang2023unisim,
  title = {Learning Interactive Real-World Simulators},
  author = {Sherry Yang and Yilun Du and Kamyar Ghasemipour and Jonathan Tompson and Leslie Kaelbling and Dale Schuurmans and Pieter Abbeel},
  journal = {arXiv preprint arXiv:2310.06114},
  year = {2023},
  eprint = {2310.06114},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2310.06114}
}

@article{hu2023gaia1,
  title = {GAIA-1: A Generative World Model for Autonomous Driving},
  author = {Anthony Hu and Lloyd Russell and Hudson Yeo and Zak Murez and George Fedoseev and Alex Kendall and Jamie Shotton and Gianluca Corrado},
  journal = {arXiv preprint arXiv:2309.17080},
  year = {2023},
  eprint = {2309.17080},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2309.17080}
}

@article{wang2023drivedreamer,
  title = {DriveDreamer: Towards Real-world-driven World Models for Autonomous Driving},
  author = {Xiaofeng Wang and Zheng Zhu and Guan Huang and Xinze Chen and Jiagang Zhu and Jiwen Lu},
  journal = {arXiv preprint arXiv:2309.09777},
  year = {2023},
  eprint = {2309.09777},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2309.09777}
}

@article{zhao2024drivedreamer2,
  title = {DriveDreamer-2: LLM-Enhanced World Models for Diverse Driving Video Generation},
  author = {Guosheng Zhao and Xiaofeng Wang and Zheng Zhu and Xinze Chen and Guan Huang and Xiaoyi Bao and Xingang Wang},
  journal = {arXiv preprint arXiv:2403.06845},
  year = {2024},
  eprint = {2403.06845},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2403.06845}
}

@article{nvidia2025cosmos,
  title = {Cosmos World Foundation Model Platform for Physical AI},
  author = {{NVIDIA et al.}},
  journal = {arXiv preprint arXiv:2501.03575},
  year = {2025},
  eprint = {2501.03575},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2501.03575}
}

@article{ren2025videoworld,
  title = {VideoWorld: Exploring Knowledge Learning from Unlabeled Videos},
  author = {Zhongwei Ren and Yunchao Wei and Xun Guo and Yao Zhao and Bingyi Kang and Jiashi Feng and Xiaojie Jin},
  journal = {arXiv preprint arXiv:2501.09781},
  year = {2025},
  eprint = {2501.09781},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2501.09781}
}

@article{huang2025vid2world,
  title = {Vid2World: Crafting Video Diffusion Models to Interactive World Models},
  author = {Siqiao Huang and Jialong Wu and Qixing Zhou and Shangchen Miao and Mingsheng Long},
  journal = {arXiv preprint arXiv:2505.14357},
  year = {2025},
  eprint = {2505.14357},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2505.14357}
}

@article{bakhtin2019phyre,
  title = {PHYRE: A New Benchmark for Physical Reasoning},
  author = {Anton Bakhtin and Laurens van der Maaten and Justin Johnson and Laura Gustafson and Ross Girshick},
  journal = {arXiv preprint arXiv:1908.05656},
  year = {2019},
  eprint = {1908.05656},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/1908.05656}
}

@article{yi2019clevrer,
  title = {CLEVRER: CoLlision Events for Video REpresentation and Reasoning},
  author = {Kexin Yi and Chuang Gan and Yunzhu Li and Pushmeet Kohli and Jiajun Wu and Antonio Torralba and Joshua B. Tenenbaum},
  journal = {arXiv preprint arXiv:1910.01442},
  year = {2019},
  eprint = {1910.01442},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/1910.01442}
}

@article{bear2021physion,
  title = {Physion: Evaluating Physical Prediction from Vision in Humans and Machines},
  author = {Daniel M. Bear and Elias Wang and Damian Mrowca and Felix J. Binder and Hsiao-Yu Fish Tung and R. T. Pramod and Cameron Holdaway and Sirui Tao and Kevin Smith and Fan-Yun Sun and Li Fei-Fei and Nancy Kanwisher and Joshua B. Tenenbaum and Daniel L. K. Yamins and Judith E. Fan},
  journal = {arXiv preprint arXiv:2106.08261},
  year = {2021},
  eprint = {2106.08261},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2106.08261}
}

@article{bansal2024videophy,
  title = {VideoPhy: Evaluating Physical Commonsense for Video Generation},
  author = {Hritik Bansal and Zongyu Lin and Tianyi Xie and Zeshun Zong and Michal Yarom and Yonatan Bitton and Chenfanfu Jiang and Yizhou Sun and Kai-Wei Chang and Aditya Grover},
  journal = {arXiv preprint arXiv:2406.03520},
  year = {2024},
  eprint = {2406.03520},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2406.03520}
}

@article{meng2024phygenbench,
  title = {Towards World Simulator: Crafting Physical Commonsense-Based Benchmark for Video Generation},
  author = {Fanqing Meng and Jiaqi Liao and Xinyu Tan and Wenqi Shao and Quanfeng Lu and Kaipeng Zhang and Yu Cheng and Dianqi Li and Yu Qiao and Ping Luo},
  journal = {arXiv preprint arXiv:2410.05363},
  year = {2024},
  eprint = {2410.05363},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2410.05363}
}

@article{kang2024howfar,
  title = {How Far is Video Generation from World Model: A Physical Law Perspective},
  author = {Bingyi Kang and Yang Yue and Rui Lu and Zhijie Lin and Yang Zhao and Kaixin Wang and Gao Huang and Jiashi Feng},
  journal = {arXiv preprint arXiv:2411.02385},
  year = {2024},
  eprint = {2411.02385},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2411.02385}
}

@article{motamed2025physicsiq,
  title = {Do generative video models learn physical principles from watching videos?},
  author = {Saman Motamed and Laura Culp and Kevin Swersky and Priyank Jaini and Robert Geirhos},
  journal = {arXiv preprint arXiv:2501.09038},
  year = {2025},
  eprint = {2501.09038},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2501.09038}
}

@article{duan2025worldscore,
  title = {WorldScore: A Unified Evaluation Benchmark for World Generation},
  author = {Haoyi Duan and Hong-Xing Yu and Sirui Chen and Li Fei-Fei and Jiajun Wu},
  journal = {arXiv preprint arXiv:2504.00983},
  year = {2025},
  eprint = {2504.00983},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2504.00983}
}
```

## Section integration guide

以下對應 Part 4。這張表是直接針對你目前稿件的 Section 04–08 重寫路徑而做；因為稿件本身已在 Section 4、6、7、8 明確承認多個分支尚未 evidence-ready 或仍是 metadata-only coverage target，所以「加哪些 paper」不是附加美化，而是結構性補洞。fileciteturn0file0

| Manuscript section | Which new papers should be added | Which old claims they support | Which new comparison dimensions they enable | What overclaims they help avoid |
|---|---|---|---|---|
| Section 04 | P041–P049，尤其是 P046 SimVP、P047 PhyDNet、P048 MCVD、P049 VideoGPT。 | 把目前只靠 Atari action-conditioned prediction、robot video prediction、SV2P 的窄證據基礎，擴成真正具有代表性的 baseline layer；也直接填上你稿子自己承認的「architecture-oriented baselines not yet evidence-ready」缺口。 | recurrent vs CNN vs diffusion vs tokenized prediction；deterministic vs stochastic vs physics-informed forecasting；simplicity vs complexity；passive prediction vs action-conditioned use。 | 避免讀者覺得你把「video prediction」縮減成少數早期 paper，也避免後面 object-centric / latent / diffusion 分支缺乏公平 baseline 對照。 |
| Section 05 | P050–P055，尤其是 P050 Slot Attention、P051 SAVi、P052 SAVi++、P053 C-SWM、P055 SlotFormer。 | 把目前「slot-based and compositional extensions are coverage targets」那一段，升級成真正可綜合 object discovery、temporal consistency、structured latent transitions、planning-relevant slot dynamics 的 section。 | explicit objects vs learned slots；synthetic vs real-world video；reconstruction vs contrastive learning；segmentation hints / depth cues vs minimal supervision；representation learning vs dynamics simulation vs planning。 | 避免過度暗示 object-centric 證據只等同於 IN / VIN / O2P2，也避免讓讀者以為 object-centric 方法一定要 privileged states 或 proposals。 |
| Section 06 | P056–P062，尤其是 P056 DreamerV2、P057 DreamerV3、P058 IRIS、P059 DayDreamer、P060 DINO-WM、P061 ContextWM。 | 直接填掉你稿件明講的 DreamerV2、IRIS、DayDreamer、DINO-WM、ContextWM placeholders，也把 latent world models 的故事從 PlaNet + Dreamer 2020 擴到 discrete、transformer、feature-space、real robot、in-the-wild pretraining。 | continuous vs discrete latents；RSSM vs Transformer；online planning vs amortized policy learning；simulator control vs physical robot deployment；learned latents vs pre-trained features；narrow-domain training vs in-the-wild pretraining。 | 避免讓 latent-world-model storyline 停在 2019–2020，也避免把 latent world models 說成只在模擬器、只做重建、或只適用於 RSSM 家族。 |
| Section 07 | P063–P070，尤其是 P063 Sora report、P064 UniSim、P065 GAIA-1、P066 DriveDreamer、P069 VideoWorld、P070 Vid2World。 | 這些 paper 正是你 diffusion / interactive section 所缺的主體證據；目前稿子對 broader diffusion-video lineage、video-only world models、VideoWorld/Vid2World 都還停在 provisional coverage mode。 | from-scratch world models vs adaptation of pretrained video generators；image-space diffusion vs token/autoregressive worlds；known actions vs language conditioning vs learned controls；general internet video vs driving vs embodied interaction；qualitative simulator claims vs tested interactivity。 | 避免把 visual realism 直接等同 simulator competence；避免把所有 controllable generation 都當成 grounded action-conditioned world modeling；也避免把 Sora-style report 寫成「已證明 video models 是 world simulators」。OpenAI 自己的 technical report 同時聲稱 scaling is promising，也明確列出 physics inaccuracies、state-change failures、long-duration incoherencies 等限制。citeturn23view0turn48view0 |
| Section 08 | P071–P078，尤其是 P071 PHYRE、P072 CLEVRER、P073 Physion、P074 VideoPhy、P075 PhyGenBench、P076 How Far、P077 Physics-IQ。 | 把目前 metadata-only benchmark placeholders 變成一個真正完整的 evaluation framework：intervention、causal / counterfactual reasoning、physical prediction、text-to-video physical commonsense、physical-law generalization、broader world generation。 | reconstruction vs task utility vs causal / counterfactual reasoning vs physical-law adherence vs controllability；puzzle/action tasks vs QA benchmarks vs T2V evaluation；human judgments vs automatic evaluators；narrow physics checks vs broader world-generation evaluation。 | 避免把 realism metrics、task return、或 VideoPhy 單一 benchmark 當成 world-model validity 的充分證據。尤其 P075–P077 很有價值，因為它們共同支持一個更精確的結論：**visual realism 與 physical understanding 並不等價**。citeturn24academia2turn25academia1turn25academia0turn25academia2 |