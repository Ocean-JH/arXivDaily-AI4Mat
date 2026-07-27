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

*Last updated: 2026-07-28 06:59:31 (SGT)*

### 1. SAGE-Net: Semantics-Augmented Geometric Encoder for Material Property Prediction

**Authors:** Guanghui Zhang, Yuxuan Yao, Kieran B. Spooner, Jun Yin, Dan Han, David O. Scanlon, Lijun Zhang

**Published:** 2026-07-24

**Category:** cond-mat.mtrl-sci

**ID:** 2607.22271v1

**Link:** [http://arxiv.org/abs/2607.22271v1](http://arxiv.org/abs/2607.22271v1)

**Summary:** Reliable structure-property modeling is crucial for accelerating materials discovery, where crystal graphs and structure-derived crystallographic descriptions provide complementary geometric and semantic information. Existing multimodal materials models primarily incorporate textual information through post-encoding fusion, latent-space alignment, or attention-based representation interaction mechanisms. However, in most cases, crystallographic semantics are introduced after structural encoding and therefore cannot directly guide the formation of atom-level crystal-graph representations. Here, we present Semantics-Augmented Geometric Encoder Network (SAGE-Net), a flexible multimodal framework that injects description-derived chemical and crystallographic semantics into geometric message passing. SAGE-Net introduces Semantic-Guided Message Passing (SGMP), which gates atom-level updates and enables crystallographic semantics to directly modulate local geometric interactions across multiple graph neural network (GNN) backbones. Across benchmarks covering bandgap, mechanical, transport-related properties, and synthesizability assessment, the SAGE-Net instantiated with different GNN backbones achieves the lowest MAE on eight out of ten JARVIS-DFT regression targets and delivers strong or highly competitive performance against both structure-based and multimodal baselines. For synthesizability assessment, the SAGE-Net demonstrate outstanding classification performance and high recall rates. Interpretability analysis unravels that SAGE-Net effectively captures physically interpretable crystallographic features, viz. space group, dimensionality, polyhedral environments, among others. Together, these results demonstrate SGMP-based SAGE-Net as a general and transferable framework for deeply integrated multimodal materials learning....

---

### 2. Property-Guided Diffusion for Inverse Design of Crystalline Materials

**Authors:** Sourav Mal, Subhankar Mishra, Prasenjit Sen

**Published:** 2026-07-23

**Category:** cond-mat.mtrl-sci

**ID:** 2607.21849v1

**Link:** [http://arxiv.org/abs/2607.21849v1](http://arxiv.org/abs/2607.21849v1)

**Summary:** Diffusion-based generative models with property guidance have emerged as a promising paradigm for inverse materials design by enabling the generation of crystalline materials with user-specified target properties. However, despite recent advances, the effectiveness of property guidance, its influence on crystallographic symmetry, and the physical viability of generated materials remain poorly understood. To address these questions, we develop a property-guided framework based on the lightweight diffusion model DiffCrysGen using parameter-efficient adapter fine-tuning and classifier-free guidance (CFG). The resulting framework enables efficient multi-property crystal generation while preserving the knowledge learned during unconditional pre-training. Using formation energy together with saturation magnetization and Vickers hardness as representative inverse-design tasks, we systematically investigate the influence of CFG across a broad range of guidance strengths. Increasing the guidance scale progressively steers the generated property distributions toward the prescribed targets while reducing the fraction of lowest-symmetry ($P1$) structures and increasing the proportion of higher-symmetry structures. To evaluate physical viability, generated structures are geometrically prescreened and subsequently validated using a machine-learning interatomic potential (MLIP)-based workflow comprising structural relaxation and thermodynamic, dynamical, and property-specific analyses. The framework identifies thermodynamically and dynamically stable magnetic and mechanically hard materials with overall success rates of 12.3\% and 3.9\%, respectively. These results establish property-guided DiffCrysGen as an efficient framework for inverse materials design while providing new insights into the role of classifier-free guidance in crystal generation....

---

### 3. Generative and multimodal AI for materials prediction and design: Progress, challenges, and perspectives

**Authors:** Xianyuan Liu, Charles Anjah, Benjamin E. Jolly, Jonathon F. S. Markanday, Joshua Berry, Haolin Wang, Nicola A. Morley, Robert D. J. Oliver, Alexandra J. Ramadan, Delvin Ce Zhang, Katerina A. Christofidou, Haiping Lu

**Published:** 2026-07-22

**Category:** cond-mat.mtrl-sci

**ID:** 2607.21660v1

**Link:** [http://arxiv.org/abs/2607.21660v1](http://arxiv.org/abs/2607.21660v1)

**Summary:** Artificial intelligence (AI) is accelerating materials prediction and design by enabling efficient exploration of chemical and structural spaces, with particular promise for novel materials discovery. However, novelty in materials discovery encompasses chemical plausibility, structural distinctiveness, property relevance and experimental realisability, making AI-driven novelty claims difficult to substantiate. We introduce a materials property hierarchy, from intrinsic, composition-determined properties to extrinsic, processing-dependent performance, to clarify deployment constraints and distinguish structural, physical and deployment novelty. This framework motivates an evidence-based view of multimodal materials data spanning chemical composition, microstructure, processing, and testing and characterisation, showing that current evidence remains concentrated in composition and idealised structure while heterogeneous, under-represented and weakly integrated modalities limit support for physical and deployment novelty. It also highlights the limitations of benchmarks based mainly on computational labels and proxy novelty criteria. Community-wide standards for data collection, modality alignment and evidence synthesis are needed to support multimodal data construction, process-aware multimodal modelling, feasibility-first generative modelling and deployment-aware benchmarking, so that generative and multimodal AI can design experimentally realisable materials with defensible scientific and practical novelty....

---


<!-- ARXIV_PAPERS_END -->