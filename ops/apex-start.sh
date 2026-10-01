#!/usr/bin/env bash
set -Eeuo pipefail
IFS=$'\n\t'
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
printf '\nAPEX START — %s\n' "$(basename "$ROOT")"
printf '%s\n' '----------------------------------------'
if [[ -f "$ROOT/.env.local" ]]; then set -a; source "$ROOT/.env.local"; set +a
elif [[ -f "$ROOT/.env" ]]; then set -a; source "$ROOT/.env"; set +a
fi
[[ -x "$ROOT/ops/apex-guard.sh" ]] && "$ROOT/ops/apex-guard.sh"
command -v git >/dev/null 2>&1 || { echo 'ERROR: git is required.' >&2; exit 1; }
if [[ -f package.json ]]; then
  command -v node >/dev/null 2>&1 && command -v npm >/dev/null 2>&1 || { echo 'ERROR: Node.js + npm are required.' >&2; exit 1; }
  if [[ ! -d node_modules ]]; then [[ -f package-lock.json ]] && npm ci || npm install; fi
  if node -e 'const p=require("./package.json"); process.exit(p.scripts?.dev ? 0 : 1)' 2>/dev/null; then exec npm run dev; fi
  if node -e 'const p=require("./package.json"); process.exit(p.scripts?.start ? 0 : 1)' 2>/dev/null; then exec npm start; fi
  echo 'ERROR: package.json has no dev or start script.' >&2; exit 1
fi
echo 'No package.json startup contract found.' >&2
echo 'Use APEX_START_CMD="your command" ./ops/apex-start.sh' >&2
[[ -n "${APEX_START_CMD:-}" ]] && exec bash -lc "$APEX_START_CMD"
exit 1
