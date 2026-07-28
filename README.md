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

*Last updated: 2026-07-29 06:55:33 (SGT)*

### 1. Physics-Guided Generative AI for Property-Targeted 3D Porous Media Design

**Authors:** Peng Wang

**Published:** 2026-07-27

**Category:** cs.LG

**ID:** 2607.24274v1

**Link:** [http://arxiv.org/abs/2607.24274v1](http://arxiv.org/abs/2607.24274v1)

**Summary:** Inverse design of three-dimensional porous media is central to applications in filtration, catalysis, energy storage, fuel cells, thermal management, and biomedical scaffolds, but remains challenging because many distinct pore geometries can share similar porosity or permeability while small structural changes can strongly affect transport behaviour. This paper proposes a physics-guided generative AI framework for property-targeted porous media design, combining a property-aware variational autoencoder, a conditional latent diffusion model, and an independently trained differentiable structure-to-property surrogate. The framework learns a compact, physically informative latent design space, generates porous structures conditioned on target porosity and directional permeability, and refines generated samples using property-level feedback during denoising and decoding. Experiments on procedurally generated structures and real micro-CT porous-media datasets show improved target-property matching, directional permeability control, and property correlation compared with representative property-aware variational-autoencoder and latent-diffusion baselines. The results demonstrate a scalable route towards controllable inverse design of complex porous geometries and establish a foundation for simulation-informed generative AI tools in engineering and advanced materials discovery....

---

### 2. Catalyst Diffusion Transformer: Generative Inverse Design of Heterogeneous Catalysts

**Authors:** Hayoung Doo, Dong Hyeon Mok, Seoin Back, Jonggeol Na

**Published:** 2026-07-27

**Category:** cond-mat.mtrl-sci

**ID:** 2607.24272v1

**Link:** [http://arxiv.org/abs/2607.24272v1](http://arxiv.org/abs/2607.24272v1)

**Summary:** The vast chemical design space and complex, interdependent design variables make catalyst discovery for targeted properties highly labor- and resource-intensive. Although generative models have emerged as a promising solution, existing approaches are generally limited to single-property conditioning or narrow chemical spaces. Here, we present Catalyst Diffusion Transformer (CatDiT), a unified framework for inverse catalyst design that generates valid and novel structures ranging from intermetallic alloys to oxide surfaces. By learning compressed latent representations, CatDiT enables efficient training and rapid sampling while supporting simultaneous conditioning on adsorbate type, binding energy, and catalyst class. The model provides reliable control of discrete properties and directional control of continuous properties, enriching candidate pools for reaction-specific catalyst discovery. As a representative application, multi-conditional generation for the nitrogen reduction reaction (NRR) yields 28 density functional theory (DFT)-relaxed alloy candidates that satisfy the target activity window and lie above the pure-metal *N-*H scaling line, corresponding to a ~1.5-fold enrichment over the source distribution. These results establish CatDiT as a practical and scalable approach for property-directed catalyst inverse design and targeted catalyst generation....

---

### 3. Stoichiometric cluster learning for few-shot property prediction of multi-ionic integrated energetic materials

**Authors:** Ming-Yu Guo, Wei-Jia Zou, Yu Shang, Wei-Xiong Zhang

**Published:** 2026-07-25

**Category:** cond-mat.mtrl-sci

**ID:** 2607.23208v1

**Link:** [http://arxiv.org/abs/2607.23208v1](http://arxiv.org/abs/2607.23208v1)

**Summary:** Multi-ionic materials pose a distinct representational challenge in machine learning-driven materials design. Different from single-molecule or composition-based materials, their properties arise from how charged building blocks aggregate into specific assemblies. Here, we show how pretrained machine-learned interatomic potentials (MLIPs) can bypass full crystal-structure prediction and support pre-synthesis screening from stoichiometric ionic clusters using multi-ionic integrated explosives (MIXs) as a synthesis-facing example. This strategy combines a stoichiometric ionic-cluster representation, which represents each candidate material by a non-periodic, stoichiometry-preserved formula-unit cluster, with multi-task fine-tuning (MT-FT), which adapts a pretrained atomistic backbone while retaining the energy--force objective as physical regularization for the sparse detonation-velocity labels. With the pretrained backbone regularized by MT-FT, this surrogate provides a cross-validated screen across only 25 structurally curated perovskite-type energetic materials (PEMs) with experimentally derived Kamlet--Jacobs (K--J) detonation velocities. Representation probes show that the learned descriptors implicitly retain site-aware ionic organization, density information, and coarse packing compatibility, implying why non-periodic clusters can remain predictive before full crystal structures are known. The surrogate extends known PEMs chemistry to three newly synthesized ABX$_4$ materials with both unseen ABX$_4$ stoichiometry and an unseen ethylenediammonium B-site cation, yielding three-point concordance with K--J reference velocities and a mean absolute error (MAE) of 92~m$\cdot$s$^{-1}$ without retraining. Together, these results establish stoichiometry-preserved cluster learning as a synthesis-facing screening strategy for data-scarce multi-ionic materials....

---


<!-- ARXIV_PAPERS_END -->