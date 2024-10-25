# Generated by Django 5.1.1 on 2024-10-24 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrmApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='photo',
            field=models.FileField(help_text='students id card image', null=True, upload_to='media/'),
        ),
    ]
