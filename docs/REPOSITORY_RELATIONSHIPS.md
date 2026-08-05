<!-- ore-org-baseline:begin -->
# Repository relationships for `meta-agents-demo`

This file is rendered from `repository-relationships.json`. The JSON registry is authoritative.

- Audience: `public`
- Repositories represented: **3**
- Relationships represented: **2**
- Inventory digest: `sha256:5bd2972917495e3ca04c61c1b65935744553c04953462975353193983c9f7391`

## Immutable routing identity

| Field | Value |
|---|---|
| Mapping ID | `context:meta-agents-demo` |
| GitHub owner ID | `311188342` |
| Linear project ID | `9914b9c3-8157-4ae5-a0c3-50b0a654ba06` |
| Linear team ID | `eb8ab169-5afe-4b6f-9cab-3f2aa3e887dc` |

## Repositories

| Repository | Visibility | Roles | Archived |
|---|---|---|---|
| `meta-agents-demo/.github` | `public` | `community-health`, `governance`, `relationship-registry` | no |
| `meta-agents-demo/meta-agent-control-plane.rs` | `public` | `repository` | no |
| `meta-agents-demo/meta-agents-server.rs` | `public` | `repository` | no |

## Relationships

| From | Type | To | Status | Required |
|---|---|---|---|---|
| `meta-agents-demo/.github` | `governs` | `meta-agents-demo/meta-agent-control-plane.rs` | `declared` | yes |
| `meta-agents-demo/.github` | `governs` | `meta-agents-demo/meta-agents-server.rs` | `declared` | yes |

## Editing relationships

Put reviewed public declarations in `repository-relationships.manual.json`; do not edit the generated registry directly.
Private repository names and private-only relationships belong in the private `approved-private-registry` mirror.
Inferred edges are advisory and must remain visibly labeled until reviewed.
<!-- ore-org-baseline:end -->
