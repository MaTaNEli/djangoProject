from django.urls import path
from . import views

urlpatterns = [
    path('', views.getALL),
    path('savedata/', views.addData),
    path('city/', views.getByCity),
    path('dob/', views.getByDOB)
]