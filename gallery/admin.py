from django.contrib import admin
from .models import PostImage , Post



class PostImageAdmin(admin.StackedInline):
    model = PostImage

# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
    class Meta:
        modle = Post


# @admin.register(PostImageAdmin)
class PostImageAdmin(admin.ModelAdmin):
    pass
admin.site.register(PostImage, PostImageAdmin)