import pytest
from functions.level_1.one_gender import genderalize

@pytest.mark.parametrize(
        'verb_male, verb_female, gender, expected_result',
        [
            ('учился', 'училась', 'male', 'учился'),
            ('учился', 'училась', 'blah', 'учился'),
            ('учился', 'училась', 'female', 'училась')
        ]
)
def test_genderalize(verb_male, verb_female, gender, expected_result):
    result = genderalize(verb_male, verb_female, gender)
    
    if gender not in ('male','female'):
        assert result is not expected_result
    else:
        assert result is expected_result

@pytest.mark.parametrize(
        'verb_male, verb_female, gender, expected_result',
        [

            ('учился', 'училась', 'blah', 'учился')
        ]
)
def test_genderalize_false(verb_male, verb_female, gender, expected_result):
    assert genderalize(verb_male, verb_female, gender) is not expected_result
