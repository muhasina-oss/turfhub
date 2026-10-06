from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from book_now.models import Booking
from book_now.serializers import BookingSerializer
from turf.models import TurfModel
# Create your views here.
class BookingListCreateView(APIView):
  
  def get(self,request):
    
    qs = Booking.objects.all()
    
    serializr_instance = BookingSerializer(qs,many=True)
    
    return Response(data=serializr_instance.data)
  
  def post(self,request):
    
    form_data = request.data
    
    serializr_instance = BookingSerializer(data=form_data)
    
    if serializr_instance.is_valid():
      
      cleaned_data = serializr_instance.validated_data
      
      Booking.objects.create(**cleaned_data)
      
      response_data = {"message":"booked"}
      
      return Response(data=response_data)
    
    else:
      
      return Response(data=serializr_instance.errors)
    
class BookingREtrieveUpdateDelete(APIView):
  
  def get(Self,request,pk=None):
    
    qs = Booking.objects.get(id=pk)
    
    serializer_instace = BookingSerializer(qs)
    
    return Response(data=serializer_instace.data)
  
  def put(self,request,pk=None):
    
    form_data = request.data
    
    serializer_instance = BookingSerializer(data=form_data)
    
    if serializer_instance.is_valid():
      
      cleaned_data = serializer_instance.validated_data
      
      Booking.objects.filter(id=pk).update(**cleaned_data)
      
      return Response(data={"message":"updated"})
    
    else:
     
     return Response(data=serializer_instance.errors)
   
  def delete(self,request,pk=None):
    
    Booking.objects.filter(id=pk).delete()
    
    return Response(data={"message":"deleted"})
     
  
  
    
