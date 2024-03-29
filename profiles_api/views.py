from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers, models, permissions


# Create your views here.
class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function',
            'Is similar to atraditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs'
        ]
        
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    
    def post(self, request):
        """Create a hello message with our name and"""
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
        """Handle updating an object"""
        return Response({
            'method': 'PUT'
        })
    
    def patch(self, request, pk=None):
        """Handle partial update of an object"""
        return Response({
            'method': 'PATCH'
        })
    
    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({
            'method': 'DELETE'
        })

class HelloViewSet(viewsets.ViewSet):
    """Test View Sets"""
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Get list of object"""
        return Response({
            'message': 'Hello!'
        })
    
    def create(self, request):
        """Create an object"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            
            return Response({
                'message': message
            })
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profile"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )