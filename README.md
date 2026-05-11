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

## New Papers (2)

*Last updated: 2026-05-12 06:51:59 (SGT)*

### 1. RIDER: 3D RNA Inverse Design with Reinforcement Learning-Guided Diffusion

**Authors:** Tianmeng Hu, Yongzheng Cui, Biao Luo, Ke Li

**Published:** 2026-02-18

**Category:** cs.LG

**ID:** 2602.16548v2

**Link:** [http://arxiv.org/abs/2602.16548v2](http://arxiv.org/abs/2602.16548v2)

**Summary:** The inverse design of RNA three-dimensional (3D) structures is crucial for engineering functional RNAs in synthetic biology and therapeutics. While recent deep learning approaches have advanced this field, they are typically optimized and evaluated using native sequence recovery, which is a limited surrogate for structural fidelity, since different sequences can fold into similar 3D structures and high recovery does not necessarily indicate correct folding. To address this limitation, we propose RIDER, an RNA Inverse DEsign framework with Reinforcement learning that directly optimizes for 3D structural similarity. First, we develop and pre-train a GNN-based generative diffusion model conditioned on the target 3D structure, achieving a 9% improvement in native sequence recovery over state-of-the-art methods. Then, we fine-tune the model with an improved policy gradient algorithm using four task-specific reward functions based on 3D self-consistency metrics. Experimental results show that RIDER improves structural similarity by over 100% across all metrics and discovers designs that are distinct from native sequences....

---

### 2. LLM-Guided Open Hypothesis Learning from Autonomous Scanning Probe Microscopy Experiments

**Authors:** Boris Slautin, Utkarsh Pratiush, Yu Liu, Kamyar Barakati, Sergei Kalinin

**Published:** 2026-05-07

**Category:** cond-mat.mtrl-sci

**ID:** 2605.06839v1

**Link:** [http://arxiv.org/abs/2605.06839v1](http://arxiv.org/abs/2605.06839v1)

**Summary:** Autonomous experimentation has transformed microscopy and materials discovery by enabling closed-loop optimization including imaging and spectroscopy tuning, strucutre property relationship discovery, and exploration of combinatorial libraries. However, most current workflows remain limited to selecting measurements within fixed objective or hypothesis spaces, rather than generating new physical models from experimental data. Here, we introduce an open hypothesis-learning framework that combines symbolic regression with large-language-model-based physical evaluation and implement it for autonomous scanning probe microscopy. Symbolic regression generates candidate analytical relationships directly from sparse measurements, while the language-model evaluator ranks these candidates according to physical plausibility, scaling behavior, and consistency with known mechanisms. We demonstrate the approach on autonomous piezoresponse force microscopy measurements of ferroelectric domain switching in a PZT thin film. Starting from five seed measurements, the workflow evolves from physically incomplete candidate expressions toward interpretable voltage-time growth laws consistent with kinetic domain-wall motion. This work extends autonomous microscopy from closed-loop optimization toward open hypothesis discovery, where candidate physical laws emerge from the experiment itself rather than being specified in advance. More broadly, the framework establishes a route for integrating symbolic regression, physical reasoning, and adaptive experimentation into hierarchical autonomous scientific workflows....

---


<!-- ARXIV_PAPERS_END -->