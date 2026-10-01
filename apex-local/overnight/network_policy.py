"""Overnight network policy: local services only, except explicit notifier transport."""
from urllib.parse import urlparse

LOOPBACK_HOSTS = {"127.0.0.1", "localhost", "::1", "[::1]"}


def assert_local_target(url: str) -> None:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or parsed.hostname not in LOOPBACK_HOSTS:
        raise ValueError(f"overnight network target is not loopback: {parsed.hostname or '<missing>'}")


def is_local_target(url: str) -> bool:
    try:
        assert_local_target(url)
        return True
    except ValueError:
        return False
