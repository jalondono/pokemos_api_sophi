from core.tests.constants import PROPERTY_URI, NOT_FOUND_ERROR_MESSAGE, PRICING_RULE_URI, ID
from .base import RESTTestCase
from core.tests.endpoints.payloads import CREATE_PROPERTY_CASE_1_PAYLOAD, CREATE_RULE_PRICING_CASE_1_PAYLOAD, \
    PATCH_BOOKING_NAME_PAYLOAD, PATCH_PRICING_RULE_PRICE_MODIFIER_PAYLOAD
from core.serializers import PricingRuleSerializer
from core.constants import PRICE_MODIFIER, PROPERTY


class PricingRuleTestCase(RESTTestCase):

    def setUp(self) -> None:
        self.property = self.do_post_test_request(uri=PROPERTY_URI, payload=CREATE_PROPERTY_CASE_1_PAYLOAD)
        self.pricing_rule_payload = CREATE_RULE_PRICING_CASE_1_PAYLOAD
        self.pricing_rule_payload[PROPERTY] = self.property.get(ID)

    def test_create_pricing_rule(self):
        response_post = self.do_post_test_request(uri=PRICING_RULE_URI, payload=self.pricing_rule_payload)
        expected_result = PricingRuleSerializer(response_post)
        self.assertDictEqual(response_post, expected_result.data)

    def test_get_pricing_rule(self):
        response_post = self.do_post_test_request(uri=PRICING_RULE_URI, payload=self.pricing_rule_payload)
        self.do_get_test_request(uri=PRICING_RULE_URI, obj_id=response_post.get(ID))

    def test_update_pricing_rule(self):
        response_post = self.do_post_test_request(uri=PRICING_RULE_URI, payload=self.pricing_rule_payload)
        patch_response = self.do_patch_test_request(uri=PRICING_RULE_URI,
                                                    payload=PATCH_PRICING_RULE_PRICE_MODIFIER_PAYLOAD,
                                                    obj_id=response_post.get(ID))
        get_response = self.do_get_test_request(uri=PRICING_RULE_URI, obj_id=response_post.get(ID))
        self.assertEqual(patch_response.get(PRICE_MODIFIER), get_response.get(PRICE_MODIFIER))

    def test_delete_pricing_rule(self):
        response_post = self.do_post_test_request(uri=PRICING_RULE_URI, payload=self.pricing_rule_payload)
        self.do_delete_test_request(uri=PRICING_RULE_URI, obj_id=response_post.get(ID))
        uri = self.detail_url(uri=PRICING_RULE_URI, obj_id=response_post.get(ID))
        get_response = self.client.get(uri)
        self.assertEqual(get_response.json().get('detail'), NOT_FOUND_ERROR_MESSAGE)
