# Generated by Django 5.0.6 on 2024-08-27 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.ImageField(default='/albimage/default.png', upload_to='albimage'),
        ),
    ]
