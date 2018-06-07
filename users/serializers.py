from rest_framework.serializers import ModelSerializer

from .models import UserAnswer,Profile

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
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


