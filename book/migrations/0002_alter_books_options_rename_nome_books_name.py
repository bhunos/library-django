# Generated by Django 5.0.3 on 2024-03-26 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'verbose_name': 'Book'},
        ),
        migrations.RenameField(
            model_name='books',
            old_name='nome',
            new_name='name',
        ),
    ]
