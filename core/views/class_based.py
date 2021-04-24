from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DeleteView


from ..mixins import IsAuthorMixin
from ..models import Article


class TopView(LoginRequiredMixin, ListView):
    queryset = articles = Article.objects.order_by("-views")[:3]
    template_name = "top.html"

class DeleteArticleView(IsAuthorMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        article = Article.objects.get(pk=kwargs["id"])
        article.delete()
        return HttpResponse("Статья успешно удалена")