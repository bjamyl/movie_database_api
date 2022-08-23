from rest_framework import permissions

class AdminOrReadOnly(permissions.isAdminUser):
    
    def has_permission(self, request, view):
        admin_permission = bool(request.user and request.user.is_staff)
        return request.method == 'GET' and admin_permission
    

class ReviewUserOrReadOnly(permissions.BasePermisson):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
            # Check permissions for read-only request
        else:
            return obj.review_user == request.user
            #check permissions for write request