from rest_framework import serializers
from django_restql.serializers import NestedModelSerializer

from core.models.property import Property


class PropertySerializer(NestedModelSerializer):
    base_price = serializers.FloatField(min_value=0.0)

    class Meta:
        model = Property
        fields = '__all__'
