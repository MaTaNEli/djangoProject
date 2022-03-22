from django.urls import path
from . import views

# declear the rout and what function each of url will do
urlpatterns = [
    path('', views.getALL),
    path('savedata/', views.addData),
    path('city/', views.getByCity),
    path('dob/', views.getByDOB)
]