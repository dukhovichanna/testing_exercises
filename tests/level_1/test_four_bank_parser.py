from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense
import datetime
import decimal


def test_parse_ineco_expense():
    sms = SmsMessage(text="1000.00 USD, 1234123412341234 23.11.23 15:29 UNIQLO authcode XXXX", author="company", sent_at=datetime.datetime(2023, 11, 23, 15, 30))
    cards = [BankCard(last_digits="1234", owner="Jane")]
    result = parse_ineco_expense(sms,cards)
    expected = Expense(amount=decimal.Decimal('1000.00'), card=BankCard(last_digits='1234', owner='Jane'), spent_in='UNIQLO', spent_at=datetime.datetime(2023, 11, 23, 15, 29))
    assert result == expected

