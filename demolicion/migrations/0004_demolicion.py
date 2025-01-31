# Generated by Django 5.0.3 on 2024-03-04 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demolicion', '0003_rename_demolicion_demolition'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demolicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='demolicion/images')),
                ('video', models.FileField(blank=True, null=True, upload_to='demolicion/video/%Y')),
            ],
        ),
    ]
