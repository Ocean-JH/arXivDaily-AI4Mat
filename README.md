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

## New Papers (6)

*Last checked: 2026-11-17 12:19:07 (SGT)*

### 1. Space Group Conditional Flow Matching

**Authors:** Omri Puny, Yaron Lipman, Benjamin Kurt Miller

**Published:** 2025-09-28

**Category:** cs.LG

**ID:** 2509.23822v2

**Link:** [https://arxiv.org/abs/2509.23822v2](https://arxiv.org/abs/2509.23822v2)

**Summary:** Inorganic crystals are periodic, highly-symmetric arrangements of atoms in three-dimensional space. Their structures are constrained by the symmetry operations of a crystallographic \\emph{space group} and restricted to lie in specific affine subspaces known as \\emph{Wyckoff positions}. The frequency an atom appears in the crystal and its rough positioning are determined by its Wyckoff position. Most generative models that predict atomic coordinates overlook these symmetry constraints, leading to unrealistically high populations of proposed crystals exhibiting limited symmetry. We introduce Space Group Conditional Flow Matching, a novel generative framework that samples significantly closer to the target population of highly-symmetric, stable crystals. We achieve this by conditioning the entire generation process on a given space group and set of Wyckoff positions; specifically, we define a conditionally symmetric noise base distribution and a group-conditioned, equivariant, parametric vector field that restricts the motion of atoms to their initial Wyckoff position. Our form of group-conditioned equivariance is achieved using an efficient reformulation of \\emph{group averaging} tailored for symmetric crystals. Importantly, it reduces the computational overhead of symmetrization to a negligible level. We achieve state of the art results on crystal structure prediction and de novo generation benchmarks. We also perform relevant ablations.

---

### 2. Nahual: A Sequence Model for Language and Atoms

**Authors:** Austin H. Cheng, Marcel Müller, Andreas Burger, Yeonghun Kang, Tsz Wai Ko, Marta Skreta, Luka Mucko, Ella Miray Rajaonson, Cher Tian Ser, Jérôme F. Gonthier, Alex Zook, Varinia Bernales, Alán Aspuru-Guzik

**Published:** 2026-11-14

**Category:** cs.LG

**ID:** 2611.19072v1

**Link:** [https://arxiv.org/abs/2611.19072v1](https://arxiv.org/abs/2611.19072v1)

**Summary:** Generative models play a rapidly growing role in the design and simulation of molecules. The most widely used applications of generative models are in large language models (LLMs), owing to the natural flexibility of language for specifying and answering queries. However, generalist LLMs do not effectively handle large sets of 3D coordinates, whereas specialist generative models of 3D molecules cannot reach the controllability afforded by language. To bridge these capabilities, we propose Nahual, a decoder-only autoregressive diffusion model for any sequence of text and 3D molecules. To enable expressive autoregression on continuous coordinates, we propose next-token diffusion, whereby a causal transformer denoises each token while attending to the clean tokens before it, without increasing context size. We train Nahual on a curated set of twelve 3D chemistry tasks ranging from microsolvation to molecular conformer search to adsorption on metal surfaces, with associated evaluation metrics and baselines. The result is a single set of end-to-end-trained weights that simultaneously performs all tasks and surpasses state-of-the-art models specialized for crystal structure prediction and property-conditional molecule generation. Our results demonstrate the viability of scaling generalist decoder-only models for native multimodal understanding and generation across language and chemistry. Code is available at https://github.com/the-matter-lab/nahual.

---

### 3. CGTransformer: A Topology-Aware Autoregressive Framework for Crystal Generation and Inverse Design

**Authors:** Zhennan Zhang, Shaobo Yu, Haoting Zhang, Yu Han, Zhiyue Guo, Junjie Wang, Hao Gao, Jian Sun

**Published:** 2026-11-13

**Category:** physics.comp-ph

**ID:** 2611.18303v1

**Link:** [https://arxiv.org/abs/2611.18303v1](https://arxiv.org/abs/2611.18303v1)

**Summary:** Autoregressive language models offer a unified route to crystal generation and inverse design, but their performance depends on how periodic structures are serialized. Symmetry equivalent and closely related crystals can receive different atomic orders under coordinate-based serialization, introducing variability unrelated to their structural connectivity. Here, we present CGTransformer (Crystal Graph Transformer), an autoregressive generative framework that addresses this challenge via a graph-embedded sorting strategy. Using quotientgraph topology and barycentric embeddings, Element Symmetry Graph (ESG) converts periodic crystal networks into topology-guided one-dimensional sequences that retain key local and symmetry-related structural information. CGTransformer achieves high generation validity and the highest single shot crystal structure prediction (CSP) match rate among the compared MP-20 baselines (63.24%), while same backbone comparisons show improved structure recovery over coordinate-based ordering. Furthermore, we demonstrate property-conditioned inverse design for wide-bandgap semiconductors, where ESG achieves a much higher stable, unique and novel (S.U.N.) rate and stronger target-property alignment than the coordinate-based baseline. These results establish topology-guided sequence construction as an effective route to improving crystal generation and property-directed design at fixed model capacity.

---

### 4. A Practitioner's Guide to Materials Theory and Computation in the Age of Big Data and Artificial Intelligence

**Authors:** Jack Yang

**Published:** 2026-11-13

**Category:** cond-mat.mtrl-sci

**ID:** 2611.18797v1

**Link:** [https://arxiv.org/abs/2611.18797v1](https://arxiv.org/abs/2611.18797v1)

**Summary:** Computational modelling has become a cornerstone of materials science, with advances in atomistic simulations, high-throughput computation, and artificial intelligence transforming how materials are understood, discovered, and designed. These developments build upon generations of theoretical innovations that have translated complex mathematical and physical principles into practical predictive tools. However, the growing diversity of computational methods presents challenges for practitioners seeking a coherent understanding of their theoretical foundations. Drawing upon the author's research experience, this monograph provides a practitioner-oriented, pedagogical overview of computational materials science, unified through the concepts of potential-energy landscapes and statistical sampling. It explores how these concepts underpin structural stability, phase behaviour, and electronic and magnetic properties, through a systematic treatment of empirical force fields, density-functional theory, many-body electronic-structure methods, statistical sampling, and property prediction. It further examines high-throughput workflows, materials databases, and the probabilistic foundations of artificial intelligence. Particular emphasis is placed on atomistic representations, graph neural networks, and generative models, highlighting the roles of symmetry, group theory, differential geometry, and stochastic processes in modern materials modelling. By connecting established physical theories with emerging data-driven approaches, this monograph offers a unified perspective on computational materials science and identifies opportunities and challenges toward physics-informed, efficient, and reliable materials discovery.

---

### 5. Crystal Structure Prediction from Search to Learning: A 30-Year Expedition

**Authors:** Jianjun Hu, Ying Feng

**Published:** 2026-11-13

**Category:** cond-mat.mtrl-sci

**ID:** 2611.17670v1

**Link:** [https://arxiv.org/abs/2611.17670v1](https://arxiv.org/abs/2611.17670v1)

**Summary:** Crystal structure prediction (CSP) determines periodic atomic or molecular arrangements from chemical composition and physical conditions. Over three decades, CSP has evolved from chemical construction and global energy optimization to hybrid approaches combining symmetry, learned potentials, adaptive search, and deep generative models. This survey reviews method, software, review, and benchmark records from 1996 to October 2026, covering inorganic and molecular crystals, including formula-conditioned diffusion, flow, and autoregressive models that preserve composition. We classify methods by candidate construction and exploration: template and discrete construction, random search, evolutionary search, swarm and differential evolution, energy-landscape exploration, adaptive machine-learning-guided search, and learned generation. We distinguish representation, relaxation, ranking, and physical qualification. Benchmarks reveal no universally dominant approach. In a 46-target leaderboard snapshot, the best-performing template method achieves higher top-1 recovery than leading generative models, but paired tests show no statistically significant differences from several generative competitors. We also audit predictions for 68 experimentally examined materials, including 52 with structures confirmed by diffraction or microscopy. Predictions for 23 of the 68 preceded experiment, mostly through first-principles global search. Within the reviewed evidence, we find no independently confirmed discovery in which a deep generative model predicted the structure before experiment. We conclude with the principal limitations of current CSP algorithms and priorities for future research.

---

### 6. Diffusion Tree Sampling for Inference Time Adaptation of Crystal Generative Models

**Authors:** Daniel T. Levy, Vineet Jain, Tara Akhound-Sadegh, Sékou-Oumar Kaba, Siamak Ravanbakhsh

**Published:** 2026-11-12

**Category:** cs.LG

**ID:** 2611.17462v1

**Link:** [https://arxiv.org/abs/2611.17462v1](https://arxiv.org/abs/2611.17462v1)

**Summary:** Diffusion-based generative models have become strong priors over plausible crystal structures, but turning that prior into promising candidates requires steering toward several conflicting properties at once. Fine-tuning is expensive and produces a new model for every new objective, while differentiable guidance is not applicable to many real-world tasks. We instead adapt these generative models at inference time using Diffusion Tree Sampling (DTS), a Monte Carlo tree search procedure over the denoising trajectory. We make two technical contributions on top of DTS that are particularly relevant for AI-for-science applications. First, we show how to use existing property-conditional generative models (e.g., models fine-tuned for classifier-free guidance) as guided proposals inside DTS, without distorting the target distribution. Second, we extend DTS to multi-objective sampling, so that a single search produces samples spanning an entire Pareto front. We instantiate both adaptations on de novo crystal generation: improving the stability of crystals generated by different models, using pretrained conditional models to generate crystals belonging to rare space groups or with high bulk modulus, and generating crystals along a Pareto front of high dielectric constant and high bandgap materials. Across these tasks, DTS-based inference-time adaptation successfully improves model outputs without modifying the models themselves.

---

<!-- ARXIV_PAPERS_END -->
