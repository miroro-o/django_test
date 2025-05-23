from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')  # Какие поля показывать
    search_fields = ('title', 'content')  # Поиск по заголовкам и содержанию
    list_filter = ('pub_date',)           # Фильтр по дате