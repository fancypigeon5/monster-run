from django.db import models
from django.contrib.auth.models import User
from monster.models import Monster
from equipment.models import Equipment


class RunData(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="runs")
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE,
                                  blank=True, null=True, default=None, related_name="unlock_runs")
    monster = models.ForeignKey(Monster, on_delete=models.CASCADE,
                                blank=True, null=True, default=None, related_name="recover_runs")
    distance = models.IntegerField()
    pace = models.DurationField(blank=True, null=True)
    created_on = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.distance}Km run on {self.created_on}"
