
from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .permissions import IsSelfOrReadOnly
from .serializers import UserProfileSerializer
User = get_user_model()

class UserProfileView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsSelfOrReadOnly]
    serializer_class = UserProfileSerializer
    lookup_field = 'user_id'
