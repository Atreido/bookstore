# Generated by Django 5.0 on 2023-12-28 19:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasure', '0002_alter_books_options_alter_discount_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name="Імя'"),
            preserve_default=False,
        ),
    ]