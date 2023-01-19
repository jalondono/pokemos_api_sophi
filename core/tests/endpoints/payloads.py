
CREATE_POKEMON_1 = {
        "user": None,
        "pokemon_type": None,
        "attack": 100,
        "defense": 100,
        "velocity": 100,
        "resistance": 100,
        "is_public": True
}

# CASE 1 PAYLOADS

CREATE_PROPERTY_CASE_1_PAYLOAD = {
    "name": "Property case 1",
    "base_price": 10
}
CREATE_RULE_PRICING_CASE_1_PAYLOAD = {
    "property": None,
    "price_modifier": -10,
    "min_stay_length": 7
}
CREATE_BOOKING_CASE_1_PAYLOAD = {
    "property": None,
    "date_start": "01-01-2022",
    "date_end": "01-10-2022",
    "final_price": 80
}

EXPECTED_FINAL_PRICE_VALUE_CASE_1 = 90

# CASE 2 PAYLOADS

CREATE_PROPERTY_CASE_2_PAYLOAD = {
    "name": "Property case 2",
    "base_price": 10
}
CREATE_RULE_PRICING_CASE_2_PAYLOAD_1 = {
    "property": None,
    "price_modifier": -10,
    "min_stay_length": 7
}

CREATE_RULE_PRICING_CASE_2_PAYLOAD_2 = {
    "property": None,
    "price_modifier": -10,
    "min_stay_length": 7
}

CREATE_BOOKING_CASE_2_PAYLOAD = {
    "property": None,
    "date_start": "01-01-2022",
    "date_end": "01-10-2022",
    "final_price": 80
}

EXPECTED_FINAL_PRICE_VALUE_CASE_2 = 90

# CASE 3 PAYLOADS

CREATE_PROPERTY_CASE_3_PAYLOAD = {
    "name": "Property case 3",
    "base_price": 10
}
CREATE_RULE_PRICING_MODIFIER_CASE_3_PAYLOAD = {
    "property": None,
    "price_modifier": -10,
    "min_stay_length": 7
}

CREATE_RULE_PRICING_FIXED_PRICE_CASE_3_PAYLOAD = {
    "property": None,
    "specific_day": "01-04-2022",
    "fixed_price": 20
}
CREATE_BOOKING_CASE_3_PAYLOAD = {
    "property": None,
    "date_start": "01-01-2022",
    "date_end": "01-10-2022",
    "final_price": 80
}
EXPECTED_FINAL_PRICE_VALUE_CASE_3 = 101

# Patch Payloads

PATCH_PROPERTY_NAME_PAYLOAD = {
    "name": "patched name test",
}

PATCH_BOOKING_NAME_PAYLOAD = {
    "date_start": "01-20-2022",
    "date_end": "01-30-2022",
}

PATCH_PRICING_RULE_PRICE_MODIFIER_PAYLOAD = {
    "price_modifier": -30
}
