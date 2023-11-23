from functions.level_1.two_date_parser import compose_datetime_from
import datetime


def test_compose_datetime_from():
    result = compose_datetime_from("today", "12:30")
    expected = datetime.datetime.now().replace(hour=12, minute=30, second=0, microsecond=0)
    assert result == expected

    result = compose_datetime_from("tomorrow", "15:45")
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    expected = datetime.datetime(tomorrow.year, tomorrow.month, tomorrow.day, 15, 45)
    assert result == expected
