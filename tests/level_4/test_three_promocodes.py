from functions.level_4.three_promocodes import generate_promocode

def test__generate_promocode__return_true_if_default_length_is_8():
    code = generate_promocode()
    assert len(code) == 8

def test__generate_promocode__return_true_if_code_contains_only_alphabetic_characters():
    code = generate_promocode()
    assert code.isalpha()

def test__generate_promocode__return_true_if_code_len_equals_custom_length():
    code = generate_promocode(12)
    assert len(code) == 12

def test__generate_promocode__return_empty_str_for_invalid_length():
    code = generate_promocode(-1)
    assert len(code) == 0

def test_generate_promocode_return_empty_str_for_zero_length():
    code = generate_promocode(0)
    assert len(code) == 0

def test__generate_promocode__return_true_if_promocode_is_uppercase():
    code = generate_promocode(10)
    assert code.isupper()

