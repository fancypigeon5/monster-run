from django.db import models
from django.contrib.auth.models import User


class MonsterType(models.Model):
    name = models.CharField(max_length=255)
    base_max_health = models.IntegerField()
    base_damage = models.IntegerField()
    type_svg = models.TextField()
    created_on = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} | health: {self.base_max_health}, damage: {self.base_damage}"

class ExcludeEnemyMonsters(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(name='Enemy')

class Monster(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="monsters")
    type = models.ForeignKey(MonsterType, on_delete=models.CASCADE, related_name="monsters")
    color = models.CharField(max_length=7, default='#f60000')
    health = models.IntegerField()
    max_health = models.IntegerField()
    damage = models.IntegerField()
    created_on = models.TimeField(auto_now_add=True)
    
    objects = ExcludeEnemyMonsters()
    all_objects = models.Manager()

    def __str__(self):
        return f"{self.name} from {self.owner}"