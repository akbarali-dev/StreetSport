from utils.base_model import BaseModel
from django.db import models
from .stadium import  Stadium
class Seat(BaseModel):
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, related_name='seats')
    row = models.CharField(max_length=5)  # o'rindiq qatorlari yoziladi
    number = models.IntegerField()
    price = models.IntegerField()


    def __str__(self):
        return f"{self.stadium.name} - Row {self.row}, Seat {self.number}"
