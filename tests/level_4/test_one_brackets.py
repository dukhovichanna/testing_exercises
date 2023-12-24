import pytest
from functions.level_4.one_brackets import delete_remove_brackets_quotes

def test__delete_remove_brackets_quotes__return_string_without_brackets_when_input_has_brackets():
    result = delete_remove_brackets_quotes("{ example }")
    assert result == "example"

def test__delete_remove_brackets__return_same_string_when_input_has_no_brackets():
    result = delete_remove_brackets_quotes("example")
    assert result == "example"

def test__delete_remove_brackets_quotes__raise_error_when_input_is_empty_string():
    with pytest.raises(IndexError):
        result = delete_remove_brackets_quotes("")

def test__delete_remove_brackets_quotes__return_shortened_str_when_no_space_between_brackets_and_str():
    result = delete_remove_brackets_quotes("{abc}")
    assert result == "b"

def test__delete_remove_brackets_quotes__return_shorter_string_when_input_has_missing_closing_bracket():
    result = delete_remove_brackets_quotes("{ abc ")
    assert result == "ab"

def test__delete_remove_brackets_quotes__return_full_input_str_with_closing_bracket_when_input_has_missing_opening_bracket():
    result = delete_remove_brackets_quotes("abc}")
    assert result == "abc}"
