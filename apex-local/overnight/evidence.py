"""Append-only JSONL evidence ledger with centralized redaction."""
import json
from datetime import datetime, timezone
from pathlib import Path
from .redaction import redact

ROOT = Path(__file__).resolve().parent.parent
RUN_DIR = ROOT / "logs" / "overnight"


class EvidenceLog:
    def __init__(self, run_id: str, root: Path | None = None):
        self.run_id = run_id
        self.root = Path(root or ROOT)
        self.path = self.root / "logs" / "overnight" / f"{run_id}.jsonl"
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def write(self, task: str, status: str, payload: dict) -> None:
        entry = {
            "ts": datetime.now(timezone.utc).isoformat(),
            "run": self.run_id,
            "task": task,
            "status": status,
            "payload": redact(payload),
        }
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(entry, ensure_ascii=False) + "\n")

    def read_all(self) -> list[dict]:
        if not self.path.exists():
            return []
        entries = []
        for line in self.path.read_text(encoding="utf-8").splitlines():
            try:
                entries.append(json.loads(line))
            except json.JSONDecodeError:
                continue
        return entries
