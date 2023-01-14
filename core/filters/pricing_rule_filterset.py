from django_filters import DateFilter

from core.filters import BaseFilterSet
from core.filters.constants import ID_LOOKUP_EXPR, QTY_LOOKUP_EXPR, EXACT_EXPR
from core.models.princing_rule import PricingRule


class PricingRuleFilterSet(BaseFilterSet):
    specific_day = DateFilter('specific_day', EXACT_EXPR)

    class Meta:
        model = PricingRule
        fields = {
            'property': ID_LOOKUP_EXPR,
            'price_modifier': QTY_LOOKUP_EXPR,
            'min_stay_length': QTY_LOOKUP_EXPR,
            'fixed_price': QTY_LOOKUP_EXPR,
        }
