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

*Last checked: 2026-09-25 08:16:31 (SGT)*

### 1. OMatG-flash: An All-Atom Flow Map with Reinforce Adjoint Matching for Scalable Materials Discovery

**Authors:** Thomas Egg, Harry Winston Sullivan, Ellad B. Tadmor, Stefano Martiniani

**Published:** 2026-09-22

**Category:** cs.LG

**ID:** 2609.26402v1

**Link:** [https://arxiv.org/abs/2609.26402v1](https://arxiv.org/abs/2609.26402v1)

**Summary:** The discovery of novel inorganic materials drives technological breakthroughs in critical fields such as computing and energy storage. Generative AI has promised to accelerate the materials discovery pipeline, but state-of-the-art flow and diffusion models remain bottlenecked by the cost of proposing candidate materials. To address this, we introduce OMatG-flash, an all-atom flow map for inorganic crystal structure prediction (CSP) and de novo generation (DNG). OMatG-flash is a Pareto-optimal inference engine for materials, sampling candidate materials with an order of magnitude fewer inference steps and less wall-clock time than existing flow and diffusion models while demonstrating benchmark performance on par with the state-of-the-art. To enable post-training fine-tuning we apply Reinforce Adjoint Matching to flow maps, further improving match rates and RMSE on the unconditional CSP task. OMatG-flash showcases the potential of flow maps to accelerate generation of high-quality candidate inorganic materials and demonstrates a step forward in sample throughput necessary for data-hungry materials discovery workflows.

---

<!-- ARXIV_PAPERS_END -->
