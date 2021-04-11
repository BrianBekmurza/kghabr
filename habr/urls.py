"""habr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', sing_in, name='login'),
    path('logout', sing_out, name='logout'),
    # path('article/', first_article, name='first-article-page'),
    path('', articles, name='articles'),
    path('article/<int:id>/', article_page, name='article'),
    path('authors/', authors, name='authors'),
    path('author/<int:pk>/edit', author_page, name='author'),
    path('about/', about, name='about'),
    path('article/<int:pk>/edit/', edit_article, name='article-edit'),
    path('article/add/', add_article, name="article-add"),
    path('article/<int:id>/delete/', delete_article, name='article_delete'),
    path('article/<int:id>/hide/', hide_article, name='article_hide'),
    path('search/', search, name='search'),
    path('top/', top, name='top')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
