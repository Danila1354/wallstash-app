from django.db import models
from django.conf import settings

from wallpapers.models import Wallpaper

class Collection(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="collections"
    )
    wallpapers = models.ManyToManyField(
        Wallpaper,
        through="CollectionWallpaper",
        related_name="collections"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "title")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} ({self.user.username})"


class CollectionWallpaper(models.Model):
    collection = models.ForeignKey(
        Collection, on_delete=models.CASCADE, related_name="collection_wallpapers"
    )
    wallpaper = models.ForeignKey(
        Wallpaper, on_delete=models.CASCADE, related_name="collection_entries"
    )
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("collection", "wallpaper")
        ordering = ["-added_at"]

    def __str__(self):
        return f"{self.wallpaper.title} in {self.collection.title}"
