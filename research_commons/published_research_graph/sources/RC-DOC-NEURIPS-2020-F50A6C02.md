# RC-DOC-NEURIPS-2020-F50A6C02

## Source identity

- Title: *Avoiding Side Effects in Complex Environments*
- Authors: Alexander Matt Turner, Neale Ratzlaff, Prasad Tadepalli
- Venue: NeurIPS 2020, Advances in Neural Information Processing Systems 33
- arXiv: `2006.06547v1`
- Canonical proceedings URL: `https://proceedings.neurips.cc/paper/2020/hash/f50a6c02a3fc5a3a5d4d9391f05f3efc-Abstract.html`
- Source custody: NeurIPS proceedings / arXiv / original authors
- `authority_effect: NONE`

## Admission basis

This source is admitted under `RC-CTRL-001` because it materially extends empirical side-effect evaluation into SafeLife rather than merely sharing a conceptual safety theme. The paper contrasts AI Safety Gridworlds with SafeLife as a move from dozens to billions of states, deterministic to stochastic dynamics, preset to randomly generated environments, one to many side-effect opportunities, and immediate to delayed/chaotic effects.

The paper evaluates AUP on four SafeLife tasks using learned auxiliary-value machinery and reports task completion with many side effects avoided and modest overhead. It also states a bounded scalability limitation for state-reachability penalties: naive estimation of all reachability functions scales quadratically in state-space size.

## Bounded graph treatment

- `RC-REL-SAFELIFE-REFINES-GRIDWORLDS-001`: empirical refinement of the represented Gridworlds evaluation surface into a substantially harder environment class. It does not claim replication or correction of all Gridworlds results.
- `RC-REL-SAFELIFE-CHALLENGES-RR-SCALING-001`: mechanism-specific challenge to scalability of the represented reachability-style approach. It does not dispute the earlier toy-environment relative-reachability result.

No relation from this source establishes scientific truth, publication authority, governance authority, execution authority, reuse admissibility, or support for StegVerse IICT.
