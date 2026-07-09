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

*Last updated: 2026-07-10 07:09:17 (SGT)*

### 1. Neural Operator-enabled Topology-informed Evolutionary Strategy for PDE-Constrained Optimization

**Authors:** Xiangming Huang, Guannan Zhang, Lu Lu, Raphaël Pestourie

**Published:** 2026-07-08

**Category:** cs.LG

**ID:** 2607.07682v1

**Link:** [http://arxiv.org/abs/2607.07682v1](http://arxiv.org/abs/2607.07682v1)

**Summary:** The inverse design of physical systems governed by partial differential equations is computationally demanding due to the high dimensionality and non-convexity of design spaces. Generative models for inverse design often lack robustness and transferability, whereas evolutionary strategies are robust but struggle in high-dimensional spaces. This paper introduces a Neural Operator-enabled Topology-informed Evolutionary Strategy (NOTES) that integrates dimensionality reduction, representation learning, and evolutionary optimization for efficient and transferable inverse design. NOTES couples a DeepONet-based neural operator with the Covariance Matrix Adaptation Evolution Strategy (CMA-ES) to perform global optimization in a compact latent space that encodes topology-aware priors while discovering high-performance designs for unseen operating conditions. Applied to nanophotonic beam-deflector inverse design governed by Maxwell's equations, NOTES reduces the design dimensionality from 256 to 25 and consistently achieves over 95 percent efficiency, outperforming CMA-ES, topology optimization, and other baselines. Applied to structural optimization, NOTES discovers designs that achieve compliance down to 246. By decoupling topology learning of a DeepONet from the governing physics in a PDE solver, NOTES provides a flexible and transferable framework for the inverse design of physical systems....

---

### 2. Human and LLM Collaboration for Accelerated Materials Synthesis and Discovery

**Authors:** Gregory Bassen, Wyatt Bunstine, Sarah Okandey, Sarah Cheung, Elaine Flowers, Ritwik Bose, Joshua Hummel, Christopher D. Stiles, Maxime A. Siegler, Tyrel M. McQueen

**Published:** 2026-07-08

**Category:** cond-mat.mtrl-sci

**ID:** 2607.07604v1

**Link:** [http://arxiv.org/abs/2607.07604v1](http://arxiv.org/abs/2607.07604v1)

**Summary:** Although Large Language Models (LLM) and Artificial Intelligence (AI) tools have enabled a rapid increase in the generation rate of predicted materials, the rate of new materials discovery has lagged behind. This is due to the challenges associated with designing a sequence of chemical reactions to predictably produce new materials, especially in new structure types. Here, we report a study of human and LLM generated recipes for the synthesis of known and new materials. The success of the recipes is determined through in-lab experimentation, and the results are passed back to the humans and LLMs in a closed-loop process to study the effects of their collaboration. The Ruddlesden-Popper homologous series was selected for all material candidates to provide a materials phase space that is simultaneously well studied and likely to host undiscovered materials. We find that humans (H) and LLM (L) have similar success rates: 83(8)% (H) and 75(9)% (L) [known materials, round one], 17(9)% (H) and 22(10)% (L) [unknown materials, round one], 79(8)% (H) and 71(9)% (L) [known materials, round two], and 22(7)% (H) and 14(6)% (L) [unknown materials, round two]. Through this collaborative human-LLM effort, we discovered Ba3PtO5, a material with a new structural prototype that constitutes the missing 1D member of the herein reported dimensionally tunable Rock-Salt Perovskite (RSP) homologous series of the form (AX)m(ABX3)p, of which the Ruddlesden-Popper series is a subset....

---

### 3. Bayesian Optimization of Genetic Algorithm Hyperparameters in a Multi-Fidelity Framework for Efficient Lattice Material Design

**Authors:** Sergei Zorkaltsev, Maciej Haranczyk, Christina Schenk

**Published:** 2026-07-08

**Category:** cond-mat.mtrl-sci

**ID:** 2607.07289v1

**Link:** [http://arxiv.org/abs/2607.07289v1](http://arxiv.org/abs/2607.07289v1)

**Summary:** This study presents a multi-fidelity framework for the systematic optimization of genetic algorithm (GA) hyperparameters. The framework integrates three fidelity levels: high-fidelity Fast Fourier Transform (FFT) homogenization for validation, a medium-fidelity 3D convolutional neural network surrogate for rapid property evaluation, and a low-fidelity Gaussian process (GP) surrogate within a Bayesian optimization (BO) framework to guide the hyperparameter search. Various acquisition functions are evaluated, with logNEI achieving the best performance by effectively accounting for the noise inherent in GA evaluations. The proposed framework identifies hyperparameter configurations that enable a 25-generation GA run to achieve elastic modulus values comparable to those obtained in a full 75-generation optimization. Furthermore, introducing a penalized BO objective significantly reduces the number of required lattices with only minor decreases in absolute achieved elastic modulus, revealing a practical trade-off between performance and the number of structures that must be evaluated. High-fidelity FFT validation verifies the effectiveness of the surrogate-driven optimization strategy. The optimized hyperparameters allow for rapid convergence, eliminate the need for lattice mutation, and reduce the overall computational cost by 24% (from 225 to 171 hours) while preserving mechanical performance. These results demonstrate the potential of multi-fidelity optimization as an efficient and practical approach for GA hyperparameter tuning and future experimental lattice design studies....

---


<!-- ARXIV_PAPERS_END -->