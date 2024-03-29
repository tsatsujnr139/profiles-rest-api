from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profiles_api import serializers, models, permissions


class HelloApiView(APIView):
    """test api view

    Arguments:
    """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """get a list of api features

        Arguments:
            request {[type]} --

        Keyword Arguments:
            format {[type]} -- (default: {None})
        """
        apiview = [
            'Uses http methods as functions (get, post, patch, put, delete)'
        ]

        return Response(
            {
                'message': 'Hello!',
                'apiview': apiview
            }
        )

    def post(self, request):
        """return hello with name passed in request

        Arguments:
            request {[type]}
        """
        seriliazer = self.serializer_class(data=request.data)

        if seriliazer.is_valid():
            name = seriliazer.validated_data.get('name')
            message = f'Hello {name }'
            return Response({'message': message})
        else:
            return Response(
                seriliazer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """updates an object

        Arguments:
            request  -- http request

        Keyword Arguments:
            pk --  (default: {None})
        """
        return Response(
            {
                'method': 'PUT'
            }
        )

    def patch(self, request, pk=None):
        """handle partial update

        Arguments:
            request  --

        Keyword Arguments:
            pk  --  (default: {None})
        """
        return Response(
            {
                'method': 'PATCH'
            }
        )

    def delete(self, request, pk=None):
        """handle partial update

        Arguments:
            request  --

        Keyword Arguments:
            pk  --  (default: {None})
        """
        return Response(
            {
                'method': 'DELETE'
            }
        )


class HelloViewSet(viewsets.ViewSet):
    """test api viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ returns a hello message """

        a_viewset = [
            'uses actions list,create,retrieve,update,partial_update'
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """ create a new hello message """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """ retrieve object by id"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """ update object by id"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """ partial update of object by id """
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """ delete object by id """
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """ handles creating and updating users"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """handles user auth tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnFeedItem,IsAuthenticated)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()

    def perform_create(self, serializer):
        """ setsu the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
