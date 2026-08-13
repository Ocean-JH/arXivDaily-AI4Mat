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

*Last checked: 2026-08-14 06:38:09 (SGT)*

### 1. Planar Symmetric Pattern Generation

**Authors:** Ning Lin, Luxi Chen, Huaguan Chen, Jiacheng Cen, Chongxuan Li, Wenbing Huang, Hao Sun

**Published:** 2026-06-01

**Category:** cs.LG

**ID:** 2606.02073v2

**Link:** [https://arxiv.org/abs/2606.02073v2](https://arxiv.org/abs/2606.02073v2)

**Summary:** Generating objects with specific symmetries is essential in various real-world scenarios. However, adapting existing 2D continuous representations to enforce planar group symmetry remains a challenge, as the transformation of non-reflective group elements may disrupt continuity. To overcome this limitation, we propose a symmetrization framework for arbitrary planar groups. Our method transforms any 2D continuous representation into a symmetric one while preserving continuity. We provide the mathematical formulation of this representation, demonstrate its approximation capability for symmetric functions, and detail the construction methodology. We validate our approach through three visual design tasks (pattern design, paper-cutting design and stylized topology design) and one material design task. Experiments confirm that our representation enables effective symmetry control and demonstrate its broader applicability.

---

### 2. Two-Stage Deformable-Convolutional Inverse Design of Nanophotonic Absorbers from Optical Spectra

**Authors:** Waleed Waseer, Muhammad Shahid Jabbar, Muhammad Sohail Ibrahim, Shujaat Khan

**Published:** 2026-08-12

**Category:** physics.optics

**ID:** 2608.11860v1

**Link:** [https://arxiv.org/abs/2608.11860v1](https://arxiv.org/abs/2608.11860v1)

**Summary:** Data-driven inverse design enables efficient generation of nanophotonic structures with prescribed optical responses, but spectrum-to-geometry mapping remains challenging due to non-uniqueness and fine geometric features. This work presents a two-stage deformable-convolutional framework for reconstructing metal--insulator--metal resonator geometries from 80-dimensional absorption spectra. The spectrum is projected to a $150\\times4\\times4$ latent representation and decoded into a $64\\times64$ resonator mask. Training combines supervised reconstruction with least-squares adversarial refinement initialized from the best supervised checkpoint. A three-run ablation compares deformable convolution with plain convolution, involution, Dynamic Conv, and ODConv under the same architecture. The proposed model achieves $20.79\\pm0.31$~dB PSNR and $0.8501\\pm0.0082$ SSIM, improving over plain convolution by 2.16~dB and 0.0831, respectively. It further achieves Dice $0.9623\\pm0.0027$, IoU $0.9342\\pm0.0038$, and boundary F-score $0.9550\\pm0.0027$. Spectral consistency evaluated using a frozen forward surrogate yields RMSE $0.0805\\pm0.0013$ and $R^2=0.7923\\pm0.0065$. Learned offsets show stronger adaptive sampling at coarse and intermediate decoder stages. Overall, deformable sampling with supervised initialization and adversarial refinement improves spectrum-conditioned geometry reconstruction.

---

<!-- ARXIV_PAPERS_END -->
