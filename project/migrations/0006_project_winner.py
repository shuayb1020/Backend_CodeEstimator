# Generated by Django 4.2 on 2023-06-25 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_alter_project_owned_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='winner',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]