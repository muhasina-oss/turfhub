from django.db import models

from turf.models import TurfModel

# Create your models here.

class Booking(models.Model):
  
  team_name = models.CharField(max_length=200)
  
  phone = models.CharField(max_length=200)
  
  turf = models.ForeignKey(TurfModel,on_delete=models.CASCADE)
  
  booking_date = models.DateField()
  
  booking_time = models.TimeField()
  
  duration = models.DurationField() 
  
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    
    return self.team_name