from rest_framework.serializers import ModelSerializer

from .models import Topics,SubTopics,Questions,QuestionImages,QuestionAnswers

class TopicsSerializer(ModelSerializer):
    class Meta:
        model = Topics
        fields= [
            'topic',
            'active',
        ]

class SubTopicsSerializer(ModelSerializer):
    class Meta:
        model = SubTopics
        fields= [
            'subTopic',
            'topic',
            'active',
        ]

class QuestionsSerializer(ModelSerializer):
    class Meta:
        model = Questions
        fields= [
            'question',
            'type',
            'topic',
            'subTopic',
            'difficultyLevel',
            'totalAttempt',
            'totalCurrectAttempt',
            'is_subscribed',
            'thrasoldTime',
            'videoLink',
            'active',
        ]

        
class QuestionImagesSerializer(ModelSerializer):
    class Meta:
        model = QuestionImages
        fields= [
            'question',
            'image',
        ]
        
        
class QuestionAnswersSerializer(ModelSerializer):
    class Meta:
        model = QuestionAnswers
        fields= [
            'question',
            'answer',
            'answanswer_sequenceer',
            'answerType',
            'image',
            'active',
        ]
        