from rest_framework import serializers

from turf.models import TurfModel

class BookingSerializer(serializers.Serializer):
  
  team_name = serializers.CharField()
  
  phone = serializers.CharField()
  
  turf = serializers.PrimaryKeyRelatedField(
        queryset=TurfModel.objects.all()
    )
  
  booking_time = serializers.TimeField()
  
  booking_date = serializers.DateField()
  
  duration = serializers.DurationField()
  
  created_at =  serializers.DateTimeField(read_only=True)
  
  