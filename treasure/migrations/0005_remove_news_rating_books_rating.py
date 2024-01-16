# Generated by Django 5.0 on 2023-12-28 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasure', '0004_news_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='rating',
        ),
        migrations.AddField(
            model_name='books',
            name='rating',
            field=models.CharField(default=1, max_length=50, verbose_name='Рейтинг'),
            preserve_default=False,
        ),
    ]