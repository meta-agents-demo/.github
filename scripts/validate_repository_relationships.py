#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
sys.path.insert(0, str(ROOT / 'scripts'))

from repository_relationships_lib import (  # noqa: E402
    PUBLIC_AUDIENCE,
    RelationshipValidationError,
    parse_manual_declarations,
    validate_relationship_graph,
)


def fail(message: str) -> None:
    print(f'ERROR: {message}', file=sys.stderr)
    raise SystemExit(1)

required = [
    'repository-relationships.json',
    'repository-relationships.manual.json',
    'repository-relationships.schema.json',
    'repository-relationships.manual.schema.json',
    'docs/REPOSITORY_RELATIONSHIPS.md',
    'architecture/repository-relationships.json',
    'architecture/repository-relationships.schema.json',
    'architecture/REPOSITORY_RELATIONSHIPS.md',
]
missing = [path for path in required if not (ROOT / path).is_file()]
if missing:
    fail('missing relationship files: ' + ', '.join(missing))

try:
    graph = json.loads((ROOT / 'repository-relationships.json').read_text(encoding='utf-8'))
    validate_relationship_graph(graph)
    owner = graph['owner']['login']
    manual = parse_manual_declarations(
        (ROOT / 'repository-relationships.manual.json').read_text(encoding='utf-8'),
        owner,
        audience=PUBLIC_AUDIENCE,
    )
    architecture = json.loads(
        (ROOT / 'architecture/repository-relationships.json').read_text(encoding='utf-8')
    )
    for schema_path in (
        ROOT / 'repository-relationships.schema.json',
        ROOT / 'repository-relationships.manual.schema.json',
        ROOT / 'architecture/repository-relationships.schema.json',
    ):
        schema = json.loads(schema_path.read_text(encoding='utf-8'))
        if schema.get('$schema') != 'https://json-schema.org/draft/2020-12/schema':
            fail(f'{schema_path.name} is not JSON Schema draft 2020-12')
except (KeyError, json.JSONDecodeError, RelationshipValidationError) as exc:
    fail(str(exc))

graph_edges = {
    (edge['from'].casefold(), edge['type'], edge['to'].casefold()): edge
    for edge in graph['relationships']
}
for index, edge in enumerate(manual['relationships']):
    key = (edge['from'].casefold(), edge['type'], edge['to'].casefold())
    generated = graph_edges.get(key)
    if generated is None:
        fail(f'manual relationship {index} is missing from generated registry')
    if generated['status'] != edge.get('status', 'declared'):
        fail(f'manual relationship {index} status differs from generated registry')

markdown = (ROOT / 'docs/REPOSITORY_RELATIONSHIPS.md').read_text(encoding='utf-8')
if graph['generated']['inventory_digest'] not in markdown:
    fail('relationship documentation digest does not match JSON registry')
if graph.get('audience') != PUBLIC_AUDIENCE:
    fail('organization .github relationship registry must have public audience')
for edge in manual['relationships']:
    key = (edge['from'].casefold(), edge['type'], edge['to'].casefold())
    generated = graph_edges[key]
    expected = (
        f"| `{generated['from']}` | `{generated['type']}` | `{generated['to']}` | "
        f"`{generated['status']}` | {'yes' if generated.get('required') else 'no'} |"
    )
    if expected not in markdown:
        fail(f"generated documentation omits manual relationship {generated['id']}")

public_repositories = {repository['full_name'].casefold() for repository in graph['repositories']}
architecture_repositories = {
    repository['full_name'].casefold(): repository
    for repository in architecture['repositories']
}
for repository in architecture_repositories.values():
    if (
        repository.get('visibility') != 'public'
        or repository['full_name'].casefold() not in public_repositories
    ):
        fail(
            'architecture registry exposes a non-public or uninventoried repository: '
            f"{repository['full_name']}"
        )

control_plane_name = 'meta-agents-demo/meta-agent-control-plane.rs'
legacy_server_name = 'meta-agents-demo/meta-agents-server.rs'
expected_policy = {
    control_plane_name: {
        'canonical': True, 'lifecycle': 'active', 'role': 'domain_service',
    },
    legacy_server_name: {
        'lifecycle': 'superseded', 'role': 'reference_implementation',
        'superseded_by': control_plane_name,
    },
}
for repository_name, expected in expected_policy.items():
    actual = architecture_repositories.get(repository_name.casefold()) or {}
    if any(actual.get(field) != value for field, value in expected.items()):
        fail(f'architecture registry has stale production policy for {repository_name}')
if not any(
    edge.get('from') == control_plane_name
    and edge.get('kind') == 'supersedes'
    and edge.get('to') == legacy_server_name
    and edge.get('status') == 'declared'
    for edge in architecture['relationships']
):
    fail(
        'architecture registry is missing the declared control-plane supersedes '
        'server relationship'
    )

architecture_markdown = (
    ROOT / 'architecture/REPOSITORY_RELATIONSHIPS.md'
).read_text(encoding='utf-8')
for repository in architecture['repositories']:
    expected = (
        f"| [`{repository['name']}`](https://github.com/{repository['full_name']}) | "
        f"`{repository['role']}` | `{repository['lifecycle']}` |"
    )
    if expected not in architecture_markdown:
        fail(
            'architecture relationship documentation omits current role for '
            f"{repository['full_name']}"
        )
if 'is the canonical production domain service.' not in architecture_markdown:
    fail(
        'architecture relationship documentation omits the canonical production '
        'service declaration'
    )

print(
    'PASS: validated repository relationship registry for '
    f"{owner} ({len(graph['repositories'])} repositories, {len(graph['relationships'])} relationships)"
)
