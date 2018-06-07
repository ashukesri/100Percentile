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

class QuestionAnswerSerializer(ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields= [
            'question',
            'answer',
            'is_right_option',
            'answer_sequence',
            'image',
            'active',
        ]
        

class QuestionSerializer(ModelSerializer):
#    image = QuestionImageSerializer(source='taskimage_set', many=True, read_only=True)
    QuestionImages=QuestionImageSerializer(many=True, read_only=True)
    QuestionAnswers=QuestionAnswerSerializer(many=True)
    class Meta:
        model = Question
        fields= [
            'id',
            'question',
            'questionType',
            'topic',
            'subTopic',
            'difficultyLevel',
            'totalAttempt',
            'totalCorrectAttempt',
            'is_subscribed',
            'thrasoldTime',
            'videoLink',
            'active',
            'QuestionImages',
            'QuestionAnswers',
        ]
        read_only_fields = ('totalAttempt','totalCorrectAttempt')
        
#    def validate(self, data):
#
#        if data['questionType'] ==1 and QuestionAnswers==True:
#            raise serializers.ValidationError("You are accessing options for subjective question")
#        return data

    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
#        request = self.context.get('request')
        question= Question.objects.create(**validated_data)
        for image_data in images_data.values():
            QuestionImage.objects.create(question=question, image=image_data)
            
#        if request.data.get('QuestionAnswers'):
#            QuestionAnswers_data = request.data.get('QuestionAnswers')
#            for QuestionAnswer_data in QuestionAnswers_data:
#                QuestionAnswer.objects.create(question=question, **QuestionAnswer_data)
        
        return question

    def update(self, instance, validated_data):
        images_data = self.context.get('view').request.FILES
        
        instance.question = validated_data.get("question", instance.question)
        instance.questionType = validated_data.get("questionType", instance.questionType)
        instance.topic= validated_data.get("topic", instance.topic)
        instance.subTopic= validated_data.get("subTopic", instance.subTopic)
        instance.difficultyLevel= validated_data.get("difficultyLevel", instance.subTopic)
        instance.is_subscribed= validated_data.get("is_subscribed", instance.is_subscribed)
        instance.thrasoldTime= validated_data.get("thrasoldTime", instance.thrasoldTime)
        instance.videoLink= validated_data.get("videoLink", instance.videoLink)
        instance.active= validated_data.get("active", instance.active)

        if images_data:
            for image_data in images_data.values():
                QuestionImage.objects.create(question=instance, image=image_data)
        instance.save()
        return instance
            
        

