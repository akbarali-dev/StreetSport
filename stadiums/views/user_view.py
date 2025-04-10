from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from django.db.models import Subquery
from config.permissions import IsUser
from stadiums.models import Stadium,StadiumBooking
from stadiums.serializers import StadiumSerializerGet, StadiumBookingSerializer


@extend_schema(
        summary="stadionlar ro'yxatini ko'rish(USER)",
        description="Bron qilinmagan stadionlar ro'yxatini ko'rish(USER)",
    )
class ActiveStadiumsListView(ListAPIView):
    serializer_class = StadiumSerializerGet
    permission_classes = [IsAuthenticated, IsUser]

    def get_queryset(self):
        booked_ids = StadiumBooking.objects.filter(is_active=True).values_list('stadium_id', flat=True).distinct()
        return Stadium.objects.filter(is_confirmed=True).exclude(id__in=booked_ids)

@extend_schema(
        summary="stadionlar bron qilish(USER)",
        description="Bron qilish(USER)",
    )
class StadiumBookingCreateView(CreateAPIView):
    queryset = StadiumBooking.objects.all()
    serializer_class = StadiumBookingSerializer
    permission_classes = [IsAuthenticated, IsUser]