# Generated by Django 2.0.1 on 2020-04-28 12:30

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('notes', '0002_note_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
