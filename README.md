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

## New Papers (3)

*Last checked: 2026-09-11 07:43:08 (SGT)*

### 1. uFlowCSP: Crystal Structure Prediction using Mean flow generative models

**Authors:** Sourin Dey, Dipannoy Das Gupta, Lai Wei, Sadman Sadeed Omee, Jianjun Hu

**Published:** 2026-09-09

**Category:** cond-mat.mtrl-sci

**ID:** 2609.09799v1

**Link:** [https://arxiv.org/abs/2609.09799v1](https://arxiv.org/abs/2609.09799v1)

**Summary:** Crystal structure prediction (CSP) is fundamental to computational materials discovery. Generative models including CDVAE, DiffCSP, FlowMM, and CrystalFlow learn stable-crystal distributions directly, but diffusion and flow-matching inference requires tens to thousands of sequential network evaluations per candidate.   We introduce uFlowCSP, a MeanFlow-based CSP model that learns the average, rather than instantaneous, probability-flow velocity. It generates a complete structure in one to five evaluations, delivering 5x-58x faster inference with equal or better performance. A chemistry- and symmetry-aware Transformer uses canonical atom ordering, global composition, and per-token chemistry embeddings. A coarse crystal-system token is used only during training; it provides additive gains, particularly improving space-group agreement despite being absent at inference, which remains formula-only.   On MP-20 with 20 candidates per target, one step matches CrystalFlow (78.38% vs. 78.34%) with 100x fewer evaluations and about 10x lower wall-clock time. Five steps reach 83.64%, exceeding CrystalFlow (78.34% at 2,000 evaluations) and DiffCSP (77.93% at about 20,000), while using 20x fewer evaluations. uFlowCSP generates 10,000 structures in 0.39-1.31 minutes, versus 6.5 for CrystalFlow and 76.1 for DiffCSP. Under CSPBench's energy-ranked top-five structure-and-space-group criterion, five-step uFlowCSP reaches 72%/72%/65% structure, space-group, and consensus match rates. CrystalFlow reaches 78%/73%/68% at 100 steps but falls to 49%/32%/31% at five. Thus, uFlowCSP improves accuracy per network evaluation, not merely peak accuracy.

---

### 2. Synthesizability Prediction of Crystalline Structures with Structure-Aware Feature Learning and Uncertainty Quantification

**Authors:** Danial Ebrahimzadeh, Sarah Sharif, Yaser Mike Banad

**Published:** 2025-10-22

**Category:** cond-mat.mtrl-sci

**ID:** 2510.19251v2

**Link:** [https://arxiv.org/abs/2510.19251v2](https://arxiv.org/abs/2510.19251v2)

**Summary:** Predicting which hypothetical inorganic crystals can be experimentally realized remains a central challenge in accelerating materials discovery. SyntheFormer is a positive-unlabeled framework that learns synthesizability directly from crystal structure, combining Fourier-transformed crystal properties (FTCP) representation with structure-aware feature extraction, Random-Forest feature selection, and a compact deep MLP classifier. The model is trained on historical data from 2011 through 2018 and evaluated prospectively on future years from 2019 to 2025, where the positive class constitutes only 1.02 percent of samples. Under this temporally separated evaluation, SyntheFormer achieves a test AUC of 0.735, AUPRC of 0.099 and 97.6 percent recall at 94.2 percent coverage with dual-threshold calibration. Direct prospective validation supports this result as two materials that were unlabeled at the time of data curation, Y6Fe(SiS7)2 and BaYb2F8, were assigned high SyntheFormer scores (0.961 and 0.753, respectively) and were subsequently reported experimentally. Crucially, the model recovers experimentally confirmed metastable compounds that lie far from the convex hull and simultaneously assigns low scores to many thermodynamically stable yet unsynthesized candidates, demonstrating that stability alone is insufficient to predict experimental attainability.

---

### 3. Atomistic Modeling of Chemical Disorder in Materials: Bridging Conventional Methods and AI-Assisted Approaches

**Authors:** Jiayu Peng, Peichen Zhong

**Published:** 2026-05-18

**Category:** cond-mat.mtrl-sci

**ID:** 2605.19124v2

**Link:** [https://arxiv.org/abs/2605.19124v2](https://arxiv.org/abs/2605.19124v2)

**Summary:** Chemical disorder, originating from the mixed occupation of crystallographic sites by multiple elements, is widespread in alloys, ceramics, and compositionally complex materials, where short- and long-range orderings strongly influence properties. A central obstacle is the representation gap between experiments and simulations: experiments often report disorder as partial occupancies and ensemble-averaged behaviors, whereas atomistic simulations and AI workflows usually require fully specified configurations. Tackling this gap requires computational methods that convert averaged disorder descriptions into representative configurational ensembles while balancing cost, bias, and fidelity. This challenge has become more urgent in AI-driven computational discovery, where ignoring disorder may cause AI workflows to misrank stability, misjudge novelty, and misdirect experiments with too-idealized representations. This Review highlights how conventional and AI-driven methods can bridge this representation gap. We assess the strengths and limitations of approaches spanning mean-field theories, cluster expansion, quasi-random approximations, Monte Carlo, and emerging schemes powered by universal interatomic potentials and generative models. We further highlight how AI can accelerate various computational schemes by lowering the cost of microstate evaluation, configurational exploration, and atomistic-to-thermodynamic closure. We also emphasize how AI can enable disorder-native capabilities, including workflow triage, ordering-sensitive and alchemical representations, generative models of disordered structures and distributions, and kinetics-aware disorder prediction. Together, this framework outlines a practical roadmap toward disorder-native AI, which can transform chemical disorder from a representational obstacle into a controllable variable for realistic AI-accelerated materials discovery.

---

<!-- ARXIV_PAPERS_END -->
