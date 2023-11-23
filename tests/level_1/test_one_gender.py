from functions.level_1.one_gender import genderalize


def test_genderalize():
    assert genderalize('учился','училась','male') == 'учился'
    assert not genderalize('учился','училась','blah') == 'учился'
    assert genderalize('учился','училась','female') == 'училась'

