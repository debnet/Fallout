# Generated by Django 3.0.4 on 2020-04-07 23:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fallout", "0009_random_modifiers"),
    ]

    operations = [
        migrations.AddField(
            model_name="damagehistory",
            name="damage_rate",
            field=models.FloatField(default=0.0, verbose_name="taux de dégâts"),
        ),
        migrations.AddField(
            model_name="damagehistory",
            name="source",
            field=models.CharField(blank=True, max_length=200, verbose_name="source"),
        ),
    ]
