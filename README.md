# ArXiv Daily - AI4MAT

**Daily automatic updates of the latest arXiv papers on AI for Materials Science (AI4MatSci).** 

Stay informed with cutting-edge research at the intersection of artificial intelligence and materials science — automatically!

## :bookmark: Related Fields

- (Computational) Materials Science
- Machine Learning
- Materials Design
- Crystal Structure Prediction
- Generative AI for Materials Discovery

## :star: Customize Yours

Let's start with a star :star:!

And then, feel free to adjust the `query` field in the file `config.json` to match your own research interests(see [arXiv API User's Manual](https://info.arxiv.org/help/api/user-manual.html#51-details-of-query-construction) for more information)!

## :handshake: Contributions

Contributions are welcome!
 Feel free to open an Issue or a Pull Request if you have ideas for improvement, new features, or better queries.

## :blue_heart: ​Acknowledge

Thank you to [arXiv](https://arxiv.org/) for use of its open access interoperability.

---

## :scroll: Paper List


<!-- ARXIV_PAPERS_START -->

## New Papers (3)

*Last updated: 2026-05-06 06:53:25 (SGT)*

### 1. Composition-Weighted Symbolic Regression for General-Purpose Property Prediction

**Authors:** Yang Huang, Jingrun Chen

**Published:** 2026-05-04

**Category:** cond-mat.mtrl-sci

**ID:** 2605.02267v1

**Link:** [http://arxiv.org/abs/2605.02267v1](http://arxiv.org/abs/2605.02267v1)

**Summary:** We introduce a composition-weighted symbolic regression framework for interpretable prediction of materials properties directly from chemical composition. The method jointly learns analytical functional forms and task-dependent elemental weightings without predefined descriptors. By incorporating max/min operators, it naturally enforces constraints such as non-negative band gaps and bounded classification probabilities, unifying regression and classification tasks. Efficient search is achieved through a hybrid Monte Carlo tree search--genetic programming algorithm with gradient-based refinement and parallel computation. Benchmarks on MatBench tasks show competitive accuracy relative to state-of-the-art black-box models while yielding explicit analytical expressions. Applied to III--V semiconductor alloys, the model produces smooth composition-dependent trends and learned elemental weights with chemically meaningful periodic behavior. This framework provides a scalable and interpretable route for materials discovery and property screening....

---

### 2. Agentic Fusion of Large Atomic and Language Models to Accelerate Superconductor Discovery

**Authors:** Mingze Li, Yu Rong, Songyou Li, Lihong Wang, Jiacheng Cen, Liming Wu, Anyi Li, Zongzhao Li, Qiuliang Liu, Rui Jiao, Tian Bian, Pengju Wang, Hao Sun, Jianfeng Zhang, Ji-Rong Wen, Deli Zhao, Shifeng Jin, Tingyang Xu, Wenbing Huang

**Published:** 2026-04-26

**Category:** cs.LG

**ID:** 2604.23758v3

**Link:** [http://arxiv.org/abs/2604.23758v3](http://arxiv.org/abs/2604.23758v3)

**Summary:** Artificial intelligence has accelerated materials discovery through high-throughput prediction and generation, yet the decision problem remains a formidable bottleneck. While current AI systems readily propose millions of candidates, navigating the decision regarding a viable experimental target requires resolving multi-dimensional judgments across atomic-scale numerical computation and high-level semantic reasoning. Here we present ElementsClaw, an agentic framework for materials discovery that orchestrates a suite of Large Atomic Model (LAM) tools finetuned from our proposed 1-billion-parameter model Elements for numerical computation, while leveraging Large Language Models (LLMs) for semantic reasoning. Applied to superconductors, ElementsClaw rediscovers 66 experimentally verified superconductors that are absent from the standard SuperCon3D database. Scaling to 2.4 million equilibrium crystals, ElementsClaw identifies 68,000 high-confidence candidates in just 28 GPU hours (https://developer.damo-academy.com/material), expanding known superconducting space by orders of magnitude compared to datasets curated over decades. Guided by the agent's reasoning, we experimentally synthesize and verify four novel superconductors: the motif-guided Zr$_3$ScRe$_8$ ($T_c$ = 6.5 K), the de novo generated HfZrRe$_4$ ($T_c$ = 5.9 K), the structurally reinterpreted Zr$_4$VRe$_7$ ($T_c$ = 3.5 K), and the database-latent Hf$_{21}$Re$_{25}$ ($T_c$ = 2.5 K). Together, our results establish a knowledge integrated, autonomously orchestrated, and experimentally grounded paradigm for materials discovery....

---

### 3. Inverse Materials Design via Joint Generation of Crystal Structures and Local Electronic Descriptors

**Authors:** Ibuki Okuda, Izumi Takahara, Teruyasu Mizoguchi

**Published:** 2026-05-02

**Category:** cond-mat.mtrl-sci

**ID:** 2605.01286v1

**Link:** [http://arxiv.org/abs/2605.01286v1](http://arxiv.org/abs/2605.01286v1)

**Summary:** Inverse design of inorganic crystals, in which structures are generated to satisfy a target property while preserving diversity and physical plausibility, remains more demanding than ab initio generation, as property conditioning can degrade the structural quality that current generative models otherwise achieve. We propose a diffusion framework that jointly denoises crystal-structure variables and site-resolved local electronic descriptors through a shared score network. As representative descriptors, we adopt Bader charge and atomic density of states (atomic DOS). Under both band-gap and formation energy conditioned generation, the joint models achieved higher success rates than the structure-only baseline in most target conditions, while simultaneously increasing the fraction of generated structures that satisfy uniqueness, novelty, thermodynamic stability, and physical validity (VSUN criteria). A dummy-variable control confirms that these gains originate from the electronic content of the descriptors rather than from auxiliary site-wise variables. The generated Bader charges agree with DFT references with an MAE of 5.5e-2 e on stable structures, and the generated atomic DOS captures the coarse spectral profile of the DFT reference around the modal accuracy range, although finer details and accuracy vary with elemental species. These results establish local electronic descriptors as effective generative variables that serve two complementary roles: broadening the explored materials space through increased structural diversity, and mitigating the trade-off between property targeting and structural quality by guiding the structural trajectory toward electronically plausible configurations during joint denoising....

---


<!-- ARXIV_PAPERS_END -->