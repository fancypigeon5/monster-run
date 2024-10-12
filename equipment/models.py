from django.db import models
from monster.models import Monster
from django.contrib.auth.models import User

CATEGORIES = ((0, 'Armour'), (1, 'Weapon'))


class EquipmentType(models.Model):
    """
    Model representing different types of equipment in the game.
    Methods:
        __str__(): Returns a string representation of the equipment, including its name, health benefit, and damage benefit.
    """

    name = models.CharField(max_length=255)
    category = models.IntegerField(choices=CATEGORIES, default=0)
    benefit_health = models.IntegerField(default=0)
    benefit_damage = models.IntegerField(default=0)
    distance_needed = models.IntegerField()
    equipment_svg = models.TextField()
    created_on = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} | health: +{self.benefit_health}, damage: +{self.benefit_damage}"


class Equipment(models.Model):
    """
    Equipment model representing an item that can be owned by a user and optionally equipped to a monster.
    Methods:
        __str__: Returns a string representation of the equipment, indicating the owner and whether it is equipped to a monster.
    """
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="equipments")
    type = models.ForeignKey(
        EquipmentType, on_delete=models.CASCADE, related_name='equipments')
    unlocked = models.BooleanField(default=False)
    progress = models.IntegerField(default=0)
    monster = models.ForeignKey(Monster, on_delete=models.SET_NULL,
                                blank=True, null=True, default=None, related_name='equipped')
    created_on = models.TimeField(auto_now_add=True)

    def __str__(self):
        if self.monster:
            displaystring = f"{self.owner.username}'s {self.type.name} equipped to {self.monster.name}"
        else:
            displaystring = f"{self.owner.username}'s {self.type.name} not equipped"
        return displaystring
