import pytest
from functions.level_1.five_title import change_copy_item

@pytest.mark.parametrize("title, max_main_item_title_length, expected", [
    pytest.param("Thermodynamics", None, "Copy of Thermodynamics", id="copy_when_default"),
    pytest.param("Thermodynamics", 5, "Thermodynamics", id="do_not_copy_when_short_title"),
    pytest.param("Copy of Thermodynamics", None, "Copy of Thermodynamics (2)", id="increment_copy_when_copy_exists"),
    pytest.param("Copy of Thermodynamics (2)", None, "Copy of Thermodynamics (3)", id="increment_copy_when_existing_copy"),
    pytest.param("Copy of Thermodynamics (2)", 5, "Copy of Thermodynamics (2)", id="do_not_increment_when_short_title"),
])
def test_change_copy_item(title, max_main_item_title_length, expected):
    if max_main_item_title_length is None:
        max_main_item_title_length = 100

    result = change_copy_item(title, max_main_item_title_length)
    
    assert result == expected
