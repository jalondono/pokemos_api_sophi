from rest_framework import filters, mixins, pagination, status, viewsets
from core.models.pokemon import Pokemon
from core.serializers.pokemon import PokemonSerializer
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from rest_framework import serializers


class PokemonViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    def get_queryset(self):
        """
        Return the own pokemons and public
        """
        user = self.request.user
        return Pokemon.objects.filter(Q(user_id=user.id) | Q(is_public=True))

    def destroy(self, request, *args, **kwargs):
        """
        Avoid delete your own pokemons if the user is not the owner
        """
        pokemon = self.get_object()
        user = request.user
        if pokemon:
            if pokemon.user_id == user.id:
                return super().destroy(request, *args, **kwargs)
            else:
                raise serializers.ValidationError("Error, Is not allowed to delete the public pokemons that not belong "
                                                  "to you")
        return super().destroy(request, *args, **kwargs)
