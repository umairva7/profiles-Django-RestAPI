from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets
from profiles import serializers

class HelloAPIView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over the application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
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

    def put(self, request, pk=None):
        """Handle updating an object (full update)"""
        return Response({'method': 'PUT', 'message': 'This would update an object completely.'})

    def patch(self, request, pk=None):
        """Handle partial update of an object"""
        return Response({'method': 'PATCH', 'message': 'This would update part of the object.'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE', 'message': 'This would delete an object.'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            "Uses actions like list, create, retrieve, update, partial_update",
            "Automatically maps to URLs using routers",
            "Provides more functionality with less code",
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message"""
        return Response({'method': 'POST', 'message': 'Hello from create method!'})

    def retrieve(self, request, pk=None):
        """Handle getting a single object by its ID"""
        return Response({'method': 'GET', 'message': f'Retrieve object {pk}'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT', 'message': f'Update object {pk}'})

    def partial_update(self, request, pk=None):
        """Handle partial update of an object"""
        return Response({'method': 'PATCH', 'message': f'Partial update object {pk}'})

    def destroy(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE', 'message': f'Delete object {pk}'})
