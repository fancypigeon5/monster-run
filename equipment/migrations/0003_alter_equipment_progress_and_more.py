# Generated by Django 4.2.16 on 2024-10-01 11:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("equipment", "0002_equipment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="equipment",
            name="Progress",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="equipmenttype",
            name="benefit_damage",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="equipmenttype",
            name="benefit_health",
            field=models.IntegerField(default=0),
        ),
    ]
