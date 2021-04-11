import factory
from .models import Article



class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article
    title = factory.Sequence(lambda n: f"My awsome test {n}")