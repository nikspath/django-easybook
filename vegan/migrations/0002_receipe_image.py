# Generated by Django 4.2.1 on 2023-05-16 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipe',
            name='image',
            field=models.FileField(default='', upload_to='receipe'),
        ),
    ]
