import pytest
from functions.level_1.one_gender import genderalize

@pytest.mark.parametrize(
        'verb_male, verb_female, gender, expected_result',
        [
            pytest.param('учился', 'училась', 'male', 'учился', id='return_true_when_male_gender'),
            pytest.param('учился', 'училась', 'blah', 'учился', id='return_false_for_neither_male_nor_female_gender', marks=pytest.mark.xfail(reason='gender is not valid')),
            pytest.param('учился', 'училась', 'female', 'училась', id='return_true_when_female_gender')
        ]
)
def test_genderalize(verb_male, verb_female, gender, expected_result):
    result = genderalize(verb_male, verb_female, gender)

    assert result is expected_result
