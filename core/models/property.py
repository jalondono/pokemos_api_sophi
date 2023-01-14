from django.db import models


class Property(models.Model):
    """
        Model that represents a property.
        A property could be a house, a flat, a hotel room, etc.
    """
    name = models.CharField(max_length=255, blank=True, null=True)
    """name: Name of the property"""
    base_price = models.FloatField(null=True, blank=True)
    """base_price: base price of the property per day"""
