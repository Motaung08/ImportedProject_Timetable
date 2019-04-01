# Generated by Django 2.1.7 on 2019-03-31 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0004_auto_20190329_0532'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisteredStaffs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Staff_no', models.IntegerField(max_length=100)),
                ('Course_Code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RegisteredStd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Std_no', models.IntegerField(max_length=100)),
                ('Course_Code', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='RegisteredStaff',
        ),
        migrations.DeleteModel(
            name='RegisteredStds',
        ),
    ]
