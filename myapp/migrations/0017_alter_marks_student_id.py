# Generated by Django 5.0 on 2024-03-09 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_remove_marks_studentid_marks_student_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='student_id',
            field=models.CharField(max_length=100),
        ),
    ]
