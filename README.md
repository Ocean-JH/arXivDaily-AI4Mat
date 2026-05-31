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

## New Papers (12)

*Last updated: 2026-06-01 06:58:13 (SGT)*

### 1. Optimization and Generation in Aerodynamics Inverse Design

**Authors:** Huaguan Chen, Ning Lin, Luxi Chen, Jiacheng Cen, Rui Zhang, Wenbing Huang, Chongxuan Li, Hao Sun

**Published:** 2026-02-03

**Category:** cs.LG

**ID:** 2602.03582v3

**Link:** [http://arxiv.org/abs/2602.03582v3](http://arxiv.org/abs/2602.03582v3)

**Summary:** Aerodynamic inverse design can improve vehicle and aircraft efficiency, but practical design rarely seeks performance alone: vehicle refinement must reduce drag while preserving visual features linked to design language, brand recognition and user perception. Traditional CFD-driven optimization is accurate but slow for broad exploration, and current learning-based methods are still largely performance-driven and lack a coherent target linking optimization, generation and visual consistency. Here we formulate visual preservation and aerodynamic improvement as one probability target. Designs consistent with a reference shape or view define a learned visual design distribution, which is reweighted by aerodynamic cost. Optimization then refines an initial geometry toward a low-cost, high-probability design, whereas guided generation samples lower-cost 3D candidates from the same input view. OpenFOAM evaluation shows that visual-feature-preserving optimization reduces vehicle drag by 5.8\% relative to the initial vehicle and reduces the best valid aircraft drag-to-lift objective by 28.8\% relative to the initial aircraft while preserving input visual features. For view-based generation, guidance reduces vehicle drag by 3.0\% and the aircraft drag-to-lift objective by 68.6\% relative to direct generation from the same view, while maintaining visual consistency. Wind-tunnel tests with 3D-printed vehicle prototypes provide an independent wake-level check, and controlled analyses explain the distributional mechanisms behind these results. This work provides a probabilistic foundation and practical route for visual-feature-preserving aerodynamic refinement and early-stage 3D design exploration....

---

### 2. Prototype-Guided Latent Alignment for Data-Efficient Fine-Tuning of Molecular Foundation Models

**Authors:** Rushikesh Pawar, Harshit Rawat, Ayush Kumar, Phani Motamarri

**Published:** 2026-05-28

**Category:** cond-mat.mtrl-sci

**ID:** 2605.29969v1

**Link:** [http://arxiv.org/abs/2605.29969v1](http://arxiv.org/abs/2605.29969v1)

**Summary:** Machine learning interatomic potentials (MLIPs) have transformed materials discovery by leveraging graph neural networks (GNNs) to predict material properties with near density functional theory (DFT) accuracy. While large-scale pretrained foundation models offer transferable baseline representations, they frequently struggle to generalise to out-of-distribution (OOD) target systems -- a common challenge in modelling complex or chemically diverse materials. Fine-tuning is the standard remedy, but the high cost of generating DFT-labelled configurations confines adaptation to data-scarce regimes, where over-parameterised GNNs amplify overfitting and degrade target-domain performance. To address this, we propose a prototype-based alignment approach for data-efficient fine-tuning of MLIPs. Our method identifies local structural similarities between the source and target domains by grouping atoms with analogous chemical environments based on their latent representations. Each target-domain atom's energy contribution is aligned to its source-domain prototype, introducing an inductive bias that anchors fine-tuned representations to the pretrained structure, encouraging effective reuse of learned interactions and improving generalisation without restrictive assumptions on the target chemistry. We evaluate our method on the rMD17 benchmark using equivariant MACE and invariant SchNet across varying data budgets, and extend evaluation to the MACE-OFF foundation models on the SPICE dataset. Our approach consistently improves predictive accuracy in the low-data regime, reducing energy MAE by up to 18% over standard fine-tuning baselines....

---

### 3. Discovery and recovery of crystalline materials with property-conditioned transformers

**Authors:** Cyprien Bone, Matthew Walker, Bradley A. A. Martin, Kuangdai Leng, Luis M. Antunes, Ricardo Grau-Crespo, Amil Aligayev, Javier Dominguez, Keith T. Butler

**Published:** 2025-11-26

**Category:** cond-mat.mtrl-sci

**ID:** 2511.21299v2

**Link:** [http://arxiv.org/abs/2511.21299v2](http://arxiv.org/abs/2511.21299v2)

**Summary:** Generative models have recently shown great promise for accelerating the design and discovery of new functional materials. Conditional generation enhances this capacity by allowing inverse design, where specific desired properties can be requested during the generation process. However, conditioning of transformer-based approaches, in particular, is constrained by discrete tokenisation schemes and the risk of catastrophic forgetting during fine-tuning. This work introduces CrystaLLM-π (property injection), a conditional autoregressive framework that integrates continuous property representations directly into the transformer's attention mechanism. Two architectures, Property-Key-Value (PKV) Prefix attention and PKV Residual attention, are presented. These methods bypass inefficient sequence-level tokenisation and preserve foundational knowledge from unsupervised pre-training on Crystallographic Information Files (CIFs) as textual input. We establish the efficacy of these mechanisms through systematic robustness studies and evaluate the framework's versatility across two distinct tasks. First, for structure recovery, the model processes high-dimensional, heterogeneous X-ray diffraction patterns, achieving structural accuracy competitive with specialised models and demonstrating applications to experimental structure recovery and polymorph differentiation. Second, for materials discovery, the model is fine-tuned on a specialised photovoltaic dataset to generate novel, stable candidates validated by Density Functional Theory (DFT). It implicitly learns to target optimal band gap regions for high photovoltaic efficiency, demonstrating a capability to map complex structure-property relationships. CrystaLLM-π provides a unified, flexible, and computationally efficient framework for inverse materials design....

---

### 4. Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era

**Authors:** Reid A. Coyle, Shyam Chand Pal, Peter Walther, Saeun Park, Bin Feng, Zhiling Zheng

**Published:** 2026-05-27

**Category:** cond-mat.mtrl-sci

**ID:** 2605.29179v1

**Link:** [http://arxiv.org/abs/2605.29179v1](http://arxiv.org/abs/2605.29179v1)

**Summary:** Metal-organic frameworks (MOFs) are excellent candidates for water harvesting due to their tunable pore environments, which can be precisely engineered to capture and release water in arid conditions. Integrating artificial intelligence (AI) into MOF discovery can further accelerate the design of high-performance sorbents by identifying structural features that enhance atmospheric water harvesting (AWH), stability, and cycling efficiency. In this Perspective, we examine key MOF design principles, including cooperative adsorption, operational relative humidity (RH), uptake capacity, hysteresis, and scalability. We highlight recent design advancements such as multivariate strategies and long-arm linker extension, and examine how these principles tune pore capacity and hydrophilicity, while preserving stability and crystallinity. Furthermore, we discuss how AI, large language models (LLMs), and data mining can accelerate the discovery process through predictive synthesis, inverse design, and elucidating synthesis-structure-property relationships for the next generation of MOF water harvesters....

---

### 5. Materials Acceleration Platform for Electrochemistry: a Platform for Autonomous Electrochemistry

**Authors:** Daniel Persaud, Mike Werezak, Mark Xu, Melyne Zhou, Frank Benkel, Xin Pang, Vahid Attari, Brian DeCost, Ashley Dale, Nicholas Senior, Gabriel Birsan, Jason Hattrick-Simpers

**Published:** 2026-03-10

**Category:** cond-mat.mtrl-sci

**ID:** 2603.09845v2

**Link:** [http://arxiv.org/abs/2603.09845v2](http://arxiv.org/abs/2603.09845v2)

**Summary:** Corrosion testing is slow, labor-intensive, and sensitive to operator technique, limiting the generation of large, high-quality datasets for data-driven materials discovery. The Materials Acceleration Platform for Electrochemistry (MAP-E) is an autonomous, high-throughput system, capable of performing parallel electrochemical experiments. It integrates robotic liquid handling, sample transfer with a multi-channel potentiostatic control to extract corrosion metrics without human intervention. Validation against an ASTM G61-analog benchmark demonstrates good reproducibility, with a standard deviation of 75 mV in pitting potential across 32 automated measurements. The platform was then employed to autonomously construct pH-chloride stability diagrams for 304 stainless steel using an uncertainty-driven sampling strategy on a Gaussian process surrogate model. This approach reduces operator involvement and accelerates the exploration of environmental spaces. The MAP-E establishes a framework for autonomous electrochemical experimentation, enabling generation of corrosion datasets that inform materials discovery, alloy design, and durability assessment in service environments....

---

### 6. MatFormBench: A Benchmarking Evaluation Framework for Target-Driven Materials Formulation

**Authors:** Linhan Wu, Chenxi Wang, Chuhan Yang, Zhengwei Yang, Yuyang Liu

**Published:** 2026-05-26

**Category:** cond-mat.mtrl-sci

**ID:** 2605.26741v1

**Link:** [http://arxiv.org/abs/2605.26741v1](http://arxiv.org/abs/2605.26741v1)

**Summary:** Inverse design of materials has significantly advanced target-driven formulation optimization, yet existing materials machine learning benchmarks remain limited to forward property prediction, failing to systematically evaluate inverse optimization and generation algorithms, a critical gap that hinders the progress of target-driven materials design. To address this limitation, we propose MatFormBench, a novel benchmarking ecosystem tailored to evaluate and guide generative strategies for target-driven formulation. MatFormBench integrates a physics-driven formulation generation scheme to generate synthetic samples that faithfully emulate realistic materials structure-property response relationships, complemented by five escalating difficulty levels to quantify the complexity of these relationships. To rigorously assess algorithm performance, we further propose MatFormScore, a multi-dimensional metric that comprehensively quantifies performance across five critical axes: target success, search efficiency, exploratory capacity, robustness, and stability. We validate MatFormBench by evaluating 39 diverse inverse design algorithms, covering classical surrogate-assisted black-box search, state-of-the-art deep generative models, and increasingly popular Large Language Model (LLM)-based recommendation strategies. Across 1170 standardized algorithm-task evaluations, diffusion-based models demonstrate the strongest overall performance, while Variational Autoencoder (VAE)-based and Genetic Algorithm (GA)-based methods exhibit distinct advantages in specific scenarios. By establishing a unified evaluation standard for target-driven materials formulation, MatFormBench enables reproducible benchmarking, principled algorithm comparison, and diagnostic analysis of inverse design strategies, providing a foundational tool for advancing materials inverse design....

---

### 7. PolyFusionAgent: A Multimodal Foundation Model and Autonomous AI Assistant for Polymer Property Prediction and Inverse Design

**Authors:** Manpreet Kaur, Xingying Zhang, Qian Liu

**Published:** 2026-05-26

**Category:** cs.AI

**ID:** 2605.26543v1

**Link:** [http://arxiv.org/abs/2605.26543v1](http://arxiv.org/abs/2605.26543v1)

**Summary:** Polymer discovery is central to fields ranging from energy storage to biomedicine, but it is hindered by an astronomically large chemical design space and fragmented representations of structure, properties, and prior knowledge. This fragmentation leaves many AI models disconnected from physical and experimental reality, restricting their ability to support directly actionable design decisions. Here we introduce PolyFusionAgent, an interactive framework coupling a multimodal polymer foundation model (PolyFusion) with a tool-augmented, literature-grounded design agent (PolyAgent). PolyFusion aligns complementary polymer views including sequence, topology, 3D geometry, and fingerprints across millions of polymers to learn a shared latent space transferable across chemistries and data regimes, improving thermophysical property prediction and enabling property-conditioned generation of chemically valid, structurally novel polymers beyond the reference design space. PolyAgent closes the design loop by linking prediction and inverse design with evidence retrieval from the polymer literature, proposing, evaluating, and contextualizing hypotheses with explicit precedent in one workflow. Together, PolyFusionAgent enables interactive, evidence-linked polymer discovery combining large-scale representation learning, multimodal chemical knowledge, and verifiable scientific reasoning....

---

### 8. Accelerating Bayesian inverse design in computational fluid dynamics using neural operators

**Authors:** Bipin Tiwari, Omer San

**Published:** 2026-05-25

**Category:** physics.flu-dyn

**ID:** 2605.26059v1

**Link:** [http://arxiv.org/abs/2605.26059v1](http://arxiv.org/abs/2605.26059v1)

**Summary:** Bayesian inverse design provides a principled framework for inferring aerodynamic geometries from sparse flow observations while quantifying uncertainty. However, its practical use in computational fluid dynamics (CFD) is severely limited by the cost of repeated high-fidelity simulations required for gradient-based Markov chain Monte Carlo (MCMC) sampling. While surrogate models are commonly proposed to reduce this cost, their effect on posterior geometry and uncertainty, especially for shock-dominated flows, remains poorly understood. In this work, we demonstrate that neural operator surrogates can be embedded directly within the MCMC inference loop while preserving posterior structure. Using a fully Bayesian inverse formulation of quasi-one-dimensional nozzle flow, we demonstrate that geometry parameterization plays a decisive role in identifiability and posterior conditioning, with cubic B-splines yielding stable and physically meaningful uncertainty estimates. Building on this formulation, a Deep Operator Network trained on CFD-generated data is substituted for the CFD solver within a No-U-Turn Sampler, while keeping the likelihood model, priors, and sampling configuration unchanged. Across sparse to fully observed regimes, surrogate-based inference reproduces the posterior geometry and uncertainty trends of the CFD reference. As a result of surrogate integration, total inference time is reduced to under one second, corresponding to a speedup exceeding three orders of magnitude. In addition, a direct inverse neural operator is examined as a deterministic alternative for inverse design, enabling single-shot geometry reconstruction without posterior sampling. These results demonstrate that neural operator-accelerated Bayesian inference enables practical, uncertainty-aware inverse design workflows for aerodynamic applications....

---

### 9. Benchmarking Transparent Conductors

**Authors:** Amit Cohen, Lior Kornblum

**Published:** 2026-05-25

**Category:** cond-mat.mtrl-sci

**ID:** 2605.25904v1

**Link:** [http://arxiv.org/abs/2605.25904v1](http://arxiv.org/abs/2605.25904v1)

**Summary:** Transparent conducting oxides (TCOs) are central to optoelectronic technologies, yet their design is often guided by popular figures of merit that are disconnected from the electrical requirement of actual devices. As a result, widely used metrics guide material design under conditions that can be impractical for devices. Here, we introduce a benchmarking framework to guide TCO development, in which transparent conductors are evaluated at fixed, application-relevant sheet resistance $(R_S)$. The resulting metric, $T_{app}(R_S)$, anchors comparison to device requirements, asking instead: What optical transparency can be obtained at the sheet resistance required by a given application? This approach provides a directly interpretable measure of performance, enabling materials to be benchmarked in terms of absolute transparency gains at a specified $R_S$. Applied to representative conventional and emerging TCOs, the framework defines the sheet-resistance landscape relevant to each application and maps how different materials perform within it. In doing so, it provides an application-rooted guide to material development and selection. More broadly, this approach establishes a general strategy for evaluating materials under fixed operational constraints, bridging the gap between materials design and device integration....

---

### 10. General spin models from noncollinear spin density functional theory and spin-cluster expansion

**Authors:** Tomonori Tanaka, Yoshihiro Gohda

**Published:** 2025-12-04

**Category:** cond-mat.mtrl-sci

**ID:** 2512.04458v3

**Link:** [http://arxiv.org/abs/2512.04458v3](http://arxiv.org/abs/2512.04458v3)

**Summary:** We present a data-efficient framework for constructing general classical spin Hamiltonians by combining the spin-cluster expansion (SCE) with fully self-consistent noncollinear spin density functional theory (DFT). The key idea is to fit the SCE model to magnetic torques rather than to total energies. Because torques are site-resolved vectors, each spin configuration provides many informative regression targets, improving conditioning and substantially reducing the number of required DFT calculations, especially for large supercells. Applied to the B20-type chiral magnets ${\rm Mn}_{1-x}{\rm Fe}_{x}{\rm Ge}$ and ${\rm Fe}_{1-y}{\rm Co}_{y}{\rm Ge}$, the resulting SCE models determine full pairwise exchange tensors -- including isotropic exchange, symmetric anisotropic exchange, and the Dzyaloshinskii--Moriya interaction -- and predict the helical spin period via a micromagnetic mapping. The composition trends and the divergence of the period at the chirality sign-change point are well reproduced, in agreement with experiment. Moreover, the systematic nature of SCE enables controlled assessment of interaction order: as the training spin configurations become more disordered, the lowest-order model loses torque accuracy, whereas including higher-order interactions restores predictive power. These advances enable near-DFT-accurate spin models for finite-temperature magnetism and complex spin textures at modest computational cost, providing an extensible route to quantitative first-principles parameterization and predictive materials design. An open-source implementation is available as a Julia package, \textit{Magesty.jl}....

---

### 11. Composable Crystals: Controllable Materials Discovery via Concept Learning

**Authors:** Nian Liu, Yuwei Zeng, Ryoji Kubo, Nikita Kazeev, Stephen Gregory Dale, Artem Maevskiy, Pengru Huang, Thomas Laurent, Kostya S. Novoselov, Xavier Bresson

**Published:** 2026-05-14

**Category:** cs.LG

**ID:** 2605.14769v2

**Link:** [http://arxiv.org/abs/2605.14769v2](http://arxiv.org/abs/2605.14769v2)

**Summary:** De novo crystal generation, a central task in materials discovery, aims to generate crystals that are simultaneously valid, stable, unique, and novel. Existing methods mainly rely on black-box stochastic sampling, providing limited control over how generated structures move beyond the observed distribution. In this paper, we introduce a concept-based compositional framework for crystal generation. We train a vector-quantized variational autoencoder to automatically discover a shared set of reusable crystal concepts, which serve as building blocks for guided generation. These learned concepts naturally exhibit interpretability from both local atomic environments and global symmetry patterns, and generalize to crystals from different distributions. By recombining such concepts, our framework enables controllable exploration of novel crystals beyond the training distribution, rather than relying solely on unconstrained random sampling. To further improve composition efficiency, we introduce a composition generator and iteratively refine it using high-quality samples generated by the model itself. The resulting concept compositions are then used to condition downstream crystal generation. Numerical experiments on MP-20 and Alex-MP-20 show that compositing concepts separately increase base model up to 53.2% and 51.7% on V.S.U.N metric, with particular gains in novelty....

---

### 12. Generative structure search for efficient and diverse discovery of molecular and crystal structures

**Authors:** Yifang Qin, Yu Shi, Junfu Tan, Chang Liu, Ming Zhang, Ziheng Lu

**Published:** 2026-04-30

**Category:** cs.AI

**ID:** 2604.27636v2

**Link:** [http://arxiv.org/abs/2604.27636v2](http://arxiv.org/abs/2604.27636v2)

**Summary:** Predicting stable and metastable structures is central to molecular and materials discovery, but remains limited by the cost of searching high-dimensional energy landscapes. Deep generative models offer efficient structure sampling, yet their outputs remain shaped by training data and can underexplore minima that are rare but physically relevant. We introduce generative structure search (GSS), a unified framework that formulates diffusion-based generation and random structure search (RSS) as limiting regimes of a common sampling process driven by learned score fields and physical forces. Coupling these drivers lets GSS use data priors to accelerate sampling while retaining energy-guided exploration of local minima. Across molecular and crystalline systems, GSS recovers diverse metastable structures with more than tenfold lower sampling cost than RSS for broad coverage and remains effective for compositions outside the training distribution. The results establish a physically grounded generative search strategy for discovering structures beyond the reach of data-driven sampling alone....

---


<!-- ARXIV_PAPERS_END -->