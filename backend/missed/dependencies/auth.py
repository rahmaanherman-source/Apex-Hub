#!/usr/bin/env bash
set -euo pipefail

echo "🔱 Verifying Apex-Hub stack..."

echo -n "FastAPI backend: "
if curl -sf http://localhost:8000/health > /dev/null; then
    echo "✅ healthy"
else
    echo "❌ not reachable"
    exit 1
fi

echo -n "Frontend dev server: "
if curl -sf http://localhost:3000 > /dev/null; then
    echo "✅ healthy"
else
    echo "⚠️ not running (maybe not started)"
fi

echo -n "PostgreSQL: "
if psql "$DATABASE_URL" -c "SELECT 1" > /dev/null 2>&1; then
    echo "✅ connected"
else
    echo "⚠️ not reachable (check Docker or DATABASE_URL)"
fi

echo -n "Redis: "
if redis-cli ping > /dev/null 2>&1; then
    echo "✅ PONG"
else
    echo "⚠️ not reachable"
fi

echo -n "Qdrant: "
if curl -sf http://localhost:6333 > /dev/null; then
    echo "✅ healthy"
else
    echo "⚠️ not reachable"
fi

echo -n "Bifrost gateway: "
if curl -sf http://localhost:8002/health > /dev/null 2>&1; then
    echo "✅ healthy"
else
    echo "⚠️ not running"
fi

echo ""
echo "Stack verification complete."