from rest_framework.permissions import BasePermission, SAFE_METHODS


class UpdateOwnProfile(BasePermission):
    """Check whether user is updating it's own profile or not."""
    
    def has_object_permission(self, request, view, obj):
        """Check whether requesting user is authorized or not."""
        if request.method in SAFE_METHODS:
            return True
        return obj.id == request.user.id