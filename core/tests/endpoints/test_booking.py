from core.tests.constants import PROPERTY_URI, NOT_FOUND_ERROR_MESSAGE, BOOKING_URI, ID
from .base import RESTTestCase
from core.tests.endpoints.payloads import CREATE_PROPERTY_CASE_1_PAYLOAD, CREATE_BOOKING_CASE_1_PAYLOAD, \
    PATCH_BOOKING_NAME_PAYLOAD
from core.serializers import BookingSerializer
from core.constants import DATE_START, PROPERTY


class BookingTestCase(RESTTestCase):

    def setUp(self) -> None:
        self.property = self.do_post_test_request(uri=PROPERTY_URI, payload=CREATE_PROPERTY_CASE_1_PAYLOAD)
        self.booking_payload = CREATE_BOOKING_CASE_1_PAYLOAD
        self.booking_payload[PROPERTY] = self.property.get(ID)

    def test_create_booking(self):
        response_post = self.do_post_test_request(uri=BOOKING_URI, payload=self.booking_payload)
        expected_result = BookingSerializer(response_post)
        self.assertDictEqual(response_post, expected_result.data)

    def test_get_booking(self):
        response_post = self.do_post_test_request(uri=BOOKING_URI, payload=self.booking_payload)
        self.do_get_test_request(uri=BOOKING_URI, obj_id=response_post.get(ID))

    def test_update_booking(self):
        response_post = self.do_post_test_request(uri=BOOKING_URI, payload=self.booking_payload)
        patch_response = self.do_patch_test_request(uri=BOOKING_URI, payload=PATCH_BOOKING_NAME_PAYLOAD,
                                                    obj_id=response_post.get(ID))
        get_response = self.do_get_test_request(uri=BOOKING_URI, obj_id=response_post.get(ID))
        self.assertEqual(patch_response.get(DATE_START), get_response.get(DATE_START))

    def test_delete_booking(self):
        response_post = self.do_post_test_request(uri=BOOKING_URI, payload=self.booking_payload)
        self.do_delete_test_request(uri=BOOKING_URI, obj_id=response_post.get(ID))
        uri = self.detail_url(uri=BOOKING_URI, obj_id=response_post.get(ID))
        get_response = self.client.get(uri)
        self.assertEqual(get_response.json().get('detail'), NOT_FOUND_ERROR_MESSAGE)
