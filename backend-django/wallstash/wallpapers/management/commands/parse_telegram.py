from django.core.management.base import BaseCommand
from django.core.files import File
from wallpapers.models import Wallpaper, Category
from wallpapers.services.telegram_parser import TelegramService

class Command(BaseCommand):
    help = "Parse Telegram channel and add wallpapers"

    def add_arguments(self, parser):
        parser.add_argument("--channel", required=True, help="Telegram channel username or ID")
        parser.add_argument("--limit", type=int, default=50, help="Number of latest messages to parse")

    def handle(self, *args, **options):
        channel = options["channel"]
        limit = options["limit"]

        category_name = channel.lstrip('@')
        category, created_cat = Category.objects.get_or_create(title=category_name)
        if created_cat:
            self.stdout.write(self.style.SUCCESS(f"Created new category: {category_name}"))

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

            if created:
                self.stdout.write(self.style.SUCCESS(f"Saved wallpaper: {filename}"))
            else:
                self.stdout.write(self.style.WARNING(f"Wallpaper already exists: {filename}"))