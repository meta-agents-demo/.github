## Purpose

Describe the problem, user-visible behavior, owning repositories/components,
compatibility impact, and rollback path. Mark non-applicable checks as `N/A`
with a reason.

## Review path and dependencies

- [ ] All commits are on a non-default topic branch, and this PR is the proposed path into the default branch.
- [ ] No generated tool, bot, migration runner, or deployment process writes directly to a protected default branch.
- [ ] The change is small enough to review, or its staged rollout and follow-up PRs are identified.
- [ ] Cross-repository dependencies are pinned by immutable commit, lockfile, or released Zed package.

## Scope and boundaries

- [ ] The change is focused and does not silently cross repository ownership boundaries.
- [ ] No `*-infra` repository is introduced as a Git submodule under `*-monorepo/apps`.
- [ ] Public contracts, compatibility, migration, rollback, telemetry, and failure behavior are documented.
- [ ] Shared functionality is imported from its owning repository rather than copied into a new local implementation.
- [ ] Breaking changes include migration, rollback, and staged rollout notes.

## Contracts, SQL, and state

- [ ] Cross-runtime contracts use independently authored TypeSpec and JSON Schema Draft 2020-12 peer authorities, checked by `ORESoftware/typespec-json-schema-validator`; generated types/schemas are comparison or runtime evidence, and discrepancies block promotion.
- [ ] Generated language interfaces, ORM models, fixtures, and migration declarations were updated deterministically, with consumer compatibility checked.
- [ ] No SQL changes, or every declaration uses the registered logical namespace `<organization>.<domain>`, stable `<domain>_` object prefixes where a shared PostgreSQL schema such as `public` is required, and an explicit owning repository.
- [ ] Domain SQL may remain in its owning organization, but identity, ordering, checksums, drift detection, and promotion are registered through `declarative-migrations`.
- [ ] Application startup validates schema compatibility and does not apply production DDL.
- [ ] Destructive changes include compatibility, backfill, rollback, tenant isolation, RLS/authorization, idempotency, and state-machine evidence.

## Infrastructure and security

- [ ] Application manifests remain app-owned; cluster composition uses `oresoftware/k8s-cluster` and `oresoftware/k8s-libs-and-shared-defs`, without creating a second cluster control plane.
- [ ] Workloads use least privilege, workload identity, restricted Pod Security, non-root execution, default-deny networking, explicit egress, probes, bounded resources, secret handling, and immutable image/dependency references where applicable.
- [ ] Authentication and authorization failures are fail-closed, and sensitive operations are auditable.

## Verification and observability

- [ ] Zed lifecycle hooks cover deterministic format, lint, build, contract, pre-test, and pre-publish checks without bypassing language-native validation.
- [ ] Unit, integration, adversarial, migration, and end-to-end tests cover the changed behavior in the appropriate test organization.
- [ ] Destructive and cross-runtime tests run in the corresponding `*-test` organization or an isolated e2e environment, with teardown evidence.
- [ ] ORES OTEL trace/correlation propagation is present where applicable, with secret and user-content capture disabled by default.

## Validation evidence and residual risk

Provide exact commands, format/lint/build results, schema/codegen checks,
fixtures, test-org run links, migration/drift validation, security checks, and
manual verification. Explain any check that could not run. List residual risks,
follow-up work, and intentionally deferred repositories.

## Safety

- [ ] No credentials, secrets, personal/customer data, private-repository inventory, sensitive telemetry, or user content is included in source, logs, fixtures, or build artifacts.
- [ ] Conflicts were resolved semantically using both sides and relevant history.
- [ ] Destructive Git recovery, force pushes to protected branches, and history rewrites were not used.
- [ ] Logs and traces preserve tenant boundaries.

## Salvage check

If this PR supersedes or replaces an older one, say which and name at least one
concrete thing carried forward from it, such as a test, fixture, error message,
pin, or documentation paragraph. See
[`docs/pr-salvage-policy.md`](docs/pr-salvage-policy.md).

- [ ] Supersedes nothing, **or** the salvaged item is named above.
