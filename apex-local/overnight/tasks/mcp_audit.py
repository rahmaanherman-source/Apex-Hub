"""Local MCP configuration inventory without contacting remote servers."""
from pathlib import Path
from .base import Task

ROOT = Path(__file__).resolve().parents[2]
CONFIG_NAMES = {"mcp.json", "mcp.yaml", "mcp.yml", "claude_desktop_config.json", "config.json"}
SKIP = {".git", "node_modules", "venv", ".venv", "__pycache__"}


class MCPAudit(Task):
    name = "mcp_audit"
    timeout_s = 90

    def run(self):
        found = []
        for path in ROOT.rglob("*"):
            if not path.is_file() or any(part in SKIP for part in path.parts):
                continue
            if path.name in CONFIG_NAMES and "mcp" in path.name.lower():
                found.append(str(path.relative_to(ROOT)))
        return {"config_files": found, "remote_connections_attempted": False}
