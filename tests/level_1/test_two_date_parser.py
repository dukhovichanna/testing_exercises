import pytest
from freezegun import freeze_time
from functions.level_1.two_date_parser import compose_datetime_from
import datetime

@freeze_time("2023-12-4 12:30:00")
@pytest.mark.parametrize(
        "date_str, time_str, expected_result",
        [
            pytest.param("today", "12:30", datetime.datetime(2023, 12, 4, 12, 30), id="compose_datetime_from_today_at_12:30"),
            pytest.param("tomorrow", "15:45", datetime.datetime(2023, 12, 5, 15, 45), id="compose_datetime_from_tomorrow_at_15:45")
        ]
)
def test__compose_datetime_from(date_str, time_str, expected_result):
    result = compose_datetime_from(date_str, time_str)

    assert result == expected_result