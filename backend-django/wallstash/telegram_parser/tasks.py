from celery import shared_task
from django.core.files import File
from telethon.errors import FloodWaitError, RpcCallFailError, FloodError

from wallpapers.models import Wallpaper, Category
from .services.telegram_parser import TelegramService
from .models import TelegramChannel


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
    channel_obj, created_tg = TelegramChannel.objects.get_or_create(
        username=channel, defaults={"username": channel}
    )
    last_message_id = channel_obj.last_message_id

    try:
        for bio, filename, message_id in service.iter_channel_images(
            channel, limit=limit, offset_id=last_message_id
        ):
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
                channel_obj.last_message_id = message_id
                channel_obj.save(update_fields=["last_message_id"])

    except FloodWaitError as e:
        raise self.retry(countdown=e.seconds)
