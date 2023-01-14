from core.tests.constants import PROPERTY_URI, NOT_FOUND_ERROR_MESSAGE
from .base import RESTTestCase
from core.tests.endpoints.payloads import CREATE_PROPERTY_CASE_1_PAYLOAD, PATCH_PROPERTY_NAME_PAYLOAD
from core.serializers import PropertySerializer


class PropertyTestCase(RESTTestCase):
    # base_name = "property-list"

    def setUp(self) -> None:
        self.property = self.do_post_test_request(uri=PROPERTY_URI, payload=CREATE_PROPERTY_CASE_1_PAYLOAD)

    def test_create_property(self):
        expected_result = PropertySerializer(self.property)
        self.assertDictEqual(self.property, expected_result.data)

    def test_get_property(self):
        self.do_get_test_request(uri=PROPERTY_URI, obj_id=self.property.get('id'))

    def test_update_property(self):
        patch_response = self.do_patch_test_request(uri=PROPERTY_URI, payload=PATCH_PROPERTY_NAME_PAYLOAD,
                                                    obj_id=self.property.get('id'))
        get_response = self.do_get_test_request(uri=PROPERTY_URI, obj_id=self.property.get('id'))
        self.assertEqual(patch_response.get('name'), get_response.get('name'))

    def test_delete_property(self):
        self.do_delete_test_request(uri=PROPERTY_URI, obj_id=self.property.get('id'))
        uri = self.detail_url(uri=PROPERTY_URI, obj_id=self.property.get('id'))
        response = self.client.get(uri)
        self.assertEqual(response.json().get('detail'), NOT_FOUND_ERROR_MESSAGE)
