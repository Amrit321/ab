from django.contrib import admin

# Register your models here.
from . import models

@admin.register(models.News)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'likes', 'date', 'image')  