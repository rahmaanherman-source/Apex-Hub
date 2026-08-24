"""Reference APEX AuditBus contract.

This file is a source-level implementation reference. It is not evidence that
any runtime has executed. A concrete repository adapter must implement the
repo methods against the selected persistence layer.
"""
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
import uuid
import hashlib
import json

GENESIS_HASH = "0" * 64

@dataclass(frozen=True)
class AuditEvent:
    event_type: str
    source: str
    action: str
    severity: str = "info"
    actor_type: str = "system"
    actor_id: str | None = None
    resource_type: str | None = None
    resource_id: str | None = None
    provider: str | None = None
    country: str | None = None
    currency: str | None = None
    amount_minor: int | None = None
    correlation_id: str | None = None
    payload: dict = field(default_factory=dict)
    event_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    occurred_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

class AuditBus:
    def __init__(self, repo, environment: str = "live"):
        self.repo = repo
        self.environment = environment

    def emit(self, event: AuditEvent):
        row = {**asdict(event), "environment": self.environment}
        # Repository contract: insert must be idempotent on event_id.
        return self.repo.insert_audit_event(row)

    def route_decided(self, intent_id, provider, method, country, currency, reason):
        return self.emit(AuditEvent(
            event_type="router.decision", source="router", action="route",
            provider=provider, country=country, currency=currency,
            correlation_id=intent_id, payload={"method": method, "reason": reason}))

    def circuit_broken(self, provider, correlation_id=None):
        return self.emit(AuditEvent(
            event_type="router.circuit_breaker.open", source="router", action="break",
            severity="critical", provider=provider, correlation_id=correlation_id))

    def model_event(self, event_type, model_id, node_id=None, decision=None, evidence=None, data_egress=False):
        return self.emit(AuditEvent(
            event_type=event_type, source="model_fabric", action=event_type.split(".")[-1],
            resource_type="model", resource_id=model_id,
            payload={"node_id": node_id, "decision": decision or {}, "evidence": evidence or [],
                     "data_egress": data_egress}))

class AuditFeed:
    def __init__(self, repo, name, filter_spec=None):
        self.repo, self.name, self.filter = repo, name, filter_spec or {}

    def poll(self, batch_size=100):
        rows = self.repo.poll_audit_events(self.name, batch_size, self.filter)
        for row in rows:
            self.handle(row)
        if rows:
            self.repo.advance_cursor(self.name, rows[-1]["seq"])
        return len(rows)

    def handle(self, event):
        raise NotImplementedError

class ChainVerifier:
    def __init__(self, repo):
        self.repo = repo

    def verify(self):
        rows = self.repo.audit_events_ordered()
        prev = GENESIS_HASH
        problems = []
        for row in rows:
            if row["prev_hash"] != prev:
                problems.append(f"seq={row['seq']}: prev_hash broken")
            digest = hashlib.sha256((row["prev_hash"] + row["canonical"]).encode()).hexdigest()
            if digest != row["hash"]:
                problems.append(f"seq={row['seq']}: hash mismatch")
            prev = row["hash"]
        clean = not problems
        self.repo.emit_chain_result(clean, problems[:20])
        return clean, problems

def deterministic_canonical(event: AuditEvent) -> str:
    """Application-side reference serialization for tests; DB trigger remains authoritative."""
    selected = {
        "event_id": event.event_id, "occurred_at": event.occurred_at,
        "severity": event.severity, "source": event.source, "event_type": event.event_type,
        "resource_type": event.resource_type, "resource_id": event.resource_id,
        "provider": event.provider, "correlation_id": event.correlation_id,
        "amount_minor": event.amount_minor, "currency": event.currency, "payload": event.payload,
    }
    return json.dumps(selected, separators=(",", ":"), sort_keys=True, default=str)
