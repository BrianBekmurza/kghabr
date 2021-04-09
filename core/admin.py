from django.contrib import admin
from core.models import Article, Author, ArticleImage
# Register your models here.

admin.site.register(Article)
admin.site.register(Author)
admin.site.register(ArticleImage)