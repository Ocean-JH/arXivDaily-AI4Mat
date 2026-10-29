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

## New Papers (2)

*Last checked: 2026-10-29 09:32:24 (SGT)*

### 1. The Acridine Polymorph Landscape: Characterization and Selective Control by Additives

**Authors:** Adam Lahouari, Hengyu Zhou, Nikolaos Galanakis, Michael Kilgour, Daisuke Kuroshima, Jihye Han, Bart Kahr, Mark E. Tuckerman, Alexander G. Shtukenberg, Jutta Rogal

**Published:** 2026-10-27

**Category:** cond-mat.mtrl-sci

**ID:** 2610.37597v1

**Link:** [https://arxiv.org/abs/2610.37597v1](https://arxiv.org/abs/2610.37597v1)

**Summary:** Polymorphism in molecular crystals presents a major challenge for controlling crystallization. Here, we combine experiment and theory to characterize the polymorph landscape of acridine and investigate its selective control by additives. Melt crystallization experiments resolve the previously unknown structure of form VIII, while topological crystal structure prediction recovers all seven known unsolvated polymorphs with determined crystal structures. Combining a fine-tuned machine-learned interatomic potential with anharmonic free energy calculations reproduces the experimentally observed stability relationships and reveals a shallow free energy landscape. Finally, experimentally observed additive-induced polymorph preferences correlate with mixed-crystal substitutional defect energies and topological similarities between additive and acridine crystal structures. Together, these results provide a comprehensive picture of acridine polymorphism, linking crystal structure, thermodynamic stability, and additive-controlled crystallization.

---

### 2. Magnetic crystal generation with site-resolved magnetic moments via Gaussian-mixture retargeting and finite-budget yield prediction

**Authors:** Wen-Chuang Shang, Chenyu Shen, Mikito Tsujimoto, Tomonori Tanaka, Yoshihiro Gohda

**Published:** 2026-10-27

**Category:** cond-mat.mtrl-sci

**ID:** 2610.37222v1

**Link:** [https://arxiv.org/abs/2610.37222v1](https://arxiv.org/abs/2610.37222v1)

**Summary:** We introduce GMMag, a workflow for generating crystal structures together with their site-resolved magnetic moments, built on a conditional variational autoencoder with a graph neural network encoder and a transformer decoder. Gaussian-mixture sampling redirects generation towards selected chemical and magnetic targets without retraining. We systematically investigate how encoder and decoder design, the representation of magnetic-moment magnitudes and relative signs, and sampling choices affect reconstruction, generation quality and diversity. Because a higher screening pass rate does not necessarily yield more qualifying candidates with distinct chemical formulas absent from the reference dataset, we model how repeated generation of the same chemical formulas limits their accumulation and test the model in two separate ten-million-draw runs. As an application, the workflow identifies Nd-containing candidates with chemical formulas absent from the reference dataset, negative formation energies and high estimated saturation magnetization.

---

<!-- ARXIV_PAPERS_END -->
