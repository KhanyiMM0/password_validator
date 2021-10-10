from password_validator.password_validator import password_is_valid, password_strength
import pytest


def test_password_exits():
    with pytest.raises(ValueError) as error:
        password_is_valid("")
    assert "password should exist" in str(error.value)


@pytest.mark.parametrize("password", [("jhbcpt"), ("mj@ jbpp")])
def test_password_length(password):
    with pytest.raises(ValueError) as error:
        password_is_valid(password)
    assert "password should be longer than 8 characters" in str(error.value)


@pytest.mark.parametrize("password", [("UMUZI CODE"), ("HELLO 2021")])
def test_password_lowercase(password):
    with pytest.raises(ValueError) as error:
        password_is_valid(password)
    assert "password should have at least one lowercase letter" in str(error.value)


@pytest.mark.parametrize("password", [("abcdefghi"), ("012345678s")])
def test_password_uppercase(password):
    with pytest.raises(ValueError) as error:
        password_is_valid(password)
    assert "password should have at least one uppercase letter" in str(error.value)


@pytest.mark.parametrize("password", [("@bmmHJKK]"), ("(&^Alpss)(")])
def test_password_digit(password):
    with pytest.raises(ValueError) as error:
        password_is_valid(password)
    assert "password should at least have one digit" in str(error.value)


@pytest.mark.parametrize("password", [("YQFDi 8677"), ("hsiODG89306")])
def test_password_special_character(password):
    with pytest.raises(ValueError) as error:
        password_is_valid(password)
    assert "password should have at least one special character" in str(error.value)


@pytest.mark.parametrize("password", [("Summer80?"), ("IV3@>nmtmmns")])
def test_password_whitespace_character(password):
    with pytest.raises(ValueError) as error:
        password_is_valid(password)
    assert "password should have at least one whitespace character" in str(error.value)


@pytest.mark.parametrize("password, expected", [("", "invalid"), ("pass", "invalid")])
def test_invalid_password(password, expected):
    assert (
        password_strength(password) == expected
    ), "Password strength should be invalid"


@pytest.mark.parametrize(
    "password, expected", [("weakesttt", "weak"), ("123456789", "weak")]
)
def test_weak_password(password, expected):
    assert password_strength(password) == expected, "Password strength should be weak"


@pytest.mark.parametrize(
    "password, expected", [("Wordss???", "medium"), ("passport7", "medium")]
)
def test_medium_password(password, expected):
    assert password_strength(password) == expected, "Password strength should be medium"


@pytest.mark.parametrize(
    "password, expected", [("k@ng@r 00ABC", "strong"), ("Strong -2001", "strong")]
)
def test_strong_password(password, expected):
    assert password_strength(password) == expected, "Password strength should be strong"
