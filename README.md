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

*Last updated: 2026-07-04 07:01:11 (SGT)*

### 1. Mirror Illusion Art

**Authors:** Xiaopei Zhu, Zeyuan Li, Jun Zhu, Xiaolin Hu

**Published:** 2026-07-02

**Category:** cs.CV

**ID:** 2607.02015v1

**Link:** [http://arxiv.org/abs/2607.02015v1](http://arxiv.org/abs/2607.02015v1)

**Summary:** Mirror Illusion Art is a novel reflection-conditioned 3D illusion where one object yields two target appearances (front and mirror). The task is formulated as inverse design from two target 2D images (front and mirror) to a printable 3D object with geometry and texture. Prior topology-driven and shadow-based approaches demand substantial manual effort, optimize shape only, and often yield non-smooth or incomplete geometry. To address these challenges, we propose AutoMIA, an automated Mirror Illusion Art design pipeline that jointly optimizes shape and color. To stabilize optimization and suppress artifacts, four mechanisms are introduced: (1) projection-alignment component (PAC) selection to reduce surface noise, (2) position-weighted adaptive (PWA) suppression for background noise, (3) internal voxel preservation (IVP) to prevent internal fractures, and (4) shape-color decoupled (SCD) optimization that balance shape and color optimization. AutoMIA generate diverse smooth Mirror Illusion artworks successfully both in the digital and physical world, with only around 76s design time and 2.6 GB memory on average using a single RTX 3090, advancing inverse graphics and computational design. Our code is available at https://github.com/zxp555/AutoMIA....

---

### 2. Complex crystal structure prediction using ML-enhanced multi-minima iterative genetic algorithm

**Authors:** Ling Tang, Weiyi Xia, Tyler J. Slade, Paul C. Canfield, Cai-Zhuang Wang

**Published:** 2026-07-01

**Category:** cond-mat.mtrl-sci

**ID:** 2607.01004v1

**Link:** [http://arxiv.org/abs/2607.01004v1](http://arxiv.org/abs/2607.01004v1)

**Summary:** Current machine learning (ML) approaches for materials discovery rely heavily on known structural databases, limiting their ability to identify entirely novel structure types. In this work, we develop a multi-minima iterative genetic algorithm (MMIGA) that integrates an artificial-neural-network machine learning (ANN-ML) interatomic potential with an iterative, metadynamics-inspired penalty scheme. We demonstrate the robustness of this method on a complex ternary La-Co-Pb system, characterized by Co-Pb immiscibility and an intricate energy landscape. The ML-enhanced MMIGA successfully predicts the ground-state Pbam structure of the recently synthesized La4Co4Pb antagonistic-pair-phase, a novel structure missed by previous database-reliant ML predictions, while also identifying multiple metastable competing phases. Additionally, we challenged the MMIGA method to predict the structure of La5CoPb2 antagonistic-pair-phase, a new compound discovered during earlier attempts to synthesize the predicted phase La3CoPb. With only knowledge of the composition, our MMIGA approach successfully predicts the orthorhombic structure of La5CoPb2, producing an exact match with the structure independently determined by x-ray diffraction. By efficiently mapping both global minimum and relevant competing metastable states, this approach provides critical theoretical insights into phase selection for novel quantum and magnetic materials....

---

### 3. Graph-Native Reinforcement Learning Enables Traceable Scientific Hypothesis Generation through Conceptual Recombination

**Authors:** Subhadeep Pal, Shashwat Sourav, Tirthankar Ghosal, Markus J. Buehler

**Published:** 2026-07-01

**Category:** cs.AI

**ID:** 2607.00924v1

**Link:** [http://arxiv.org/abs/2607.00924v1](http://arxiv.org/abs/2607.00924v1)

**Summary:** Accelerating materials discovery requires AI systems that can generate scientifically valid hypotheses through multi-step, domain-grounded reasoning. Standard large language models often produce fluent but weakly traceable responses to open-ended materials design problems, making it difficult to determine whether final answers are supported by coherent intermediate reasoning. We develop Graph-PRefLexOR, a family of graph-native reasoning models fine-tuned with Group Relative Policy Optimization (GRPO) to organize reasoning into explicit phases for mechanism exploration, graph construction, pattern extraction, and hypothesis synthesis. This design links neural language generation with symbolic relational structure, enabling causal connections to be constructed, inspected, and reused. On 100 open-ended questions from materials science and mechanics literature, Graph-PRefLexOR achieves 40-65% improvements over corresponding base models, with the largest gains in reasoning traceability. Embedding analyses show broader semantic exploration and approximately 2-3 times greater semantic diversity than baselines. Semantic backtracking and layer-wise hidden-state analyses further show stronger alignment between structured reasoning and final answers. Finally, test-time graph expansion reveals that additional compute primarily increases long-range conceptual recombination within a bounded semantic space, rather than simply expanding semantic coverage. These results establish graph-native reinforcement learning as a pathway toward interpretable AI systems for scientific hypothesis generation in materials design and other scientific applications....

---

### 4. Large language model-enabled automated data extraction for concrete materials informatics

**Authors:** Zhanzhao Li, Kengran Yang, Qiyao He, Kai Gong

**Published:** 2026-04-24

**Category:** cond-mat.mtrl-sci

**ID:** 2604.22938v2

**Link:** [http://arxiv.org/abs/2604.22938v2](http://arxiv.org/abs/2604.22938v2)

**Summary:** The promise of data-driven materials discovery remains constrained by the scarcity of large, high-quality, and accessible experimental datasets. Here, we introduce a generalizable large language model (LLM)-powered pipeline for automated extraction and structuring of materials data from unstructured scientific literature, using concrete materials as a representative and particularly challenging example. The pipeline exhibits robust performance across a broad range of LLMs and achieves an $F_1$ score of up to 0.98 for diverse composition--process--property attributes. Within one hour, it extracts nearly 9,000 high-quality records with over 100 attributes from a corpus screened from more than 27,000 publications, enabling the construction of the largest open laboratory database for blended cement concrete. Machine learning analyses underscore the importance of large, diverse, and information-rich datasets for enhancing both in-distribution accuracy and out-of-distribution generalization to unseen materials. The proposed pipeline is readily adaptable to other materials domains and accelerates the development of scalable data infrastructures for materials informatics....

---


<!-- ARXIV_PAPERS_END -->