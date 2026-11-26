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

## Latest Papers (3)

_No new papers were found in the latest check; showing the most recent additions._

*Last checked: 2026-11-26 11:56:29 (SGT)*

### 1. Diagnostic Accuracy Is Not Deployment Value: Decision-Aligned Reliability Evaluation for Foundation MLIPs in Materials Discovery

**Authors:** Harry Sevi, Joonatan E. M. Laulainen

**Published:** 2026-11-23

**Category:** cs.LG

**ID:** 2611.30066v1

**Link:** [https://arxiv.org/abs/2611.30066v1](https://arxiv.org/abs/2611.30066v1)

**Summary:** In AI-guided materials discovery, machine-learning models increasingly decide which candidate materials should receive expensive first-principles or experimental evaluation. Standard reliability metrics such as uncertainty, calibration, novelty, and ranking accuracy evaluate properties of the predictions, but success on these metrics does not necessarily imply a better downstream screening decision. We study this mismatch for foundation machine-learned interatomic potentials (MACE-MP, CHGNet, Orb V3) used to rank candidate crystal structures before DFT verification. We evaluate three representative reliability interventions (novelty detection, sparse DFT calibration, and chemistry-level ranking audits) using a deployment objective that measures how much DFT can be avoided while maintaining a required recall of near-hull candidates. Across all three, a reliability signal can succeed on its immediate target without improving the final screening decision: novelty detects distribution shift but weakly ranks failure severity; calibration can improve pooled ranking metrics while leaving screening unchanged or degrading it; and sparse audits identify MLIP-chemistry combinations with poor ranking reliability without yielding a robustly beneficial routing policy. A two-oracle analysis further shows that the source of failure depends on the screening decision itself: under formation-energy screening, even perfect knowledge of average ranking reliability can select the wrong model, whereas in the evaluated hull-aligned variant the oracle target becomes decision-aligned but finite-budget audits still fail to realize the value. Reliability should be evaluated relative to the decision it supports: the relevant question is not whether a model is uncertain or inaccurate, but whether acquiring and acting on additional information will improve the final discovery decision enough to justify its cost.

---

### 2. Unveiling the Complex high-pressure phases of Sodium at the Melting Curve Minimum via Data-Drive Crystal Structure Prediction

**Authors:** Zhenyu Wang, Chengqian Zhang, Xiaoyang Wang, Haiyang Niu, Jian Lv, Han Wang

**Published:** 2026-11-23

**Category:** cond-mat.mtrl-sci

**ID:** 2611.29889v1

**Link:** [https://arxiv.org/abs/2611.29889v1](https://arxiv.org/abs/2611.29889v1)

**Summary:** Sodium exhibits a remarkable concentration of complex crystalline phases near its melting-curve minimum, yet the atomic arrangements of several experimentally observed phases remain unresolved. Here, we combine CALYPSO crystal structure prediction with Deep Potential models developed through concurrent learning to explore this structural landscape. Searches over more than 1.6 million configurations recover the previously reported $I4/m$ structure of $tI50$ and identify candidate atomic arrangements for $oC120$ and $aP90$, together with three additional low-enthalpy structures, $tI52$, $oP72$, and $oP92$. The proposed candidates reproduce key features of the experimentally indexed cell geometries. First-principles enthalpy calculations, Gibbs free-energy comparisons, and solid--liquid coexistence simulations reveal close competition among these structures and established sodium phases. Near the calculated reference melting minimum, $tI50$ is favored over $cI16$ and $oP8$, whereas $oC120$ and $aP90$ remain closely competitive, with their relative stability sensitive to model accuracy. These results provide testable structural models for unresolved experimental phases and reveal multiple closely competing low-enthalpy configurations near sodium's melting minimum

---

### 3. Generating grain boundary structures at a specified energy with a symmetry-constrained diffusion model

**Authors:** Kazuya Miyamoto, Ibuki Okuda, Izumi Takahara, Teruyasu Mizoguchi

**Published:** 2026-11-20

**Category:** cond-mat.mtrl-sci

**ID:** 2611.27188v1

**Link:** [https://arxiv.org/abs/2611.27188v1](https://arxiv.org/abs/2611.27188v1)

**Summary:** Grain boundaries (GBs) govern many properties of polycrystalline materials, and inverse design would make the GB structure itself a design variable. Crystal generative models such as MatterGen operate on periodic cells, which contain two GBs. The cell energy defines a single GB only when the two are equivalent, but existing models do not enforce this equivalence. Building on MatterGen, we developed a symmetry-constrained diffusion model in which the two GBs are related by a symmetry operation: atoms near one GB are generated, and those near the other are reconstructed through a symmetry projection applied at every denoising step. We applied it to the $Σ5(210)[001]$ symmetric tilt GB in Al, conditioning generation on the GB energy from a machine-learning interatomic potential (MLIP). All 350 generated structures kept a geometrically equivalent GB pair after relaxation. Given a target GB energy, the model generated structures at that energy: for the three in-range targets with many nearby training structures, 44% to 70% fell within $\\pm 0.1$ J/m$^2$ of the target. Tracking weakened at higher energies and failed outside the training range. Of the 91 near-target structures, 90 matched no training structure under the adopted geometric criterion, indicating that the model can propose configurations near the target energy that are distinct from the training structures, a capability that could help identify unknown metastable GB structures observed in experiments. Building GB-pair equivalence into generation thus makes GB properties well-defined design targets, enabling inverse design of GB structures.

---

<!-- ARXIV_PAPERS_END -->
