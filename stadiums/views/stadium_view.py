from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models import Stadium, StadiumBooking
from ..serializers import StadiumSerializer, StadiumSerializerGet, StadiumUpdateSerializer, StadiumBookingListSerializer
from config.permissions import IsOwnerUser, IsAdminUser,  IsManagerUser
from drf_spectacular.utils import extend_schema

@extend_schema(
        summary="Stadion qo‘shish(owner)",
        description="Faqat 'owner' roliga ega foydalanuvchilar stadion qo‘shishi mumkin.",
    )
class StadiumCreateView(CreateAPIView):
    serializer_class = StadiumSerializer
    queryset = Stadium.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerUser]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

@extend_schema(
        summary="Bron qilingan stadionlar (owner)",
        description="Faqat 'owner' roliga ega foydalanuvchilar Bron qilingan stadionlarni kuzatadi.",
    )
class BookingsListView(ListAPIView):
    serializer_class = StadiumBookingListSerializer
    permission_classes = [IsAuthenticated, IsOwnerUser]

    def get_queryset(self):
        return StadiumBooking.objects.filter(stadium__owner=self.request.user).order_by('-created_at')

@extend_schema(
        summary="O'ziga tegishli stadionlar(ower)",
        description="Faqat o'ziga tegishli stadionlarni ko'rishi mumkin(Owner)",
    )
class MyStadiumsListView(ListAPIView):
    serializer_class = StadiumSerializerGet
    permission_classes = [IsAuthenticated, IsOwnerUser]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'owner':
            return Stadium.objects.filter(owner=user)
        return Stadium.objects.none()

@extend_schema(
        summary="Stadionni tasdiqlash(admin)",
        description="Adminlar stadionlarni tasdiqlaydi(admin)",
    )
class StadiumConfirmView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request, stadium_id):

        try:
            stadium = Stadium.objects.get(id=stadium_id)
        except Stadium.DoesNotExist:
            return Response({"detail": "Stadion topilmadi."}, status=404)

        if stadium.is_confirmed:
            return Response({"detail": "Stadion allaqachon tasdiqlangan."}, status=400)

        stadium.is_confirmed = True
        stadium.save()

        return Response({"detail": f"{stadium.name} stadion tasdiqlandi."}, status=200)

@extend_schema(
        summary="O'zgartirish(admin)",
        description="Adminlar stadionlarni o'zgartirish(admin)",
    )
class AdminStadiumEditView(UpdateAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumUpdateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    def perform_update(self, serializer):
        serializer.save()

@extend_schema(
        summary="O'chirish(admin)",
        description="Adminlar stadionlarni o'chiradi(admin)",
    )
class AdminStadiumDeleteView(DestroyAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumUpdateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

@extend_schema(
        summary="Stadion soni",
        description="Adminlar stadionlarni sonini ko'radi(admin)",
    )
class StadiumCountViewSet(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]


    def get(self, request):
        confirmed_count = Stadium.objects.filter(is_confirmed=True).count()
        dont_confirmed_count = Stadium.objects.filter(is_confirmed=False).count()
        return Response({
            "stadium_confirmed_count": confirmed_count,
            "stadium_dont_confirmed_count": dont_confirmed_count,
        })



class ConfirmPaymentByManagerView(APIView):
    permission_classes = [IsAuthenticated, IsManagerUser]

    def post(self, request, booking_id):
        try:
            booking = StadiumBooking.objects.get(id=booking_id)
        except StadiumBooking.DoesNotExist:
            return Response({"detail": "Bron topilmadi."}, status=404)

        if booking.is_paid:
            return Response({"detail": "Bu bron allaqachon to‘langan."}, status=400)

        booking.is_paid = True
        booking.save()

        return Response({"detail": "To‘lov tasdiqlandi."}, status=200)



