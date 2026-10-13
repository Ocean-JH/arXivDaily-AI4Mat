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

*Last checked: 2026-10-13 10:49:50 (SGT)*

### 1. Necessary conditions for benchmarking next-generation AI in materials discovery

**Authors:** Daniel E Widdowson, Tatiana V Kurlina, Olga D Anosova, Vitaliy A Kurlin

**Published:** 2026-10-09

**Category:** cond-mat.mtrl-sci

**ID:** 2610.13885v1

**Link:** [https://arxiv.org/abs/2610.13885v1](https://arxiv.org/abs/2610.13885v1)

**Summary:** Current AI predicts materials by speeding up energy minimisation and training on large databases. However, scaling data generation prevents manual analysis by domain experts. If novelty is evaluated by chemical compositions or traditional representations in Crystallographic Information Files, or standard structure matchers based on manually chosen thresholds, one can easily generate millions of ``new'' compositions or files without discovering truly novel materials.   This paper uses a hierarchy of crystal invariants to continuously trace and quantify structural novelty based on the new mathematical definition of a crystal structure and asymptotic guarantees for invariant descriptors. The invariant-based analysis through cascade computations on a modest computer exposes the unexpected scale of duplication in the world's largest materials databases, shown here in the high-profile case of GNoME datasets. To prevent current ``embarrassment of over-prediction'', we propose necessary conditions for next-generation AI that should be automatically enforced before claiming any new materials.

---

### 2. Doubly Metastable Synthesis for Accelerated Quantum Materials Discovery

**Authors:** Kyuho Lee, Berit H. Goodge, Soonhyun Kwon, Yash Anand, Theo Manev, Maximilien F. Debbas, Weiliang Luo, Takehito Suzuki, Heather J. Kulik, Joseph G. Checkelsky

**Published:** 2026-10-09

**Category:** cond-mat.mtrl-sci

**ID:** 2610.13859v1

**Link:** [https://arxiv.org/abs/2610.13859v1](https://arxiv.org/abs/2610.13859v1)

**Summary:** New physics emerges from new materials, which in turn rely on the development of new synthesis techniques. Identifying the enlargement of metastable synthesis window as enabling for realizing novel materials, we develop diffusion-activated epitaxy, a technique which combines two metastable synthesis methods of diffusion and epitaxy. We observe that within a narrow window of investigated synthesis space we can experimentally identify the stabilization of four distinct phases, three of which show X-ray diffraction and scanning transmission electron microscopy characterization data that are incompatible with the crystal structures registered in experimental and computational inorganic structure databases. These results suggest an enlarged metastable synthesis window is enabled by this synthesis approach, identifying doubly metastable synthesis as a promising method for exploration of quantum materials.

---

### 3. Predictive Synthesis of MOFs and COFs

**Authors:** Bin Feng, Reid A. Coyle, Shyam Chand Pal, Peter Walther, Saeun Park, Zhiling Zheng

**Published:** 2026-10-08

**Category:** physics.chem-ph

**ID:** 2610.12739v1

**Link:** [https://arxiv.org/abs/2610.12739v1](https://arxiv.org/abs/2610.12739v1)

**Summary:** Predictive synthesis concerns the prospective modeling of how a targeted structure can be realized. The synthesis of metal-organic frameworks (MOFs) and covalent organic frameworks (COFs) intrinsically involves a multidimensional space of interdependent variables, posing a challenge for bench chemists to parameterize and predict. In this Perspective, we discuss the evolution from chemical-intuition-driven experimentation toward the integration of artificial intelligence (AI) and machine learning (ML) in the laboratory. By virtue of prior knowledge, uncertainty, and experimental failure in determining what should be attempted next, we envision predictive synthesis progressing from static recipe recommendation toward real-time control and transferable principles of framework formation. In this context, the significance lies in transforming trial-and-error practice into a means of measurable chemical reasoning, thereby accelerating crystalline materials discovery and advancing synthetic chemistry.

---

<!-- ARXIV_PAPERS_END -->
