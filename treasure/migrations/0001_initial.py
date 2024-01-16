# Generated by Django 5.0 on 2023-12-27 15:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20, verbose_name='Категорія')),
            ],
            options={
                'verbose_name': 'Категорія',
                'verbose_name_plural': 'Категорії',
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Назва')),
                ('description', models.TextField(max_length=300, verbose_name='Опис')),
                ('discount', models.SmallIntegerField(default=0, verbose_name='Знижка')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Пости',
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75, verbose_name='Назва')),
                ('author', models.CharField(max_length=75, verbose_name='Автор')),
                ('description', models.TextField(max_length=1000, verbose_name='Опис')),
                ('image', models.ImageField(blank=True, upload_to='uploads')),
                ('price', models.FloatField(verbose_name='Ціна')),
                ('pages', models.SmallIntegerField(verbose_name='Сторінок')),
                ('ISBN', models.CharField(max_length=25, verbose_name='ISBN')),
                ('quantity', models.IntegerField(verbose_name='Кількість на складі')),
                ('fk_category', models.ManyToManyField(blank=True, related_name='books', to='treasure.categories')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Пости',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish_date', models.DateTimeField(auto_created=True, verbose_name='Дата і час')),
                ('comment', models.TextField(verbose_name='Коментар')),
                ('posted', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treasure.books', verbose_name='Пост')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Користувач')),
            ],
            options={
                'verbose_name': 'Коментар',
                'verbose_name_plural': 'Коментарі',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_date', models.DateTimeField(auto_created=True, verbose_name='дата і час')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='uploads')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='користувач')),
            ],
            options={
                'verbose_name': 'Новина',
                'verbose_name_plural': 'Новини',
            },
        ),
    ]