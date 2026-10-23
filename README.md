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

*Last checked: 2026-10-23 08:23:28 (SGT)*

### 1. Orbitol: Crystal Generation on Wyckoff Orbits

**Authors:** Ivan Žugec, Joshua Rosenthal, Ivor Lončarić, Jan-Willem van de Meent, Tin Hadži Veljković

**Published:** 2026-10-21

**Category:** cs.LG

**ID:** 2610.30086v1

**Link:** [https://arxiv.org/abs/2610.30086v1](https://arxiv.org/abs/2610.30086v1)

**Summary:** Generative models propose crystalline materials by learning composition and geometry, but unconditional sampling gives no direct control over the space group, which constrains whether responses such as piezoelectricity are symmetry-allowed. We present Orbitol, a crystal generator built on the Crystalite diffusion Transformer that replaces atom tokens with Wyckoff-orbit tokens. Given a space group and a collection of occupied Wyckoff positions, Orbitol generates the atom type and free coordinates of each orbit together with a compatible lattice, so every valid structure is invariant under the operations of the requested group. It generates structures two to three orders of magnitude faster than the symmetry-aware baselines at the evaluated settings. On MP-20, 13.8% of Orbitol's attempts yielded stable or metastable, unique and novel structures that retained the requested space group after relaxation, compared with 10.8% for SGFM, the next best model. We also introduce SPARC, a score that combines retention of the raw detected space group with agreement between the retained-group and training distributions. Finally, we used Orbitol to generate candidates in piezoelectric crystal classes. Of the structures selected by internal screening, 89% passed our density functional theory checks, and 79% also matched no Materials Project or Alexandria entry with the same space group. Their median figure of merit was nine times that of the piezoelectric materials computed in the Materials Project, and 24% of the new candidates ranked in that set's top 10%.

---

### 2. Crystal-structure design by agentic AI in a language of motifs

**Authors:** Dinh-Khiet Le, Minh-Quyet Ha, Hong-Phuc Vu-Dinh, Viet-Cuong Nguyen, Huan Tran, Truyen Tran, Takashi Miyake, Hiori Kino, Hieu-Chi Dam

**Published:** 2026-08-16

**Category:** cond-mat.mtrl-sci

**ID:** 2608.15900v2

**Link:** [https://arxiv.org/abs/2608.15900v2](https://arxiv.org/abs/2608.15900v2)

**Summary:** Data-driven materials discovery interpolates more reliably than it extrapolates and seldom reveals new structure types. We present MatEvolve, an agentic-AI framework that designs crystals in an interpretable \\emph{language of motifs}, in which each crystal is written as a \\emph{motif profile} that describes the recurring geometric patterns---the \\emph{motifs}---composing the crystal. The motif profile serves not merely as a description of a material but as the medium for material design: the agent edits the profile with a stated rationale and constructs a crystal from the modified one; the most promising candidates are then validated by first-principles calculations. MatEvolve is built on the state-of-the-art language model Claude Fable~5 without fine-tuning. It is applied to the design of rare-earth-lean permanent-magnet compounds and finds novel (meta)stable crystals that are both new structural prototypes and magnet compounds; under an equal validation budget, it does so an order of magnitude more often than generative models. Beyond design, analyzing the human-readable profiles of the discovered crystals reveals their structure--property relationships.

---

<!-- ARXIV_PAPERS_END -->
