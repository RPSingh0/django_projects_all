# Generated by Django 4.1.4 on 2023-01-01 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0009_userprofile_tech_worked_with'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_image',
            field=models.ImageField(blank=True, null=True, upload_to='user_profile_images'),
        ),
    ]