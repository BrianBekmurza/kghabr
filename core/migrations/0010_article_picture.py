# Generated by Django 3.1.7 on 2021-04-02 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_article_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='articles_image', verbose_name='Картинка статьи'),
        ),
    ]
