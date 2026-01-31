from rest_framework import permissions

class IsSelfOrReadOnly(permissions.BasePermission):
    """
    Позволяет изменять объект только его владельцу,
    все остальные имеют только read-only доступ.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj