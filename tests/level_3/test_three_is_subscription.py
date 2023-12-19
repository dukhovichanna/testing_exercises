import pytest
import decimal
from datetime import timedelta
from functions.level_3.models import Expense
from functions.level_3.three_is_subscription import is_subscription

def test_is_subscription_with_subscription(sample_expenses_for_subscription_check):
    result = is_subscription(sample_expenses_for_subscription_check[0], sample_expenses_for_subscription_check)
    assert result is True

def test_is_subscription_without_subscription(sample_expenses_for_subscription_check, sample_expenses):
    result = is_subscription(sample_expenses_for_subscription_check[0], sample_expenses)
    assert result is False

def test_is_subscription_with_multiple_per_month(sample_expenses_for_subscription_check):
    extra_expense = Expense(
        amount=decimal.Decimal('20.50'),
        currency='USD',
        card=sample_expenses_for_subscription_check[0].card,
        spent_in=sample_expenses_for_subscription_check[0].spent_in,
        spent_at=sample_expenses_for_subscription_check[0].spent_at + timedelta(days=1),
        category=None
    )
    sample_expenses_for_subscription_check.append(extra_expense)
    
    result = is_subscription(sample_expenses_for_subscription_check[0], sample_expenses_for_subscription_check)
    assert result is False

