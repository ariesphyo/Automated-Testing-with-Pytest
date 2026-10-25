import pytest

from src.data_validator import (
    InvalidAgeError,
    InvalidEmailError,
    InvalidUsernameError,
    ValidationError,
    WeakPasswordError,
    validate_age,
    validate_email,
    validate_password,
    validate_registration,
    validate_username,
)


@pytest.mark.parametrize(
    "email",
    [
        "user@example.com",
        "first.last@example.co",
        "user@mail.example.com",
        "user+tag@example.com",
        "user_name-1@example-domain.org",
    ],
)
def test_validate_email_accepts_valid_addresses(email):
    assert validate_email(email) is True


@pytest.mark.parametrize(
    ("email", "message"),
    [
        ("", "Email cannot be empty."),
        ("userexample.com", "is not a valid email address"),
        ("user@", "is not a valid email address"),
        ("user@localhost", "is not a valid email address"),
        ("user@example.c", "is not a valid email address"),
        ("first..last@example.com", "is not a valid email address"),
        ("user @example.com", "is not a valid email address"),
    ],
)
def test_validate_email_rejects_invalid_addresses(email, message):
    with pytest.raises(InvalidEmailError, match=message):
        validate_email(email)


@pytest.mark.parametrize("email", [None, 123, True, ["user@example.com"]])
def test_validate_email_rejects_non_string_input(email):
    with pytest.raises(TypeError, match="Email must be a string"):
        validate_email(email)


@pytest.mark.parametrize(
    "password",
    [
        "Strong1!Pass",
        "Aa1!bcde",
        "Aa1!" + "b" * 124,
    ],
)
def test_validate_password_accepts_passwords_meeting_all_rules(password):
    assert validate_password(password) is True


@pytest.mark.parametrize(
    ("password", "message"),
    [
        ("Aa1!abc", "at least 8 characters"),
        ("Aa1!" + "b" * 125, "maximum allowable length of 128"),
        ("Strong 1!Pass", "must not contain whitespace"),
        ("strong1!pass", "at least one uppercase letter"),
        ("STRONG1!PASS", "at least one lowercase letter"),
        ("Strong!!Pass", "at least one digit"),
        ("Strong1Pass", "at least one special character"),
    ],
)
def test_validate_password_rejects_weak_passwords_with_reason(password, message):
    with pytest.raises(WeakPasswordError, match=message):
        validate_password(password)


@pytest.mark.parametrize("password", [None, 123, True, ["Strong1!Pass"]])
def test_validate_password_rejects_non_string_input(password):
    with pytest.raises(TypeError, match="Password must be a string"):
        validate_password(password)


@pytest.mark.parametrize("username", ["abc", "A_1", "User_123", "a" * 20])
def test_validate_username_accepts_valid_usernames(username):
    assert validate_username(username) is True


@pytest.mark.parametrize(
    ("username", "message"),
    [
        ("ab", "between 3 and 20"),
        ("a" * 21, "between 3 and 20"),
        ("1user", "start with a letter"),
        ("_user", "start with a letter"),
        ("user-name", "contain only alphanumeric characters and underscores"),
        ("user name", "contain only alphanumeric characters and underscores"),
        ("user.name", "contain only alphanumeric characters and underscores"),
    ],
)
def test_validate_username_rejects_invalid_usernames(username, message):
    with pytest.raises(InvalidUsernameError, match=message):
        validate_username(username)


@pytest.mark.parametrize("username", [None, 123, True, ["user"]])
def test_validate_username_rejects_non_string_input(username):
    with pytest.raises(TypeError, match="Username must be a string"):
        validate_username(username)


@pytest.mark.parametrize("age", [13, 25, 120])
def test_validate_age_accepts_ages_inclusive_of_bounds(age):
    assert validate_age(age) is True


@pytest.mark.parametrize(
    ("age", "message"),
    [(12, "at least 13"), (121, "must not exceed 120")],
)
def test_validate_age_rejects_ages_outside_bounds(age, message):
    with pytest.raises(InvalidAgeError, match=message):
        validate_age(age)


@pytest.mark.parametrize("age", [13.0, "13", None, True, False])
def test_validate_age_rejects_non_integer_and_boolean_inputs(age):
    with pytest.raises(TypeError, match="Age must be an integer"):
        validate_age(age)


def test_validate_registration_accepts_valid_payload():
    data = {
        "username": "valid_user",
        "email": "user@example.com",
        "password": "Strong1!Pass",
        "age": 25,
    }

    assert validate_registration(data) is True


@pytest.mark.parametrize("field", ["username", "email", "password", "age"])
def test_validate_registration_rejects_each_missing_required_field(field):
    data = {
        "username": "valid_user",
        "email": "user@example.com",
        "password": "Strong1!Pass",
        "age": 25,
    }
    del data[field]

    with pytest.raises(ValidationError, match=f"Missing required registration field: '{field}'"):
        validate_registration(data)


@pytest.mark.parametrize(
    ("field", "value", "exception", "message"),
    [
        ("username", "1invalid", InvalidUsernameError, "start with a letter"),
        ("email", "user@localhost", InvalidEmailError, "is not a valid email address"),
        ("password", "Strong1Pass", WeakPasswordError, "at least one special character"),
        ("age", 12, InvalidAgeError, "at least 13"),
    ],
)
def test_validate_registration_propagates_invalid_field_errors(
    field, value, exception, message
):
    data = {
        "username": "valid_user",
        "email": "user@example.com",
        "password": "Strong1!Pass",
        "age": 25,
    }
    data[field] = value

    with pytest.raises(exception, match=message):
        validate_registration(data)


@pytest.mark.parametrize("data", [None, [], "registration", 1])
def test_validate_registration_rejects_non_dictionary_payload(data):
    with pytest.raises(TypeError, match="Registration data must be a dictionary"):
        validate_registration(data)
