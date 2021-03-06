from django.test import TestCase
from django.urls import reverse
from .models import Article 
from .factories import ArticleFactory, UserFactory

# Create your tests here.
class HomepageTestCase(TestCase):
    def setUp(self):
        self.url = reverse('articles')

    def test_homepage_loads_success(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'article')

    def test_homepage_with_articles_success(self):
        # n = 3
        # for i in range(3):
        #     article = Article()
        #     article.title = 'Test title'
        #     article.text = 'bla bla bla text'
        #     article.save()

        n = 3
        for i in range(n):
            article = ArticleFactory()

        response = self.client.get(self.url)
        self.assertIn('articles', response.context)
        articles = Article.objects.filter(is_active=True)
        self.assertEqual(articles.count(), n)

        for article in articles:
            self.assertContains(response, article.title)
            print(article.title)
            self.assertContains(response, article.text)

class LoginTestCase(TestCase):
    def test_login_success(self):
        user = UserFactory()
        url = reverse('login')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

