# Generated by Django 4.2 on 2023-05-06 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='code1',
            field=models.FileField(default=0, upload_to='code-file'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='code2',
            field=models.FileField(default=0, upload_to='code-file'),
            preserve_default=False,
        ),
    ]
