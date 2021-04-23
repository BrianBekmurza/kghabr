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
    ordering = ['title']
    list_filter = ['is_active', 'updated_at']
    search_fields = ['title', 'text']

    fields = ('title', 'text', 'picture', 'views', 'created_at', 'updated_at')
    readonly_fields = ('views', 'created_at', 'updated_at', 'readers')

admin.site.register(Article, ArticleAdmin)