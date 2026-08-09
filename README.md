# ArXiv Daily — AI for Materials Science

ArXiv Daily is a focused, automatically updated index of research at the
intersection of artificial intelligence and materials science.

[Browse the live site](https://ocean-jh.github.io/arXivDaily-AI4Mat/) ·
[Search the archive](https://ocean-jh.github.io/arXivDaily-AI4Mat/archive.html)

## What it tracks

- Machine learning for materials discovery and inverse design
- Crystal structure prediction
- Generative models for materials
- Related computational materials science research

The search expression, result limit, and arXiv request pacing live in
[`config.json`](config.json). The default client requests 100 records per page,
waits 10 seconds between requests, and retries transient failures five times.
See the
[arXiv API query documentation](https://info.arxiv.org/help/api/user-manual.html#51-details-of-query-construction)
before adapting the query for another topic.

## Local setup

Python 3.13 is used in automation.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install --requirement requirements.txt
python -m pip install --requirement requirements-dev.txt
npm install --ignore-scripts --no-package-lock
```

Run the tracker from the repository root:

```bash
python arxiv_tracker.py
```

The command contacts arXiv, updates the local paper state, and regenerates the
README, home page, archive pages, search index, feed, sitemap, and deployment
status. If arXiv remains unavailable with a rate-limit or server error after
the configured retries, an existing installation rebuilds from its latest
saved results so a temporary upstream outage does not block deployment. Review
the resulting diff before committing it.

## Architecture

- `arxiv_tracker.py` handles arXiv ingestion, version-aware deduplication, and
  durable state updates.
- `site_renderer.py` renders the paginated site, search data, feeds, sitemap,
  and health metadata from normalized paper records.
- `templates/` and `static/` contain the source HTML, CSS, JavaScript, and image
  assets.
- `data/known_papers.json` and `data/results/` are the durable ingestion state.
- `data/archive-search-index.json` is the compact public search index.
- `index.html`, `archive.html`, `archive/page-*.html`, `feed.xml`,
  `sitemap.xml`, and `site-status.json` are generated outputs.
- `scripts/prepare_site_artifact.py` validates generated HTML and assembles a
  strict allowlist of files for GitHub Pages.

The Pages artifact intentionally excludes Python source, templates, tests,
configuration, and ingestion-state files.

## Tests and validation

Run the same checks used by CI:

```bash
python -m pytest
python -m compileall -q arxiv_tracker.py site_renderer.py scripts tests
python -m ruff check .
python scripts/prepare_site_artifact.py check
for script in static/js/*.js; do node --check "$script"; done
npm run test:frontend
```

Pull requests and pushes to `main` run these checks without write permissions.

## Updates and deployment

The daily workflow runs at 06:00 Singapore time, on pushes to `main`, and when
manually dispatched. It tests the project before generation, commits generated
changes with the GitHub Actions bot, packages only public files, and deploys
them through the protected `github-pages` environment. A final smoke check
compares the deployed `site-status.json` timestamp with the artifact from the
same run, so a stale deployment fails visibly.

The deployment requires **GitHub Actions** under **Settings → Pages → Source**.
The workflow rejects every other publishing source before generation begins.
It uses the repository-provided token and requires no personal access token or
deployment secret.

## Contributing

Issues and pull requests for query improvements, UI refinements, and pipeline
hardening are welcome. Please run the test and validation commands above before
opening a pull request.

## Acknowledgements

Paper metadata is provided by [arXiv](https://arxiv.org/). Please respect
arXiv's API access and attribution requirements.

---

## Latest generated paper list


<!-- ARXIV_PAPERS_START -->

## Latest Papers (9)

_No new papers were found in the latest check; showing the most recent additions._

*Last checked: 2026-08-10 06:27:57 (SGT)*

### 1. ASE2SPRKKR: a unified Python framework integrating the Spin-Polarized Relativistic Korringa-Kohn-Rostoker method into the Atomic Simulation Environment

**Authors:** Ridha Eddhib, Matyáš Novák, Hubert Ebert, Aki Pulkkinen, Ján Minár

**Published:** 2026-08-06

**Category:** cond-mat.mtrl-sci

**ID:** 2608.05957v1

**Link:** [https://arxiv.org/abs/2608.05957v1](https://arxiv.org/abs/2608.05957v1)

**Summary:** The Spin-Polarized Relativistic Korringa-Kohn-Rostoker (SPR-KKR) is an all-electron ab-initio multiple-scattering code that provides unique capabilities for treating chemical disorder, finite-temperature magnetism, relativistic effects, and spectroscopic properties of various types of solids through its fundamental formulation in terms of the single-particle Green's function rather than eigenstates. We present ASE2SPRKKR, a comprehensive Python interface that integrates SPR-KKR into the Atomic Simulation Environment (ASE), making SPR-KKR more accessible, streamlined, and uniform. Our implementation extends the ASE's Atoms object to handle fractional site occupations for coherent-potential-approximation calculations while maintaining full compatibility with ASE's extensive ecosystem of structure builders, optimizers, and analysis tools. Automated input generation with validation, comprehensive output parsing, and direct MPI support enable seamless integration into high-throughput and multi-method workflows. We demonstrate the interface through representative applications: semi-infinite surface calculations reproducing Rashba-split Au(111) surface states; one-step photoemission modeling capturing matrix-element effects; exchange-parameter extraction for atomistic spin dynamics; and X-ray absorption spectroscopy including magnetic circular dichroism. Beyond these demonstrations, ASE2SPRKKR is designed with transferability as a first-class concern. By grounding its architecture in FAIR principles of Findability, Accessibility, Interoperability, and Reusability, it establishes a replicable blueprint for bringing other specialized Green's function and first-principles codes into the collaborative, reproducible workflows that modern materials discovery requires.

---

### 2. Domain-Gated Latent Diffusion: Generative Inverse Design of HMX-Class Energetic Materials with First-Principles Validation

**Authors:** Yehudit Aperstein, Alexander Apartsin

**Published:** 2026-05-26

**Category:** physics.chem-ph

**ID:** 2605.26540v2

**Link:** [https://arxiv.org/abs/2605.26540v2](https://arxiv.org/abs/2605.26540v2)

**Summary:** Energetic materials power mining, demolition, propulsion and airbags, yet today's compounds were designed decades ago. A successor must combine high energy release, low sensitivity to accidental initiation and a practical synthesis route, found within an astronomically large molecular space. Generative models are the natural search tool, but their training data are mostly untrustworthy: of approximately 66,000 molecules with recorded properties, only approximately 3,000 were measured or computed from first principles. Models trained on all of them imitate the rough estimates and propose molecules that collapse under real physics. We introduce Domain-Gated Latent Diffusion (DGLD), a diffusion model that treats data reliability as an explicit design parameter: labels are sorted into four trust tiers, and only trustworthy ones steer generation, while the unreliable majority still teaches the model what a plausible molecule looks like. Learned controls tune performance, safety and viability independently, and every proposal passes a four-stage screen ending in a quantum-chemical DFT audit. DGLD proposes 10 molecules unknown to PubChem that survive this screen. The best, 3,4,5-trinitro-1,2-isoxazole, matches the benchmark explosives HMX and PETN in calculated detonation performance, is unlike molecules in its training set, and has a four-step synthesis route. Trust gating is chemistry-independent and can be applied wherever abundant weak data surround a reliable core.

---

### 3. Physics-Informed and Knowledge-Driven Generative AI for Autonomous Discovery of Porous Oxide Energy Materials: Opportunities and Challenges

**Authors:** Dibakar Datta

**Published:** 2026-08-03

**Category:** cond-mat.mtrl-sci

**ID:** 2608.02858v1

**Link:** [https://arxiv.org/abs/2608.02858v1](https://arxiv.org/abs/2608.02858v1)

**Summary:** The discovery of next-generation energy-storage materials is increasingly limited by the complexity of the underlying design problem rather than by computational capability alone. Porous transition-metal oxides represent a particularly challenging class of battery materials because their performance emerges from coupled interactions among crystal chemistry, pore architecture, ion transport, electrochemistry, electro-chemo-mechanics, synthesis, manufacturing, and battery-system operation. Recent advances in generative artificial intelligence (AI) have demonstrated remarkable capabilities for generating chemically plausible crystal structures. However, current approaches remain largely focused on crystallographic validity and thermodynamic stability. This perspective presents a roadmap for advancing generative AI beyond crystal generation toward physics-informed, application-aware, and synthesis-aware inverse design. Using porous oxide electrodes as a representative materials platform, we propose a seven-tier physics-informed inverse-design framework integrating chemistry, thermodynamics, transport, electrochemistry, durability, cell compatibility, and manufacturability. We further identify the "Missing Data Problem" as a fundamental bottleneck limiting application-aware AI and introduce an autonomous knowledge-generation framework supported by a Porous Oxide Energy Materials Ontology and a continuously evolving "Knowledge Base". Together, these concepts establish the foundation for Synthesis-Aware, Closed-Loop Autonomous Discovery, providing a general framework for AI-enabled autonomous materials discovery across energy-storage materials and other functional materials.

---

### 4. An Autonomous Scientific Knowledge Generation Framework for AI-Driven Scientific Discovery

**Authors:** Dibakar Datta

**Published:** 2026-07-09

**Category:** cs.DL

**ID:** 2607.09806v2

**Link:** [https://arxiv.org/abs/2607.09806v2](https://arxiv.org/abs/2607.09806v2)

**Summary:** Artificial intelligence (AI) is transforming scientific discovery, but its effectiveness is fundamentally limited by the availability of structured scientific knowledge. Although existing databases have accelerated data-driven materials research, much of the knowledge needed for predictive modeling and inverse design remains embedded in unstructured scientific literature. We present an Autonomous Scientific Knowledge Generation Framework that transforms scientific publications into a Unified AI-Ready Scientific Knowledge Base. The framework integrates ontology-guided literature acquisition, hybrid scientific knowledge extraction, semantic harmonization, knowledge fusion, and validation within a unified workflow. Rather than treating literature retrieval, information extraction, and database construction as separate tasks, the framework progressively converts scientific publications into structured, semantically consistent, and provenance-preserving knowledge suitable for AI-driven reasoning. As a proof of concept, the framework was applied to electro-optic materials. Autonomous literature acquisition retrieved and validated about 1,000 publications from multiple scholarly repositories. A representative subset of eight publications was processed through the complete workflow, generating 29 structured scientific records that were harmonized into 7 canonical scientific records. The results demonstrate the complete transformation from scientific literature to an AI-ready scientific knowledge base while preserving quantitative measurements, operating conditions, provenance, and scientific context. The proposed framework provides a scalable, domain-independent foundation for predictive AI, generative AI, and closed-loop AI-driven scientific discovery.

---

### 5. Conditional grain-graph diffusion for property-guided inverse design of polycrystalline microstructures

**Authors:** Yuheng Zhou, Xiao Shang, Huicong Chen, Yu Zou

**Published:** 2026-08-01

**Category:** cond-mat.mtrl-sci

**ID:** 2608.00707v1

**Link:** [https://arxiv.org/abs/2608.00707v1](https://arxiv.org/abs/2608.00707v1)

**Summary:** Graph representations compactly encode polycrystalline microstructures while retaining grain topology and grain boundary information. We present a conditional graph diffusion framework for property-guided inverse design of dual-phase Ti-6Al-4V microstructures. An enhanced grain graph neural network (GNN) with grain boundary edge features, learnable node and edge embeddings, and multi-statistic pooling serves as a forward surrogate for stress prediction and candidate evaluation. The conditional diffusion model generates candidates through reverse diffusion under prescribed α-phase volume fraction, elastic modulus, and yield-stress proxy targets. Across four target regimes and independently seeded starting sets, generated candidates consistently approach the prescribed properties, including a target outside the property envelope of the existing microstructures. Local crystallographic consistency is evaluated post-generation from deviations from the Burgers orientation relationship (BOR). BOR-aware ranking increases mean BOR consistency by up to 44.9% and 56.4% for the in- and out-of-envelope targets, respectively, while maintaining property alignment. Finite element validation of the five best candidates in each primary design case yields a maximum absolute relative error of 1.0% in their mean properties. In a representative benchmark, diffusion requires 32 candidate evaluations per input graph, compared with approximately 40,000 for random search and evolutionary optimization, and reduces runtime by approximately two orders of magnitude in the tested implementations. These results establish conditional grain-graph diffusion as an efficient framework for property-guided polycrystalline microstructure design.

---

### 6. Machine Learning for Designing Undesignable Metal-Organic Frameworks

**Authors:** Satya Kokonda

**Published:** 2026-07-29

**Category:** cond-mat.mtrl-sci

**ID:** 2607.27368v1

**Link:** [https://arxiv.org/abs/2607.27368v1](https://arxiv.org/abs/2607.27368v1)

**Summary:** Many crucial processes are too complex for computational modeling, requiring experimentation to identify promising materials. Here, a methodology for material design is presented, while photocatalysis is presented as a specific case-study. Metal-Organic Frameworks (MOFs) are a subset of highly promising porous nanomaterials, used in a variety of unmodellable applications. Reinforcement learning generated 60,000 novel MOFs optimized for CO/H20 selectivity. A predictor funnel system was created, iteratively removing low-scoring MOFs to 10,986 potential candidates, improving computational efficiency by 276%. While trained Crystal Graph Convolutional Neural Network (CGCNN) models predicted features for creating a fitness function incorporating stability, catalytic ability, material cost, sustainability, and adsorption while allowing the inclusion of application specific design criterion. This designed function provides a computational method to model photocatalytic performance- and filtered down to two promising MOFs which each pass a myriad of synthesis criteria, first a Cr-based MOF with photocatalyst score 230% higher than the control. Second, a Zn-based MOF outperforms the best control across all relevant metrics, demonstrating robustness against variable fitness functions. This work designed 20 materials, each 125% better than the control for this application. Furthermore, analysis revealed insightful design patterns, such as the significant influence of metal cluster N262 on catalytic performance, providing a method for future work to narrow the chemical space. By incorporating industrially applicable features such as cost or stability of the material, this work successfully designs industrially promising materials in otherwise unmodellable processes such as drug delivery, while paving a method for multi-objective optimization incorporating 260% more features than prior work.

---

### 7. Instability-induced bistable shape-morphing kirigami structures

**Authors:** Xiaoyuan Ying, Marcelo A. Dias

**Published:** 2026-07-29

**Category:** cond-mat.soft

**ID:** 2607.26941v1

**Link:** [https://arxiv.org/abs/2607.26941v1](https://arxiv.org/abs/2607.26941v1)

**Summary:** Deployable shape-morphing structures that transform from flat sheets into stable three-dimensional configurations are highly desirable for applications ranging from soft robotics and biomedical devices to adaptive architecture and aerospace systems. Existing kirigami-based morphing systems primarily rely on isotropic deployment, compliant soft materials, or external constraints to maintain deployed shapes, which limits geometric programmability, structural integrity, and applicability in rigid-material systems. Here, we present an inverse design framework for anisotropic bistable kirigami structures that enables programmable shape morphing through controlled geometric frustration and instability-induced deployment. The framework combines a semi-analytical mechanical model with geometry to establish a direct connection between geometric transformation and the underlying energy landscape. We show that instability-induced shape morphing leads to tunable bistability and directional deployment in anisotropic kirigami structures. The results are validated through finite element simulations and experiments, demonstrating stable deployed configurations and programmable anisotropic morphing. The proposed framework further provides a general design strategy that can be integrated with various active actuation systems, enabling broader engineering applications.

---

### 8. Thermodynamics-Informed Machine Learning for Energy Materials Discovery

**Authors:** Pol Benítez, Cibrán López, Claudio Cazorla

**Published:** 2026-07-28

**Category:** cond-mat.mtrl-sci

**ID:** 2607.26296v1

**Link:** [https://arxiv.org/abs/2607.26296v1](https://arxiv.org/abs/2607.26296v1)

**Summary:** Machine learning (ML) is transforming materials discovery by enabling rapid prediction of properties that previously required computationally expensive first-principles calculations. Yet most current ML models remain fundamentally limited to zero-temperature descriptions, learning static lattice energies while neglecting the thermodynamic effects that govern materials behaviour at finite temperature. Because phase stability, functional response, and performance are governed by free-energy landscapes rather than static energies alone, this limitation represents a major barrier to predictive materials design under realistic operating conditions. In this Perspective, we argue that developing thermodynamics-informed ML constitutes one of the most important and least explored frontiers in materials discovery. We examine the fundamental shortcomings of energy-based models, highlighting the essential roles of entropy and anharmonicity in determining free energies and materials functionality. We review emerging strategies, including machine-learned interatomic potentials and hybrid ML-statistical mechanics frameworks, while identifying key challenges related to data availability, transferability, and thermodynamic consistency. Building on these advances, we outline a roadmap for thermodynamics-informed ML centred on direct free-energy learning, entropy-aware representations, and adaptive sampling across temperature. We highlight the transformative opportunities this paradigm offers for energy materials and argue that the next generation of ML models must move beyond static energy predictions towards a thermodynamic description of materials behaviour under realistic operating conditions.

---

### 9. SeqGPT: A Constrained Transformer Agent for the Inverse Design of Multi-Panel Composite Structures

**Authors:** Driss Chraibi, Alejandro García Pis, Stéphane Grihon, Sixin Zhang

**Published:** 2026-07-03

**Category:** cs.NE

**ID:** 2607.11910v1

**Link:** [https://arxiv.org/abs/2607.11910v1](https://arxiv.org/abs/2607.11910v1)

**Summary:** Optimizing composite stacking sequences to match continuous targets (e.g., Lamination or Buckling Parameters) with discrete manufacturing constraints represents a challenging combinatorial inverse problem that regularly occurs in composite design especially when numerical optimization approaches are used (bi-step, bi-level configurations). In multipanel configurations, this complexity is further intensified by blending, a global compatibility/continuity requirement between the different panel stackings. This study presents SeqGPT, a conditional Transformer agent developed to replace computationally expensive iterative methods. To ensure both global continuity and manufacturing feasibility by construction, we implemented a hybrid neurosymbolic decoding strategy. SeqGPT predicts a conditional distribution that guides a Constrained Beam Search, where any branch violating blending rules is strictly pruned. Numerical experiments on the 18-panel horseshoe benchmark demonstrate that SeqGPT generates solutions near-instantaneously with buckling performance comparable to evolutionary methods, offering a significant speed-up compared to the state of the art.

---

<!-- ARXIV_PAPERS_END -->
