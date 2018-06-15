from rest_framework.serializers import ModelSerializer

from .models import BlogPosts,BlogImages


class BlogPostsSerializer(ModelSerializer):
    class Meta:
        model = BlogPosts
        fields= [
            'id',
            'author',
            'difficultyLevel',
            'title',
            'topic',
            'text',
            'published_date',
        ]
        

        
class BlogPostAndImagesSerializer(ModelSerializer):
    blog=BlogPostsSerializer(required=True)
    class Meta:
        model = BlogImages
        fields= [
            'id',
            'blog',
            'image',
        ]
    
    def create(self, validated_data):
        blog_data = validated_data.pop('blog')
        blog= BlogPosts.objects.create(**blog_data)
        blog_image=BlogImages.objects.create(blog=blog, **validated_data)
        return blog_image

    def update(self, instance, validated_data):
        blog_data = validated_data.pop('blog', None)
        blog = instance.blog
        instance.image = validated_data.get("image", instance.image)
        instance.save()
        if blog_data:
            user.difficultyLevel = user_data.get("difficultyLevel", user.difficultyLevel)
            user.title = user_data.get("title", user.title)
            user.topic= user_data.get("topic", user.topic)
            user.text= user_data.get("text", user.text)
            user.save()

            
#        ('1',('Admin')),
#        ('2',('Publisher')),
#        ('3',('Reviewer')),
#        ('4',('Visitor'))

#class BlogPostAndImagesSerializer(ModelSerializer):
#    blog=BlogPostsSerializer(required=True)
#    class Meta:
#        model = BlogImages
#        fields= [
#            'id',
#            'blog',
#            'image',
#        ]
#    
#    def create(self, validated_data):
#        blog_data = validated_data.pop('blog')
#        blog= BlogPosts.objects.create(**blog_data)
#        blog_image=BlogImages.objects.create(blog=blog, **validated_data)
#        return blog_image
#
#    def update(self, instance, validated_data):
#        blog_data = validated_data.pop('blog', None)
#        blog = instance.blog
#        instance.image = validated_data.get("image", instance.image)
#        instance.save()
#        if blog_data:
#            user.difficultyLevel = user_data.get("difficultyLevel", user.difficultyLevel)
#            user.title = user_data.get("title", user.title)
#            user.topic= user_data.get("topic", user.topic)
#            user.text= user_data.get("text", user.text)
#            user.save()

    