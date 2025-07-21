from django.contrib import admin
from .models import Post, Category, User

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(User)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
