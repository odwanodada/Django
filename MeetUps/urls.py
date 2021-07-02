from django.urls import path

from . import views

urlpatterns = [
    path('MeetUps/', views.index) #our-domain.com/MeetUps

]