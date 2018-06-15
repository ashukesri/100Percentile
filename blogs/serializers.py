from rest_framework.serializers import ModelSerializer, StringRelatedField
from rest_framework import serializers
from .models import BlogPost,BlogImage


class BlogImageSerializer(ModelSerializer):
    class Meta:
        model = BlogImage
        fields= [
            'id',
            'blog',
            'image',
        ]

class BlogPostSerializer(ModelSerializer):
#    image = BlogImageSerializer(source='taskimage_set', many=True, read_only=True)
    BlogImages=BlogImageSerializer(many=True, read_only=True)

    class Meta:
        model = BlogPost
        fields= [
            'id',
#            'author',   #this will be added read_only_fields and added in serializer.save
            'difficultyLevel',
            'title',
            'topic',
            'status',
            'text',
            'published_date',
            'BlogImages',
        ]
        read_only_fields = ('author',)
        
    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        blog= BlogPost.objects.create(**validated_data)
        for image_data in images_data.values():
            BlogImage.objects.create(blog=blog, image=image_data)
        return blog
    
    
    def update(self, instance, validated_data):
        images_data = self.context.get('view').request.FILES
        instance.difficultyLevel = validated_data.get("difficultyLevel", instance.difficultyLevel)
        instance.title = validated_data.get("title", instance.title)
        instance.topic= validated_data.get("topic", instance.topic)
        instance.status= validated_data.get("status", instance.status)
        instance.text= validated_data.get("text", instance.text)
        

        if images_data:
            for image_data in images_data.values():
                BlogImage.objects.create(blog=instance, image=image_data)
        instance.save()
        return instance
                
    def validate_status(self, value):
        """
        Check that the Status of the post is changed according to the permssion.
        """
        if(self.context['request'].user.profile.role == '4'):
            if(value == 1 or value==2):
                return value
            else:
                raise serializers.ValidationError("User do not have permission to change the status of the post #4")
        elif(self.context['request'].user.profile.role == '3'):
            if(value == 1 or value == 2 or value == 3):
                return value
            else:
                raise serializers.ValidationError("User do not have permission to Publish the post #5")
        else:
            return value

    
#        ('1',('Admin')),
#        ('2',('Publisher')),
#        ('3',('Reviewer')),
#        ('4',('Visitor'))
        
#        ('1', ('Submited')),
#        ('2', ('Discarded')),
#        ('3', ('Reviewed')),
#        ('4', ('Publised'))