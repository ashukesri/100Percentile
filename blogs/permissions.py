from rest_framework.permissions import BasePermission

class IsAuthorOrReadOnly(BasePermission):
    message = 'You must be the author of this post.'
    
    def has_object_permission(self,request,view,obj):
        return obj.Author == request.UserProfile    
    
class IsBlogAuthorOrReadOnly(BasePermission):
    message = 'You must be the author of this post.'
    
    def has_object_permission(self,request,view,obj):
        return obj.blog.Author == request.UserProfile