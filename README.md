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

*Last checked: 2026-08-27 10:54:36 (SGT)*

### 1. Inverse Design of Inorganic Compounds with Generative AI

**Authors:** Hannes Kneiding, Lucía Morán-González, Nishamol Kuriakose, Ainara Nova, David Balcells

**Published:** 2026-04-11

**Category:** physics.chem-ph

**ID:** 2604.11827v3

**Link:** [https://arxiv.org/abs/2604.11827v3](https://arxiv.org/abs/2604.11827v3)

**Summary:** Machine learning is revolutionizing chemistry. Beyond the value of predictive models accelerating virtual screening, generative AI aims at enabling inverse design, reversing the compound-to-property prediction paradigm into property-to-compound generation. Chemists now have access to a rich AI toolbox for organic chemistry, including drug discovery. However, the application of these methods to inorganic compounds remains limited by the challenges posed by their intrinsic nature. This Review analyzes how these challenges have been addressed, considering widely diverse systems ranging from molecules to crystals, including transition metal complexes and microporous materials. The analysis focuses on how generative AI methods have evolved towards data-representation-model pipelines that address the full complexity of inorganic compounds, including their chemical composition, geometry, symmetry, and electronic structure. Future directions, like benchmark standardization and the development of synthesizability metrics, are also discussed.

---

### 2. Interpretable physics-informed retrieval-augmented generation language model for end-to-end inorganic crystal synthesis planning

**Authors:** Wei-Jian Jiang, Ye-Nan Sha, Hui Guo, Jie Chen, Yu-Cai Liang, Ke Zhou, Qi-Long Gao, Dong-Lin Han, Xin-Gao Gong, Wan-Jian Yin

**Published:** 2026-08-26

**Category:** cond-mat.mtrl-sci

**ID:** 2608.25392v1

**Link:** [https://arxiv.org/abs/2608.25392v1](https://arxiv.org/abs/2608.25392v1)

**Summary:** Synthesis planning for inorganic materials requires predicting both synthesizability and viable routes by linking microscopic thermodynamic stability with macroscopic synthesis methods, precursors, and processing conditions. Here, we develop an interpretable Physics-Informed Retrieval-Augmented Generation Language Model (PIRAG-LM) for end-to-end inorganic crystal synthesis planning. We construct a material-centered Structured Synthesis Knowledge Base (SSKB) containing route-level records for 13,820 experimentally synthesized inorganic crystals. PIRAG-LM retrieves historical precedents using chemical, structural, and thermodynamic similarity, then employs a structured LLM reasoning module to propose routes, precursors, and processing conditions and assess thermodynamic feasibility, kinetics, and accessibility. It achieves 91.4% accuracy in synthesis-method prediction, compared with 72.1% for the LLM alone, and generalizes to materials reported after the knowledge cutoff. Because the framework relies on retrieval rather than parametric memorization, its performance can be improved by expanding the SSKB without retraining the language model. Guided by PIRAG-LM, we experimentally synthesize five new compounds: BaMo0.3In0.7O2.95, BaNb0.4In0.6O2.9, Hg[B(CN)4]2, CoCo(CN)6, and SrNb2Fe2(PO4)6, via solid-state and solution routes. These results demonstrate an interpretable machine-learning approach that helps bridge computational materials discovery and experimental realization.

---

<!-- ARXIV_PAPERS_END -->
