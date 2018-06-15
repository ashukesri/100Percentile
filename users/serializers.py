from rest_framework.serializers import (ModelSerializer,                       
                                        ValidationError,
                                        CharField,
                                        EmailField,
                                       PrimaryKeyRelatedField,)
from django.contrib.auth.models import User
from .models import UserAnswer,Profile#,Follow
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.authtoken.models import Token
User = get_user_model()

        
class UserCreateSerialzer(ModelSerializer):
    class Meta:
        model = User
        fields=[
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
        ]
        extra_kwargs = {"password":{"write_only":True}}
        
    def create(self, validated_data):
        username=validated_data['username']
        email=validated_data['email']
        password=validated_data['password']
        first_name=validated_data['first_name']
        last_name=validated_data['last_name']
        user_obj= User(
                username=username,
                email=email
            )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data
    
    def validate(self,data):
        username=data['username']
        email=data['email']
        
        user_un= User.objects.filter(username=username)
        user_em= User.objects.filter(email=email)
        if user_un.exists():
            raise ValidationError("Username already exits")
        if user_em.exists():
            raise ValidationError("Email already exits")
        return data
    
        

    
class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]
    
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields= [
            'username',
            'id',
            'profile',
        ]
        
class ProfileSerializer(ModelSerializer):
    user = UserSerializer(many= False,read_only=True)
    class Meta:
        model = Profile
        fields=[
            'role' ,
            'active',
            'is_subscribed',
            'user',
        ]

class UserAnswerSerializer(ModelSerializer):
    class Meta:
        model = UserAnswer
        fields= [
            'question',
            'answer',
            'subjective_answer',
            'user',
            'active',
        ]

        read_only_fields = ('user',)
        

#class FollowSerializer(ModelSerializer):
#    class Meta:
#        model=Follow
#        fields=[
#            'follower',
#            'following',
#        ]

#class UserLoginSerialzer(ModelSerializer):
#    token = CharField(allow_blank=True,read_only=True)
#    username= CharField(required=False, allow_blank=True)
#    email= EmailField(label = 'Email Address',required=False, allow_blank=True )
#    class Meta:
#        model = User
#        fields=[
#            'username',
#            'password',
#            'email',
#            'token',
#        ]
#        extra_kwargs = {"password":{"write_only":True}}
#        
#    def validate(self,data):
#        user_obj=None
#        username=data.get("username",None)
#        email=data.get("email",None)
#        password= data["password"]
#        if not email and not username:
#            raise ValidationError("A username or email is required")
#            
#        user = User.objects.filter(
#                Q(email=email) |
#                Q(username=username)
#            ).distinct()
#        user=user.exclude(email__isnull=True).exclude(email__iexact='')
#        if user.exists() and user.count() ==1:
#            user_obj = user.first()
#        else: 
#            raise ValidationError("This username/email is not valid")
#        
#        if user_obj:
#            if not user_obj.check_password(password):
#                raise ValidationError("Incorrect password")
#        data["token"]= token = Token.objects.create(user=user_obj)
#        print(data["token"])
#        return data
    