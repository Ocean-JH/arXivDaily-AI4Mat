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

## New Papers (2)

*Last updated: 2026-06-06 07:06:29 (SGT)*

### 1. Inverse Design of Amorphous Materials with Targeted Properties

**Authors:** Jonas A. Finkler, Yan Lin, Tao Du, Jilin Hu, Morten M. Smedskjaer

**Published:** 2025-09-17

**Category:** cond-mat.mtrl-sci

**ID:** 2509.13916v2

**Link:** [http://arxiv.org/abs/2509.13916v2](http://arxiv.org/abs/2509.13916v2)

**Summary:** Disordered (amorphous) materials, such as glasses, are emerging as promising candidates for applications within energy storage, nonlinear optics, and catalysis. Their lack of long-range order and complex short- and medium-range orderings, which depend on composition as well as thermal and pressure history, offer a vast materials design space. To this end, relying on machine learning methods instead of trial and error is promising, and among these, inverse design has emerged as a tool for generating materials with desired properties. Although inverse design methods based on diffusion models have shown success for crystalline materials and molecules, similar methods targeting amorphous materials remain less developed, mainly because of the limited availability of large-scale datasets and the requirement for larger simulation cells. In this work, we propose and validate an inverse design method for amorphous materials, introducing AMDEN (Amorphous Material DEnoising Network), a diffusion model-based framework that generates structures of amorphous materials. These low-energy configurations are typically obtained through a thermal motion-driven random search-like process that cannot be replicated by standard denoising procedures. We therefore introduce an energy-based AMDEN variant that implements Hamiltonian Monte Carlo refinement for generating these relaxed structures. We further introduce several amorphous material datasets with diverse properties and compositions to evaluate our framework and support future development....

---

### 2. Inverse Critical Experiment Design via Gradient Optimization and a Multigroup Attention-Based Neural Network Architecture

**Authors:** Will Savage, Logan Burnett, Dean Price

**Published:** 2026-06-01

**Category:** cs.LG

**ID:** 2606.04033v1

**Link:** [http://arxiv.org/abs/2606.04033v1](http://arxiv.org/abs/2606.04033v1)

**Summary:** The validation of advanced nuclear reactor designs and fuel concepts requires critical experiments with high neutronic similarity to the target technology. Neutronic similarity is quantified by the correlation coefficient $c_k$, which captures the shared bias in $k_\text{eff}$ induced by uncertainties in nuclear data. Generally, a $c_k\geq0.9$ is needed for an experiment to be sufficiently similar to a target technology. This work presents a methodology for the inverse design of critical experiments. Deep neural network surrogate modeling and nonparametric gradient optimization are used to generate experiment geometries that maximize $c_k$.
  A deep neural network is trained on OpenMC-calculated sensitivity vectors for grid-based critical experiment geometries. The model architecture combines a U-Net convolutional encoder-decoder with a novel multigroup attention pooling layer, introduced to capture the differing spatial dependencies of sensitivities. Multigroup attention pooling is shown to achieve better performance than traditional pooling, as well as interpretable internal behavior. The differentiability of the surrogate enables gradient-based optimization of the full combinatorial design space, allowing $c_k$ to be maximized by directly changing the material assignment of each position in the geometry grid.
  The method is applied to the validation of the TN-Americas TN-LC transportation cask with HALEU fuel, for which existing critical experiment coverage is limited. The optimization procedure is shown to produce experiment geometries achieving $c_k$ scores of 0.97757, 0.81324, and 0.93276 for three configurations of interest. This approach demonstrates the potential of deep learning and gradient optimization to accelerate the development of advanced nuclear technology....

---


<!-- ARXIV_PAPERS_END -->