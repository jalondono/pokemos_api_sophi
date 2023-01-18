"""This file contains the wiring up between urls and views
"""
from rest_framework import routers

from core.views import (
    PokemonViewSet,
    EnumPokemonTypeViewSet, ProfileViewSet
)


class ApiRouter:
    """
    Encapsulate the adding of view sets to the api router.
    """

    @classmethod
    def get(cls):
        router = routers.SimpleRouter()
        router.register(r'me', ProfileViewSet, basename='profile')
        router.register(r'pokemon_type', EnumPokemonTypeViewSet)
        router.register(r'pokemon', PokemonViewSet)

        return router
