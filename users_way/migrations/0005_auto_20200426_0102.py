# Generated by Django 3.0.5 on 2020-04-25 22:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users_way', '0004_auto_20200426_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='synergyuser',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
    ]
