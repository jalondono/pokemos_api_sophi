from rest_framework import filters, mixins, pagination, status, viewsets

from core.filters.property_filterset import PropertyFilterSet
from core.models.property import Property
from core.serializers.property import PropertySerializer


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filterset_class = PropertyFilterSet
