from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from myApp.models import CitizenDetails

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitizenDetails
        fields = ('FirstName', 
         'LastName', 
         'BirthDay', 
         'Address', 
         'City', 
         'ZipCode', 
         'LandLine', 
         'Phone', 
         'isInfected', 
         'Conditions'
        )