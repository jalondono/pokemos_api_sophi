from rest_framework import filters, mixins, pagination, status, viewsets

from core.filters.pricing_rule_filterset import PricingRuleFilterSet
from core.models.princing_rule import PricingRule
from core.serializers.pricing_rule import PricingRuleSerializer


class PricingRuleViewSet(viewsets.ModelViewSet):
    queryset = PricingRule.objects.all()
    serializer_class = PricingRuleSerializer
    filterset_class = PricingRuleFilterSet
