"""Evidence-only revenue readiness inventory. No commercial mutations."""
from pathlib import Path
from .base import Task
from .connected_apps import inventory_connected_apps

ROOT = Path(__file__).resolve().parents[2]


class RevenueReadiness(Task):
    name = "revenue_readiness"
    timeout_s = 60

    def run(self):
        apps = inventory_connected_apps(ROOT)
        return {
            "verified_in_this_run": False,
            "commercial_mutations_performed": False,
            "shopify": apps.get("shopify", {"status": "UNVERIFIED"}),
            "stripe": apps.get("stripe", {"status": "UNVERIFIED"}),
            "prepared_opportunities": [
                "Review authenticated commerce state during daytime owner-authorized checks.",
                "Review advertising/publishing readiness only where current evidence exists.",
            ],
        }
