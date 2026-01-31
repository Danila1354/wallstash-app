from PIL import Image
import uuid
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from taggit.managers import TaggableManager

from .utils import wallpaper_upload_to


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Wallpaper(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="wallpapers"
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to=wallpaper_upload_to)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="wallpapers"
    )
    tags = TaggableManager(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes_count = models.PositiveIntegerField(default=0)
    downloads_count = models.PositiveIntegerField(default=0)
    width = models.PositiveIntegerField(blank=True)
    height = models.PositiveIntegerField(blank=True)
    file_size = models.PositiveBigIntegerField(blank=True)

    @property
    def orientation(self):
        return "landscape" if self.width >= self.height else "portrait"

    def save(self, *args, **kwargs):
        if self.image:
            self.file_size = self.image.size
            img = Image.open(self.image)
            self.width, self.height = img.size
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



@receiver(pre_save, sender=Wallpaper)
def generate_slug(sender, instance, **kwargs):
    if not instance.slug:
        base_slug = slugify(instance.title)
        instance.slug = f"{base_slug}-{uuid.uuid4().hex[:8]}"


class WallpaperLike(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='wallpaper_likes'
    )
    wallpaper = models.ForeignKey(
        Wallpaper,
        on_delete=models.CASCADE,
        related_name='liked_by'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'wallpaper'],
                name='unique_user_wallpaper_like'
            )
        ]