# Generated by Django 4.2 on 2023-04-26 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="test",
            name="cantidad",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
