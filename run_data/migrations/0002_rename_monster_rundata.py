# Generated by Django 4.2.16 on 2024-10-02 10:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("monster", "0005_monster_max_health"),
        ("equipment", "0004_rename_progress_equipment_progress"),
        ("run_data", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Monster",
            new_name="RunData",
        ),
    ]
