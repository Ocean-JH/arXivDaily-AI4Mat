# ArXiv Daily - AI4MAT

**Daily automatic updates of the latest arXiv papers on AI for Materials Science (AI4MatSci).** 

Stay informed with cutting-edge research at the intersection of artificial intelligence and materials science — automatically!

## :bookmark: Related Fields

- (Computational) Materials Science
- Machine Learning
- Materials Design
- Crystal Structure Prediction
- Generative AI for Materials Discovery

## :star: Customize Yours

Let's start with a star :star:!

And then, feel free to adjust the `query` field in the file `config.json` to match your own research interests(see [arXiv API User's Manual](https://info.arxiv.org/help/api/user-manual.html#51-details-of-query-construction) for more information)!

## :handshake: Contributions

Contributions are welcome!
 Feel free to open an Issue or a Pull Request if you have ideas for improvement, new features, or better queries.

## :blue_heart: ​Acknowledge

Thank you to [arXiv](https://arxiv.org/) for use of its open access interoperability.

---

## :scroll: Paper List


<!-- ARXIV_PAPERS_START -->

## New Papers (2)

*Last updated: 2026-06-12 07:19:48 (SGT)*

### 1. Tensor Methods: A Unified and Interpretable Approach for Material Design

**Authors:** Shaan Pakala, Aldair E. Gongora, Brian Giera, Evangelos E. Papalexakis

**Published:** 2026-02-11

**Category:** cs.LG

**ID:** 2602.10392v2

**Link:** [http://arxiv.org/abs/2602.10392v2](http://arxiv.org/abs/2602.10392v2)

**Summary:** When designing new materials, it is often necessary to tailor the material design to have some desired properties. As the set of design parameters grow, the search space grows exponentially, making the actual synthesis and evaluation of all material combinations virtually impossible. Even using traditional computational methods such as Finite Element Analysis becomes too computationally heavy to search the design space. Recent methods use machine learning (ML) surrogate models to more efficiently determine optimal material designs; unfortunately, these methods often (i) are notoriously difficult to interpret and (ii) under perform when the training data comes from a non-uniform sampling of the design space. We suggest the use of tensor completion methods as an all-in-one approach for interpretability and predictions. We observe classical tensor methods are able to compete with traditional ML in predictions, with the added benefit of their interpretable tensor factors (which are given completely for free, as a result of the prediction). In our experiments, we are able to rediscover physical phenomena via the tensor factors, indicating that our predictions are aligned with the true underlying physics of the problem. This also means these tensor factors could be used by experimentalists to identify potentially novel patterns, given we are able to rediscover existing ones. We also study the effects of both types of surrogate models when we encounter training data from a non-uniform sampling of the design space. We observe more specialized tensor methods that can give better generalization in these non-uniforms sampling scenarios. We find the best generalization comes from a tensor model, which is able to improve upon the baseline ML methods by up to 5% on aggregate $R^2$, and halve the error in some out of distribution regions....

---

### 2. Open Materials Generation with Inference-Time Reinforcement Learning

**Authors:** Philipp Hoellmer, Stefano Martiniani

**Published:** 2026-01-31

**Category:** cs.LG

**ID:** 2602.00424v2

**Link:** [http://arxiv.org/abs/2602.00424v2](http://arxiv.org/abs/2602.00424v2)

**Summary:** Continuous-time generative models for crystalline materials enable inverse materials design by learning to predict stable crystal structures, but incorporating explicit target properties into the generative process remains challenging. Policy-gradient reinforcement learning (RL) provides a principled mechanism for aligning generative models with downstream objectives but typically requires access to the score, which has prevented its application to flow-based models that learn only velocity fields. We introduce Open Materials Generation with Inference-time Reinforcement Learning (OMatG-IRL), a policy-gradient RL framework that operates directly on the learned velocity fields and eliminates the need for the explicit computation of the score. OMatG-IRL leverages stochastic perturbations of the underlying generation dynamics preserving the baseline performance of the pretrained generative model while enabling exploration and policy-gradient estimation at inference time. Using OMatG-IRL, we present the first application of RL to crystal structure prediction (CSP). Our method enables effective reinforcement of an energy-based objective while preserving diversity through composition conditioning, and it achieves performance competitive with score-based RL approaches. Finally, we show that OMatG-IRL can learn time-dependent velocity-annealing schedules, enabling accurate CSP with order-of-magnitude improvements in sampling efficiency and, correspondingly, reduction in generation time. The OMatG-IRL code is included in a new release of the Open Materials Generation (OMatG) framework available at https://github.com/FERMat-ML/OMatG....

---


<!-- ARXIV_PAPERS_END -->