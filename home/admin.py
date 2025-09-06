from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html, urlencode
from django.db.models import Count

# Register your models here.
from . import models

@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'likes', 'date', 'image', 'comment_count')  

    
    
    def comment_count(self, obj):
        link = (reverse('admin:home_comment_changelist')
                + '?'
                + urlencode({
                    'post_id': str(obj.id)
                }))
        return format_html('<a href="{}">{} comments</a>', link, obj.comment_count)
        
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            comment_count=Count('comment')
            
            )


    




@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','body', 'date', 'post')   

