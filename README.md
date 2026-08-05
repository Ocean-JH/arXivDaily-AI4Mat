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

The search expression and result limit live in [`config.json`](config.json).
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
status. Review the resulting diff before committing it.

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

## New Papers (3)

*Last checked: 2026-08-06 06:56:02 (SGT)*

### 1. Physics-Informed and Knowledge-Driven Generative AI for Autonomous Discovery of Porous Oxide Energy Materials: Opportunities and Challenges

**Authors:** Dibakar Datta

**Published:** 2026-08-03

**Category:** cond-mat.mtrl-sci

**ID:** 2608.02858v1

**Link:** [https://arxiv.org/abs/2608.02858v1](https://arxiv.org/abs/2608.02858v1)

**Summary:** The discovery of next-generation energy-storage materials is increasingly limited by the complexity of the underlying design problem rather than by computational capability alone. Porous transition-metal oxides represent a particularly challenging class of battery materials because their performance emerges from coupled interactions among crystal chemistry, pore architecture, ion transport, electrochemistry, electro-chemo-mechanics, synthesis, manufacturing, and battery-system operation. Recent advances in generative artificial intelligence (AI) have demonstrated remarkable capabilities for generating chemically plausible crystal structures. However, current approaches remain largely focused on crystallographic validity and thermodynamic stability. This perspective presents a roadmap for advancing generative AI beyond crystal generation toward physics-informed, application-aware, and synthesis-aware inverse design. Using porous oxide electrodes as a representative materials platform, we propose a seven-tier physics-informed inverse-design framework integrating chemistry, thermodynamics, transport, electrochemistry, durability, cell compatibility, and manufacturability. We further identify the "Missing Data Problem" as a fundamental bottleneck limiting application-aware AI and introduce an autonomous knowledge-generation framework supported by a Porous Oxide Energy Materials Ontology and a continuously evolving "Knowledge Base". Together, these concepts establish the foundation for Synthesis-Aware, Closed-Loop Autonomous Discovery, providing a general framework for AI-enabled autonomous materials discovery across energy-storage materials and other functional materials.

---

### 2. An Autonomous Scientific Knowledge Generation Framework for AI-Driven Scientific Discovery

**Authors:** Dibakar Datta

**Published:** 2026-07-09

**Category:** cs.DL

**ID:** 2607.09806v2

**Link:** [https://arxiv.org/abs/2607.09806v2](https://arxiv.org/abs/2607.09806v2)

**Summary:** Artificial intelligence (AI) is transforming scientific discovery, but its effectiveness is fundamentally limited by the availability of structured scientific knowledge. Although existing databases have accelerated data-driven materials research, much of the knowledge needed for predictive modeling and inverse design remains embedded in unstructured scientific literature. We present an Autonomous Scientific Knowledge Generation Framework that transforms scientific publications into a Unified AI-Ready Scientific Knowledge Base. The framework integrates ontology-guided literature acquisition, hybrid scientific knowledge extraction, semantic harmonization, knowledge fusion, and validation within a unified workflow. Rather than treating literature retrieval, information extraction, and database construction as separate tasks, the framework progressively converts scientific publications into structured, semantically consistent, and provenance-preserving knowledge suitable for AI-driven reasoning. As a proof of concept, the framework was applied to electro-optic materials. Autonomous literature acquisition retrieved and validated about 1,000 publications from multiple scholarly repositories. A representative subset of eight publications was processed through the complete workflow, generating 29 structured scientific records that were harmonized into 7 canonical scientific records. The results demonstrate the complete transformation from scientific literature to an AI-ready scientific knowledge base while preserving quantitative measurements, operating conditions, provenance, and scientific context. The proposed framework provides a scalable, domain-independent foundation for predictive AI, generative AI, and closed-loop AI-driven scientific discovery.

---

### 3. Conditional grain-graph diffusion for property-guided inverse design of polycrystalline microstructures

**Authors:** Yuheng Zhou, Xiao Shang, Huicong Chen, Yu Zou

**Published:** 2026-08-01

**Category:** cond-mat.mtrl-sci

**ID:** 2608.00707v1

**Link:** [https://arxiv.org/abs/2608.00707v1](https://arxiv.org/abs/2608.00707v1)

**Summary:** Graph representations compactly encode polycrystalline microstructures while retaining grain topology and grain boundary information. We present a conditional graph diffusion framework for property-guided inverse design of dual-phase Ti-6Al-4V microstructures. An enhanced grain graph neural network (GNN) with grain boundary edge features, learnable node and edge embeddings, and multi-statistic pooling serves as a forward surrogate for stress prediction and candidate evaluation. The conditional diffusion model generates candidates through reverse diffusion under prescribed α-phase volume fraction, elastic modulus, and yield-stress proxy targets. Across four target regimes and independently seeded starting sets, generated candidates consistently approach the prescribed properties, including a target outside the property envelope of the existing microstructures. Local crystallographic consistency is evaluated post-generation from deviations from the Burgers orientation relationship (BOR). BOR-aware ranking increases mean BOR consistency by up to 44.9% and 56.4% for the in- and out-of-envelope targets, respectively, while maintaining property alignment. Finite element validation of the five best candidates in each primary design case yields a maximum absolute relative error of 1.0% in their mean properties. In a representative benchmark, diffusion requires 32 candidate evaluations per input graph, compared with approximately 40,000 for random search and evolutionary optimization, and reduces runtime by approximately two orders of magnitude in the tested implementations. These results establish conditional grain-graph diffusion as an efficient framework for property-guided polycrystalline microstructure design.

---

<!-- ARXIV_PAPERS_END -->
