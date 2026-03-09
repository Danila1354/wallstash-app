import os
from io import BytesIO
from telethon import TelegramClient
from telethon.tl.types import MessageMediaDocument
from dotenv import load_dotenv
from typing import Iterator, Tuple

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION_NAME = "wallstash_parser"
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png"}


class TelegramService:
    def __init__(self) -> None:
        self.client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
        self.client.start()

    def iter_channel_images(
        self, channel: str, limit: int = 20
    ) -> Iterator[Tuple[BytesIO, str]]:
        """Генератор, который возвращает файлы по одному."""
        with self.client:
            for message in self.client.iter_messages(channel, limit=limit):
                if not message.media or not isinstance(
                    message.media, MessageMediaDocument
                ):
                    continue

                filename = message.file.name or f"{message.id}.dat"
                ext = os.path.splitext(filename)[1].lower()
                if ext not in ALLOWED_EXTENSIONS:
                    continue

                bio = BytesIO()
                bio.name = filename
                self.client.loop.run_until_complete(
                    self.client.download_media(message.media, file=bio)
                )
                bio.seek(0)
                yield bio, filename
