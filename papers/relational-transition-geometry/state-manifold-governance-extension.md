# RTG State-Manifold Governance Extension

Status: research-formalism integration draft bound to `Admissible-Existence/AE:AE-AUTO-0011`. This note does not claim universal physical law.

## Resolution-indexed relational transition

For a manifold `M`, let `C_rho(M)` be the causal relation established by evidence available at observation resolution `rho`. RTG records

`tau_rho = (x, C_rho, y)`

only when `(x,y) in C_rho(M)`. Co-membership of `x` and `y` in separate snapshots does not establish `tau_rho`.

An admissible refinement `rho' >= rho` may expose a chain

`x -> z_1 -> ... -> z_n -> y`.

The refinement is required to preserve the coarse projection when it represents the same causal relation:

`F_(rho'->rho)(tau_rho') = tau_rho`.

This is a projection condition, not a claim that the finer representation contains no additional independent transitions.

## Relational ledger consequence

The comparative event ledger becomes resolution-aware:

`Lambda_(k,rho) = ({S_i^-}, Theta_(k,rho), kappa_k, {S_i^+}, correlations_(k,rho))`.

A finer ledger may add intermediate transition entries and correlations while preserving the established source-to-target relation under the declared projection. Reconstruction sufficiency is therefore distinct from transition identity: a ledger may establish `x -> y` without uniquely reconstructing every intermediate state.

## Governance as a separate relational coordinate

RTG transition geometry and governance admissibility are not the same relation. Let `N` be a manifold causally capable of constraining transitions of target manifold `M`. Define

`T_1(M)` = first-order transitions realizable under operative reality,

`T_(N->M) subseteq T_1(M)` = transitions permitted by the higher-order constraint relation induced by `N`.

For observed `tau`, first-order realization is witnessed by

`tau in T_1(M)`.

Higher-order governance may nevertheless satisfy

`tau notin T_(N->M)`.

RTG must retain both facts: the transition occurred as a causal relation and a higher-order governor classified/restricted it.

## No implicit trajectory contamination

For trajectory `P=(tau_1,...,tau_n)`, RTG imposes no default rule

`A_N(tau_i)=0 => A_N(tau_j)=0` for `j != i`.

A descendant-taint rule is represented explicitly by an additional lineage relation `L_N`. This permits a trajectory to contain a governance-restricted transition followed by another transition that is independently admissible under the same governor.

## Constraint graph

Governance topology is represented as a directed graph `G=(V,E)` whose vertices are state manifolds and whose edges encode causal constraint capacity. Ordinal labels such as first-, second-, or third-order describe the relation topology; they do not by themselves establish precedence. A precedence rule is another explicit relation.

## Classification versus enforcement

A governance classification `Q_N(tau)` is evidentiary unless a causal intervention operator changes the target manifold's reachable transition set. RTG therefore distinguishes:

- classification ledger entry;
- intervention transition;
- changed reachable-set evidence;
- realized target transition.

This distinction applies to `ALLOW`, `DENY`, `REVIEW`, and `FAIL_CLOSED`. `FAIL_CLOSED` is represented as a realized response transition such as `pending -> quarantined`, not absence of state transition.

## Cross-formalism obligations

- TT must classify transition blocks without implicit lineage taint.
- STCM receipts must retain observation resolution and governor identity separately.
- GTG reconstruction must distinguish causal reconstruction from governance admissibility reconstruction.
- StegCore planners may propagate explicit dependency/bundle constraints but not infer causal contamination where no relation is declared.
- RTG-Tests must independently challenge the projection, no-taint, and classification/enforcement invariants.

The full proof obligations and falsification conditions remain owned by AE-AUTO-0011; this document is the StegScholar integration surface rather than a competing source formalism.
