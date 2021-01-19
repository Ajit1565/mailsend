from django.urls import path, include
from django.contrib.auth import views
from app import views


urlpatterns = [
   path('mail-send/', views.send_mail, name="mail_send"),


]