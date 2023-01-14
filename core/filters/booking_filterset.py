from django_filters import DateFromToRangeFilter

from core.filters import BaseFilterSet
from core.filters.constants import ID_LOOKUP_EXPR
from core.models.booking import Booking


class BookingFilterSet(BaseFilterSet):
    date_start = DateFromToRangeFilter(field_name='date_start')
    date_end = DateFromToRangeFilter(field_name='date_end')

    class Meta:
        model = Booking
        fields = {'property': ID_LOOKUP_EXPR}
