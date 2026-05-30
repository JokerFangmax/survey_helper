以下是我按**critical survey-paper reviewer**视角给出的评审。整体判断：**方向很好，但目前还不是投稿级 survey；更像一篇结构清晰的 extended position paper / preliminary survey draft。需要 major revision。**

我主要基于你上传的 manuscript 进行评价，同时补充了近期相关文献检查。你的稿件已经明确提出：**video generation 的视觉真实感不能等价于 world-model validity；真正的 predictive world model 应该从 action / control / physical consistency / planning utility / evaluation criteria 等角度判断**。这一点在摘要、引言和 taxonomy 中反复出现，是全文最有价值的主线 。

---

## 1. Major strengths

**第一，论文有一个清楚且有潜力的 thesis。**
你的核心论点不是简单综述“video prediction / video generation / world model 都有哪些论文”，而是强调：**世界模型的有效性不应由视觉 plausibility 单独决定，而应由预测、控制、物理一致性、交互性和评估协议共同决定**。这比普通 video generation survey 更有辨识度。

**第二，taxonomy 的五个轴是合理的。**
“modeling goal / representation / dynamics / conditioning / evaluation” 这五个维度能够覆盖 video prediction、latent world model、object-centric dynamics、diffusion simulator、interactive environment 等不同分支。尤其把 **evaluation** 作为 taxonomy axis，而不是最后附带讨论，是一个正确方向 。

**第三，文章不是完全在 listing papers。**
你已经在尝试 synthesis，例如反复提出 abstraction–fidelity trade-off：latent state 有利于 planning efficiency，而 image-space diffusion 可能保留 control-relevant visual details。这个对比贯穿 Introduction、Section 6 和 Section 7，是目前最像“综述贡献”的地方。

**第四，作者态度谨慎。**
文中多处明确说明某些 diffusion-video、benchmark、latent-control papers 目前只是 coverage targets，还没有 evidence-ready notes。这避免了直接过度 claim。但这个优点同时也是当前稿件最大的问题之一：**这些内部工作流痕迹不应该出现在最终投稿稿件中**。

---

## 2. Major weaknesses

**最大问题：literature coverage 明显不足。**
全文 references 只有 23 篇左右，而且许多关键类别只靠 1–3 篇支撑。例如 diffusion world models 基本由 DIAMOND 和 Genie 支撑，physical evaluation 主要由 VideoPhy 支撑，object-centric dynamics 主要由 Interaction Networks / VIN / O2P2 支撑。对于 survey 来说，这会被审稿人认为 coverage 不充分，尤其是题目覆盖了 “Generative Simulation and Physical Dynamics” 这么大的范围。

**第二，稿件里出现了过多“内部笔记系统”的痕迹。**
例如 “completed notes”、“evidence-ready examples”、“P004 / P005 / P037”、“UNKNOWN evidence fields”、“claim bank” 等表达，在审稿人眼中会非常不正式。它们适合你的本地研究管理流程，但不能出现在最终论文。Table 1 里用 P004、P005 作为 examples，也不符合 survey paper 的学术呈现方式 。

**第三，taxonomy 有用，但原创性还不够锋利。**
五轴 taxonomy 合理，但它目前更像“通用组织框架”，还没有形成一个只有这篇 survey 才有的强视角。近期已有工作也在从 state construction / dynamics modeling / evaluation shift 等角度讨论 video generation as world models，例如 2026 年的 *A Mechanistic View on Video Generation as World Models* 就提出围绕 state construction 和 dynamics modeling 的分类，并强调从 visual fidelity 转向 functional benchmarks ([arXiv][1])。因此你需要更明确地说明：你的 taxonomy 相比已有 survey 的独特贡献在哪里。

**第四，physical dynamics / generative simulation angle 还不够强。**
题目中 “Physical Dynamics” 很显眼，但 Section 5 主要停留在 Interaction Networks、VIN、O2P2 这些经典 object-centric / relational dynamics 工作；Section 8 虽然提到 VideoPhy、PHYRE、CLEVRER、Physion、PhyGenBench、Physics-IQ，但许多只是“待补充”。这会导致题目承诺强，正文证据弱。

**第五，video prediction / video generation / world modeling 的边界定义清楚，但缺少对照表和 failure cases。**
文字上你已经解释了三者差别，但 reviewer 可能仍会问：“哪些 video generation papers 不应算 world models？哪些 video prediction papers 可以算弱 world models？action-conditioned video generation 与 interactive world model 的边界在哪里？” 目前缺少一个 crisp decision table。

**第六，正文重复较多。**
“visual realism is not enough”“task return is not physical validity”“latent abstraction vs image-space fidelity” 这些观点多次出现，但每次推进有限。综述需要重复主线，但更需要每次重复都带来新的比较维度、证据或设计原则。

**第七，Introduction 和 Conclusion 在概念上匹配，但 body 还没有完全兑现。**
Introduction 承诺要系统比较 video prediction、latent world models、diffusion-based simulators、interactive environments、physical evaluation。Conclusion 也总结了这些分支。但正文目前每个分支的 coverage 深度不均衡，导致结论听起来正确，但证据基础偏薄。

---

## 3. Section-by-section review

| Section                                          | 评价                                                       | 主要修改建议                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------ | -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Abstract                                         | 清楚、有 thesis，但略像 position statement。                      | 加入更具体的 survey contribution：例如“we compare X families across Y criteria and identify Z evaluation mismatch”。                                                                                                                                                                                                                     |
| Introduction                                     | 主线明确，能区分 video generation 与 world modeling。              | 删除“completed notes / coverage targets”这类内部表达；把 scope 写成正式 criteria，而不是写成当前证据状态。                                                                                                                                                                                                                                                |
| Section 2 Background and Scope                   | 是全文较强部分，定义 world model beyond future frames 很重要。         | 建议加入一个正式定义：**A video world model is a learned transition model over observations, latent states, or tokens that supports counterfactual rollout under actions/controls or physically meaningful evaluation.**                                                                                                                  |
| Section 3 Taxonomy                               | 框架合理，但 Table 1 太像内部工作表。                                  | Table 1 应改成正式 matrix：rows = families，columns = goal / state / transition / conditioning / evaluation / representative papers / limitations。不要用 P004。                                                                                                                                                                           |
| Section 4 Video Prediction                       | 能说明 action-conditioned prediction 是通往 world modeling 的桥。 | 覆盖太窄，需要加入 SimVP、MCVD、VideoGPT、PhyDNet、PredRNN/ConvLSTM 类方法，并解释哪些只是 video prediction baseline，哪些与 world modeling 相关。MCVD 是 conditional video diffusion for prediction/generation/interpolation，应该至少作为 diffusion-video prediction bridge 出现 ([NeurIPS Papers][2])。                                                               |
| Section 5 Object-Centric Dynamics                | 逻辑清楚，是 physical dynamics angle 的基础。                      | 需要补 Slot Attention、SAVi、C-SWM、SlotFormer 等 object-centric / slot-based dynamics。SlotFormer 明确做 object-centric visual dynamics simulation，并连接 video prediction、VQA 和 planning，与你的主题高度相关 ([arXiv][3])。                                                                                                                           |
| Section 6 Latent World Models                    | PlaNet / Dreamer 线索正确。                                   | 必须补 DreamerV2/V3、IRIS、DayDreamer、DINO-WM。DreamerV3 已经被定位为跨 150+ tasks 的通用 world-model control 方法，IRIS 则是 discrete autoencoder + autoregressive Transformer world model，DayDreamer 是 real-robot world model 关键证据，DINO-WM 代表 feature-space world model ([Nature][4])。                                                            |
| Section 7 Diffusion and Interactive World Models | 方向非常重要，但证据太薄。                                            | 需要补 Sora discussion、UniSim、GAIA-1、DriveDreamer、Cosmos、VideoWorld、Vid2World。OpenAI 的 Sora report 明确提出 scaling video models toward general-purpose simulators，但这应被作为 contested claim，而不是直接接受 ([OpenAI][5])。Vid2World、UniSim、GAIA-1 都直接对应 interactive / controllable / action-conditioned generative simulator ([OpenReview][6])。 |
| Section 8 Evaluation                             | 是全文最有潜力的 section。                                        | 需要从“open challenges list”升级为系统 evaluation framework。补充 PHYRE、CLEVRER、Physion、PhyGenBench、How Far Is Video Generation from World Model、Physics-IQ。PhyGenBench 和 How Far Is Video Generation from World Model 都直接支撑 physical-law evaluation，不应只是 future coverage target ([OpenReview][7])。                                       |
| Conclusion                                       | 与 Introduction 匹配，但偏泛。                                   | 应该回扣 taxonomy，并给出 3–5 条 design principles，而不是只重复“visual realism is not enough”。                                                                                                                                                                                                                                                |

---

## 4. Missing literature

下面这些不是全部都要详细展开，但至少需要进入 paper pool，并在正文中按 taxonomy 放入合适位置。

### A. Video prediction / visual dynamics baselines

需要补：

* **ConvLSTM / PredRNN / PredRNN++ / MIM / E3D-LSTM**：经典 recurrent video prediction backbone。
* **SimVP**：重要 baseline，因为它质疑复杂 architecture 是否必要，提出简单 CNN + MSE 也能在多个 prediction benchmark 上取得强结果 ([CVF 開放存取][8])。
* **PhyDNet**：与你的 physical dynamics 主题直接相关，因为它尝试 disentangle PDE-like physical dynamics 与 unknown factors ([CVF 開放存取][9])。
* **MCVD**：连接 video prediction 与 diffusion generation 的关键桥梁，能做 prediction、generation、interpolation ([NeurIPS Papers][2])。
* **VideoGPT**：tokenized video generation / action-conditional generation 的早期代表，适合放在 tokenized video dynamics 或 generation-to-world-model bridge 中 ([arXiv][10])。

### B. Object-centric / structured world models

需要补：

* **Slot Attention**：object-centric representation 的基础方法，虽然不是 dynamics paper，但为后续 slot-based world models 提供基础 ([proceedings.neurips.cc][11])。
* **SAVi / SAVi++**：video object-centric representation 和 temporal consistency。
* **C-SWM**：contrastive structured world models，直接与 object-centric model-based RL 相关 ([OpenReview][12])。
* **SlotFormer**：非常关键，标题本身就是 *Unsupervised Visual Dynamics Simulation with Object-Centric Models*，并报告 video prediction、future reasoning、goal-conditioned planning 等任务 ([arXiv][3])。

### C. Latent / token / feature-space world models

需要补：

* **DreamerV2 / DreamerV3**：DreamerV3 是目前 world-model control 系列中非常重要的进展，不能只停在 Dreamer 2020 ([Nature][4])。
* **IRIS**：discrete autoencoder + autoregressive Transformer world model，是 tokenized latent world model 的关键代表 ([arXiv][13])。
* **DayDreamer**：real-world physical robot learning，能显著增强你的 embodied / physical angle ([arXiv][14])。
* **DINO-WM / DINO-world**：feature-space world models，正好填补 “not pixel reconstruction, not compact learned-from-scratch latent” 这个中间路线 ([OpenReview][15])。

### D. Generative simulation / interactive world models

需要补：

* **Sora / video generation models as world simulators**：必须讨论，但要作为“scale may induce simulator-like capabilities”这一争议命题，不应无条件接受 ([OpenAI][5])。
* **UniSim**：learning interactive real-world simulators，是你的 Section 7 必补论文 ([ICLR 會議記錄][16])。
* **GAIA-1 / DriveDreamer / DriveDreamer-2**：autonomous driving world models，体现 video + action + controllable scenario generation ([arXiv][17])。
* **Cosmos World Foundation Model Platform**：physical AI / world foundation model 方向，适合在 large-scale generative simulators 或 industrial-scale world foundation models 中讨论 ([arXiv][18])。
* **VideoWorld**：unlabeled-video knowledge learning，连接 video-only learning、latent dynamics、planning / robotic control ([arXiv][19])。
* **Vid2World**：明确把 pretrained video diffusion models 转成 interactive world models，是你 Section 7 的核心 missing work ([OpenReview][6])。

### E. Physical evaluation / benchmark literature

需要补：

* **PHYRE, CLEVRER, Physion**：基础 physical reasoning / causal video reasoning benchmark。
* **VideoPhy**：你已经写了，但还需要更系统比较。
* **PhyGenBench / PhyGenEval**：面向 text-to-video physical commonsense correctness，包含物理规律维度和 human-aligned evaluator ([OpenReview][7])。
* **How Far Is Video Generation from World Model**：非常契合你的 thesis，因为它直接检验 video generation models 是否能从视觉数据中学习 physical laws，并强调 in-distribution / OOD / combinatorial generalization ([arXiv][20])。
* **Physics-IQ**：可以作为 newer physical principle evaluation benchmark 补充。

---

## 5. Overclaiming risks

**风险 1：把“video generation may be world simulator”说得太自然。**
你的文章总体是谨慎的，但题目和 Section 7 容易让读者觉得你默认 diffusion/video generation 是 world model。建议明确分级：

1. video generator：生成 plausible clips；
2. predictive video model：conditioned on past frames；
3. action-conditioned predictive model：conditioned on interventions；
4. interactive world model：supports stable controllable rollouts；
5. physical simulator-like world model：supports causal / physical / counterfactual generalization。

**风险 2：把 control return 当成 world-model validity。**
你已经指出这个问题，但需要更强。Atari control return、robot task success、FVD、human preference、physical-law score分别测试不同东西，不能互相替代。

**风险 3：physical dynamics coverage 不足却在标题中承诺过强。**
如果不补 PhyDNet、PHYRE、CLEVRER、Physion、PhyGenBench、How Far、Physics-IQ、physical robot world models，标题中的 “Physical Dynamics” 会显得虚。

**风险 4：taxonomy 看似 comprehensive，但每个 cell 的代表论文太少。**
例如 diffusion world model 只靠 DIAMOND，interactive environment 只靠 Genie，physical benchmark 只靠 VideoPhy，这会让审稿人认为 taxonomy 是先验设计，而不是从 literature 中归纳出来的。

**风险 5：内部术语破坏专业性。**
“completed notes”“UNKNOWN evidence fields”“P004” 这些必须删除。投稿稿件不能暴露你的资料整理状态。

---

## 6. Necessary figures and tables

我建议至少加入以下 5 个核心图表。

**Figure 1：Conceptual boundary diagram**
展示 video prediction、video generation、predictive world model、interactive simulator、physical simulator 的包含/交叉关系。重点标出：action conditioning、latent control、planning utility、physical consistency。

**Figure 2：Taxonomy map**
以五轴 taxonomy 为基础，但不要只列轴。建议画成二维主图：
x-axis = representation abstraction level：pixels → tokens/features → latent states → objects/graphs；
y-axis = interaction/control level：passive → action-conditioned → policy/planning → interactive latent control → physical/counterfactual evaluation。
把代表论文放到图中。

**Table 1：Formal taxonomy matrix**
替代现在的 P004 表。列建议为：family / representative methods / representation / transition mechanism / conditioning / evaluation / strengths / limitations。

**Table 2：Evaluation protocol comparison**
列出 PSNR/SSIM/LPIPS/FVD、control return、planning success、controllability score、physical consistency benchmark、causal reasoning、long-horizon identity consistency。说明每个 metric 测什么、不测什么。

**Figure 3：Abstraction–fidelity trade-off**
展示 latent world models、object-centric models、image-space diffusion simulators 的 trade-off：planning efficiency、visual detail、physical interpretability、long-horizon stability。

**Table 3：Missing benchmark / dataset landscape**
按 benchmark 类型组织：video prediction datasets、robot interaction datasets、physical reasoning benchmarks、T2V physical evaluation、driving simulators、interactive game environments。

---

## 7. Concrete revision plan

### Step 1：重写 thesis statement

现在的 thesis 是有的，但分散。建议在 Introduction 最后明确写成一句：

> This survey argues that video-based world models should be evaluated not by visual realism alone, but by whether their learned state and dynamics support prediction under interventions, controllable rollout, physical and causal consistency, and downstream decision-making.

然后全文每个 section 都回扣这句话。

### Step 2：删除所有内部笔记痕迹

需要全局删除或替换：

* completed notes
* evidence-ready
* coverage targets
* UNKNOWN evidence fields
* claim bank
* P004 / P005 / P037

替换方式：
不要写“this paper is indexed but not evidence-ready”，而是写正式综述语言：

> Recent works such as X, Y, and Z extend this line, but their evaluation settings differ substantially and should not be treated as directly comparable.

### Step 3：扩大文献池到至少 70–100 篇

最低要求不是每篇都详细讲，但每个 family 至少要有：

* canonical papers
* recent representative papers
* evaluation/benchmark papers
* limitations / critique papers

目前 23 篇太少。对于这个题目，投稿级 survey 至少应覆盖 video prediction、model-based RL/world models、object-centric dynamics、video diffusion、interactive simulators、robotics/driving world models、physical evaluation benchmarks、related surveys。

### Step 4：把 Section 4–7 改成“比较型综述”，而不是“分支介绍”

每个方法族都应该回答同一组问题：

1. What is the learned state?
2. What is the transition/dynamics model?
3. What conditioning/intervention signal is supported?
4. What is the rollout mechanism?
5. What is the evaluation protocol?
6. What failure mode remains?

这样 taxonomy 才会真正驱动正文。

### Step 5：强化 physical dynamics 主线

建议新增一个独立 subsection：

**“From visual plausibility to physical-law generalization”**

其中比较：

* object-centric inductive bias：Interaction Networks / VIN / O2P2 / SlotFormer
* physics-informed video prediction：PhyDNet
* physical reasoning benchmarks：PHYRE / CLEVRER / Physion
* T2V physical evaluation：VideoPhy / PhyGenBench / How Far / Physics-IQ
* embodied physical learning：DayDreamer / robot interaction video prediction

这样题目中的 “Physical Dynamics” 才会被正文真正支撑。

### Step 6：重新组织 Section 7

现在 Section 7 的逻辑是对的，但证据太少。建议改成四小节：

1. **Video diffusion as predictive generation**：VDM, MCVD, VideoGPT, Sora-style scaling。
2. **Action-conditioned image-space world models**：DIAMOND, UniSim, Vid2World。
3. **Large-scale interactive / embodied simulators**：Genie, VideoWorld, GAIA, DriveDreamer, Cosmos。
4. **Why these are not automatically physical simulators**：接 Section 8。

### Step 7：把 Conclusion 改成 design principles

Conclusion 不要只是总结各分支。建议最后给出 5 条原则：

1. A world model must specify its state.
2. A world model must specify what interventions it supports.
3. Visual fidelity is insufficient without rollout validity.
4. Control success is insufficient without physical and causal robustness.
5. Future benchmarks should jointly test prediction, control, long-horizon consistency, and physical-law generalization.

---

## 8. Final reviewer-style verdict

**Recommendation: Major Revision.**

这篇 manuscript 的选题有潜力，thesis 也比普通 video-generation survey 更清楚。最强的贡献方向是：**把 predictive world modeling 从“生成看起来真实的视频”重新定义为“在动作、交互、物理一致性和评估协议下可验证的动态建模问题”。**

但目前还不够投稿级，主要原因是：**文献覆盖不足、内部笔记痕迹明显、taxonomy 虽合理但原创性表达不够强、physical dynamics 证据链偏薄、diffusion/interactive world model 部分缺少近期关键工作。**

最优先的修改不是润色语言，而是：
**扩大文献池 → 重建 taxonomy table → 删除内部 evidence-ready 表达 → 增强 physical evaluation 和 interactive simulator 两条主线 → 用统一比较维度重写 Section 4–8。**