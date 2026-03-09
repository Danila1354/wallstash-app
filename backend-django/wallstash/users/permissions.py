from typing import Any
from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import APIView


class IsSelfOrReadOnly(permissions.BasePermission):
    """
    Позволяет изменять объект только его владельцу,
    все остальные имеют только read-only доступ.
    """

    def has_object_permission(self, request: Request, view: APIView, obj: Any) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj
