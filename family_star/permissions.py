from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    A profile can only change family members that belongs to that profile. 
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.belongs_to_profile.user == request.user