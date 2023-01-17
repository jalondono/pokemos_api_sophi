from django_restql.serializers import NestedModelSerializer
from django_restql.fields import NestedField
from rest_framework import serializers
from core.models import Account, Pokemon
from .user import RegistrationSerializer
from .enum_pokemon_type import EnumPokemonTypeSerializer


class PokemonSerializer(NestedModelSerializer, serializers.ModelSerializer):
    user = NestedField(RegistrationSerializer, accept_pk_only=True)
    pokemon_type = NestedField(EnumPokemonTypeSerializer, accept_pk_only=True)
    attack = serializers.FloatField(min_value=0.0)
    defense = serializers.FloatField(min_value=0.0)
    velocity = serializers.FloatField(min_value=0.0)
    resistance = serializers.FloatField(min_value=0.0)

    class Meta:
        model = Pokemon
        exclude = ('created_at', 'updated_at')
