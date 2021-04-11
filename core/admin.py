from django.contrib import admin
from core.models import Article, Author, ArticleImage
# Register your models here.

admin.site.register(Author)
admin.site.register(ArticleImage)

class ArticleAdmin(admin.ModelAdmin):
    class Meta:
        model = Article

    list_display = ("title", "author", "views", "is_active")
    list_editable = ("author", )

admin.site.register(Article, ArticleAdmin)