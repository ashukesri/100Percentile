from rest_framework.serializers import ModelSerializer

from .models import BlogPosts,BlogImages


class BlogPostsSerializer(ModelSerializer):
    class Meta:
        model = BlogPosts
        fields= [
            'author',
            'difficultyLevel',
            'title',
            'topic',
            'text',
            'published_date',
        ]
        

class BlogImagesSerializer(ModelSerializer):
    class Meta:
        model = BlogImages
        fields= [
            'blog',
            'image',
        ]


    