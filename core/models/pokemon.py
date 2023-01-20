from .user import Account
from .base_model import BaseModel

from django.db import models


class Pokemon(BaseModel):
    """
        Model that represent a Pokemon.
    """
    user: Account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    name: str = models.CharField(max_length=128, unique=True)
    pokemon_type = models.ForeignKey(
        'EnumPokemonType',
        on_delete=models.PROTECT,
        db_column='pokemon_type',
        to_field='name',
    )
    velocity: float = models.FloatField(default=0.0)
    attack: float = models.FloatField(default=0.0)
    defense: float = models.FloatField(default=0.0)
    resistance: float = models.FloatField(default=0.0)
    is_public: bool = models.BooleanField(default=False)

    class Meta:
        ordering = ["id"]
