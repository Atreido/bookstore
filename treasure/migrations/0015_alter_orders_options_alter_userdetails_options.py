# Generated by Django 5.0 on 2024-01-13 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treasure', '0014_remove_orders_orderedbook_orders_orderedbook'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders',
            options={'verbose_name': 'Замовлення', 'verbose_name_plural': 'Замовлення'},
        ),
        migrations.AlterModelOptions(
            name='userdetails',
            options={'verbose_name': 'Деталі користувача', 'verbose_name_plural': 'Деталі користувача'},
        ),
    ]