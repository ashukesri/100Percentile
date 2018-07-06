from rest_framework.permissions import BasePermission
from rest_framework import permissions

from rest_framework.authentication import SessionAuthentication, BasicAuthentication 

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening

class BlogPostPermission(BasePermission):
    message = "You are not allowed to edit this post. #2"
#    def has_permission(self, request, view):
#        return False

    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            if request.user.profile.role=='4':
                return obj.author == request.user
            elif request.user.profile.role=='3':
                return obj.status !='4'
            else: 
                return True
        else:
            return False

    
class BlogPostListPermission(BasePermission):
    message = "You are not allowed to access this post."
    def has_permission(self, request, view):
#        print(len(request.user.profile.role))
        if(request.GET.get('user')):
            if int(request.GET.get('user')) == request.user.id:
                return True
            else:
                return request.user.profile.role=="1"
        else:
            return True 

    def has_object_permission(self,request,view,obj):
        return False
    
class UserBlogPostPermission(BasePermission):
    message = "You are not allowed"
    
#    def has_permission(self,request,view):
#        if request.user.profile.role == "3":
#            return request
        

        
#        if(request.GET.get('user')):
#            if int(request.GET.get('user')) == request.user.id:
#                return True
#            else:
#                return request.user.profile.role=="1"
#        else:
#            return True 

        
# if a user is accessing all post then he will see all the published post
# if want to get post of a particular user by "blog?user=3" then he should be loged in
# admin user can see the post of all the user by "blog?user=3"


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
#    
#class BlogPostPermission(BasePermission):
#    message = "You are not allowed to edit this post."
#    def has_object_permission(self,request,view,obj):
#        return obj.author == request.user
