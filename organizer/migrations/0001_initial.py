# Generated by Django 2.2.12 on 2020-04-19 14:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(help_text='A label for URL config.', max_length=31, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('slug', models.SlugField(help_text='A label for URL config.', max_length=31, unique=True)),
                ('description', models.TextField()),
                ('founded_date', models.DateField(verbose_name='date founded')),
                ('contact_email', models.EmailField(max_length=254)),
                ('website', models.URLField(max_length=255)),
                ('tags', models.ManyToManyField(to='organizer.Tag')),
            ],
            options={
                'ordering': ['name'],
                'get_latest_by': 'founded_date',
            },
        ),
        migrations.CreateModel(
            name='NewsLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link', models.URLField(max_length=255)),
                ('pub_date', models.DateField(verbose_name='date published')),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizer.Startup')),
            ],
            options={
                'ordering': ['-pub_date'],
                'verbose_name': ' news article',
                'get_latest_by': 'pub_date',
            },
        ),
    ]