# Generated by Django 4.1.4 on 2022-12-28 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_userprofile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='github_url',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
