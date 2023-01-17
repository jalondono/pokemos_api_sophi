from rest_framework import filters, mixins, pagination, status, viewsets
from core.models.pokemon import Pokemon
from core.serializers.pokemon import PokemonSerializer
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


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
