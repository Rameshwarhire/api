
from rest_framework import serializers
from . models import User
from rest_framework.validators import ValidationError

#for token generation
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    

    email = serializers.CharField(max_length = 100)
    username = serializers.CharField(max_length = 50)
    password = serializers.CharField(min_length = 8, write_only = True)

    class Meta:
        model = User
        fields = ["email", "username", "password"]

    def validate(self, attrs):

        email_already_exists = User.objects.filter(email = attrs['email']).exists()

        if email_already_exists:
            raise ValidationError(f"Enterd email id {attrs['email']} already exists")
        
        return super().validate(attrs)
    #this method for saving password in incripted formet
    def create(self, validated_data):

        password=validated_data.pop("password")
        user=super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user

#creat token auth

        
 