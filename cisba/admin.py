from django.contrib import admin

# Register your models here.

from .models import Category, Article, Author
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Author)