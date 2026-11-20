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

*Last checked: 2026-11-20 10:49:29 (SGT)*

### 1. GEODE: Symmetry-Preserving Cartesian Diffusion for Crystal Generation

**Authors:** Yuchen Lou, Alex M. Ganose

**Published:** 2026-10-01

**Category:** cond-mat.mtrl-sci

**ID:** 2610.01898v2

**Link:** [https://arxiv.org/abs/2610.01898v2](https://arxiv.org/abs/2610.01898v2)

**Summary:** Most known inorganic crystals exhibit symmetric atomic arrangements, yet generative models often fail to reproduce them. Explicitly enforcing these symmetries has so far yielded fewer stable and novel structures than unconstrained generation. We introduce Generative Equivariant Orbit Diffusion Engine (GEODE), to our knowledge the first model to combine coordinate and lattice diffusion in Cartesian space. GEODE first samples symmetry templates, then jointly generates the lattice, atomic coordinates and atom types while preserving the specified symmetry with a novel Wyckoff-constrained loss. Cartesian diffusion gives coordinate noise a consistent physical scale that we empirically demonstrate improves performance. Unconditional generation achieves a metastable, unique and novel (mSUN) rate of 11.9%, compared with 7.7% for the next best symmetry-aware model. We also introduce sampling time template filtering, which increases mSUN by ~6% without retraining, making GEODE competitive with leading symmetry-agnostic models. Template selection also enables joint symmetry and property guidance, which we demonstrate through classifier-free guidance of permittivity.

---

### 2. Autonomous discovery of new structure-plausibility laws for explainable and rapid crystal diagnosis and screening

**Authors:** Zhilong Song, Heung Law, Lixue Cheng

**Published:** 2026-09-01

**Category:** cond-mat.mtrl-sci

**ID:** 2609.01209v2

**Link:** [https://arxiv.org/abs/2609.01209v2](https://arxiv.org/abs/2609.01209v2)

**Summary:** Generative models and autonomous agents now propose candidate inorganic crystals by the million, yet most screens test little beyond a minimum-distance cutoff and give no chemical reason for failure. For nearly a century, Pauling's rules have served as the main empirical theory of crystal-structure stability, but they remain qualitative and idealized, leading to only 6.5% of known ionic crystals satisfying rules 2--5 simultaneously. Here our agents generate, test and refute two million candidate laws to discover eight Plausibility Rules for Inorganic Structures (PRIS). These laws encode five physical mechanisms: short-range repulsion, ionic contact and packing, electrostatic balance, bond-valence conservation and crystallographic site simplicity. Experimental structures satisfy the PRIS law sets in 82--99% of cases, and the strictest set detects 87.9% of artificially damaged structures, far above the 1.6--3.2% of conventional distance cutoffs. Although derived without synthesis labels, PRIS plausibility is highly linearly correlated with synthesizability, and a continuous PRIS-derived synthesis score (PSS) explainably filters out 83.7% of hard-to-synthesize structures while retaining 80.7% of experimental structures. In an inverse-design task targeting ultra-incompressible crystals, explainable screening by PRIS and PSS cuts the density functional theory (DFT) validation queue by up to 67.3% while retaining 99.2% of the DFT-verified target candidates. Beyond screening, PRIS traces GNoME's low-symmetry excess to artificial element ordering and identifies falsified crystal structures. PRIS moves screening from a pass-or-fail verdict to a chemical reason for failure, showing that autonomous agents can discover, by active refutation, physicochemical laws that guide calculations and experiments.

---

<!-- ARXIV_PAPERS_END -->
