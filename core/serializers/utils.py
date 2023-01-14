from rest_framework.serializers import ValidationError

from core.constants import FINAL_PRICE, DATE_FORMAT, ISO_STANDARD, DATE_END, DATE_START, PROPERTY


def validate_dates(validated_data) -> bool:
    """
    Validate that the start_date  is less than end_date. otherwise Ria
    :validated_data: Validated data by the serializer
    :return: True in success
    """
    end_date = validated_data[DATE_END]
    start_date = validated_data[DATE_START]
    if start_date >= end_date:
        raise ValidationError(
            f"start_date: {start_date} can't be greater or equal than end_time: {end_date}"
        )
    return True
