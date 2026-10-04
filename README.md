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
[`config.json`](config.json). The default client requests up to 500 records per
page, so the configured 500-result search normally needs just one request.
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
same run, so a stale deployment fails visibly.

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

## Latest Papers (4)

_No new papers were found in the latest check; showing the most recent additions._

*Last checked: 2026-10-04 08:21:30 (SGT)*

### 1. GEODE: Symmetry-Preserving Cartesian Diffusion for Crystal Generation

**Authors:** Yuchen Lou, Alex M. Ganose

**Published:** 2026-10-01

**Category:** cond-mat.mtrl-sci

**ID:** 2610.01898v1

**Link:** [https://arxiv.org/abs/2610.01898v1](https://arxiv.org/abs/2610.01898v1)

**Summary:** Most known inorganic crystals exhibit symmetric atomic arrangements, yet generative models often fail to reproduce them. Explicitly enforcing these symmetries has so far yielded fewer stable and novel structures than unconstrained generation. We introduce Generative Equivariant Orbit Diffusion Engine (GEODE), to our knowledge the first model to combine coordinate and lattice diffusion in Cartesian space. GEODE first samples symmetry templates, then jointly generates the lattice, atomic coordinates and atom types while preserving the specified symmetry with a novel Wyckoff-constrained loss. Cartesian diffusion gives coordinate noise a consistent physical scale that we empirically demonstrate improves performance. Unconditional generation achieves a metastable, unique and novel (mSUN) rate of 11.9%, compared with 7.7% for the next best symmetry-aware model. We also introduce sampling time template filtering, which increases mSUN by ~6% without retraining, making GEODE competitive with leading symmetry-agnostic models. Template selection also enables joint symmetry and property guidance, which we demonstrate through classifier-free guidance of permittivity.

---

### 2. EP-Flow: Disordered Crystal Structure Prediction without Site-Level Annotations

**Authors:** Qiuliang Liu, Liming Wu, Qi Li, Zhonglong Peng, Chang Chen, Xiaolong Chen, Wenbing Huang, Shifeng Jin

**Published:** 2026-10-01

**Category:** cs.LG

**ID:** 2610.01315v1

**Link:** [https://arxiv.org/abs/2610.01315v1](https://arxiv.org/abs/2610.01315v1)

**Summary:** Generative models have made rapid progress in ordered crystal structure prediction, yet many functional materials are intrinsically disordered, with substitutional mixing, vacancies, or interstitial species controlling their properties. Existing crystal generators either assume deterministic site occupations or require site-level disorder annotations, which are often unavailable when the chemical formula is the primary input. We formulate disordered crystal structure prediction through an Occupancy Distribution Matrix (ODM), a continuous site-by-species representation that unifies ordered crystals, solid solutions, vacancy disorder, and interstitial occupancy. A valid ODM must satisfy coupled site-wise occupancy, mass-conservation, and non-negativity constraints, placing each sample on a formula-dependent transportation polytope. We propose Entropic Polytope Flow (EP-Flow), a marginal-constrained flow matching framework that canonicalizes heterogeneous polytopes into a shared double-centered space, learns a marginal-preserving flow, and recovers feasible occupancies through a Sinkhorn inverse map. By jointly generating occupancies, fractional coordinates, and lattice parameters, EP-Flow achieves state-of-the-art performance on formula-conditioned disordered CSP benchmarks derived from COD and MPDS, substantially outperforming adapted ordered-crystal generators. Analyses further show that EP-Flow recovers sparse and chemically meaningful local disorder patterns rather than merely matching global composition statistics.

---

### 3. Imaging Surface Magnetization in Altermagnetic MnTe Films

**Authors:** Ling-Jie Zhou, Senlei Li, Zi-Jie Yan, Yufei Zhao, Hongtao Rong, Zelong Xiong, Yiran Zhao, Zhaorong Gu, Pu Xiao, Ke Wang, Lok Kan Lai, Hyeonhu Bae, Haoyu Liu, Chao-Xing Liu, Binghai Yan, Cui-Zu Chang, Hailong Wang, Chunhui Rita Du

**Published:** 2026-05-24

**Category:** cond-mat.mtrl-sci

**ID:** 2605.25241v2

**Link:** [https://arxiv.org/abs/2605.25241v2](https://arxiv.org/abs/2605.25241v2)

**Summary:** Altermagnets with pronounced spin-splitting band structure, unconventional magnetic and crystal symmetries, and exotic magneto-transport properties have received immense interest in cutting-edge spintronics, materials science, and condensed matter physics research. Microscopic imaging of spontaneous magnetic domains and phases in altermagnets constitutes an important step for investigating their underlying material properties, mechanisms, and spin behaviors. Taking advantage of scanning-probe quantum microscopy, here we report nanoscale quantum sensing of a prototypical altermagnet candidate $α$-MnTe. We visualize evanescent magnetization and the associated magnetic domains in epitaxial MnTe films, which allows external magnetic fields to control the intrinsic altermagnetic order and configurations. By evaluating a series of MnTe films with different thicknesses down to the atomic scale, we further present evidence for the interfacial origin of the observed weak magnetization and show its correlation with the anomalous Hall effect in MnTe film. Our results advance the current understanding of emergent altermagnetism, providing insights into future material design of altermagnet-integrated spintronic devices.

---

### 4. Riemannian Flow Models with Reinforcement Learning for Molecular Crystal Structure Prediction

**Authors:** Thomas Egg, Harry Winston Sullivan, Maya M. Martirossyan, Philipp Höllmer, Cheng Zeng, Adrian Roitberg, Mingjie Liu, Richard Hennig, Sapna Sarupria, Ellad B. Tadmor, Stefano Martiniani

**Published:** 2026-09-30

**Category:** cs.LG

**ID:** 2609.39773v1

**Link:** [https://arxiv.org/abs/2609.39773v1](https://arxiv.org/abs/2609.39773v1)

**Summary:** Crystal structure governs material properties, making crystal structure prediction (CSP) a fundamental problem in materials science. Generative models are a promising approach for solving this problem, but the prevalence of polymorphism, coupled with large unit cells and complex packing geometry, makes the molecular CSP task challenging for existing models. To address this, we introduce Coarse-Grained Open Materials Generation (CG-OMatG), an equivariant Riemannian flow-based generative model. CG-OMatG predicts molecular crystal structures \\textit{via} a coarse-grained, hierarchical representation. CG-OMatG treats molecules as rigid bodies---performing both inter- and intra-molecular message passing to construct a geometric representation for molecular packings---and learns to reconstruct molecule centroid positions, orientations, and lattice parameters, conditioned on chemical species and conformer geometry. We train the model on subsets of the Open Molecular Crystals (OMC25) and Cambridge Structural Database (CSD) datasets. Further, we fine-tune the model \\textit{via} policy gradient reinforcement learning to steer the model towards generating low-energy candidate structures. We validate the generated structures on the CSP blind test benchmark, assessing agreement with experimentally determined crystals using COMPACK packing-similarity analysis. CG-OMatG exhibits strong performance for generative molecular crystal structure prediction, paving the way for accelerated polymorph screening and organic solid-state materials discovery.

---

<!-- ARXIV_PAPERS_END -->
