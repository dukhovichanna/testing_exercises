from functions.level_1.five_title import change_copy_item


def test_change_copy_item():
    assert change_copy_item('Thermodynamics') == 'Copy of Thermodynamics'
    assert change_copy_item('Thermodynamics', 5) == 'Thermodynamics'
    assert change_copy_item('Copy of Thermodynamics') == 'Copy of Thermodynamics (2)'
    assert change_copy_item('Copy of Thermodynamics (2)') == 'Copy of Thermodynamics (3)'
    assert change_copy_item('Copy of Thermodynamics (2)', 5) == 'Copy of Thermodynamics (2)'
