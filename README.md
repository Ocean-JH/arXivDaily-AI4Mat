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

## New Papers (3)

*Last checked: 2026-10-15 08:17:04 (SGT)*

### 1. CondMSP: Condition-Informed and Resource-Aware Inorganic Materials Synthesis Planning

**Authors:** Heewoong Noh, Gyoung S. Na, Elton Pan, Namkyeong Lee, Chanyoung Park

**Published:** 2026-10-11

**Category:** cs.AI

**ID:** 2610.15603v1

**Link:** [https://arxiv.org/abs/2610.15603v1](https://arxiv.org/abs/2610.15603v1)

**Summary:** Materials synthesis planning (MSP) connects AI-driven materials discovery to experimental realization by proposing precursors, synthesis operations, and processing conditions for a target material. Existing approaches predict these components separately or in pairs and treat conditions only as a prediction target. Consequently, MSP remains centered on recipe prediction: it leaves unexplored how conditions can serve as process context for constructing synthesis routes, and it does not address which candidate routes should be executed under limited experimental resources. We propose CondMSP, which extends MSP from recipe prediction to execution-aware planning. CondMSP predicts temperature, time, and atmosphere by combining a joint predictor with variable-specific experts, and then uses these predictions both as process context, grounding the generation and retrieval of operation sequences, and as execution requirements, specifying which thermal stages can share a furnace run and at what cost. This specification is held fixed across all compared methods; within it, CondMSP ranks routes across precursor sets by a common utility and, under furnace budgets, jointly selects routes and allocates their thermal stages by constrained optimization. CondMSP improves condition and operation prediction and, under this shared constraint, raises reference-recipe recovery from 27.9% to 32.9% at three simulated furnace runs per target and from 34.7% to 40.0% at 30 trials, while a new evaluation set of 2,344 targets supports generalization beyond oxide-dominated training chemistry.

---

### 2. Inverse Designing Reconfigurable Piezoelectric Tensors via Architectural and Modal Programming

**Authors:** Anish Satpati, Marco Maurizi, Hyunmoon Cho, Victor Couedel, Nicolas Mule, Xiaoyu, Zheng

**Published:** 2026-10-10

**Category:** cond-mat.mtrl-sci

**ID:** 2610.14761v1

**Link:** [https://arxiv.org/abs/2610.14761v1](https://arxiv.org/abs/2610.14761v1)

**Summary:** Piezoelectricity arises from the coupling between electric polarization and mechanical deformation, described by a third-rank tensor whose coefficients are constrained by crystal symmetry. In natural crystals, atomic periodicity and energetic stability restrict accessible symmetries, limited to 20 distinct anisotropies that can exist. Here we establish a general framework, based on graph representation, for controlling the full effective piezoelectric tensor through architecture by resolving how macroscopic symmetry, local polarization and deformation of structural elements act together. This enables each coefficient to be traced to the members that reinforce or cancel it and be controlled through targeted geometric changes. We further uncover frequency-selective tensor reconfiguration, in which excitation frequency switches the dominant piezoelectric coefficients of a single architecture. These principles open a broader class of applications in which a single piezoelectric architecture can deliver programmable sensing, actuation and mode conversion across multiple directions and deformation states. We realize a multi-degree-of-freedom actuator that integrates distinct actuation modes in one block and reduces volume by 90% relative to conventional multi-stack assemblies.

---

### 3. Large Out-of-plane Polarization in Two-dimensional Bi2O3 Monolayers Predicted by an AI-driven Inverse-design Workflow

**Authors:** Hongmei Tan, Jing Zhang, Shan Gao, Yueyu Zhang, Xiangmei Duan

**Published:** 2026-10-10

**Category:** cond-mat.mtrl-sci

**ID:** 2610.14429v1

**Link:** [https://arxiv.org/abs/2610.14429v1](https://arxiv.org/abs/2610.14429v1)

**Summary:** Two-dimensional (2D) polar oxides with built-in electric fields offer promising opportunities for nanoscale electronics, optoelectronics, and surface charge engineering. However, their discovery remains challenging due to the enormous structural complexity of nonlayered oxide networks. Here, we combine inverse structural design with a machine-learning interatomic potential and first-principles calculations to explore 2D oxide configurations. Using Bi2O3 as a representative system, we identify two previously unreported polar monolayers with tetragonal and orthorhombic symmetries. Both structures exhibit vertically separated Bi and O sublayers, giving rise to pronounced intrinsic polarity with Berry-phase 2D polarizations of 34.12 and 37.15 pC/m, respectively. Notably, the o-Bi2O3 monolayer exhibits one of the largest reported out-of-plane polarizations among 2D oxides. Both monolayers exhibit dynamical stability, finite-temperature structural integrity, and wide band gaps (~3.8 eV). The large polarization originates from dimensionality-induced reconstruction of the nonlayered Bi-O network, which breaks local coordination symmetry and produces out-of-plane charge redistribution, while the stereochemically active Bi 6s2 lone pair further favors asymmetric Bi-O bonding. These findings suggest dimensionality-induced local-coordination symmetry breaking as a promising design motif for high-polarization 2D oxides, and demonstrate the utility of combining inverse design with machine-learning-assisted screening to explore unconventional polar phases in nonlayered oxide networks.

---

<!-- ARXIV_PAPERS_END -->
