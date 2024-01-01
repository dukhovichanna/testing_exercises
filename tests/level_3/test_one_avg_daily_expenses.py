import pytest
import datetime
from functions.level_3.one_avg_daily_expenses import calculate_average_daily_expenses
import decimal
from statistics import StatisticsError


def test__calculate_average_daily_expenses__list_of_sample_valid_expenses(make_expense, spent_at_date):
    expenses = [
        make_expense(amount=decimal.Decimal('15.00')),
        make_expense(
            amount=decimal.Decimal('50.00'),
            spent_at=spent_at_date + datetime.timedelta(days=1)),
        make_expense(
            amount=decimal.Decimal('25.00'),
            spent_at=spent_at_date + datetime.timedelta(days=2))
    ]
    result = calculate_average_daily_expenses(expenses)
    assert result == decimal.Decimal('30.00')


def test__calculate_average_daily_expenses__raise_error_when_empty_list_of_expenses():
    with pytest.raises(StatisticsError):
        calculate_average_daily_expenses([])


def test__calculate_average_daily_expenses__single_valid_expense(sample_expenses):
    single_expense = [sample_expenses[0]]
    result = calculate_average_daily_expenses(single_expense)
    assert result == sample_expenses[0].amount
