"""Deterministic HMAC signing for release manifests.

The signing secret is supplied at runtime through APEX_RELEASE_HMAC_SECRET and
is never persisted in the repository or evidence layer.
"""
from __future__ import annotations
import hashlib
import hmac
import json
import os
from pathlib import Path


def canonical_manifest_bytes(manifest: dict) -> bytes:
    return json.dumps(manifest, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sign_manifest(manifest: dict) -> str:
    secret = os.environ.get("APEX_RELEASE_HMAC_SECRET")
    if not secret:
        raise RuntimeError("APEX_RELEASE_HMAC_SECRET is required; refusing unsigned release")
    return hmac.new(secret.encode("utf-8"), canonical_manifest_bytes(manifest), hashlib.sha256).hexdigest()


def verify_manifest(manifest: dict, signature: str) -> bool:
    secret = os.environ.get("APEX_RELEASE_HMAC_SECRET")
    if not secret:
        return False
    expected = hmac.new(secret.encode("utf-8"), canonical_manifest_bytes(manifest), hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature)
