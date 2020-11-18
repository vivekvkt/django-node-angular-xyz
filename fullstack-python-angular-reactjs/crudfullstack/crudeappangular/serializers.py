from rest_framework import serializers
from crudeappangular.models import Userdata

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userdata
        fields = '__all__' #['first_name']

class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)