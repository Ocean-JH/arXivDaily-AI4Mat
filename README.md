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

## New Papers (2)

*Last checked: 2026-08-07 09:28:47 (SGT)*

### 1. ASE2SPRKKR: a unified Python framework integrating the Spin-Polarized Relativistic Korringa-Kohn-Rostoker method into the Atomic Simulation Environment

**Authors:** Ridha Eddhib, Matyáš Novák, Hubert Ebert, Aki Pulkkinen, Ján Minár

**Published:** 2026-08-06

**Category:** cond-mat.mtrl-sci

**ID:** 2608.05957v1

**Link:** [https://arxiv.org/abs/2608.05957v1](https://arxiv.org/abs/2608.05957v1)

**Summary:** The Spin-Polarized Relativistic Korringa-Kohn-Rostoker (SPR-KKR) is an all-electron ab-initio multiple-scattering code that provides unique capabilities for treating chemical disorder, finite-temperature magnetism, relativistic effects, and spectroscopic properties of various types of solids through its fundamental formulation in terms of the single-particle Green's function rather than eigenstates. We present ASE2SPRKKR, a comprehensive Python interface that integrates SPR-KKR into the Atomic Simulation Environment (ASE), making SPR-KKR more accessible, streamlined, and uniform. Our implementation extends the ASE's Atoms object to handle fractional site occupations for coherent-potential-approximation calculations while maintaining full compatibility with ASE's extensive ecosystem of structure builders, optimizers, and analysis tools. Automated input generation with validation, comprehensive output parsing, and direct MPI support enable seamless integration into high-throughput and multi-method workflows. We demonstrate the interface through representative applications: semi-infinite surface calculations reproducing Rashba-split Au(111) surface states; one-step photoemission modeling capturing matrix-element effects; exchange-parameter extraction for atomistic spin dynamics; and X-ray absorption spectroscopy including magnetic circular dichroism. Beyond these demonstrations, ASE2SPRKKR is designed with transferability as a first-class concern. By grounding its architecture in FAIR principles of Findability, Accessibility, Interoperability, and Reusability, it establishes a replicable blueprint for bringing other specialized Green's function and first-principles codes into the collaborative, reproducible workflows that modern materials discovery requires.

---

### 2. Domain-Gated Latent Diffusion: Generative Inverse Design of HMX-Class Energetic Materials with First-Principles Validation

**Authors:** Yehudit Aperstein, Alexander Apartsin

**Published:** 2026-05-26

**Category:** physics.chem-ph

**ID:** 2605.26540v2

**Link:** [https://arxiv.org/abs/2605.26540v2](https://arxiv.org/abs/2605.26540v2)

**Summary:** Energetic materials power mining, demolition, propulsion and airbags, yet today's compounds were designed decades ago. A successor must combine high energy release, low sensitivity to accidental initiation and a practical synthesis route, found within an astronomically large molecular space. Generative models are the natural search tool, but their training data are mostly untrustworthy: of approximately 66,000 molecules with recorded properties, only approximately 3,000 were measured or computed from first principles. Models trained on all of them imitate the rough estimates and propose molecules that collapse under real physics. We introduce Domain-Gated Latent Diffusion (DGLD), a diffusion model that treats data reliability as an explicit design parameter: labels are sorted into four trust tiers, and only trustworthy ones steer generation, while the unreliable majority still teaches the model what a plausible molecule looks like. Learned controls tune performance, safety and viability independently, and every proposal passes a four-stage screen ending in a quantum-chemical DFT audit. DGLD proposes 10 molecules unknown to PubChem that survive this screen. The best, 3,4,5-trinitro-1,2-isoxazole, matches the benchmark explosives HMX and PETN in calculated detonation performance, is unlike molecules in its training set, and has a four-step synthesis route. Trust gating is chemistry-independent and can be applied wherever abundant weak data surround a reliable core.

---

<!-- ARXIV_PAPERS_END -->
