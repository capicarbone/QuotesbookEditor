from django.contrib import admin
from .models import Author, Quote

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    list_display = ('id', 'first_name', 'last_name', 'short_description')

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):

    list_display = ('body', 'author_id')


