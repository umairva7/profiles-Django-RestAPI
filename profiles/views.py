from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloAPIView(APIView):
    """Test API View"""
    def get(self,request,format=None):
        """Return list of APIView features"""

        an_apiview=[
        'Uses HTTP method as funcation (get,post,patch,put,delete)',
        'Is similiar to a traditional Django View',
        'Gives you the most control over the application logic',
        'Is mapped manually to URLs',

        ]
        return Response({'message':'Hello','an_apiview':an_apiview})
