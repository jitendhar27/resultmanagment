# Generated by Django 5.0 on 2024-03-09 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_register_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='register',
            table='Registrations',
        ),
    ]