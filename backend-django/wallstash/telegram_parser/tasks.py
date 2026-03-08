from celery import shared_task
from django.core.files import File

from wallpapers.models import Wallpaper, Category
from telegram_parser.services.telegram_parser import TelegramService


@shared_task
def parse(channel, limit):
    category_name = channel.lstrip("@")
    category, created_cat = Category.objects.get_or_create(name=category_name)

    service = TelegramService()

    for bio, filename in service.iter_channel_images(channel, limit=limit):
        django_file = File(bio, name=filename)
        wallpaper, created = Wallpaper.objects.get_or_create(
            title=f"TG {filename}",
            defaults={
                "image": django_file,
                "user_id": 1,
                "category": category,
            },
        )
        bio.close()
