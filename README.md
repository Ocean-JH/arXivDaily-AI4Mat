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

*Last checked: 2026-08-23 06:19:02 (SGT)*

### 1. Grounded verification of chemical and materials reasoning: detection is the bottleneck

**Authors:** Can Polat, Mustafa Kurban, Erchin Serpedin, Hasan Kurban

**Published:** 2026-07-19

**Category:** cs.LG

**ID:** 2607.17417v2

**Link:** [https://arxiv.org/abs/2607.17417v2](https://arxiv.org/abs/2607.17417v2)

**Summary:** Language models are moving into chemistry and materials discovery workflows, where a wrong molecular formula, space group, or formation energy can silently propagate into downstream decisions. These confabulations hide inside fluent reasoning traces and concentrate on rare, long-tail entities, where model confidence is least trustworthy. Retrieving reference data for every prompt would catch them, but at a heavy coverage and abstention cost. We show that deterministic, database-grounded verification catches and repairs these errors selectively, and that the binding constraint is detection rather than repair. Our tiered verifier extracts each checkable claim, tests it against authoritative databases and physical law, and retrieves a reference value only when a check fails. Across four models and over five hundred prompts with pinned conditions, gated correction cuts the error rate of committed formulas from 22% to 4% with 3.2 times fewer retrievals than blanket augmentation, and it outperforms a conversational retrieval oracle when every answer, corrected or not, is scored. When a flag fires, repair almost always succeeds; the benefit reaches the final answer only where the verifier's scope covers it and where long-tail error exists. Checkable claims, checked cheaply, are a practical lever for trustworthy machine reasoning in chemistry.

---

<!-- ARXIV_PAPERS_END -->
