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

*Last updated: 2026-07-14 06:54:06 (SGT)*

### 1. Physics-grounded generative design of inherently stable, novel and controllable crystal structures

**Authors:** Zhilong Song, Qionghua Zhou, Chongyi Ling, Qiang Li, Lixue Cheng, Jinlan Wang

**Published:** 2025-07-25

**Category:** cond-mat.mtrl-sci

**ID:** 2507.19307v2

**Link:** [http://arxiv.org/abs/2507.19307v2](http://arxiv.org/abs/2507.19307v2)

**Summary:** Generative inverse design is reshaping the discovery of functional crystalline materials. Yet current generative models face challenges in simultaneously achieving stability, novelty, and precise controllability in a single trained model. We address these challenges with a key physical insight: the diversity of crystals is governed by their crystallographic information (CI), namely composition, space group and lattice, whereas only a few stable atomic configurations remain once the CI is fixed. Built on this insight, we introduce SCGEN (stable and controllable crystal structure generation), a physics-grounded generative model with two components. A variational autoencoder samples diverse, physically plausible CI, and a symmetry- and Wyckoff-position-constrained optimizer locates stable atomic positions via universal machine-learning potentials. Benchmarked on roughly two million structures, SCGEN reaches state-of-the-art stability while preserving comparable novelty, and it satisfies any specified composition, space group, lattice or joint constraint with 100% success and no task-specific retraining. Applied to photocatalytic water splitting, property-guided optimization with SCGEN generates 200,000 candidate structures and identify top 22 stable, active and synthesizable photocatalysts. By decoupling CI generation from coordinate optimization, SCGEN establishes a physics-grounded inverse-design paradigm that yields synthesis-ready crystals on demand, rather than structures requiring post hoc repair, relaxation, or retraining....

---

### 2. Tensor Methods: A Unified and Interpretable Approach for Material Design

**Authors:** Shaan Pakala, Aldair E. Gongora, Brian Giera, Evangelos E. Papalexakis

**Published:** 2026-02-11

**Category:** cs.LG

**ID:** 2602.10392v3

**Link:** [http://arxiv.org/abs/2602.10392v3](http://arxiv.org/abs/2602.10392v3)

**Summary:** When designing new materials, it is often necessary to tailor the material design to have some desired properties. As the set of material design parameters grows, the search space grows exponentially, making the actual synthesis and evaluation of all combinations of designs virtually impossible. Even using traditional computational methods, such as Finite Element Analysis (FEA), becomes too computationally heavy to search this design space. Recent methods use machine learning (ML) surrogate models to more efficiently determine optimal material designs; unfortunately, these methods often (i) are notoriously difficult to interpret and (ii) under perform when the training data comes from a non-uniform sampling of the entire design space. In this work, we suggest the use of tensor completion methods as an all-in-one approach for interpretability and predictions. We observe classical tensor methods are able to compete with traditional ML methods in predictions, with the added benefit of their interpretable tensor factors (which are given for free). In our experiments, we are able to rediscover physical phenomena via the tensor factors, indicating that our predictions are aligned with the physics of the problem. This also means these factors could be used by experimentalists to identify potentially novel patterns, given we are able to rediscover existing ones. We also study the effects of both types of surrogate models (traditional ML \& tensor-based) when we encounter training data from a non-uniform sampling of the design space. We observe some more specialized tensor methods that are able to give better generalization in these non-uniform sampling scenarios, due to the low-rank constraint. We find the best generalization comes from a tensor model, which is able to improve upon the baseline ML methods by up to 5\% on aggregate $R^2$, and halve the error in some out of distribution sections....

---


<!-- ARXIV_PAPERS_END -->