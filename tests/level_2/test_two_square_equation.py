from functions.level_2.two_square_equation import solve_square_equation

def test__solve_square_equation__basic_functionality():
    result = solve_square_equation(1.0, -3.0, 2.0)
    assert result == (1.0, 2.0)

def test__solve_square_equation__discriminant_less_than_zero():
    result = solve_square_equation(5.0, 3.0, 1.0)
    assert result == (None, None)

def test__solve_square_equation__discriminant_equals_zero():
    result = solve_square_equation(1.0, -4.0, 4.0)
    assert result == (2.0, 2.0)

def test__solve_square_equation__no_square_coefficient_no_linear_coefficient():
    result = solve_square_equation(0.0, 0.0, 5.0)
    assert result == (None, None)

def test__solve_square_equation__no_square_coefficient_with_linear_coefficient():
    result = solve_square_equation(0.0, 2.0, -8.0)
    assert result == (4.0, None)

def test__solve_square_equation__no_constant_coefficient():
    result = solve_square_equation(1.0, -3.0, 0.0)
    assert result == (0.0, 3.0)
