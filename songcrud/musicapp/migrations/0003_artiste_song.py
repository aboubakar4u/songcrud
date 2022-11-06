# Generated by Django 4.1.2 on 2022-11-06 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0002_alter_artiste_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='artiste',
            name='song',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='musicapp.song'),
            preserve_default=False,
        ),
    ]
