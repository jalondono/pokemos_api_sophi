from faker import Faker
import random

from core.models import Pokemon, EnumPokemonType, Account

faker = Faker('en-US')


def create_random_pokemon_type():
    pokemon_type, is_created = EnumPokemonType.objects.get_or_create(name=faker.name)
    return pokemon_type


def create_random_pokemon(user: Account = None, is_public: bool = True,
                          pokemon_type: EnumPokemonType = None) -> (bool, Pokemon):
    """
    Create a single random pokemon
    """
    if not pokemon_type:
        random_pokemon_type = create_random_pokemon_type()
    else:
        random_pokemon_type = pokemon_type
    name = faker.name()
    pokemon_params = {
        "user": user or None,
        "pokemon_type": random_pokemon_type,
        "attack": random.randint(0, 100),
        "defense": random.randint(0, 100),
        "velocity": random.randint(0, 100),
        "resistance": random.randint(0, 100),
        "is_public": is_public or True
    }
    pokemon, is_created = Pokemon.objects.get_or_create(name=name, defaults=pokemon_params)

    return is_created, pokemon


def create_batch_of_pokemons() -> int:
    """
    Create a batch of pokemons
    """
    count = 0
    pokemon_types = EnumPokemonType.objects.all()
    for pokemon_type in pokemon_types:
        is_created, pokemon = create_random_pokemon(user=None, is_public=True, pokemon_type=pokemon_type)
        if is_created:
            count += 1
    return count


def create_random_user() -> bool:
    """
    Create a random user
    """
    email_name = faker.name().replace(" ", "")
    email = f"{email_name}@hotmail.com"
    args = {"password": "bMvnu2?!20y."}
    return Account.objects.get_or_create(email=email, defaults=args)[1]

