from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializers a namefield to testing out APIView"""

    name = serializers.CharField(max_length=10)