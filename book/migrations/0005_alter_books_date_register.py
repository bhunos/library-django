# Generated by Django 5.0.3 on 2024-03-26 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_books_date_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='date_register',
            field=models.DateField(auto_now_add=True),
        ),
    ]
