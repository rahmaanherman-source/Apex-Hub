"""Evidence-driven morning report. No hard-coded commerce success claims."""
from pathlib import Path
from .base import Task


class Report(Task):
    name = "report"
    timeout_s = 60

    def run(self):
        entries = self.log.read_all()
        ok = [e["task"] for e in entries if e.get("status") == "OK"]
        failed = [e["task"] for e in entries if e.get("status") == "FAIL"]
        stopped = any(e.get("status") == "STOPPED" for e in entries)

        report = {
            "run_id": self.log.run_id,
            "checks_ok": ok,
            "checks_failed": failed,
            "stopped": stopped,
            "verified_in_this_run": bool(ok) and not failed and not stopped,
            "commercial_mutations_performed": False,
            "note": "This report only states what the overnight evidence ledger supports. Daytime owner-authorized checks are required for authenticated cloud services.",
        }

        path = self.log.root / "logs" / "APEX_OVERNIGHT_REPORT.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        lines = [
            "# APEX Overnight Report",
            "",
            f"Run: `{self.log.run_id}`",
            "",
            f"Verified in this run: **{'YES' if report['verified_in_this_run'] else 'NO'}**",
            f"Commercial mutations performed: **NO**",
            "",
            "## Checks OK",
            *[f"- {name}" for name in ok] or ["- None"],
            "",
            "## Checks Failed",
            *[f"- {name}" for name in failed] or ["- None"],
            "",
            "## Morning Action",
            "- Review any failed checks and explicit owner-approval requests.",
            "- Perform authenticated/cloud commerce or advertising checks only during the daytime owner-authorized window.",
            "- Do not treat preparation or configuration as proof of a completed transaction.",
        ]
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return report
