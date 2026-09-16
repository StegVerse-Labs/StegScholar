# Published Research Graph

This directory is the source-neutral relation layer for StegVerse and external published research. It preserves document, claim, evidence, and relation identity while keeping publication/source custody external and keeping every graph document and relation at `authority_effect: NONE`.

A graph edge records bounded research lineage only. It does not establish scientific truth, causation, priority, replication, publication authority, governance authority, execution authority, or reuse admissibility. Machine-discovered relations require explicit review before admission or rejection.

## Current harder-environment empirical continuation

The sixth external exemplar is Turner, Ratzlaff, and Tadepalli, *Avoiding Side Effects in Complex Environments* (NeurIPS 2020; arXiv `2006.06547v1`; `RC-DOC-NEURIPS-2020-F50A6C02`). The paper scales Attainable Utility Preservation evaluation from toy Gridworlds into SafeLife, which represents billions of states, stochastic dynamics, randomly generated environments, many side-effect opportunities, and delayed/chaotic effects.

The graph records two bounded relations:
- `RC-REL-SAFELIFE-REFINES-GRIDWORLDS-001`: empirical refinement of environment complexity/evaluation coverage beyond the represented AI Safety Gridworlds baseline surface.
- `RC-REL-SAFELIFE-CHALLENGES-RR-SCALING-001`: mechanism-specific challenge to scalability of state-reachability penalties, based on the paper's observation that naive reachability estimation is quadratic in state-space size.

Neither relation claims full replication, scientific equivalence among AUP/relative reachability/future-task preservation, invalidation of earlier toy-environment results, or support for StegVerse IICT.

Source custody remains with NeurIPS proceedings, arXiv, and the original authors. The corresponding custody record is `sources/RC-DOC-NEURIPS-2020-F50A6C02.md`.

## Seventh-source admission threshold and screening

The next external source is intentionally held to a stronger empirical threshold. Admission requires an independently authored source that either:
- directly benchmarks at least two already represented side-effect mitigation mechanisms under the same environment/protocol; or
- independently reproduces or fails to reproduce one represented mechanism in a substantially different domain.

Quantitative side-effect and task-performance outcomes are preferred. Conceptual adjacency, a comparison involving only one represented method, or a modified related method in another gridworld-style benchmark does not satisfy this threshold by itself.

The current screening pass admitted no seventh graph source. Vamplew et al. (2021), Burden et al. (2021), Lindner et al. (2021), and Turner et al. (2020) were reviewed and rejected for this specific continuation threshold for distinct reasons recorded in `SEVENTH_SOURCE_SCREENING_NOTE.md`. The graph itself remains unchanged.

## Validation

Run the canonical Research Commons validation contract from the repository root, including `python research_commons/tools/validate_published_research_graph.py` and `python research_commons/tools/check_research_commons_control_state.py`.
