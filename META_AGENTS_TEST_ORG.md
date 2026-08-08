# `meta-agents-demo-test` proof boundary

The test organization is the proving ground for changes that should not consume production-org capacity or touch production credentials.

## Bootstrap checklist

1. Create or confirm the `meta-agents-demo-test` organization.
2. Install the same GitHub App used for repository automation, with repository contents, pull requests, issues, and Actions access.
3. Create a private `secure-env-e2e` fixture repository from the `meta-agents-demo/metacog-e2e` secure-environment harness.
4. Keep only synthetic fixture values. Generate age identities during each workflow run and destroy the workspace copy at job exit.
5. Run Linux and macOS round-trip jobs there. Keep the production-org caller to one Linux policy proof until the test-org matrix is green.
6. Publish only result metadata through the AI agent bridge: repository, commit, profile, operation, ciphertext hash, and pass/fail status.
7. Link test-org PRs and workflow runs back to the Linear issue that owns the production rollout.

A missing organization, missing GitHub App installation, or missing fixture repository is an infrastructure gap, not a reason to block unrelated tickets. Track it independently and continue repository-local hardening.
