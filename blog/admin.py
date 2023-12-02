from django.contrib import admin
from .models import Post
from django.contrib import admin

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name',)