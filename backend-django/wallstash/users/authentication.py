from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from typing import Optional
from rest_framework.request import Request

User = get_user_model()


class UsernameOrEmailBackend(ModelBackend):
    """
    Аутентифицирует пользователя по username или email
    """

    def authenticate(
        self,
        request: Optional[Request] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        **kwargs
    ) -> Optional[User]:
        if not username or not password:
            return None
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
        except User.DoesNotExist:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
