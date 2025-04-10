from rest_framework import serializers
from .models import Stadium, StadiumManager, StadiumBooking


class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = ['name', 'location', 'price']

class StadiumUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = ['id','name', 'location', 'price',]

class StadiumSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = ['name', 'location', 'id', 'is_confirmed', 'price']

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StadiumManager
        fields = ['stadium', 'manager']


class StadiumManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StadiumManager
        fields = ['id', 'stadium', 'manager']

    def validate(self, data):
        request = self.context['request']
        stadium = data['stadium']
        manager = data['manager']

        if stadium.owner != request.user:
            raise serializers.ValidationError("Siz faqat o'zingizning stadionlaringizga manager biriktira olasiz.")

        if manager.role != 'manager':
            raise serializers.ValidationError("Faqat manager roliga ega foydalanuvchini biriktira olasiz.")

        return data


class StadiumBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = StadiumBooking
        fields = ['id', 'stadium', 'price', 'is_paid']

        read_only_fields = ['price', 'is_paid']

    def validate_stadium(self, value):
        if not value.is_confirmed:
            raise serializers.ValidationError("Bu stadion hali tasdiqlanmagan.")
        return value

    def create(self, validated_data):
        user = self.context['request'].user
        stadium = validated_data['stadium']
        price = stadium.price

        booking = StadiumBooking.objects.create(
            user=user,
            stadium=stadium,
            price=price
        )
        return booking

class StadiumBookingListSerializer(serializers.ModelSerializer):
    stadium_name = serializers.CharField(source='stadium.name', read_only=True)
    stadium_location = serializers.CharField(source='stadium.location', read_only=True)

    class Meta:
        model = StadiumBooking
        fields = ['id', 'stadium', 'stadium_name', 'stadium_location', 'price', 'is_paid', 'created_at']
