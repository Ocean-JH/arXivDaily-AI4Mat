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
[`config.json`](config.json). The default client requests 100 records per page,
waits 10 seconds between requests, and retries transient failures five times.
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
saved results so a temporary upstream outage does not block deployment. Review
the resulting diff before committing it.

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

## New Papers (2)

*Last checked: 2026-09-03 07:51:33 (SGT)*

### 1. Autonomous discovery of new structure-plausibility laws for explainable and rapid crystal diagnosis and screening

**Authors:** Zhilong Song, Lixue Cheng

**Published:** 2026-09-01

**Category:** cond-mat.mtrl-sci

**ID:** 2609.01209v1

**Link:** [https://arxiv.org/abs/2609.01209v1](https://arxiv.org/abs/2609.01209v1)

**Summary:** Crystal generators and tool-using agents propose structures faster than density functional theory (DFT) energy and phonon calculations or experiments can assess them. Deciding which candidates merit expensive assessment is therefore the bottleneck, yet most screens test little beyond atomic overlap and give no chemical reason for failure. Here, our agents generate, test and actively refute two million candidate laws, leaving eight Plausibility Rules for Inorganic Structures (PRIS). These laws encode five mechanisms: short-range repulsion, ionic contact and packing, electrostatic balance, bond-valence conservation and crystallographic site complexity. Experimental structures satisfy our law sets at 82--99%, but satisfy Pauling's rules 2--5 together at only 6.5%. The strictest set detects 87.9% of damaged crystal structures, whereas distance cutoffs detect only 1.6--3.2%. PRIS plausibility is linearly correlated with synthesizability, so the PRIS-derived synthesis score (PSS) explainably screens 83.7% of hard-to-synthesize structures while retaining 80.7% of experimental structures. In a property-conditioned inverse-design run, PRIS and PSS can reduce the DFT validation queue by up to 67.3% and keep 99.2% of the candidates whose DFT-validated bulk moduli reach the design target. Beyond screening, PRIS explains why GNoME remains enriched in rare low-symmetry structures and reveals how wrong-element assignments in falsified crystal reports hide behind plausible coordinates. PRIS moves screening from a pass-or-fail verdict to a chemical reason for failure, showing that autonomous agents can discover, by active refutation, physicochemical laws that guide calculations and experiments.

---

### 2. Fourier Neural Operators for Composition-Driven Crystal Structure Discovery

**Authors:** Zhijie Yu, Jingyu Li, Yang Huang, Jingrun Chen

**Published:** 2026-09-01

**Category:** cond-mat.mtrl-sci

**ID:** 2609.00900v1

**Link:** [https://arxiv.org/abs/2609.00900v1](https://arxiv.org/abs/2609.00900v1)

**Summary:** Crystalline materials discovery is essential for energy, electronics, and catalysis, but the vast chemical and structural space makes exhaustive screening infeasible. Existing voxel-based methods are limited by the local receptive fields of three-dimensional convolutional neural networks and the posterior collapse of high-dimensional variational autoencoders. Here, we develop a Fourier Neural Operator (FNO)-based crystal-field solver that maps a prescribed chemical formula and lattice parameters to periodic number-density and electron-density fields. By operating on global Fourier modes, the solver captures long-range correlations in periodic crystal fields beyond conventional local convolutions. Building on this solver, we construct a coupled generation-solving framework in which a conditional variational autoencoder generates diverse candidate lattice parameters in a low-dimensional basis-coefficient space, followed by density-field prediction and atomic reconstruction through peak detection, position optimization, and weight optimization. The reconstructed structures are further screened using voxel-level filtering, machine-learning interatomic-potential relaxation, and first-principle calculations. The framework generates novel structures across 104 chemical formulas with competitive reconstruction accuracy, demonstrating high generative diversity and structural validity. By extending Fourier neural operators to periodic crystal fields and coupling them with composition-conditioned lattice generation, our approach provides a scalable route to crystal structure discovery from prescribed chemical compositions.

---

<!-- ARXIV_PAPERS_END -->
