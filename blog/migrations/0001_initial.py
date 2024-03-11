# Generated by Django 5.0.3 on 2024-03-10 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts/')),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('job_title', models.CharField(max_length=100)),
                ('author_image', models.ImageField(blank=True, null=True, upload_to='authors/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
