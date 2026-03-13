from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone


class TelegramChannel(models.Model):
    username = models.CharField(max_length=255, unique=True)
    last_message_id = models.BigIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    last_parsed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"@{self.username}"


@receiver(pre_save, sender=TelegramChannel)
def set_last_parsed_at(sender, instance, **kwargs):
    if instance.last_message_id:
        instance.last_parsed_at = timezone.now()
