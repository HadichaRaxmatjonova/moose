# Generated by Django 5.0.3 on 2024-03-10 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post',
            new_name='category',
        ),
    ]
