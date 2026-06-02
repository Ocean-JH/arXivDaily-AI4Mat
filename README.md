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

## New Papers (7)

*Last updated: 2026-06-03 07:43:42 (SGT)*

### 1. Towards Automated Discovery: A Review of Generative Models, Multimodal Learning and Closed-Loop Workflows in Inverse Materials Design

**Authors:** Anand Babu, Rogério Almeida Gouvêa, Gian-Marco Rignanese

**Published:** 2026-06-01

**Category:** cond-mat.mtrl-sci

**ID:** 2606.02507v1

**Link:** [http://arxiv.org/abs/2606.02507v1](http://arxiv.org/abs/2606.02507v1)

**Summary:** Inverse materials design is shifting materials discovery from forward prediction to targeted proposal of candidates that satisfy objectives under physical constraints. Here, we review recent advances in generative crystal structure modeling, multimodal learning, and closed-loop design pipelines for crystalline solids. We survey how modern generators learn chemical-structural priors from large databases to enable controllable sampling of periodic structures, and compare leading model classes including variational autoencoders, normalizing flows, autoregressive formulations, and diffusion models. Particular attention is given to how feasibility constraints and physical priors are enforced across the workflow, through representation choices, training objectives, sampling-time guidance, and post-generation screening and relaxation. We also discuss how multimodal learning fuses diverse materials modalities, including crystal structures, thermodynamic, electronic information, microscopy, spectroscopy, processing context, and scientific text, to construct a more universal, transferable representation of chemical space. In addition, diverse inverse-design strategies are examined, particularly those that integrate conditional generation with latent optimization, Bayesian optimization, reinforcement learning, and active learning. Finally, we highlight recurring failure modes, such as surrogate exploitation, diversity collapse, distribution shift, and the stability-synthesizability gap, and outline discovery-grade evaluation practices based on staged reporting of validity, novelty, uniqueness, stability, and cost....

---

### 2. Large Electron Model: A Universal Ground State Predictor

**Authors:** Timothy Zaklama, Max Geier, Liang Fu

**Published:** 2026-03-02

**Category:** cond-mat.str-el

**ID:** 2603.02346v2

**Link:** [http://arxiv.org/abs/2603.02346v2](http://arxiv.org/abs/2603.02346v2)

**Summary:** We introduce Large Electron Model, a single neural network model that produces variational wavefunctions of interacting electrons over the entire Hamiltonian parameter manifold. Our model employs the Fermi Sets architecture, a universal representation of many-body fermionic wavefunctions, which is further conditioned on Hamiltonian parameter and particle number. For interacting electrons in a two-dimensional harmonic potential, a single trained model accurately predicts the ground state wavefunction while generalizing across unseen coupling strengths and particle-number sectors, producing both accurate real-space charge densities and ground state energies, even up to $50$ particles. Our results establish a foundation model method for material discovery that is grounded in the variational principle, while accurately treating strong electron correlation beyond the capacity of density functional theory....

---

### 3. A Padding Method for Enhanced Encoding of Inorganic Structures with Varying Chemical Compositions

**Authors:** Thang Dang, Haderbache Amir, Tzanakakis Alexandros, Yoshimoto Yuta

**Published:** 2026-05-29

**Category:** cond-mat.mtrl-sci

**ID:** 2605.30743v2

**Link:** [http://arxiv.org/abs/2605.30743v2](http://arxiv.org/abs/2605.30743v2)

**Summary:** Designing novel inorganic materials through generative models remains an important challenge for material science, driven by the complexity and diversity of inorganic structures across expansive chemical compositions and structural landscape. The vast combinatorial space of inorganic compounds demands innovative, AI-driven approaches to overcome limitations in generative accuracy and efficiency. To address this, we introduce a novel method that redefines the encoding and generation of inorganic materials by utilizing domain-specific symmetry-aware representation. Our approach not only refines the representation of intricate inorganic structures but also contributes to the field of material discovery by enhancing the precision and stability of generated candidates. Central to our methodology is a novel padding technique that exploits crystal symmetry information to enhance the encoding process. By integrating Wyckoff position length-aware padding into an encoder architecture, we achieve a more robust informed representation of inorganic materials. This symmetry-driven enhancement improves deep learning models to generate stable, previously unexplored inorganic structures with superior accuracy and computational efficiency. Furthermore, we introduce an end-to-end system that leverages the machine learning potential models to seamlessly generate novel, even those unseen in the training data, and stable inorganic materials from initial data to validated output. This pipeline integrates advanced generative models with stability analysis, marking a significant leap forward in the automated exploration and design of next-generation inorganic materials. Our method improved reconstruction accuracy 5.3% in proton conductor data, and generated 63.5% more novel stable inorganic material to baseline model on the perov-5 dataset....

---

### 4. Graph Energy Matching: Transport-Aligned Energy-Based Modeling for Graph Generation

**Authors:** Michal Balcerak, Suprosanna Shit, Chinmay Prabhakar, Sebastian Kaltenbach, Michael S. Albergo, Yilun Du, Bjoern Menze

**Published:** 2026-03-24

**Category:** cs.LG

**ID:** 2603.23398v3

**Link:** [http://arxiv.org/abs/2603.23398v3](http://arxiv.org/abs/2603.23398v3)

**Summary:** Generative modeling of discrete data, such as graphs, underpins many scientific and industrial applications, including molecular discovery and materials design. In these domains, probabilistic inference is particularly valuable, as it enables composable generation and principled incorporation of desired constraints, such as structural or functional properties. Energy-based models naturally support this goal by capturing relative likelihoods and enabling composable inference by directly enforcing constraints during inference. However, discrete energy-based models typically struggle with efficient and high-quality sampling, as off-support regions often contain spurious local minima, trapping samplers and causing training instabilities, resulting in a fidelity gap compared to discrete diffusion models. To address this gap, we introduce Graph Energy Matching (GEM), a discrete generative framework inspired by the Jordan-Kinderlehrer-Otto (JKO) transport-map optimization perspective. GEM learns a permutation-invariant potential energy that simultaneously guides discrete transport from noise toward high-likelihood graph regions and refines samples within these regions. We further introduce a sampling protocol leveraging an energy-based switching strategy, seamlessly bridging rapid, gradient-guided transport and a local mixing regime for effective exploration. On molecular graph benchmarks, GEM matches or surpasses strong discrete diffusion baselines on most reported metrics. Beyond improving generation quality, GEM's relative likelihood modeling enables targeted exploration, facilitating compositional generation, property-constrained sampling, and interpolation between graphs. Project page: https://michalbalcerak.ai/graph-energy-matching/....

---

### 5. Planar Symmetric Pattern Generation

**Authors:** Ning Lin, Luxi Chen, Huaguan Chen, Jiacheng Cen, Chongxuan Li, Wenbing Huang, Hao Sun

**Published:** 2026-06-01

**Category:** cs.LG

**ID:** 2606.02073v1

**Link:** [http://arxiv.org/abs/2606.02073v1](http://arxiv.org/abs/2606.02073v1)

**Summary:** Generating objects with specific symmetries is essential in various real-world scenarios. However, adapting existing 2D continuous representations to enforce planar group symmetry remains a challenge, as the transformation of non-reflective group elements may disrupt continuity. To overcome this limitation, we propose a symmetrization framework for arbitrary planar groups. Our method transforms any 2D continuous representation into a symmetric one while preserving continuity. We provide the mathematical formulation of this representation, demonstrate its approximation capability for symmetric functions, and detail the construction methodology. We validate our approach through three visual design tasks (pattern design, paper-cutting design and stylized topology design) and one material design task. Experiments confirm that our representation enables effective symmetry control and demonstrate its broader applicability....

---

### 6. Coupling Language Models with Physics-based Simulation for Synthesis of Inorganic Materials

**Authors:** Edward W. Staley, Tom Arbaugh, Michael Pekala, Alexander New, Christopher D. Stiles, Nam Q. Le, Gregory Bassen, Wyatt Bunstine, Tyrel McQueen

**Published:** 2026-05-29

**Category:** cs.AI

**ID:** 2606.00315v1

**Link:** [http://arxiv.org/abs/2606.00315v1](http://arxiv.org/abs/2606.00315v1)

**Summary:** Modern generative machine learning (ML) models can propose novel inorganic crystalline materials with targeted properties; however, synthesis planning of these materials remains difficult due to the complexity of the associated physical processes and limited availability of computational tools. We introduce a novel hybrid framework to evaluate Large Language Models (LLMs) in inorganic synthesis planning by combining thermodynamic databases with simplified kinetics models to approximate realistic synthesis conditions. As a case study, we focus on the niobium-oxygen system, which features multiple industrially relevant oxide phases with well-characterized data. In computational simulations, we compare LLM-generated synthesis routes with classical path-planning algorithms, showing that the implicit priors in LLMs can yield more viable strategies. In our evaluation setting, classical search methods serve primarily as a foil rather than a direct competitor. This illustrates the relative complexity of the problem and highlights where the LLM's implicit priors add value....

---

### 7. AI-Guided Design and Optimization of Graphite-Based Anodes via Iterative Experimental Feedback

**Authors:** Qian Du, Mark M. Sullivan, James E. Saal, Florian Huber

**Published:** 2026-05-29

**Category:** cs.LG

**ID:** 2606.00187v1

**Link:** [http://arxiv.org/abs/2606.00187v1](http://arxiv.org/abs/2606.00187v1)

**Summary:** This study presents an iterative AI-guided workflow that accelerates graphite-based anode development by improving both formulation feasibility and process robustness. Sequential learning via AI/ML-guided multiobjective inverse design for anode optimization was implemented using the Citrine Platform. Starting from a noisy, incomplete dataset, the Citrine Platform was used to generate early surrogate models, which despite low predictive certainty highlighted missing process constraints. By iteratively adding feasibility labels and boundary condition failures, the workflow rapidly converged toward manufacturable, higher-performing formulations. Fabrication reliability improved from frequent process failures to 100% successful cell production, while the fraction of cells delivering $\geq$ 350 mAh g$^{-1}$ increased from 28.4% to 84.8%, with capacity retention rising from 42.1% to 97.3%. These results demonstrate that structured, feedback-driven AI workflows can transform imperfect industrial data into actionable guidance, enabling faster, more reproducible optimization of battery electrode manufacturing....

---


<!-- ARXIV_PAPERS_END -->