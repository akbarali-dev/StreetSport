from django.db import models
from django.conf import settings
from utils.base_model import BaseModel

class Stadium(BaseModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='stadiums')
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    is_confirmed = models.BooleanField(default=False)
    price = models.IntegerField()

    def __str__(self):
        return self.name


