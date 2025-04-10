from django.db import models
from stadiums.models.stadium import Stadium
from utils.base_model import BaseModel

class Session(BaseModel):
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, related_name='sessions')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.stadium.name} ({self.start_time.strftime('%Y-%m-%d %H:%M')})"

