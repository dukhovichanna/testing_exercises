from functions.level_1.five_title import change_copy_item
import pytest

@pytest.mark.paramterize(
        'title, max_main_item_title_length, expected_result',
        [
            ('Thermodynamics', None, 'Copy of Thermodynamics'),
            ('Thermodynamics', 5, 'Thermodynamics'),
            ('Copy of Thermodynamics', None, 'Copy of Thermodynamics (2)'),
            ('Copy of Thermodynamics (2)', None, 'Copy of Thermodynamics (3)'),
            ('Copy of Thermodynamics (2)', 5, 'Copy of Thermodynamics (2)')
        ]
)
def test__change_copy_item(title, max_main_item_title_length, expected_result):
    assert change_copy_item(title, max_main_item_title_length) is expected_result
