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

## Result

No seventh external graph ingestion was admitted in this screening pass. The Published Research Graph is intentionally unchanged.

The next admissible source must clear the frozen threshold without weakening it: an independently authored same-protocol quantitative comparison of at least two represented mechanisms (preferably AUP, Relative Reachability, and/or future-task preservation), or an independent reproduction/failure of one represented mechanism in a substantially different domain with explicit task-performance and side-effect outcomes.

This screening record is provenance only. It does not establish scientific truth, publication authority, governance authority, execution authority, reuse admissibility, or any support for StegVerse research.
