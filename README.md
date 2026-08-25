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

## Latest Papers (1)

_No new papers were found in the latest check; showing the most recent additions._

*Last checked: 2026-08-26 06:23:55 (SGT)*

### 1. Towards Automated Discovery: A Review of Generative Models, Multimodal Learning and Closed-Loop Workflows in Inverse Materials Design

**Authors:** Anand Babu, Rogério Almeida Gouvêa, Gian-Marco Rignanese

**Published:** 2026-06-01

**Category:** cond-mat.mtrl-sci

**ID:** 2606.02507v2

**Link:** [https://arxiv.org/abs/2606.02507v2](https://arxiv.org/abs/2606.02507v2)

**Summary:** Inverse materials design is shifting materials discovery from forward prediction toward targeted proposal of candidates that satisfy objectives under physical constraints. Here, we review advances in generative crystal structure modeling, multimodal learning, and closed-loop design pipelines for crystalline solids. We survey how generators learn chemical-structural priors from databases to enable controllable sampling of periodic structures, comparing variational autoencoders, normalizing flows, autoregressive models, and diffusion models. Across these families, we examine where feasibility constraints and physical priors enter, from representations and training objectives to sampling-time guidance, screening, and relaxation. We also discuss multimodal learning combining crystal structures, thermodynamic and electronic information, microscopy, spectroscopy, processing context, and scientific text to construct materials representations. Inverse-design strategies integrating conditional generation with latent optimization, Bayesian optimization, reinforcement learning, and active learning are also examined. We highlight recurring failure modes, including surrogate exploitation, diversity collapse, distribution shift, and the stability-synthesizability gap, and outline evaluation based on validity, novelty, uniqueness, stability, and cost. To support credible claims, we define a nine-rung discovery-credibility ladder and propose a minimum reporting standard: declared matching tolerances and database snapshots; separate reporting of uniqueness, training-set memorization, and external rediscovery; novelty as a continuous distance distribution; energy-above-hull distributions with functional and hull version; relaxation-survival and dynamical stability rates; and validation cost per credible hit. Headline validity or S.U.N. rates without these disclosures should be treated as uninformative.

---

<!-- ARXIV_PAPERS_END -->
