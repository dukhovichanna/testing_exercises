from functions.level_2.five_replace_word import replace_word

def test_basic_functionality():
    assert replace_word('banana apple orange', 'banana', 'kiwi') == 'kiwi apple orange'

def test_empty_text():
    assert replace_word('', 'banana', 'orange') == ''

def test_empty_replace_from():
    assert replace_word('banana orange apple', '', 'orange') == 'banana orange apple'

def test_empty_replace_to():
    assert replace_word('banana orange apple', 'banana', '') == ' orange apple'

def test_empty_all_args():
    assert replace_word('', '', '') == ''

def test_multiple_replacements():
    assert replace_word('banana orange apple banana', 'banana', 'kiwi') == 'kiwi orange apple kiwi'



    