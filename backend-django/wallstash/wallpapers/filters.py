from django.db.models import F
from django_filters import rest_framework as filters

from .models import Wallpaper


class WallpaperFilter(filters.FilterSet):
    tags = filters.CharFilter(method='filter_by_tags')
    orientation = filters.CharFilter(method='filter_by_orientation')

    class Meta:
        model = Wallpaper
        fields = ['category']

    def filter_by_tags(self, queryset, name, value):
        tag_list = value.split(',')
        return queryset.filter(
            tags__name__in=[tag.strip() for tag in tag_list]
        ).distinct()

    def filter_by_orientation(self, queryset, name, value):
        if value.lower() == 'landscape':
            return queryset.filter(width__gte=F('height'))
        elif value.lower() == 'portrait':
            return queryset.filter(height__gt=F('width'))
        elif value.lower() == 'square':
            return queryset.filter(width=F('height'))
        return queryset
