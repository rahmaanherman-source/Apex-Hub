"""Post-repair verification pass."""
from .base import Task
from .build_test import BuildTest


class Reverify(Task):
    name = "reverify"
    timeout_s = 900

    def run(self):
        # Execute deterministic verification without adding a second evidence record;
        # this task's wrapper records the complete result.
        nested = BuildTest(self.log)
        result = nested.run()
        failed = []
        for key, value in result.items():
            if isinstance(value, dict) and value.get("ok") is False:
                failed.append(key)
        return {"post_repair": result, "verified": not failed, "failures": failed}
