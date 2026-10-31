# WickedJester Creative Command Center — Integration Architecture

## Purpose
Provide one coordinated workspace for creative projects, assets, production workflows, publishing approvals, and technical operations. This repository is the technical scaffold, not the storage location for private business records or credentials.

## System boundaries
- **Command center:** project index, task state, connection registry, workflow definitions, and health checks.
- **Asset source of truth:** the user's chosen cloud storage provider. Keep originals in place; index references and metadata rather than duplicating media.
- **Development source of truth:** Git repositories for source code, automation definitions, documentation, and version history.
- **Creative production:** design, image, video, and audio tools remain their own production systems; the hub tracks inputs, outputs, versions, and approval state.
- **Communications and publishing:** draft and review first. Sending, posting, publishing, or sharing requires explicit approval.
- **Automation:** scheduled read-only checks first; write actions only after a specific workflow is reviewed and approved.
- **Private records:** legal, medical, family, identity, and financial information must remain in separate private systems and must not be copied into this repository or public creative systems.

## Integration pattern
1. Use provider-supported OAuth/API integrations; never collect passwords, recovery codes, cookies, or raw API keys in chat or source control.
2. Grant least privilege. Start with read-only scopes; request write access only for a demonstrated workflow.
3. Store secrets only in a provider-approved secret manager or local secure environment, never in Git.
4. Normalize cross-app references into a shared project/asset index: provider, external item ID, project ID, type, title, status, modified time, and source URL where safe.
5. Keep large binary media in its source storage. The index stores references and non-sensitive metadata.
6. Use stable project IDs so a design, source repository, media render, and publishing draft can belong to the same project without being copied into one system.
7. Record each integration's state as one of: connected-and-tested, connected-unverified, authorization-required, unavailable, or manual-workflow.
8. Record last verification time and approved scopes. Never infer a connection from an installed app alone.

## Standard creative workflow
1. Capture an idea or request in the project index.
2. Assign a project ID and owner.
3. Link source assets and working files.
4. Produce in the appropriate creative application.
5. Register output versions and review status.
6. Require user approval before publishing, sending, sharing, deleting, moving, or overwriting.
7. Record the final destination and retain the original source.

## Reliability and safety
- Do not change passwords, MFA, recovery settings, or revoke tokens as part of routine integration.
- Do not interrupt active uploads, downloads, builds, automations, or running services.
- Back up configuration before edits and use reversible changes.
- Test one integration at a time, beginning with read-only checks.
- Do not claim sync or end-to-end functionality until a real round-trip test succeeds.
- Keep this repository free of personal data, private customer information, legal/medical/financial records, and credentials.

## Current implementation stages
- [ ] Confirm authoritative private hub repository or create one through GitHub's user interface.
- [ ] Confirm organization membership and access.
- [ ] Establish provider connection registry without secrets.
- [ ] Build project and asset index schema.
- [ ] Connect Dropbox asset references.
- [ ] Connect GitHub project/repository references.
- [ ] Add Canva design references.
- [ ] Verify Gmail identity and add draft-only workflow.
- [ ] Add media-production integrations after provider authorization.
- [ ] Add approval-gated automation and dashboard.
- [ ] Run end-to-end test on one non-sensitive sample project.

## Public repository notice
This repository is currently public. Only generic architecture, reusable code, and non-sensitive documentation belong here. Do not add account identifiers, private asset inventories, project contracts, financial data, family records, or integration secrets.
