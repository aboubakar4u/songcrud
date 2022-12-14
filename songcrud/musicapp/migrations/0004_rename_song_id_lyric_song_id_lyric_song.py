# Generated by Django 4.1.2 on 2022-11-06 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0003_artiste_song'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lyric',
            old_name='song_id',
            new_name='Song_id',
        ),
        migrations.AddField(
            model_name='lyric',
            name='song',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='musicapp.song'),
            preserve_default=False,
        ),
    ]
