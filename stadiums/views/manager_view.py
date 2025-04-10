from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from ..models import StadiumManager
from ..serializers import StadiumManagerSerializer
from config.permissions import IsOwnerUser
from drf_spectacular.utils import extend_schema

@extend_schema(
        summary="Manager biriktirish",
        description="Faqat 'owner'lar 'manager' biriktirish mumkin",
)
class StadiumAddManagerView(CreateAPIView):
    serializer_class = StadiumManagerSerializer
    queryset = StadiumManager.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerUser]






