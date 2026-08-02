# Research Commons Hosted Validation Receipt

## Identity

```text
workflow: Build and validate Research Commons
run_number: 19
run_id: 30743296790
head_branch: rc/hosted-validation-receipt
head_sha: 2eb5a024dca537c02cf1dc65b1c4b4a37e6c78a4
pull_request: 39
job_id: 91484432172
job_name: validate
workflow_conclusion: success
artifact_id: 8832017929
artifact_name: research-commons-validation
artifact_digest: sha256:ad1b972edb6d7913e3fc6c017b22cf0e451bfba0534fc321e05cdcc5a39b5c87
```

## Inspected job results

All required steps completed successfully:

1. checkout;
2. Python 3.12 setup;
3. parse all 16 Research Commons JSON files;
4. build deterministic indexes and registry receipt;
5. validate Publisher-paper registry;
6. detect duplicate records;
7. validate Site projection boundary;
8. build fail-closed Site dispatch packet;
9. validate Research Commons control state;
10. upload generated validation artifacts.

## Inspected artifact

The downloaded artifact contained:

```text
indexes/publisher-papers/categories.json
indexes/publisher-papers/knowledge-postures.json
indexes/publisher-papers/publisher-statuses.json
projection/site-projection-dispatch-packet.json
reports/duplicate-detection.json
sources/publisher-papers/registry-hash-receipt.json
```

Observed results:

```text
Publisher-paper registry validation: PASS
entries: 5
relations: 9
duplicate detector state: COMPLETE
exact record duplicates: 0
normalized title duplicates: 0
registry digest: db1c30c62e09cd84c684a15d584bdfd7ce403ea54291ac9d3448bad0ae063149
dispatch state: BLOCKED
authority effect: NONE
```

The dispatch packet correctly retained these blockers:

```text
projection_manifest_not_authorized
sv-gcat-bcat-admissibility-2026: blocked_pending_source_reconciliation
sv-god-framework-2026: blocked_pending_complete_source_record
```

## Validation interpretation

This receipt proves hosted structural and deterministic validation of the current Research Commons control surface. It does not prove Publisher reconciliation, Site acceptance, deployment, public-path accessibility, scientific validity, publication authority, reuse admissibility, or governed activation.

## Claim disposition

The session-specific hosted-validation claim is complete and may be released. Remaining work is repository-native or dependency-blocked under `RESEARCH_COMMONS_MIRROR_HANDOFF.md`, `research_commons/control/task-registry.json`, issue #37, issue #38, and issue #21.
