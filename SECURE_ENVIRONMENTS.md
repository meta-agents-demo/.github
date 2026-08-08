# Secure environment standard

The canonical implementation is [`ORESoftware/ores-sops`](https://github.com/ORESoftware/ores-sops). Meta Agents repositories consume that package through Nix and delegate environment recipes through `just`; they do not copy or fork its shell logic.

## Repository contract

Exactly two secret-bearing ciphertext paths are approved:

```text
env/enc/dev.env.enc
env/enc/prod.env.enc
```

Plaintext remains local-only:

```text
env/dec/dev.env
env/dec/prod.env
.env -> env/dec/dev.env   # or prod; relative managed symlink
```

Private age identities, KMS credentials, decrypted files, and generated `.env` links never enter Git history, workflow artifacts, logs, prompts, Linear, or agent-bridge payloads. Ciphertext is validated by content and policy, not trusted merely because its filename ends in `.enc`.

`ores-sops` owns the exact dev/prod allowlist, explicit SOPS dotenv typing, atomic encryption/decryption, directory and file modes, managed symlink safety, hooks, keyless verification, and protected decrypt verification. Arbitrary environment names are intentionally rejected.

## Nix and `just`

Pin `ores-sops` through a flake lock or an exact revision. The `meta-agents-demo/metacog-e2e` pilot pins a reviewed commit and exposes the upstream development shell and checks.

Application repositories keep recipes as thin delegates:

```just
use name:
    @ores-sops use {{ name }}

encrypt name:
    @ores-sops encrypt {{ name }}

status:
    @ores-sops status

lock:
    @ores-sops lock

audit:
    @ores-sops verify
```

This preserves one implementation across organizations while retaining a stable task interface for people and agents.

## CI and proof boundary

Pull-request checks are keyless by default: they validate tracked paths, ignore rules, SOPS policy, ciphertext structure, symlink safety, and the absence of private-key material. A protected test job may generate an ephemeral age identity and set `ORES_SOPS_VERIFY_DECRYPT=1` to prove a synthetic round trip. Production identities are never exposed to fork-originated workflows.

A conforming repository may call:

```yaml
jobs:
  secure-env:
    uses: meta-agents-demo/.github/.github/workflows/reusable-secure-env.yml@main
```

The caller provides a pinned `flake.nix` and `just env-ci`. External actions remain pinned to full commit SHAs, workflow permissions stay read-only, and no plaintext is uploaded as an artifact.

## Agent and bridge boundary

Agents may request an operation, but only the process holding decryption authority performs it. Bridge/coordinator evidence is metadata-only:

```json
{
  "schema": "meta-agents.secure-env.v1",
  "repository": "owner/name",
  "profile": "dev",
  "operation": "roundtrip",
  "ciphertext_sha256": "<hex>",
  "result": "passed"
}
```

Never include plaintext values, private keys, environment dumps, auth headers, command output containing secrets, or encrypted file bodies. The hash identifies the reviewed ciphertext without disclosing it.

## Test organization

`meta-agents-demo-test` is the intended execution boundary for the Linux/macOS matrix, Windows relative-symlink prerequisite, destructive fixtures, and bridge ingestion tests. Until the organization and GitHub App installation are available, `meta-agents-demo/metacog-e2e` carries a non-destructive synthetic proof in the production org. That infrastructure gap is tracked independently and must not block unrelated tickets.

## Rotation and recovery

Recipient rotation is additive: add the new recipient, run `sops updatekeys` for both tracked ciphertext files, validate with the new identity, and only then retire the old identity. Rotate application credentials when compromise or offboarding requires it. Recovery identities belong in an independently controlled secret manager, never in Git or an R2 bucket.
