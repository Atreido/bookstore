# Generated by Django 5.0 on 2023-12-28 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasure', '0005_remove_news_rating_books_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='rating',
            field=models.CharField(default=1, max_length=50, verbose_name='Рейтинг'),
            preserve_default=False,
        ),
    ]
