from rest_framework.permissions import BasePermission
from rest_framework import permissions


class QuestionPermission(BasePermission):
    message = "You are not allowed to access this question. #"
#    def has_permission(self, request, view):
#        return False

    def has_object_permission(self,request,view,obj):
        if request.user.profile.role=='4':
            return obj.author == request.user
        elif request.user.profile.role=='3':
            return obj.status !='4'
        else: return True;

    
class BlogPostListPermission(BasePermission):
    message = "You are not allowed to access this post."
    def has_permission(self, request, view):
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
        
        
        
#        ('1',('Admin')),
#        ('2',('Publisher')),
#        ('3',('Reviewer')),
#        ('4',('Visitor'))
        
        
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
