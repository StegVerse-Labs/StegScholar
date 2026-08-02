# Funding Deadline Watch Validation Request

Purpose: trigger hosted execution of the funding deadline and active-claim watcher after installation.

Expected evidence:
- Funding Deadline Watch workflow run and job IDs;
- successful execution of `funding/tools/check_funding_deadlines.py`;
- uploaded `funding-deadline-watch` artifact and digest;
- confirmation that current PESOSE and OTF claims are active and applications are not overdue;
- no change to applicant, budget, IP, ethics, or submission authority.

This marker must not be merged after evidence is committed to the canonical handoff and deadline-watch registry.
