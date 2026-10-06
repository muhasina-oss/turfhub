from django.contrib.auth.models import User

from datetime import datetime

from rest_framework import serializers

from book_now_v2.models import Booking

class BookingSerializer(serializers.ModelSerializer):
  
  class Meta:
    
    model = Booking
    
    fields = "__all__"
    
    read_only_fields = ["end_time","created_at"]
    
  def validate(self,validated_data):
    
    booking_date = validated_data.get("booking_date")
    
    if booking_date < datetime.today().date():
      
      raise serializers.ValidationError("invalid date")
    
    else: 
      
      return validated_data

class SignUpSerializer(serializers.ModelSerializer):
  
  class Meta:
    
    model = User
    
    fields = ["username","email","password"]
    
    