# Generated by Django 2.1.7 on 2019-05-16 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('Course_Code', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Course_Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RegisteredStaffs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Staff_no', models.IntegerField(max_length=100)),
                ('Course_Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RegisteredStaffs', to='Courses.Courses')),
            ],
        ),
        migrations.CreateModel(
            name='RegisteredStd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Std_no', models.IntegerField(max_length=100)),
                ('Course_Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RegisteredStd', to='Courses.Courses')),
            ],
        ),
        migrations.CreateModel(
            name='StudentsRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_No', models.IntegerField()),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('CellPhone_No', models.IntegerField()),
            ],
        ),
    ]
