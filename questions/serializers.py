from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import (
    Topic,SubTopic,Question,QuestionImage,QuestionOption,
    QuestionSolution,
    QuestionDiscussion,
)

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

class QuestionSolutionSerializer(ModelSerializer):
    class Meta:
        model = QuestionSolution
        fields= [
            'question',
            'author',
            'solution',
            'image',
            'created_at',
            'updated_at',
        ]
        
class QuestionDiscussionSerializer(ModelSerializer):
    class Meta:
        model = QuestionDiscussion
        fields= [
            'question',
            'user',
            'comment',
            'created_at',
            'updated_at',
        ]
        

class QuestionImageSerializer(ModelSerializer):
    class Meta:
        model = QuestionImage
        fields= [
            'id',
            'question',
            'image',
        ]

class QuestionOptionSerializer(ModelSerializer):
    class Meta:
        model = QuestionOption
        fields= [
            'question',
            'answer',
            'is_right_option',
            'answer_sequence',
            'image',
            'active',
        ]
        

class QuestionSerializer(ModelSerializer):
    
    QuestionImages=QuestionImageSerializer(many=True, read_only=True)
    QuestionOptions=QuestionOptionSerializer(many=True , read_only=True)
    class Meta:
        model = Question
        fields= [
            'id',
            'author',
            'question',
            'questionType',
            'topic',
            'status',
            'subTopic',
            'difficultyLevel',
            'totalAttempt',
            'totalCorrectAttempt',
            'is_subscribed',
            'thrasoldTime',
            'videoLink',
            'active',
            'QuestionImages',
            'QuestionOptions',
        ]
        read_only_fields = ('totalAttempt','totalCorrectAttempt','author')

        
    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        question= Question.objects.create(**validated_data)
        for image_data in images_data.values():
            QuestionImage.objects.create(question=question, image=image_data)
                
        return question

    def update(self, instance, validated_data):
        images_data = self.context.get('view').request.FILES

        instance.question = validated_data.get("question", instance.question)
        instance.questionType = validated_data.get("questionType", instance.questionType)
        instance.topic= validated_data.get("topic", instance.topic)
        instance.status= validated_data.get("status", instance.status)
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
            
    def validate_status(self, value):
        """
        Check that the Status of the quesion is changed according to the permssion.
        """
        if(self.context['request'].user.profile.role == '4'):
            if(value == 1 or value== 2):
                return value
            else:
                raise serializers.ValidationError("User do not have permission to change the status of the question #Q4")
        elif(self.context['request'].user.profile.role == '3'):
            if(value == 1 or value == 2 or value == 3):
                print("value edited",value)
                return value
            else:
                raise serializers.ValidationError("User do not have permission to Publish the Question #Q5")
        else:
            return value  

