from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Q, F

class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    following = models.ManyToManyField(
        "self",
        through="UserFollow",
        symmetrical=False,
        related_name="followers",
        blank=True,
    )

    def __str__(self):
        return self.username

    class Meta:
        db_table = "users"


class UserFollow(models.Model):
    from_user = models.ForeignKey(
        User,
        related_name='following_relations',
        on_delete=models.CASCADE
    )
    to_user = models.ForeignKey(
        User,
        related_name='follower_relations',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
        models.UniqueConstraint(
            fields=['from_user', 'to_user'],
            name='unique_user_follow'
        ),
        models.CheckConstraint(
            condition=~Q(from_user=F('to_user')),
            name='prevent_self_follow'
        ),
    ]
