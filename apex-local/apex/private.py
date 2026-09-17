"""Private data lane for local test credentials.

Private mode is an explicit runtime guard: personal contact data is treated as
sensitive, routed to the local Gatekeeper boundary for storage/use, and must
never be emitted to ordinary chat responses, logs, telemetry, or source.
"""
from __future__ import annotations

import hashlib
import re
import secrets
import time
from dataclasses import dataclass
from typing import Optional

_PHONE_RE = re.compile(r"(?:\+?1[\s.-]?)?(?:\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4})")
_EMAIL_RE = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)

DEFAULT_TTL_SECONDS = 60


def mask(value: str, visible: int = 2) -> str:
    if not value:
        return "••••"
    return "•" * max(4, len(value) - visible) + value[-visible:]


def classify(value: str) -> str:
    if _EMAIL_RE.fullmatch(value.strip()):
        return "email"
    if _PHONE_RE.fullmatch(value.strip()):
        return "phone"
    return "private"


@dataclass
class PrivateLease:
    lease_id: str
    kind: str
    value: str
    created_at: float
    expires_at: float
    purpose: str

    def expired(self) -> bool:
        return time.monotonic() >= self.expires_at

    def public_record(self) -> dict:
        return {
            "lease_id": self.lease_id,
            "kind": self.kind,
            "masked": mask(self.value),
            "expires_in_seconds": max(0, int(self.expires_at - time.monotonic())),
            "purpose": self.purpose,
        }


class PrivateMode:
    """One-toggle privacy boundary for personal contact data.

    The gatekeeper remains the only component that should persist or release
    the value. This class represents the short-lived authorization lease used
    by local test workflows.
    """

    def __init__(self, ttl_seconds: int = DEFAULT_TTL_SECONDS) -> None:
        self.ttl_seconds = ttl_seconds
        self.enabled = False
        self._leases: dict[str, PrivateLease] = {}

    def enable(self) -> None:
        self.enabled = True

    def disable(self) -> None:
        self.enabled = False
        self._leases.clear()

    def put(self, value: str, purpose: str) -> dict:
        if not self.enabled:
            raise PermissionError("PRIVATE mode is OFF")
        value = value.strip()
        if not value:
            raise ValueError("Private value cannot be empty")
        kind = classify(value)
        lease_id = secrets.token_urlsafe(18)
        now = time.monotonic()
        lease = PrivateLease(
            lease_id=lease_id,
            kind=kind,
            value=value,
            created_at=now,
            expires_at=now + self.ttl_seconds,
            purpose=purpose,
        )
        self._leases[lease_id] = lease
        return lease.public_record()

    def consume(self, lease_id: str, purpose: str) -> str:
        if not self.enabled:
            raise PermissionError("PRIVATE mode is OFF")
        lease = self._leases.pop(lease_id, None)
        if lease is None or lease.expired():
            raise PermissionError("Private lease expired or invalid")
        if lease.purpose != purpose:
            raise PermissionError("Private lease purpose mismatch")
        return lease.value

    def redact_text(self, text: str) -> str:
        text = _EMAIL_RE.sub("[PRIVATE_EMAIL]", text)
        text = _PHONE_RE.sub("[PRIVATE_PHONE]", text)
        return text


def fingerprint(value: str) -> str:
    """Stable non-secret fingerprint for local verification evidence."""
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:16]
