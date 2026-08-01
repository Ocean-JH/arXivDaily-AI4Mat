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

**Required one-time setting:** in the repository's **Settings → Pages** screen,
select **GitHub Actions** as the publishing source. The workflow checks this
before generating or publishing anything. It uses the repository-provided token
and requires no personal access token or deployment secret.

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

## Latest Papers (1)

_No new papers were found in the latest check; showing the most recent additions._

*Last checked: 2026-08-01 16:19:47 (SGT)*

### 1. MDTransformer: A Hardware-Software Co-Design of Mode-Division Photonic Transformer Accelerator with Inverse-Designed Coherent Crossbar

**Authors:** Solomon Micheal Serunjogi, Rachmad Vidya Wicaksana Putra, Ayat Taha, Muhammad Shafique, Mahmoud Rasras

**Published:** 2026-07-28

**Category:** cs.AR

**ID:** 2607.26016v1

**Link:** [https://arxiv.org/abs/2607.26016v1](https://arxiv.org/abs/2607.26016v1)

**Summary:** Recently, photonic transformer accelerators (PTAs) have successfully achieved significant speedup and energy efficiency improvements over electronic accelerators for expediting Transformer inference. However, state-of-the-art rely on expensive multi-wavelength light generation and large dot-product units due to active phase-shifter components, thus making their approach inefficient and impractical. To address this, we propose MDTransformer, a novel hardware-software co-design of PTA based on mode-division optical dataflow and operations. Specifically, MDTransformer performs complex matrix operations using spatial-mode interference, that leverages the inverse-designed multi-mode couplers, crossings, and Mach-Zehnder IQ modulators into a compact mode-division photonic tensor core (MPTC), capable of executing matrix multiplications in the optical domain. Its each guided mode (i.e., TE0-TE3) acts as an independent computational lane, enabling four-fold parallelism-per-waveguide without spectral filtering or free-spectral-range limitations. Moreover, its coherent detection and IQ modulation jointly encode amplitude and phase, realizing complex-valued arithmetic for full-range operations in transformers. MDTransformer offers analog multiplication with sub-4-bit effective precision and inter-modal crosstalk below -30 dB. Its inverse-designed approach also offers scalable and full compatibility with single-laser continuous-wave operation at 1550 nm. Experimental results show that MDTransformer achieves 40.4% area reduction, 63.6% power saving, 40.6% energy saving, and comparable latency over the state-of-the-art PTA across different workloads (i.e., DeiT-Tiny/Small/Base and BERT-Base/Large). These results show that MDTransformer offers a practical solution for high-performance and energy-efficient transformer-based systems.

---

<!-- ARXIV_PAPERS_END -->
