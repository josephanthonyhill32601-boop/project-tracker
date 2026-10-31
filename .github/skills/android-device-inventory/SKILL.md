---
name: android-device-inventory
description: Safely inventory installed Android apps and account providers, beginning with read-only discovery.
---

# Android Device Inventory

## Use when
The user wants all phone apps or accounts included in an integration inventory.

## Procedure
1. Confirm device model and Android version only from current device output or user-provided information.
2. Prefer a user-shared app drawer screenshot, Settings > Passwords & accounts screenshot, or an explicitly authorized read-only Termux/ADB inventory.
3. Do not assume every installed app has a ChatGPT connector.
4. Separate installed apps from signed-in accounts and from available provider integrations.
5. Mask email addresses and account identifiers in reports unless the full value is necessary.
6. Categorize sensitive apps (banking, health, legal, family, identity) as private by default.
7. Provide a single deduplicated inventory and avoid asking for the same screenshot or account details again.

## Device commands
If an authorized local shell is available, use read-only commands first. Explain what each command reads before running it. Do not run package removal, permission changes, account changes, debloating, or performance-tuning commands as part of inventory.

## Limitations
A cloud agent cannot inspect Android Settings or the installed-app list without a supported device bridge or user-provided inventory.