# Generated by Django 5.2 on 2025-04-10 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stadiums', '0006_remove_stadiumbooking_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stadiumbooking',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
