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

## New Papers (1)

*Last checked: 2026-09-23 07:58:55 (SGT)*

### 1. SCALE: Simulation-Calibrated Amortized Learning for Energy Materials (A hybrid architecture connecting deterministic modeling, real-world data, and transformer-scale inference for accelerated energy-materials discovery)

**Authors:** Kuan Huang, Bo Bai

**Published:** 2026-09-03

**Category:** cs.LG

**ID:** 2609.22233v1

**Link:** [https://arxiv.org/abs/2609.22233v1](https://arxiv.org/abs/2609.22233v1)

**Summary:** Energy systems face converging pressures for security, affordability, resilience, and sustainability, creating a need for faster discovery of deployable energy materials. Here we introduce SCALE (Simulation-Calibrated Amortized Learning for Energy Materials), a physics-grounded, real-world-data-calibrated learning architecture that connects deterministic scientific operators, experimental calibration, expanded calibrated label generation, and transformer-scale inference. SCALE converts selected high-cost mechanistic computation and measured evidence into reusable models for rapid screening, ranking, inverse design, and active learning. We formulate the framework, identify ten method-based application regimes, and demonstrate SCALE for solid-state metal-hydride hydrogen-storage capacity prediction. In this implementation, a hydride phase-equilibrium capacity operator is calibrated against 381 measured ML-HydPARK capacity anchors and used to generate 5,000 candidate-condition-prototype teacher labels. A crystallographically anchored periodic-graph representation preserves atomic sites, periodic neighbor relationships, and local metal environments absent from formula-only encodings. An edge-biased graph transformer with 2.90 million parameters reproduces calibrated teacher labels with five-fold surrogate fidelity of MAE 0.0582 wt% H2, RMSE 0.0833 wt% H2, R2 = 0.9927, and Pearson r = 0.9963. Post hoc attention analysis suggests that SCALE learns chemically organized element groupings and metal-metal relationships consistent with established hydride chemistry, without chemistry-group labels as supervision. Once trained, SCALE shifts million-candidate evaluation from repeated deterministic workflow execution to batched learned inference, reducing per-candidate screening cost by approximately 10^7-10^8 while retaining links to simulation and experimental evidence.

---

<!-- ARXIV_PAPERS_END -->
