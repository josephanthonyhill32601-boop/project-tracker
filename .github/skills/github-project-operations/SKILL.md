---
name: github-project-operations
description: Inspect and maintain the Creative Command Center GitHub project, preserving existing files and repository privacy.
---

# GitHub Project Operations

## Use when
The user asks to locate repositories, add agent skills, inspect code, manage issues, or maintain project documentation.

## Workflow
1. Search the connected account's accessible repositories by known username, organization, project name, and relevant description terms.
2. Verify repository ownership, visibility, default branch, and write permission before changing anything.
3. Inspect the root tree and relevant files before creating or updating paths.
4. Add reusable agent guidance under `.github/skills/<skill-name>/SKILL.md`; use `AGENTS.md` for repository-wide rules.
5. Never overwrite an existing file without fetching its current contents and obtaining approval for the intended replacement.
6. Keep secrets in provider-managed secret stores; never commit keys or tokens.
7. Prefer small, reviewable commits with descriptive messages.
8. Keep the repository private unless the user explicitly approves publication.

## Validation
After writing, confirm the commit response and fetch the new files to verify their contents. Report exact paths and commit status.