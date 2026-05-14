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

## New Papers (4)

*Last updated: 2026-05-15 06:54:38 (SGT)*

### 1. OpenAaaS: An Open Agent-as-a-Service Framework for Distributed Materials-Informatics Research

**Authors:** Peng Kang, Bixuan Li, Xiaoya Huang, Shuo Shi, Weiqiao Zhou, Zhen Li, Yu Liu, Lei Zheng

**Published:** 2026-05-13

**Category:** cond-mat.mtrl-sci

**ID:** 2605.13618v1

**Link:** [http://arxiv.org/abs/2605.13618v1](http://arxiv.org/abs/2605.13618v1)

**Summary:** The Materials Genome Initiative catalyzed the proliferation of centralized platforms--SaaS, PaaS, and IaaS--that aggregate computational and experimental resources for accelerated materials discovery. In parallel, breakthroughs in large language models (LLMs) and autonomous agents have created powerful new reasoning capabilities for scientific research. Yet a critical "last mile" problem remains: while we possess world-class models and vast repositories of materials data, we lack the organizational infrastructure to compose these capabilities securely across institutional boundaries. The development of structural and functional materials for harsh service environments--high-temperature alloys, radiation resistant steels, corrosion-resistant coatings--remains characterized by long-term iteration, mechanistic complexity, and high domain expertise--demands that exceed both monolithic agent systems and traditional centralized platforms. To address this gap we propose OpenAaaS, an open-source hierarchical and distributed Agent-as-a-Service framework that enables organized multi-agent collaboration for intelligent materials design. OpenAaaS is built on a single foundational principle: code flows, data stays still. A Master Agent plans and decomposes complex research tasks without requiring direct access to subordinate agents' managed data and computational resources. Sub-agents, deployed as near-data execution nodes, retain full sovereignty over local datasets, proprietary algorithms, and specialized hardware. This architecture guarantees that raw data never leaves its domain of origin while enabling cross-scale, cross-domain secure integration of previously isolated materials intelligence silos. We validate the framework through two representative case studies: (i) AlphaAgent, an evidence-grounded materials literature analysis executor that achieves 4.66/5.0 on deep analytical questions against single-pass RAG baselines; and (ii) an ultra-large-scale hexa-high-entropy alloy descriptor database service that demonstrates secure near-data execution and domain-specific scientific workflows under strict data-sovereignty constraints. OpenAaaS establishes a principled pathway toward "organized research" via agent collectives, offering a scalable foundation for next-generation materials intelligent design platforms. All source code is available at https://github.com/Wolido/OpenAaaS....

---

### 2. When Diffusion Breaks Constraints: Sequential Autoregressive Generation with RL and MCTS

**Authors:** Zirui Zhao, Boye Niu, Harold Soh, David Hsu, Wee Sun Lee

**Published:** 2025-12-01

**Category:** cs.CV

**ID:** 2512.01242v3

**Link:** [http://arxiv.org/abs/2512.01242v3](http://arxiv.org/abs/2512.01242v3)

**Summary:** Data-driven generative models excel in language and vision, but diffusion models often fail in constrained planning and design tasks, exhibiting severe constraint violations in engineering inverse design, molecular generation, multi-robot planning, and floorplan/scene synthesis even with projection or guidance. Such tasks combine hard-to-specify semantic goals with strict geometric or physical constraints (e.g., non-overlap, connectivity), yielding feasible solutions that lie on low-dimensional, small, and sometimes disconnected regions of the output space. This paper studies the failure mode through tangram generation from language, where seven fixed shapes must form a text-described silhouette while remaining connected and non-overlapping, and a simplified rectangle composition task with a learned bounding-box constraint. We find diffusion models struggle to satisfy constraints, consistent with difficulty generating samples near low-dimensional submanifolds. Motivated by locally feasible reparameterizations, we reformulate constrained generation as discrete autoregressive sequential generation. Reinforcement learning improves feasibility and task success, and Monte Carlo tree search quantifies the value of look-ahead when feasible regions shrink. Overall, the empirical, theoretical, and prior-work evidence points to a structural limitation of continuous density matching on this class of constrained-generation problems, and suggests sequential constraint-aware generation as a promising alternative....

---

### 3. Electrospinning-Data.org: A FAIR, Structured Knowledge Resource for Nanofiber Fabrication

**Authors:** Mehrab Mahdian, Ferenc Ender, Tamas Pardy

**Published:** 2026-03-29

**Category:** cs.DB

**ID:** 2603.27841v2

**Link:** [http://arxiv.org/abs/2603.27841v2](http://arxiv.org/abs/2603.27841v2)

**Summary:** Electrospinning is a versatile nanofabrication technique whose outcomes emerge from a complex, high-dimensional interplay between solution properties, processing parameters, and environmental conditions. Optimizing this parameter space for targeted fiber morphology is inherently challenging, often driving extensive trial-and-error experimentation and generating vast experimental data across laboratories worldwide. Yet this knowledge remains fragmented and underutilized due to inconsistent reporting and a pervasive bias toward successful outcomes, limiting reproducibility and hindering data-driven research. Here we introduce Electrospinning-Data.org, a FAIR-aligned data aggregation infrastructure that organizes dispersed electrospinning experiments into structured, reusable, and failure-aware scientific records. The platform is built around a unified process-structure-property data model linking experimental inputs, environmental conditions, and nanofiber morphology, annotated through a controlled vocabulary, within a consistent, machine-readable schema. A two-stage moderation pipeline combining automated validation with expert review supports data quality and long-term interoperability. The resulting structured, failure-inclusive corpus provides a framework for data-driven research, including predictive modelling, inverse design of target morphologies, and systematic mapping of instability regimes that would otherwise require extensive trial-and-error experimentation....

---

### 4. Generative AI for material design: A mechanics perspective from burgers to matter

**Authors:** Vahidullah Tac, Ellen Kuhl

**Published:** 2026-04-03

**Category:** cs.CE

**ID:** 2604.03409v2

**Link:** [http://arxiv.org/abs/2604.03409v2](http://arxiv.org/abs/2604.03409v2)

**Summary:** Generative artificial intelligence offers a new paradigm to design matter in high-dimensional spaces. However, its underlying mechanisms remain difficult to interpret and limit adoption in computational mechanics. This gap is striking because its core tools-diffusion, stochastic differential equations, and inverse problems-are fundamental to the mechanics of materials. Here we show that diffusion-based generative AI and computational mechanics are rooted in the same principles. We illustrate this connection using a three-ingredient burger as a minimal benchmark for material design in a low-dimensional space, where both forward and reverse diffusion admit analytical solutions: Markov chains with Bayesian inversion in the discrete case and the Ornstein-Uhlenbeck process with score-based reversal in the continuous case. We extend this framework to a high-dimensional design space with 146 ingredients and 8.9x10^43 possible configurations, where analytical solutions become intractable. We therefore learn the discrete and continuous reverse processes using neural network models that infer inverse dynamics from data. We train the models on only 2,260 recipes and generate one million samples that capture the statistical structure of the data, including ingredient prevalence and quantitative composition. We further generate five new burgers and validate them in a blinded restaurant-based sensory study with n = 101 participants, where three of the AI-designed burgers outperform the classical Big Mac in overall liking, flavor, and texture. These results establish diffusion-based generative modeling as a physically grounded approach to design in high-dimensional spaces. They position generative AI as a natural extension of computational mechanics, with applications from burgers to matter, and establish a path toward data-driven, physics-informed generative design....

---


<!-- ARXIV_PAPERS_END -->