from django_restql.serializers import NestedModelSerializer
from django_restql.fields import NestedField
from rest_framework import serializers

from core.serializers.property import PropertySerializer
from core.models.booking import Booking

from core.serializers.utils import validate_dates

from core.constants import FINAL_PRICE, DATE_FORMAT, ISO_STANDARD, DATE_END, DATE_START, PROPERTY


class BookingSerializer(NestedModelSerializer):
    property = NestedField(PropertySerializer, accept_pk_only=True)
    date_start = serializers.DateField(format=DATE_FORMAT, input_formats=[DATE_FORMAT, ISO_STANDARD])
    date_end = serializers.DateField(format=DATE_FORMAT, input_formats=[DATE_FORMAT, ISO_STANDARD])

    def compute_final_price(self, validated_data) -> float:
        """
        compute the final price for a booking
        :validated_data: Validated data by the serializer
        :return: computed final price value
        """
        last_price_modifier = 0
        fixed_day_prices_dict = {}

        end_date = validated_data[DATE_END]
        start_date = validated_data[DATE_START]
        total_stay = (end_date - start_date).days + 1

        property_obj = validated_data[PROPERTY]
        rules = property_obj.pricing_rules.all()
        for rule in rules:
            if rule.min_stay_length and rule.price_modifier:
                # Get the max price_modifier whose min_stay_length apply
                if total_stay >= rule.min_stay_length and rule.price_modifier <= last_price_modifier:
                    last_price_modifier = rule.price_modifier
            if rule.specific_day and rule.fixed_price:
                # Create a dictionary with each specific_day as key and as fixed_price, so, we can update the
                # fixed_price on a duplicated specific_day, Getting the max fixed_price
                if start_date <= rule.specific_day <= end_date and \
                        rule.fixed_price >= fixed_day_prices_dict.get(str(rule.specific_day), 0.0):
                    fixed_day_prices_dict[str(rule.specific_day)] = rule.fixed_price

        # Compute the sum of all values for fixed_price days
        fixed_day_price_list = [price for key, price in fixed_day_prices_dict.items()]
        fixed_day_price_value = sum(fixed_day_price_list)

        # compute the price for normal days, It subtract the number of fixed_price days to the total_stay days,
        # then multiply by the base_price
        price_per_normal_days = ((total_stay - len(fixed_day_price_list)) * property_obj.base_price)

        # Compute the percentage of increment or decrement
        percentage_increment_decrement = ((100 + last_price_modifier) / 100)

        # Compute the final price
        final_price = (price_per_normal_days * percentage_increment_decrement) + fixed_day_price_value
        return final_price

    def create(self, validated_data):
        """
        On Booking creation some validations take place:
        - User can't provide a final price value, It only should be computed base on the property rules.
        - If a final_price value is passed, It is dropped from the payload
        :param validated_data: Dict, validated payload data
        :return: Created booking instance
        """
        validate_dates(validated_data)
        validated_data.pop(FINAL_PRICE, None)
        final_price = self.compute_final_price(validated_data)
        validated_data[FINAL_PRICE] = final_price
        booking = super(BookingSerializer, self).create(validated_data)
        return booking

    def update(self, instance, validated_data):
        """
        On Booking update some validations take place:
        - User can't provide a final price value, It only should be computed base on the property rules.
        - If a final_price value is passed, It is dropped from the payload
        :param instance: Booking instance
        :param validated_data: Dict, validated payload data
        :return: Updated booking instance
        """
        validate_dates(validated_data)
        validated_data.pop(FINAL_PRICE, None)
        booking = super(BookingSerializer, self).update(instance, validated_data)
        return booking

    class Meta:
        model = Booking
        fields = '__all__'
