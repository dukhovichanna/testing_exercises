from functions.level_2.three_first import first, NOT_SET
import pytest

def test__first__with_items():
    assert first([1,2,3]) == 1

def test__first__with_empty_items_and_int_default():
    assert first([],3) == 3

def test__first__with_empty_items_and_str_default():
    assert first([],'test') == 'test'

def test__first__with_empty_items_and_no_default():
    with pytest.raises(AttributeError):
        first([])

def test__first__with_empty_items_and_default_set_to_not_set():
    with pytest.raises(AttributeError):
        first([], default=NOT_SET)