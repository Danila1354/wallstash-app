from datetime import datetime
import os

from .models import Wallpaper


def wallpaper_upload_to(instance: Wallpaper, filename: str) -> str:
    ext = filename.split(".")[-1]
    unique_filename = f"{instance.slug}.{ext}"
    now = datetime.now()
    return os.path.join(
        "wallpapers", str(now.year), str(now.month), str(now.day), unique_filename
    )
