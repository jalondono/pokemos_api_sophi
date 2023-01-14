from django.db import models
from core.models.property import Property


class Booking(models.Model):
    """
        Model that represent a booking.
        A booking is done when a customer books a property for a given range of days.
        The booking model is also in charge of calculating the final price the customer will pay.
    """
    property = models.ForeignKey(Property, blank=False, null=False, on_delete=models.CASCADE, related_name="bookings")
    """property: The property this booking is for"""
    date_start = models.DateField(blank=False, null=False)
    """date_start: First day of the booking"""
    date_end = models.DateField(blank=False, null=False)
    """date_end: Last date of the booking"""
    final_price = models.FloatField(null=True, blank=True)
    """final_price: Calculated final price"""
