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

*Last checked: 2026-11-04 09:53:24 (SGT)*

### 1. MSP-LLM: A Structured Large Language Model Framework for Inorganic Material Synthesis Planning

**Authors:** Heewoong Noh, Gyoung S. Na, Namkyeong Lee, Chanyoung Park

**Published:** 2026-02-07

**Category:** cs.AI

**ID:** 2602.07543v4

**Link:** [https://arxiv.org/abs/2602.07543v4](https://arxiv.org/abs/2602.07543v4)

**Summary:** Material synthesis planning (MSP) remains a fundamental and underexplored bottleneck in AI-driven materials discovery, as it requires not only identifying suitable precursor materials but also designing coherent sequences of synthesis operations to realize a target material. Although several AI-based approaches have been proposed to address isolated subtasks of MSP, a methodology for solving the entire MSP task has yet to be established. We propose MSP-LLM, a structured LLM-based framework that formulates MSP as a two-stage process composed of two constituent subproblems: precursor prediction (PP) and synthesis operation prediction (SOP). Our approach introduces a discrete material class as an intermediate decision variable that organizes both tasks into a chemically consistent decision chain. For SOP, we further incorporate hierarchical precursor types as synthesis-relevant inductive biases and employ precursor constraint factorization that preserves precursor-related information in the autoregressive decoding state. Extensive experiments show that MSP-LLM consistently outperforms existing methods on both PP and SOP, as well as on the MSP task, demonstrating an effective and scalable framework with practical potential for autonomous MSP.

---

### 2. Site-orbit masked twin-branch Transformer for symmetry-constrained crystal generation

**Authors:** Junchi Liu, Haoran Si, Luo Yan, Sergei Tretiak, Liujiang Zhou

**Published:** 2026-11-02

**Category:** physics.comp-ph

**ID:** 2611.02906v1

**Link:** [https://arxiv.org/abs/2611.02906v1](https://arxiv.org/abs/2611.02906v1)

**Summary:** Generative models for crystal structure prediction (CSP) have expanded the search space for novel materials and improved screening efficiency. However, simultaneously generating stable and novel structures remains challenging because of the complex structural and physical constraints governing crystals. To address this challenge, we propose site-orbit masked twin-branch Transformer model (ST2M), a symmetry-guided discrete--continuous diffusion framework incorporating degree-of-freedom masks and conditioned on Wyckoff patterns. ST2M represents crystal structures as sequences of independent occupied Wyckoff orbits and employs a twin-branch Transformer to jointly denoise discrete and continuous variables. In our experiments, ST2M achieves a structural validity of 96.37\\%. For known patterns in dataset, 23.86\\% of generated structures simultaneously satisfy stability, uniqueness, and novelty criteria, representing a relative improvement of 68.15\\% over the best-performing baseline. First-principles calculations identify a total of 21 previously unreported stable structures among selected candidates with low predicted energies. These results demonstrate that ST2M can generate chemically viable crystal candidates under prescribed crystallographic constraints and generalize to unknown Wyckoff patterns, providing a practical route to accelerated materials discovery.

---

### 3. Data-driven candidate structure ensemble generation beyond the convex hull with crystALL approach

**Authors:** Adam M. Krajewski, Ricardo Amaral, Jonathan W. Siegel, Luke A. Myers, Rushi Gong, Shun-Li Shang, Zi-Kui Liu

**Published:** 2026-11-02

**Category:** cond-mat.mtrl-sci

**ID:** 2611.02584v1

**Link:** [https://arxiv.org/abs/2611.02584v1](https://arxiv.org/abs/2611.02584v1)

**Summary:** Real materials consist of multiple stable or metastable states under real-world conditions, existing as statistical ergodic ensembles of configurations rather than ideal crystals. Yet, data-driven computational materials discovery increasingly biases itself toward finding "new stable structures" from ground-state DFT calculations alone. This limits our long-term ability to discover materials whose properties emerge from metastable phases, to explain experimental observations, or to model thermodynamic behavior comprehensively. Predicting ergodic sets of atomic configurations of known and hypothetical solids is a fundamental challenge in theoretical crystallography, approached via many complementary methods. We discuss this conceptually and introduce crystALL, a pragmatic and powerful data-driven approach to discovering ensembles beyond the convex hull, embracing structural diversity over stability alone, enabling robust experiment matching in cases evading traditional methods. crystALL leverages 5 million relaxed structures from OPTIMADE and MPDD to rapidly generate a comprehensive candidate set by: (1) species substitutions; (2) ML feature-space analysis with pySIPFENN; (3) representative structure selection via clustering and energy-minimization or property matching; and (4) construction of the final candidate ensemble for experimental or ab initio validation. We also uniquely address the common challenge of experimental composition uncertainties spanning many integer stoichiometries by new efficient searches across anonymized compositional ranges rather than fixed formulas. Overall, crystALL's ensemble-focused philosophy provides critical advantages over the prevailing convex-hull-searching paradigm, which often fails to account for key experimental observations and increases AI/ML discovery bias over time - akin to model collapse in LLMs retrained on iteratively generated content.

---

<!-- ARXIV_PAPERS_END -->
