from django.contrib import admin

from telegram_parser.models import TelegramChannel


@admin.register(TelegramChannel)
class TelegramChannelAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "last_message_id",
        "is_active",
        "last_parsed_at",
        "created_at",
    )
    list_filter = ("is_active", "created_at")
    search_fields = ("username",)
