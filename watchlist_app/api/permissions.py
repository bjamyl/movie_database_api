from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
            # Check permissions for read-only request
        else:
            bool(request.user and request.user.is_staff)   
        
            

class ReviewUserOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
            # Check permissions for read-only request
        else:
            return obj.review_user == request.user
            #check permissions for write request