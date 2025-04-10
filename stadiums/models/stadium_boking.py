from django.db import models
from django.conf import settings

from stadiums.models import Stadium
from utils.base_model import BaseModel

class StadiumBooking(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    price = models.IntegerField()
    is_paid = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.stadium.name


