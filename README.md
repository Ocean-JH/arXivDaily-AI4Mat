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

## Latest Papers (2)

_No new papers were found in the latest check; showing the most recent additions._

*Last checked: 2026-11-06 09:58:57 (SGT)*

### 1. AMGenC: Generating Charge Balanced Amorphous Materials

**Authors:** Yan Lin, Jilin Hu, N. M. Anoop Krishnan, Morten M. Smedskjaer

**Published:** 2026-04-30

**Category:** cs.LG

**ID:** 2604.27613v2

**Link:** [https://arxiv.org/abs/2604.27613v2](https://arxiv.org/abs/2604.27613v2)

**Summary:** Amorphous (disordered) materials require simulation cells with at least hundreds to thousands of atoms to accurately capture their diverse local atomic environments, compared to crystalline materials that can be described by unit cells containing a few to hundreds of atoms. To advance the design of amorphous materials with desired properties and facilitate the exploration of their vast design space, generative inverse design has emerged as a promising approach. It aims to directly output materials with properties closely aligned with the desired ones using probabilistic generative models conditioned on desired properties, which can be more resource efficient than the traditional trial-and-error approach. However, due to the inherent stochasticity of probabilistic generative models, when element assignments are unconstrained, a large portion of generated materials may be charge unbalanced, and existing methods either fix the composition in advance or discard charge unbalanced samples after generation. In this work, we propose AMGenC, a new generative inverse design method for amorphous materials that can guarantee the generation of formally charge balanced samples, with minimal additional computational overhead and without sacrificing inverse design accuracy. AMGenC achieves this through an element noise that gives the generation process a starting point centered around charge balance, and the combination of a per-step soft projection and a final discrete projection for steering the elements toward exact charge balance throughout the generation. We perform extensive experiments on two amorphous materials datasets. Experimental results provide evidence that AMGenC achieves its design goal.

---

### 2. Physics-Informed and Knowledge-Driven Generative AI for Autonomous Discovery of Porous Oxide Energy Materials: Opportunities and Challenges

**Authors:** Dibakar Datta

**Published:** 2026-08-03

**Category:** cond-mat.mtrl-sci

**ID:** 2608.02858v2

**Link:** [https://arxiv.org/abs/2608.02858v2](https://arxiv.org/abs/2608.02858v2)

**Summary:** The discovery of next-generation energy-storage materials is increasingly limited by the complexity of the underlying design problem rather than by computational capability alone. Porous transition-metal oxides represent a particularly challenging class of battery materials because their performance emerges from coupled interactions among crystal chemistry, pore architecture, ion transport, electrochemistry, electro-chemo-mechanics, synthesis, manufacturing, and battery-system operation. Recent advances in generative artificial intelligence (AI) have demonstrated remarkable capabilities for generating chemically plausible crystal structures. However, current approaches remain largely focused on crystallographic validity and thermodynamic stability. This perspective presents a roadmap for advancing generative AI beyond crystal generation toward physics-informed, application-aware, and synthesis-aware inverse design. Using porous oxide electrodes as a representative materials platform, we propose a seven-tier physics-informed inverse-design framework integrating chemistry, thermodynamics, transport, electrochemistry, durability, cell compatibility, and manufacturability. We further identify the "Missing Data Problem" as a fundamental bottleneck limiting application-aware AI and introduce an autonomous knowledge-generation framework supported by a Porous Oxide Energy Materials Ontology and a continuously evolving "Knowledge Base". Together, these concepts establish the foundation for Synthesis-Aware, Closed-Loop Autonomous Discovery, providing a general framework for AI-enabled autonomous materials discovery across energy-storage materials and other functional materials.

---

<!-- ARXIV_PAPERS_END -->
