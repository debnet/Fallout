# Generated by Django 2.1.7 on 2019-03-31 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fallout', '0002_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='secondary',
            field=models.BooleanField(default=False, verbose_name='secondaire'),
        ),
    ]
