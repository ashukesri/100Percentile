from rest_framework.serializers import ModelSerializer

from .models import UserAnswer

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields= [
            'user',
            'role',
            'active',
            'is_subscribed',
        ]

class UserAnswerSerializer(ModelSerializer):
    class Meta:
        model = UserAnswer
        fields= [
            'question',
            'answer',
            'answer_sequence',
            'user',
            'active',
        ]


