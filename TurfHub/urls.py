"""
URL configuration for TurfHub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from turf import views
from turf.views import TurfListCreateView,TurfRetrieveUpdataDeleteView
from book_now.views import BookingListCreateView,BookingREtrieveUpdateDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-register/',views.AdminRegisterView.as_view()),
    
    path('turfs/',TurfListCreateView.as_view()),
    path('turfs/<int:pk>/',TurfRetrieveUpdataDeleteView.as_view()),
    
    path('bookings/',BookingListCreateView.as_view()),
    path('bookings/<int:pk>/',BookingREtrieveUpdateDelete.as_view()),
    
    #bbok_now_v2 app route
    path("v2/book_now/",include("book_now_v2.urls")),
    
]
