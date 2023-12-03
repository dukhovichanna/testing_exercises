from functions.level_2.five_replace_word import replace_word

def test__replace_word__basic_functionality():
    assert replace_word('banana apple orange', 'banana', 'kiwi') == 'kiwi apple orange'

def test__replace_word__empty_text():
    assert replace_word('', 'banana', 'orange') == ''

def test__replace_word__empty_replace_from():
    assert replace_word('banana orange apple', '', 'orange') == 'banana orange apple'

def test__replace_word__empty_replace_to():
    assert replace_word('banana orange apple', 'banana', '') == ' orange apple'

def test__replace_word__empty_all_args():
    assert replace_word('', '', '') == ''

def test__replace_word__multiple_replacements():
    assert replace_word('banana orange apple banana', 'banana', 'kiwi') == 'kiwi orange apple kiwi'



    