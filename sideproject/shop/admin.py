from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'short_desc', 'price', 'is_publish']

    list_display_links = ['name']

    list_filter = ['is_publish', 'updated_at']

    # or 조건으로 검색됨
    search_fields = ['name']

    def short_desc(self, item):
        return item.description[:20]
