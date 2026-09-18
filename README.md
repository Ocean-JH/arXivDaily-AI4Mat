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

*Last checked: 2026-09-19 07:52:34 (SGT)*

### 1. Robust and Efficient AI Frameworks for Scalable Material Design and Property Prediction

**Authors:** Kishalay Das

**Published:** 2026-09-15

**Category:** cond-mat.mtrl-sci

**ID:** 2609.17646v1

**Link:** [https://arxiv.org/abs/2609.17646v1](https://arxiv.org/abs/2609.17646v1)

**Summary:** This thesis develops robust and efficient AI frameworks for accelerating crystalline materials discovery by addressing both major stages of the materials-design pipeline: crystal property prediction and crystal structure generation. Motivated by the high computational cost of Density Functional Theory (DFT) and the limited availability of labeled materials data, the thesis explores graph representation learning, pretraining, multimodal learning, and generative modeling for scalable materials design.   For property prediction, the thesis first introduces CrysXPP, which learns transferable crystal representations through unsupervised graph autoencoding, reducing dependence on large property-labeled datasets. It then proposes CrysGNN, a large-scale self-supervised graph pretraining framework that captures atomic connectivity, chemical attributes, and global structural information and transfers this knowledge to downstream property predictors through knowledge distillation. CrysMMNet further enriches crystal representations by jointly modeling graph structure and textual descriptions, thereby incorporating both local chemical and global structural knowledge.   For crystal generation, the thesis introduces TGDMat, a text-guided joint diffusion framework that jointly models lattice parameters, atomic types, and atomic coordinates while incorporating textual structural knowledge during denoising. This enables the generation of more valid and stable periodic materials while also supporting conditional generation from natural-language descriptions.   Overall, the thesis establishes a unified AI-based framework for data-efficient property prediction and controllable crystal generation, demonstrating how graph learning, multimodal representations, and generative models can reduce computational cost and improve the scalability of materials

---

<!-- ARXIV_PAPERS_END -->
