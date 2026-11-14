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

*Last checked: 2026-11-14 09:58:13 (SGT)*

### 1. ORCHID-SAGE: Fully Reproducible CALPHAD Assessment from Evidence to Phase Diagram

**Authors:** Raymundo Arróyave

**Published:** 2026-11-12

**Category:** cond-mat.mtrl-sci

**ID:** 2611.16308v1

**Link:** [https://arxiv.org/abs/2611.16308v1](https://arxiv.org/abs/2611.16308v1)

**Summary:** Knowledge of phase stability is the first requirement for materials design, and predicting the conditions under which new materials can be synthesized has become a key capability of self-driving laboratories (SDLs). For inorganic materials, notably alloys, these predictions come from thermodynamic databases built with the CALPHAD method. Building a database, however, requires expert judgment at many steps, and because these decisions are rarely recorded, others can use a database but cannot regenerate or update it. Machines can already collect the data, build a first model with machine-learned interatomic potentials and refine it against experiments. The assessment itself, the sequence of judgments that turns these parts into a reliable database, is still carried out by human experts. We argue that it can be automated reproducibly only if the expert knowledge behind an assessment is encoded in formal protocols, so that an assessment delivers a record of its construction and not only its parameters. We introduce ORCHID-SAGE, a standard that organizes this record into reproducible and automatable protocols. In this first attempt, applied to Cr-Ni, the database was regenerated from its record by a script on a second machine, by an AI agent working only through the Model Context Protocol (MCP) and by a refit from public sources only, with the same predictions. Recorded in this way, a database need no longer be fixed at publication but can be updated by AI agents as SDLs and other sources provide new evidence, while the judgment remains with people and on the record.

---

### 2. Quantum Material Generation via Coherent Hamiltonian Search

**Authors:** Jiang Yuhan, Matthew Otten

**Published:** 2026-11-11

**Category:** quant-ph

**ID:** 2611.16016v1

**Link:** [https://arxiv.org/abs/2611.16016v1](https://arxiv.org/abs/2611.16016v1)

**Summary:** Discovering new materials with targeted properties is a central goal of materials science, yet the space of candidates is vast. Data-driven generative models learn the distribution of known materials, but they extrapolate poorly, and a generated structure is not known to be stable. A material's properties follow from its Hamiltonian, and a quantum computer can calculate them from it. We introduce the quantum material generative algorithm (QMage), a coherent search, guided by the Hamiltonian, over crystalline configurations of atomic composition, unit cell structure, and atomic positions, for one whose calculated properties meet the targets to within a given error tolerance. The computation is a single coherent quantum circuit in which each configuration's Hamiltonian is block-encoded, its target eigenstate isolated and properties evaluated, and the satisfying configurations amplified by fixed-point search and measured. One framework covers many targets, from formation energy and band gaps to elasticity and conductivity. We design the algorithm for the mature fault-tolerant era and estimate its cost in logical qubits and Toffoli depth from a classically routine benchmark to targets where established methods are unreliable. The approach generates candidate materials from first principles, rather than generalizing from those known, and could enable materials discovery when the target properties are difficult to predict classically.

---

<!-- ARXIV_PAPERS_END -->
