# StegVerse R4 Authority-Reconstruction Challenge Corpus

## Purpose

This StegVerse-owned challenge corpus keeps development moving while the independent FACTORY-R4 observation remains unchanged. It does not replace the canonical GTG R4 contract or independent validation factory.

## Bounded role

The corpus tests whether an authority-reconstruction claim survives adversarial variations in time, scope, delegation, revocation, consent, standing, and conflicting sources.

## Required challenge classes

1. current scope-matched delegation;
2. expired delegation;
3. revoked delegation;
4. missing revocation history;
5. conflicting canonical authority sources;
6. scope mismatch;
7. subject mismatch;
8. consent without authority;
9. standing without delegation;
10. prior approval after policy or authority change.

## Outcomes

- `CHALLENGE_SURVIVES`: the bounded authority reconstruction remains internally coherent under the declared challenge.
- `CHALLENGE_PARTIAL`: required evidence is missing or temporally unresolved.
- `CHALLENGE_FAIL_CLOSED`: the challenge defeats the authority claim.

No result creates execution authority, certification, legal authority, mathematical closure, independent verification, release readiness, or archive readiness.
