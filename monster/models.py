from django.db import models
from cloudinary.models import CloudinaryField


class MonsterType(models.Model):
    name = models.CharField(max_length=255)
    base_max_health = models.IntegerField()
    base_damage = models.IntegerField()
    type_image = CloudinaryField('image')
    created_on = models.TimeField(auto_now_add=True)