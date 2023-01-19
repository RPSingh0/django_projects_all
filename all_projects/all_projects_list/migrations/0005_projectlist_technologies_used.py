# Generated by Django 4.1.4 on 2023-01-04 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technologies', '0005_remove_technologieslist_known_by'),
        ('all_projects_list', '0004_projectlist_belongs_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectlist',
            name='technologies_used',
            field=models.ManyToManyField(to='technologies.technologieslist'),
        ),
    ]
