
from django.core.management.base import BaseCommand

from core.models.utils import create_batch_of_pokemons


class Command(BaseCommand):

    def handle(self, *args, **options):
        counter = create_batch_of_pokemons()
        self.stdout.write(f'{counter} pokemons added')
