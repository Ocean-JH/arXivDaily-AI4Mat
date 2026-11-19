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

*Last checked: 2026-11-19 10:55:56 (SGT)*

### 1. How anion composition governs structural frameworks and Li-ion transport in oxychloride solid-state electrolytes

**Authors:** Jiho Lee, Seungwoo Hwang, Seungwu Han, Jung-Hoon Lee, Jisu Jung, Youngho Kang, Sungwoo Kang

**Published:** 2026-11-10

**Category:** cond-mat.mtrl-sci

**ID:** 2611.13611v2

**Link:** [https://arxiv.org/abs/2611.13611v2](https://arxiv.org/abs/2611.13611v2)

**Summary:** Mixed-anion lithium oxychlorides exhibit high Li conductivity, but the relationship between oxygen content, structural framework, and Li-ion transport remains unclear. Here, crystal structure prediction and molecular dynamics simulations with machine-learning interatomic potentials are used to examine $\\mathrm{Li}_yM\\mathrm{O}_x\\mathrm{Cl}_{6-2x}$ ($M$ = Nb and Ta [Group 5] and $M$ = Ti, Zr, and Hf [Group 4]). Increasing oxygen content changes isolated chloride-rich polyhedra into one-dimensional chains and subsequently more highly connected two- and three-dimensional frameworks. In the Group 5 series, fast Li diffusion occurs over $x \\approx 0.67$--1.5, where the Li sites form a three-dimensional percolating network. Potential of mean force maps and nudged elastic band calculations reveal that fast Li-ion transport requires a low-dimensional framework supporting long-range migration through undercoordinated Li sites with low barriers, together with similar energies across Li sites. Finally, we perform fine-grid compositional search, which identifies $\\mathrm{LiNbO}_{0.67}\\mathrm{Cl}_{4.67}$, $\\mathrm{LiTaO}_{0.75}\\mathrm{Cl}_{4.5}$, $\\mathrm{LiNbO}_{1.5}\\mathrm{Cl}_3$, and $\\mathrm{LiTaO}_{1.5}\\mathrm{Cl}_3$ as stable candidates with predicted room-temperature self-diffusivities of up to $\\sim 10^{-6}\\,\\mathrm{cm}^2/\\mathrm{s}$. These findings establish how oxygen content controls framework and Li-ion transport, guiding the design of lithium oxyhalide electrolytes.

---

### 2. Physics-Guided Crystal Structure Elucidation from Powder X-Ray Diffraction with Universal Machine-Learning Interatomic Potentials

**Authors:** Yunsung Lim, Seungwoo Hwang, Seungwu Han

**Published:** 2026-11-18

**Category:** cond-mat.mtrl-sci

**ID:** 2611.23760v1

**Link:** [https://arxiv.org/abs/2611.23760v1](https://arxiv.org/abs/2611.23760v1)

**Summary:** Determining unique atomic coordinates from powder X-ray diffraction (PXRD) remains challenging because peak overlap, weak scattering from light elements, limited scattering contrast between elements with similar atomic numbers, and experimental noise render the inverse problem underdetermined. Here, we present XCAPE (XRD-Constrained Accelerated Prediction Engine), a crystal structure prediction (CSP) framework that integrates experimentally derived composition, unit cell parameters, space group, and PXRD data into a symmetry-aware evolutionary search. XCAPE explores Wyckoff-site configurations using tailored mutation operations, evaluates candidates by both energetic stability and diffraction agreement, and accelerates geometry optimization using a universal machine-learning interatomic potential (MLIP). The framework recovered 71 of 77 database-derived benchmark structures (92.2%) from simulated PXRD patterns and all 12 reference structures from experimental PXRD patterns. It further identified 12 candidate structure assignments that are consistent with experimental PXRD patterns, lack matching entries in the Inorganic Crystal Structure Database (ICSD), and are thermodynamically competitive at the MLIP level. Density functional theory (DFT) calculations showed that 10 of these 12 candidates lie within 10 meV/atom of the convex hull. By bridging experimental diffraction data and physically plausible atomistic models, XCAPE can provide structural insight into previously unresolved materials and support accelerated materials discovery in automated research workflows.

---

<!-- ARXIV_PAPERS_END -->
