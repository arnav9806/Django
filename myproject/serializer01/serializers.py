from rest_framework import serializers
from .models import User
class UserSerializer(serializers.Serializer):
    name= serializers.CharField(max_length=100)
    adress= serializers.CharField(max_length=200)
    age= serializers.IntegerField()    