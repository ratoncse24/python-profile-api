from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from . import models

# Create your views here.

class HelloApiview(APIView):
    """Test api view"""

    serializers_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView feature"""

        an_apiview = [
        'Usese HTTP methods as function',
        'It is similar to a tradidational view',
        'Gives you the most control',
        'Is mapped manually to urls'
        ]

        return Response({'message': 'Hello', 'api_view': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updaing an object"""

        return Response({'methods': 'put'})

    def patch(self, request, pk=None):
        """Patch request only update fields provided in request"""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Deletes an object"""

        return Response({'method': 'delete'})


class HelloViewsets(viewsets.ViewSet):
    """Test API viewsets"""

    def list(self, request):

            an_apiview = [
            'Testing viewsets for you!',
            'Provides more functionality with '
            ]

            return Response({'message': 'Hello', 'api_view': an_apiview})



class UserProfileVewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.object.all()
