from rest_framework.permissions import  BasePermission, SAFE_METHODS

class IsSuperuser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)

class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS and request.user.is_authenticated  :
            return True
        return bool(request.user and request.user.is_staff or request.user.is_superuser) 

class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS and request.user.is_authenticated:
            return True
        
        return bool(
            request.user.is_superuser or 
            obj.author == request.user
        )

class IsSuperuserOrStaffReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS and request.user.is_authenticated:
            return True
        return bool(request.user and request.user.is_superuser or request.user.is_staff)

