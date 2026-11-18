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

*Last checked: 2026-11-18 11:18:33 (SGT)*

### 1. What Do LLMs Use to Judge Synthesis Recipes? An Experimental Analysis on 240 Solid-State Syntheses

**Authors:** Derek van Tilborg, Laura-Bianca Pasca, Harry Sevi, Kyle Reeves, Thomas Loux, Aikaterini Flessa Savvidou, Varincka Jean-Gilles, Marilou Carouge, Joonatan E. M. Laulainen

**Published:** 2026-11-17

**Category:** cs.CE

**ID:** 2611.22623v1

**Link:** [https://arxiv.org/abs/2611.22623v1](https://arxiv.org/abs/2611.22623v1)

**Summary:** Inorganic materials discovery is increasingly limited by synthesis rather than by material design. Large language models (LLMs) are being adopted to propose synthesis conditions with little experimental evidence of their capabilities and biases. Here, we carry out an experimental synthesis benchmark of 240 experiments across eight known and unknown inorganic oxides and subsequently evaluate an LLM as a zero-shot ranker over fixed banks of solid-state synthesis recipes. For each pair of recipes for the same oxide target, `GPT-5.6-Sol` selects the recipe expected to yield higher target-phase purity. We aggregate these pairwise preferences using a regularized Bradley-Terry model to obtain a ranked list of synthesis recipes for a given target material. By comparison with the actual purity, obtained through X-ray diffraction, we measure `GPT-5.6-Sol`'s performance as a zero-shot ranker (0.72 pairwise accuracy). By selective removal of the information exposed to the model during this ranking, we conclude that ranking is driven predominantly by thermal features, with reaction chemistry modulating the effect. Ranking accuracy tracks the purity-temperature correlation by target (Spearman ρ= 0.91\\), \\(p = 0.002\\), and on the six thermally-driven targets withholding all chemical identity hardly impacts performance (0.68) compared to withholding temperature (0.56). Ranking performance was higher on known than unknown targets, but the group-level difference was not statistically conclusive. The methodological choices highlight the need for more experimentally validated synthesis benchmarks and position LLMs as a thermally informed prior.

---

### 2. DSADiff: Data Structure-Aware Diffusion for Crystal Structure Prediction via Mitigating Complexity- and Imbalance-Induced Biases

**Authors:** Jiang Xiaobo, Dinghong Lai

**Published:** 2026-11-17

**Category:** cs.LG

**ID:** 2611.22050v1

**Link:** [https://arxiv.org/abs/2611.22050v1](https://arxiv.org/abs/2611.22050v1)

**Summary:** Crystal Structure Prediction (CSP) is an important step in accelerating the generation and discovery of new materials. In recent years, diffusion-based CSP methods have made significant progress. However, existing models still suffer from generation bias when facing diverse materials spaces, while systematic approaches for tracing the sources of such performance variations remain limited. To address this issue, we propose LAS (Layered Analysis Strategy), a mechanism analysis framework that identifies crystal complexity and elemental composition imbalance as two key factors affecting generation difficulty and further reveals their relationships with model generation performance. Building on these findings, we further propose DSADiff (Data Structure-Aware Diffusion), a data structure-aware diffusion model that transforms the key factors identified by LAS into a unified generation difficulty representation and uses it to jointly drive feature modeling and training strategy optimization. This enables the model to adapt its representation and generation capability to samples with different data structures and difficulty levels, thereby mitigating learning bias across samples. Experiments on three CSP benchmark datasets, including Carbon-24, demonstrate that DSADiff consistently improves both Match Rate and RMSE, with a maximum Match Rate improvement of 9%, surpassing existing state-of-the-art methods and achieving new state-of-the-art performance. This work deepens the understanding of diffusion-based CSP models from the perspective of generation bias and provides a new direction for designing less biased generative models for complex materials spaces.

---

<!-- ARXIV_PAPERS_END -->
