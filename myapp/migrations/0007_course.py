# Generated by Django 5.0 on 2024-03-09 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_register_confirm_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('credits', models.IntegerField()),
                ('grade_points', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
