from celery import shared_task
from django.core.files import File
from telethon.errors import FloodWaitError, RpcCallFailError, FloodError

from wallpapers.models import Wallpaper, Category
from .services.telegram_parser import TelegramService


@shared_task(
    bind=True,
    autoretry_for=(RpcCallFailError, FloodError, TimeoutError, OSError),
    retry_backoff=True,
    retry_kwargs={"max_retries": 5},
)
def parse(self, channel: str, limit: int) -> None:
    category_name = channel.lstrip("@")
    category, created_cat = Category.objects.get_or_create(name=category_name)

    service = TelegramService()

    try:
        for bio, filename in service.iter_channel_images(channel, limit=limit):
            with bio:
                django_file = File(bio, name=filename)

                wallpaper, created = Wallpaper.objects.get_or_create(
                    title=f"TG {filename}",
                    defaults={
                        "image": django_file,
                        "user_id": 1,
                        "category": category,
                    },
                )

    except FloodWaitError as e:
        raise self.retry(countdown=e.seconds)
