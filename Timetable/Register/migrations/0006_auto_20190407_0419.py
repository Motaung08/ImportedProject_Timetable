# Generated by Django 2.1.7 on 2019-04-07 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0005_auto_20190331_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeredstd',
            name='Course_Code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register.Courses'),
        ),
    ]