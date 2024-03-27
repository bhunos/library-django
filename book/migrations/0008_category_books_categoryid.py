# Generated by Django 5.0.3 on 2024-03-27 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0007_alter_books_borrowed_name_alter_books_co_author_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("description", models.TimeField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name="books",
            name="categoryId",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="book.category",
            ),
            preserve_default=False,
        ),
    ]
