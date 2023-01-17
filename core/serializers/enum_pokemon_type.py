from django_restql.mixins import DynamicFieldsMixin
from rest_framework import serializers

from core.models import EnumPokemonType


class EnumPokemonTypeSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = EnumPokemonType
        exclude = ('created_at', 'updated_at')
