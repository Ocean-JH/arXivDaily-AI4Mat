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

The search expression and result limit live in [`config.json`](config.json).
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
status. Review the resulting diff before committing it.

## Architecture

- `arxiv_tracker.py` handles arXiv ingestion, version-aware deduplication, and
  durable state updates.
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
python -m compileall -q arxiv_tracker.py site_renderer.py scripts tests
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

## New Papers (3)

*Last checked: 2026-08-02 19:59:16 (SGT)*

### 1. Machine Learning for Designing Undesignable Metal-Organic Frameworks

**Authors:** Satya Kokonda

**Published:** 2026-07-29

**Category:** cond-mat.mtrl-sci

**ID:** 2607.27368v1

**Link:** [https://arxiv.org/abs/2607.27368v1](https://arxiv.org/abs/2607.27368v1)

**Summary:** Many crucial processes are too complex for computational modeling, requiring experimentation to identify promising materials. Here, a methodology for material design is presented, while photocatalysis is presented as a specific case-study. Metal-Organic Frameworks (MOFs) are a subset of highly promising porous nanomaterials, used in a variety of unmodellable applications. Reinforcement learning generated 60,000 novel MOFs optimized for CO/H20 selectivity. A predictor funnel system was created, iteratively removing low-scoring MOFs to 10,986 potential candidates, improving computational efficiency by 276%. While trained Crystal Graph Convolutional Neural Network (CGCNN) models predicted features for creating a fitness function incorporating stability, catalytic ability, material cost, sustainability, and adsorption while allowing the inclusion of application specific design criterion. This designed function provides a computational method to model photocatalytic performance- and filtered down to two promising MOFs which each pass a myriad of synthesis criteria, first a Cr-based MOF with photocatalyst score 230% higher than the control. Second, a Zn-based MOF outperforms the best control across all relevant metrics, demonstrating robustness against variable fitness functions. This work designed 20 materials, each 125% better than the control for this application. Furthermore, analysis revealed insightful design patterns, such as the significant influence of metal cluster N262 on catalytic performance, providing a method for future work to narrow the chemical space. By incorporating industrially applicable features such as cost or stability of the material, this work successfully designs industrially promising materials in otherwise unmodellable processes such as drug delivery, while paving a method for multi-objective optimization incorporating 260% more features than prior work.

---

### 2. Instability-induced bistable shape-morphing kirigami structures

**Authors:** Xiaoyuan Ying, Marcelo A. Dias

**Published:** 2026-07-29

**Category:** cond-mat.soft

**ID:** 2607.26941v1

**Link:** [https://arxiv.org/abs/2607.26941v1](https://arxiv.org/abs/2607.26941v1)

**Summary:** Deployable shape-morphing structures that transform from flat sheets into stable three-dimensional configurations are highly desirable for applications ranging from soft robotics and biomedical devices to adaptive architecture and aerospace systems. Existing kirigami-based morphing systems primarily rely on isotropic deployment, compliant soft materials, or external constraints to maintain deployed shapes, which limits geometric programmability, structural integrity, and applicability in rigid-material systems. Here, we present an inverse design framework for anisotropic bistable kirigami structures that enables programmable shape morphing through controlled geometric frustration and instability-induced deployment. The framework combines a semi-analytical mechanical model with geometry to establish a direct connection between geometric transformation and the underlying energy landscape. We show that instability-induced shape morphing leads to tunable bistability and directional deployment in anisotropic kirigami structures. The results are validated through finite element simulations and experiments, demonstrating stable deployed configurations and programmable anisotropic morphing. The proposed framework further provides a general design strategy that can be integrated with various active actuation systems, enabling broader engineering applications.

---

### 3. Thermodynamics-Informed Machine Learning for Energy Materials Discovery

**Authors:** Pol Benítez, Cibrán López, Claudio Cazorla

**Published:** 2026-07-28

**Category:** cond-mat.mtrl-sci

**ID:** 2607.26296v1

**Link:** [https://arxiv.org/abs/2607.26296v1](https://arxiv.org/abs/2607.26296v1)

**Summary:** Machine learning (ML) is transforming materials discovery by enabling rapid prediction of properties that previously required computationally expensive first-principles calculations. Yet most current ML models remain fundamentally limited to zero-temperature descriptions, learning static lattice energies while neglecting the thermodynamic effects that govern materials behaviour at finite temperature. Because phase stability, functional response, and performance are governed by free-energy landscapes rather than static energies alone, this limitation represents a major barrier to predictive materials design under realistic operating conditions. In this Perspective, we argue that developing thermodynamics-informed ML constitutes one of the most important and least explored frontiers in materials discovery. We examine the fundamental shortcomings of energy-based models, highlighting the essential roles of entropy and anharmonicity in determining free energies and materials functionality. We review emerging strategies, including machine-learned interatomic potentials and hybrid ML-statistical mechanics frameworks, while identifying key challenges related to data availability, transferability, and thermodynamic consistency. Building on these advances, we outline a roadmap for thermodynamics-informed ML centred on direct free-energy learning, entropy-aware representations, and adaptive sampling across temperature. We highlight the transformative opportunities this paradigm offers for energy materials and argue that the next generation of ML models must move beyond static energy predictions towards a thermodynamic description of materials behaviour under realistic operating conditions.

---

<!-- ARXIV_PAPERS_END -->
