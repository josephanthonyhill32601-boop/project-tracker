---
name: account-integration-audit
description: Inventory services and safely map persistent connection status for the Creative Command Center.
---

# Account Integration Audit

## Use when
The user asks to connect, integrate, audit, or reconcile accounts and apps across their phone or creative workspace.

## Procedure
1. Start from the user's supplied app list, screenshots, exported inventory, or an explicitly authorized read-only device inventory. Never imply the agent can see the entire phone unless a supported device tool provides it.
2. Normalize provider names and deduplicate aliases and multiple accounts.
3. Match each service against available, enabled connectors and record capability coverage.
4. Reuse verified connection status across sessions when the provider supports it. Recheck only if access fails, is stale, or the user requests verification.
5. Classify each entry: Connected, Needs user authorization, Available but not connected, Unavailable/blocked, or Manual-only.
6. Request minimum OAuth scopes. Prefer read-only scopes before write scopes.
7. Have the user complete official sign-in and consent. Never request credentials in chat.
8. Run a read-only test and report confirmed results.

## Output
Maintain one consolidated inventory with service, masked account label, status, available capabilities, required user action, and privacy class.

## Safety
Never connect sensitive personal, medical, legal, or financial data to a public/business workspace by default. Never disconnect accounts, change passwords, or broaden permissions without explicit approval.