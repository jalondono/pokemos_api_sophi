from .base_model import BaseModel

from django.db import models


class EnumPokemonType(BaseModel):
    """
        Model that represent a Pokemon.
    """
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f"{self.id} - {self.name}"
