# Generated by Django 4.2.10 on 2024-02-25 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=300)),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menues',
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=300)),
                ('manu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu_app.menu')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
