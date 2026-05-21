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

*Last updated: 2026-05-21 13:15:31 (SGT)*

### 1. WorldParticle: Unified World Simulation of Lagrangian Particle Dynamics via Transformer

**Authors:** Caoliwen Wang, Minghao Guo, Siyuan Chen, Heng Zhang, Mengdi Wang, Xingyu Ni, Hanson Sun, Kunyi Wang, Zherong Pan, Kui Wu, Lingjie Liu, Yin Yang, Chenfanfu Jiang, Taku Komura, Wojciech Matusik, Peter Yichen Chen

**Published:** 2026-05-14

**Category:** cs.GR

**ID:** 2605.15305v4

**Link:** [http://arxiv.org/abs/2605.15305v4](http://arxiv.org/abs/2605.15305v4)

**Summary:** A unified simulator that can model diverse physical phenomena without solver-specific redesign is a long-standing goal across simulation science. We present a learning-based particle simulator built on a single transformer architecture to model cloth, elastic solds, Newtonian and non-Newtonian fluids, granular materials, and molecular dynamics. Our model follows a prediction-correction design on a shared Lagrangian particle representation. An explicit predictor first advances particles under the known external forces, producing an intermediate state that captures externally driven motion but not inter-particle interactions. A learned corrector then predicts the residual position and velocity updates through three stages: a particle tokenizer that encodes local particle-particle, particle-boundary, and topology-guided interactions; a super-token encoder that hierarchically merges particle tokens into a compact set of super tokens via alternating self-attention and token merging; and a super-token decoder that lifts these super tokens back to particle resolution through cross-attention to predict per-particle position and velocity corrections. Progressive token merging reduces the attention cost at successive encoder layers by halving the token count at each level, and the decoder communicates through the compact super-token set rather than full particle-to-particle attention. Across the six dynamics categories, the same architecture generalizes to unseen materials, boundary configurations, initial conditions, and external forces. We further demonstrate downstream interactive control, inverse design, and learning from real-world manipulation data, reducing the need for per-phenomenon solver engineering....

---

### 2. Transferable 3D Convolutional Neural Networks for Elastic Constants Prediction in Nanoporous Metals

**Authors:** Sergei Zorkaltsev, Rafał Topolnicki, Tal-El Carmon, Santhosh Mathesan, Paweł Dłotko, Dan Mordehai, Maciej Harańczyk

**Published:** 2026-05-20

**Category:** cond-mat.mtrl-sci

**ID:** 2605.20890v1

**Link:** [http://arxiv.org/abs/2605.20890v1](http://arxiv.org/abs/2605.20890v1)

**Summary:** The topology of nanoporous metals is crucial for determining their mechanical response. In this work, we generated 6,000 gold and 422 silver nanoporous structures and calculated three components of elastic modulus with Molecular Dynamics simulations, resulting in 19,263 data points. This study compared two distinct approaches of predicting elastic modulus: a Fully-Connected neural network trained on precomputed topological descriptors, and several 3D Convolutional neural network architectures adapted from computer vision. The 3D CNNs outperformed the descriptor-based baseline model ($R^2 = 0.704$), with to-performing DenseNet-201 architecture achieving $R^2 = 0.955$. Additionally, the effects of training grid resolution, dataset size, and descriptor integration into a model were investigated. We further demonstrated model robustness through Transfer learning: a pretrained model was fine-tuned on a much smaller dataset of denser gold structures and the dataset of denser silver structures. Finally, the trained model was employed to evaluate the mechanical properties of 100,000 stochastic nanoporous gold structures and identify the Pareto optimal designs....

---

### 3. Open Materials 2024 (OMat24) Inorganic Materials Dataset and Models

**Authors:** Luis Barroso-Luque, Muhammed Shuaibi, Xiang Fu, Brandon M. Wood, Misko Dzamba, Meng Gao, Ammar Rizvi, C. Lawrence Zitnick, Zachary W. Ulissi

**Published:** 2024-10-16

**Category:** cond-mat.mtrl-sci

**ID:** 2410.12771v2

**Link:** [http://arxiv.org/abs/2410.12771v2](http://arxiv.org/abs/2410.12771v2)

**Summary:** The ability to discover new materials with desirable properties is critical for numerous applications from helping mitigate climate change to advances in next generation computing hardware. AI has the potential to accelerate materials discovery and design by more effectively exploring the chemical space compared to other computational methods or by trial-and-error. While substantial progress has been made on AI for materials data, benchmarks, and models, a barrier that has emerged is the lack of publicly available training data and open pre-trained models. To address this, we present a Meta FAIR release of the Open Materials 2024 (OMat24) large-scale open dataset and an accompanying set of pre-trained models. OMat24 contains over 110 million density functional theory (DFT) calculations focused on structural and compositional diversity. Our EquiformerV2 models achieve state-of-the-art performance on the Matbench Discovery leaderboard and are capable of predicting ground-state stability and formation energies to an F1 score above 0.9 and an accuracy of 20 meV/atom, respectively. We explore the impact of model size, auxiliary denoising objectives, and fine-tuning on performance across a range of datasets including OMat24, MPtraj, and Alexandria. The open release of the OMat24 dataset and models enables the research community to build upon our efforts and drive further advancements in AI-assisted materials science....

---


<!-- ARXIV_PAPERS_END -->