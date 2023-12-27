import pytest
from functions.level_2.two_square_equation import solve_square_equation

@pytest.mark.parametrize(
    "square_coeff, linear_coeff, const_coeff, expected",
    [
        pytest.param(1.0, -3.0, 2.0, (1.0, 2.0), id='basic_functionality'),
        pytest.param(5.0, 3.0, 1.0, (None, None), id='discriminant_less_than_zero'),
        pytest.param(1.0, -4.0, 4.0, (2.0, 2.0), id='discriminant_equals_zero'),
        pytest.param(0.0, 0.0, 5.0, (None, None), id='no_square_coefficient_no_linear_coefficient'),
        pytest.param(0.0, 2.0, -8.0, (4.0, None), id='no_square_coefficient_with_linear_coefficient'),
        pytest.param(1.0, -3.0, 0.0, (0.0, 3.0), id='no_constant_coefficient'),
    ]
)
def test__solve_square_equation(square_coeff, linear_coeff, const_coeff, expected):
    result = solve_square_equation(square_coeff, linear_coeff, const_coeff)

    assert result == expected