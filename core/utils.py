import re


def check_password_complexity(user_password: str) -> bool:
    """
    Check password complexity and return True if the password is strong enough
    Rules:
        -  at least 8 chars long
        -  lower case (a to z)
        -  upper case (A to Z)
        -  special char (e.g. !@#$%^&*()_+-=.)
    """
    pat = "^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[*.!@#$%^&(){}[\]:;<>,.?/~_+\-=|]).{10,128}$"
    return bool(re.match(pat, user_password))


def check_email_format(email: str) -> bool:
    """
    Check email format and return True if the email is valid
    Rules:
        -  characters (a to z)
        -  @
        -  characters (a to z) - domain
        -  dot (.) and characters (a to z)
    """
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return bool(re.match(pat, email))
