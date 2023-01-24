# Generated by Django 4.1.4 on 2023-01-09 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=50)),
                ('sage', models.IntegerField()),
                ('sphno', models.BigIntegerField()),
                ('scity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentapp.city')),
                ('scourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentapp.course')),
            ],
        ),
    ]