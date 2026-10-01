import time

import pytest

from apex.private import PrivateMode, fingerprint


def test_private_mode_blocks_when_off():
    p = PrivateMode()
    with pytest.raises(PermissionError):
        p.put("test@example.com", "email_delivery_test")


def test_private_phone_email_are_masked_and_single_use():
    p = PrivateMode(ttl_seconds=60)
    p.enable()

    phone = p.put("312-555-0100", "sms_test")
    email = p.put("test@example.com", "email_test")

    assert phone["kind"] == "phone"
    assert email["kind"] == "email"
    assert "555-0100" not in str(phone)
    assert "test@example.com" not in str(email)

    assert p.consume(phone["lease_id"], "sms_test") == "312-555-0100"
    with pytest.raises(PermissionError):
        p.consume(phone["lease_id"], "sms_test")

    assert p.consume(email["lease_id"], "email_test") == "test@example.com"


def test_private_lease_expires():
    p = PrivateMode(ttl_seconds=0.01)
    p.enable()
    lease = p.put("test@example.com", "email_test")
    time.sleep(0.02)
    with pytest.raises(PermissionError):
        p.consume(lease["lease_id"], "email_test")


def test_fingerprint_is_non_secret_length():
    fp = fingerprint("test@example.com")
    assert len(fp) == 16
    assert "@" not in fp
