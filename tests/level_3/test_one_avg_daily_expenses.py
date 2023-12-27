import pytest
from functions.level_3.one_avg_daily_expenses import calculate_average_daily_expenses
import decimal
from statistics import StatisticsError

def test__calculate_average_daily_expenses__assert_result_is_decimal(sample_expenses):
    result = calculate_average_daily_expenses(sample_expenses)    
    assert isinstance(result, decimal.Decimal)

def test__calculate_average_daily_expenses__list_of_sample_valid_expenses(sample_expenses):
    result = calculate_average_daily_expenses(sample_expenses)
    assert result == decimal.Decimal('135.25')


def test__calculate_average_daily_expenses__raise_error_when_empty_list_of_expenses():
    with pytest.raises(StatisticsError):
        calculate_average_daily_expenses([])


def test__calculate_average_daily_expenses__single_valid_expense(sample_expenses):
    single_expense = [sample_expenses[0]]
    result = calculate_average_daily_expenses(single_expense)
    assert result == sample_expenses[0].amount
