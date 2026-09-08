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

## New Papers (1)

*Last checked: 2026-09-09 07:49:43 (SGT)*

### 1. GEWUM: General Exploration Workflow for the Utopia of Materials: A Unified Platform for Automated Structure Generation, Selection, and Validation

**Authors:** Jiexi Song, Aixian She, Changpeng Song, Diwei Shi, Fengyuan Xuan, Chongde Cao

**Published:** 2026-04-23

**Category:** cond-mat.mtrl-sci

**ID:** 2604.21401v2

**Link:** [https://arxiv.org/abs/2604.21401v2](https://arxiv.org/abs/2604.21401v2)

**Summary:** The fragmented landscape of existing computational tools often hinders the seamless integration of large-scale structure prediction with rigorous stability validation. To address this, we present GEWUM (General Exploration Workflow for the Utopia of Materials), an open-source platform that integrates the Selective Random Structure Search (SRSS) strategy with universal Machine Learning Interatomic Potentials (uMLIPs) to automate and accelerate materials discovery. With native support for SLURM-based HPC clusters, GEWUM unifies the entire workflow from structure generation and diversity-preserving selection to thermodynamic/dynamic stability assessments and property calculations. The platform further incorporates built-in visualization tools, including Sankey diagrams for space-group evolution, violin plots for energy distributions, and t-SNE/UMAP embeddings for structural diversity, enabling intuitive interpretation of screening results. We demonstrate GEWUM through three case studies: low-energy polymorph prediction in Al-Sc-N, identification of a P-62c phase of U3Si5, and high-pressure structure prediction of ThH10 at 150 GPa. Benchmark tests confirm reasonable agreement in thermophysical property predictions.

---

<!-- ARXIV_PAPERS_END -->
