# Generated by Django 4.0.5 on 2024-09-04 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_details_requestdetails'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='requestdetails',
            options={'verbose_name_plural': 'RequestDetail'},
        ),
    ]
