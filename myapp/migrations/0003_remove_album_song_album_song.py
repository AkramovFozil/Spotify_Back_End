# Generated by Django 4.2.7 on 2023-11-18 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_song_album_remove_song_image_album_song'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='song',
        ),
        migrations.AddField(
            model_name='album',
            name='song',
            field=models.ManyToManyField(to='myapp.song'),
        ),
    ]
