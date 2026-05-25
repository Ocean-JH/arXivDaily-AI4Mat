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

## New Papers (1)

*Last updated: 2026-05-26 06:59:07 (SGT)*

### 1. MatClaw: An Autonomous Code-First LLM Agent for End-to-End Materials Exploration

**Authors:** Chenmu Zhang, Boris I. Yakobson

**Published:** 2026-04-03

**Category:** cond-mat.mtrl-sci

**ID:** 2604.02688v3

**Link:** [http://arxiv.org/abs/2604.02688v3](http://arxiv.org/abs/2604.02688v3)

**Summary:** Existing LLM agents for computational materials science are constrained by pipeline-bounded architectures tied to specific simulation codes and by dependence on manually written tool functions that grow with task scope. We present MatClaw, a code-first agent that writes and executes Python directly, composing any installed domain library to orchestrate multi-code workflows on remote HPC clusters without predefined tool functions. To sustain coherent execution across multi-day workflows, MatClaw uses a four-layer memory architecture that prevents progressive context loss, and retrieval-augmented generation over domain source code that raises per-step API-call accuracy to ${\sim}$99 %. Three end-to-end demonstrations on ferroelectric CuInP2S6 (machine-learning force field training via active learning, Curie temperature prediction, and heuristic parameter-space search) reveal that the agent handles code generation reliably but struggles with tacit domain knowledge. The missing knowledge, such as appropriate simulation timescales, equilibration protocols, and sampling strategies, is the kind that researchers accumulate through experience but rarely formalize. Two lightweight interventions, literature self-learning and expert-specified constraints, bridge these gaps, defining a guided autonomy model in which the researcher provides high-level domain knowledge while the agent handles workflow execution. Our results demonstrate that the gap between guided and fully autonomous computational materials research is narrower than ever before: LLMs already handle code generation and scientific interpretation reliably, and the rapid improvement in their capabilities will accelerate materials discovery beyond what manual workflows can achieve. All code and benchmarks are open-source....

---


<!-- ARXIV_PAPERS_END -->