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

*Last updated: 2026-07-15 06:54:48 (SGT)*

### 1. CatRetriever: Contrastive Representation Learning for Slab-to-Bulk Retrieval in Generative Catalyst Discovery

**Authors:** Jungho Oh, Woosung Kim, Dong Hyeon Mok, Jonggeol Na, Seoin Back

**Published:** 2026-07-13

**Category:** cs.LG

**ID:** 2607.11712v1

**Link:** [http://arxiv.org/abs/2607.11712v1](http://arxiv.org/abs/2607.11712v1)

**Summary:** Inverse design is an emerging data-driven paradigm for efficiently navigating vast chemical spaces to discover new materials with targeted properties, and in the context of heterogeneous catalysis, surface generative models have recently advanced this goal by directly generating catalyst surface-adsorbate structures. However, these models typically operate at the slab level and do not provide the corresponding parent bulk structure, making it difficult to assess bulk-dependent properties such as formation energy, surface energy, crystallographic symmetry, and synthesizability. Here, we address this missing slab-to-bulk connection as a retrieval problem and introduce CatRetriever, a contrastive representation learning model that aligns slab and bulk crystal representations in a shared latent space. From a slab query, CatRetriever accurately retrieves plausible parent bulk candidates with R@1 > 91% and R@3 > 98% on both the in-distribution and holdout evaluation sets. We further extend the CatRetriever framework into an adsorption energy targeted bulk discovery pipeline that combines bulk retrieval, generative search space expansion, and adsorption energy distribution analysis. This workflow evaluates candidates by both structural compatibility with the query slab and their ability to access the target adsorption energy range across diverse surface environments. CatRetriever therefore provides a scalable route for connecting catalyst generative models with physically plausible and adsorption energy compatible bulk catalyst discovery....

---

### 2. Uncertainty-Aware Structure-Property Mapping of Spinodoid Metamaterials via Heteroscedastic Gaussian Process Regression

**Authors:** Minwoo Park, Junseo Park, Mingyu Lee, Hugon Lee, Hanbin Cho, Ikjin Lee, Seunghwa Ryu

**Published:** 2026-07-13

**Category:** physics.comp-ph

**ID:** 2607.11209v1

**Link:** [http://arxiv.org/abs/2607.11209v1](http://arxiv.org/abs/2607.11209v1)

**Summary:** Spinodoid metamaterials offer a broad, tunable design space for anisotropic mechanical properties, yet their structure-property relationships are commonly treated as representative mappings from cone-angle descriptors to single effective stiffness values. This deterministic view overlooks the stochastic nature of Gaussian random field (GRF)-based topology generation, where identical cone-angle descriptors can produce different morphology realizations and property scatter. Here, we present an uncertainty-aware structure-property mapping framework that reinterprets cone-angle descriptors as stochastic descriptors associated with input-dependent property distributions. Using heteroscedastic Gaussian process regression (GPR), the framework infers input-dependent predictive uncertainty from sparse one-realization-per-point data without requiring empirical variance labels at every design point. The results show that stiffness scatter differs across tensor components according to each component's mechanically active directions, and that parameter sets yielding identical mean stiffness can carry different aleatoric uncertainty. Applying this uncertainty to reliability-based design optimization (RBDO), we show that a deterministic optimum is highly susceptible to constraint violation once morphology-induced variability is considered, and that a homoscedastic RBDO formulation fails to meet the prescribed reliability target - only the heteroscedastic formulation satisfies the reliability target under the heteroscedastic uncertainty evaluation. This establishes uncertainty-aware surrogate modeling as essential for reliability-aware inverse design of spinodoid metamaterials; extending the framework to nonlinear responses remains for future work....

---

### 3. A Multi-Agent Framework for Zero-Dimensional Reduced-Order Model Planning

**Authors:** Bingteng Sun, Hao Yin, Yiling Chen, Renjie Xiao, Lei Xie, Shanyou Wang, Ruonan Wang, Shubao Chen, Qingzong Xu, Lin Lu, Qiang Du, Junqiang Zhu

**Published:** 2026-07-13

**Category:** cs.LG

**ID:** 2607.10994v1

**Link:** [http://arxiv.org/abs/2607.10994v1](http://arxiv.org/abs/2607.10994v1)

**Summary:** Zero-dimensional reduced-order models (0D ROMs) are central to multi-dimensional design workflows for high-end complex equipment. However, the planning process currently relies on manual expertise, limiting topological exploration and prolonging iterations. Even traditional optimization methods such as Genetic Algorithms (GA) are typically confined to local parameter tuning. Although Large Language Model (LLM) agents have shown promise in exploring large sample spaces, and frameworks such as Chain of Thought (CoT) and Reason and Act (ReAct) improve reasoning reliability, while Retrieval-Augmented Generation (RAG) overcomes domain knowledge barriers, a single agent still falls short for the long-horizon and highly coupled nature of complex 0D ROM planning. This paper proposes the Zero-dimensional reduced-order model CO-Planning framework (Z-COPA), a multi-agent architecture featuring a Symbolic Action Graph Engine (SAGE) and a MILP-Guided Navigation (MGN) optimizer. Its core innovation is a dedicated graph representation method that accurately encodes the 0D flow network topology, converting the empirical planning process into a rigorous graph structure optimization problem. We validate the forward and inverse design capabilities and generalization performance of Z-COPA on two real aircraft engine secondary-air systems, two IEEE power-distribution reconfiguration benchmarks, and two water-distribution network benchmarks. The results show superior task completion quality, obtaining the best performance in both forward and reverse design of air systems. Z-COPA disrupts the traditional 0D model planning paradigm, providing a new technical approach for exploring broader topological space and achieving highly automated, globally optimal air system architectures....

---

### 4. Large language model agents accelerate inverse design of metal-organic frameworks for gas separation

**Authors:** Zhaolin Hu, Hehe Fan, Wangyihan Guo, Meng Xu, Chenhao Rao, Qiwei Yang, Yi Yang

**Published:** 2026-07-12

**Category:** cs.AI

**ID:** 2607.10559v1

**Link:** [http://arxiv.org/abs/2607.10559v1](http://arxiv.org/abs/2607.10559v1)

**Summary:** Metal-organic frameworks (MOFs) offer a highly modular platform for adsorptive gas separation, yet their vast reticular design space makes inverse design difficult under simultaneous constraints of chemical validity, separation performance, and structural diversity. Here, we present LEMO Agent, a large-language-model agent framework for closed-loop inverse design of gas-separation MOFs in MOFid space. LEMO Agent couples language-based candidate generation with MOFid standardization, explicit validity checking, Transformer-based property prediction, structured design memory, and multi-island exploration. Through iterative generate--validate--evaluate--remember cycles, the agent uses feedback from both successful and failed candidates to guide chemically constrained search across linker, metal, and topology choices. We evaluate LEMO Agent on CH$_4$/N$_2$ and CO$_2$/N$_2$ separation tasks. Compared with representative generative, optimization, and agentic baselines, LEMO Agent enriches high-performing candidates, improves predicted separation performance, and maintains broad chemical and topological diversity. Selected candidates are further reconstructed, evaluated by GCMC simulations, and passed through an experimental down-selection workflow based on chemical feasibility and ligand purchasability, leading to initial wet-lab synthesis and SEM characterization. These results demonstrate that large language model agents can serve as interpretable and scalable design engines for accelerating MOF discovery beyond conventional fixed-library screening....

---

### 5. The evolution of AI from image interpretation toward scientific inference in nanoparticle electron microscopy

**Authors:** Evropi Toulkeridou, Jiafei Li, Leonardo Lari, Panagiotis Grammatikopoulos

**Published:** 2026-07-11

**Category:** cond-mat.mtrl-sci

**ID:** 2607.10388v1

**Link:** [http://arxiv.org/abs/2607.10388v1](http://arxiv.org/abs/2607.10388v1)

**Summary:** Artificial intelligence (AI) is transforming electron microscopy by enabling quantitative analysis of increasingly large and complex datasets for nanoparticle characterization. Recent advances in machine learning (ML) and deep learning (DL) have expanded microscopy from a descriptive imaging technique into a data-driven platform for structural interpretation, dynamic analysis, and scientific inference. This review examines AI methodologies for nanoparticle electron microscopy, focusing on transmission electron microscopy (TEM), high-resolution transmission electron microscopy (HRTEM), scanning transmission electron microscopy (STEM), and in situ TEM. The discussion is organized around the principal challenges in nanoparticle characterization, including particle detection, segmentation, morphology quantification, atomic-resolution restoration, defect identification, two-dimensional-to-three-dimensional structural inference, and analysis of dynamic processes in situ. We review computational approaches from conventional ML and convolutional neural networks to transformer architectures, self-supervised learning, foundation models, multimodal AI, and physics-informed learning. We further discuss integrating microscopy data with simulations, metadata, and autonomous experimentation to relate nanoparticle structure, dynamics, synthesis conditions, and functional properties. The advantages, limitations, benchmarking, and data requirements of current methodologies are critically assessed. Finally, emerging opportunities for foundation models, AI-guided microscopy, closed-loop experimentation, and autonomous materials discovery are discussed. By integrating advances across computer vision, materials informatics, and electron microscopy, this review highlights the role of AI in next-generation nanoparticle characterization and accelerated materials discovery....

---

### 6. An Autonomous Scientific Knowledge Generation Framework for AI-Driven Scientific Discovery

**Authors:** Dibakar Datta

**Published:** 2026-07-09

**Category:** cs.DL

**ID:** 2607.09806v1

**Link:** [http://arxiv.org/abs/2607.09806v1](http://arxiv.org/abs/2607.09806v1)

**Summary:** Artificial intelligence (AI) is transforming scientific discovery, but its effectiveness is fundamentally limited by the availability of structured scientific knowledge. Although existing databases have accelerated data-driven materials research, much of the knowledge needed for predictive modeling and inverse design remains embedded in unstructured scientific literature. We present an Autonomous Scientific Knowledge Generation Framework that transforms scientific publications into a Unified AI-Ready Scientific Knowledge Base. The framework integrates ontology-guided literature acquisition, hybrid scientific knowledge extraction, semantic harmonization, knowledge fusion, and validation within a unified workflow. Rather than treating literature retrieval, information extraction, and database construction as separate tasks, the framework progressively converts scientific publications into structured, semantically consistent, and provenance-preserving knowledge suitable for AI-driven reasoning. As a proof of concept, the framework was applied to electro-optic materials. Autonomous literature acquisition retrieved and validated about 1,000 publications from multiple scholarly repositories. A representative subset of eight publications was processed through the complete workflow, generating 29 structured scientific records that were harmonized into 7 canonical scientific records. The results demonstrate the complete transformation from scientific literature to an AI-ready scientific knowledge base while preserving quantitative measurements, operating conditions, provenance, and scientific context. The proposed framework provides a scalable, domain-independent foundation for predictive AI, generative AI, and closed-loop AI-driven scientific discovery....

---

### 7. SlaKoNet-VQD: A universal Slater-Koster tight-binding Hamiltonian for variational quantum band-structure calculations on near-term hardware

**Authors:** Akshaya Ajith, Jaehyung Lee, Charles Rhys Campbell, Kamal Choudhary

**Published:** 2026-07-06

**Category:** cond-mat.mtrl-sci

**ID:** 2607.09761v1

**Link:** [http://arxiv.org/abs/2607.09761v1](http://arxiv.org/abs/2607.09761v1)

**Summary:** Variational quantum algorithms such as VQE and VQD are promising for near-term electronic structure calculations, but for periodic solids their reach is limited by the cost of building a faithful second-quantized Hamiltonian, typically via DFT plus Wannierization or hand-fit tight-binding parameters. SlaKoNet addresses this by combining deep learning with the Slater-Koster tight-binding formalism to fit hopping and overlap parameters across 65 elements, enabling deterministic Hamiltonian construction for any crystal built from these elements. Here we couple a SlaKoNet model trained on JARVIS-TBmBJ with a Qiskit-based VQD algorithm, replacing costly Hamiltonian construction with a universal neural Hamiltonian generator. The resulting SlaKoNet-VQD workflow is structure-agnostic, differentiable, and suited to high-throughput bandstructure screening. We benchmark on silicon, recovering the full eight-band structure along the standard k-path with mean absolute deviation of 1.78 meV from exact diagonalization on a 3-qubit simulator, and extend to five conventional superconductors (Al, Ta, Nb, V, ZrN) with similar accuracy. We demonstrate execution on IBM Quantum hardware for a k-point ground-state calculation on aluminum (MAE ~0.37 eV). We further promote the Hamiltonian to a correlated Hubbard model solved via dynamical mean-field theory, recovering weakening correlations across group-5 metals and strong quasiparticle renormalization in La2CuO4, identifying the impurity problem as a natural quantum solver target. This pipeline enables high-throughput VQA benchmarking across the periodic table and gradient-based ansatz-Hamiltonian co-optimization for materials discovery. Web app: https://atomgpt.org/quantum....

---


<!-- ARXIV_PAPERS_END -->