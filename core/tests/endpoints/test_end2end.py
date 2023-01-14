from core.tests.constants import PROPERTY_URI, NOT_FOUND_ERROR_MESSAGE, BOOKING_URI, ID, PRICING_RULE_URI
from .base import RESTTestCase
from core.tests.endpoints.payloads import *
from core.serializers import BookingSerializer
from core.constants import DATE_START, PROPERTY, FINAL_PRICE


class End2EndTestCase(RESTTestCase):

    def test_e2e_all_cases(self):
        """
        Takes the payloads for the 3 cases, send the needed post request for object creation, then is asserted the
        expected final_price, with the result of booking response
        """

        booking_payload_list = [CREATE_BOOKING_CASE_1_PAYLOAD,
                                CREATE_BOOKING_CASE_2_PAYLOAD,
                                CREATE_BOOKING_CASE_3_PAYLOAD]

        pricing_rule_payload_list = [CREATE_RULE_PRICING_CASE_1_PAYLOAD,
                                     [CREATE_RULE_PRICING_CASE_2_PAYLOAD_1,
                                      CREATE_RULE_PRICING_CASE_2_PAYLOAD_2],
                                     [CREATE_RULE_PRICING_MODIFIER_CASE_3_PAYLOAD,
                                      CREATE_RULE_PRICING_FIXED_PRICE_CASE_3_PAYLOAD]]

        expected_final_price_list = [EXPECTED_FINAL_PRICE_VALUE_CASE_1,
                                     EXPECTED_FINAL_PRICE_VALUE_CASE_2,
                                     EXPECTED_FINAL_PRICE_VALUE_CASE_3]

        for idx in range(len(booking_payload_list)):
            expected_final_price = expected_final_price_list[idx]
            pricing_rule_payload = pricing_rule_payload_list[idx]
            booking_payload = booking_payload_list[idx]
            property_id = self.do_post_test_request(uri=PROPERTY_URI, payload=CREATE_PROPERTY_CASE_1_PAYLOAD).get(ID)

            # sending the POST request for pricing rules creation
            if isinstance(pricing_rule_payload, list):
                # some cases have more than one rules
                for payload in pricing_rule_payload:
                    payload.update({PROPERTY: property_id})
                    self.do_post_test_request(uri=PRICING_RULE_URI, payload=payload)
            else:
                pricing_rule_payload.update({PROPERTY: property_id})
                self.do_post_test_request(uri=PRICING_RULE_URI, payload=pricing_rule_payload)

            # Sending POST request for booking creation
            booking_payload[PROPERTY] = property_id
            booking_response = self.do_post_test_request(uri=BOOKING_URI, payload=booking_payload)

            self.assertEqual(expected_final_price, booking_response.get(FINAL_PRICE))
