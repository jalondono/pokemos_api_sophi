from rest_framework import filters, mixins, pagination, status, viewsets
from core.models.pokemon import Pokemon
from core.serializers.pokemon import PokemonSerializer
from rest_framework.permissions import IsAuthenticated


class PokemonViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
