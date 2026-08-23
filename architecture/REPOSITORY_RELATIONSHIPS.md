# `meta-agents-demo` repository relationships

Generated from reviewed policy and the current **public** repository inventory.

- Public repositories declared: **3**
- Private repository names withheld: **3**
- Relationship edges: **5**

## Repository roles

| Repository | Role | Lifecycle |
|---|---|---|
| [`.github`](https://github.com/meta-agents-demo/.github) | `organization_governance` | `active` |
| [`meta-agents-server.rs`](https://github.com/meta-agents-demo/meta-agents-server.rs) | `reference_implementation` | `superseded` |
| [`meta-agent-control-plane.rs`](https://github.com/meta-agents-demo/meta-agent-control-plane.rs) | `domain_service` | `active` |

`meta-agent-control-plane.rs` is the canonical production domain service. `meta-agents-server.rs` remains public as a legacy/reference implementation for historical context, protocol comparison, and local development; it is not a production deployment target.

## Declared edges

| From | Relationship | To | Status/basis |
|---|---|---|---|
| `meta-agents-demo/.github` | `governs` | `meta-agents-demo/meta-agent-control-plane.rs` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `meta-agents-demo/.github` | `governs` | `meta-agents-demo/meta-agents-server.rs` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `meta-agents-demo/meta-agent-control-plane.rs` | `supersedes` | `meta-agents-demo/meta-agents-server.rs` | `declared` / `reviewed-production-policy`: canonical production domain service supersedes the legacy/reference implementation |
| `organization://meta-agents-demo` | `deployed_via` | `platform://ORESoftware/k8s-cluster` | `platform-default` / `platform-policy`: immutable artifacts are promoted by digest through GitOps |
| `organization://meta-agents-demo` | `packaged_via` | `platform://zed-pkg` | `platform-default` / `platform-policy`: Zed resolves artifacts while submodules compose editable source |

## Composition, service, and observability contract

Git submodules compose editable source; Zed packages resolve packages/artifacts; dual-managed commits must match. Production deploys immutable image digests, not runtime source builds. Cross-service access uses APIs/SDKs/events rather than another service database. MCP uses the product API/SDK. Services emit OpenTelemetry traces, bounded metrics, and correlated structured logs.

## Privacy boundary

This public registry deliberately omits private repository names and edges; the count above makes the boundary explicit.
