# Generated by Django 5.0.6 on 2024-07-23 09:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.gender'),
        ),
    ]
