# Generated by Django 3.0 on 2020-02-07 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite1', '0003_auto_20200207_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_path',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]