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

*Last updated: 2026-07-01 07:10:01 (SGT)*

### 1. Accelerated Inorganic Electrides Discovery by Generative Models and Hierarchical Screening

**Authors:** Shuo Tao, Qiang Zhu

**Published:** 2026-01-28

**Category:** cond-mat.mtrl-sci

**ID:** 2601.21077v2

**Link:** [http://arxiv.org/abs/2601.21077v2](http://arxiv.org/abs/2601.21077v2)

**Summary:** Electrides are exotic compounds in which excess electrons occupy interstitial regions of the crystal lattice and serve as anions, exhibiting exceptional properties such as low work function, high electron mobility, and strong catalytic activity. Although they show promise for diverse applications, identifying new electrides remains challenging due to the difficulty of achieving energetically favorable electron localization in crystal cavities. Here, we present an accelerated materials discovery framework that combines physical principles, diffusion-based materials generation with hierarchical thermodynamic and electronic structure screening. Using this workflow, we systematically explored 1,510 binary and 6,654 ternary chemical compositions containing excess valence electrons from electropositive alkaline, alkaline-earth, and early transition metals, and then filtered them with a high throughput validation on both thermodynamical stability and electronic structure analysis. As a result, we have identified 264 new electron rich compounds within 0.05 eV/atom above the convex hull at the density functional theory (DFT) level, including 13 thermodynamically stable electrides. Our approach demonstrates a generalizable strategy for targeted materials discovery in a vast chemical space....

---

### 2. Interpretable Inverse Design of Metal-Organic Frameworks with Large Language Model Agents

**Authors:** Kyungmin Nam, Seunghee Han, Jihan Kim

**Published:** 2026-06-28

**Category:** cs.LG

**ID:** 2606.29459v1

**Link:** [http://arxiv.org/abs/2606.29459v1](http://arxiv.org/abs/2606.29459v1)

**Summary:** Inverse design of metal-organic frameworks (MOFs) requires searching a combinatorially vast space where property labels are expensive and most machine-learning models reveal little about why a structure succeeds. We introduce LLM4MOF, a closed-loop framework in which language-model agents reason about chemistry, build candidate MOFs, and test them in simulation, refining hypotheses over ten autonomous iterations. One agent proposes interpretable design hypotheses over metal nodes, linkers, pore geometry, and functional chemistry, and a second translates them into constraints that select candidate MOFs, each made of a metal node, organic linker, and matching topology. Each hypothesis is tested through four diagnostic beams that apply different subsets of its constraints, so comparing them shows whether geometry, chemistry, or metal choice drives performance. Even when blind to the global property landscape of databases, LLM4MOF concentrates its search on top-performing structures across six adsorption, separation, and electronic-structure tasks within 400 property evaluations. The same loop also generates new MOFs de novo and validates them in live simulation, where it adapts the geometry to each requested condition, outperforming random search and a genetic algorithm at roughly $1 per campaign. LLM4MOF shows that language-model agents can run interpretable, simulation-grounded inverse design without training a model per objective....

---

### 3. Latent Genetic Algorithm for Crystal Structure Prediction

**Authors:** Kaixin Zheng, Wanjian Yin, Hongyu Yu, Hongjun Xiang

**Published:** 2026-06-28

**Category:** physics.comp-ph

**ID:** 2606.29220v1

**Link:** [http://arxiv.org/abs/2606.29220v1](http://arxiv.org/abs/2606.29220v1)

**Summary:** Predicting crystal structures requires navigating rugged energy landscapes in which favorable local motifs must be inherited across candidates with incompatible cells, densities, and symmetries. Conventional real-space crossover often destroys these motifs when parent structures are geometrically mismatched. Here we show that latent representations learned by pretrained universal interatomic potentials can serve as continuous evolutionary coordinates for crystal structure prediction. In the Latent Genetic Algorithm (LGA), offspring are generated by inverse optimization of atomic positions and lattice vectors to match a target latent representation, which is constructed via interpolation of the parent latent vectors. LGA suppresses high-energy and short-contact offspring, increases the HfO$_2$ ground-state recovery rate from 20-35% to 60-95%, and enables a unified variable-supercell search over 16 perovskites with a nearly tenfold reduction in search cost. Applied to (PbTiO$_3$)$_n$/(PbZrO$_3$)$_n$ superlattices, LGA reveals $\sqrt{2} \times 3\sqrt{2} \times 1$ long-period ground-state structures characterized by a common in-plane finite-$q$ modulation $q{_\parallel} = (1/6,1/6)$ and layer-coupled sidebands. To our knowledge, this in-plane periodicity has not been reported in any related oxide perovskite superlattice studies. Altogether, LGA offers a powerful representation-guided paradigm for ground-state structure prediction and provides a practical, decoder-free route toward materials inverse design....

---

### 4. Surrogate-Gated Generation and Foundation-Model Embeddings for Bayesian Materials Design

**Authors:** Sk Md Ahnaf Akif Alvi, Jan Janssen, Danny Perez, Douglas Allaire, Raymundo Arroyave

**Published:** 2026-06-26

**Category:** cond-mat.mtrl-sci

**ID:** 2606.28578v1

**Link:** [http://arxiv.org/abs/2606.28578v1](http://arxiv.org/abs/2606.28578v1)

**Summary:** Closed-loop materials discovery iterates between proposing candidate structures and evaluating their properties, and property evaluation dominates the cost. In the generative variant, a learned prior proposes candidate crystals and a property oracle scores them; we ask whether a cheap probabilistic surrogate can triage the generator's output, and what such a surrogate must do well. Across three architecturally distinct pretrained diffusion priors (MatterGen, CrystalFlow, ADiT) and two targets (room-temperature heat capacity and bulk modulus), we insert a Gaussian process acquisition gate between structure generation and the oracle in an RL-steered generative workflow. The gate matches or exceeds ungated fine-tuning of the generative model while capping oracle calls at a fixed per-cycle budget. Budget-matched ablations isolate the mechanism. At an identical four-call budget, ranking-based selection outperforms arbitrary selection, confirming that the gain comes from the surrogate's choice; the gate comes within $\sim$9\% of exhaustive oracle spending at roughly one-fifth of the calls. A density-functional-theory check of the bulk-modulus discoveries confirms the learned oracle to within 2.5\% on average and the surrogate's ranking of the generated structures at Spearman $ρ= 0.94$. A cross-factorial benchmark of surrogate performance spanning mechanical, electronic, and vibrational properties identifies pretrained ORB embeddings with a Gaussian process as the most reliable combination, which we adopt as the building blocks of the proposed workflow. The complete pipeline is released as open-source software....

---


<!-- ARXIV_PAPERS_END -->