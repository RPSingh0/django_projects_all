# Generated by Django 4.1.4 on 2022-12-31 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technologies', '0005_remove_technologieslist_known_by'),
        ('user_profile', '0008_remove_userprofile_tech_worked_with'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='tech_worked_with',
            field=models.ManyToManyField(blank=True, to='technologies.technologieslist'),
        ),
    ]
