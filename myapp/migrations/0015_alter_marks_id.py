# Generated by Django 5.0 on 2024-03-09 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_rename_course_marks_alter_marks_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
