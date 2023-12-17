import pytest
import decimal
from datetime import datetime, timedelta
from functions.level_3.models import Expense
from functions.level_3.four_fraud import find_fraud_expenses

def test_find_fraud_expenses_with_fraud(sample_expenses_for_fraud_check):
    # When there are fraud expenses with a chain length greater than or equal to min_fraud_chain_length
    result = find_fraud_expenses(sample_expenses_for_fraud_check)
    assert len(result) == 2  # Expecting the two fraud transactions

def test_find_fraud_expenses_without_fraud(sample_expenses):
    # When there are no fraud expenses
    result = find_fraud_expenses(sample_expenses)
    assert len(result) == 0

def test_find_fraud_expenses_with_short_chain(sample_expenses_for_fraud_check):
    # When there is a fraud expense, but the chain length is less than min_fraud_chain_length
    # It should not be considered as fraud
    short_chain_fraud = Expense(
        amount=decimal.Decimal('2000.00'),
        currency='USD',
        card=sample_expenses_for_fraud_check[0].card,
        spent_in='Fraudville',
        spent_at=spent_at_date + timedelta(days=2),
        category=None
    )
    sample_expenses_for_fraud_check.append(short_chain_fraud)

    result = find_fraud_expenses(sample_expenses_for_fraud_check)
    assert len(result) == 2  # Expecting the two fraud transactions from the first chain only
