from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import models
from . import permissions

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
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class LoginViewSet(viewsets.ViewSet):
    """Check auth token and return token"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken for create token"""

        return ObtainAuthToken().post(request)

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """"Handling creating , reading and updating user profile"""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated)


    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)
