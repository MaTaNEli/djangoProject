from django.urls import path
from . import views

urlpatterns = [
    path('', views.data),
    path('savedata/', views.addData)
]