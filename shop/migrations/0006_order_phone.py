# Generated by Django 3.0.6 on 2020-06-06 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200606_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='', max_length=50),
        ),
    ]