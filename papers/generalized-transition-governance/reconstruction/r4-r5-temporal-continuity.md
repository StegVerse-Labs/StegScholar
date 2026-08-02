# R4–R5 Temporal Continuity

Status: StegVerse bounded research layer.

A valid authority chain and valid reality-contact evidence do not jointly support a transition unless their validity intervals overlap at the relevant decision or execution boundary.

## Required intervals

- authority validity: delegation start through expiry or revocation;
- evidence validity: observation time through its bounded freshness limit;
- transition boundary: the specific decision or execution time being assessed.

## Outcomes

- `TEMPORAL_CONTINUITY_SURVIVES`: authority and evidence are both valid at the boundary and their subject, action, and scope bindings agree.
- `TEMPORAL_CONTINUITY_PARTIAL`: overlap cannot be reconstructed because required timestamps, expiry, freshness, or revocation timing are missing.
- `TEMPORAL_CONTINUITY_FAIL_CLOSED`: no overlap exists, evidence postdates authority expiry, authority postdates the observation without a valid continuing evidence window, revocation precedes the boundary, or timestamps conflict.

This layer does not create execution authority, certification authority, canonical R5 completion, independent verification, mathematical closure, release readiness, or archive readiness.
