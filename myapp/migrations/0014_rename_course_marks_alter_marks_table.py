# Generated by Django 5.0 on 2024-03-09 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_course_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course',
            new_name='Marks',
        ),
        migrations.AlterModelTable(
            name='marks',
            table='Marks_table',
        ),
    ]
