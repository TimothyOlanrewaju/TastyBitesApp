# Generated by Django 3.2.7 on 2024-07-16 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name_plural': 'Department'},
        ),
        migrations.AlterModelOptions(
            name='unit',
            options={'verbose_name_plural': 'Unit'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'User'},
        ),
    ]
