from rest_framework import filters, mixins, pagination, status, viewsets

from core.filters.booking_filterset import BookingFilterSet
from core.models.booking import Booking
from core.serializers.booking import BookingSerializer
from rest_framework.permissions import IsAuthenticated


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filterset_class = BookingFilterSet
