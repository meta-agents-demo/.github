# meta-agents-demo

This organization maintains software, infrastructure, interfaces, clients, services, and supporting documentation under a shared engineering baseline.

## Working principles

- Keep changes reviewable, tested, and reversible.
- Treat security, privacy, compatibility, and data durability as design constraints.
- Resolve merge conflicts semantically: reconstruct both sides' intent, preserve compatible behavior, and document deliberate trade-offs.
- Prefer canonical repositories and short, stable names; deprecate duplicates with migration notes rather than silently deleting history.
- Keep cross-repository dependencies explicit and pinned where reproducibility matters.

Organization-wide contribution and security guidance lives in this `.github` repository.

<!-- org-project-routing:start -->
## Planning and delivery

- [GitHub Project: meta-agents-demo-project](https://github.com/orgs/meta-agents-demo/projects/1)
- [Linear planning project](https://linear.app/denman/project/meta-agents-demo-e6f63b3acf1f)
- [Detailed project-routing contract](../docs/PROJECTS.md)

GitHub owns code and delivery evidence; Linear owns planning and dependencies. The linked organization Project provides the cross-repository execution view.
<!-- org-project-routing:end -->

<!-- ore-org-baseline:begin -->
## Planning and governance

- Canonical Linear project: https://linear.app/denman/project/meta-agents-demo-e6f63b3acf1f
- Organization defaults: https://github.com/meta-agents-demo/.github
- Canonical agent policy: https://github.com/meta-agents-demo/.github/blob/main/agents.md
- Security policy: https://github.com/meta-agents-demo/.github/security/policy

Repositories in this organization use semantic conflict resolution with 3–10 relevant prior commits when useful, full cross-repository context, pull-request delivery, and a hard automated-agent denylist for destructive or history-rewriting operations.
<!-- ore-org-baseline:end -->

<!-- BEGIN MANAGED REPOSITORY RELATIONSHIPS v1 -->
## Repository relationship registry

`meta-agents-demo` declares repository roles, dependency edges, cross-organization capabilities, deployment ownership, and the git-submodule/Zed-package contract:

- [Human-readable map](architecture/REPOSITORY_RELATIONSHIPS.md)
- [Machine-readable manifest](architecture/repository-relationships.json)
- [JSON Schema](architecture/repository-relationships.schema.json)

The public registry withholds private repository names and edges.
<!-- END MANAGED REPOSITORY RELATIONSHIPS v1 -->
