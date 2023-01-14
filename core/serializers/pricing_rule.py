from django_restql.serializers import NestedModelSerializer
from django_restql.fields import NestedField
from rest_framework import serializers

from core.serializers.property import PropertySerializer

from core.models.princing_rule import PricingRule

from core.constants import DATE_FORMAT, ISO_STANDARD


class PricingRuleSerializer(NestedModelSerializer):
    property = NestedField(PropertySerializer, accept_pk_only=True)
    specific_day = serializers.DateField(required=False, format=DATE_FORMAT, input_formats=[DATE_FORMAT, ISO_STANDARD])

    class Meta:
        model = PricingRule
        fields = '__all__'
