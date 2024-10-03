# Generated by Django 4.2.16 on 2024-10-03 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("monster", "0005_monster_max_health"),
    ]

    operations = [
        migrations.AlterField(
            model_name="monster",
            name="type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="monsters",
                to="monster.monstertype",
            ),
        ),
    ]
