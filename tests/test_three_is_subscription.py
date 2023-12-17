import pytest
import decimal
from datetime import timedelta
from functions.level_3.models import Expense
from functions.level_3.three_is_subscription import is_subscription

def test_is_subscription_with_subscription(sample_expenses_for_subscription_check):
    # When there are at least 3 expenses with the same spent_in value and only 1 per month
    result = is_subscription(sample_expenses_for_subscription_check[0], sample_expenses_for_subscription_check[1:])
    assert result is True

def test_is_subscription_without_subscription(sample_expenses):
    # When there are less than 3 expenses with the same spent_in value
    result = is_subscription(sample_expenses[0], sample_expenses[1:])
    assert result is False

def test_is_subscription_with_multiple_per_month(sample_expenses_for_subscription_check):
    # When there are at least 3 expenses with the same spent_in value, but more than 1 per month
    # It should still return False
    extra_expense_3 = Expense(
        amount=decimal.Decimal('40.00'),
        currency='USD',
        card=sample_expenses_for_subscription_check[0].card,
        spent_in=sample_expenses_for_subscription_check[0].spent_in,
        spent_at=sample_expenses_for_subscription_check[0].spent_at + timedelta(days=1),
        category=None
    )
    sample_expenses_for_subscription_check.append(extra_expense_3)
    
    result = is_subscription(sample_expenses_for_subscription_check[0], sample_expenses_for_subscription_check[1:])
    assert result is False

