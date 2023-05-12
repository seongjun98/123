from rest_framework import serializers
from .models import User

class userserializers(serializers.ModelSerializer):
    class User:
        model  = User
        fields = '__all__'