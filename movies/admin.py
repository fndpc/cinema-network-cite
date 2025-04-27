from django.contrib import admin
from .models import Movies

class MoviesAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_date', 'rating', 'duration', 'filmmaker')  # Поля для отображения в списке
    search_fields = ('title', 'genre', 'filmmaker', 'actors')  # Поля для поиска
    list_filter = ('genre', 'release_date', 'rating')  # Фильтры для списка
    prepopulated_fields = {'slug': ('title',)}  # Автоматическое заполнение поля slug на основе title
    ordering = ('-release_date',)  # Сортировка по дате выхода (новые фильмы первыми)
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'image')
        }),
        ('Информация о фильме', {
            'fields': ('genre', 'release_date', 'rating', 'duration', 'filmmaker', 'actors', 'country')
        }),
    )

# Регистрация модели в админке
admin.site.register(Movies, MoviesAdmin)