from functions.level_1.five_title import change_copy_item
import pytest

@pytest.mark.paramterize(
        "title, max_main_item_title_length, expected_result",
        [
            ('Thermodynamics', None, 'Copy of Thermodynamics')
        ]
)
def test_change_copy_item(title, max_main_item_title_length, expected_result):
    ##assert change_copy_item('Thermodynamics') == 'Copy of Thermodynamics'
    # assert change_copy_item('Thermodynamics', 5) == 'Thermodynamics'
    # assert change_copy_item('Copy of Thermodynamics') == 'Copy of Thermodynamics (2)'
    # assert change_copy_item('Copy of Thermodynamics (2)') == 'Copy of Thermodynamics (3)'
    # assert change_copy_item('Copy of Thermodynamics (2)', 5) == 'Copy of Thermodynamics (2)'
    assert change_copy_item(title, max_main_item_title_length) is expected_result
