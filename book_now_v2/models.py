from django.db import models

from turf.models import TurfModel

class Booking(models.Model):
  
  team_name = models.CharField(max_length=200)
  
  phone = models.CharField(max_length=200)
  
  turf = models.ForeignKey(TurfModel,on_delete=models.CASCADE,related_name="bookings_v2")
  
  booking_date = models.DateField()
  
  booking_time = models.TimeField()
  
  duration = models.DurationField() 
  
  end_time = models.TimeField()
  
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    
    return self.team_name