# PR Description Draft

## Title
Add first-stage team-aware compatibility for WiseDev Suite

## Summary
This PR introduces the first stage of a compatibility-safe team-aware upgrade for WiseDev Suite.

The goal is not to turn the suite into a team-only workflow, but to preserve the existing single-skill and single-stage usage model while adding a compatible branch for long-lived multi-role product-delivery teams.

## What Changed

### 1. Added `AgentTeam/` design package
Introduced a dedicated `AgentTeam/` directory containing:
- team role specifications
- shared artifact layout
- review / assignment / acceptance / handoff templates
- runtime rules
- adoption plan
- implementation backlog
- compatibility guidelines
- changelog

### 2. Upgraded control-layer skills
Updated:
- `using-wisedev/SKILL.md`
- `wisedev-orchestrator/SKILL.md`

Key additions:
- team-aware context detection
- leader-oriented control behavior
- shared artifact awareness
- reviewer / acceptance / handoff awareness
- compatibility rules to preserve non-team workflows

### 3. Added lightweight team-aware rules to child skills
Updated:
- `wisedev-meeting-to-spec/SKILL.md`
- `wisedev-requirement-spec/SKILL.md`
- `wisedev-design-doc/SKILL.md`
- `wisedev-openapi-contract/SKILL.md`
- `wisedev-prototype-design/SKILL.md`
- `wisedev-vue-mock-prototype/SKILL.md`

Key additions:
- compatibility sections
- lightweight team-aware sections
- role-boundary guidance
- shared artifact write-back preference
- upstream-instability pushback rules

## Compatibility Strategy
This PR follows a compatibility-first approach:

1. default skill behavior remains intact
2. team-aware logic is an enhancement branch, not the only branch
3. control-layer skills strongly sense team context
4. child skills only get lightweight team-aware rules
5. `AgentTeam/` is referenced as an optional coordination layer, not a hard runtime dependency

## Why This Matters
This creates a foundation for evolving WiseDev Suite from a staged single-controller skill bundle into a long-lived multi-role delivery team, without immediately breaking the current standalone skill usage model.

## Scope Boundaries
This PR does not yet:
- implement real AgentTeam runtime integration
- enforce shared artifact initialization automatically
- add runtime-level reviewer loops
- validate every flow end-to-end via executable tests

## Recommended Review Focus
1. verify the compatibility wording in all modified `SKILL.md` files
2. verify that non-team usage is still clearly supported
3. verify that team-aware rules are additive and not destructive
4. verify consistency between `AgentTeam/` docs and skill-level changes

## Suggested Smoke Test Areas
1. standalone single-stage requirement-spec generation
2. standalone OpenAPI generation
3. standalone Vue mock prototype generation
4. team-context routing through `using-wisedev` and `wisedev-orchestrator`
5. child skill behavior when shared artifacts are present vs absent

## Commits Included
- `bfe7617` Add AgentTeam design package and team-aware control layer
- `c267469` Add team-aware compatibility to output skills
- `d9470e6` Add team-aware changelog

## Follow-up Work
1. run manual bundle-level smoke checks
2. decide whether to refine any child skill wording after review
3. plan runtime-side integration for shared artifacts and leader/reviewer flow
