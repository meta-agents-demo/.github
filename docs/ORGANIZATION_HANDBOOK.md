# meta-agents-demo organization handbook

> Shared operating defaults for repositories maintained under **meta-agents-demo**. Repository-local policy may strengthen these rules but should not silently weaken them.

## Mission

meta-agents-demo maintains experimental agent orchestration, introspection, memory, connector, and demonstration software. This `.github` repository is the canonical home for shared policy, reusable templates, community health files, and planning links.

## Repository contract

Each active repository must document purpose, ownership, maturity, supported runtimes and providers, development and test commands, authoritative message and state formats, release and rollback procedures, compatibility policy, and GitHub Project/Linear links. Agent components should also document tool permissions, trust boundaries, prompt and policy sources, memory lifecycle, connector behavior, timeouts, budgets, determinism limits, evaluation methods, human-approval gates, and failure containment.

## Change workflow

1. Anchor work in an issue, Linear item, or documented maintenance objective.
2. Keep branches and pull requests focused.
3. Explain motivation, scope, safety and behavior impact, validation, compatibility, migration, and rollback.
4. Test unavailable tools, malformed outputs, prompt injection, permission denial, timeout, retry, budget exhaustion, restart, and human-escalation paths as relevant.
5. Resolve conflicts semantically by reconstructing both sides' intent.
6. Prefer squash merges for focused work unless commit structure materially improves auditability.

## Evidence, security, and documentation

Pull requests should include reproducible commands, synthetic fixtures, evaluation cases, expected and observed behavior, negative-path coverage, documentation updates, and CI or local-equivalent evidence. Never commit credentials, private conversations, hidden prompts, production identities, or sensitive logs. Follow `SECURITY.md` for private reporting. Keep tool permissions least-privileged, examples sanitized, evaluation limits explicit, and important safety, memory, compatibility, and operational decisions recorded.

## Planning ownership

GitHub owns code, reviews, checks, releases, and delivery evidence. Linear owns priority, dependencies, sequencing, and cross-project planning. The organization GitHub Project is the cross-repository execution view; see `PROJECTS.md` for routing details.

## Organization health

- [ ] Profiles, descriptions, topics, and READMEs are current.
- [ ] Community health files and reusable issue/PR guidance are present.
- [ ] Tool permissions, prompt sources, memory, budgets, approvals, evaluations, and failure containment are documented.
- [ ] Required checks cover adversarial inputs, denied/unavailable tools, compatibility, privacy, and supply-chain risk.
- [ ] Stale experiments are archived or clearly marked.
- [ ] GitHub Project and Linear links resolve and reflect completed work.
