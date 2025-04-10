from django.db import models
from django.conf import settings
from utils.base_model import BaseModel
from .stadium import Stadium

class StadiumManager(BaseModel):
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, related_name='managers')
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.manager.username} -> {self.stadium.name}"

