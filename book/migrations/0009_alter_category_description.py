# Generated by Django 5.0.3 on 2024-03-27 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0008_category_books_categoryid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="description",
            field=models.TextField(blank=True),
        ),
    ]
