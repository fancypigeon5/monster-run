from colorfield.fields import ColorField
from django.db import models
from django.contrib.auth.models import User


class MonsterType(models.Model):
    """
    MonsterType is a Django model that represents different types of monsters in the game.
    Methods:
        __str__(): Returns a string representation of the monster type, including its name, base health, and base damage.
    """

    name = models.CharField(max_length=255)
    base_max_health = models.IntegerField()
    base_damage = models.IntegerField()
    type_svg = models.TextField()
    created_on = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} | health: {self.base_max_health}, damage: {self.base_damage}"


class ExcludeEnemyMonsters(models.Manager):
    """
    Custom manager to exclude monsters with the name 'Enemy' from the queryset.
    Methods: 
        get_queryset(): Returns a queryset excluding monsters with the name 'Enemy'.
    """

    def get_queryset(self):
        return super().get_queryset().exclude(name='Enemy')


class Monster(models.Model):
    """
    Monster model representing a monster entity in the game.
    Managers:
        objects (ExcludeEnemyMonsters): Custom manager to exclude enemy monsters.
        all_objects (models.Manager): Default manager for all monster objects.
    Methods:
        __str__: Returns a string representation of the monster.
    """

    name = models.CharField(max_length=200)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="monsters")
    type = models.ForeignKey(
        MonsterType, on_delete=models.CASCADE, related_name="monsters")
    color = ColorField(default='#f60000')
    health = models.IntegerField()
    max_health = models.IntegerField()
    damage = models.IntegerField()
    score = models.IntegerField(default=0)
    created_on = models.TimeField(auto_now_add=True)

    objects = ExcludeEnemyMonsters()
    all_objects = models.Manager()

    def __str__(self):
        return f"{self.name} from {self.owner}"
