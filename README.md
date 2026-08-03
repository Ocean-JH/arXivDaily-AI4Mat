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

## New Papers (1)

*Last checked: 2026-08-04 06:57:38 (SGT)*

### 1. SeqGPT: A Constrained Transformer Agent for the Inverse Design of Multi-Panel Composite Structures

**Authors:** Driss Chraibi, Alejandro García Pis, Stéphane Grihon, Sixin Zhang

**Published:** 2026-07-03

**Category:** cs.NE

**ID:** 2607.11910v1

**Link:** [https://arxiv.org/abs/2607.11910v1](https://arxiv.org/abs/2607.11910v1)

**Summary:** Optimizing composite stacking sequences to match continuous targets (e.g., Lamination or Buckling Parameters) with discrete manufacturing constraints represents a challenging combinatorial inverse problem that regularly occurs in composite design especially when numerical optimization approaches are used (bi-step, bi-level configurations). In multipanel configurations, this complexity is further intensified by blending, a global compatibility/continuity requirement between the different panel stackings. This study presents SeqGPT, a conditional Transformer agent developed to replace computationally expensive iterative methods. To ensure both global continuity and manufacturing feasibility by construction, we implemented a hybrid neurosymbolic decoding strategy. SeqGPT predicts a conditional distribution that guides a Constrained Beam Search, where any branch violating blending rules is strictly pruned. Numerical experiments on the 18-panel horseshoe benchmark demonstrate that SeqGPT generates solutions near-instantaneously with buckling performance comparable to evolutionary methods, offering a significant speed-up compared to the state of the art.

---

<!-- ARXIV_PAPERS_END -->
