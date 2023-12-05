import pytest
from functions.level_2.five_replace_word import replace_word

@pytest.mark.parametrize(
    "text, replace_from, replace_to, expected",
    [
        pytest.param('banana apple orange', 'banana', 'kiwi', 'kiwi apple orange', 
                     id='replace_one_word'),
        pytest.param('', 'banana', 'orange', '', 
                     id='return_empty_str_when_empty_text'),
        pytest.param('banana orange apple', '', 'orange', 'banana orange apple', 
                     id='return_text_when_empty_replace_from'),
        pytest.param('banana orange apple', 'banana', '', ' orange apple', 
                     id='return_text_without_replace_from_when_empty_replace_to'),
        pytest.param('', '', '', '', 
                     id='return_empty_str_when_all_args_empty'),
        pytest.param('banana orange apple banana', 'banana', 'kiwi', 'kiwi orange apple kiwi', 
                     id='replace_multiple_occurances_of_replace_from_word'),
    ]
)
def test__replace_word(text, replace_from, replace_to, expected):
    result = replace_word(text, replace_from, replace_to)
    assert result == expected
