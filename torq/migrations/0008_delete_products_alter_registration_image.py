# Generated by Django 5.1.1 on 2024-10-06 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torq', '0007_products_registration_company'),
    ]

    operations = [
        migrations.DeleteModel(
            name='products',
        ),
        migrations.AlterField(
            model_name='registration',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='user/'),
        ),
    ]
