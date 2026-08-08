# `meta-agents-demo-test` proof boundary

## Current status

As of August 8, 2026, `meta-agents-demo-test` was not discoverable through the installed GitHub App and the organization endpoint returned not found. No test-org repository, workflow run, or App installation can therefore be claimed as verified yet. The production-org `meta-agents-demo/metacog-e2e` repository is the temporary non-destructive proving ground.

## Bootstrap checklist

1. Create or confirm the `meta-agents-demo-test` organization.
2. Install the same GitHub App used for repository automation, with repository contents, pull requests, issues, and Actions access.
3. Create a private `secure-env-e2e` fixture repository based on the `metacog-e2e` conformance harness.
4. Pin `ORESoftware/ores-sops` through Nix; do not copy its implementation.
5. Generate age identities and synthetic dev/prod ciphertext during each workflow run. Never commit a private identity, even for fixtures.
6. Run Linux and macOS round-trip jobs. Limit Windows to the native relative-symlink prerequisite until the canonical tool supports a complete native lane.
7. Add a fresh-clone/no-identity negative case and prove keyless `ores-sops verify` remains usable.
8. Publish only result metadata through the AI agent bridge: repository, commit, profile, operation, ciphertext hash, and pass/fail result.
9. Link test-org PRs and workflow runs to the owning Linear issue and production rollout PR.

A missing organization, App installation, hosted-runner budget, or fixture repository is an infrastructure gap, not a reason to weaken the secret boundary or block unrelated engineering work.
