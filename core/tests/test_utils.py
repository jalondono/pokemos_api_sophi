from django.test import SimpleTestCase
from core.utils import check_password_complexity, check_email_format
from rest_framework.serializers import ValidationError


class TestUtils(SimpleTestCase):
    def test_valid_password(self):
        """
        Validate password meet the requirements
        """
        passwords_to_tests = [
            ["bMvnu2?20y.", True],  # valid password
            ["bMvnu2?20", False],  # min len < 10
            ["bmvnu2?20y.", False],  # no Upper case
            ["bMvnu220y200", False]  # no special character
        ]

        for password in passwords_to_tests:
            validated_password = check_password_complexity(password[0])
            self.assertEqual(validated_password, password[1])

    def test_valid_email(self):
        emails_to_tests = [
            ["foobaar@hotmail.com", True],  # valid email
            ["FooBarr@hotmaail.co", True],  # valid email
            ["foobarhotmail.com", False],  # No @ - invalid
            ["foobar@hotmailcom", False]  # not dot (.) - invalid
        ]
        for email in emails_to_tests:
            validated_email = check_email_format(email[0])
            self.assertEqual(validated_email, email[1])
