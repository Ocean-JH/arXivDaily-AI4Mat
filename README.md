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
[`config.json`](config.json). The default client requests up to 100 records per
page, retaining the configured 500-result search limit. Smaller pages reduce
response time and avoid repeatedly requesting a large response during arXiv
server failures. HTTP 5xx errors and read timeouts halve the failing page size
down to 25 records, keeping the same offset and using the smaller size for later
pages. Rate limits (HTTP 429) keep the same request and respect the cooldown.
Requests remain sequential with a 10-second delay between pages (at least
3 seconds is required by the [arXiv API terms](https://info.arxiv.org/help/api/tou.html)).
Temporary HTTP and network failures retry the same page up to five times, with
60, 120, 240, then 300-second backoff and a small random delay. The starting
backoff and cap are configurable through `arxiv_retry_backoff_seconds` and
`arxiv_retry_max_seconds`. Server `Retry-After` instructions take precedence,
including HTTP dates. Retries share a 15-minute wait budget across the search;
if a cooldown exceeds the remaining budget, the search stops instead of retrying
early. Requests have 10-second connection and 60-second read timeouts.
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
saved results so a temporary upstream outage does not block deployment. A failed
refresh displays a notice on the home page, records `"status": "stale"` in
`site-status.json`, and emits a GitHub Actions warning. A new generation timestamp
therefore does not imply a successful arXiv refresh. Review the resulting diff
before committing it.

## Architecture

- `arxiv_tracker.py` handles arXiv ingestion, version-aware deduplication, and
  durable state updates.
- `arxiv_client.py` adds bounded backoff and respects server cooldowns using
  the pinned `arxiv==2.2.0` client's parsing and pagination.
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
python -m compileall -q arxiv_client.py arxiv_tracker.py site_renderer.py scripts tests
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
same run and requires `"status": "ok"`. Saved content is still deployed during
an arXiv outage, but the workflow then fails explicitly so a successful
deployment cannot hide a failed refresh.

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

*Last checked: 2026-10-24 08:15:10 (SGT)*

### 1. CrystalAR: Autoregressive Modeling for Symmetric Crystal Generation

**Authors:** Ziqiao Meng, Rongsheng Chen, Zhi Zheng, Nikita Kazeev, Zhenkun Wang, Andrey Ustyuzhanin, Wee Sun Lee

**Published:** 2026-10-20

**Category:** cs.AI

**ID:** 2610.27762v2

**Link:** [https://arxiv.org/abs/2610.27762v2](https://arxiv.org/abs/2610.27762v2)

**Summary:** Deep generative modeling has achieved remarkable progress in crystal generation. Given the rich symmetries inherent in crystalline structures, recent work has sought to explicitly incorporate space-group symmetry into generative models, enabling more effective exploration of novel symmetry templates. Yet introducing symmetry templates increases the combinatorial complexity of stoichiometric relationships between atomic species and crystallographic sites, while creating a fundamental tension between flexible exploration of discrete crystallographic templates and faithful realization of these templates as continuous three-dimensional structures. To address these challenges, we propose CrystalAR, a unified autoregressive framework that models Wyckoff symmetry templates and complete crystal structures within a single generative sequence. Specifically, CrystalAR reformulates continuous coordinate generation as a symmetry-conditioned hierarchy of discrete spatial localization decisions, autoregressively refining the positions of all symmetry-inequivalent sites across resolution levels while jointly modeling their spatial configuration within each level. This discrete hierarchical formulation further enables constraint-aware search over both crystallographic templates and geometric realizations. As a result, CrystalAR retains strong symmetry-template generation capability while achieving competitive de novo generation performance and template-free crystal structure prediction (CSP) accuracy. These results suggest that symmetry-template generation can be retained alongside broadly competitive de novo generation performance and competitive CSP without reliance on symmetry templates retrieved from prior data, providing a promising alternative paradigm for symmetry-preserving crystal generation.

---

<!-- ARXIV_PAPERS_END -->
