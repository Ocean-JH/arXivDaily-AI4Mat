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

*Last checked: 2026-10-27 09:07:29 (SGT)*

### 1. TCSP3.0: Template-Based Crystal Structure Prediction with Coefficient-Preserving Element Substitution and Structural Diversity

**Authors:** Ying Feng, Jeffrey Hu, Lai Wei, Liang Tao, Madeline Miklos, Dipannoy Das Gupta, Hossein Erfanshekooh, Jianjun Hu

**Published:** 2026-10-25

**Category:** cond-mat.mtrl-sci

**ID:** 2610.34029v1

**Link:** [https://arxiv.org/abs/2610.34029v1](https://arxiv.org/abs/2610.34029v1)

**Summary:** Template-based crystal structure prediction (CSP) transfers a known crystal structure to a new composition by element substitution, so its accuracy depends on retrieving suitable templates, mapping elements and ranking the resulting candidates correctly. Auditing the original TCSP2.0 implementation on the T180 benchmark, we found that 469 of its 2,347 selected structures (20%) have the wrong composition, caused by element mappings that ignore stoichiometric coefficients and by sequential text substitution that cascades or corrupts element symbols. We propose TCSP3.0, which enforces coefficient-preserving mappings, substitutes species simultaneously on parsed structures and validates every candidate's composition and cell. It further adds periodic-number retrieval, soft oxidation-state evidence, radius-compatibility scoring, structural deduplication, and ORB-v3 machine-learning-potential relaxation and energy ranking of its candidates, as used by deep generative CSP baselines. TCSP3.0 achieves Top-1 and Top-20 match rates of 72.2% and 90.6% on T180, compared with 28.3% and 45.6% for TCSP2.0, and a Top-20 match rate of 74.0% on a new 800-target benchmark (T800). On T180 it also outperforms PNcsp+ and deep generative models CrystalFlow and MaskGXT (Top-1 72.2% versus at most 63.9%). Even without relaxation, TCSP3.0 reaches 67.8% at Top-1 and 90.6% at Top-20 in a median of 28 s per target on two CPU cores, about ten times faster than CrystalFlow. Paired ten-arm ablations on T180 and T800 show that most of the improvement comes from the correctness fixes; structural deduplication significantly improves the Top-5 match rate, embedding-based retrieval is required for coverage, and the remaining scoring features have small or null effects.

---

### 2. Exploring Joint-Embedding Predictive Architectures for Self-Supervised Representation Learning of Powder X-ray Diffraction Patterns

**Authors:** Ming-Chiang Chang, Brian DeCost

**Published:** 2026-10-23

**Category:** cond-mat.mtrl-sci

**ID:** 2610.33310v1

**Link:** [https://arxiv.org/abs/2610.33310v1](https://arxiv.org/abs/2610.33310v1)

**Summary:** Powder X-ray diffraction (XRD) is the primary high-throughput method for resolving crystal structures, a cornerstone of materials science. As high-throughput synthesis and self-driving laboratories advance, automated XRD pattern analysis has become vital for accelerating materials discovery. However, traditional matrix factorization methods fail when lattice variations cause non-linear peak shifts. At the same time, supervised learning approaches face a combinatorial explosion when handling multi-phase mixtures. To overcome these challenges, we adopt a self-supervised Joint Embedding Predictive Architecture (JEPA) to learn representation embeddings from 1D diffraction patterns. By optimizing a masked self-prediction loss directly within the latent space, the framework captures high-level crystallographic semantics. Downstream evaluations show that lightweight attentive probes trained on frozen JEPA representations achieve space group classification and lattice parameter estimation accuracy close to much larger supervised vision transformers. Furthermore, latent probing reveals that the learned representation space naturally organizes physical transformations, isolating smooth trajectories for peak broadening. Interestingly, decoding along latent paths between single-phase crystal representations yields realistic multi-phase mixture patterns, demonstrating an emergent continuous structure learned without explicit multi-phase supervision.

---

### 3. An LLM agent for end-to-end computational materials discovery

**Authors:** Chen Yuntong, Huang Lijiang, Li Yingqi, Liu Yu, Zhao Dan, Sun Mingqi, Ju Chentian, Liu Yanbing, Li Xiao-Yan, Zhao Guobin

**Published:** 2026-08-20

**Category:** cond-mat.mtrl-sci

**ID:** 2608.20434v2

**Link:** [https://arxiv.org/abs/2608.20434v2](https://arxiv.org/abs/2608.20434v2)

**Summary:** Coordinating multi-scale tasks is an effective strategy for computational materials discovery, yet the diverse algorithms and tools involved make this process highly challenging. Here we present DREAMS, a large language model (LLM)-based agent system capable of executing the entire screening pipeline for metal-organic frameworks (MOFs). DREAMS processes a large body of MOF literature, links publications to their crystal structures, and curates them into a computation-ready database, which is then screened with progressively more expensive simulations. The promising candidates identified for separation under wet flue gas conditions all originate from independent studies. By bridging the heterogeneous stages from literature mining to high-throughput simulation, DREAMS operates across application domains and enables even non-experts to discover high-performance materials in an end-to-end, automated manner.

---

<!-- ARXIV_PAPERS_END -->
