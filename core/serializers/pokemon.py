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

    def update(self, instance, validated_data):
        """
        Validate that the item will be updated really belong to the owner
        """
        request = self.context.get('request')
        if instance.user_id == request.user.id:
            return super().update(instance, validated_data)
        raise serializers.ValidationError("The Pokemon can not be updated. Since it does not belong to you")