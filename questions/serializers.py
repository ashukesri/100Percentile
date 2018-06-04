from rest_framework.serializers import ModelSerializer

from .models import Topic,SubTopic,Question,QuestionImage,QuestionAnswer

class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields= [
            'topic',
            'active',
        ]
        

class SubTopicSerializer(ModelSerializer):
    class Meta:
        model = SubTopic
        fields= [
            'subTopic',
            'topic',
            'active',
        ]
        

class QuestionImageSerializer(ModelSerializer):
    class Meta:
        model = QuestionImage
        fields= [
            'question',
            'image',
        ]
        

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields= [
            'question',
            'questionType',
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
    
    
class QuestionAndImageSerializer(ModelSerializer):
    image = QuestionImageSerializer(source='taskimage_set', many=True, read_only=True)

    class Meta:
        model = Question
        fields= [
            'question',
            'questionType',
            'topic',
            'subTopic',
            'difficultyLevel',
            'totalAttempt',
            'totalCurrectAttempt',
            'is_subscribed',
            'thrasoldTime',
            'videoLink',
            'active',
            'image',
        ]
#        read_only_fields = ('id',)

    def create(self, validated_data):
        image_data = self.context.get('view').request.FILES
        question= Question.objects.create(**validated_data)
        for image_data in image_data.values():
            BlogImage.objects.create(question=question, image=image_data)
            
        return question

        

class QuestionAnswerSerializer(ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields= [
            'question',
            'answer',
            'answanswer_sequenceer',
            'answerType',
            'image',
            'active',
        ]
        