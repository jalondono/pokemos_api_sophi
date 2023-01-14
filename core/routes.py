"""This file contains the wiring up between urls and views
"""
from rest_framework import routers

from core.views import (
    BookingViewSet,
    PropertyViewSet,
    PricingRuleViewSet
)


class ApiRouter:
    """
    Encapsulate the adding of view sets to the api router.
    """

    @classmethod
    def get(cls):
        router = routers.SimpleRouter()
        router.register(r'bookings', BookingViewSet)
        router.register(r'properties', PropertyViewSet)
        router.register(r'pricing_rules', PricingRuleViewSet)

        return router
