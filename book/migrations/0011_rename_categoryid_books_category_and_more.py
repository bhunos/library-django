# Generated by Django 5.0.3 on 2024-03-28 16:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_books_userid'),
        ('users', '0002_alter_users_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='categoryId',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='books',
            old_name='userId',
            new_name='user',
        ),
        migrations.AddField(
            model_name='category',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.users'),
            preserve_default=False,
        ),
    ]
