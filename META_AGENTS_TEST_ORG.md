# `meta-agents-demo-test` proof boundary

## Current status

As of August 12, 2026, the exact `meta-agents-demo-test` organization is not
discoverable through the installed GitHub App and no accessible test-org
repository, workflow run, or approved runner can be verified. This is an
infrastructure/bootstrap gap, not passing E2E evidence.

The canonical control-plane production hardening is merged in
`meta-agents-demo/meta-agent-control-plane.rs` PR #40. The requested independent
E2E repository identity `meta-agents-demo/meta-agents-demo-e2e` is not present.
`meta-agents-demo/metacog-e2e` remains the explicitly labeled temporary carrier;
its draft PR #5 contains the hardened migration and bootstrap contract.

Private GitHub-hosted jobs are currently rejected before runner assignment by
the account billing/spending-limit condition. A run with `steps: null` or
`steps: []` and no runner is pre-execution infrastructure evidence only. It is
never a product-test failure or a passing result.

## Canonical topology

| Role | Exact identity |
|---|---|
| Production source | `meta-agents-demo/meta-agent-control-plane.rs` |
| Requested E2E repository | `meta-agents-demo/meta-agents-demo-e2e` |
| Temporary E2E carrier | `meta-agents-demo/metacog-e2e` |
| Isolated test organization | `meta-agents-demo-test` |
| Required test fixture | `meta-agents-demo-test/secure-env-e2e` |
| Approved runner labels | `self-hosted`, `linux`, `meta-agents-demo-e2e` |

The E2E carrier's `profile.json` and `test-org.bootstrap.json` are the
machine-readable source of truth for the candidate SHA, repository migration,
permissions, runner labels, mutation boundary, and evidence allowlist.

## Bootstrap checklist

1. Create or confirm the exact `meta-agents-demo-test` organization.
2. Install the GitHub App with bounded read access to Contents, Actions, issues,
   and pull requests. Expand permissions only through a separately reviewed
   administrative operation.
3. Create private `secure-env-e2e` with workflow permissions limited to
   `contents: read` and persisted checkout credentials disabled.
4. Create or rename the production-org E2E repository to the exact requested
   `meta-agents-demo-e2e` identity. Preserve reviewed history and do not create a
   second competing carrier.
5. Register an approved Linux runner with every required label. Do not expose a
   privileged Docker socket to untrusted pull requests.
6. Pin the reusable workflow reference and `candidate_sha` to the same reviewed
   40-character control-plane commit.
7. Run the source-owned Nix + Just + `ores-sops` synthetic round trip, including
   the no-identity decryption refusal and guaranteed `env/dec` creation.
8. Build and run the exact production candidate with synthetic values; verify
   non-root execution, read-only root, dropped capabilities,
   `no-new-privileges`, health/readiness, protected reads, and clean shutdown.
9. Run OpenAI and Anthropic doctor checks separately on a trusted host using
   protected key files. Provider credentials are prohibited in the test
   organization.

## Evidence boundary

Record only reviewed, non-secret release metadata: source SHA, image digest or
ID, workflow/run identity, runner labels, profile, bounded ciphertext hash where
applicable, and pass/fail result.

Never upload or log decrypted dotenv files, age identities, runtime secrets,
Compose environments, ciphertext bodies, provider prompts/transcripts, cookies,
or tokens. The E2E workflow must not upload artifacts containing runtime state.

## Current implementation evidence

Draft carrier PR: <https://github.com/meta-agents-demo/metacog-e2e/pull/5>

At head `2594eaaae9c05fcccacf3d8f600fb19d6cccb02b`, the credential-free harness has
17 passing tests plus JavaScript syntax, JSON, and credential-shape checks. The
live test-org, Docker, and secure-environment release gates remain unfulfilled
until the exact organization/repositories and approved runner are available.

Tracking: DEN-3496, DEN-1069, DEN-3028, and DEN-2932.
