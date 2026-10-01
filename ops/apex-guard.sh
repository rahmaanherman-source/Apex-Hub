#!/usr/bin/env bash
set -Eeuo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
fail=0
for f in .env .env.local .env.production .env.development; do
  if git ls-files --error-unmatch "$f" >/dev/null 2>&1; then echo "BLOCKED: tracked secret file: $f" >&2; fail=1; fi
done
if git grep -nE -- ':!*.md' ':!*.example' ':!*.sample' ':!*.template' '(sk_live_[A-Za-z0-9]{16,}|ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9-]{20,}|shpat_[A-Za-z0-9]{20,}|-----BEGIN (RSA |EC |OPENSSH |)PRIVATE KEY-----)' >/tmp/apex-secret-hits.$$ 2>/dev/null; then
  echo 'BLOCKED: possible credential material found in tracked files:' >&2
  sed -n '1,20p' /tmp/apex-secret-hits.$$ >&2
  fail=1
fi
rm -f /tmp/apex-secret-hits.$$
if [[ "$fail" -ne 0 ]]; then echo 'APEX GUARD FAILED. Remove/rotate exposed credentials before starting.' >&2; exit 1; fi
echo 'APEX GUARD: PASS — no tracked env files or high-signal credentials detected.'
