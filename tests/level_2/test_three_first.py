import pytest
from functions.level_2.three_first import first, NOT_SET

@pytest.mark.parametrize(
    "items, default, expected",
    [
        pytest.param([1, 2, 3], NOT_SET, 1, id='return_first_item_with_non_empty_items'),
        pytest.param([], 3, 3, id='return_default_with_empty_items_and_int_default'),
        pytest.param([], 'test', 'test', id='return_default_with_empty_items_and_str_default'),
        pytest.param([], NOT_SET, None, id='raise_error_with_empty_items_and_no_default'),
        pytest.param([], NOT_SET, None, id='raise_error_with_empty_items_and_default_set_to_not_set'),
    ]
)
def test__first(items, default, expected):
    if (default == NOT_SET) and (items == []):
        with pytest.raises(AttributeError):
            result = first(items)
    else:
        result = first(items, default)
        
        assert result == expected
