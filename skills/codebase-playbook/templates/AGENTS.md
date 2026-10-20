# AGENTS.md

## Purpose

<One paragraph: what this project does and for whom.>

## Stack

- Language:
- Framework:
- Database:
- Hosting:
- Package manager:
- Runtime version:

## Commands

```bash
# install
# dev
# format
# lint
# typecheck
# test
# test one file
# build
# deploy
```

## Architecture map

```text
src/
  app/          <routes, pages, entry points>
  features/     <vertical feature modules>
  server/       <API, services, jobs>
  db/           <schema, migrations, queries>
  lib/          <shared utilities>
  components/   <shared UI>
```

- Request flow:
- Background jobs:
- Data ownership:
- External services:

## Conventions

- Naming:
- Error handling:
- Logging:
- State management:
- Styling:
- Commit messages:
- Branch names:

## Boundaries

- Do not edit generated files: <paths>
- Do not change the database schema without a migration.
- Do not add a dependency without checking license and maintenance.
- Ask before changing: <auth, billing, public API, infrastructure>
- Never commit secrets or real customer data.

## Verification

Before calling a task done, run:

```bash
<format>
<lint>
<typecheck>
<test>
<build>
```

A task is not done if any of these fail. Report the exact output.

## Docs

- Product brief: `docs/product-brief.md`
- Roadmap: `docs/roadmap.md`
- ADRs: `docs/adr/`
- Testing strategy: `docs/testing-strategy.md`
- Runbooks: `docs/runbooks/`

## Gotchas

- 
- 
