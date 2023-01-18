import random

from django.core.management.base import BaseCommand
from faker import Faker

from core.models import Pokemon, EnumPokemonType

faker = Faker('en-US')


class Command(BaseCommand):

    def handle(self, *args, **options):
        pokemon_params = {}
        pokemon_types = EnumPokemonType.objects.all()
        counter = 0
        for idx, pokemon_type in enumerate(pokemon_types):
            name = faker.name()
            pokemon_params = {
                "user": None,
                "pokemon_type": pokemon_type,
                "attack": random.randint(0, 100),
                "defense": random.randint(0, 100),
                "velocity": random.randint(0, 100),
                "resistance": random.randint(0, 100),
                "is_public": True
            }
            if Pokemon.objects.get_or_create(name=name, defaults=pokemon_params)[1]:
                counter += 1
        self.stdout.write(f'{counter} pokemons added')
