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

*Last updated: 2026-05-19 06:59:31 (SGT)*

### 1. ColPackAgent: Agent-Skill-Guided Hard-Particle Monte Carlo Workflows for Colloidal Packing

**Authors:** Lijie Ding, Changwoo Do

**Published:** 2026-05-15

**Category:** cs.AI

**ID:** 2605.15625v1

**Link:** [http://arxiv.org/abs/2605.15625v1](http://arxiv.org/abs/2605.15625v1)

**Summary:** We introduce ColPackAgent, an agent framework that autonomously runs Monte Carlo simulations of colloidal packing through a Model Context Protocol (MCP) tool server and an agent skill, whether as a standalone agent or inside an existing agent system. By harnessing the MCP server and agent skill, ColPackAgent executes a structured workflow for colloidal packing simulations, which are central to studies of phase behavior, self-assembly, and materials design. Without dedicated simulation tools and workflow instructions, general-purpose Large Language Model (LLM) agents tend to describe such workflows rather than execute them reliably. The MCP server exposes a custom-built colpack Python package that wraps HOOMD-blue hard-particle Monte Carlo, and the skill encodes a four-stage workflow contract. ColPackAgent can carry out the workflow interactively with human feedback, autonomously from an end-to-end prompt, or as autoresearch following a provided program file. We demonstrate the system in different modes with several colloidal packing simulation examples such as cube particles in 3D, a binary system of disks and capsules in 2D, and the 2D hard-disk freezing transition using autoresearch. We also compare model performance on this workflow across a panel of LLMs with 17 stage-specific prompts. This benchmark provides a stage-level check of how reliably different models follow the setup, planning, and analysis workflow. Together, these results show that pairing a domain Python package with MCP tools and a portable agent skill provides a practical route for turning a simulation toolkit into an agent-assisted research workflow....

---

### 2. Unified Simulation of Lagrangian Particle Dynamics via Transformer

**Authors:** Caoliwen Wang, Minghao Guo, Siyuan Chen, Heng Zhang, Mengdi Wang, Xingyu Ni, Hanson Sun, Kunyi Wang, Zherong Pan, Kui Wu, Lingjie Liu, Yin Yang, Chenfanfu Jiang, Taku Komura, Wojciech Matusik, Peter Yichen Chen

**Published:** 2026-05-14

**Category:** cs.GR

**ID:** 2605.15305v1

**Link:** [http://arxiv.org/abs/2605.15305v1](http://arxiv.org/abs/2605.15305v1)

**Summary:** A unified simulator that can model diverse physical phenomena without solver-specific redesign is a long-standing goal across simulation science. We present a learning-based particle simulator built on a single transformer architecture to model cloth, elastic solds, Newtonian and non-Newtonian fluids, granular materials, and molecular dynamics. Our model follows a prediction-correction design on a shared Lagrangian particle representation. An explicit predictor first advances particles under the known external forces, producing an intermediate state that captures externally driven motion but not inter-particle interactions. A learned corrector then predicts the residual position and velocity updates through three stages: a particle tokenizer that encodes local particle-particle, particle-boundary, and topology-guided interactions; a super-token encoder that hierarchically merges particle tokens into a compact set of super tokens via alternating self-attention and token merging; and a super-token decoder that lifts these super tokens back to particle resolution through cross-attention to predict per-particle position and velocity corrections. Progressive token merging reduces the attention cost at successive encoder layers by halving the token count at each level, and the decoder communicates through the compact super-token set rather than full particle-to-particle attention. Across the six dynamics categories, the same architecture generalizes to unseen materials, boundary configurations, initial conditions, and external forces. We further demonstrate downstream interactive control, inverse design, and learning from real-world manipulation data, reducing the need for per-phenomenon solver engineering....

---


<!-- ARXIV_PAPERS_END -->