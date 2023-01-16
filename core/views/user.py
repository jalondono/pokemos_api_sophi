from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics


from core.serializers.user import RegistrationSerializer


class RegistrationView(generics.CreateAPIView):
    """Create a new user in the system (This is a public view)"""
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer
