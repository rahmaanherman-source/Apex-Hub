"""Centralized secret redaction for overnight evidence and notifications."""
import re
from typing import Any

REDACT_KEYS = {
    "password", "passwd", "secret", "token", "api_key", "apikey", "private_key",
    "client_secret", "access_token", "refresh_token", "authorization",
    "shopify_admin_token", "stripe_secret_key", "stripe_key", "credential_value",
}

SECRET_PATTERNS = [
    re.compile(r"sk_(?:live|test)_[A-Za-z0-9]{16,}"),
    re.compile(r"shpat_[A-Za-z0-9]{16,}"),
    re.compile(r"shpca_[A-Za-z0-9]{16,}"),
    re.compile(r"AIza[0-9A-Za-z_-]{30,}"),
    re.compile(r"Bearer\s+[A-Za-z0-9._~+/=-]{16,}", re.I),
    re.compile(r"(?i)(?:password|secret|api[_-]?key|token|authorization)\s*[:=]\s*\S+"),
]


def contains_secret_like_value(text: str) -> bool:
    if not isinstance(text, str):
        return False
    return any(p.search(text) for p in SECRET_PATTERNS)


def _redact_string(value: str) -> str:
    if contains_secret_like_value(value):
        return "[REDACTED]"
    return value


def redact(value: Any, _key: str | None = None) -> Any:
    if _key and _key.lower() in REDACT_KEYS:
        return "[REDACTED]"
    if isinstance(value, dict):
        return {str(k): redact(v, str(k)) for k, v in value.items()}
    if isinstance(value, list):
        return [redact(v) for v in value]
    if isinstance(value, tuple):
        return tuple(redact(v) for v in value)
    if isinstance(value, str):
        return _redact_string(value)
    return value


def safe_error(exc: BaseException) -> str:
    return redact(f"{type(exc).__name__}: {exc}")
