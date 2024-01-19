from django.contrib import admin
from .models import PageContent


class PagesAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title',)


admin.site.register(PageContent, PagesAdmin)
