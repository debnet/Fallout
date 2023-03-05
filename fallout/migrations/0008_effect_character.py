# Generated by Django 3.0.2 on 2020-01-25 22:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fallout", "0007_character_extra_data"),
    ]

    operations = [
        migrations.AddField(
            model_name="effect",
            name="character",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="perks",
                to="fallout.Character",
                verbose_name="personnage",
            ),
        ),
    ]
