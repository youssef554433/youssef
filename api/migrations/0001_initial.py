# Generated by Django 4.2.13 on 2024-09-15 06:44

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberchapter', models.CharField(max_length=100)),
                ('namemanga', models.CharField(max_length=100)),
                ('datepost', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='img')),
                ('typee', models.CharField(blank=True, choices=[('manga', 'مانجا يابانية'), ('manho', 'مانهو كورية')], max_length=70, null=True)),
                ('aounther', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField()),
                ('reviews', models.CharField(blank=True, max_length=100, null=True)),
                ('chapter', models.ManyToManyField(blank=True, null=True, related_name='chapter', to='api.chapter')),
            ],
        ),
        migrations.CreateModel(
            name='ImageChapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='imaaa')),
                ('chapters', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imageschapter', to='api.chapter')),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='imagemanga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='imagechapter', to='api.manga'),
        ),
        migrations.CreateModel(
            name='Cartitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartmanga', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='api.manga')),
            ],
        ),
    ]