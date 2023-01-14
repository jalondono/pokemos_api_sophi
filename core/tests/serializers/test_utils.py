from django.test import SimpleTestCase
from core.serializers.utils import validate_dates
from rest_framework.serializers import ValidationError


class TestBookingSerializer(SimpleTestCase):
    def test_validate_dates(self):
        validated_data = {
            "date_start": "01-01-2022",
            "date_end": "01-10-2022",
        }

        self.assertTrue(validate_dates(validated_data=validated_data))

    def test_date_start_cannot_be_greater_than_date_end(self):
        validated_data = {
            "date_start": "01-20-2022",
            "date_end": "01-10-2022",
        }
        with self.assertRaises(ValidationError):
            validate_dates(validated_data=validated_data)
