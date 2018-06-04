from rest_framework.serializers import ModelSerializer

from .models import BlogPosts,BlogImage


class BlogImageSerializer(ModelSerializer):
    class Meta:
        model = BlogImage
        fields= [
            'id',
            'blog',
            'image',
        ]

    
class BlogPostsSerializer(ModelSerializer):
    class Meta:
        model = BlogPosts
        fields= [
            'id',
            'author',   #this will be added read_only_fields and added in serializer.save
            'difficultyLevel',
            'title',
            'topic',
            'text',
            'published_date',
        ]
        
        
class BlogPostAndImageSerializer(ModelSerializer):
    image = BlogImageSerializer(source='taskimage_set', many=True, read_only=True)
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
            'image',
        ]
#        read_only_fields = ('author',)
        
    def create(self, validated_data):
        image_data = self.context.get('view').request.FILES
        blog= BlogPosts.objects.create(**validated_data)
        for image_data in image_data.values():
            BlogImage.objects.create(blog=blog, image=image_data)
            
        return blog

