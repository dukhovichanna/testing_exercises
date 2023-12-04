import pytest
from functions.level_1.one_gender import genderalize

@pytest.mark.parametrize(
        'verb_male, verb_female, gender, expected_result',
        [
            pytest.param('учился', 'училась', 'male', 'учился', id='male_gender'),
            pytest.param('учился', 'училась', 'blah', 'учился', id='return_false_for_neither_male_nor_female_gender'),
            pytest.param('учился', 'училась', 'female', 'училась', id='female_gender')
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
