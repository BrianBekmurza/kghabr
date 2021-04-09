from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article, Author
from django.db.models import Q
# Create your views here.

# def first_article(request):
#     article = Article.objects.first()
#     return render(
#         request, 
#         'article-page.html',
#         {'article': article}
#     )

def articles(request):
    articles = Article.objects.filter(is_active=True)
    return render(
        request,
        'articles.html',
        {'articles': articles}
    )

def authors(request):
    authors = Author.objects.all()
    return render(
        request,
        'authors.html',
        {'authors': authors}
    )

def author_page(request, pk):
    author = Author.objects.get(pk=pk)
    context = {
        'author': author,
        'user': author.user,
    }
    return render(request, 'author.html', context)

def article_page(request, id):
    article = Article.objects.get(id=id)
    article.views += 1
    article.readers.add(request.user)
    article.save()
    return render(request, "article.html", {"article": article})

def about(request):
    return render(request, 'about.html')

def edit_article(request, pk):
    article = Article.objects.get(id=pk)

    if request.method == "POST":
        title = request.POST.get("title")
        text = request.POST.get("text")
        article.title = title
        article.text = text
        article.save()
        return redirect(article_page, pk)

    return render(request, 'update.html', {"article": article})

def add_article(request):
    if request.method == "GET":
        return render(request, "add_article.html")
    elif request.method == "POST":
        form = request.POST
        title = form.get("title")
        text = form.get("text")
        # new_article = Article (title=title, text=text)
        # new_article.save()

        new_article = Article()
        new_article.title = title
        new_article.text = text
        user = request.user
        if not Author.objects.filter(user==user).exists():
            author = Author(user=user, nik=user.username)
            author.save()

        author = user.author
        new_article.author = author
        new_article.save()
        return redirect(article_page, new_article.pk)

def delete_article(request, id):
    article = Article.objects.get(pk=id)
    article.delete()
    return HttpResponse("Статья успешно удалена")

def hide_article(request, id):
    article = Article.objects.get(id=id)
    article.is_active = False
    article.save()
    return redirect(articles)

def search(request):
    word = request.GET.get('word')
    articles = Article.objects.filter(
        Q(title__icontains=word) | Q(text__icontains=word),
        is_active=True
    )
    return render(request, "articles.html", {'articles': articles})

def top(request):
    articles = Article.objects.order_by("-views")[:3]
    return render(request, "articles.html", {"articles": articles})