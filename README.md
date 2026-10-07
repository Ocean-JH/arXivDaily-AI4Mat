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

*Last checked: 2026-10-07 09:12:31 (SGT)*

### 1. ManifoldCache: Training-Free Diffusion Acceleration via Constraint Manifold Caching

**Authors:** Prashant Pandey, Devineni Sri Venkatraya Chowdary, Brejesh Lall

**Published:** 2026-10-03

**Category:** cs.AI

**ID:** 2610.04510v1

**Link:** [https://arxiv.org/abs/2610.04510v1](https://arxiv.org/abs/2610.04510v1)

**Summary:** Diffusion models for structured scientific generation must produce samples satisfying hard geometric constraints imposed by physics, chemistry, or biology, yet inference in these settings is prohibitively slow, demanding hundreds to thousands of neural-function evaluations per sample. We unify eight state-of-the-art models spanning medical volumetrics, molecular conformations, protein backbone design, crystal structure prediction, and multi-view 3D scenes under a single abstraction, Constraint-Manifold Diffusion Models (CMDMs), in which the target distribution is supported on a manifold defined by an externally specified constraint map. All existing acceleration families fail on this class: quantization exhausts memory on high-dimensional volumetric operators; pruning breaks constraint fidelity; fast ODE solvers allow trajectories to drift off the constraint manifold; and feature-caching heuristics are blind to constraint geometry, inducing mode confusion in the high-noise regime. We introduce ManifoldCache, the first training-free, data-free accelerator designed from first principles for CMDMs. The key insight is that the conditional score decomposes orthogonally into a normal component, which enforces constraint satisfaction, and a tangential component, which navigates within the manifold. Exploiting this structure, we prove that the noise-schedule midpoint is a sharp safe-caching boundary: caching before it incurs provably bounded error, while caching after it guarantees a strictly positive fraction of trajectories suffer mode confusion, a gap that persists up to the boundary. We further prove that deeper network blocks admit provably larger certified cache strides within the safe phase, as a consequence of the score decomposition propagating through block Jacobians. The resulting schedule requires no calibration data, along with zero training overhead.

---

### 2. Molecular Crystal Structure Prediction from Conditional Flow on the Unit Cells

**Authors:** Qiang Zhu, Yihan Weng

**Published:** 2026-10-03

**Category:** cond-mat.mtrl-sci

**ID:** 2610.04193v1

**Link:** [https://arxiv.org/abs/2610.04193v1](https://arxiv.org/abs/2610.04193v1)

**Summary:** A molecular crystal structure is jointly described by its space group symmetry, unit cell, and the molecular alignment within the asymmetric unit. Concurrently predicting all three variables is a daunting task, as it mixes discrete symmetry choices with a high-dimensional search in the continuous space. To address this challenge, we decouple these variables using a three-step generation process. Specifically, we train a flow model to learn the conditional distribution of invariant lattice descriptors (e.g. direct- and reciprocal-lattice successive minima and Selling scalars) from a molecular graph, a Hall setting, and the number of molecules in the asymmetric unit ($Z'$). Using a two sequential quasi-random sampling processes, we first reconstruct the cell parameters that match the predicted lattice invariants and density requirements, and then conduct a molecular packing search within the give symmetry and unit cell constraint. On 84 single-component systems with $Z' \\le 1$, our approach reproduces experimental matches for 83 systems; the remaining failure stems from force-field limitations in preserving the experimental structure. These results demonstrate that learned cell proposals can effectively support crystal structure prediction (CSP) for a given Hall setting and $Z'$, which may be extended to fully blind prediction with variable symmetry and $Z'$ settings in the future.

---

### 3. Reinforcement Learning on the Discrete Composition Channel of a Crystal Generator: Validated Gains and Reward Hacking

**Authors:** Pawan Prakash, Philipp Höllmer, Addis Fuhr, Peter Hirschfeld, P. Ganesh, Stefano Martiniani, Richard Hennig

**Published:** 2026-10-02

**Category:** cs.LG

**ID:** 2610.03880v1

**Link:** [https://arxiv.org/abs/2610.03880v1](https://arxiv.org/abs/2610.03880v1)

**Summary:** Inverse materials design is a long-standing goal of computational materials discovery. Generative models for crystalline materials are typically trained to match the distribution of a structure database, while nothing in their training objective points them at specific design goals such as targeted properties. We use group-relative policy optimization (GRPO) to align a generative model based on stochastic interpolants and discrete flow matching with general black-box reward functions through reinforcement learning. Atom types are generated by a discrete flow and the policy gradient of our generalization of GRPO directly acts on the likelihoods of the atom-type transitions, which differentiates our work from previous reinforcement-learning approaches for diffusion and flow-based generative models of crystalline materials. We introduce a reward function that raises the yield of metastable, unique and novel structures (mSUN) from 13.4% for the pretrained model to 45.5% for the reinforced model, as evaluated by a community benchmark. Our reward also improves the performance of a reinforcement learning framework for crystalline materials based on latent denoising diffusion models. At the same time, we find that directly reinforcing atom-type transition likelihoods enables reward exploitation that has to be prevented with explicit guards. The same analysis also exposes a gap in the community metric. Single-element structures in distinct packings are counted as metastable, unique and novel materials and inflate mSUN without yielding any new compounds. A stability claim is only as good as its reference hull. We report every result split by the number of reference phases behind it and argue that benchmarks should do the same.

---

### 4. LATHE: LAnguage-driven Toolkit for Hypothesis-based crystal Editing

**Authors:** Qianyu Zheng, Shuyi Jia, Victor Fung

**Published:** 2026-10-02

**Category:** cond-mat.mtrl-sci

**ID:** 2610.02671v1

**Link:** [https://arxiv.org/abs/2610.02671v1](https://arxiv.org/abs/2610.02671v1)

**Summary:** Manipulating crystal structures towards targeted geometric properties or symmetry constraints is a longstanding challenge. Existing computational frameworks fall short: LLMs have poor spatial awareness and operate at coarse granularity in the token space, while diffusion- and gradient-based structure generation approaches generally produce complete structures \\textit{de novo} rather allowing for fine-grained editing of a given input under arbitrary constraints. We present LATHE, a geometric toolkit that closes this gap by expressing seven classes of crystallographic properties --- bond length, bond angle, dihedral angle, coordination environment, lattice parameters, cell volume, and space group, as differentiable objectives to enable direct geometric editing of crystal structures. To demonstrate its usage in materials design, we further expose LATHE through a Model Context Protocol server and embed it in a closed-loop multi-agent system which translates hypotheses intogeometric modifications in natural language towards a given design objective. Across single-property benchmarks, LATHE attains near-perfect constraint satisfaction on all seven property types while keeping optimized structures close to local energy minima. The LATHE-equipped agent translates over 87.5\\% of natural-language prompts into valid executable configurations and faithfully completes them. In a band-gap inverse-design case study, the multi-agent loop reaches the target tolerance window in nine of ten independent runs at a typical cost of thirteen hypothesis-evaluation cycles. By bridging natural-language hypothesis generation and physically grounded gradient-based structural editing, this work establishes a paradigm for interpretable, closed-loop computational materials discovery that is immediately applicable to a broad class of functional material design tasks.

---

<!-- ARXIV_PAPERS_END -->
