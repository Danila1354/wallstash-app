from django.db.models import F, QuerySet
from django_filters import rest_framework as filters

from .models import Wallpaper


class WallpaperFilter(filters.FilterSet):
    tags = filters.CharFilter(method="filter_by_tags")
    orientation = filters.CharFilter(method="filter_by_orientation")

    class Meta:
        model = Wallpaper
        fields = ["category"]

    def filter_by_tags(
        self, queryset: QuerySet[Wallpaper], name: str, value: str
    ) -> QuerySet:
        tag_list = value.split(",")
        return queryset.filter(
            tags__name__in=[tag.strip() for tag in tag_list]
        ).distinct()

    def filter_by_orientation(
        self, queryset: QuerySet[Wallpaper], name: str, value: str
    ) -> QuerySet:
        if value.lower() == "landscape":
            return queryset.filter(width__gte=F("height"))
        elif value.lower() == "portrait":
            return queryset.filter(height__gt=F("width"))
        elif value.lower() == "square":
            return queryset.filter(width=F("height"))
        return queryset
