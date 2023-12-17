import datetime
import decimal
import pytest
from functions.level_3.models import Expense, Currency, BankCard, ExpenseCategory

@pytest.fixture
def sample_bank_card():
    return BankCard(last_digits='1234', owner='Jane')

@pytest.fixture
def spent_at():
    return datetime.datetime(2023, 11, 23, 15, 29)

@pytest.fixture
def sample_expense_with_trigger(spent_at):
    return Expense(
        amount=decimal.Decimal('1000.00'),
        currency='USD',
        card=None,
        spent_in='Moscow Cinema',
        spent_at=spent_at,
        category=None
    )

@pytest.fixture
def sample_expense_without_trigger(spent_at):
    return Expense(
        amount=decimal.Decimal('250.00'),
        currency='USD',
        card=None,
        spent_in='Random Store',
        spent_at=spent_at,
        category=None
    )

@pytest.fixture
def sample_expenses(sample_bank_card, sample_expense_with_trigger, sample_expense_without_trigger):
    expenses = [
        sample_expense_with_trigger,
        sample_expense_with_trigger,
        Expense(
        amount=decimal.Decimal('1000.00'),
        currency=Currency.USD,
        card=sample_bank_card,
        spent_in='HANNAFORD',
        spent_at=datetime.datetime(2023, 11, 23, 15, 29),
        category=ExpenseCategory.SUPERMARKET
        ),
        Expense(
            amount=decimal.Decimal('175.50'),
            currency=Currency.USD,
            card=sample_bank_card,
            spent_in='CBG',
            spent_at=datetime.datetime(2023, 1, 1, 8, 0, 0),
            category=ExpenseCategory.BAR_RESTAURANT
        ),
        Expense(
            amount=decimal.Decimal('20.75'),
            currency=Currency.EUR,
            card=sample_bank_card,
            spent_in='CVS',
            spent_at=datetime.datetime(2023, 1, 1, 12, 0, 0),
            category=ExpenseCategory.MEDICINE_PHARMACY
        )
    ]
    return expenses
