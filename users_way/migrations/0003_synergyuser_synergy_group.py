# Generated by Django 3.0.5 on 2020-04-18 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_way', '0002_synergygroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='synergyuser',
            name='synergy_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users_way.SynergyGroup', verbose_name='user_group'),
        ),
    ]
