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

*Last checked: 2026-10-28 08:57:37 (SGT)*

### 1. Precursor Ratio-Controlled Chloride Vacancies in Lead-Free KCuCl3-x Memristors for Forming-Free Gradual Resistive Switching and Neuromorphic Learning

**Authors:** Chinmayee Mandar Mhaskar, Sangeeta Roy Chaudhuri, Ayan Roy Chaudhuri

**Published:** 2026-10-26

**Category:** cond-mat.mtrl-sci

**ID:** 2610.35436v1

**Link:** [https://arxiv.org/abs/2610.35436v1](https://arxiv.org/abs/2610.35436v1)

**Summary:** Defect engineering of memristive materials offers a powerful strategy for regulating ionic transport and analog resistive switching required for neuromorphic computing. Here, we report a wet chemical synthesis route for chloride-vacancy (VCl) engineering in lead-free all-inorganic KCuCl3-x thin films and establish a direct correlation between defect concentration, electronic structure, transport dynamics, and neuromorphic performance. Controlled precursor-ratio variation systematically tunes the VCl concentration in KCuCl3-x thin films, driving preferential vacancy formation at the terminal chloride sites, band-gap narrowing, and enhanced electronic disorder. W/KCuCl3-x/FTO memristors exhibit stable bipolar VCM-type resistive switching, with increasing VCl concentration promoting forming-free operation. An optimal VCl concentration (~ 1.3*10^21 cm^-3) provides a balance between ionic mobility and defect controllability, resulting in highly linear potentiation/depression characteristics and superior pulse endurance (&gt;104 cycles). When the experimentally measured conductance characteristics of the optimized memristor are implemented as synaptic weights in artificial neural network simulations, recognition accuracies of 98.96% and 91.82% are achieved on the MNIST and Fashion-MNIST datasets, respectively. These findings establish precursor ratio-controlled VCl engineering as an effective strategy for simultaneously optimizing ionic transport, analog switching, and neuromorphic learning in lead-free halide perovskite memristors, providing a general materials design principle for energy-efficient neuromorphic electronics.

---

### 2. SymADiT: Symmetry-Aware Crystal Generation with Latent Flow Matching

**Authors:** Anmar Karmush, Cedric Mathieu Brandenburg, Soheil Ershadrad, Johanna Rosen, Michael Felsberg, Filip Ekström Kelvinius

**Published:** 2026-05-11

**Category:** cs.LG

**ID:** 2605.10115v2

**Link:** [https://arxiv.org/abs/2605.10115v2](https://arxiv.org/abs/2605.10115v2)

**Summary:** Tackling the task of crystal generation, we aim to enhance the previously proposed, symmetry-agnostic, All-atom Diffusion Transformer (ADiT) by introducing SymADiT, a symmetry-aware variant. To do so, we use a representation of crystals based on Wyckoff positions. We follow ADiT and perform generative modelling in latent space, adapted to our symmetry-aware representation. By forcing the output of the generative model to adhere to the symmetry restrictions imposed by the generated crystal's space group and each atom's Wyckoff position, the generated crystals exhibit more realistic symmetry properties. We benchmark our method against both symmetry-aware and symmetry-agnostic models for crystal generation and show competitive performance, generating stable, symmetric, and physically plausible crystals with only an off-the-shelf Transformer architecture. Our code is available at https://github.com/Karmush21/SymADiT.

---

### 3. From Autonomous Knowledge Generation to Generalizable Property Prediction: A Precision-First Pipeline for Electro-Optic Materials Discovery

**Authors:** Dibakar Datta

**Published:** 2026-10-25

**Category:** cond-mat.mtrl-sci

**ID:** 2610.34628v1

**Link:** [https://arxiv.org/abs/2610.34628v1](https://arxiv.org/abs/2610.34628v1)

**Summary:** Electro-optic materials, whose refractive index changes linearly with an applied electric field (the Pockels effect), set the speed and energy of optical modulators and microwave-to-optical links for quantum computing. Designing better materials requires optimizing composition alongside temperature, strain, and bias field. However, general repositories lack electro-optic tensor data. We present a pipeline that builds such a database from literature following the rule: "no value is better than a wrong value." The pipeline has five stages: physics-aware acquisition, layout-aware extraction via LLM and deterministic table parsers, a three-tier verification gate, cross-paper consensus using median and median absolute deviation, and a noise-robust surrogate model audited by leave-one-material-out (LOMO) testing. Physics enters directly: notation is mapped, point-group symmetry-forbidden Pockels components are rejected, equivalent labels are merged, and values carry provenance tags. In a run over 49 publications, the gate processed 816 candidates into 414 accepted, 215 held for review, and 187 rejected. Against a hand-certified gold standard of 303 values from 16 papers, the run achieved a precision of 0.51 and recall of 0.48 for exact record matches. Across four database snapshots, held-out materials where the surrogate model beat a predict-the-mean baseline grew from 1 of 4 to 9 of 13 as the database expanded from 10 to 22 materials. While not a controlled comparison, this trend supports the premise that a precision-oriented, physics-checked database can power forward models beyond its training set and clarifies requirements for inverse material design.

---

<!-- ARXIV_PAPERS_END -->
