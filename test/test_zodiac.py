"""Test zodiac module."""

from tools.zodiac import fetch_zodiac_sign


def test_valid_date_to_sign():
    """Valid date."""
    date = "28.08.1982"
    assert fetch_zodiac_sign(date) == "Virgo"


def test_invalid_format_date_to_none():
    """Wrong date format - dd.mm.yyyy ."""
    date = "28.08.198"
    assert fetch_zodiac_sign(date) is None


def test_invalid_date_to_none():
    """Not valid date - 30 feb or 13 month.""" 
    date = "30.02.2000"
    assert fetch_zodiac_sign(date) is None
