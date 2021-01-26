from django.contrib import admin
from news.models import New

# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', 'preview')


admin.site.register(New, NewsAdmin)