from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_api import serializers
from rest_framework import status


class HelloApiView(APIView):
    """test api view

    Arguments:
    """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """get a list of api view features

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
