# Generated by Django 5.0 on 2024-01-19 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythonDev', '0002_page_delete_indexpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='url_name',
            field=models.CharField(default=models.CharField(default='Новая страница', max_length=20), max_length=20, unique=True),
        ),
    ]