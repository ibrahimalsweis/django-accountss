from django.contrib import admin 
from .models import PostImage , Post 



class PostImageAdmin(admin.StackedInline):
    model = PostImage
    min_num = 10
    extra =0
    # verbose_name = 'images 00000000000000000000000000'
    # verbose_name_plural = '5555""'x``
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
        
