# Generated by Django 5.0 on 2024-03-09 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_alter_studentprofile_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='branch',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='contact',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='full_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='studentId',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='year_of_study',
            field=models.IntegerField(max_length=100),
        ),
    ]