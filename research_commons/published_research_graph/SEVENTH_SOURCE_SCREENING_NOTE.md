# Seventh-source screening record

Goal: `RC-CTRL-001`
Canonical source threshold: admit a seventh external source only if it is independently authored and either (a) directly benchmarks at least two already represented side-effect mitigation mechanisms under the same environment/protocol, or (b) independently reproduces or fails to reproduce one represented mechanism in a substantially different domain. Conceptual-only or single-method adjacency is insufficient.

Authority effect: `NONE`

## Screened candidates

### Vamplew, Foale, Dazeley, and Bignold (2021)

Title: `Potential-based multiobjective reinforcement learning approaches to low-impact agents for AI safety`
Venue: Engineering Applications of Artificial Intelligence 100 (2021) 104186
DOI: `10.1016/j.engappai.2021.104186`
Canonical URL: `https://doi.org/10.1016/j.engappai.2021.104186`
External custody: Elsevier / journal version of record / original authors
Disposition: `REJECTED_FOR_SEVENTH_GRAPH_INGESTION`

Evidence posture:
- independently authored relative to the represented Relative Reachability authors;
- contains a direct empirical comparison between the authors' potential-based TLOA method and a learned Relative Reachability variant across four benchmark environments;
- reports task and alignment/impact outcomes over repeated runs;
- however, only Relative Reachability is an already represented mitigation mechanism in that comparison;
- the comparison uses a modified learned RR implementation rather than an exact reproduction of the represented RR configuration;
- the benchmark remains gridworld-style reinforcement learning rather than a substantially different application domain.

Reason for rejection: strong empirical near-match, but it does not satisfy either frozen route: it does not benchmark two represented mechanisms, and it is not an independent reproduction/failure of the represented RR mechanism in a substantially different domain.

### Burden, Hernandez-Orallo, and O hEigeartaigh (2021)

Title: `Negative Side Effects and AI Agent Indicators: Experiments in SafeLife`
Venue: SafeAI@AAAI 2021 / CEUR Workshop Proceedings Vol. 2808
Canonical URL: `https://ceur-ws.org/Vol-2808/Paper_24.pdf`
External custody: CEUR-WS / original authors
Disposition: `REJECTED_FOR_SEVENTH_GRAPH_INGESTION`

Evidence posture:
- independently authored and empirical;
- evaluates DQN, PPO, and a uniform-random agent in SafeLife with quantitative reward, pass-rate, exploration, and side-effect metrics;
- finds non-monotonic relationships between capability/reward and side-effect scores;
- cites Relative Reachability and AUP background work but does not evaluate either represented mitigation mechanism.

Reason for rejection: empirical SafeLife evidence is relevant to negative-side-effect measurement, but it does not reproduce, fail to reproduce, or directly compare any represented mitigation mechanism.

### Lindner, Matoba, and Meulemans (2021)

Title: `Challenges for Using Impact Regularizers to Avoid Negative Side Effects`
Venue: SafeAI@AAAI 2021
arXiv: `2101.12509`
Canonical URL: `https://arxiv.org/abs/2101.12509`
External custody: arXiv / CEUR-WS / original authors
Disposition: `REJECTED_FOR_SEVENTH_GRAPH_INGESTION`

Evidence posture:
- independently authored;
- directly analyzes Relative Reachability, Attainable Utility, and future-task impact regularization;
- but the paper is an analytical/challenge survey rather than a same-protocol empirical benchmark or independent reproduction in a substantially different domain.

Reason for rejection: fails the empirical threshold.

### Turner, Hadfield-Menell, and Tadepalli (2020)

Title: `Conservative Agency via Attainable Utility Preservation`
Disposition: `REJECTED_FOR_SEVENTH_GRAPH_INGESTION`

Evidence posture:
- directly compares AUP with Relative Reachability on benchmark tasks;
- however, it is the source family that introduces AUP and therefore does not satisfy the frozen independently-authored continuation requirement.

Reason for rejection: direct comparison exists, but independence criterion fails for this continuation.

### Alizadeh Alamdari, Klassen, Toro Icarte, and McIlraith (2022)

Title: `Be Considerate: Avoiding Negative Side Effects in Reinforcement Learning`
Venue: AAMAS 2022, Main Track, pp. 18-26
Canonical URL: `https://www.ifaamas.org/Proceedings/aamas2022/pdfs/p18.pdf`
External custody: IFAAMAS proceedings / original authors
Disposition: `REJECTED_FOR_SEVENTH_GRAPH_INGESTION`

Evidence posture:
- independently authored and empirical;
- explicitly situates its approach against prior Relative Reachability, Attainable Utility Preservation, and future-task-style work;
- augments an acting agent's reward using expected future return / agency of other agents and reports qualitative and quantitative gridworld experiments;
- the experiments evaluate the authors' considerate-agent formulations rather than a same-protocol head-to-head benchmark of at least two already represented mitigation mechanisms;
- the evaluation remains gridworld reinforcement learning rather than a substantially different application domain;
- therefore it neither independently reproduces nor fails to reproduce a represented mechanism under the frozen different-domain route.

Reason for rejection: relevant independent empirical extension of side-effect avoidance toward other-agent welfare and agency, but it does not satisfy either frozen admission path.

### Adaptive querying for reward learning from human feedback (2025)

Title: `Adaptive querying for reward learning from human feedback`
Venue: Frontiers in Robotics and AI (2025)
Canonical URL: `https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1734564/full`
External custody: Frontiers journal version of record / original authors
Disposition: `REJECTED_FOR_SEVENTH_GRAPH_INGESTION`

Evidence posture:
- independently authored and empirical;
- directly frames evaluation around avoidable and unavoidable negative side effects;
- reports empirical evaluation across four simulation domains, a human-subjects simulation study, and an in-person study using a Kinova Gen3 7DoF robotic arm;
- therefore provides substantially different-domain and embodied negative-side-effect evidence relative to the represented gridworld-style literature;
- however, it evaluates adaptive human-feedback selection / reward learning rather than Attainable Utility Preservation, Relative Reachability, or future-task preservation;
- it does not reproduce or fail to reproduce any represented mitigation mechanism, and it does not directly benchmark at least two represented mechanisms under one protocol.

Reason for rejection: clears the empirical and substantially-different-domain relevance bar but fails the represented-mechanism requirement of both frozen admission routes.

### Overman and Bayati (2026)

Title: `Calibrating Conservatism for Scalable Oversight`
Venue: ICML 2026 / Stanford GSB working paper / arXiv
arXiv: `2605.28807v1`
DOI: `10.48550/arXiv.2605.28807`
Canonical URL: `https://arxiv.org/abs/2605.28807`
External custody: arXiv / Stanford Graduate School of Business / original authors
Disposition: `REJECTED_FOR_SEVENTH_GRAPH_INGESTION`

Evidence posture:
- independently authored relative to the represented AUP source family;
- experimentally evaluates Calibrated Collective Oversight in substantially different domains including MACHIAVELLI text-adventure trajectories and a modified SWE-bench software-engineering protocol, reporting both violation/misalignment rates and task/reward outcomes;
- Appendix H also implements a fixed-lambda AUP baseline using the original Q-value-style penalty structure and records both violation rate and total reward over repeated runs;
- however, that actual AUP baseline is evaluated only in a purpose-built non-stationary gridworld with species-harm dynamics;
- the MACHIAVELLI and SWE-bench experiments use the authors' generalized CCO method rather than AUP itself;
- therefore the paper does not independently reproduce or fail to reproduce AUP in the substantially different domains, and it does not directly benchmark two already represented mechanisms under one protocol.

Reason for rejection: exceptionally close empirical near-match, but the domain-diverse experiments exercise CCO rather than the represented AUP mechanism; the direct AUP comparison remains gridworld-style, so neither frozen route is satisfied.

### Nayebi (2026)

Title: `Core Safety Values for Provably Corrigible Agents`
Venue: AAAI 2026 Machine Ethics Workshop / CEUR Workshop Proceedings Vol. 4189, pp. 94-107
Canonical URL: `https://ceur-ws.org/Vol-4189/paper7.pdf`
External custody: CEUR-WS / original author
Disposition: `REJECTED_FOR_SEVENTH_GRAPH_INGESTION`

Evidence posture:
- independently authored relative to the represented AUP source family;
- defines a belief-based extension of Attainable Utility Preservation for partially observed multi-step corrigibility and preserves a stepwise inaction-style counterfactual baseline;
- extends the represented mechanism conceptually into a partially observed off-switch / corrigibility setting;
- the contribution is primarily formal: the paper proves corrigibility and safety properties rather than reporting the required empirical reproduction or failure-to-reproduce with explicit task-performance and side-effect outcomes;
- it does not directly benchmark at least two represented mechanisms under one shared empirical protocol.

Reason for rejection: materially extends AUP into a different formal setting but fails the frozen empirical requirement.

### Smith, Klassert, and Pihlakas (2023)

Title: `Using soft maximin for risk averse multi-objective decision-making`
Venue: Autonomous Agents and Multi-Agent Systems 37, article 11 (2023)
DOI: `10.1007/s10458-022-09586-2`
Canonical URL: `https://link.springer.com/article/10.1007/s10458-022-09586-2`
External custody: Springer Nature journal version of record / original authors
Disposition: `REJECTED_FOR_SEVENTH_GRAPH_INGESTION`

Evidence posture:
- independently authored relative to the represented AUP, Relative Reachability, and future-task source families;
- empirically evaluates proposed continuous non-linear multi-objective utility functions, especially SFELLA, in tabular gridworld environments including low-impact tasks inherited from Vamplew et al. and resource-balancing tasks;
- explicitly discusses conservative agency and Attainable Utility Preservation as motivating low-impact background;
- the direct head-to-head low-impact comparison is SFELLA against Vamplew et al.'s thresholded lexicographic alignment objective (TLOA), not against represented AUP, Relative Reachability, or future-task preservation;
- no Relative Reachability implementation is evaluated in the paper and AUP is not empirically exercised as a mechanism;
- all reported low-impact experiments remain simple gridworlds rather than a substantially different domain.

Reason for rejection: independent and empirical, but it benchmarks an unrepresented thresholded alignment method against the authors' new SFELLA method; it neither compares two represented mechanisms under one protocol nor reproduces/fails to reproduce a represented mechanism in a substantially different domain.

### Tong, Lu, Sun, Han, Liu, Zhao, and Zeng (2025)

Title: `Autonomous Alignment with Human Value on Altruism through Considerate Self-imagination and Theory of Mind`
Venue: arXiv preprint / author-hosted manuscript
arXiv: `2501.00320`
Canonical URL: `https://arxiv.org/abs/2501.00320`
External custody: arXiv / Beijing Normal University author-hosted manuscript / original authors
Disposition: `REJECTED_FOR_SEVENTH_GRAPH_INGESTION`

Evidence posture:
- independently authored relative to the represented AUP, Relative Reachability, and future-task source families;
- explicitly identifies Relative Reachability, Attainable Utility Preservation, and Future Task Rewards as prior approaches to avoiding negative environmental effects;
- empirically evaluates a self-imagination plus Theory-of-Mind framework across multiple Sima-Guang-style gridworld variants with explicit task completion, human-rescue, and irreversible environmental-damage tradeoffs;
- ablation experiments evaluate the authors' negative-side-effect penalty and empathy components against classic/modified DQN-style baselines;
- none of the represented AUP, Relative Reachability, or future-task mechanisms is itself implemented or empirically exercised in the reported comparison;
- the experiments remain gridworld-style rather than a substantially different domain.

Reason for rejection: independent, empirical, and explicitly connected to all three represented mechanism families, but it evaluates a new self-imagination/ToM mechanism rather than directly benchmarking two represented mechanisms or reproducing/failing to reproduce one represented mechanism in a substantially different domain.

### Miret, Majumdar, and Wainwright (2020)

Title: `Safety Aware Reinforcement Learning (SARL)`
Venue: arXiv / ICLR 2021 submission
arXiv: `2010.02846`
Canonical URL: `https://arxiv.org/abs/2010.02846`
External custody: arXiv / original authors
Disposition: `REJECTED_FOR_SEVENTH_GRAPH_INGESTION`

Evidence posture:
- independently authored relative to the represented AUP, Relative Reachability, and future-task source families;
- empirically evaluates task reward and post-episode side-effect outcomes across still and dynamic SafeLife prune/append tasks, a substantially more complex non-tabular environment than the early gridworld tests;
- explicitly discusses Relative Reachability and conservative/AUP-style work and distinguishes SARL from the AUP SafeLife extension;
- the implemented mechanism is SARL's own virtual safety agent with a distribution-distance regularizer, trained using the SafeLife side-effect information channel;
- neither AUP nor Relative Reachability nor future-task preservation is implemented as the tested mechanism or direct baseline in the reported experiments.

Reason for rejection: independent and empirical in a complex SafeLife domain, but it does not empirically exercise any represented mechanism there and therefore neither reproduces/fails to reproduce one represented mechanism in a substantially different domain nor benchmarks two represented mechanisms under one shared protocol.

## Result

No seventh external graph ingestion was admitted in these screening passes. The Published Research Graph is intentionally unchanged.

The next admissible source must clear the frozen threshold without weakening it: an independently authored same-protocol quantitative comparison of at least two represented mechanisms (preferably AUP, Relative Reachability, and/or future-task preservation), or an independent empirical reproduction/failure of one represented mechanism in a substantially different domain with explicit task-performance and side-effect outcomes. An inspired replacement method in a different domain is not sufficient unless the represented mechanism itself is empirically exercised there.

This screening record is provenance only. It does not establish scientific truth, publication authority, governance authority, execution authority, reuse admissibility, or any support for StegVerse research.
