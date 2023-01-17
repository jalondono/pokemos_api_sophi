from rest_framework import filters, mixins, pagination, status, viewsets
from core.models import EnumPokemonType
from core.serializers import EnumPokemonTypeSerializer
from rest_framework.permissions import IsAuthenticated


class EnumPokemonTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = EnumPokemonType.objects.all()
    serializer_class = EnumPokemonTypeSerializer
    http_method_names = ["get"]
