# Generated by Django 2.0.1 on 2020-04-30 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_note_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
