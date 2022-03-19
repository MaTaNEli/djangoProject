from email import message
from wsgiref import validate
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from myApp.tests import checkInput
from myApp.models import CitizenDetails
from myApp.serializers import DepartmentSerializer
from django.core.exceptions import ValidationError


@api_view(['GET'])
def getALL(request):
    dep = CitizenDetails.objects.all()
    dep_ser = DepartmentSerializer(dep, many=True)
    return JsonResponse(dep_ser.data, safe = False)

@api_view(['GET'])
def getByCity(request):
    #citizens = CitizenDetails.objects.filter(BirthDay__range=["1997-01-01", "2011-01-31"])
    #http://127.0.0.1:8000/city/?city=tel%20aviv
    #http://127.0.0.1:8000/city/?city=jerusalem
    citizens = CitizenDetails.objects.filter(City=request.GET['city'])
    dep_ser = DepartmentSerializer(citizens, many=True)
    return JsonResponse(dep_ser.data, safe = False)

@api_view(['GET'])
def getByDOB(request):
    #http://127.0.0.1:8000/dob/?first=1992-11-18&second=2000-05-15
    citizens = CitizenDetails.objects.filter(BirthDay__range=[request.GET['first'], request.GET['second']])
    dep_ser = DepartmentSerializer(citizens, many=True)
    return JsonResponse(dep_ser.data, safe = False)

@api_view(['POST'])
def addData(request):

    data1 = JSONParser().parse(request)
    message = checkInput(data1)

    if message != "":
        JsonResponse.status_code = 400
        return JsonResponse({"message": message}, safe = False)
        
    serializer = DepartmentSerializer(data = data1)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({"message": "User signed in successfully"}, safe = False)
   
    JsonResponse.status_code = 400
    return JsonResponse({"message": "There seems to be a problem with the program Please fill in the details again"}, safe = False)

