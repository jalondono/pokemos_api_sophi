from django_filters import rest_framework as filters


class NumberInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass


class BaseFilterSet(filters.FilterSet):
    id = filters.NumberFilter(field_name='id')
    id__in = NumberInFilter(field_name='id', lookup_expr='in')
