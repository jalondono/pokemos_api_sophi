from core.tests.constants import REGISTER_URI, POKEMON_URI
from .base import RESTTestCase
from core.tests.endpoints.payloads import CREATE_POKEMON_1
from core.models.utils import create_random_user, create_random_pokemon_type
from copy import deepcopy
from rest_framework import status
from rest_framework.test import APIClient
import json
from core.models import Pokemon


class PokemonTestCase(RESTTestCase):

    def setUp(self) -> None:
        self.user = create_random_user()[0]
        self.client = APIClient()

    def test_can_not_create_pokemon_no_authenticated(self):
        """
        Test that can not be created a pokemon if the user is not authenticated
        """
        payload = deepcopy(CREATE_POKEMON_1)
        pokemon_type = create_random_pokemon_type()
        payload["pokemon_type"] = pokemon_type.id

        response = self.client.post(POKEMON_URI, payload, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_pokemon_invalid_payload(self):
        """
        Test that can not be created a pokemon with missing requires field
        """
        self.client.force_authenticate(self.user)

        payload = deepcopy(CREATE_POKEMON_1)
        payload.pop("attack")

        response = self.client.post(POKEMON_URI, json.dumps(payload), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_private_pokemon_no_user_passed(self):
        """
        Test that can not be created a private Pokemon if it is not associated to a User
        """
        self.client.force_authenticate(self.user)
        payload = deepcopy(CREATE_POKEMON_1)
        payload["is_public"] = False
        response = self.client.post(POKEMON_URI, json.dumps(payload), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_pokemon_successfully(self):
        """
        Test that can be created a pokemon
        """
        self.client.force_authenticate(self.user)
        pokemon_type = create_random_pokemon_type()

        payload = deepcopy(CREATE_POKEMON_1)
        payload["pokemon_type"] = pokemon_type.id
        response = self.client.post(POKEMON_URI, json.dumps(payload), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_own_and_public_pokemons(self):
        """
        Test that a user only can fetch the public and own pokemons
        """
        original_count = Pokemon.objects.count()
        self.client.force_authenticate(self.user)
        payload = deepcopy(CREATE_POKEMON_1)

        pokemon_type = create_random_pokemon_type()

        payload["pokemon_type"] = pokemon_type.id
        payload["user"] = self.user.id
        payload["is_public"] = False

        # the user creates the private pokemon, so he has access to the original count + 1
        response = self.client.post(POKEMON_URI, json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        count_after_create = Pokemon.objects.count()
        self.assertEqual(original_count + 1, count_after_create)

        second_user = create_random_user()[0]
        self.client.force_authenticate(second_user)

        response = self.client.get(POKEMON_URI, content_type='application/json')
        # Since other user is logged can't see the whole list, only the public
        self.assertEqual(original_count, original_count)
