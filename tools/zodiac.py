import datetime
import re

from zodiac_sign import get_zodiac_sign


def fetch_zodiac_sign(date: str):
    """Return zodiac sign by date.
    Arguments:
      - date: str - "dd.mm.yyyy"
    """
    date = re.findall(r"(\d{1,2})\.(\d{1,2})\.(\d{4})", date)
    if date:
        day, month, year = map(int, date[0])
        try:
            date_object = datetime.date(day=day, month=month, year=year)
        except ValueError:
            return None
        return get_zodiac_sign(date_object) 
    return None
