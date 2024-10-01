from django.db import models

CATEGORIES = ((0, 'Armour'), (1, 'Weapon'))

class EquipmentType(models.Model):
    name = models.CharField(max_length=255)
    category = models.IntegerField(choices=CATEGORIES, default=0)
    benefit_health = models.IntegerField()
    benefit_damage = models.IntegerField()
    distance_needed = models.IntegerField()
    equipment_svg = models.TextField()
    created_on = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} | health: +{self.benefit_health}, damage: +{self.benefit_damage}"