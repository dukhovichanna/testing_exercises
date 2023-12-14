import pytest
from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense
import datetime
import decimal

@pytest.mark.parametrize(
    "sms, cards, expected_result",
    [
        pytest.param(
            SmsMessage(
                text="1000.00 USD, 1234123412341234 23.11.23 15:29 UNIQLO authcode XXXX", 
                author="company", sent_at=datetime.datetime(2023, 11, 23, 15, 30)
            ), 
            [BankCard(last_digits="1234", owner="Jane")], 
            Expense(
                amount=decimal.Decimal('1000.00'),
                card=BankCard(last_digits='1234', owner='Jane'),
                spent_in='UNIQLO',
                spent_at=datetime.datetime(2023, 11, 23, 15, 29),
        ), id="return_true_when_valid_expense"),
        pytest.param(
            SmsMessage(
                text="1000.00 USD, 1234123412345647 23.11.23 15:29 UNIQLO authcode XXXX", 
                author="company", sent_at=datetime.datetime(2023, 11, 23, 15, 30)
            ), 
            [BankCard(last_digits="1234", owner="Jane")], 
            Expense(
                amount=decimal.Decimal('1000.00'),
                card=BankCard(last_digits='1234', owner='Jane'),
                spent_in='UNIQLO',
                spent_at=datetime.datetime(2023, 11, 23, 15, 29),
        ), id="return_false_when_invalid_card",                     
        marks=pytest.mark.xfail(reason='card is not valid'))        # Не уверена, что правильно обрабатываю этот случай. Может нужно как-то raise error?
    ]
)
def test__parse_ineco_expense(sms, cards, expected_result):
    result = parse_ineco_expense(sms,cards)
    assert result == expected_result

