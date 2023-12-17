import pytest
from functions.level_3.two_expense_categorizer import guess_expense_category, is_string_contains_trigger
from functions.level_3.models import ExpenseCategory

def test__guess_expense_category__successful_detection(sample_expense_with_trigger):
    result = guess_expense_category(sample_expense_with_trigger)
    assert result == ExpenseCategory.THEATRES_MOVIES_CULTURE

def test__guess_expense_category__no_trigger_detected(sample_expense_without_trigger):
    result = guess_expense_category(sample_expense_without_trigger)
    assert result is None

def test__is_string_contains_trigger__starts_with(sample_expense_with_trigger):
    result = is_string_contains_trigger(sample_expense_with_trigger.spent_in, "moscow")
    assert result is True

def test__is_string_contains_trigger__ends_with(sample_expense_with_trigger):
    result = is_string_contains_trigger(sample_expense_with_trigger.spent_in, "cinema")
    assert result is True

def test__is_string_contains_trigger__in_middle(sample_expense_with_trigger):
    result = is_string_contains_trigger(sample_expense_with_trigger.spent_in, "cinema")
    assert result is True

def test__is_string_contains_trigger__not_present(sample_expense_without_trigger):
    result = is_string_contains_trigger(sample_expense_without_trigger.spent_in, "cinema")
    assert result is False