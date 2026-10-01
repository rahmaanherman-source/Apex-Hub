"""Minimal local API helpers for the APEX PRIVATE mode.

The API surface returns only public metadata. Values are consumed internally
through a purpose-bound, single-use, 60-second lease.
"""
from __future__ import annotations

from .private import PrivateMode

PRIVATE = PrivateMode(ttl_seconds=60)


def enable_private() -> dict:
    PRIVATE.enable()
    return {"private": True, "label": "PRIVATE: ON", "ttl_seconds": PRIVATE.ttl_seconds}


def disable_private() -> dict:
    PRIVATE.disable()
    return {"private": False, "label": "PRIVATE: OFF"}


def put_private(value: str, purpose: str = "local_test") -> dict:
    return PRIVATE.put(value, purpose)


def consume_private(lease_id: str, purpose: str = "local_test") -> str:
    return PRIVATE.consume(lease_id, purpose)


def status() -> dict:
    return {
        "private": PRIVATE.enabled,
        "label": "PRIVATE: ON" if PRIVATE.enabled else "PRIVATE: OFF",
        "active_leases": len(PRIVATE._leases),
        "ttl_seconds": PRIVATE.ttl_seconds,
    }
