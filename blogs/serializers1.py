from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer

from .models import BlogPosts,BlogImages

class BlogImagesSerializer(ModelSerializer):
    class Meta:
        model = BlogImages
        fields= [
            'id',
            'blog',
            'image',
        ]
    

#class TaskSerializer(HyperlinkedModelSerializer):
#    user = serializers.ReadOnlyField(source='user.username')
#    images = TaskImageSerializer(source='taskimage_set', many=True, read_only=True)
#
#    class Meta:
#        model = Task
#        fields = ('id', 'title', 'user', 'images')
#
#    def create(self, validated_data):
#        images_data = self.context.get('view').request.FILES
#        task = Task.objects.create(title=validated_data.get('title', 'no-title'),user_id=1)
#        for image_data in images_data.values():
#            TaskImage.objects.create(task=task, image=image_data)
#        return task
#    
    

class  BlogPostAndImagesSerializer(ModelSerializer):
    images=BlogImagesSerializer(source='taskimage_set', many=True)
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
            'images',
        ]
        
            
    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        blog = BlogPosts.objects.create(validated_data)
        
        for image_data in images_data.values():
            BlogImages.objects.create(blog=blog, image=image_data)
        return blog
    

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

    