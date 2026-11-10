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

*Last checked: 2026-11-10 11:57:10 (SGT)*

### 1. Quantitative Assessment of Crystal Structure Prediction

**Authors:** Sergio Rincón, Gabriel González, Nicolás Andrade, Rafael Velásquez, Sebastián Ojeda, Juanita Puentes, Nicolás Aparicio, Paula Cárdenas, Pablo Arbeláez

**Published:** 2026-11-07

**Category:** cs.LG

**ID:** 2611.10380v1

**Link:** [https://arxiv.org/abs/2611.10380v1](https://arxiv.org/abs/2611.10380v1)

**Summary:** Crystal Structure Prediction (CSP) aims to predict a material's 3D structure from its chemical composition, with applications from energy storage to biomedical devices. Despite its importance, existing evaluation frameworks suffer from key limitations: they rely on threshold-sensitive or incomparable metrics, focus predominantly on geometric performance while overlooking physical plausibility, and fail to account for polymorphism, where a chemical composition can crystallize into multiple stable structures. In parallel, recent Symmetry-Informed CSP (SICSP) methods often report results alongside standard CSP baselines while receiving crystallographic templates at inference, which constrain the search space and make SICSP a fundamentally different task. To address these limitations, we introduce an Orientation-invariant, Polymorph-Aware, Large Benchmark (OPAL-Bench) that evaluates CSP and SICSP as separate tasks. We evaluate 7 CSP and 2 SICSP methods under OPAL-Bench across 4 datasets using threshold-free geometric and physical distance metrics. Our results show that no method dominates across all metrics, and that geometric performance is not strongly correlated with physical plausibility. We also release OPAL-CSP, an SE(3)-equivariant flow-matching baseline for the CSP track that performs competitively on geometric metrics and ranks among the best on physical ones. By unifying geometric and physical metrics under a polymorph-aware protocol, OPAL-Bench enables a more comprehensive assessment of generative quality in CSP.

---

### 2. Inverse design of superconductors and semiconductors with differentiable foundation models

**Authors:** Cristóbal Méndez, Justin Tahmassebpur, Tomás A. Arias

**Published:** 2026-11-06

**Category:** cond-mat.mtrl-sci

**ID:** 2611.09572v1

**Link:** [https://arxiv.org/abs/2611.09572v1](https://arxiv.org/abs/2611.09572v1)

**Summary:** Designing a crystal for a target property requires choosing its elements, stoichiometry, and atomic structure together, yet gradients exist only for the continuous structural variables. We introduce differentiable Equiformer fast effective-atom theory (DEFEAT), which lets a pretrained EquiformerV3 foundation model accept continuous species weights and site occupancies without retraining on fractional data, thereby enabling gradient-based materials optimization. Gradients from fine-tuned property models and a machine-learned energy penalty then guide updates to composition, atom count, atomic positions, and lattice vectors in a single optimization. In a search for phonon-mediated superconductors, density-functional perturbation theory on 45 structurally novel designs gives isotropic Allen-Dynes critical temperatures above 10 K for 39; the highest is 24.0 K for ZrTiNb2CN3, and H4LiPd3 (23.2 K) lies on the static DFT hull. In searches for photovoltaic absorbers, SCAN calculations confirm ten novel crystal structures with band gaps within 20% of a 1.34 eV target on their respective raw or empirically corrected scales, all within 70 meV/atom of the DFT hull, and show that the systematic gap error of the training functional propagates into the designs unless the objective corrects for it. Quasiharmonic free energies from machine-learned potentials further show that finite-temperature competition with solid phases can reorder candidates relative to the static hull.

---

<!-- ARXIV_PAPERS_END -->
