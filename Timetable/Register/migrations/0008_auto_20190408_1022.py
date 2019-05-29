# Generated by Django 2.1.7 on 2019-04-08 08:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0007_auto_20190407_0501'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcements',
            name='Created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='announcements',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
