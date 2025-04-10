from bookings.models.session import Session
from stadiums.models.seat import Seat
from django.db import models

from users.models import CustomUser
from utils.base_model import BaseModel
class SeatBooking(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.seat}"
