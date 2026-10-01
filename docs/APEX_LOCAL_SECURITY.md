# APEX Local Start + Security Contract

This repository uses a dependency-free startup and secret guard.

## Start

```bash
bash ops/apex-start.sh
```

For Apex-Hub, the equivalent npm command is:

```bash
npm run apex:start
```

## What happens

1. Loads `.env.local` (or `.env`) only into the startup process.
2. Runs `ops/apex-guard.sh` before the application starts.
3. Blocks tracked `.env*` secret files.
4. Checks tracked files for high-signal credential formats.
5. Installs dependencies only when `node_modules` is absent.
6. Runs the repository `dev` script, then `start` if no `dev` script exists.
7. Never prints secret values.

## Credentials

Real credentials belong outside Git. Use local `.env.local` for development or the existing APEX Omni Vault/runtime secret system for deployed services. Commit only placeholders such as `.env.example`.

Do not put API keys, private keys, payment secrets, GitHub tokens, JWT signing secrets, or service-role credentials in source code, documentation, screenshots, logs, or commits.

## Free protection stack

The startup/guard layer uses Bash, Git, Node.js/npm, and repository-native checks. No paid security dependency is required. GitHub also provides push protection for users by default and provides free secret-scanning protections for public repositories; use those controls where available.

## Incident rule

If a real credential is ever exposed, treat it as compromised: revoke/rotate it at the provider, remove it from the working tree/history as appropriate, and record the remediation in the security log.
