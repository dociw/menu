# Generated by Django 4.2.10 on 2024-02-25 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='manu',
            new_name='menu',
        ),
    ]