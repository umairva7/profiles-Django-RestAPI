from rest_framework import serializers

class HelloSerializer(serialzers.Serializer):
    """Serializer a name field for testing our APIView"""
    name=serialzers.CharField(max_length=10)
