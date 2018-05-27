from rest_framework import serializers
from . import models

class UserProfileSerializer(serializers.ModelSerializer):
    
    password= serializers.CharField(write_only=True)
    
    class Meta:
        model= models.UserProfile
        fields= ('id','email','password','role')
        extra_kwargs={'password':{'write_only':True}}
    def create(self, validated_data):
        user= models.UserProfile(
            email= validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    