from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    A profile can only get, change and delete  
    family members/tasks that belongs to that profile. 
    """
    def has_object_permission(self, request, view, obj):
        return obj.belongs_to_profile.user == request.user 
