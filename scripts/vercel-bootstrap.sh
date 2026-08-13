#!/usr/bin/env bash
set -euo pipefail

echo "APEX / Vercel bootstrap"
echo ""
echo "1) Install Vercel CLI"
npm i -g vercel

echo ""
echo "2) Authenticate"
vercel login

echo ""
echo "3) Deploy preview"
vercel

echo ""
echo "4) Deploy production when preview verification passes"
read -r -p "Deploy this project to production with 'vercel --prod'? [y/N] " answer
if [[ "$answer" =~ ^[Yy]$ ]]; then
  vercel --prod
fi

echo ""
echo "5) Optional AI-agent support"
echo "Claude Code / Cursor: npx plugins add vercel/vercel-plugin"
echo "Other supported agents: npx skills add vercel-labs/agent-skills"
echo ""
echo "APEX rule: do not mark GREEN until the deployment is independently verified."
