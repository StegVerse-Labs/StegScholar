# Research Commons Publisher → Site Dispatch Handoff

## Purpose

Define the fail-closed boundary between Publisher publication custody, Research Commons indexing, and Site display.

## Ordered path

```text
Publisher source observation
→ Publisher catalog reconciliation
→ Research Commons registry refresh
→ canonical registry hash receipt
→ index generation
→ Commons validation
→ Site projection validation
→ dispatch request
→ Site acceptance and evidence receipt
→ activation decision
```

## Required evidence

A live dispatch request must reference:

- Publisher commit and source blob identities;
- reconciliation decisions for every divergent record;
- canonical Commons registry digest;
- Commons validation run identity;
- exact projection manifest digest;
- list of records proposed for display;
- blocked or excluded records and reasons;
- Site target and expected paths.

## Authority boundary

The following do not independently authorize public display:

- presence in Publisher;
- presence in Research Commons;
- a generated index;
- successful structural validation;
- a sharing consent;
- a payment or discount;
- a dispatch request.

Activation requires a separate Site acceptance receipt and an explicit activation decision.

## Fail-closed conditions

Dispatch must remain blocked when:

- Publisher sources have drifted beyond the pinned observation;
- a catalog discrepancy lacks a reconciliation decision;
- the Commons registry receipt is missing or stale;
- a projected record requires reconciliation;
- projection metadata overstates scientific or peer-review posture;
- required source, license, privacy, or consent evidence is absent;
- the Site acceptance surface cannot preserve provenance and posture.

## Dispatch packet

The eventual machine-readable packet should contain:

```json
{
  "packet_type": "research_commons_site_dispatch_request",
  "publisher_observation_ref": "...",
  "reconciliation_ref": "...",
  "registry_hash_ref": "...",
  "commons_validation_ref": "...",
  "projection_manifest_ref": "...",
  "requested_records": [],
  "excluded_records": [],
  "creates_activation_authority": false
}
```

## Governing statement

> Publisher controls the publication record. Research Commons controls governed indexing and reuse lineage. Site controls display acceptance. None may silently collapse the authority of the others.
