import re

CONDITIONS = (
    (r".{1,}", "password should exist"),
    (r".{9,}", "password should be longer than 8 characters"),
    (r"[a-z]+", "password should have at least one lowercase letter"),
    (r"[A-Z]+", "password should have at least one uppercase letter"),
    (r"\d+", "password should at least have one digit"),
    (
        r"[\"`[@_!#\$%\^&\*\(\)<'>\?\/\|\}\{~,;:\+\.\]\\=-]+",
        "password should have at least one special character",
    ),
    (r"\s+", "password should have at least one whitespace character"),
)


def password_is_valid(password):
    for pattern, message in CONDITIONS:
        if re.search(pattern, password) == None:
            raise ValueError(message)
    return True


def password_strength(password):

    conditions_met = sum(
        bool(re.search(pattern, password)) for pattern, message in CONDITIONS
    )

    if len(password) == 0 or len(password) < 9:
        return "invalid"
    elif conditions_met >= 6:
        return "strong"
    elif conditions_met >= 4:
        return "medium"
    else:
        return "weak"


def password_is_ok(password):
    if password_strength(password) != "invalid":
        return True
    else:
        return False


print(password_strength("idSk 44fonsks"))
