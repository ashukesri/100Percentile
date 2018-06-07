from rest_framework.permissions import BasePermission

#class IsAuthorOrReadOnly(BasePermission):
#    message = 'You must be the author of this post.'
#    
#    def has_object_permission(self,request,view,obj):
#        return obj.Author == request.Profile    
#    
#class IsBlogAuthorOrReadOnly(BasePermission):
#    message = 'You must be the author of this post.'
#    
#    def has_object_permission(self,request,view,obj):
#        return obj.blog.Author == request.Profile
#    
    
class BlogPostPermission(BasePermission):
    message = "You are not allowed to edit this post."
    def has_object_permission(self,request,view,obj):
#        return obj.author == request.user
        return False

        
        
#class BlogPostPermission(BasePermission):
#    message = "You are not allowed to edit this post."
#    
#    def has_object_permission(self,request,view,obj):
#        if(request.user.role=='4'):
#            print("yes")
#            return True
#        else:
#            print("no")
#            return False
