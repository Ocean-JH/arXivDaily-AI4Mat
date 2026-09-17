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

## Latest Papers (3)

_No new papers were found in the latest check; showing the most recent additions._

*Last checked: 2026-09-17 08:04:48 (SGT)*

### 1. Multi4D: an end-to-end neural network for structural determination at complex material interfaces

**Authors:** Haoran Zhang, Zian Mao, Shufen Chu, Xiaoya He, Yuyan Guan, Antong Yang, Mingze Li, Xiaoqin Zeng, Yujun Xie

**Published:** 2026-09-13

**Category:** cond-mat.mtrl-sci

**ID:** 2609.14348v1

**Link:** [https://arxiv.org/abs/2609.14348v1](https://arxiv.org/abs/2609.14348v1)

**Summary:** Heterogeneous interfaces dictate the performance and degradation of functional materials, making it essential to link local structural variations with macroscopic failure mechanisms to guide future materials design. Yet structural heterogeneity, phase overlap, and local disorder produce highly convoluted diffraction signatures, making extended transition regions difficult to interpret at atomic resolution across large fields of view. Here, we introduce Multi4D, a physics-informed neural network framework for automated multi-component crystallographic identification using four-dimensional scanning transmission electron microscopy (4D-STEM). By combining a latent-space Diffusion Transformer for physics-constrained style translation with a rotation-invariant convolutional neural network for orientation-agnostic classification, this approach translates multi-components diffraction datasets into deterministic crystallographic maps with 98.82% accuracy. In addition, we introduce Diffraction-Inferred Structural Complexity as an information-theoretic entropy metric derived from classifier predictive uncertainty that quantifies local structural ambiguity. We apply Multi4D to generate high-fidelity structural maps of complex superconducting heterostructures, corroded alloy surfaces, and degraded solid-state battery interfaces down to single-nanometer spatial resolution. This framework establishes a statistically robust analytical paradigm for automated microscopy, facilitating both industrial quality control and the data-driven discovery of interfacial design principles.

---

### 2. Symmetry- and Property-Aware Crystal Generation with Reinforcement Learning for Inverse Materials Design

**Authors:** Ting-Wei Hsu, Arun Bansil, Qimin Yan

**Published:** 2026-09-11

**Category:** cond-mat.mtrl-sci

**ID:** 2609.13468v1

**Link:** [https://arxiv.org/abs/2609.13468v1](https://arxiv.org/abs/2609.13468v1)

**Summary:** The inverse design of crystalline materials ultimately seeks structures with desired physical properties. However, for many functional responses, a favorable numerical value is meaningful only when supported by the symmetry of the underlying crystal. Without the appropriate crystallographic constraints, an apparent response may be ill defined, accidental, or not symmetry protected. Here we introduce SPARC, a symmetry- and property-aware reinforcement learning framework that optimizes physical objectives while preserving the structural conditions required for their realization. We demonstrate SPARC on two complementary tasks. The first targets strong uniaxial dielectric anisotropy, a tensorial response that is well defined only within appropriate crystal classes. The second maximizes the spectroscopic limited maximum efficiency, a scalar device-level objective without a prescribed symmetry class, allowing the framework to identify favorable crystallographic motifs. These results show that symmetry is not merely an additional design constraint, but a physical foundation for generating candidates with meaningful, robust, and realizable functional properties.

---

### 3. Remote epitaxial frustration stabilizes a correlated interfacial state

**Authors:** Taehwan Jung, Nicholas Hagopian, Anshu Sirohi, Quinn Campbell, Chengye Dong, Zachary T. LaDuca, Tamalika Samanta, Joshua Robinson, Paul M. Voyles, Jason K. Kawasaki

**Published:** 2025-12-07

**Category:** cond-mat.mtrl-sci

**ID:** 2512.06986v2

**Link:** [https://arxiv.org/abs/2512.06986v2](https://arxiv.org/abs/2512.06986v2)

**Summary:** Remote epitaxy exploits substrate interactions transmitted across atomically thin materials to replicate substrate crystal structure. Here we show that competition among graphene-, substrate-, and reconstruction-derived interactions can instead produce frustration. Using GdAuGe films on $N$-layer graphene/SiC(0001), we identify at intermediate $N$ a self-limited interfacial state with broken long-range translational order, accompanied by non-monotonic crystallographic orientation selection in the epitaxial film above. The frustrated interface is accompanied by strongly enhanced magnetic irreversibility above 300 K, with an interface-dominated rather than volume-scaled response, linking epitaxial frustration to an emergent collective property. Annealing drives an initially epitaxial crystal into the frustrated state, distinguishing it from kinetically trapped disorder. First-principles calculations reveal a multi-periodic interfacial potential that provides a microscopic basis for frustration. Together, these results establish epitaxial frustration as a materials-design principle for stabilizing correlated interfacial states and emergent collective properties.

---

<!-- ARXIV_PAPERS_END -->
