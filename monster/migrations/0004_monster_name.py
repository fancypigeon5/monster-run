# Generated by Django 4.2.16 on 2024-09-27 10:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("monster", "0003_monster"),
    ]

    operations = [
        migrations.AddField(
            model_name="monster",
            name="name",
            field=models.CharField(default="name", max_length=200),
            preserve_default=False,
        ),
    ]
