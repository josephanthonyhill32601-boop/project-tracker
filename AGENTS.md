# Creative Command Center — Agent Operating Rules

This repository is a private-first phone/cloud project tracker for the Wicked Jester creative ecosystem.

## Core rules
- Treat the user as the owner and final approver of all accounts, assets, and projects.
- Never ask for, store, print, or commit passwords, API keys, OAuth tokens, recovery codes, or session cookies.
- Use official OAuth or provider authorization flows. Explain requested scopes before authorization.
- Reuse verified existing connections; do not repeat completed account checks without a specific reason.
- Never claim an integration is connected, installed, synced, or working until a provider response or test confirms it.
- Do not disconnect accounts, change passwords, revoke access, publish content, or change visibility without explicit approval.
- Do not delete, move, overwrite, or share files without showing the proposed change and obtaining approval.
- Keep personal, family, medical, legal, and financial information in separate private stores. Do not copy it into public repositories, public websites, creative catalogs, analytics, or marketing systems.
- Keep creative/business assets separate from sensitive personal records. Use least-privilege access.
- Default repositories and previews to private/unpublished. Never publish automatically.

## Integration workflow
1. Inventory services and app names supplied by the user.
2. Classify each as connected, authorization required, unavailable, or manual-only.
3. Record only provider name, connection status, approved scopes, last verification time, and non-sensitive notes.
4. Ask the user to complete provider sign-in/consent when required.
5. Test read-only access first; request write scopes only when a task requires them.
6. Report confirmed results and remaining blockers in one consolidated status list.

## Device safety
- Do not run broad Android optimization commands or alter system settings without an explicit, reviewed plan.
- Do not disable security, battery, backup, accessibility, or privacy protections to improve performance.
- Use read-only device inventory first; separate optional setup steps from diagnostic steps.

## Skill library
Reusable agent workflows live under `.github/skills/`. These are instruction packages, not credentials, plugins, or installed mobile applications.