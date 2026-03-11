
from app.tokens import token_from_iso
from datetime import datetime, timezone

def test_token_from_iso_handles_timezone_correctly():
    iso_string = "2026-03-11T12:00:00Z"
    expected_dt = datetime(2026, 3, 11, 12, 0, 0, tzinfo=timezone.utc)
    expected_timestamp = int(expected_dt.timestamp())
    
    token = token_from_iso("test-token", iso_string)
    
    assert token.expires_at == expected_timestamp



def test_token_from_iso_with_explicit_offset():
    """
    Test that the function handles explicit timezone offsets (e.g., +05:00)
    and correctly normalizes them to a UTC Unix timestamp.
    """
    iso_string_with_offset = "2026-03-11T12:00:00+05:00"
    
    expected_utc_dt = datetime(2026, 3, 11, 7, 0, 0, tzinfo=timezone.utc)
    expected_timestamp = int(expected_utc_dt.timestamp())
    
    token = token_from_iso("offset-token", iso_string_with_offset)
    
    assert token.expires_at == expected_timestamp, (
        f"Failed: Expected {expected_timestamp}, got {token.expires_at}. "
        "The code likely ignored the +05:00 offset."
    )