# Generated by Django 3.0.5 on 2020-12-18 14:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0003_auto_20201218_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='nascimento',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
