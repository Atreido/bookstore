# Generated by Django 5.0 on 2023-12-29 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasure', '0006_comments_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='additionalInfo',
            field=models.TextField(default=1, max_length=500, verbose_name='Додаткова інформація'),
            preserve_default=False,
        ),
    ]
