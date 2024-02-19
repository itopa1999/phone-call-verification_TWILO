from django.urls import path, include
from . import views


urlpatterns = [
    
    path('', views.index, name='index'),
    path('verify', views.verification_sent, name='verify'),
    
]
