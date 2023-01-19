from core.tests.constants import REGISTER_URI, POKEMON_URI
from .base import RESTTestCase
from core.tests.endpoints.payloads import CREATE_POKEMON_1
from core.models.utils import create_random_user, create_random_pokemon_type
from copy import deepcopy
from rest_framework import status


class PokemonTestCase(RESTTestCase):

    def setUp(self) -> None:
        self.user = create_random_user()

    def test_can_not_create_pokemon_no_authenticated(self):
        payload = deepcopy(CREATE_POKEMON_1)
        pokemon_type = create_random_pokemon_type()
        payload["pokemon_type"] = pokemon_type.id
        response = self.client.post(POKEMON_URI, payload, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_pokemon_invalid_payload(self):
        pass

    def test_create_private_pokemon_no_user_passed(self):
        pass

    def test_create_pokemon_successfully(self):
        pass

    def test_get_own_and_public_pokemons(self):
        pass

    def test_update_own_pokemon(self):
        pass



    # def test_create_booking(self):
    #     response_post = self.do_post_test_request(uri=BOOKING_URI, payload=self.booking_payload)
    #     expected_result = BookingSerializer(response_post)
    #     self.assertDictEqual(response_post, expected_result.data)
    #
    # def test_get_booking(self):
    #     response_post = self.do_post_test_request(uri=BOOKING_URI, payload=self.booking_payload)
    #     self.do_get_test_request(uri=BOOKING_URI, obj_id=response_post.get(ID))
    #
    # def test_update_booking(self):
    #     response_post = self.do_post_test_request(uri=BOOKING_URI, payload=self.booking_payload)
    #     patch_response = self.do_patch_test_request(uri=BOOKING_URI, payload=PATCH_BOOKING_NAME_PAYLOAD,
    #                                                 obj_id=response_post.get(ID))
    #     get_response = self.do_get_test_request(uri=BOOKING_URI, obj_id=response_post.get(ID))
    #     self.assertEqual(patch_response.get(DATE_START), get_response.get(DATE_START))
    #
    # def test_delete_booking(self):
    #     response_post = self.do_post_test_request(uri=BOOKING_URI, payload=self.booking_payload)
    #     self.do_delete_test_request(uri=BOOKING_URI, obj_id=response_post.get(ID))
    #     uri = self.detail_url(uri=BOOKING_URI, obj_id=response_post.get(ID))
    #     get_response = self.client.get(uri)
    #     self.assertEqual(get_response.json().get('detail'), NOT_FOUND_ERROR_MESSAGE)
