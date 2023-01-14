from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


from core.serializers.user import RegistrationSerializer


class RegistrationView(GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        """
        Create a new user
        """
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Successfully registered a new user"
            data['email'] = account.email
            data['username'] = account.username
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
