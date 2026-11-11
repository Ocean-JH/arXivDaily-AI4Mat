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

## New Papers (4)

*Last checked: 2026-11-11 09:41:59 (SGT)*

### 1. Challenges in Non-Polymeric Crystal Structure Prediction: Why a Geometric, Permutation-Invariant Loss is Needed

**Authors:** Emmanuel Jehanno, Romain Menegaux, Julien Mairal, Sergei Grudinin

**Published:** 2025-08-31

**Category:** cs.LG

**ID:** 2509.00832v4

**Link:** [https://arxiv.org/abs/2509.00832v4](https://arxiv.org/abs/2509.00832v4)

**Summary:** Crystalline structure prediction is an essential prerequisite for designing materials with targeted properties. Yet, it is still an open challenge in materials design and drug discovery. Despite recent advances in computational materials science, accurately predicting three-dimensional non-polymeric crystal structures remains elusive. In this work, we focus on the molecular assembly problem, where a set~$\\mathcal{S}$ of identical rigid molecules is packed to form a crystalline structure. Such a simplified formulation provides a useful approximation to the actual problem. However, while recent state-of-the-art methods have increasingly adopted sophisticated techniques, the underlying learning objective remains ill-posed. We propose a better formulation that introduces a loss function capturing key geometric molecular properties while ensuring permutation invariance over $\\mathcal{S}$. Remarkably, we demonstrate that within this framework, a simple regression model already outperforms prior approaches, including flow matching techniques, on the COD-Cluster17 benchmark, a curated non-polymeric subset of the Crystallography Open Database (COD). Our code is available at https://github.com/inria-thoth/SinkFast.

---

### 2. ManifoldCache: Training-Free Diffusion Acceleration via Constraint Manifold Caching

**Authors:** Prashant Pandey, Devineni Sri Venkatraya Chowdary, Brejesh Lall

**Published:** 2026-10-03

**Category:** cs.AI

**ID:** 2610.04510v3

**Link:** [https://arxiv.org/abs/2610.04510v3](https://arxiv.org/abs/2610.04510v3)

**Summary:** Diffusion models for structured scientific generation must produce samples satisfying hard geometric constraints imposed by physics, chemistry, or biology, yet inference in these settings is prohibitively slow, demanding hundreds to thousands of neural-function evaluations per sample. We unify eight state-of-the-art models spanning medical volumetrics, molecular conformations, protein backbone design, crystal structure prediction, and multi-view 3D scenes under a single abstraction, Constraint-Manifold Diffusion Models (CMDMs), in which the target distribution is supported on a manifold defined by an externally specified constraint map. All existing acceleration families fail on this class: quantization exhausts memory on high-dimensional volumetric operators; pruning breaks constraint fidelity; fast ODE solvers allow trajectories to drift off the constraint manifold; and feature-caching heuristics are blind to constraint geometry, inducing mode confusion in the high-noise regime. We introduce ManifoldCache, the first training-free, data-free accelerator designed from first principles for CMDMs. The key insight is that the conditional score decomposes orthogonally into a normal component, which enforces constraint satisfaction, and a tangential component, which navigates within the manifold. Exploiting this structure, we prove that the noise-schedule midpoint is a sharp safe-caching boundary: caching before it incurs provably bounded error, while caching after it guarantees a strictly positive fraction of trajectories suffer mode confusion, a gap that persists up to the boundary. We further prove that deeper network blocks admit provably larger certified cache strides within the safe phase, as a consequence of the score decomposition propagating through block Jacobians. The resulting schedule requires no calibration data, along with zero training overhead.

---

### 3. LeMat-GenBench: A Unified Evaluation Framework for Crystal Generative Models

**Authors:** Siddharth Betala, Samuel P. Gleason, Ali Ramlaoui, Andy Xu, Georgia Channing, Daniel Levy, Clémentine Fourrier, Nikita Kazeev, Chaitanya K. Joshi, Sékou-Oumar Kaba, Félix Therrien, Alex Hernandez-Garcia, Rocío Mercado, N. M. Anoop Krishnan, Alexandre Duval

**Published:** 2025-12-04

**Category:** cs.LG

**ID:** 2512.04562v3

**Link:** [https://arxiv.org/abs/2512.04562v3](https://arxiv.org/abs/2512.04562v3)

**Summary:** Generative machine learning (ML) models hold great promise for accelerating materials discovery through the inverse design of inorganic crystals, enabling an unprecedented exploration of chemical space. Yet, the lack of standardized evaluation frameworks makes it challenging to evaluate, compare, and further develop these ML models meaningfully. In this work, we introduce LeMat-GenBench, a unified benchmark for generative models of crystalline materials, supported by a set of evaluation metrics designed to better inform model development and downstream applications. We release both an open-source evaluation suite and a public leaderboard on Hugging Face, and benchmark 12 recent generative models. Results reveal that an increase in stability is accompanied by lower novelty and diversity on average, with no model excelling across all dimensions. Altogether, LeMat-GenBench establishes a reproducible and extensible foundation for fair model comparison and aims to guide the development of more reliable, discovery-oriented generative models for crystalline materials.

---

### 4. Fast Organic Crystal Structure Prediction with Unit Cell Flow Matching

**Authors:** Alston Lo, Luka Mucko, Austin H. Cheng, Andy Cai, Alastair J. A. Price, Wojciech Matusik, Alán Aspuru-Guzik

**Published:** 2026-06-02

**Category:** cs.LG

**ID:** 2606.03199v2

**Link:** [https://arxiv.org/abs/2606.03199v2](https://arxiv.org/abs/2606.03199v2)

**Summary:** Organic crystal structure prediction (CSP) is a requirement for computational modelling of organic solids, but traditionally costs several CPU-years per molecule. Generative models such as OXtal dramatically reduce this cost by sampling stable organic crystal structures directly. However, OXtal forgoes explicit lattice parametrization in favour of modelling large crops of the bulk material with expensive triangle layers, which can incur a computational cost of minutes per molecule. In this paper, we reduce this to seconds with Clari, a large-scale flow matching model that generates redundancy-free unit cells and replaces triangle layers with pair-bias attention. Clari requires only atom types and bonds as input and does not need an RDKit-sanitizable input molecule, which expands its applicability to challenging chemistries such as fullerenes, metal complexes, and atom clusters. We further ablate key design choices such as auxiliary losses, timestep distributions, noise priors, and self-conditioning. On OXtal's test sets, we surpass OXtal's solve rate while obtaining a speedup of 15-30$\\times$. Because Clari also models explicit hydrogens, it supports inference-time scaling via direct energy ranking, without any decoration or relaxation step. When generating 150 crystals and selecting the top-30 by energy, we further improve solve rate while maintaining a speedup of 5-8$\\times$. We also introduce the CSD Teaching Subset as a new test split of diverse and complex molecules for future benchmarking. Our contributions enable CSP within seconds, making large-scale virtual screening of organic solids practical. Code is available at https://github.com/the-matter-lab/clari.

---

<!-- ARXIV_PAPERS_END -->
