from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from turf.serializers import UserSerializer,TurfSerializer
from turf.models import TurfModel
# Create your views here.
class AdminRegisterView(APIView):
  
  def post(self,request):
    
    form_data = request.data
    
    serializer_instance = UserSerializer(data=form_data)
    
    if serializer_instance.is_valid():
      
      cleaned_data = serializer_instance.validated_data
      
      User.objects.create_superuser(**cleaned_data)
      
      return Response(data=serializer_instance.validated_data)
    
    else:
      
      return Response(data=serializer_instance.errors)
    
class TurfListCreateView(APIView):
  
  authentication_classes = [authentication.BasicAuthentication]
  
  permission_classes = [permissions.IsAdminUser]
  
  def get(self,request):
    
    qs = TurfModel.objects.all()
    
    serializer_instance = TurfSerializer(qs,many=True)
    
    return Response(data=serializer_instance.data)
  
  def post(self,request):
    
    form_data = request.data
    
    serializer_instance = TurfSerializer(data=form_data)
    
    if serializer_instance.is_valid():
      
      cleaned_data = serializer_instance.validated_data
      
      TurfModel.objects.create(**cleaned_data)
      
      return Response(data=serializer_instance.validated_data)
    
    else:
      
      return Response(data=serializer_instance.errors)
      
class TurfRetrieveUpdataDeleteView(APIView):
  
  authentication_classes = [authentication.BasicAuthentication]
  
  permission_classes = [permissions.IsAdminUser]
  
  def get(self,request,pk=None):
    
    qs = TurfModel.objects.get(id=pk)
    
    serializer_instance = TurfSerializer(qs)
    
    return Response(data=serializer_instance.data)
  
  def put(self,request,pk=None):
    
    form_data = request.data
    
    serializer_instance = TurfSerializer(data=form_data)
    
    if serializer_instance.is_valid():
      
      cleaned_data = serializer_instance.validated_data
      
      TurfModel.objects.filter(id=pk).update(**cleaned_data)
      
      return Response(data=serializer_instance.validated_data)
    
    else:
      
      return Response(data=serializer_instance.errors)
      
  def delete(self,request,pk=None):
    
    TurfModel.objects.get(id=pk).delete()
    
    return Response(data={"message":"Turf deleted"})
      