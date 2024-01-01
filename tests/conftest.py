import datetime
from dateutil.relativedelta import relativedelta
import decimal
import pytest
import os
from functions.level_3.models import Expense, BankCard
from functions.level_4.two_students import Student

@pytest.fixture
def sample_bank_card():
    return BankCard(last_digits='1234', owner='Jane')

@pytest.fixture
def spent_at_date():
    return datetime.datetime(2023, 11, 23, 15, 29)

@pytest.fixture
def subscription_amount():
    return decimal.Decimal('20.50')

@pytest.fixture
def make_expense(sample_bank_card, spent_at_date):
    def inner(
        amount: decimal.Decimal | None = None, 
        currency: str | None = None,
        spent_in: str | None = None,
        spent_at: datetime.datetime | None = None,
        category: str | None = None
    ):
        return Expense(
            amount=amount or decimal.Decimal('20.50'),
            currency=currency or 'USD',
            card=sample_bank_card,
            spent_in=spent_in or 'Moscow Cinema',
            spent_at=spent_at or spent_at_date,
            category=category
        )
    return inner

@pytest.fixture
def sample_expense_with_trigger(make_expense):
    return make_expense()

@pytest.fixture
def sample_expense_without_trigger(make_expense, spent_at_date):
    return make_expense(
        amount=decimal.Decimal('250.00'),
        spent_in='Random Store', 
        spent_at=spent_at_date + datetime.timedelta(days=1))

@pytest.fixture
def sample_expenses(sample_expense_with_trigger, sample_expense_without_trigger):
    expenses = [
        sample_expense_with_trigger,
        sample_expense_without_trigger
    ]
    return expenses

@pytest.fixture
def sample_expenses_for_subscription_check(make_expense,spent_at_date):
    list_of_expenses = []

    for i in range(3):
        list_of_expenses.append(make_expense(spent_at=spent_at_date + relativedelta(month=+i)))

    return list_of_expenses

@pytest.fixture
def sample_expenses_for_fraud_check(sample_expense_with_trigger, sample_expense_without_trigger):
    fraud_expenses = [sample_expense_with_trigger] * 3
    normal_expense = sample_expense_without_trigger
    
    return fraud_expenses + [normal_expense]


@pytest.fixture
def sample_students():
    return [
        Student("John", "Doe", "@john_doe"),
        Student("Jane", "Smith", None),
        Student("Alice", "Johnson", "@alice_j"),
    ]


@pytest.fixture
def temp_file_with_content():
    content = "Line 1\n# Comment\nLine 2\nLine 3"
    file_path = "temp_file.txt"
    with open(file_path, "w") as file:
        file.write(content)

    yield file_path

    if os.path.exists(file_path):
        os.remove(file_path)

@pytest.fixture
def temp_config():
    temp_config_content = "[tool:app-config]\n" \
                          "extra_fields = \n" \
                          "    key1: 'value1'\n" \
                          "    key2: 42\n" \
                          "other_field1 = 'value2'\n" \
                          "other_field2 = 3.14"

    temp_config_path = "temp_config.cfg"
    with open(temp_config_path, "w") as f:
        f.write(temp_config_content)

    yield temp_config_path

    if os.path.exists(temp_config_path):
        os.remove(temp_config_path)
