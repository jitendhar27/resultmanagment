# Generated by Django 5.0 on 2024-03-09 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_studentprofile_address_studentprofile_branch_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='studentId',
            field=models.CharField(max_length=12),
        ),
    ]
