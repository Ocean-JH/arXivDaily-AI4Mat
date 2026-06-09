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

## New Papers (6)

*Last updated: 2026-06-10 07:15:55 (SGT)*

### 1. CatalyticMLLM: A Graph-Text Multimodal Large Language Model for Catalytic Materials

**Authors:** Yanjie Li, Jian Xu, Xu-Yao Zhang, Shiming Xiang, Nian Ran, Weijun Li, Cheng-Lin Liu

**Published:** 2026-05-17

**Category:** cs.AI

**ID:** 2605.17254v3

**Link:** [http://arxiv.org/abs/2605.17254v3](http://arxiv.org/abs/2605.17254v3)

**Summary:** Property prediction and inverse structural design of catalytic materials are typically modeled as two independent tasks: the former predicts target properties from given structures, whereas the latter generates candidate structures according to desired properties. Although the decoupled paradigm facilitates the implementation of a ``generation--evaluation--screening'' workflow, the inconsistency between the generative model and the property prediction model in terms of representation spaces and training objectives can readily introduce data distribution shifts and evaluator bias, thereby limiting the stability of closed-loop optimization.
  In this work, we propose CatalyticMLLM, a unified graph--text multimodal large language model for catalytic materials, which integrates property prediction and \textbf{inverse design} within the same model and shared representation space. Under this unified framework, CatalyticMLLM can not only perform reliable property prediction by leveraging three-dimensional structures and textual information, but also generate and screen physically feasible CIF candidates conditioned on target properties, thereby forming a closed-loop optimization workflow of ``inverse design--prediction--screening--redesign.'' Experimental results demonstrate that this unified paradigm outperforms decoupled baselines on both catalytic relaxed-energy prediction and inverse design tasks, validating the effectiveness of jointly modeling property prediction and structure generation within a single multimodal model....

---

### 2. Physics-Guided Sequence-Based Generative Framework for Acoustic Metamaterial Inverse Design

**Authors:** Yijie Li, Jiahao Xu, Ching-Chih Tsao, Lili Qiu, Jingxian Wang

**Published:** 2026-06-08

**Category:** cs.SD

**ID:** 2606.09266v1

**Link:** [http://arxiv.org/abs/2606.09266v1](http://arxiv.org/abs/2606.09266v1)

**Summary:** Acoustic metamaterial (AMM) inverse design is particularly challenging for broadband target responses due to acoustic dispersion: a structure that matches the desired response at one frequency may deviate at others, and modifying geometry to improve one sub-band often perturbs neighboring sub-bands. Yet existing broadband inverse-design approaches are either constrained by predefined templates, or rely on image representations that fail to preserve the geometric precision and structural connectivity required by acoustic structures. We present MetaSeq, a physics-guided, sequence-based generative framework for acoustic metamaterial inverse design. At its core, MetaSeq introduces a language that represents each AMM as a structured sequence, rather than as a pixel grid or fixed template. This representation preserves precise geometry, explicitly encodes connectivity, and casts inverse design as a sequence-to-sequence task from target response to structure sequence. MetaSeq further constructs a balanced, high-fidelity dataset with efficient calibration and complexity-based sampling. To address the one-to-many nature of inverse design, MetaSeq combines supervised pretraining with reinforcement learning fine-tuning guided by a physics-based solver and validity checker. Extensive evaluations against COMSOL and five baselines show that MetaSeq reduces response error by 45% over the best baseline....

---

### 3. Hyper-Dimensional Fingerprints as Molecular Representations

**Authors:** Jonas Teufel, Luca Torresi, André Eberhard, Pascal Friederich

**Published:** 2026-04-30

**Category:** cs.LG

**ID:** 2604.27810v2

**Link:** [http://arxiv.org/abs/2604.27810v2](http://arxiv.org/abs/2604.27810v2)

**Summary:** Computational molecular representations underpin virtual screening, property prediction, and materials discovery. Conventional fingerprints are efficient and deterministic but lose structural information through hash-based compression, particularly at low dimensionalities. Learned representations from graph neural networks recover this expressiveness but require task-specific training and substantial computational resources. Here we introduce hyperdimensional fingerprints (HDF), which replace the learned transformations of message-passing neural networks with algebraic operations on high-dimensional vectors, producing deterministic molecular representations without any training. Across diverse property prediction benchmarks, HDF outperforms conventional fingerprints in the majority of tasks while exhibiting greater consistency across datasets and models. Crucially, HDF embeddings preserve molecular similarity faithfully: at 32 dimensions, distances in HDF space achieve a 0.9 Pearson correlation with graph edit distance, compared to 0.55 for Morgan fingerprints at equivalent size. This structural fidelity persists at low dimensions where hash-based methods degrade, allowing simple nearest-neighbor regression to remain predictive with as few as 64 components. We further demonstrate the practical impact in Bayesian molecular optimization, where HDF-based surrogate models achieve substantially improved sample efficiency in regimes where Morgan fingerprints perform comparably to random search. HDF thus provides a general-purpose, training-free alternative to conventional molecular fingerprints, suggesting that the information loss long accepted as inherent to fixed-length fingerprints is a limitation of the hash-based encoding scheme rather than the fingerprint paradigm itself....

---

### 4. A large-scale nanocrystal database with aligned synthesis and properties enabling generative inverse design

**Authors:** Kai Gu, Yingping Liang, Senliang Peng, Aotian Guo, Haizheng Zhong, Ying Fu

**Published:** 2026-01-04

**Category:** cond-mat.mtrl-sci

**ID:** 2601.02424v2

**Link:** [http://arxiv.org/abs/2601.02424v2](http://arxiv.org/abs/2601.02424v2)

**Summary:** The synthesis of nanocrystals has been highly dependent on trial-and-error, due to the complex correlation between synthesis parameters and physicochemical properties. Although deep learning offers a potential methodology to achieve generative inverse design, it is still hindered by the scarcity of high-quality datasets that align nanocrystal synthesis routes with their properties. Here, we present the construction of a large-scale, aligned Nanocrystal Synthesis-Property (NSP) database and demonstrate its capability for generative inverse design. To extract structured synthesis routes and their corresponding product properties from literature, we develop NanoExtractor, a large language model (LLM) enhanced by well-designed augmentation strategies. NanoExtractor is validated against human experts, achieving a weighted average score of 88% on the test set, significantly outperforming chemistry-specialized (3%) and general-purpose LLMs (38%). The resulting NSP database contains nearly 160,000 aligned entries and serves as training data for our NanoDesigner, an LLM for inverse synthesis design. The generative capability of NanoDesigner is validated through the successful design of viable synthesis routes for both well-established PbSe nanocrystals and rarely reported MgF2 nanocrystals. Notably, the model recommends a counter-intuitive, non-stoichiometric precursor ratio (1:1) for MgF2 nanocrystals, which is experimentally confirmed as critical for suppressing byproducts. Our work bridges the gap between unstructured literature and data-driven synthesis, and also establishes a powerful human-AI collaborative paradigm for accelerating nanocrystal discovery....

---

### 5. Data-model Coevolution as the Architectural Principle for AI-Native Materials Databases

**Authors:** Fengyu Xie, Ruoyu Wang, Taoyuze Lv, Yuxiang Gao, Hongyu Wu, Zhicheng Zhong

**Published:** 2025-11-16

**Category:** cond-mat.mtrl-sci

**ID:** 2511.12420v2

**Link:** [http://arxiv.org/abs/2511.12420v2](http://arxiv.org/abs/2511.12420v2)

**Summary:** AI-native approaches are reshaping computational materials discovery into iterative data-model coevolution cycles. However, most existing materials databases remain fundamentally data-centric, where predictive models remain external to database state and data growth is decoupled from model updating. Here we formalize data-model coevolution as the architectural basis of AI-native materials databases, where data and predictive models evolve through endogenous generation-evaluation-refinement cycles. Using the Li-P-S ternary as a demonstrative prototype, we generated approximately 70,000 candidate structures, more than 10,000 of which satisfy the stable-unique-novel (S.U.N.) criterion, achieving rapid saturation of local chemical environments together with stabilization of energy distributions. We autonomously found chemically plausible phases and motifs outside the Materials Project (MP) and Alexandria databases, including a stable Li$_2$PS$_3$ phase, the (PS$_3$)$_3^{3-}$ trimer, the (P$_3$S$_8$)$^{3-}$ ring, two isomers of the (P$_2$S$_8$)$^{2-}$ ring, and polymeric (PS$_4$)$_n^{n-}$ chains. Within two to three iterations, the integrated predictive models converged to high precision under a low first-principles cost, and the resulting data-model state can be directly queried for atomistic and electronic-structure properties within the same unified framework. Data-model states can be reused and extended across related chemical systems, enabling scalable and continuous accumulation of computational materials knowledge. These results demonstrate data-model coevolution as a practical architectural principle for AI-era materials data infrastructure....

---

### 6. Information-Theoretic Requirements for Gradient-Based Task Affinity Estimation in Multi-Task Learning

**Authors:** Jasper Zhang, Bryan Cheng

**Published:** 2026-04-09

**Category:** cs.LG

**ID:** 2604.07848v2

**Link:** [http://arxiv.org/abs/2604.07848v2](http://arxiv.org/abs/2604.07848v2)

**Summary:** Multi-task learning shows strikingly inconsistent results -- sometimes joint training helps substantially, sometimes it actively harms performance -- yet the field lacks a principled framework for predicting these outcomes. We identify a fundamental but unstated assumption underlying gradient-based task analysis: tasks must share training instances for gradient conflicts to reveal genuine relationships. When tasks are measured on the same inputs, gradient alignment reflects shared mechanistic structure; when measured on disjoint inputs, any apparent signal conflates task relationships with distributional shift. We discover this sample overlap requirement exhibits a sharp phase transition: below 30% overlap, gradient-task correlations are statistically indistinguishable from noise; above 40%, they reliably recover known biological structure. Comprehensive validation across multiple datasets achieves strong correlations and recovers biological pathway organization. Standard benchmarks systematically violate this requirement -- MoleculeNet operates at <5% overlap, TDC at 8-14% -- far below the threshold where gradient analysis becomes meaningful. This provides the first principled explanation for seven years of inconsistent MTL results....

---


<!-- ARXIV_PAPERS_END -->