from django.db import models

# Create your models of the DB table.
class CitizenDetails(models.Model):
    Id = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    BirthDay = models.DateField()
    Address = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    ZipCode = models.IntegerField()
    LandLine = models.CharField(max_length=100)
    Phone = models.IntegerField()
    isInfected = models.BooleanField()
    Conditions = models.CharField(max_length=100, blank=True)