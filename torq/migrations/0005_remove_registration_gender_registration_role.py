# Generated by Django 5.1.1 on 2024-10-06 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torq', '0004_remove_registration_profile_registration_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='gender',
        ),
        migrations.AddField(
            model_name='registration',
            name='role',
            field=models.CharField(blank=True, choices=[('A', 'admin'), ('C', 'customer'), ('S', 'seller')], max_length=10, null=True),
        ),
    ]
