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

## New Papers (3)

*Last checked: 2026-10-01 09:03:30 (SGT)*

### 1. Let CSP Be Your ANCHOR: Adaptive Crystal Search over Frozen Structure Priors

**Authors:** Emma Lei Hovmand, Jonas Elsborg, Melih Kandemir, Arghya Bhowmik

**Published:** 2026-09-27

**Category:** cond-mat.mtrl-sci

**ID:** 2609.33407v2

**Link:** [https://arxiv.org/abs/2609.33407v2](https://arxiv.org/abs/2609.33407v2)

**Summary:** De novo crystal generation (DNG) models decide where to search in composition space and how to generate structures with one set of weights. We argue that discovery is better served by separating the two. A crystal structure prediction (CSP) model is a physical prior that should be improved by likelihood training, while rewards, including novelty measured against the search's own history, should act on a search over compositions. We introduce ANCHOR, a GRPO composition policy trained with multi-objective rewards around a frozen CSP model, and continuous adaptive novelty (CAN), a graded novelty score against known structures and a growing discovery history. Using the frozen CSP model as a fixed ruler under one evaluator, we test where adaptation should act. Replacing DNG compositions with ANCHOR's policy on the same CSP backbone raises MSUN from 11.4% to 47.6% and SUN from 1.1% to 22.1% at 99.9% formula uniqueness. Fine-tuning DNG models directly on the same rewards instead moves their composition marginal without raising their on-hull fraction. We show that KL-regularized fine-tuning of a DNG model can only reweight chemistry the pretrained model already supports by a bounded factor, while unregularized DNG fine-tunes move toward known or less stable chemistry. Even a stability-only reward routed into ANCHOR's CSP backbone roughly halves SUN relative to the frozen backbone, whereas likelihood training on structures found during search can improve a CSP backbone. Under MatterGen's evaluation pipeline, ANCHOR raises state-of-the-art MSUN from 29.2% to 41.3%, transfers without retraining to two further CSP backbones, and reaches 47.1% after distillation into Crystalite-CSP. As with any model optimised against a potential, its on-hull rate depends on that potential.

---

### 2. Finetuning-Free Diffusion Model with Adaptive Constraint Guidance for Inorganic Crystal Structure Generation

**Authors:** Auguste de Lambilly, Vladimir Baturin, David Portehault, Guillaume Lambard, Nataliya Sokolovska, Florence d'Alché-Buc, Jean-Claude Crivello

**Published:** 2026-04-14

**Category:** cond-mat.mtrl-sci

**ID:** 2604.13354v4

**Link:** [https://arxiv.org/abs/2604.13354v4](https://arxiv.org/abs/2604.13354v4)

**Summary:** Generative diffusion models have emerged as powerful tools for the discovery of inorganic crystal structures, yet steering their sampling process toward user-defined physical and chemical objectives remains challenging. We present a computational framework that integrates adaptive constraint guidance into a pre-trained crystal diffusion model, enabling the generation of candidate structures that satisfy targeted structural and chemical requirements without model retraining. The approach incorporates differentiable constraint functions directly during sampling, providing an interpretable mechanism for expert-driven exploration of the crystal structure space. To assess the reliability of generated candidates, we introduce a multi-stage validation workflow combining descriptor-based analysis, duplicate removal, comparison with reference crystal databases, graph neural network energy prediction, and thermodynamic stability evaluation through convex-hull analysis. The framework is applied to several classes of inorganic compounds and to constraints involving atomic volume, local coordination environments, and near-neighbor structural motifs. Results demonstrate that adaptive guidance effectively redirects the sampling distribution toward structures exhibiting the desired characteristics while preserving chemical plausibility. Subsequent validation reveals which generated candidates remain viable after energetic and thermodynamic screening. The proposed methodology provides a practical and transparent strategy for incorporating expert knowledge into crystal generative models and establishes a general computational framework for constrained materials discovery.

---

### 3. Where Should Physics Enter a Molecular Crystal Generator?

**Authors:** Haocheng Tang, Junmei Wang, Wengong Jin

**Published:** 2026-09-28

**Category:** q-bio.BM

**ID:** 2609.36398v1

**Link:** [https://arxiv.org/abs/2609.36398v1](https://arxiv.org/abs/2609.36398v1)

**Summary:** Generative models make molecular crystal structure prediction fast, but their samples still exhibit geometric and packing violations. Physics can be introduced during training, post-training, or inference, yet these choices are rarely compared with the generator and physical signal held fixed. We introduce CrystAF, an all-atom crystal flow-map generation model, and use it with the UMA interatomic potential to systematically study where physics should enter. Post-training learns physical preferences directly into CrystAF, improving molecular validity and crystal packing while leaving sampling unchanged: physics is paid for once during training rather than repeatedly at deployment. In contrast, UMA relaxation is effective at repairing local clashes but makes generation 6--26$\\times$ slower, while learning from relaxed targets provides little benefit. These routes are complementary rather than competing. Physics-informed post-training first shifts the generated distribution toward more physically reasonable structures, after which inexpensive inference-time corrections further remove clashes and restore stereochemistry that the generator cannot represent. Importantly, the same post-training strategy also improves the multi-step all-atom Clari-M and rigid-body MolCrystalFlow generators, demonstrating transfer across architectures and representations. Together, our results suggest a simple principle: learn reusable physical alignment into the generator, and reserve inference-time physics for residual constraints that are better corrected than learned.

---

<!-- ARXIV_PAPERS_END -->
