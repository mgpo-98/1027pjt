# Generated by Django 3.2.13 on 2022-10-27 05:46

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]