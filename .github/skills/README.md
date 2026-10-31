# Creative Command Center Skill Library

These repository-local skills provide reusable instructions for an AI coding agent or operator working on this project.

| Skill | Purpose |
|---|---|
| `account-integration-audit` | Inventory services and safely map connection status |
| `android-device-inventory` | Build a read-only inventory of phone apps and accounts |
| `dropbox-asset-operations` | Find, inspect, organize, and share creative files safely |
| `github-project-operations` | Inspect and maintain repositories without overwriting work |
| `creative-production-workflows` | Coordinate Canva and creative production assets |
| `email-workflows` | Search, summarize, and draft Gmail messages safely |

## Important limitation
A skill file is agent guidance. It does not itself create an OAuth connection, install a provider app, grant API access, or add capabilities to the Android operating system. Provider integrations must be configured separately using supported connectors and explicit user authorization.

All workflows follow the repository's `AGENTS.md` privacy, approval, and least-privilege rules.