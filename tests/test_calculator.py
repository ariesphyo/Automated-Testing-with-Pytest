import pytest

from src.calculator import calculate_average, factorial, find_maximum, is_prime, power


# Average tests cover rounding, supported sequence types, and validation of
# empty inputs, out-of-range scores, and invalid score values.
@pytest.mark.parametrize(
    ("scores", "expected"),
    [
        ([80, 90, 100], 90.0),
        ([0, 100], 50.0),
        ([10.5, 20.25], 15.38),
        ([42], 42.0),
        ((25, 75), 50.0),
    ],
)
def test_calculate_average_returns_rounded_average(scores, expected):
    assert calculate_average(scores) == expected


@pytest.mark.parametrize("scores", [[], ()])
def test_calculate_average_rejects_empty_sequences(scores):
    with pytest.raises(ValueError):
        calculate_average(scores)


@pytest.mark.parametrize("score", [-0.01, 100.01])
def test_calculate_average_rejects_scores_outside_valid_range(score):
    with pytest.raises(ValueError):
        calculate_average([score])


@pytest.mark.parametrize("scores", [None, 50, "50", {"score": 50}])
def test_calculate_average_rejects_non_sequence_input(scores):
    with pytest.raises(TypeError):
        calculate_average(scores)


@pytest.mark.parametrize("score", ["90", None, True, [90]])
def test_calculate_average_rejects_non_numeric_scores(score):
    with pytest.raises(TypeError):
        calculate_average([score])


# Maximum tests verify results for positive, negative, duplicate, and decimal
# values, along with the errors raised for empty or invalid input.
@pytest.mark.parametrize(
    ("numbers", "expected"),
    [
        ([1, 8, 3], 8),
        ([-8, -2, -5], -2),
        ([-4, 0, 6], 6),
        ([3.5], 3.5),
        ([2, 9, 9, 4], 9),
        ((-3, -7, -1), -1),
    ],
)
def test_find_maximum_returns_largest_value(numbers, expected):
    assert find_maximum(numbers) == expected


@pytest.mark.parametrize("numbers", [[], ()])
def test_find_maximum_rejects_empty_sequences(numbers):
    with pytest.raises(ValueError):
        find_maximum(numbers)


@pytest.mark.parametrize("numbers", [None, 12, "123", {"value": 12}])
def test_find_maximum_rejects_non_sequence_input(numbers):
    with pytest.raises(TypeError):
        find_maximum(numbers)


@pytest.mark.parametrize("number", ["12", None, True, [12]])
def test_find_maximum_rejects_non_numeric_elements(number):
    with pytest.raises(TypeError):
        find_maximum([number])


# Primality tests check values at and below the lower boundary, known primes,
# composite numbers, and rejection of values that are not integers.
@pytest.mark.parametrize("number", [-10, -1, 0, 1])
def test_is_prime_returns_false_for_numbers_at_most_one(number):
    assert is_prime(number) is False


@pytest.mark.parametrize("number", [2, 3, 29, 97])
def test_is_prime_returns_true_for_prime_numbers(number):
    assert is_prime(number) is True


@pytest.mark.parametrize("number", [4, 8, 16, 9, 15, 25, 49, 121])
def test_is_prime_returns_false_for_composite_numbers(number):
    assert is_prime(number) is False


@pytest.mark.parametrize("number", [2.0, True, "7", None])
def test_is_prime_rejects_non_integer_input(number):
    with pytest.raises(TypeError):
        is_prime(number)


# Factorial tests cover base cases and ordinary non-negative inputs, while
# confirming that negative and non-integer arguments raise the expected errors.
@pytest.mark.parametrize(("number", "expected"), [(0, 1), (1, 1), (5, 120), (7, 5040)])
def test_factorial_calculates_non_negative_integer_factorials(number, expected):
    assert factorial(number) == expected


def test_factorial_rejects_negative_input():
    with pytest.raises(ValueError):
        factorial(-1)


@pytest.mark.parametrize("number", [2.5, True, "5", None])
def test_factorial_rejects_non_integer_input(number):
    with pytest.raises(TypeError):
        factorial(number)


# Power tests exercise positive, zero, negative, and fractional-base cases,
# plus invalid arguments and the undefined zero-to-negative case.
@pytest.mark.parametrize(
    ("base", "exponent", "expected"),
    [
        (2, 3, 8),
        (5, 0, 1),
        (2, -2, 0.25),
        (2.5, 2, 6.25),
    ],
)
def test_power_calculates_valid_powers(base, exponent, expected):
    assert power(base, exponent) == expected


def test_power_rejects_zero_raised_to_negative_exponent():
    with pytest.raises(ValueError):
        power(0, -1)


@pytest.mark.parametrize("base", ["2", None, True])
def test_power_rejects_non_numeric_base(base):
    with pytest.raises(TypeError):
        power(base, 2)


@pytest.mark.parametrize("exponent", [2.0, True, "2", None])
def test_power_rejects_non_integer_exponent(exponent):
    with pytest.raises(TypeError):
        power(2, exponent)
