import pytest
from functions.level_3.two_expense_categorizer import guess_expense_category, is_string_contains_trigger
from functions.level_3.models import ExpenseCategory

def test__guess_expense_category__successful_category_detection(sample_expense_with_trigger):
    result = guess_expense_category(sample_expense_with_trigger)
    assert result == ExpenseCategory.THEATRES_MOVIES_CULTURE

def test__guess_expense_category__return_none_when_no_trigger_detected(sample_expense_without_trigger):
    result = guess_expense_category(sample_expense_without_trigger)
    assert result is None

@pytest.mark.parametrize("input_string, trigger, expected_result", [
    ("Moscow Cinema", "cinema", True),
    ("Random Store", "cinema", False),
    ("Cinema", "cinema", True),
    ("Cinema.", "cinema", True),
    ("Cinema-Gallery", "cinema", True),
    ("Cinema / Gallery", "cinema", True),
    ("Grocery Store", "cinema", False),
])
def test__is_string_contains_trigger(input_string, trigger, expected_result):
    result = is_string_contains_trigger(input_string, trigger)
    assert result == expected_result