from datetime import datetime,timedelta,time
from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers

from book_now_v2.serializers import SignUpSerializer,BookingSerializer
from book_now_v2.models import Booking

# Create your views here.


class SignUpView(APIView):
  
  def post(self,request):
    
    form_data = request.data
    
    serializer_instance = SignUpSerializer(data=form_data)
    
    if serializer_instance.is_valid():
      
      cleaned_data = serializer_instance.validated_data
      
      user_object = User.objects.create_user(**cleaned_data)
      
      serializer_instance = SignUpSerializer(user_object)
      
      return Response(data=serializer_instance.data)
    
    else:
      
      return Response(data=serializer_instance.errors)
    
class BookingListCreateiew(APIView):
  
  def get(Self,requset):
    
    qs = Booking.objects.all()
    
    serializer_instance = BookingSerializer(qs,many=True)
    
    return Response(data=serializer_instance.data)
  
  def post(self,request):
    
    form_data = request.data
    
    serializer_instance = BookingSerializer(data=form_data)
    
    if serializer_instance.is_valid():
      
      cleaned_data = serializer_instance.validated_data
      
      booking_date = cleaned_data.get("booking_date")
         
      booking_time = cleaned_data.get("booking_time")
      
      duration = cleaned_data.get("duration")
      
      end_date_time = datetime.combine(booking_date,booking_time)+duration
      
      end_time = end_date_time.time()
      
      turf = cleaned_data.get("turf")
      
      booking_objects = Booking.objects.filter(turf=turf,booking_date=booking_date)
      
      for i in booking_objects:
        
        if booking_time < i.end_time and end_time > i.booking_time:
          
          return Response({"message":"no available booking slot in the selected time duration"})
      
      qs = Booking.objects.create(**cleaned_data,end_time=end_time)
      
      serializer_instance = BookingSerializer(qs)
      
      return Response(data=serializer_instance.data)
    
    else:
       
      return Response(data=serializer_instance.errors)
      
            
      
      
       