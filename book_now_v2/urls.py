from django.urls import path

from book_now_v2.views import SignUpView,BookingListCreateiew

urlpatterns = [
    
    path("signup/",SignUpView.as_view()),
    
    path('bookings/',BookingListCreateiew.as_view()),
    
]
