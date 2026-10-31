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

*Last checked: 2026-10-31 09:25:04 (SGT)*

### 1. Framework-Conditional Open Materials Generation

**Authors:** Maya M. Martirossyan, Hillary Pan, Philipp Höllmer, Stefano Martiniani

**Published:** 2026-10-29

**Category:** cs.LG

**ID:** 2610.40443v1

**Link:** [https://arxiv.org/abs/2610.40443v1](https://arxiv.org/abs/2610.40443v1)

**Summary:** Theoretical predictions of novel materials rely on a variety of techniques, from data-mining-based ion substitution methods to fully de novo generative models. Each approach imposes specific constraints and encounters unique challenges when extrapolating beyond the distribution of known materials to discover new ones. The foremost goal of materials generation is to produce stable, unique, and novel (S.U.N.) structures. Predicted structures that meet these criteria, however, typically result from novel chemical compositions mapped onto known structural prototypes or frameworks. We leverage this heuristic insight to present a new generative paradigm for the de novo prediction of inorganic crystalline materials constrained by their structural framework---i.e., the unit cell shapes and respective particle positions. Our method, termed OMatG-FC (Open Materials Framework-Conditional Generation), learns via a combination of discrete flow matching on the atomic species and stochastic interpolants for the volume scaling of the unit cell lattice, while fixing in-place the fractional coordinates and the unit-volume lattice vectors, dramatically reducing the dimensionality of the problem compared to unconstrained (framework-free) generation. Our method is more flexible than existing prototype-constrained methods, demonstrating capability for discovery of unseen, stable prototypes derived from known structural frameworks. We also investigate the number of unique frameworks in the MP-20 dataset, demonstrating the propensity of duplicate frameworks within the dataset and providing a framework-split version. We benchmark the performance of our model using the LeMat-GenBench suite using three ML interatomic potentials and achieve state-of-the-art S.U.N. rate below the convex hull, eschewing the need to learn atomic packings for materials discovery.

---

### 2. AtomSteer: Test-Time Constraint Steering for Atomistic Generative Models

**Authors:** Pengfei Cai, Katharina S. C. Jäger, Utkarsh Utkarsh, Nofit Segal, Bowen Deng, Akshay Subramanian, Rafael Gomez-Bombarelli

**Published:** 2026-10-28

**Category:** cs.LG

**ID:** 2610.38517v1

**Link:** [https://arxiv.org/abs/2610.38517v1](https://arxiv.org/abs/2610.38517v1)

**Summary:** Diffusion and flow matching models offer scalable approaches to generating crystalline materials, molecular conformers, and protein-ligand complexes. However, satisfying crystallographic symmetry, structural geometry, and accurate stereochemistry remains challenging. Satisfying these requirements calls for corrections that preserve the geometry already captured by the pretrained model. In this work, we propose AtomSteer, a test-time inference framework for steering pretrained atomistic generative models with structural constraints. During sampling, AtomSteer corrects intermediate structure predictions with bounded local projections, graph-rigid stereochemical transformations, and projections over periodic symmetries, accepting updates that improve constraint satisfaction while limiting changes to the rest of the structure. We demonstrate AtomSteer across three pretrained backbones, FlowMM, ET-Flow, and Boltz-2, spanning de novo crystal generation and crystal structure prediction, molecular conformer generation, and protein-ligand complex structure prediction. AtomSteer improves space-group distribution coverage in de novo crystal generation and improves target space-group recovery in crystal structure prediction. AtomSteer improves molecular validity and E/Z stereochemical accuracy while retaining conformer ensemble fidelity. For protein-ligand complexes, AtomSteer reduces ligand E/Z errors relative to experimental reference structures while achieving competitive docking success and PoseBusters validity. Our method provides a unified framework for adding chemical and crystallographic control to existing atomistic generative models without retraining or architectural changes.

---

### 3. Crystoria: A Large-Scale Crystal Dataset Linking Thermodynamic and Dynamical Stability for Materials AI

**Authors:** Ke-Xin Pang, Ze-Feng Gao, Yan Gao, Zhong-Yi Lu

**Published:** 2026-10-28

**Category:** cond-mat.mtrl-sci

**ID:** 2610.38195v1

**Link:** [https://arxiv.org/abs/2610.38195v1](https://arxiv.org/abs/2610.38195v1)

**Summary:** Large-scale crystal databases have transformed materials discovery by making millions of structures and thermodynamic properties accessible to materials informatics. Yet dynamical stability remains sparsely characterized at a comparable scale because its evaluation is substantially more computationally demanding than conventional structure and energy calculations. This mismatch creates a critical gap between the rapidly expanding crystal-structure space and the physical information available for materials research and machine learning. Here we introduce Crystoria, a large-scale crystal dataset designed to bring dynamical stability to the scale of modern materials data. We construct Crystoria by systematically curating low-energy and metastable inorganic crystals, standardizing their structural identities, and combining machine-learning-accelerated structural relaxation with phonon-based dynamical screening. The resulting dataset contains 2,649,640 crystal structures, spanning 89 elements, 219 of the 230 space groups, and primitive cells containing 1-48 atoms. Among them, 1,793,353 structures (67.68%) are classified as dynamically stable, revealing substantial variation in dynamical stability across chemical and crystallographic space. By bringing dynamical stability to the scale of millions of crystal structures, Crystoria provides a physically grounded foundation for materials artificial intelligence (AI) and enables systematic exploration of the dynamical crystal landscape.

---

### 4. ManifoldCache: Training-Free Diffusion Acceleration via Constraint Manifold Caching

**Authors:** Prashant Pandey, Devineni Sri Venkatraya Chowdary, Brejesh Lall

**Published:** 2026-10-03

**Category:** cs.AI

**ID:** 2610.04510v2

**Link:** [https://arxiv.org/abs/2610.04510v2](https://arxiv.org/abs/2610.04510v2)

**Summary:** Diffusion models for structured scientific generation must produce samples satisfying hard geometric constraints imposed by physics, chemistry, or biology, yet inference in these settings is prohibitively slow, demanding hundreds to thousands of neural-function evaluations per sample. We unify eight state-of-the-art models spanning medical volumetrics, molecular conformations, protein backbone design, crystal structure prediction, and multi-view 3D scenes under a single abstraction, Constraint-Manifold Diffusion Models (CMDMs), in which the target distribution is supported on a manifold defined by an externally specified constraint map. All existing acceleration families fail on this class: quantization exhausts memory on high-dimensional volumetric operators; pruning breaks constraint fidelity; fast ODE solvers allow trajectories to drift off the constraint manifold; and feature-caching heuristics are blind to constraint geometry, inducing mode confusion in the high-noise regime. We introduce ManifoldCache, the first training-free, data-free accelerator designed from first principles for CMDMs. The key insight is that the conditional score decomposes orthogonally into a normal component, which enforces constraint satisfaction, and a tangential component, which navigates within the manifold. Exploiting this structure, we prove that the noise-schedule midpoint is a sharp safe-caching boundary: caching before it incurs provably bounded error, while caching after it guarantees a strictly positive fraction of trajectories suffer mode confusion, a gap that persists up to the boundary. We further prove that deeper network blocks admit provably larger certified cache strides within the safe phase, as a consequence of the score decomposition propagating through block Jacobians. The resulting schedule requires no calibration data, along with zero training overhead.

---

<!-- ARXIV_PAPERS_END -->
