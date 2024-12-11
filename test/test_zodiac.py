from tools.zodiac import fetch_zodiac_sign


def test_valid_date_to_sign():
    date = "28.08.1982"
    assert fetch_zodiac_sign(date) == "Virgo"


def test_invalid_format_date_to_none():
    date = "28.08.198"
    assert fetch_zodiac_sign(date) == None


def test_invalid_date_to_none():
    date = "30.02.2000"
    assert fetch_zodiac_sign(date) == None
