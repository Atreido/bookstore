# Generated by Django 5.0 on 2023-12-28 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasure', '0003_comments_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='rating',
            field=models.CharField(default=1, max_length=50, verbose_name='Рейтинг'),
            preserve_default=False,
        ),
    ]