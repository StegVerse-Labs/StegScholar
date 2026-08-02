# NSF PESOSE 2026 Eligibility and Submission Gate

## Application

`FUNDING-NSF-PESOSE-2026-001`

## Gate posture

The proposal narrative may be developed, but submission must fail closed until every mandatory gate below has directly inspectable evidence.

| Gate | Required evidence | State | Owner | Release condition |
|---|---|---|---|---|
| Legal applicant | Formation or registration record showing exact legal name, entity type, and U.S. address | BLOCKED | Human corporate authority | Evidence reference committed or qualified lead organization recorded |
| U.S. ownership and control | Cap table, ownership declaration, or equivalent showing more than 50% eligible U.S. ownership and control | BLOCKED | Human corporate authority | Signed ownership/control evidence exists |
| Principal Investigator | Employment record or appointment establishing proposed PI as an employee of the applicant and normally resident in the U.S. | BLOCKED | Human corporate authority | PI identity and employment evidence exist |
| Legal right to work | Applicant-held employment eligibility evidence for funded personnel | BLOCKED | Human corporate authority | Required attestations or records exist |
| UEI | Active Unique Entity Identifier associated with the exact applicant | BLOCKED | Applicant registration authority | Active UEI recorded |
| SAM.gov | Active SAM.gov registration not expiring before submission | BLOCKED | Applicant registration authority | Active registration and expiration date recorded |
| Submission system | Research.gov or Grants.gov organization registration and authorized organizational representative | BLOCKED | Applicant registration authority | Submission workspace and AOR/SPO authority verified |
| Public open-source anchor | Public repository, license, current status, testing, dissemination, user and contributor evidence | REVIEW_REQUIRED | StegVerse-Labs/StegScholar | Canonical product evidence crosswalk completed |
| PI and team qualifications | Current biographical sketches, current and pending support, synergistic activities where required | NOT_STARTED | Application team | NSF-compliant personnel package completed |
| Budget | Detailed Track 1 budget and justification, including required I-Corps for PESOSE experiential activities | NOT_STARTED | StegVerse-Labs/StegFinCo | Budget authority approves final budget and justification |
| IP and disclosure | Review of proposal text against protected inventions and patent strategy | NOT_STARTED | StegVerse-Labs/StegPatents | Written disclosure classification issued |
| Project summary | NSF-compliant overview, intellectual merit, broader impacts, and final keyword line | DRAFT | StegVerse-Labs/StegScholar | Internal compliance review passes |
| Project description | Maximum seven-page Track 1 narrative covering all solicitation-specific elements | DRAFT | StegVerse-Labs/StegScholar | Content and page-limit validation passes |
| References | Complete primary-source references, including public open-source product pointer through citation | NOT_STARTED | StegVerse-Labs/StegScholar | Citation audit passes |
| Data management and sharing | NSF-compliant plan covering project data and artifacts | NOT_STARTED | StegVerse-Labs/StegScholar | Plan approved |
| Mentoring plan | Required only if postdoctoral researchers are budgeted | CONDITIONAL | Application team | Personnel plan determines requirement |
| Collaborators and affiliations | NSF-compliant document for senior/key personnel | NOT_STARTED | Application team | Format validation passes |
| Submission authorization | Final institutional approval to submit | BLOCKED | Authorized Organizational Representative | AOR releases submission |

## Machine-observable decision rule

- `SUBMISSION_READY` is prohibited while any mandatory gate is `BLOCKED`, `NOT_STARTED`, `REVIEW_REQUIRED`, or `DRAFT`.
- The application may move from `DRAFTING` to `INTERNAL_REVIEW` only after the public-product evidence crosswalk, project summary, project description, budget draft, and disclosure review exist.
- Only an Authorized Organizational Representative may move the application to `SUBMITTED`.

## Registration timing risk

The solicitation warns that SAM.gov registration may take several weeks. Registration evidence is therefore on the critical path and cannot be deferred until the narrative is complete.

## Next executable tasks

1. Build `funding/applications/active/FUNDING-NSF-PESOSE-2026-001-product-evidence.md` from current public StegVerse repositories.
2. Install an NSF Track 1 compliance checklist and page-budget map.
3. Draft the project summary and broader-impacts section.
4. Transfer budget development to StegFinCo through a committed contract.
5. Keep legal identity, UEI, SAM.gov, and AOR gates assigned to the named human authority boundary until evidence exists.
