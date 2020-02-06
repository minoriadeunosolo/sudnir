from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    message = "Only owner can modify"

    def has_object_permission(self, request, view, obj):
        """ True if is a safe method or user is the owner
        """
        return request.method in permissions.SAFE_METHODS or request.user == obj.owner
