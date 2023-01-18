from core.serializers import RegistrationSerializer

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from rest_framework.viewsets import GenericViewSet
from rest_framework.request import Request
from rest_framework.response import Response


class RegistrationView(generics.CreateAPIView):
    """Create a new user in the system (This is a public view)"""
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer


class ProfileViewSet(GenericViewSet):
    """
    This view displays the current user profile information
    It only allows get calls to the '/me' endpoint
    """
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]
    # forbid PUT method
    http_method_names = ["get"]

    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user

    def list(self, request: Request, *args, **kwargs) -> Response:
        """
        We override the list method to only retrieve current user's serialized data
        """
        return Response(RegistrationSerializer(
            instance=self.get_object(),
            many=False,
            context={'request': self.request}
        ).data)
