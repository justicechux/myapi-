from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "slug"]


admin.site.register(Post, PostAdmin)

# Register your models here.
