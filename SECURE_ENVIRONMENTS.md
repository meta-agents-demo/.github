# Secure environment standard

This organization uses SOPS, Nix, and `just` as one contract for local, CI, and agent-managed environment variables.

## Required layout

```text
.sops.yaml
flake.nix
justfile
env/
  enc/
    dev.env.enc
    prod.env.enc
  dec/
    dev.env
    prod.env
```

`env/enc/*.env.enc` is ciphertext and may be committed. `env/dec/*.env` is plaintext and must never be committed. A repository may expose the selected profile at its root only through a relative `.env` symlink such as `.env -> env/dec/dev.env`; the link and every plaintext `.env` file remain ignored.

## Toolchain contract

- **SOPS** performs encryption and decryption. Age is the default local and CI recipient mechanism; cloud KMS recipients are allowed where a project already owns them.
- **Nix** pins `sops`, `age`, `just`, and the shell utilities used by recipes. Contributors and agents run recipes inside `nix develop`.
- **just** is the only supported task entry point. Repositories implement `env-keygen`, `env-encrypt`, `env-decrypt`, `env-link`, `env-clean`, `env-policy`, and `env-ci`.
- Private age identities, KMS credentials, decrypted files, and generated `.env` links never enter Git history, workflow artifacts, logs, prompts, or agent-bridge payloads.

Real repositories should commit at least `env/enc/dev.env.enc` and `env/enc/prod.env.enc` after project-specific recipients are provisioned. Test fixtures use synthetic values and ephemeral age identities.

## Agent and bridge boundary

Agents may request a profile operation, but the process that holds decryption authority performs it. Bridge/coordinator events are metadata-only:

```json
{
  "schema": "meta-agents.secure-env.v1",
  "repository": "owner/name",
  "profile": "dev",
  "operation": "decrypt",
  "ciphertext_sha256": "<hex>",
  "result": "succeeded"
}
```

Never include plaintext values, private keys, environment dumps, command output containing secrets, or the encrypted data itself. Hashes identify the reviewed ciphertext without disclosing it.

## CI and test-org policy

`meta-agents-demo-test` is the execution boundary for destructive, cross-platform, and credential-integration tests. Production repositories keep a minimal policy/round-trip gate and should move larger matrices into test-org fixture repositories. Test repositories use synthetic secrets only; they do not receive production identities.

Every repository can call:

```yaml
jobs:
  secure-env:
    uses: meta-agents-demo/.github/.github/workflows/reusable-secure-env.yml@main
```

The caller must contain the required `flake.nix`, `justfile`, scripts, and directory policy. External actions are pinned to full commit SHAs and workflow permissions remain read-only.

## Rotation and recovery

Recipient rotation is additive: add the new recipient, run `sops updatekeys` for every tracked ciphertext, validate decryption with the new identity, and only then retire the old identity. Rotation work must not block unrelated engineering tickets. Recovery material belongs in the approved secret manager, never in this repository or an R2 bucket.
